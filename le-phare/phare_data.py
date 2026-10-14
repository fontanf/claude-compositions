"""« Le Phare » pour guitare seule (accord standard) -- notes en hauteurs réelles, notation LilyPond absolue.

Deux voix : v1 (hampes en haut : mélodie, accords, harmoniques) et v2 (hampes en bas : basses et arpèges).
"""
import re
from fractions import Fraction as F

TITLE = "Le Phare"
SUBTITLE = "pour guitare"
KEY = "\\key e \\minor"
TUNING = [40, 45, 50, 55, 59, 64]  # mi2 la2 ré3 sol3 si3 mi4
WINDOW = F(1, 2)                   # une forme de main gauche par demi-mesure

NBARS = 52
METER = {b: (1, "\\time 4/4") for b in range(1, NBARS + 1)}

TEMPO = {b: 66 for b in range(1, 13)}
TEMPO.update({13: 72, 14: 84, 15: 100, 16: 116})
TEMPO.update({b: 132 for b in range(17, 33)})
TEMPO.update({33: 60, 34: 40, 35: 56, 36: 56})
TEMPO.update({b: 60 for b in range(37, 49)})
TEMPO.update({47: 54, 48: 48, 49: 54, 50: 54, 51: 50, 52: 44})

MARKS = {
    1: '\\tempo "Lento, misterioso" 4 = 66 \\mark \\markup \\box "Le phare"',
    5: '\\mark \\markup \\box "A"',
    13: '\\tempo "accelerando"',
    17: '\\tempo "Agitato" 4 = 132 \\mark \\markup \\box "B — la tempête"',
    35: '\\mark \\markup \\box "Le phare"',
    37: '\\tempo "Largamente, luminoso" 4 = 60 \\mark \\markup \\box "A’" \\key e \\major',
    49: '\\tempo "Lontano" 4 = 54 \\mark \\markup \\box "Coda"',
}
TEXTS = {25: "tambora", 29: "rasgueado", 47: "rit.", 51: "rit."}
BARLINES = {4: "||", 16: "||", 32: "||", 36: "||", 48: "||", 52: "|."}

MODE = {b: "ligne" for b in range(1, NBARS + 1)}
for b in list(range(5, 17)):
    MODE[b] = "forme"

NAMES = ["c", "cis", "d", "ees", "e", "f", "fis", "g", "aes", "a", "bes", "b"]


def ly(m):
    o, pc = divmod(m, 12)
    o -= 4
    return NAMES[pc] + ("'" * o if o > 0 else "," * -o)


def dyn(s, mark):
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def arp8(shape):
    """une demi-mesure d'arpège en croches : basse, x, y, x"""
    b, x, y = shape
    return f"{b}8 {x}8 {y}8 {x}8"


def H(p, label):
    return f"<{p}\\harmonic>4^\"{label}\""


BEACON = f"r4 {H('b', 'XII②')} <e'\\harmonic>2^\"XII①\""
BEACON = BEACON.replace("<b\\harmonic>", "<b'\\harmonic>").replace("<e'\\harmonic>", "<e''\\harmonic>")

V1, V2 = {}, {}

# ---------------------------------------------------------------- Le phare (1-4) : harmoniques
for b in range(1, 5):
    V1[b] = BEACON
    V2[b] = "s1" if b < 3 else "e,1"
V1[1] = V1[1].replace("r4", "r4\\p", 1)
V2[3] = "e,1\\pp"

# ---------------------------------------------------------------- A (5-12) : le thème en mi mineur
# chaque cellule : un saut de sixte mineure, puis une chute d'un demi-ton (mi-do-si, ré-sib-la, do-lab-sol)
THEME = ["e'4. e'8 c''2", "b'2. r4", "d'4. d'8 bes'2", "a'2. r4",
         "c'4. c'8 aes'2", "g'2 fis'4 e'4", "dis'2 fis'4 c''4", "b'4 g'4 e'2"]
SHAPES = [  # (basse, x, y) par demi-mesure
    (("e,", "b,", "g"), ("e,", "g", "e'")),          # mi m | do/mi (le do aigu, sixte mineure sur la basse mi)
    (("e,", "g", "b"), ("d", "g", "b")),             # mi m | sol/ré (la basse descend mi-ré-si♭)
    (("bes,", "f", "bes"), ("bes,", "f", "d'")),     # si♭ (relation de triton avec mi)
    (("c", "e", "a"), ("c", "e", "a")),              # la m/do
    (("c", "ees", "aes"), ("c", "ees", "aes")),      # la♭/do
    (("b,", "d", "g"), ("a,", "e", "c'")),           # sol/si | fa#ø7/la
    (("b,", "fis", "a"), ("b,", "dis", "a")),        # si7 (neuvième mineure sur le do aigu)
    (("e,", "g", "b"), ("e,", "b,", "g")),           # mi m (la cadence garde sa tierce)
]
for i in range(8):
    V1[5 + i] = THEME[i]
    V2[5 + i] = arp8(SHAPES[i][0]) + " " + arp8(SHAPES[i][1])
V1[5] = dyn(V1[5], "\\mf")
V2[5] = dyn(V2[5], "\\p")
V1[11] = dyn(V1[11], "\\f")
V1[12] = dyn(V1[12], "\\mp")

# ---------------------------------------------------------------- transition (13-16) : la cellule monte par demi-tons
RISE = ["e'4. e'8 c''2", "f'4. f'8 des''2", "fis'4. fis'8 d''2", "g'4. g'8 ees''2"]
for i in range(4):
    V1[13 + i] = RISE[i]
    V2[13 + i] = "e,8 e,8 e,8 e,8 e,8 e,8 e,8 e,8"
V1[13] = dyn(V1[13], "\\mp\\<")
V1[16] = dyn(V1[16], "\\f")
V2[13] = dyn(V2[13], "\\p")


# ---------------------------------------------------------------- B (17-32) : la tempête
def quartal(n, high=False):
    """forme en quartes sur trois cordes voisines (case n), glissée chromatiquement"""
    base = [55, 59, 64] if high else [50, 55, 59]   # cordes 3-2-1 ou 4-3-2
    offs = [0, 1, 1] if high else [0, 0, 1]
    return "<" + " ".join(ly(p + n + o) for p, o in zip(base, offs)) + ">"


def storm(a, b):
    return f"e,8 e,8 {a}8-> e,8 e,8 {a}8-> e,8 {b}8->"


for i, (n1, n2) in enumerate([(3, 4), (3, 4), (4, 5), (5, 4), (5, 6), (6, 7), (7, 8), (8, 9)]):
    high = i >= 4
    V1[17 + i] = storm(quartal(n1, high), quartal(n2, high)).replace("e,8 ", "s8 ")
    V2[17 + i] = "e,8 e,8 s8 e,8 e,8 s8 e,8 s8"
V1[17] = V1[17].replace("s8", "s8\\f", 1)
V1[21] = V1[21].replace("s8", "s8\\<", 1)
V1[24] = V1[24].replace("s8", "s8\\ff", 1)
# la cellule du thème à la basse, transposée par tritons, sous des frappes tambora
for b, (p, q) in zip(range(25, 29), [("e,", "c"), ("bes,", "fis"), ("e,", "c"), ("bes,", "fis")]):
    V2[b] = f"{p}4.-> {p}8 {q}2"
    V1[b] = f"r4 {quartal(3 if b % 2 else 9)}8-> r8 r4 {quartal(4 if b % 2 else 8)}4->"
V2[25] = dyn(V2[25], "\\f")


def phryg(n):
    """accord phrygien (forme mi-si-mi-sol-do-fa) glissé à la case n ; hors position ouverte, sur cinq cordes
    (barré, majeur sur la 2e corde, annulaire et auriculaire sur les 5e et 4e)"""
    ps = [40, 47, 52, 55, 60, 65] if n == 0 else [40, 47, 52, 55, 60]
    return "<" + " ".join(ly(p + n) for p in ps) + ">"


for b, n in zip(range(29, 33), [0, 1, 3, 5]):
    c = phryg(n)
    V1[b] = f"{c}8\\arpeggio-> {c}8 {c}8 {c}8 {c}4\\arpeggio-> {c}4\\arpeggio->"
    V2[b] = "s1"
V1[29] = V1[29].replace("->", "->\\ff", 1)
V1[33] = f"{phryg(0)}1\\arpeggio->\\fff\\fermata"
V1[34] = "R1\\fermata"
V2[33] = V2[34] = "s1"
V1[35] = V1[35 - 34]
V1[35] = BEACON.replace("r4", "r4\\pp", 1)
V1[36] = BEACON
V2[35] = V2[36] = "e,1"

# ---------------------------------------------------------------- A' (37-48) : le thème en mi majeur avec sixte mineure
APRIME_V1 = [
    "<gis b e'>4. <gis b e'>8 <e gis c''>2",         # mi | mi augmenté (le do devient la quinte augmentée)
    "<e gis b'>2. r4",
    "<gis d'>4. <gis d'>8 <f d' bes'>2",             # triton ré-sol# (commun à mi7 et si♭7) | si♭/ré
    "<e c' a'>2. r4",                                # la m/do (quatrième degré mineur)
    "<e c'>4. <e c'>8 <e c' gis'>2",                 # do augmenté
    "<e b gis'>2 <cis' fis'>4 <cis' e'>4",           # mi/sol# | fa#m7/la
    "<a dis'>2 <a dis' fis'>4 <a dis' c''>4",        # si7 neuvième mineure
    "<e gis b'>4 <b e' gis'>4 <e gis b e'>2",        # mi
    "<e a c''>2 <e gis b'>2",                        # la m -> mi : cadence plagale mineure
    "<c f a'>2 <b e' gis'>2",                        # fa -> mi : cadence phrygienne (basse fa-mi)
    "<e gis c''>1",                                  # do augmenté
    "<e gis b'>1",                                   # mi
]
APRIME_V2 = ["e,2 e,2", "e,1", "d2 d2", "c1", "c1", "gis,2 a,2", "b,1", "e,1",
             "a,2 e,2", "f,2 e,2", "c1", "e,1"]
for i in range(12):
    V1[37 + i] = APRIME_V1[i]
    V2[37 + i] = APRIME_V2[i]
V1[37] = dyn(V1[37], "\\f")
V1[45] = dyn(V1[45], "\\ff")
V1[47] = dyn(V1[47], "\\>")
V1[48] = dyn(V1[48], "\\mp")

# ---------------------------------------------------------------- Coda (49-52) : le phare, puis mi majeur
V1[49] = BEACON.replace("r4", "r4\\p", 1)
V1[50] = BEACON
V1[51] = BEACON.replace("r4", "r4\\pp", 1)
V1[52] = "<e, b, e gis b e'>1\\arpeggio\\fermata"
V2.update({49: "e,1", 50: "e,1", 51: "e,1", 52: "s1"})
V1[52] = dyn(V1[52], "\\ppp")

# nuances et soufflets de la voix supérieure au-dessus de la portée
for _b in V1:
    V1[_b] = re.sub(r"(?<![\^_])\\(fff|ppp|pp|mp|mf|ff|sfz|p|f|<|>)(?![a-zA-Z])", r"^\\\1", V1[_b])

# ---------------------------------------------------------------- harmonie prévue (pour la relecture)
PLAN = {
    5: ("mi m", "do/mi"), 6: ("mi m", "sol/ré"), 7: ("si♭", "si♭"), 8: ("la m/do", "la m/do"),
    9: ("la♭/do", "la♭/do"), 10: ("sol/si", "fa#ø7/la"), 11: ("si7", "si7♭9"), 12: ("mi m", "mi m"),
    37: ("mi", "mi aug"), 38: ("mi", "mi"), 39: ("triton ré-sol#", "si♭/ré"), 40: ("la m/do", "la m/do"),
    41: ("do", "do aug"), 42: ("mi/sol#", "fa#m7/la"), 43: ("si7", "si7♭9"), 44: ("mi", "mi"),
    45: ("la m", "mi"), 46: ("fa", "mi"), 47: ("do aug", "do aug"), 48: ("mi", "mi"),
}
