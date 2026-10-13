"""« Engrenages » pour orchestre à plectres -- pièce sérielle (douze sons), notes en hauteurs réelles.

Série P0 : mi fa do♯ | si si♭ ré | la la♭ do | fa♯ sol mi♭
quatre cellules de même type (demi-ton + tierce majeure), deux à deux en miroir.
"""
import re

TITLE = "Engrenages"
SUBTITLE = "pour orchestre à plectres"
KEY = ""  # pas d'armure : musique atonale

NBARS = 70
FAST = (5 / 8, "\\time 2,3 5/8")
SLOW = (5 / 4, "\\time 2,3 5/4")
METER = {b: FAST for b in range(1, NBARS + 1)}
for b in range(37, 45):
    METER[b] = SLOW

TEMPO = {b: 112 for b in range(1, NBARS + 1)}
TEMPO.update({b: 60 for b in range(37, 45)})
TEMPO.update({44: 54, 69: 104, 70: 96})

_X = "\\once \\override Score.MetronomeMark.X-offset = #3 "
MARKS = {
    1: '\\accidentalStyle Score.modern \\tempo "Meccanico" 4 = 112',
    5: "\\mark \\default",
    21: "\\mark \\default",
    37: _X + '\\tempo "Lento, sospeso" 4 = 60 \\mark \\default',
    45: _X + '\\tempo "Tempo I" 4 = 112 \\mark \\default',
    57: "\\mark \\default",
    65: "\\mark \\default",
}
TEXTS = {44: "rit."}
BARLINES = {36: "||", 44: "||", 70: "|."}


def dyn(s, mark):
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def gear(cycle, bars, phase=0):
    """ostinato de croches de période len(cycle), découpé en mesures de 5 croches"""
    out = {}
    for b in bars:
        out[b] = " ".join(cycle[(phase + k) % len(cycle)] for k in range(5))
        phase += 5
    return out


def skip(voice, bar, pos):
    """une dent qui saute : remplace la croche n° pos d'un engrenage par un silence"""
    toks = voice[bar].split(" ")
    toks[pos] = "r8" + "".join(x for x in ("\\pp", "\\p", "\\mf") if toks[pos].endswith(x))
    voice[bar] = " ".join(toks)


def T(s):
    """trémolo sur les noires et valeurs plus longues"""
    return re.sub(r"(?<=[a-z',>])([124]\.?)(?=[\s~\\-]|$)", r"\1:32", s)


def W(p, trem=True):
    """note tenue sur une mesure à 5/4"""
    return f"{p}2:32~ {p}2.:32" if trem else f"{p}2 {p}2."


# les engrenages : 5, 3 et 4 croches -> ne coïncident que toutes les 60 croches
G1 = ["bes,8->", "e8", "a8->", "ees'8", "a8"]      # guitare
G2 = ["g8-.", "cis'8-.", "ees'8-."]                  # mandole
G2_HI = ["g'8-.", "cis''8-.", "ees''8-."]            # même engrenage, à la mandoline
G3 = ["c''8-.", "b'8-.", "r8", "f''8-."]            # mandoline 2
G1_CH = "<bes, e a ees'>"

# le thème : quatre énoncés de la série
PHRASE1 = ["e'8 f'8 cis''4.", "b'8 bes'8 d''4.", "a'8 aes'8 c''4.", "fis'8 g'8 ees''4."]      # P0
PHRASE2 = ["ees''4. g'8 fis'8", "c''4. aes'8 a'8", "d''4. bes'8 b'8", "cis''4. f'8 e'8"]      # R0
PHRASE3 = ["e''8 ees''8 g''4.", "a'8 bes'8 fis''4.", "b'8 c''8 aes''4.", "d''8 cis''8 f''4."]  # I0
PHRASE4 = ["b'16 c''16 aes''8 fis''16 f''16 a''4", "e''16 ees''16 g''8 cis''16 d''16 bes''4",  # P7
           "e''8 f''8 cis'''4.", "cis'''4.~ cis'''4"]
I6 = ["bes'8 a'8 cis''4.", "ees'8 e'8 c''4.", "f'8 fis'8 d''4.", "aes'8 g'8 b'4."]


def shift(s, octaves):
    """transpose une ligne de n octaves"""
    def f(m):
        p, o = m.group(1), m.group(2)
        n = o.count("'") - o.count(",") + octaves
        return p + ("'" * n if n > 0 else "," * -n)
    return re.sub(r"(?<![a-z\\])([a-g](?:is|es)*)([',]*)(?=\d)", f, s)


def tp(s, semis):
    """transpose une ligne de quelques demi-tons (orthographe en bémols/dièses simple)"""
    names = ["c", "cis", "d", "ees", "e", "f", "fis", "g", "aes", "a", "bes", "b"]
    steps = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
    def f(m):
        p, o = m.group(1), m.group(2)
        n = steps[p[0]] + p.count("is") - p.count("es") + 12 * (o.count("'") - o.count(",")) + semis
        octv, pc = divmod(n, 12)
        return names[pc] + ("'" * octv if octv > 0 else "," * -octv)
    return re.sub(r"(?<![a-z\\])([a-g](?:is|es)*)([',]*)(?=\d)", f, s)


R = "R8*5"
M1, M2, MA, GT = {}, {}, {}, {}
for v in (M1, M2, MA, GT):
    for b in range(1, NBARS + 1):
        v[b] = R if METER[b] == FAST else "R4*5"

# ---------------------------------------------------------------- Introduction (1-4) et A (5-20)
GT.update(gear(G1, range(1, 21)))
MA.update(gear(G2, range(2, 21)))
M2.update(gear(G3, range(3, 21)))
GT[1] = dyn(GT[1], "\\mp")
MA[2] = dyn(MA[2], "\\pp")
M2[3] = dyn(M2[3], "\\pp")
for i, s in enumerate(PHRASE1 + PHRASE2 + PHRASE3 + PHRASE4):
    M1[5 + i] = T(s)
M1[5] = dyn(M1[5], "\\mf")
M1[17] = dyn(M1[17], "\\<")
M1[19] = dyn(M1[19], "\\f")

# ---------------------------------------------------------------- B (21-36) : le thème à la mandole, puis canon au triton
for i, s in enumerate(PHRASE1 + PHRASE2):
    MA[21 + i] = T(shift(s, -1))
MA[21] = dyn(MA[21], "\\mf")
M1.update(gear(G2_HI, range(21, 29)))
M1[21] = dyn(M1[21], "\\p")
M2.update(gear(G3, range(21, 30), phase=0))
M2[21] = dyn(M2[21], "\\p")
GT.update(gear(G1, range(21, 37)))
GT[21] = dyn(GT[21], "\\p")
for i, s in enumerate(PHRASE1 + PHRASE3):
    M1[29 + i] = T(shift(s, 1) if i < 4 else s)
M1[29] = dyn(M1[29], "\\mf")
for i, s in enumerate([tp(x, -6) for x in PHRASE1] + I6[:3]):
    M2[30 + i] = T(s)
M2[30] = dyn(M2[30], "\\mf")
MA.update(gear(G2, range(29, 37)))
MA[29] = dyn(MA[29], "\\p")

# quelques dents sautées pour éviter des accords parfaits fortuits entre engrenages
skip(M2, 3, 1)
skip(M2, 8, 3)
skip(M2, 18, 1)
skip(M1, 27, 0)

# ---------------------------------------------------------------- C (37-44) : Lento, le thème en augmentation exacte
C_MEL = ["e'4 f'4 cis''2.", "b'4 bes'4 d''2.", "a'4 aes'4 c''2.", "fis'4 g'4 ees''2."]
C_RET = ["ees'2. g4 fis4", "c'2. aes4 a4", "d'2. bes4 b4", "cis'2. f4 e4"]
# chaque mesure est harmonisée par une autre cellule de la série, très espacée
C_CH = [("g,", "fis", "ees''"), ("aes,", "c'", "a''"), ("bes,", "d'", "b''"), ("e,", "f", "cis'''")]
C_CH2 = [("e,", "f'", "cis'''"), ("d", "b'", "bes''"), ("a,", "c''", "aes''"), ("g,", "fis'", "ees''")]
for i in range(4):
    b = 37 + i
    M1[b] = T(C_MEL[i])
    g, ma, m2 = C_CH[i]
    GT[b], MA[b], M2[b] = W(g, False), W(ma), W(m2)
    b = 41 + i
    MA[b] = T(C_RET[i])
    g, m2, m1 = C_CH2[i]
    GT[b], M2[b], M1[b] = W(g, False), W(m2), W(m1)
M1[37] = dyn(M1[37], "\\p")
M2[37] = dyn(M2[37], "\\pp")
MA[37] = dyn(MA[37], "\\pp")
GT[37] = dyn(GT[37], "\\pp")
MA[41] = dyn(MA[41], "\\p")
M1[41] = dyn(M1[41], "\\pp")

# ---------------------------------------------------------------- D (45-56) : strette, cycle de tierces mineures
GT.update(gear(G1, range(45, 50)))
MA.update(gear(G2, range(45, 49)))
M2.update(gear(G3, range(45, 48)))
GT[45] = dyn(GT[45], "\\p\\<")
MA[45] = dyn(MA[45], "\\p")
M2[45] = dyn(M2[45], "\\p")
for i, s in enumerate(PHRASE1):
    M1[47 + i] = T(shift(s, 1))                 # P0
    M2[48 + i] = T(tp(s, 3))                    # P3
    MA[49 + i] = T(tp(shift(s, -1), 6))         # P6
    GT[50 + i] = tp(shift(s, -1), -3)           # P9
M1[47] = dyn(M1[47], "\\mf")
M2[48] = dyn(M2[48], "\\mf")
MA[49] = dyn(MA[49], "\\mf")
GT[50] = dyn(GT[50], "\\mf")
M1.update({51: "a''4.:32\\< bes''4:32", 52: "b''4.:32 c'''4:32", 53: "cis'''4.:32 d'''4:32"})
M2.update({52: "fis''4.:32\\< g''4:32", 53: "gis''4.:32 a''4:32"})
MA[53] = "g'4.:32\\< aes'4:32"
# tutti à l'unisson (octaves) : la tête du thème monte par tierces mineures (P3, P6, P9) jusqu'au retour de P0
for b, semis, dy in ((54, 3, "\\f"), (55, 6, "\\f"), (56, 9, "\\ff")):
    head = tp("e8-> f8-> cis'4.->", semis)
    M1[b] = T(dyn(shift(head, 2), dy))
    M2[b] = T(dyn(shift(head, 1), dy))
    MA[b] = T(dyn(head, dy))
    GT[b] = dyn(shift(head, -1), dy)
M1[55] = T("bes''8->\\f b''8-> g'''4.->")   # le sommet
M1[56] = T("cis''8->\\ff d''8-> bes''4.->")
M2[56] = T("cis'8->\\ff d'8-> bes'4.->")
MA[56] = T("cis8->\\ff d8-> bes4.->")
GT[56] = "cis8->\\ff d8-> bes4.->"

# ---------------------------------------------------------------- A' (57-64) : thème tutti et son miroir
for i, s in enumerate(PHRASE1 + PHRASE2):
    M1[57 + i] = T(shift(s, 1))
    M2[57 + i] = T(s)
MIRROR = ["e'8 ees'8 g'4.", "a8 bes8 fis'4.", "b8 c'8 aes'4.", "d'8 cis'8 f'4.",  # I0
          "f'4. cis'8 d'8", "aes4. c'8 b8", "fis'4. bes8 a8", "g4. ees'8 e'8"]   # RI0
for i, s in enumerate(MIRROR):
    MA[57 + i] = T(s)
    GT[57 + i] = " ".join(f"{G1_CH}8" + ("->" if k in (0, 2) else "") for k in range(5))
for v in (M1, M2, MA, GT):
    v[57] = dyn(v[57], "\\ff")

# ---------------------------------------------------------------- Coda (65-70)
GT.update(gear(G1, range(65, 68)))
MA.update(gear(G2, range(65, 67)))
M2.update(gear(G3, range(65, 69)))
GT[65] = dyn(GT[65], "\\p")
MA[65] = dyn(MA[65], "\\pp")
M2[65] = dyn(M2[65], "\\pp")
M2[68] = dyn(M2[68], "\\ppp")
M1[65] = T("e''8\\pp f''8 cis'''4.")
head = "e8-> f8-> cis'4.->"
M1[69] = T(dyn(shift(head, 2), "\\fff"))
M2[69] = T(dyn(shift(head, 1), "\\fff"))
MA[69] = T(dyn(head, "\\fff"))
GT[69] = dyn(shift(head, -1), "\\fff")
# accord final : les douze sons
M1[70] = "<cis'' aes''>8->\\sfz r8 r4.\\fermata"
M2[70] = "<b' f''>8->\\sfz r8 r4.\\fermata"
MA[70] = "<fis c'>8->\\sfz r8 r4.\\fermata"
GT[70] = "<e, bes, ees a d' g'>8->\\sfz r8 r4.\\fermata"

PARTS = [  # (identifiant, nom, nom court, clé, musique, son)
    ("mandolineI", "Mandoline 1", "Md. 1", "treble", M1, "mandoline"),
    ("mandolineII", "Mandoline 2", "Md. 2", "treble", M2, "mandoline"),
    ("mandole", "Mandole ténor", "Mdl.", "treble", MA, "mandole"),
    ("guitare", "Guitare", "Gt.", "treble_8", GT, "guitare"),
]
TRANSPOSITION = {"mandole": "c"}  # la mandole ténor sonne une octave plus bas que l'écrit
CHORDS = {}  # pas d'harmonie tonale : la vérification porte sur l'absence d'accords parfaits
