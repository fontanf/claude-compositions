"""Rendu audio de « Fontaine » : guitare classique seule, modèle de corde pincée (Karplus-Strong).

Chaque note est attribuée à une corde par le vérificateur de doigté ; elle sonne jusqu'à ce que la
même corde soit rejouée, ou que la main gauche quitte la position (cordes frettées).
"""
import sys
from collections import defaultdict

import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt, lfilter

import fontaine_tools as t
from fontaine_data import NBARS, METER, TEMPO, MODE

SR = 44100
rng = np.random.default_rng(11)

STARTS, _ = t.bar_starts()
BAR_SEC, acc = {}, 0.0
for b in range(1, NBARS + 1):
    BAR_SEC[b] = acc
    acc += float(METER[b][0]) * 4 * 60 / TEMPO[b]
END = acc


def to_sec(x):
    x = float(x)
    for b in range(NBARS, 0, -1):
        if x >= float(STARTS[b]) - 1e-9:
            return BAR_SEC[b] + (x - float(STARTS[b])) * 4 * 60 / TEMPO[b]
    return 0.0


def karplus(freq, dur, bright, t60, pick):
    n = int(dur * SR)
    D = SR / freq - 0.5
    N = int(D)
    fr = D - N
    c0, c1, c2 = 0.5 * (1 - fr), 0.5, 0.5 * fr
    g = 10 ** (-3 / (freq * t60))
    exc = rng.uniform(-1, 1, N + 2)
    for _ in range(int(4 * (1 - bright)) + 1):
        exc = 0.5 * (exc + np.roll(exc, 1))
    exc -= np.roll(exc, max(1, int(pick * N)))
    exc -= exc.mean()
    y = np.zeros(n + N + 2)
    y[: N + 2] = exc
    i = N + 2
    while i < len(y):
        j = min(i + N, len(y))
        k = j - i
        y[i:j] = g * (c0 * y[i - N : i - N + k] + c1 * y[i - N - 1 : i - N - 1 + k] + c2 * y[i - N - 2 : i - N - 2 + k])
        i = j
    return y[:n] / (np.abs(exc).max() + 1e-9)


def harmonic_tone(freq, dur):
    n = int(dur * SR)
    tt = np.arange(n) / SR
    env = np.exp(-6.91 * tt / 3.0) * np.minimum(1, tt / 0.004)
    return env * (np.sin(2 * np.pi * freq * tt) + 0.08 * np.sin(4 * np.pi * freq * tt))


def render(path):
    notes = t.all_notes()
    _, strings = t.check(notes=notes)
    # attaques par corde, pour savoir quand une corde est rejouée
    onsets = defaultdict(list)
    events = []
    for n in notes:
        s0 = to_sec(n["start"])
        for k, p in enumerate(sorted(n["pitches"])):
            sf = strings.get((id(n), p))
            if n["harmonic"] or sf is None:
                sf = (None, 0)
            events.append((s0, n, p, sf, k))
            if sf[0] is not None:
                onsets[sf[0]].append(s0)
    for s in onsets:
        onsets[s].sort()

    buf = np.zeros(int((END + 8) * SR))
    for s0, n, p, (string, fret), k in events:
        b = n["bar"]
        freq = 440 * 2 ** ((p - 69) / 12)
        notated_end = to_sec(n["start"] + n["dur"])
        # fin de résonance
        nxt = [x for x in onsets.get(string, []) if x > s0 + 1e-4]
        end = nxt[0] if nxt else s0 + 4.0
        if fret > 0 and MODE[b] == "forme":
            window_end = to_sec(STARTS[b] + (n["pos"] // (t.F(3, 8)) + 1) * t.F(3, 8))
            end = min(end, max(notated_end, window_end) + 0.08)
        elif fret > 0 or n["voice"] == 1:
            end = min(end, notated_end + 0.06)
        if b == NBARS:
            end = s0 + 6.0
        end = min(end, s0 + 4.0) if b != NBARS else end
        # niveau
        lvl = n["level"] ** 1.3 * (1.3 if n["accent"] else 1.0)
        if 25 <= b <= 30:
            lvl *= 1.25 if n["voice"] == 2 else 0.7     # la mélodie au pouce
        elif MODE[b] == "forme" or b >= 51:
            lvl *= 1.15 if n["voice"] == 1 else 0.75    # faire chanter la mélodie
        if n["slurred"]:
            lvl *= 0.6                                    # lié : pas de nouvelle attaque
        # attaque
        t0 = max(0.0, s0 + (k * 0.016 if n["strum"] else 0.0) + rng.normal(0, 0.002))
        dur = max(end - t0, 0.05)
        if n["harmonic"]:
            sig = 0.3 * harmonic_tone(freq, max(dur, 2.5))
        else:
            bright = 0.35 if n["slurred"] else min(1.0, 0.45 + 0.35 * lvl)
            sig = karplus(freq, dur + 0.05, bright, 3.2 * (110 / freq) ** 0.5, 0.17 if n["voice"] == 1 else 0.22)
            nr = int(0.05 * SR)
            sig[-nr:] *= np.linspace(1, 0, nr) ** 2
        i = int(t0 * SR)
        buf[i : i + len(sig)] += lvl * sig

    for f0, gdb, q in [(100, 4, 1.4), (210, 3, 1.2), (2800, -3, 0.8), (4500, -4, 0.7)]:
        A = 10 ** (gdb / 40)
        w = 2 * np.pi * f0 / SR
        alpha = np.sin(w) / (2 * q)
        bb = np.array([1 + alpha * A, -2 * np.cos(w), 1 - alpha * A])
        aa = np.array([1 + alpha / A, -2 * np.cos(w), 1 - alpha / A])
        buf = lfilter(bb / aa[0], aa / aa[0], buf)
    mix = np.stack([buf, buf], axis=1)
    n_ir = int(2.0 * SR)
    tt = np.arange(n_ir) / SR
    irs = []
    for _ in range(2):
        x = rng.normal(0, 1, n_ir) * np.exp(-6.91 * tt / 1.5)
        x = sosfilt(butter(1, 4000, "lowpass", fs=SR, output="sos"), x)
        x[: int(0.012 * SR)] = 0
        irs.append(x / np.sqrt(np.sum(x**2)))
    wet = np.stack([fftconvolve(mix[:, c], irs[c])[: len(mix)] for c in range(2)], axis=1)
    out = 0.85 * mix + 0.3 * wet
    out = sosfilt(butter(2, 50, "highpass", fs=SR, output="sos"), out, axis=0)
    last = np.nonzero(np.abs(out).max(axis=1) > 1e-3 * np.abs(out).max())[0][-1]
    out = out[: last + 1]
    out /= np.max(np.abs(out)) / 0.89
    fade = int(1.0 * SR)
    out[-fade:] *= np.linspace(1, 0, fade)[:, None]
    wavfile.write(path, SR, (out * 32767).astype(np.int16))
    print(f"{path}: {len(out) / SR:.1f} s")


if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "fontaine.wav")
