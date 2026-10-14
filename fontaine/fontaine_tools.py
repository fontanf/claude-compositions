"""« Fontaine » : lecture des voix, vérification de la jouabilité à la guitare, écriture du .ly."""
import itertools
import re
import sys
from fractions import Fraction as F

from fontaine_data import (NBARS, METER, MARKS, TEXTS, BARLINES, TITLE, SUBTITLE, KEY, TUNING, MODE, V1, V2)

STEP = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
TOKEN = re.compile(r"^(<[^>]+>|[a-g](?:is|es)*[',]*|[rRs])(\d+)(\.?)(?:\*(\d+))?(.*)$")
DYN = re.compile(r"\\(sfz|ppp|pp|mp|mf|ff|p|f)(?![a-zA-Z])")
LEVEL = {"ppp": 0.22, "pp": 0.3, "p": 0.4, "mp": 0.52, "mf": 0.64, "f": 0.78, "ff": 0.92, "sfz": 1.0}
MAX_FRET = 19


def midi_of(p):
    m = re.match(r"([a-g])((?:is|es)*)([',]*)$", p)
    n = STEP[m.group(1)] + m.group(2).count("is") - m.group(2).count("es")
    return 48 + n + 12 * m.group(3).count("'") - 12 * m.group(3).count(",")


def bar_starts():
    t, out = F(0), {}
    for b in range(1, NBARS + 1):
        out[b] = t
        t += F(METER[b][0]).limit_denominator(8)
    return out, t


def parse_voice(bars, voice):
    starts, _ = bar_starts()
    notes, level, hairpin, pending_tie, in_slur = [], 0.6, None, False, False
    for b in range(1, NBARS + 1):
        length = F(METER[b][0]).limit_denominator(8)
        bt = F(0)
        for tok in re.findall(r"<[^>]+>\S*|\S+", bars[b]):
            m = TOKEN.match(tok)
            if not m:
                sys.exit(f"jeton invalide {tok!r} mesure {b}")
            pitch, den, dot, mul, post = m.groups()
            d = F(1, int(den)) * (F(3, 2) if dot else 1) * (int(mul) if mul else 1)
            if pitch == "R":
                d = length
            dm = DYN.search(post)
            if dm:
                new = LEVEL[dm.group(1)]
                if hairpin is not None:
                    seg = notes[hairpin:]
                    for k, n in enumerate(seg):
                        n["level"] += (new - n["level"]) * (k + 1) / (len(seg) + 1)
                    hairpin = None
                level = new
            if "\\<" in post or "\\>" in post:
                hairpin = len(notes)
            if pitch not in "rRs":
                harmonic = "\\harmonic" in pitch
                names = pitch.replace("\\harmonic", "").strip("<>").split()
                ps = [midi_of(x) for x in names]
                if pending_tie and notes and notes[-1]["pitches"] == ps:
                    notes[-1]["dur"] += d
                else:
                    notes.append(dict(start=starts[b] + bt, dur=d, pitches=ps, level=level, accent="->" in post,
                                      stacc="-." in post, bar=b, pos=bt, voice=voice, harmonic=harmonic,
                                      strum="\\arpeggio" in post, slurred=in_slur))
                if "(" in post:
                    in_slur = True
                if ")" in post:
                    in_slur = False
            pending_tie = "~" in post
            bt += d
        if bt != length:
            sys.exit(f"voix {voice}, mesure {b} : longueur {bt} au lieu de {length}")
    return notes


def all_notes():
    return parse_voice(V1, 1) + parse_voice(V2, 2)


# ---------------------------------------------------------------- doigté
def feasible(assign):
    """assign : liste de (corde, case). Contraintes de la main gauche."""
    fretted = [(s, f) for s, f in assign if f > 0]
    if not fretted:
        return True, 0
    frets = [f for _, f in fretted]
    lo, hi = min(frets), max(frets)
    if hi - lo > (4 if lo < 7 else 5):
        return False, None
    fingers = len(fretted)
    at_lo = sorted(s for s, f in fretted if f == lo)
    if len(at_lo) > 1:
        # barré possible seulement si aucune corde à vide ne doit sonner entre les cordes barrées
        opens = {s for s, f in assign if f == 0}
        if not any(at_lo[0] < s < at_lo[-1] for s in opens):
            fingers -= len(at_lo) - 1
    return fingers <= 4, hi - lo


def solve(pitches):
    """meilleure répartition des hauteurs sur les cordes (ou None)"""
    pitches = sorted(set(pitches))
    if len(pitches) > 6:
        return None
    best = None
    options = [[(s, p - TUNING[s]) for s in range(6) if 0 <= p - TUNING[s] <= MAX_FRET] for p in pitches]
    for combo in itertools.product(*options):
        strings = [s for s, _ in combo]
        if len(set(strings)) < len(strings):
            continue
        ok, span = feasible(combo)
        if not ok:
            continue
        # écart réduit, position basse, et pas de cases au-delà de XII sur les cordes graves (au-dessus de la caisse)
        hard = sum(1 for s_, f in combo if s_ <= 2 and f > 12)
        cost = (1.5 * span + max(f for _, f in combo) + 4 * hard, sum(f for _, f in combo))
        if best is None or cost < best[0]:
            best = (cost, dict(zip(pitches, combo)))
    return best and best[1]


def sounding(notes, t):
    return [n for n in notes if n["start"] <= t < n["start"] + n["dur"]]


def check(verbose=False, notes=None):
    notes = [n for n in (notes or all_notes()) if not n["harmonic"]]
    starts, total = bar_starts()
    issues, strings = [], {}
    for b in range(1, NBARS + 1):
        b0 = starts[b]
        if MODE[b] == "forme":
            # chaque demi-mesure : la main gauche tient la forme de l'arpège (voix 2), plus la note de mélodie
            for h in (0, 1):
                w0, w1 = b0 + F(3, 8) * h, b0 + F(3, 8) * (h + 1)
                base = [n for n in notes if n["voice"] == 2 and n["start"] < w1 and n["start"] + n["dur"] > w0]
                base = [n for n in notes if n["voice"] == 2 and w0 <= n["start"] < w1] or base
                mel = [n for n in notes if n["voice"] == 1 and n["start"] < w1 and n["start"] + n["dur"] > w0]
                for m in mel or [None]:
                    ps = [p for n in base for p in n["pitches"]] + (m["pitches"] if m else [])
                    sol = solve(ps)
                    if sol is None:
                        issues.append(f"m{b} demi-mesure {h + 1} : forme injouable {sorted(set(ps))}")
                        continue
                    for n in base + ([m] if m else []):
                        for p in n["pitches"]:
                            strings[(id(n), p)] = sol[p]
                    if verbose:
                        print(f"m{b}.{h + 1}", sorted((6 - s, f) for s, f in sol.values()))
        else:
            for t in sorted({n["start"] for n in notes if b0 <= n["start"] < b0 + F(3, 4)}):
                snd = sounding(notes, t)
                ps = [p for n in snd for p in n["pitches"]]
                sol = solve(ps)
                if sol is None:
                    issues.append(f"m{b} t={float((t - b0) * 8):.2f} croche : injouable {sorted(set(ps))}")
                    continue
                for n in snd:
                    if n["start"] == t:
                        for p in n["pitches"]:
                            strings[(id(n), p)] = sol[p]
    return issues, strings


# ---------------------------------------------------------------- partition
def global_music():
    out = []
    for b in range(1, NBARS + 1):
        pre = [METER[b][1]] if b == 1 else []
        if b in MARKS:
            pre.append(MARKS[b])
        spacer = "s8*6"
        if b in TEXTS:
            spacer += f'^\\markup {{ \\italic "{TEXTS[b]}" }}'
        post = f' \\bar "{BARLINES[b]}"' if b in BARLINES else ""
        out.append(" ".join(pre + [spacer]) + post)
    return "\n  ".join(out)


def voice_def(name, bars):
    body = " |\n  ".join(bars[b] for b in range(1, NBARS + 1))
    return f"{name} = {{\n  {body}\n}}\n"


def write_ly(path):
    staff = ('\\new Staff \\with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } '
             '<< \\global \\new Voice { \\voiceOne \\vUn } \\new Voice { \\voiceTwo \\vDeux } >>')
    with open(path, "w") as f:
        f.write(f"""\\version "2.26.0"

\\header {{
  title = "{TITLE}"
  subtitle = "{SUBTITLE}"
  composer = "Claude"
  tagline = ##f
}}

\\paper {{ #(set-paper-size "a4") }}

global = {{
  \\clef "treble_8" {KEY}
  {global_music()}
}}

{voice_def("vUn", V1)}
{voice_def("vDeux", V2)}
\\score {{
  {staff}
  \\layout {{ }}
}}

\\score {{
  {staff}
  \\midi {{ }}
}}
""")


if __name__ == "__main__":
    issues, _ = check(verbose="-v" in sys.argv)
    for line in issues:
        print(line)
    out = [a for a in sys.argv[1:] if not a.startswith("-")]
    if out:
        write_ly(out[0])
