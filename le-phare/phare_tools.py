"""« Le Phare » : lecture des voix, vérification de la jouabilité à la guitare, écriture du .ly."""
import itertools
import re
import sys
from fractions import Fraction as F

from phare_data import (NBARS, METER, MARKS, TEXTS, BARLINES, TITLE, SUBTITLE, KEY, TUNING, MODE, V1, V2,
                        WINDOW, PLAN)

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
        for k_tok, tok in enumerate(re.findall(r"<[^>]+>\S*|\S+", bars[b])):
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
                                      strum="\\arpeggio" in post, slurred=in_slur, tok=k_tok))
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
            nwin = int(F(METER[b][0]).limit_denominator(8) / WINDOW)
            for h in range(nwin):
                w0, w1 = b0 + WINDOW * h, b0 + WINDOW * (h + 1)
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
            for t in sorted({n["start"] for n in notes if b0 <= n["start"] < b0 + F(METER[b][0]).limit_denominator(8)}):
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
        pre = [METER[b][1]] if b == 1 or METER[b] != METER[b - 1] else []
        if b in MARKS:
            pre.append(MARKS[b])
        spacer = f"s8*{int(F(METER[b][0]).limit_denominator(8) * 8)}"
        if b in TEXTS:
            spacer += f'^\\markup {{ \\italic "{TEXTS[b]}" }}'
        post = f' \\bar "{BARLINES[b]}"' if b in BARLINES else ""
        out.append(" ".join(pre + [spacer]) + post)
    return "\n  ".join(out)


def voice_def(name, bars):
    body = " |\n  ".join(bars[b] for b in range(1, NBARS + 1))
    return f"{name} = {{\n  {body}\n}}\n"


def write_ly(path):
    import phare_data as data
    from doigtes import annotate
    A1, A2 = annotate(sys.modules[__name__], data)  # partition avec doigtés
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

{voice_def("vUn", A1)}
{voice_def("vDeux", A2)}
\\score {{
  {staff}
  \\layout {{ }}
}}

\\score {{
  {staff}
  \\midi {{ }}
}}
""")


# ---------------------------------------------------------------- relecture harmonique
PC = ["do", "do#", "ré", "mib", "mi", "fa", "fa#", "sol", "lab", "la", "sib", "si"]
QUAL = {(0, 4, 7): "", (0, 3, 7): "m", (0, 3, 6): "dim", (0, 4, 8): "aug"}


def chord_name(pcs, bass):
    best = None
    for r in range(12):
        rel = {(p - r) % 12 for p in pcs}
        for q, name in QUAL.items():
            if set(q) <= rel:
                score = (r == bass) * 2 + len(rel & {10, 11})
                if best is None or score > best[0]:
                    ext = sorted(rel - set(q))
                    best = (score, f"{PC[r]}{name}" + (f" +{ext}" if ext else ""))
    if best:
        return best[1]
    for r in range(12):
        rel = {(p - r) % 12 for p in pcs}
        if {0, 7} <= rel and not rel & {3, 4}:
            return f"{PC[r]} SANS TIERCE +{sorted(rel - {0, 7})}"
    return "?"


def relecture():
    """sonorité de chaque demi-mesure (ce qui sonne en même temps), comparée au plan"""
    notes = all_notes()
    starts, _ = bar_starts()
    lines = []
    for b in range(1, NBARS + 1):
        nwin = int(F(METER[b][0]).limit_denominator(8) / WINDOW)
        for h in range(nwin):
            w0, w1 = starts[b] + WINDOW * h, starts[b] + WINDOW * (h + 1)
            win = [n for n in notes if n["start"] < w1 and n["start"] + n["dur"] > w0]
            ps = sorted({p for n in win for p in n["pitches"]})
            if not ps:
                continue
            mel = sorted({PC[p % 12] for n in win if n["voice"] == 1 for p in n["pitches"]}, key=PC.index)
            plan = PLAN.get(b, ("", ""))[h] if b in PLAN else ""
            lines.append(f"m{b}.{h + 1}: basse {PC[ps[0] % 12]:4s} -> {chord_name({p % 12 for p in ps}, ps[0] % 12):26s}"
                         f" plan: {plan:12s} haut: {' '.join(mel)}")
    return lines


def paralleles():
    """quintes et octaves parallèles entre la note la plus haute et la basse, attaque par attaque"""
    notes = [dict(n) for n in all_notes() if not n["harmonic"]]
    starts, _ = bar_starts()
    for n in notes:  # dans les arpèges, la basse résonne jusqu'à la fin de la forme
        if n["voice"] == 2 and MODE[n["bar"]] == "forme":
            w = starts[n["bar"]] + (n["pos"] // WINDOW + 1) * WINDOW
            n["dur"] = max(n["dur"], w - n["start"])
    onsets = sorted({n["start"] for n in notes})
    prev, out = None, []
    for tt in onsets:
        snd = [p for n in notes if n["start"] <= tt < n["start"] + n["dur"] for p in n["pitches"]]
        top = [p for n in notes if n["voice"] == 1 and n["start"] <= tt < n["start"] + n["dur"] for p in n["pitches"]]
        if not snd or not top:
            prev = None
            continue
        cur = (max(top), min(snd))
        if prev and prev[0] != cur[0] and prev[1] != cur[1]:
            i0, i1 = (prev[0] - prev[1]) % 12, (cur[0] - cur[1]) % 12
            if i0 == i1 and i0 in (0, 7) and (cur[0] - prev[0]) * (cur[1] - prev[1]) > 0:
                b = max(b for b, s in bar_starts()[0].items() if s <= tt)
                out.append(f"m{b} : {'octaves' if i0 == 0 else 'quintes'} parallèles entre le dessus et la basse")
        prev = cur
    return out


if __name__ == "__main__":
    issues, _ = check(verbose="-v" in sys.argv)
    for line in issues + paralleles():
        print(line)
    if "--relecture" in sys.argv:
        print("\n".join(relecture()))
    out = [a for a in sys.argv[1:] if not a.startswith("-")]
    if out:
        write_ly(out[0])
