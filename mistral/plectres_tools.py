"""Parse « Mistral », vérifie mesures et harmonie, écrit le .ly."""
import re
import sys
from fractions import Fraction as F

from plectres_data import NBARS, METER, MARKS, TEXTS, BARLINES, PARTS, CHORDS

STEP = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
TOKEN = re.compile(r"^(<[^>]+>|[a-g](?:is|es)*[',]*|[rRs])(\d+)(\.?)(?:\*(\d+))?(.*)$")
DYN = re.compile(r"\\(sfz|ppp|pp|mp|mf|ff|p|f)(?![a-zA-Z])")
LEVEL = {"ppp": 0.22, "pp": 0.3, "p": 0.4, "mp": 0.52, "mf": 0.64, "f": 0.78, "ff": 0.92, "sfz": 1.0}


def pc(p):
    m = re.match(r"([a-g])((?:is|es)*)", p)
    return (STEP[m.group(1)] + m.group(2).count("is") - m.group(2).count("es")) % 12


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


def parse_voice(bars):
    """-> notes: dict(start, dur, pitches, trem, level, accent, stacc, bar, pos)"""
    starts, _ = bar_starts()
    notes, level = [], 0.6
    hairpin = None  # index de la note où commence un soufflet
    pending_tie = False
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
                if hairpin is not None:  # interpolation du soufflet
                    seg = notes[hairpin:]
                    for k, n in enumerate(seg):
                        n["level"] += (new - n["level"]) * (k + 1) / (len(seg) + 1)
                    hairpin = None
                level = new
            if "\\<" in post or "\\>" in post:
                hairpin = len(notes)
            if pitch not in "rRs":
                ps = [midi_of(x) for x in pitch[1:-1].split()] if pitch.startswith("<") else [midi_of(pitch)]
                pcs = [pc(x) for x in pitch.strip("<>").split()]
                if pending_tie and notes and notes[-1]["pitches"] == ps:
                    notes[-1]["dur"] += d
                else:
                    notes.append(dict(start=starts[b] + bt, dur=d, pitches=ps, pcs=pcs,
                                      trem=":32" in post, level=level, accent="->" in post,
                                      stacc="-." in post, bar=b, pos=bt))
            pending_tie = "~" in post
            bt += d
        if bt != length:
            sys.exit(f"mesure {b} : longueur {bt} au lieu de {length}")
    return notes


def accent_positions(b):
    sig = METER[b][1]
    if "3,3,2" in sig:
        return {0, 3, 6}
    if "2,2,3" in sig:
        return {0, 2, 4}
    return {0, 2, 4, 6}


def check():
    issues = []
    for ident, name, _, _, music, _ in PARTS:
        for n in parse_voice(music):
            b, e8 = n["bar"], n["pos"] * 8
            if e8.denominator != 1 or int(e8) not in accent_positions(b):
                continue
            chord = [c for s, c in CHORDS[b] if s <= e8][-1]
            allowed = {pc(x) for x in chord.split()}
            bad = [x for x in n["pcs"] if x not in allowed]
            if bad:
                issues.append(f"m{b} croche {int(e8)} {name}: note hors accord ({chord})")
    return issues


def global_music():
    out, prev = [], None
    for b in range(1, NBARS + 1):
        length, sig = METER[b]
        pre = []
        if sig != prev:
            pre.append(sig)
            prev = sig
        if b in MARKS:
            pre.append(MARKS[b])
        spacer = "s1" if length == 1 else "s8*7"
        if b in TEXTS:
            spacer += f'^\\markup {{ \\italic "{TEXTS[b]}" }}'
        post = f' \\bar "{BARLINES[b]}"' if b in BARLINES else ""
        out.append(" ".join(pre + [spacer]) + post)
    return "\n  ".join(out)


def music_def(ident, music, clef):
    bars = " |\n  ".join(music[b] for b in range(1, NBARS + 1))
    return f"{ident} = {{\n  \\clef \"{clef}\" \\key e \\minor\n  {bars}\n}}\n"


def write_ly(path):
    head = """\\version "2.26.0"

\\header {
  title = "Mistral"
  subtitle = "pour orchestre à plectres"
  composer = "Claude"
  tagline = ##f
}

\\paper { #(set-paper-size "a4") }

"""
    defs = f"global = {{\n  {global_music()}\n}}\n\n"
    defs += "\n".join(music_def(i, m, c) for i, _, _, c, m, _ in PARTS)
    staves = "\n".join(
        f'      \\new Staff \\with {{ instrumentName = "{n}" shortInstrumentName = "{s}" '
        f'midiInstrument = "{"acoustic guitar (nylon)" if i == "guitare" else "acoustic guitar (steel)"}" }}'
        f" << \\global \\{i} >>"
        for i, n, s, _, _, _ in PARTS)
    score = f"""
\\book {{
  \\score {{
    \\new StaffGroup <<
{staves}
    >>
    \\layout {{ }}
  }}
  \\score {{
    \\new StaffGroup <<
{staves}
    >>
    \\midi {{ }}
  }}
}}
"""
    parts = "".join(f"""
\\book {{
  \\bookOutputSuffix "{i}"
  \\header {{ instrument = "{n}" }}
  \\score {{
    \\new Staff << \\global \\compressMMRests \\{i} >>
    \\layout {{ }}
  }}
}}
""" for i, n, _, _, _, _ in PARTS)
    with open(path, "w") as f:
        f.write(head + defs + score + parts)


if __name__ == "__main__":
    for line in check():
        print(line)
    if len(sys.argv) > 1:
        write_ly(sys.argv[1])
