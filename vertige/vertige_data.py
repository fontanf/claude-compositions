"""« Vertige », toccata pour guitare seule en fa# mineur -- notes en hauteurs réelles, notation LilyPond absolue.

Deux voix : v1 (hampes en haut : pédale de cordes à vide, accords, trio) et v2 (hampes en bas : la mélodie
au pouce, basses).
"""
import re
from fractions import Fraction as F

TITLE = "Vertige"
SUBTITLE = "toccata pour guitare"
KEY = "\\key fis \\minor"
TUNING = [40, 45, 50, 55, 59, 64]
WINDOW = F(1, 4)

NBARS = 86
METER = {b: (F(1, 2), "\\time 2/4") for b in range(1, NBARS + 1)}

TEMPO = {b: 120 for b in range(1, NBARS + 1)}
TEMPO.update({b: 84 for b in range(49, 61)})
TEMPO.update({60: 76, 64: 60, 85: 108, 86: 96})

MARKS = {
    1: '\\tempo "Presto, con fuoco" 4 = 120 \\mark \\markup \\box "A"',
    17: '\\mark \\markup \\box "A2"',
    33: '\\mark \\markup \\box "B"',
    49: '\\tempo "Meno mosso, cantabile" 4 = 84 \\mark \\markup \\box "Trio" \\key a \\major',
    61: '\\tempo "Tempo I" 4 = 120 \\key fis \\minor',
    65: '\\mark \\markup \\box "A’"',
    81: '\\mark \\markup \\box "Coda"',
}
TEXTS = {1: "pouce marcato, pédale i-m légère", 33: "rasgueado", 60: "rit.", 85: "allargando"}
BARLINES = {16: "||", 32: "||", 48: "||", 60: "||", 64: "||", 80: "||", 86: "|."}
MODE = {b: "ligne" for b in range(1, NBARS + 1)}

NAMES = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]


def dyn(s, mark):
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def shift(s, octaves):
    def f(m):
        p, o = m.group(1), m.group(2)
        n = o.count("'") - o.count(",") + octaves
        return p + ("'" * n if n > 0 else "," * -n)
    return re.sub(r"(?<![a-z\\])([a-g](?:is|es)*)([',]*)(?=\d)", f, s)


def pedal(a, b, last=None):
    """la pédale des doigts, dans les trous du rythme 3+3+2 du pouce"""
    return f"r16 {a}16 {b}16 r16 {a}16 {b}16 r16 {last or b}16"


def rasg(ch):
    return f"{ch}16\\arpeggio-> {ch}16 {ch}16 {ch}16\\arpeggio-> {ch}16 {ch}16 {ch}8\\arpeggio->"


V1, V2 = {}, {}

# ---------------------------------------------------------------- A (1-16) : le thème au pouce, pédale si-mi à vide
THEME = [
    "fis8. a8. cis'8", "b8. a8. gis8", "fis8. a8. d'8", "cis'8. b8. cis'8",
    "fis8. a8. cis'8", "d'8. cis'8. b8", "a8. gis8. fis8", "cis8. gis,8. cis8",
    "fis8. a8. cis'8", "b8. a8. gis8", "fis8. a8. d'8", "cis'8. d'8. cis'8",
    "b8. a8. gis8", "a8. b8. cis'8", "d'8. cis'8. b8", "fis8. cis8. fis,8",
]
for i in range(16):
    V2[1 + i] = THEME[i].replace("8.", "8.->", 1)
    V1[1 + i] = pedal("b", "e'")
V2[1] = dyn(V2[1], "\\mf")
V1[1] = V1[1].replace("r16", "r16\\p", 1)

# ---------------------------------------------------------------- A2 (17-32) : le thème une octave plus bas, pédale inversée
for i in range(16):
    low = THEME[i] if i in (7, 15) else shift(THEME[i], -1)
    V2[17 + i] = low.replace("8.", "8.->", 1)
    V1[17 + i] = pedal("e'", "b")
V2[17] = dyn(V2[17], "\\f")

# ---------------------------------------------------------------- B (33-48) : cycle de tierces mineures
FSM = "<fis, cis fis a cis' fis'>"      # barré II
AM = "<a, e a c' e'>"                   # position ouverte
CM = "<c g c' ees'>"                    # barré III, tierce en haut (évite les quintes parallèles du cycle)
EBM = "<ees bes ees' ges'>"             # barré VI, tierce en haut
for b, ch in zip(range(33, 41), [FSM, FSM, AM, AM, CM, CM, EBM, EBM]):
    V1[b] = rasg(ch)
    V2[b] = "s2"
V1[33] = V1[33].replace("->", "->\\ff", 1)
# la tête du thème transposée sur chaque accord du cycle, avec sa pédale propre
HEADS = {
    "fis": ("fis8. a8. cis'8", "b", "e'"),
    "a": ("a,8. c8. e8", "c'", "e'"),
    "c": ("c8. ees8. g8", "ees'", "g'"),
    "ees": ("ees8. ges8. bes8", "ges'", "bes'"),
}
for b, k in zip(range(41, 48), ["fis", "a", "c", "ees", "c", "a", "fis"]):
    head, x, y = HEADS[k]
    V2[b] = head.replace("8.", "8.->", 1)
    V1[b] = pedal(x, y)
V2[41] = dyn(V2[41], "\\f")
V2[48] = "e8.-> gis8. b8"                 # mi majeur : dominante du trio
V1[48] = pedal("e'", "b", "gis'")

# ---------------------------------------------------------------- Trio (49-60) : la majeur, en tierces
TRIO_V1 = [
    "<cis'' e''>4 <a' cis''>4", "<b' d''>8 <a' cis''>8 <gis' b'>4", "<fis' a'>4 <a' cis''>4", "<gis' b'>2",
    "<cis'' e''>4 <d'' fis''>4", "<cis'' e''>8 <b' d''>8 <a' cis''>4", "<gis' b'>4 <b' d''>4", "<a' cis''>2",
    "<d'' fis''>4 <cis'' e''>4", "<b' d''>8 <a' cis''>8 <gis' b'>4", "<fis' a'>4 <e' gis'>4", "<cis' a'>2",
]
TRIO_V2 = ["a,4 e4", "b,4 e4", "a,4 e4", "e2", "a,4 d4", "cis4 a,4", "d4 b,4", "e2",
           "d4 fis4", "b,4 e4", "e4 e,4", "a,2"]
for i in range(12):
    V1[49 + i] = TRIO_V1[i]
    V2[49 + i] = TRIO_V2[i]
V1[49] = dyn(V1[49], "\\p")
V1[57] = dyn(V1[57], "\\mp")
V1[60] = dyn(V1[60], "\\p")

# ---------------------------------------------------------------- gamme et dominante (61-64)
V1[61] = "fis''16(\\mf\\< eis''16) d''16( cis''16) b'16( a'16) gis'16( fis'16)"
V1[62] = "eis'16( d'16) cis'16( b16) a16( gis16) fis16( eis16)"
C7 = "<cis eis b cis'>"                 # do#7 : x4342x
V1[63] = rasg(C7).replace("->", "->\\ff", 1)
V1[64] = f"{C7}8\\arpeggio-> r8 r4\\fermata"
for b in range(61, 65):
    V2[b] = "s2"

# ---------------------------------------------------------------- A' (65-80) : le thème, puis en octaves
for i in range(8):
    V2[65 + i] = THEME[i].replace("8.", "8.->", 1)
    V1[65 + i] = pedal("b", "e'")
V2[65] = dyn(V2[65], "\\ff")
for i in range(8, 16):
    hi = THEME[i]
    lo = shift(hi, -1)
    if i == 15:
        hi, lo = "fis8. cis'8. fis8", "fis,8. cis8. fis,8"
    V1[65 + i] = hi.replace("8.", "8.->", 1)
    V2[65 + i] = lo
V1[73] = dyn(V1[73], "\\ff")

# ---------------------------------------------------------------- Coda (81-86)
D_ = "<d a d' fis'>"
for b, ch in zip(range(81, 85), [FSM, D_, C7, FSM]):
    V1[b] = rasg(ch)
    V2[b] = "s2"
V1[85] = f"{D_}8\\arpeggio-> {D_}8\\arpeggio-> {C7}8\\arpeggio-> {C7}8\\arpeggio->"
V1[86] = f"{FSM}8\\arpeggio->\\sfz r8 r4\\fermata"
V2[85] = V2[86] = "s2"
V1[81] = V1[81].replace("->", "->\\fff", 1)

for _b in V1:
    V1[_b] = re.sub(r"(?<![\^_])\\(fff|ppp|pp|mp|mf|ff|sfz|p|f|<|>)(?![a-zA-Z])", r"^\\\1", V1[_b])

PLAN = {}
DOUBLED = set(range(73, 81))  # mélodie volontairement doublée à l'octave
