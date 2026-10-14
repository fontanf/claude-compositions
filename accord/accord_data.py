"""« Accord » pour guitare seule -- une pièce pensée en sonorités. Notes en hauteurs réelles.

Une note (mi4) jouée sur plusieurs cordes ; ses voisines qui s'écartent jusqu'à l'accord des cordes à vide
(une pile de quartes) ; cette pile rejouée en harmoniques ; le corps de l'instrument ; la note seule.

Conventions : « e'\\2 » impose la corde ; \\ord \\pont \\tasto \\pizz \\tamb changent le mode de jeu ;
\\xNotesOn ... \\xNotesOff : golpe (frappe sur la table).
"""
import re
from fractions import Fraction as F

TITLE = "Accord"
SUBTITLE = "pour guitare"
KEY = ""
TUNING = [40, 45, 50, 55, 59, 64]
WINDOW = F(1, 2)

NBARS = 36
METER = {b: (1, "\\time 4/4") for b in range(1, NBARS + 1)}
TEMPO = {b: 60 for b in range(1, NBARS + 1)}
TEMPO.update({b: 54 for b in range(13, 21)})
TEMPO.update({b: 96 for b in range(21, 31)})
TEMPO.update({31: 60, 32: 40, 33: 50, 34: 50, 35: 46, 36: 40})

MARKS = {
    1: '\\accidentalStyle Score.modern \\tempo "Lento, sospeso" 4 = 60 \\mark \\markup \\box "I. Une note"',
    7: '\\mark \\markup \\box "II. Diffraction"',
    13: '\\tempo 4 = 54 \\mark \\markup \\box "III. Halo"',
    21: '\\tempo "Secco, energico" 4 = 96 \\mark \\markup \\box "IV. Matière"',
    33: '\\tempo "Lento" 4 = 50 \\mark \\markup \\box "V. Une note"',
}
TEXTS = {7: "laisser vibrer chaque mesure", 13: "harm. XII", 15: "harm. VII", 17: "harm. V et IV",
         19: "harm. IV", 21: "golpe : frappe sur la table", 25: "rasgueado"}
BARLINES = {6: "||", 12: "||", 20: "||", 32: "||", 36: "|."}

# « ligne » : chaque attaque est vérifiée avec ce qui sonne ; « anneau » : toute la mesure résonne,
# la main gauche tient une seule forme
MODE = {b: "ligne" for b in range(1, NBARS + 1)}
for b in range(7, 13):
    MODE[b] = "anneau"


def dyn(s, mark):
    first = re.match(r"\\\S+ |<[^>]+>\S*|\S+", s).group(0).strip()
    if first.startswith("\\"):
        rest = s[len(first) + 1:]
        return first + " " + dyn(rest, mark)
    return f"{first}{mark}{s[len(first):]}"


def H(p, s):
    """harmonique naturelle (hauteur réelle) sur la corde s"""
    return f"<{p}\\harmonic\\{s}>"


V1, V2 = {}, {}

# ---------------------------------------------------------------- I. Une note (1-6)
V1.update({
    1: "\\ord e'2\\1 e'2\\2",                                   # corde à vide, puis case V
    2: "e'2\\3 e'2\\4",                                         # case IX, puis case XIV : de plus en plus sombre
    3: "<e'\\1 e'\\2>1",                                        # la même note sur deux cordes : elle bat
    4: "\\pont <e'\\1 e'\\2 e'\\3>2 \\tasto <e'\\1 e'\\2 e'\\3>2",   # trois cordes, deux timbres
    5: "\\ord <e'\\2 f'\\1>1",                                  # la voisine du dessus
    6: "<dis'\\3 e'\\1 f'\\2>1",                                # les deux voisines
})
V1[1] = dyn(V1[1], "\\p")
V1[4] = V1[4].replace("<e'\\1 e'\\2 e'\\3>2 ", "<e'\\1 e'\\2 e'\\3>2\\p ", 1)
V1[6] = dyn(V1[6], "\\mp")

# ---------------------------------------------------------------- II. Diffraction (7-12)
# les voisines s'écartent : demi-tons, tons, tierces, quartes, puis les cordes à vide (l'accord de la guitare)
V1.update({
    7: "dis'8.\\3 e'16 f'4\\2 e'8 dis'8\\3 f'4\\2",
    8: "c'8\\4 d'8\\3 fis'4\\2 e'8 c'8\\4 d'8.\\3 fis'16\\2",
    9: "d'16\\4 e'16 fis'8\\3 gis'4\\2 e'8 d'8\\4 gis'8\\2 fis'8\\3",
    10: "c'8\\4 e'8\\3 gis'8\\2 b'4\\1 gis'8\\2 e'8\\3 c'8\\4",
    11: "a8\\4 d'8\\3 g'8\\2 c''8\\1 g'8\\2 d'8\\3 a4\\4",
    12: "e,8 a,8 d8 g8 b8 e'8 r4",
})
V1[7] = dyn(V1[7], "\\p")
V1[9] = dyn(V1[9], "\\<")
V1[11] = dyn(V1[11], "\\mf")
V1[12] = dyn(V1[12], "\\>")

# ---------------------------------------------------------------- III. Halo (13-20) : les quartes des cordes, en harmoniques
XII = [("e", 6), ("a", 5), ("d'", 4), ("g'", 3), ("b'", 2), ("e''", 1)]
VII = [("b", 6), ("e'", 5), ("a'", 4), ("d''", 3), ("fis''", 2), ("b''", 1)]
V = [("e'", 6), ("a'", 5), ("d''", 4), ("g''", 3), ("b''", 2), ("e'''", 1)]
IV = [("gis'", 6), ("cis''", 5), ("fis''", 4), ("b''", 3), ("dis'''", 2), ("gis'''", 1)]
V1.update({
    13: " ".join(f"{H(p, s)}4" for p, s in XII[:4]),
    14: " ".join(f"{H(p, s)}4" for p, s in XII[4:]) + " r2",
    15: " ".join(f"{H(p, s)}4" for p, s in VII[::-1][:4]),
    16: " ".join(f"{H(p, s)}4" for p, s in VII[::-1][4:]) + " r2",
    17: " ".join(f"{H(p, s)}8" for pair in zip(V[:4], IV[:4]) for p, s in pair),
    18: " ".join(f"{H(p, s)}8" for pair in zip(V[4:], IV[4:]) for p, s in pair) + " r2",
    19: " ".join(f"{H(p, s)}4" for p, s in IV[:4]),
    20: f"{H(*IV[4])}4 {H(*IV[5])}2. ",
})
V1[13] = dyn(V1[13], "\\p")
V1[19] = dyn(V1[19], "\\pp")
V1[20] = V1[20].strip()

# ---------------------------------------------------------------- IV. Matière (21-32)
CL = "<dis'\\3 e'\\1 f'\\2>"                     # l'agrégat de la note et de ses voisines
OPEN = "<e, a, d g b e'>"                        # l'accord des cordes à vide


def tuning_at(n):
    """l'accord de la guitare barré à la case n"""
    names = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
    out = []
    for p in (40, 45, 50, 55, 59, 64):
        o, pc = divmod(p + n, 12)
        o -= 4
        out.append(names[pc] + ("'" * o if o > 0 else "," * -o))
    return "<" + " ".join(out) + ">"


V1.update({
    21: f"\\pizz {CL}16-> r16 {CL}16 r16 r8 {CL}16-> r16 r16 {CL}16 r8 {CL}8-> r8",
    22: f"{CL}16-> r16 r16 {CL}16 r8 {CL}16-> {CL}16 r8 {CL}8-> r16 {CL}16 r8",
    23: f"\\tamb {OPEN}4 \\pizz {CL}8 r8 \\tamb {OPEN}8 r8 \\pizz {CL}16 r16 {CL}8",
    24: f"\\tamb {OPEN}4 \\pizz {CL}8 {CL}8 \\tamb {OPEN}8 r8 \\pizz {CL}16 {CL}16 {CL}8->",
})
for b, n in zip(range(25, 29), [1, 2, 3, 5]):
    c = tuning_at(n)
    V1[b] = (("\\ord " if b == 25 else "") +
             f"{c}8\\arpeggio-> {c}8 {c}16 {c}16 {c}8\\arpeggio-> {c}8 r8 {c}8\\arpeggio-> {c}8")
V1[29] = f"{OPEN}16\\arpeggio-> {OPEN}16 {OPEN}16 {OPEN}16 " * 4
V1[30] = f"{OPEN}2\\arpeggio-> r2"
V1[31] = "R1"
V1[32] = "R1\\fermata"
V1[21] = V1[21].replace(f"{CL}16->", f"{CL}16->\\mf", 1)
V1[25] = V1[25].replace("\\arpeggio->", "\\arpeggio->\\f", 1)
V1[29] = V1[29].replace("\\arpeggio->", "\\arpeggio->\\fff", 1)
V2.update({b: "s1" for b in range(1, NBARS + 1)})
GOLPE = "\\xNotesOn c4 r4 c4 r4 \\xNotesOff"
V2.update({21: GOLPE, 22: "\\xNotesOn c4 r8 c8 r4 c4 \\xNotesOff", 23: "s1", 24: "s1",
           31: "\\xNotesOn c4 r2. \\xNotesOff", 32: "s1"})
V2[21] = V2[21].replace("c4", "c4\\mf", 1)
V2[31] = V2[31].replace("c4", "c4\\p", 1)

# ---------------------------------------------------------------- V. Une note (33-36)
V1.update({
    33: f"{H('e', 1).replace('<e', '<e' + chr(39) + chr(39))}1",   # mi5 en harmonique (case XII, 1re corde)
    34: "<e'\\1 e'\\2>1",
    35: "\\tasto e'1\\4",                                           # le mi le plus sombre : case XIV, 4e corde
    36: "r1\\fermata",
})
V1[33] = dyn(V1[33], "\\p")
V1[35] = dyn(V1[35], "\\pp")

for _b in V1:
    V1[_b] = re.sub(r"(?<![\^_])\\(fff|ppp|pp|mp|mf|ff|sfz|p|f|<|>)(?![a-zA-Z])", r"^\\\1", V1[_b])

PLAN = {}
