"""« Accord » : lecture des voix (modes de jeu, cordes imposées), vérification de la jouabilité, écriture du .ly."""
import itertools
import re
import sys
from fractions import Fraction as F

import accord_data as data
from accord_data import NBARS, METER, MARKS, TEXTS, BARLINES, TITLE, SUBTITLE, KEY, TUNING, MODE, V1, V2

STEP = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
TOKEN = re.compile(r"^(<[^>]+>|[a-g](?:is|es)*[',]*|[rRs])(\d+)(\.?)(?:\*(\d+))?(.*)$")
DYN = re.compile(r"\\(sfz|fff|ppp|pp|mp|mf|ff|p|f)(?![a-zA-Z])")
LEVEL = {"ppp": 0.22, "pp": 0.3, "p": 0.4, "mp": 0.52, "mf": 0.64, "f": 0.78, "ff": 0.92, "fff": 1.0, "sfz": 1.0}
TIMBRES = {"\\ord": "ord", "\\pont": "pont", "\\tasto": "tasto", "\\pizz": "pizz", "\\tamb": "tamb"}
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


def split_element(x):
    """« e'\\harmonic\\2 » -> (« e' », harmonique, corde imposée ou None)"""
    m = re.match(r"([a-g](?:is|es)*[',]*)(.*)$", x)
    rest = m.group(2)
    s = re.search(r"\\([1-6])(?![0-9])", rest)
    return m.group(1), "\\harmonic" in rest, int(s.group(1)) if s else None


def parse_voice(bars, voice):
    starts, _ = bar_starts()
    notes, level, hairpin, pending_tie = [], 0.5, None, False
    timbre, muted = "ord", False
    for b in range(1, NBARS + 1):
        length = F(METER[b][0]).limit_denominator(8)
        bt = F(0)
        for k_tok, tok in enumerate(re.findall(r"<[^>]+>\S*|\S+", bars[b])):
            if tok.startswith("\\"):
                timbre = TIMBRES.get(tok, timbre)
                muted = {"\\xNotesOn": True, "\\xNotesOff": False}.get(tok, muted)
                continue
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
                elems = pitch.strip("<>").split() if pitch.startswith("<") else [pitch + post]
                parsed = [split_element(x) for x in elems]
                ps = [midi_of(nm) for nm, _, _ in parsed]
                forced = [6 - s if s else None for _, _, s in parsed]   # corde imposée, son par son
                harmonic = any(h for _, h, _ in parsed)
                if pending_tie and notes and notes[-1]["pitches"] == ps:
                    notes[-1]["dur"] += d
                else:
                    notes.append(dict(start=starts[b] + bt, dur=d, pitches=ps, level=level, accent="->" in post,
                                      bar=b, pos=bt, voice=voice, harmonic=harmonic, forced=forced,
                                      strum="\\arpeggio" in post, timbre=timbre, muted=muted, tok=k_tok,
                                      slurred=False, stacc=False))
            pending_tie = "~" in post
            bt += d
        if bt != length:
            sys.exit(f"voix {voice}, mesure {b} : longueur {bt} au lieu de {length}")
    return notes


def all_notes():
    return parse_voice(V1, 1) + parse_voice(V2, 2)


# ---------------------------------------------------------------- doigté
def feasible(assign):
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
        opens = {s for s, f in assign if f == 0}
        if not any(at_lo[0] < s < at_lo[-1] for s in opens):
            fingers -= len(at_lo) - 1
    return fingers <= 4, hi - lo


def solve(pitches, forced=None):
    """répartition corde/case ; une même hauteur peut être jouée sur plusieurs cordes (unissons)"""
    forced = forced or {}
    items = sorted(pitches) if isinstance(pitches, list) else pitches
    # éléments : (hauteur, corde imposée ou None)
    elems = []
    for p, s in items if items and isinstance(items[0], tuple) else [(p, None) for p in items]:
        elems.append((p, s))
    if len(elems) > 6:
        return None
    best = None
    options = []
    for p, s in elems:
        strings = [s] if s is not None else range(6)
        options.append([(st, p - TUNING[st]) for st in strings if 0 <= p - TUNING[st] <= MAX_FRET])
    for combo in itertools.product(*options):
        if len({s for s, _ in combo}) < len(combo):
            continue
        ok, span = feasible(combo)
        if not ok:
            continue
        hard = sum(1 for s_, f in combo if s_ <= 2 and f > 12)
        cost = (1.5 * span + max(f for _, f in combo) + 4 * hard, sum(f for _, f in combo))
        if best is None or cost < best[0]:
            best = (cost, combo)
    return best and list(zip(elems, best[1]))


def elements(n):
    """(hauteur, corde imposée) pour chaque son d'une note ou d'un accord"""
    return list(zip(n["pitches"], n["forced"]))


def check(verbose=False, notes=None):
    notes = [n for n in (notes or all_notes()) if not n["harmonic"] and not n["muted"]]
    starts, _ = bar_starts()
    issues, strings = [], {}
    for b in range(1, NBARS + 1):
        b0, b1 = starts[b], starts[b] + F(METER[b][0]).limit_denominator(8)
        if MODE[b] == "anneau":
            group = [n for n in notes if b0 <= n["start"] < b1]
            # une même hauteur rejouée sur la même corde ne compte qu'une fois
            elems = sorted({e for n in group for e in elements(n)},
                           key=lambda e: (e[0], e[1] is None))
            uniq = {}
            for p, s in elems:
                if p not in uniq or uniq[p] is None:
                    uniq[p] = s
            sol = solve([(p, s) for p, s in sorted(uniq.items())])
            if sol is None:
                issues.append(f"m{b} : forme résonante injouable {sorted(uniq)}")
                continue
            by_pitch = {p: sf for (p, _), sf in sol}
            for n in group:
                for k, p in enumerate(n["pitches"]):
                    strings[(id(n), k)] = by_pitch[p]
            if verbose:
                print(f"m{b}", sorted((6 - s, f) for s, f in by_pitch.values()))
        else:
            for t in sorted({n["start"] for n in notes if b0 <= n["start"] < b1}):
                snd = [n for n in notes if n["start"] <= t < n["start"] + n["dur"]]
                elems = [(p, s, n, k) for n in snd for k, (p, s) in enumerate(elements(n))]
                sol = solve([(p, s) for p, s, _, _ in elems])
                if sol is None:
                    issues.append(f"m{b} t={float((t - b0) * 8):.2f} croche : injouable "
                                  f"{sorted(p for p, _, _, _ in elems)}")
                    continue
                # on recolle les solutions aux notes (attention aux unissons sur plusieurs cordes)
                pool = list(sol)
                for p, s, n, k in elems:
                    for j, ((pp, ss), sf) in enumerate(pool):
                        if pp == p and ss == s:
                            if n["start"] == t:
                                strings.setdefault((id(n), k), sf)
                            pool.pop(j)
                            break
                if verbose:
                    print(f"m{b} t={float((t - b0) * 8):.2f}", sorted((6 - s, f) for _, (s, f) in sol))
    return issues, strings


# ---------------------------------------------------------------- partition
MACROS = r'''
ord = <>^\markup \italic "ord."
pont = <>^\markup \italic "sul pont."
tasto = <>^\markup \italic "sul tasto"
pizz = <>^\markup \italic "pizz."
tamb = <>^\markup \italic "tamb."
'''


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
    from doigtes import annotate
    A1, A2 = annotate(sys.modules[__name__], data)
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
{MACROS}
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


if __name__ == "__main__":
    issues, _ = check(verbose="-v" in sys.argv)
    for line in issues:
        print(line)
    out = [a for a in sys.argv[1:] if not a.startswith("-")]
    if out:
        write_ly(out[0])
