"""Rendu audio de la fugue : orgue additif + reverberation synthetique."""
import sys

import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt

from fugue_data import VOICES
from fugue_tools import parse_voice

SR = 44100
rng = np.random.default_rng(1)

# tempo (noires/minute) par mesure : (debut en rondes, bpm)
TEMPO = [(0, 72), (26, 63), (26.5, 56), (27, 46)]
FERMATA = 1.6  # allonge l'accord final


def to_seconds(t):
    t = float(t)
    sec, edges = 0.0, TEMPO + [(1e9, None)]
    for (t0, bpm), (t1, _) in zip(edges, edges[1:]):
        if t <= t0:
            break
        sec += (min(t, t1) - t0) * 4 * 60 / bpm
    return sec


# harmoniques : montre 8' + prestant 4' (renforce les harmoniques paires)
PARTIALS = np.array([1.0, 0.62, 0.30, 0.26, 0.12, 0.11, 0.05, 0.06, 0.03, 0.03])
VOICE_CFG = {  # (gain, panoramique -1..1, ajout bourdon 16')
    "soprano": (0.85, 0.30, 0.0),
    "alto": (0.80, -0.05, 0.0),
    "basse": (0.95, -0.30, 0.35),
}


def organ_note(freq, dur, sub):
    n = int((dur + 0.15) * SR)
    t = np.arange(n) / SR
    sig = np.zeros(n)
    for k, a in enumerate(PARTIALS, start=1):
        f = freq * k
        if f > SR / 2.2:
            break
        detune = 1 + rng.normal(0, 0.0004)
        sig += a * np.sin(2 * np.pi * f * detune * t + rng.uniform(0, 2 * np.pi))
    if sub:
        sig += sub * np.sin(2 * np.pi * freq / 2 * t) + sub * 0.3 * np.sin(2 * np.pi * freq * t)
    # attaque avec leger "chiff" (bruit filtre), tenue, extinction
    att, rel = 0.025, 0.12
    env = np.ones(n)
    na = int(att * SR)
    env[:na] = np.linspace(0, 1, na) ** 1.5
    nd = int(dur * SR)
    tail = n - nd
    env[nd:] = np.exp(-np.arange(tail) / (rel / 5 * SR))
    chiff = rng.normal(0, 1, na * 3)
    sos = butter(2, [min(freq * 2, SR / 2.5), min(freq * 6, SR / 2.1)], "bandpass", fs=SR, output="sos")
    chiff = sosfilt(sos, chiff) * np.linspace(1, 0, na * 3) * 0.6
    sig[: na * 3] += chiff
    sig *= env
    return sig / PARTIALS.sum() * (freq / 261.6) ** -0.2


def reverb_ir(seconds=2.6, rt60=2.3):
    n = int(seconds * SR)
    t = np.arange(n) / SR
    decay = np.exp(-6.91 * t / rt60)
    ir = []
    for ch in range(2):
        noise = rng.normal(0, 1, n)
        lo = sosfilt(butter(1, 2500, "lowpass", fs=SR, output="sos"), noise)
        hi_cut = sosfilt(butter(1, 900, "lowpass", fs=SR, output="sos"), noise)
        mix = np.clip(t / seconds * 2, 0, 1)  # le timbre s'assombrit dans la queue
        x = ((1 - mix) * lo + mix * hi_cut) * decay
        x[: int(0.012 * SR)] = 0  # pre-delay
        ir.append(x / np.sqrt(np.sum(x**2)))
    return np.stack(ir, axis=1)


def render(out_wav):
    end = to_seconds(28) + 4 * 60 / 46 * (FERMATA - 1)
    mix = np.zeros((int((end + 15) * SR), 2))
    for name, bars in VOICES.items():
        gain, pan, sub = VOICE_CFG[name]
        l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        for start, dur, pitches in parse_voice(bars):
            s0, s1 = to_seconds(start), to_seconds(start + dur)
            if float(start + dur) >= 28:
                s1 += 4 * 60 / 46 * (FERMATA - 1)
            length = (s1 - s0) - min(0.06, 0.12 * (s1 - s0))  # articulation legerement detachee
            for p in pitches:
                note = gain * organ_note(440 * 2 ** ((p - 69) / 12), length, sub)
                i = int(s0 * SR)
                mix[i : i + len(note), 0] += l * note
                mix[i : i + len(note), 1] += r * note
    ir = reverb_ir()
    wet = np.stack([fftconvolve(mix[:, c], ir[:, c])[: len(mix)] for c in range(2)], axis=1)
    out = 0.78 * mix + 0.42 * wet
    last = np.nonzero(np.abs(out).max(axis=1) > 1e-3 * np.abs(out).max())[0][-1]
    out = out[: last + 1]
    out /= np.max(np.abs(out)) / 0.89
    fade = int(1.5 * SR)
    out[-fade:] *= np.linspace(1, 0, fade)[:, None]
    wavfile.write(out_wav, SR, (out * 32767).astype(np.int16))
    print(f"{out_wav}: {len(out) / SR:.1f} s")


if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "fugue.wav")
