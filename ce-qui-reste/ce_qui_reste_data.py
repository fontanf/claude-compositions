"""« Ce qui reste » pour orchestre à plectres -- notes en notation LilyPond absolue (hauteurs réelles).

Un thème est énoncé, puis résumé de plus en plus : ses notes principales, une note par mesure,
son rythme seul, un seul geste. À partir de ce qui reste, une nouvelle mélodie se reconstruit.
"""
import re

TITLE = "Ce qui reste"
SUBTITLE = "pour orchestre à plectres"
KEY = "\\key d \\major"

NBARS = 48
METER = {b: (1, "\\time 4/4") for b in range(1, 31)}
METER.update({b: (3 / 4, "\\time 3/4") for b in range(31, NBARS + 1)})

TEMPO = {b: 66 for b in range(1, 31)}
TEMPO[30] = 45  # silence avec point d'orgue
TEMPO.update({b: 72 for b in range(31, NBARS + 1)})
TEMPO.update({47: 60, 48: 50})


def section(title):
    return f'\\mark \\markup \\box "{title}"'


_X = "\\once \\override Score.MetronomeMark.X-offset = #4 "
MARKS = {
    1: '\\tempo "Calme, chantant" 4 = 66 ' + section("I. Le souvenir"),
    9: section("II. Résumé"),
    17: section("III. Une note par mesure"),
    25: section("IV. Le rythme seul"),
    29: section("V. Un geste"),
    31: _X + '\\tempo "Reconstruction" 4 = 72 ' + section("VI. Ce qui revient"),
}
TEXTS = {17: "sans trémolo, laisser vibrer", 25: "cordes étouffées", 47: "rit."}
BARLINES = {8: "||", 16: "||", 24: "||", 28: "||", 30: "||", 48: "|."}


def dyn(s, mark):
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def T(s):
    """trémolo sur les noires et valeurs plus longues"""
    return re.sub(r"(?<=[a-z',>])([124]\.?)(?=[\s~\\-]|$)", r"\1:32", s)


def GA8(b, x, y, z):
    """arpège de guitare à 4/4"""
    return f"{b}8 {x}8 {y}8 {x}8 {z}8 {x}8 {y}8 {x}8"


def GL(b, x, y):
    """berceuse de guitare à 3/4"""
    return f"{b}8 {x}8 {y}8 {x}8 {y}8 {x}8"


M1, M2, MA, GT = {}, {}, {}, {}
for v in (M1, M2, MA, GT):
    for b in range(1, NBARS + 1):
        v[b] = "R1" if METER[b][0] == 1 else "R2."

# ---------------------------------------------------------------- I. Le souvenir (1-8) : le thème entier
THEME = [
    "a'4 d'4 e'8 fis'8 a'4",      # la quinte descendante la-ré : deux cordes à vide
    "b'2. a'8 fis'8",
    "e''4 a'4 b'8 cis''8 e''4",   # la même quinte, une corde plus haut (mi-la)
    "fis''2. e''8 cis''8",
    "d''4 g'4 a'8 b'8 d''4",
    "e''2 d''4 b'4",
    "a'4 d'4 fis'4 e'4",
    "d'1",
]
GUIT = [("d", "a", "d'", "e'"), ("b,", "fis", "b", "d'"), ("a,", "e", "a", "b"), ("fis,", "cis", "fis", "a"),
        ("g,", "b,", "d", "a"), ("e,", "b,", "fis", "g"), ("a,", "d", "a", "fis'"), ("d", "a", "d'", "e'")]
CHORD = ["<d a d' e'>", "<b, fis b d'>", "<a, e a b>", "<fis, cis fis a>",
         "<g, b, d a>", "<e, b, fis g>", "<a, d a fis'>", "<d a d' e'>"]
ROOTS = ["d", "b,", "a,", "fis", "g,", "e", "a,", "d"]
FIFTHS = ["<d a>", "<b, fis>", "<a, e>", "<fis cis'>", "<g, d>", "<e b>", "<a, e>", "<d a>"]
M2_PAD = ["fis'", "d'", "cis'", "cis'", "d'", "b", "a'", "fis'"]
for i in range(8):
    M1[1 + i] = T(THEME[i])
    M2[1 + i] = f"{M2_PAD[i]}1:32"
    MA[1 + i] = f"{FIFTHS[i]}1:32"
    GT[1 + i] = GA8(*GUIT[i])
M1[1] = dyn(M1[1], "\\mf")
M2[1] = dyn(M2[1], "\\p")
MA[1] = dyn(MA[1], "\\p")
GT[1] = dyn(GT[1], "\\mp")

# ---------------------------------------------------------------- II. Résumé (9-16) : les notes des temps 1 et 3
SUMMARY = ["a'2 e'2", "b'1", "e''2 b'2", "fis''1", "d''2 a'2", "e''2 d''2", "a'2 fis'2", "d'1"]
for i in range(8):
    M1[9 + i] = T(SUMMARY[i])
    MA[9 + i] = f"{ROOTS[i]}1:32"
    GT[9 + i] = f"{CHORD[i]}1"
M1[9] = dyn(M1[9], "\\p")
MA[9] = dyn(MA[9], "\\pp")
GT[9] = dyn(GT[9], "\\p")

# ---------------------------------------------------------------- III. Une note par mesure (17-24)
# le squelette du thème, dispersé entre les pupitres, pincé une seule fois et laissé s'éteindre
SKELETON = [(M1, "a'"), (M2, "b'"), (MA, "e'"), (GT, "fis'"), (M1, "d''"), (M2, "e''"), (MA, "a"), (M1, "d'")]
for i, (v, p) in enumerate(SKELETON):
    v[17 + i] = f"{p}1"
for i in (0, 2, 4, 6):
    if GT[17 + i] == "R1":
        GT[17 + i] = f"{ROOTS[i]}1"
M1[17] = dyn(M1[17], "\\p")
M2[18] = dyn(M2[18], "\\p")
MA[19] = dyn(MA[19], "\\p")
GT[17] = dyn(GT[17], "\\pp")
GT[20] = dyn(GT[20], "\\p")
M1[24] = dyn(M1[24], "\\pp")

# ---------------------------------------------------------------- IV. Le rythme seul (25-28)
# le rythme des huit mesures du thème, deux fois plus vite, sur cordes étouffées (sans hauteur)
RHYTHM = ["8 8 16 16 8 4. 16 16", "8 8 16 16 8 4. 16 16", "8 8 16 16 8 4 8 8", "8 8 8 8 2"]
MUTED = {"M1": "b'", "M2": "g'", "MA": "d'", "GT": "g"}
for name, v in (("M1", M1), ("M2", M2), ("MA", MA), ("GT", GT)):
    for i, r in enumerate(RHYTHM):
        v[25 + i] = " ".join(MUTED[name] + d for d in r.split())
    v[25] = "\\xNotesOn " + dyn(v[25], "\\p")
    v[27] = dyn(v[27], "\\pp")
    v[28] = v[28] + " \\xNotesOff"

# ---------------------------------------------------------------- V. Un geste (29-30) : la quinte la-ré, cordes à vide
M1[29] = "a'2\\pp\\open d'2\\open"
for v in (M1, M2, MA, GT):
    v[30] = "R1\\fermata"

# ---------------------------------------------------------------- VI. Ce qui revient (31-48)
# la mélodie reconstruite : la quinte monte au lieu de descendre, puis la ligne redescend par degrés ;
# elle passe par toutes les notes du squelette (la, si, mi, fa#, ré, mi, la, ré)
NEW = ["a2 e'4", "d'4 cis'4 b4", "e'2 b'4", "a'4 g'4 fis'4", "d'2 a'4", "g'4 fis'4 e'4", "a2 e'4", "d'2."]
LULL = [("d", "a", "e'"), ("e", "b", "d'"), ("fis", "cis'", "e'"), ("g", "b", "fis'"),
        ("a", "d'", "e'"), ("b", "d'", "fis'"), ("cis", "e'", "a"), ("d", "a", "fis'")]
OLD = ["a", "b", "e'", "fis'", "d'", "e'", "a", "d'"]           # l'ancien squelette
BASS6 = ["d", "e", "fis", "g", "a", "b", "cis", "d"]
for i in range(8):
    MA[31 + i] = NEW[i] if i < 4 else T(NEW[i])   # d'abord pincée, puis tenue en trémolo
    GT[31 + i] = GL(*LULL[i])
    GT[39 + i] = GL(*LULL[i])
    M1[39 + i] = T(re.sub(r"([a-g](?:is|es)*)([',]*)(?=\d)", lambda m: m.group(1) + m.group(2) + "'", NEW[i]))
    M2[39 + i] = f"r4 {OLD[i]}2:32"       # le vieux souvenir arrive avec un temps de retard
    MA[39 + i] = f"{BASS6[i]}2.:32"
M2.update({35: "e'2.:32\\pp", 36: "d'2.:32", 37: "e'2.:32", 38: "fis'2.:32"})
MA[31] = dyn(MA[31], "\\p")
GT[31] = dyn(GT[31], "\\pp")
M1[39] = dyn(M1[39], "\\mf\\<")
M2[39] = dyn(M2[39], "\\mp")
MA[39] = dyn(MA[39], "\\mp")
GT[39] = dyn(GT[39], "\\mf")
M1[43] = dyn(M1[43], "\\f")
M1[45] = dyn(M1[45], "\\>")
M1[46] = dyn(M1[46], "\\mp")

# fin : un accord tenu qui s'éteint, puis il ne reste que le geste
M1[47] = "e''2.:32\\pp\\>"
M2[47] = "fis'2.:32\\pp"
MA[47] = "<d a>2.:32\\pp"
GT[47] = "<d a d' fis'>2.\\pp"
M1[48] = "a'4\\ppp\\open d'2\\open\\fermata"
for v in (M2, MA, GT):
    v[48] = "R2.\\fermata"

PARTS = [  # (identifiant, nom, nom court, clé, musique, son)
    ("mandolineI", "Mandoline 1", "Md. 1", "treble", M1, "mandoline"),
    ("mandolineII", "Mandoline 2", "Md. 2", "treble", M2, "mandoline"),
    ("mandole", "Mandole ténor", "Mdl.", "treble", MA, "mandole"),
    ("guitare", "Guitare", "Gt.", "treble_8", GT, "guitare"),
]
TRANSPOSITION = {"mandole": "c"}  # la mandole ténor sonne une octave plus bas que l'écrit

# ---------------------------------------------------------------- harmonie prévue (vérification)
H1 = ["d a e fis", "b d fis a e", "a cis e b", "fis a cis e", "g b d a", "e g b d fis", "a d fis e", "d a e fis"]
H6 = ["d a e", "e g b d cis", "fis a cis e b", "g b d fis a", "a d e", "b d fis g e", "cis e a", "d fis a e"]
CHORDS = {}
for i in range(8):
    for base in (1, 9, 17):
        CHORDS[base + i] = [(0, H1[i])]
    for base in (31, 39):
        CHORDS[base + i] = [(0, H6[i])]
CHORDS.update({29: [(0, "a d")], 47: [(0, "d fis a e")], 48: [(0, "a d")]})
