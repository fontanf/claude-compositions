"""« Lanternes », chaconne pour orchestre à plectres -- notes en notation LilyPond absolue (hauteurs réelles).

Un ground de 8 mesures (ré – do – si♭ – la – sol – mi – la – la) et neuf énoncés :
thème, sept variations, coda.
"""

TITLE = "Lanternes"
SUBTITLE = "chaconne pour orchestre à plectres"
KEY = "\\key d \\minor"

NBARS = 72
METER = {b: (3 / 4, "\\time 3/4") for b in range(1, NBARS + 1)}


def var(n):
    return range(8 * n + 1, 8 * n + 9)


TEMPO = {}
for n, q in enumerate([69, 69, 69, 84, 92, 66, 76, 76, 58]):
    for b in var(n):
        TEMPO[b] = q
TEMPO.update({63: 70, 64: 64, 71: 52, 72: 46})

_X = "\\once \\override Score.MetronomeMark.X-offset = #3 "
MARKS = {
    1: '\\tempo "Andante, con nostalgia" 4 = 69 \\mark \\markup \\box "Thème"',
    9: '\\mark \\markup \\box "Var. 1"',
    17: '\\mark \\markup \\box "Var. 2"',
    25: _X + '\\tempo "Più mosso, leggero" 4 = 84 \\mark \\markup \\box "Var. 3"',
    33: _X + '\\tempo "Con slancio" 4 = 92 \\mark \\markup \\box "Var. 4"',
    41: _X + '\\tempo "Tranquillo, dolce" 4 = 66 \\mark \\markup \\box "Var. 5"',
    49: _X + '\\tempo "Appassionato" 4 = 76 \\mark \\markup \\box "Var. 6"',
    57: '\\mark \\markup \\box "Var. 7"',
    65: _X + '\\tempo "Lento, lontano" 4 = 58 \\mark \\markup \\box "Coda"',
}
TEXTS = {63: "allargando", 71: "rit."}
BARLINES = {24: "||", 32: "||", 40: "||", 48: "||", 64: "||", 72: "|."}

# ---------------------------------------------------------------- utilitaires


def dyn(s, mark):
    import re
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def GA(b, x, y, z):
    """arpège de guitare en croches : basse, puis accord autour d'une note pivot"""
    return f"{b}8 {x}8 {y}8 {x}8 {z}8 {x}8"


def MARP(a, b, c, d):
    return f"{a}8 {b}8 {c}8 {b}8 {d}8 {b}8"


def ARP16(a, b, c, d):
    return f"{a}16 {b}16 {c}16 {d}16 {c}16 {b}16 " * 2


def STR8(ch, acc=(0,)):
    return " ".join(f"{ch}8" + ("->" if i in acc else "") for i in range(6))


def STR3(ch):
    return f"{ch}4-> {ch}8 {ch}8 {ch}8 {ch}8"


def T(s):
    """trémolo sur les noires et valeurs plus longues d'une mesure"""
    import re
    return re.sub(r"(?<=[a-z',>])([124]\.?)(?=[\s~\\]|$)", r"\1:32", s)


FC = "<c f a c' f'>"  # fa/do : réharmonisation de la 2e mesure sous la mélodie
GROUND = ["d", "c", "bes,", "a,", "g,", "e,", "a,", "a,"]
# accords de guitare (positions ouvertes ou barrés simples)
GCH = ["<d a d' f'>", "<c e g c' e'>", "<bes, f bes d' f'>", "<a, e a cis' e'>",
       "<g, d g bes d' g'>", "<e, bes, d g>", "<a, e g d' e'>", "<a, e g cis' e'>"]

MELODY = [  # la mélodie de la variation 1
    "a'4 d''4 e''4", "f''2 e''4", "d''4 f''4 a''4", "g''4. f''8 e''8 cis''8",
    "d''4 g''4 a''4", "bes''2 a''4", "g''4 e''4 d''4", "cis''2.",
]


def down8(s):
    """transpose une ligne d'une octave vers le bas"""
    import re
    def f(m):
        p, oct_ = m.group(1), m.group(2)
        if oct_.startswith("'"):
            oct_ = oct_[1:]
        else:
            oct_ += ","
        return p + oct_
    return re.sub(r"(?<![a-z\\])([a-g](?:is|es)*)([',]*)(?=\d)", f, s)


R = "R2."
M1, M2, MA, GT = {}, {}, {}, {}

# ---------------------------------------------------------------- Thème (1-8) : guitare seule
V0 = ["<a d' f'>", "<g c' e'>", "<f a d'>", "<e a cis'>", "<d g bes>", "<bes, d g>", "<e a d'>", "<e g cis'>"]
for i, b in enumerate(var(0)):
    GT[b] = f"{GROUND[i]}4 {V0[i]}2"
    M1[b] = M2[b] = MA[b] = R
GT[1] = dyn(GT[1], "\\mf")

# ---------------------------------------------------------------- Var. 1 (9-16) : la mélodie
V1_GA = [("d", "a", "f'", "e'"), ("c", "f", "a", "c'"), ("bes,", "f", "a", "d'"), ("a,", "e", "cis'", "g"),
         ("g,", "d", "bes", "f"), ("e,", "bes,", "g", "d'"), ("a,", "e", "d'", "g"), ("a,", "e", "cis'", "g")]
V1_M2 = ["a'", "a'", "a'", "a'", "bes'", "bes'", "a'", "g'"]
V1_MA = ["f", "c", "d", "cis", "d", "d", "e", "cis"]
for i, b in enumerate(var(1)):
    M1[b] = T(MELODY[i])
    M2[b] = f"{V1_M2[i]}2.:32"
    MA[b] = f"{V1_MA[i]}2.:32"
    GT[b] = GA(*V1_GA[i])
M1[9] = dyn(M1[9], "\\mp")
M2[9] = dyn(M2[9], "\\pp")
MA[9] = dyn(MA[9], "\\pp")
GT[9] = dyn(GT[9], "\\p")

# ---------------------------------------------------------------- Var. 2 (17-24) : la mélodie à la mandole
V2_M1 = ["f''", "g''", "a''", "a''", "bes''", "g''", "a''", "g''"]
V2_M2 = [("a'", "d''", "f''", "e''"), ("a'", "c''", "f''", "c''"), ("f'", "bes'", "d''", "a'"),
         ("e'", "a'", "cis''", "e''"), ("bes'", "d''", "g''", "f''"), ("d'", "g'", "bes'", "e''"),
         ("e'", "a'", "d''", "e''"), ("e'", "g'", "cis''", "e''")]
for i, b in enumerate(var(2)):
    MA[b] = T(down8(MELODY[i]))
    M1[b] = f"{V2_M1[i]}2.:32"
    M2[b] = MARP(*V2_M2[i])
    GT[b] = f"{GROUND[i]}4 {V0[i] if i != 1 else '<a c\' f\'>'}2"
MA[17] = dyn(MA[17], "\\mf")
M1[17] = dyn(M1[17], "\\p")
M2[17] = dyn(M2[17], "\\mp")
GT[17] = dyn(GT[17], "\\mp")

# ---------------------------------------------------------------- Var. 3 (25-32) : leggero, dialogue
M1.update({
    25: "a''8-.\\mp f''8-. e''8-. f''8-. d''4-.", 26: "g''8-. e''8-. d''8-. e''8-. c''4-.",
    27: R, 28: R,
    29: "bes''8-. g''8-. f''8-. g''8-. d''4-.", 30: "bes''8-. g''8-. e''8-. g''8-. d''4-.",
    31: "a''8-. g''8-. e''8-. d''8-. e''4-.", 32: "cis'''8-. a''8-. g''8-. e''8-. cis''4-.",
})
M2.update({
    25: R, 26: R,
    27: "f''8-.\\mp d''8-. c''8-. d''8-. bes'4-.", 28: "e''8-. cis''8-. b'8-. cis''8-. a'4-.",
    29: "d''8-. bes'8-. a'8-. bes'8-. f'4-.", 30: "d''8-. bes'8-. g'8-. bes'8-. e'4-.",
    31: "e''4-. d''4-. a'4-.", 32: "e''8-. cis''8-. a'8-. g'8-. e'4-.",
})
V3_MA = ["d4-. f4-. a4-.", "c4-. e4-. g4-.", "bes,4-. d4-. f4-.", "a,4-. cis4-. e4-.",
         "g,4-. bes,4-. d4-.", "e4-. g4-. bes4-.", "a,4-. d4-. e4-.", "a,4-. cis4-. g4-."]
V3_GT = ["<d' f' a'>", "<c' e' g'>", "<d' f' a'>", "<cis' e' a'>",
         "<d' f' bes'>", "<d' g' bes'>", "<d' e' a'>", "<cis' e' g'>"]
for i, b in enumerate(var(3)):
    MA[b] = V3_MA[i]
    GT[b] = f"r4 {V3_GT[i]}4-. {V3_GT[i]}4-."
MA[25] = dyn(MA[25], "\\mp")
GT[25] = "r4\\p" + GT[25][2:]

# ---------------------------------------------------------------- Var. 4 (33-40) : hémioles
M1.update({
    33: "a''2:32\\f g''4:32~", 34: "g''4:32 e''2:32", 35: "f''2:32 e''4:32~", 36: "e''4:32 cis''2:32",
    37: "bes''2:32 a''4:32~", 38: "a''4:32 g''2:32", 39: "a''4:32\\< d'''4:32 e'''4:32",
    40: "cis'''2.:32\\ff",
})
M2.update({
    33: "f''2:32\\f e''4:32~", 34: "e''4:32 c''2:32", 35: "d''2:32 a'4:32~", 36: "a'4:32 a'2:32",
    37: "g''2:32 e''4:32~", 38: "e''4:32 d''2:32", 39: "e''4:32\\< a''4:32 g''4:32", 40: "g''2.:32\\ff",
})
MA.update({
    33: "<d a>2:32\\f <c e>4:32~", 34: "<c e>4:32 <c e>2:32",
    35: "<bes, d>2:32 <a, e>4:32~", 36: "<a, e>4:32 <a, e>2:32",
    37: "<g, bes>2:32 <e bes>4:32~", 38: "<e bes>4:32 <e bes>2:32",
    39: "<a, e>2.:32\\<", 40: "<a, e>2.:32\\ff",
})
for i, b in enumerate(var(4)):
    # accents en hémiole : 2 mesures à 3/4 = 3 groupes de 2 noires
    acc = (0, 4) if i % 2 == 0 else (2,)
    GT[b] = STR8(GCH[i], acc if i < 6 else (0, 2, 4))
GT[33] = dyn(GT[33], "\\f")
GT[39] = dyn(GT[39], "\\<")
GT[40] = dyn(GT[40], "\\ff")

# ---------------------------------------------------------------- Var. 5 (41-48) : le ground au dessus, basse ascendante
V5_GA = [("bes,", "f", "d'", "a"), ("c", "g", "a", "e'"), ("d", "f", "bes", "d'"), ("e", "a", "c'", "e'"),
         ("f", "c'", "a", "g'"), ("g", "c'", "e'", "g'"), ("a,", "e", "d'", "a"), ("a,", "e", "cis'", "g")]
V5_M1 = ["d'''", "c'''", "bes''", "a''", "g''", "e''", "a''", "a''"]
V5_M2 = ["f'", "g'", "d''", "c''", "a'", "g'", "a'", "g'"]
V5_MA = ["d'", "e'", "f'", "e'", "c'", "c'", "e'", "cis'"]
for i, b in enumerate(var(5)):
    M1[b] = f"{V5_M1[i]}2.:32"
    M2[b] = f"{V5_M2[i]}2.:32"
    MA[b] = f"{V5_MA[i]}2.:32"
    GT[b] = GA(*V5_GA[i])
M1[41] = dyn(M1[41], "\\p")
M2[41] = dyn(M2[41], "\\pp")
MA[41] = dyn(MA[41], "\\pp")
GT[41] = dyn(GT[41], "\\pp")

# ---------------------------------------------------------------- Var. 6 (49-56) : retour de la mélodie, tutti
V6_M2 = ["f'4 a'4 c''4", "a'2 a'4", "bes'4 d''4 d''4", "e''4. d''8 a'4",
         "bes'4 d''4 f''4", "g''2 e''4", "e''4 g'4 a'4", "g'2."]
V6_MA = ["f", "g", "a", "a", "d", "bes", "a", "cis"]
for i, b in enumerate(var(6)):
    M1[b] = T(MELODY[i])
    M2[b] = T(V6_M2[i])
    MA[b] = f"{V6_MA[i]}2.:32"
    GT[b] = STR3(GCH[i])
GT[50] = STR3(FC)
for v in (M1, M2, MA, GT):
    v[49] = dyn(v[49], "\\f")

# ---------------------------------------------------------------- Var. 7 (57-64) : superposition ground / mélodie / doubles croches
V7_M2 = [("a'", "d''", "f''", "a''"), ("a'", "c''", "f''", "a''"), ("f'", "bes'", "d''", "f''"),
         ("e'", "a'", "cis''", "e''"), ("d'", "g'", "bes'", "d''"), ("e'", "g'", "bes'", "d''"),
         ("e'", "a'", "d''", "e''")]
for i, b in enumerate(var(7)):
    M1[b] = f"{V5_M1[i]}2.:32"
    MA[b] = T(down8(MELODY[i]))
    GT[b] = STR3(GCH[i])
    if i < 7:
        M2[b] = ARP16(*V7_M2[i])
GT[58] = STR3(FC)
M1[57] = "d'''2.:32\\ff"
M1[64] = "a''2:32 r4"
M2[64] = "e'16 a'16 cis''16 e''16 g''16 e''16 cis''16 a'16 r4"
MA[64] = "cis'2:32 r4"
GT[64] = f"{GCH[7]}4-> {GCH[7]}4-> r4"
MA[57] = dyn(MA[57], "\\ff")
M2[57] = dyn(M2[57], "\\f")
GT[57] = dyn(GT[57], "\\ff")

# ---------------------------------------------------------------- Coda (65-72) : le ground se brise, ré majeur
M1.update({
    65: "a'4\\pp d''4 e''4", 66: "f''2:32 e''4:32", 67: R, 68: R,
    69: "d''4:32 g''4:32 a''4:32", 70: "bes''2:32 a''4:32", 71: "g''2.:32", 72: "fis''2.:32\\fermata",
})
M2.update({
    65: "f'2.:32\\ppp", 66: "a'2.:32", 67: "d'4:32\\pp f'4:32 a'4:32", 68: "g'4.:32 f'8:32 e'4:32",
    69: "bes'2.:32", 70: "g'2.:32", 71: "cis''2.:32", 72: "d''2.:32\\fermata",
})
for i, (n, b) in enumerate(zip(["d", "c", "bes,", "a,", "g,", "e", "a,", "d"], var(8))):
    MA[b] = f"{n}2.:32"
MA[65] = dyn(MA[65], "\\pp")
MA[72] += "\\fermata"
CODA_G = ["<f a d' e'>", "<f a c' e'>", "<d' f' a'>", "<e a cis'>", "<g bes d' e'>", "<g bes d'>", "<g cis' e'>",
          "<d a d' fis'>"]
for i, b in enumerate(var(8)):
    GT[b] = f"{CODA_G[i]}2."
GT[65] = dyn(GT[65], "\\pp")
GT[72] += "\\fermata"

PARTS = [  # (identifiant, nom, nom court, clé, musique, son)
    ("mandolineI", "Mandoline 1", "Md. 1", "treble", M1, "mandoline"),
    ("mandolineII", "Mandoline 2", "Md. 2", "treble", M2, "mandoline"),
    ("mandole", "Mandole ténor", "Mdl.", "treble", MA, "mandole"),
    ("guitare", "Guitare", "Gt.", "treble_8", GT, "guitare"),
]
TRANSPOSITION = {"mandole": "c"}  # la mandole ténor sonne une octave plus bas que l'écrit

# ---------------------------------------------------------------- harmonie prévue (vérification)
H0 = ["d f a e", "c e g d", "bes d f a c", "a cis e g bes b", "g bes d f a e", "e g bes d", "a d e g", "a cis e g bes"]
H5 = ["bes d f a", "c e g a", "d f bes", "e a c", "f a c g", "g c e", "a d e", "a cis e g"]
H8 = ["d f a e", "c e g d", "bes d f a", "a cis e", "g bes d e a", "e g bes d", "a cis e g", "d fis a e"]
CHORDS = {}
for n in range(9):
    h = {5: H5, 8: H8}.get(n, H0)
    for i, b in enumerate(var(n)):
        CHORDS[b] = [(0, h[i])]
for b in (10, 18, 50, 58, 66):
    CHORDS[b] = [(0, "c f a e g")]
for b, nxt in ((33, "c e g"), (35, "a cis e"), (37, "e g bes d a")):  # hémioles : anticipations
    CHORDS[b].append((4, CHORDS[b][0][1] + " " + nxt))
