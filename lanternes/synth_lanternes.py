"""Rendu audio de « Lanternes » : cordes pincées (Karplus-Strong), trémolo, pupitres, réverbération."""
import sys

import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt, lfilter

from lanternes_data import NBARS, METER, TEMPO, PARTS
from lanternes_tools import parse_voice, bar_starts

SR = 44100
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- temps
STARTS, TOTAL = bar_starts()
BAR_SEC = {}
acc = 0.0
for b in range(1, NBARS + 1):
    BAR_SEC[b] = acc
    acc += float(METER[b][0]) * 4 * 60 / TEMPO[b]


def to_sec(t):
    t = float(t)
    for b in range(NBARS, 0, -1):
        if t >= float(STARTS[b]) - 1e-9:
            return BAR_SEC[b] + (t - float(STARTS[b])) * 4 * 60 / TEMPO[b]
    return 0.0


def bar_of(t):
    return max(b for b in range(1, NBARS + 1) if float(STARTS[b]) <= float(t) + 1e-9)


# ---------------------------------------------------------------- corde
def karplus(freq, dur, bright, t60, pick):
    n = int(dur * SR)
    D = SR / freq - 0.5
    N = int(D)
    fr = D - N
    c0, c1, c2 = 0.5 * (1 - fr), 0.5, 0.5 * fr
    g = 10 ** (-3 / (freq * t60))
    exc = rng.uniform(-1, 1, N + 2)
    for _ in range(int(3 * (1 - bright)) + 1):  # attaque plus ou moins brillante
        exc = 0.5 * (exc + np.roll(exc, 1))
    exc -= np.roll(exc, max(1, int(pick * N)))  # position du plectre
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


INSTR = {
    #            pupitre  cordes doublées  t60(f)                          brillance  plectre
    "mandoline": dict(players=3, course=True, t60=lambda f: 1.3 * (440 / f) ** 0.6, bright=0.9, pick=0.13, gain=2.2),
    "mandole": dict(players=2, course=True, t60=lambda f: 1.8 * (330 / f) ** 0.6, bright=0.8, pick=0.15, gain=2.1),
    "guitare": dict(players=2, course=False, t60=lambda f: 3.2 * (110 / f) ** 0.5, bright=0.55, pick=0.2, gain=0.5),
}


def pluck(buf, t0, freq, dur, level, cfg, release):
    i0 = int(t0 * SR)
    if i0 < 0:
        return
    strings = [(-1.5, 0.0), (1.5, 0.002)] if cfg["course"] else [(0.0, 0.0)]
    tail = dur + release
    for cents, delay in strings:
        f = freq * 2 ** (cents / 1200)
        s = karplus(f, tail, min(1.0, cfg["bright"] * (0.6 + 0.5 * level)), cfg["t60"](f), cfg["pick"])
        nr = int(release * SR)
        if nr:
            s[-nr:] *= np.linspace(1, 0, nr) ** 2  # étouffement
        j = i0 + int(delay * SR)
        buf[j : j + len(s)] += level * s / len(strings)


def render_part(music, kind):
    cfg = INSTR[kind]
    buf = np.zeros(int((BAR_SEC[NBARS] + 12) * SR))
    for n in parse_voice(music):
        s0, s1 = to_sec(n["start"]), to_sec(n["start"] + n["dur"])
        if n["bar"] == NBARS:
            s1 += 2.5  # point d'orgue final
        lvl = n["level"] ** 1.3 * (1.3 if n["accent"] else 1.0)
        pitches = sorted(n["pitches"])
        for player in range(cfg["players"]):
            detune = 2 ** (rng.normal(0, 3.5) / 1200)
            jitter = rng.normal(0, 0.007) if cfg["players"] > 1 else 0.0
            # accords : arpège rapide (rasgueado à la guitare)
            down = (n["pos"] * 8) % 2 == 0
            order = pitches if down or kind != "guitare" else pitches[::-1]
            spread = 0.012 if kind == "guitare" else 0.005
            for k, p in enumerate(order):
                freq = 440 * 2 ** ((p - 69) / 12) * detune
                t0 = s0 + jitter + k * spread
                if n["trem"]:
                    step = 60 / TEMPO[bar_of(n["start"])] / 8  # triples croches
                    t, up = t0, False
                    while t < s1 - 0.02:
                        nxt = t + step
                        acc_lvl = lvl * (0.82 if up else 1.0) * rng.uniform(0.9, 1.05)
                        pluck(buf, t + rng.normal(0, 0.003), freq, nxt - t + 0.03, acc_lvl * 0.8, cfg, 0.04)
                        t, up = nxt, not up
                else:
                    dur = (s1 - s0) * (0.45 if n["stacc"] else 1.0)
                    release = 0.35 if kind == "guitare" and not n["stacc"] else 0.06
                    pluck(buf, t0, freq, max(dur - 0.02, 0.05), lvl, cfg, release)
    return buf * cfg["gain"] / np.sqrt(cfg["players"])


def peaking(f0, gain_db, q):
    A = 10 ** (gain_db / 40)
    w = 2 * np.pi * f0 / SR
    alpha = np.sin(w) / (2 * q)
    b = np.array([1 + alpha * A, -2 * np.cos(w), 1 - alpha * A])
    a = np.array([1 + alpha / A, -2 * np.cos(w), 1 - alpha / A])
    return b / a[0], a / a[0]


BODY = {  # résonances de caisse : (fréquence, gain dB, Q)
    "mandoline": [(480, 4, 1.2), (2800, 3, 1.0), (150, -6, 0.7)],
    "mandole": [(300, 4, 1.2), (2000, 2, 1.0), (90, -4, 0.7)],
    "guitare": [(105, 4, 1.5), (220, 3, 1.2), (3000, -3, 0.8)],
}
PART_GAIN = {"mandolineI": 1.3, "mandolineII": 0.9, "mandole": 1.0, "guitare": 1.6}
PAN = {"mandolineI": -0.55, "mandolineII": -0.15, "mandole": 0.2, "guitare": 0.5}


def reverb_ir(seconds=2.4, rt60=1.9):
    n = int(seconds * SR)
    t = np.arange(n) / SR
    out = []
    for _ in range(2):
        x = rng.normal(0, 1, n) * np.exp(-6.91 * t / rt60)
        x = sosfilt(butter(1, 3500, "lowpass", fs=SR, output="sos"), x)
        x[: int(0.015 * SR)] = 0
        out.append(x / np.sqrt(np.sum(x**2)))
    return np.stack(out, axis=1)


def render(path):
    mix = None
    for ident, name, _, _, music, kind in PARTS:
        buf = render_part(music, kind) * PART_GAIN[ident]
        for f0, gdb, q in BODY[kind]:
            buf = lfilter(*peaking(f0, gdb, q), buf)
        p = PAN[ident]
        st = np.stack([np.cos((p + 1) * np.pi / 4) * buf, np.sin((p + 1) * np.pi / 4) * buf], axis=1)
        mix = st if mix is None else mix + st
        print(f"  {name} rendu", flush=True)
    ir = reverb_ir()
    wet = np.stack([fftconvolve(mix[:, c], ir[:, c])[: len(mix)] for c in range(2)], axis=1)
    out = 0.8 * mix + 0.35 * wet
    out = sosfilt(butter(2, 40, "highpass", fs=SR, output="sos"), out, axis=0)
    last = np.nonzero(np.abs(out).max(axis=1) > 1e-3 * np.abs(out).max())[0][-1]
    out = out[: last + 1]
    out /= np.max(np.abs(out)) / 0.89
    fade = int(0.8 * SR)
    out[-fade:] *= np.linspace(1, 0, fade)[:, None]
    wavfile.write(path, SR, (out * 32767).astype(np.int16))
    print(f"{path}: {len(out) / SR:.1f} s")


if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "lanternes.wav")
