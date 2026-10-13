"""Parse les voix de fugue_data, verifie le contrepoint, ecrit le .ly."""
import re
import sys
from fractions import Fraction as F

from fugue_data import VOICES, NBARS

STEP = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
TOKEN = re.compile(r"^(<[^>]+>|[a-g](?:is|es)*[',]*|r)(\d+)(\.?)(~?)$")


def midi_of(p):
    m = re.match(r"([a-g])((?:is|es)*)([',]*)$", p)
    n = STEP[m.group(1)] + m.group(2).count("is") - m.group(2).count("es")
    return 48 + n + 12 * m.group(3).count("'") - 12 * m.group(3).count(",")


def tokens(s):
    return re.findall(r"<[^>]+>\S*|\S+", s)


def parse_voice(bars):
    """-> list of (start, dur, [midi...]) with ties merged; start/dur in whole notes."""
    notes, t = [], F(0)
    pending_tie = False
    for b in range(1, NBARS + 1):
        bar_t = F(0)
        for tok in tokens(bars[b]):
            m = TOKEN.match(tok)
            if not m:
                sys.exit(f"bad token {tok!r} bar {b}")
            pitch, den, dot, tie = m.groups()
            d = F(1, int(den)) * (F(3, 2) if dot else 1)
            if pitch == "r":
                ps = None
            elif pitch.startswith("<"):
                ps = [midi_of(x) for x in pitch[1:-1].split()]
            else:
                ps = [midi_of(pitch)]
            if ps is not None and pending_tie and notes and notes[-1][2] == ps:
                s0, d0, p0 = notes[-1]
                notes[-1] = (s0, d0 + d, p0)
            elif ps is not None:
                notes.append((t + bar_t, d, ps))
            pending_tie = bool(tie)
            bar_t += d
        if bar_t != 1:
            sys.exit(f"bar {b} has length {bar_t}")
        t += 1
    return notes


def sounding(notes, t):
    for s, d, p in notes:
        if s <= t < s + d:
            return p[0]
    return None


def check():
    parsed = {k: parse_voice(v) for k, v in VOICES.items()}
    names = list(parsed)
    times = sorted({s for n in parsed.values() for s, _, _ in n})
    issues = []
    pos = lambda t: f"m{int(t) + 1} t{float((t % 1) * 4) + 1:.2f}"
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            hi, lo = parsed[names[i]], parsed[names[j]]
            prev = None
            for t in times:
                a, b = sounding(hi, t), sounding(lo, t)
                if a is None or b is None:
                    prev = None
                    continue
                if a < b:
                    issues.append(f"{pos(t)} croisement {names[i]}/{names[j]}")
                iv = (a - b) % 12
                if prev:
                    pa, pb, piv = prev
                    if (pa, pb) != (a, b) and pa != a and pb != b and iv == piv and iv in (0, 7):
                        if (a - pa) * (b - pb) > 0:
                            kind = "octaves" if iv == 0 else "quintes"
                            issues.append(f"{pos(t)} {kind} paralleles {names[i]}/{names[j]}")
                prev = (a, b, iv)
            # dissonances sur les temps forts entre une voix et la basse
    bass = parsed["basse"]
    for t in times:
        if (t * 4) % 1 != 0:
            continue
        b = sounding(bass, t)
        for v in ("soprano", "alto"):
            a = sounding(parsed[v], t)
            if a is None or b is None:
                continue
            iv = (a - b) % 12
            if iv in (1, 2, 10, 11):
                issues.append(f"{pos(t)} dissonance {v}/basse ({iv} demi-tons)")
    return issues


def lily_bars(bars):
    return " |\n  ".join(bars[b] for b in range(1, NBARS + 1))


def write_ly(path):
    S, A, B = VOICES["soprano"], VOICES["alto"], VOICES["basse"]
    with open(path, "w") as f:
        f.write(f"""\\version "2.26.0"

\\header {{
  title = "Fugue en do mineur"
  subtitle = "à trois voix, dans le style de J.-S. Bach"
  composer = "Claude"
  tagline = ##f
}}

global = {{
  \\key c \\minor
  \\time 4/4
}}

soprano = {{
  \\global \\voiceOne
  {lily_bars(S)} \\fermata
  \\bar "|."
}}

alto = {{
  \\global \\voiceTwo
  {lily_bars(A)} \\fermata
}}

basse = {{
  \\global \\clef bass
  {lily_bars(B)} \\fermata
}}

tempi = {{
  \\tempo "Allegro moderato" 4 = 72
  s1*26
  \\tempo 4 = 63 s2 \\tempo 4 = 56 s2
  \\tempo 4 = 46 s1
}}

tempiPartition = {{
  \\tempo "Allegro moderato" 4 = 72
  s1*26 s1^\\markup {{ \\italic "rit." }} s1
}}

\\score {{
  \\new PianoStaff <<
    \\new Staff = "haut" << \\tempiPartition \\new Voice \\soprano \\new Voice \\alto >>
    \\new Staff = "bas" \\new Voice \\basse
  >>
  \\layout {{ }}
}}

\\score {{
  \\unfoldRepeats
  \\new PianoStaff <<
    \\new Staff << \\tempi \\new Voice \\soprano \\new Voice \\alto >>
    \\new Staff \\new Voice \\basse
  >>
  \\midi {{ }}
}}
""")


if __name__ == "__main__":
    for line in check():
        print(line)
    if len(sys.argv) > 1:
        write_ly(sys.argv[1])
