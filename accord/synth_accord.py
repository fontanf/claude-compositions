"""Rendu audio de « Accord » : corde pincée (Karplus-Strong) avec modes de jeu et couleur propre à chaque corde.

- la même note sonne plus sombre sur une corde grave (case haute) que sur la chanterelle ;
- sul ponticello : attaque près du chevalet (brillant, nasal) ; sul tasto : sur la touche (rond) ;
- pizz. : corde étouffée ; tambora : accord frappé, avec le choc sur le chevalet ; golpe : frappe sur la table ;
- mesures « anneau » : chaque note résonne jusqu'à ce que sa corde soit rejouée.
"""
import sys
from collections import defaultdict

import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt, lfilter

import accord_tools as t
from accord_data import NBARS, METER, TEMPO, MODE

SR = 44100
rng = np.random.default_rng(5)
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
    for _ in range(int(5 * (1 - bright)) + 1):
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
    env = np.exp(-6.91 * tt / 3.5) * np.minimum(1, tt / 0.004)
    return env * (np.sin(2 * np.pi * freq * tt) + 0.06 * np.sin(4 * np.pi * freq * tt))


def thump(dur=0.25, f0=95):
    """choc sur la table : bruit grave et mode de caisse amorti"""
    n = int(dur * SR)
    tt = np.arange(n) / SR
    noise = sosfilt(butter(2, 900, "lowpass", fs=SR, output="sos"), rng.normal(0, 1, n))
    return (0.6 * noise * np.exp(-tt / 0.02) + np.sin(2 * np.pi * f0 * tt) * np.exp(-tt / 0.09))


def color(sig, bright):
    """couleur continue : passe-bas d'ordre 2 dont la coupure suit la brillance (corde, case, mode de jeu)"""
    fc = 600 + 7500 * bright ** 2
    return sosfilt(butter(2, min(fc, SR / 2.5), "lowpass", fs=SR, output="sos"), sig)


def string_color(bright, string, fret):
    """corde grave et case haute : son plus sombre (corde filée, longueur vibrante plus courte)"""
    return bright * (0.45 + 0.11 * string) * (1 - 0.025 * fret)


TIMBRE = {  # (brillance, position de l'attaque)
    "ord": (0.55, 0.17), "pont": (1.0, 0.05), "tasto": (0.15, 0.42), "pizz": (0.35, 0.2), "tamb": (0.25, 0.3),
}


def render(path):
    notes = t.all_notes()
    _, strings = t.check(notes=notes)
    onsets = defaultdict(list)
    for n in notes:
        for k in range(len(n["pitches"])):
            sf = strings.get((id(n), k))
            if sf:
                onsets[sf[0]].append(to_sec(n["start"]))
    for s in onsets:
        onsets[s].sort()

    buf = np.zeros(int((END + 10) * SR))

    def add(sig, t0, lvl):
        i = max(0, int(t0 * SR))
        buf[i : i + len(sig)] += lvl * sig[: len(buf) - i]

    for n in notes:
        b = n["bar"]
        s0 = to_sec(n["start"])
        notated_end = to_sec(n["start"] + n["dur"])
        lvl = n["level"] ** 1.3 * (1.3 if n["accent"] else 1.0)
        if n["muted"]:  # golpe
            add(thump(), s0, 1.4 * lvl)
            continue
        if n["timbre"] == "tamb":
            add(thump(0.15, 140), s0, 0.8 * lvl)
        order = sorted(range(len(n["pitches"])), key=lambda k: n["pitches"][k])
        for rank, k in enumerate(order):
            p = n["pitches"][k]
            freq = 440 * 2 ** ((p - 69) / 12)
            string, fret = strings.get((id(n), k), (5, 0))
            if n["harmonic"]:
                add(harmonic_tone(freq, 4.5), s0, 0.32 * lvl)
                continue
            nxt = [x for x in onsets.get(string, []) if x > s0 + 1e-4]
            if MODE[b] == "anneau":
                end = min(nxt[0] if nxt else s0 + 5, s0 + 5)
            elif n["timbre"] == "pizz":
                end = s0 + 0.12
            else:
                end = min(notated_end + 0.1, nxt[0] if nxt else notated_end + 0.1)
            if b == NBARS - 1:  # le dernier mi s'éteint de lui-même
                end = s0 + 6
            bright, pick = TIMBRE[n["timbre"]]
            # couleur de la corde : plus sombre sur une corde grave et en position haute
            bright = max(0.05, string_color(bright, string, fret))
            t60 = 0.12 if n["timbre"] == "pizz" else 3.0 * (110 / freq) ** 0.5 * (0.8 + 0.04 * string)
            t0 = s0 + (rank * (0.008 if n["timbre"] == "tamb" else 0.014) if n["strum"] or n["timbre"] == "tamb" else 0)
            dur = max(end - t0, 0.08)
            bright = min(1.0, bright + 0.15 * lvl)
            sig = karplus(freq * 2 ** (rng.normal(0, 1.5) / 1200), dur + 0.05, bright, t60, pick)
            sig = color(sig, bright)
            nr = int(0.05 * SR)
            sig[-nr:] *= np.linspace(1, 0, nr) ** 2
            add(sig, t0, lvl * (0.8 if n["timbre"] == "tamb" else 1.0))

    for f0, gdb, q in [(100, 4, 1.4), (210, 3, 1.2), (2800, -3, 0.8), (4500, -4, 0.7)]:
        A = 10 ** (gdb / 40)
        w = 2 * np.pi * f0 / SR
        alpha = np.sin(w) / (2 * q)
        bb = np.array([1 + alpha * A, -2 * np.cos(w), 1 - alpha * A])
        aa = np.array([1 + alpha / A, -2 * np.cos(w), 1 - alpha / A])
        buf = lfilter(bb / aa[0], aa / aa[0], buf)
    mix = np.stack([buf, buf], axis=1)
    n_ir = int(2.4 * SR)
    tt = np.arange(n_ir) / SR
    irs = []
    for _ in range(2):
        x = rng.normal(0, 1, n_ir) * np.exp(-6.91 * tt / 1.9)
        x = sosfilt(butter(1, 4000, "lowpass", fs=SR, output="sos"), x)
        x[: int(0.012 * SR)] = 0
        irs.append(x / np.sqrt(np.sum(x**2)))
    wet = np.stack([fftconvolve(mix[:, c], irs[c])[: len(mix)] for c in range(2)], axis=1)
    out = 0.82 * mix + 0.34 * wet
    out = sosfilt(butter(2, 45, "highpass", fs=SR, output="sos"), out, axis=0)
    last = np.nonzero(np.abs(out).max(axis=1) > 1e-3 * np.abs(out).max())[0][-1]
    out = out[: last + 1]
    out /= np.max(np.abs(out)) / 0.89
    fade = int(1.0 * SR)
    out[-fade:] *= np.linspace(1, 0, fade)[:, None]
    wavfile.write(path, SR, (out * 32767).astype(np.int16))
    print(f"{path}: {len(out) / SR:.1f} s")


if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "accord.wav")
