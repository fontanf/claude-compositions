"""« Fontaine » pour guitare seule (6e corde en ré) -- notes en hauteurs réelles, notation LilyPond absolue.

Deux voix : v1 (hampes en haut : mélodie, trémolo, traits) et v2 (hampes en bas : basses et arpèges).
"""
import re

TITLE = "Fontaine"
SUBTITLE = "pour guitare"
KEY = "\\key d \\major"
TUNING = [38, 45, 50, 55, 59, 64]  # ré2 la2 ré3 sol3 si3 mi4 (6e corde abaissée en ré)

NBARS = 56
METER = {b: (3 / 4, "\\time 6/8") for b in range(1, NBARS + 1)}

# tempo exprimé en noires (noire pointée = 56 -> noire = 84)
TEMPO = {b: 84 for b in range(1, 17)}
TEMPO.update({b: 132 for b in range(17, 35)})
TEMPO.update({34: 116})
TEMPO.update({b: 78 for b in range(35, 51)})
TEMPO.update({b: 72 for b in range(51, 57)})
TEMPO.update({55: 60, 56: 48})

MARKS = {
    1: '\\tempo "Andantino, come una fontana" 4. = 56 \\mark \\markup \\box "A"',
    17: '\\tempo "Allegro con fuoco" 4. = 88 \\mark \\markup \\box "B" \\key d \\minor',
    35: '\\tempo "Tremolo, cantabile" 4. = 52 \\mark \\markup \\box "A’" \\key d \\major',
    51: '\\tempo "Lontano" 4. = 48 \\mark \\markup \\box "Coda"',
}
TEXTS = {1: "⑥ = ré", 17: "liés", 25: "la mélodie au pouce", 31: "rasgueado", 34: "rit.", 55: "rit."}
BARLINES = {16: "||", 34: "||", 50: "||", 56: "|."}

# mode de vérification du doigté : "forme" = la main gauche tient un accord par demi-mesure (arpèges qui
# résonnent) ; "ligne" = on vérifie chaque attaque avec ce qui sonne déjà
MODE = {b: "forme" for b in range(1, NBARS + 1)}
for b in range(17, 35):
    MODE[b] = "ligne"
for b in range(51, 57):
    MODE[b] = "ligne"


def dyn(s, mark):
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def arp(shape):
    """arpège en doubles croches sur une demi-mesure : basse, puis i1 i2 i3 i2 i1"""
    b, x, y, z = shape
    return f"{b}16 {x}16 {y}16 {z}16 {y}16 {x}16"


def thumb(shape):
    """le pouce en croches pendant le trémolo : basse, i1, i2"""
    b, x, y, _ = shape
    return f"{b}8 {x}8 {y}8"


DUR8 = {"8": 1, "4": 2, "4.": 3, "2": 4, "2.": 6}


def tremolo(mel):
    """chaque croche de la mélodie devient un groupe pouce + trois triples croches (p a m i)"""
    out = []
    for tok in mel.split():
        m = re.match(r"([a-g](?:is|es)*[',]*|r)(\d+\.?)(.*)", tok)
        p, d, post = m.groups()
        for k in range(DUR8[d]):
            if p == "r":
                out.append("r8")
            else:
                out.append(f"r32 {p}32{post if k == 0 else ''} {p}32 {p}32")
    return " ".join(out)


V1, V2 = {}, {}

# ---------------------------------------------------------------- A (1-16) : mélodie aiguë sur arpèges en campanella
MEL = {
    1: "fis''4 e''8 d''4.", 2: "e''4 fis''8 a'4.", 3: "b'4 cis''8 d''4 e''8", 4: "fis''4. a''4.",
    5: "g''4 fis''8 e''4.", 6: "d''4 cis''8 b'4.", 7: "a'4 b'8 cis''4 e''8", 8: "d''2.",
    9: "fis''4 e''8 d''4.", 10: "e''4 fis''8 a''4.", 11: "gis''4 fis''8 e''4.", 12: "fis''4 e''8 d''4 b'8",
    13: "g''4 fis''8 e''4 d''8", 14: "cis''4 d''8 e''4.", 15: "fis''4. e''4.", 16: "d''4. r4.",
}
D_HI = ("d,", "d", "fis'", "a'")      # ré, la et fa# en position X, ré à vide
G_HI = ("g", "d'", "b", "g'")         # sol majeur : sol sur la 5e corde (case X), si à vide
E_MIN = ("e", "g", "b", "e'")         # mi mineur : mi sur la 6e corde (case XIV), sol et si à vide
E_MIN7 = ("e", "g", "b", "d'")
BM = ("b,", "fis", "d'", "b")         # si mineur, si grave sur la 6e corde (case IX)
A_HI = ("a,", "cis'", "e'", "a'")     # la majeur en position IX
SHAPES = {
    1: (D_HI, ("a,", "d", "fis'", "a'")),
    2: (A_HI, ("a,", "a", "cis'", "e'")),
    3: (BM, G_HI),
    4: (D_HI, ("d,", "a,", "d'", "b")),
    5: (G_HI, E_MIN),
    6: (BM, G_HI),
    7: (("a,", "d", "g", "e'"), A_HI),
    8: (D_HI, ("d,", "a,", "d", "fis'")),
    9: (D_HI, ("a,", "d", "fis'", "a'")),
    10: (A_HI, ("a,", "d", "d'", "b")),
    11: (("d,", "e'", "gis'", "b'"), ("d,", "e'", "gis'", "b'")),   # mi majeur sur pédale de ré : couleur lydienne
    12: (D_HI, ("d,", "d", "fis'", "b")),
    13: (G_HI, E_MIN7),
    14: (("a,", "cis'", "e'", "g'"), A_HI),
    15: (("a,", "d", "fis'", "a'"), ("a,", "cis'", "e'", "g'")),
    16: (D_HI, ("d,", "a,", "d", "a")),
}
for b in range(1, 17):
    V1[b] = MEL[b]
    V2[b] = arp(SHAPES[b][0]) + " " + arp(SHAPES[b][1])
V1[1] = dyn(V1[1], "\\p")
V2[1] = dyn(V2[1], "\\pp")
V1[4] = dyn(V1[4], "\\<")
V1[5] = dyn(V1[5], "\\mp")
V1[10] = dyn(V1[10], "\\<")
V1[11] = dyn(V1[11], "\\mf")
V1[15] = dyn(V1[15], "\\>")
V1[16] = dyn(V1[16], "\\p")

# ---------------------------------------------------------------- B (17-34) : toccata en ré mineur
RIFF = [
    "f'16( e'16) g'16( e'16) a'16( e'16) bes'16( e'16) a'16( e'16) g'16( e'16)",
    "f'16( e'16) g'16( e'16) a'16( e'16) d''16( e'16) c''16( e'16) bes'16( e'16)",
    "a'16( e'16) bes'16( e'16) c''16( e'16) d''16( e'16) c''16( e'16) bes'16( e'16)",
    "a'16( e'16) g'16( e'16) f'16( e'16) d'16 e'16 f'16 g'16 a'16 bes'16",
]
for i in range(4):
    V1[17 + i] = RIFF[i]
    V1[21 + i] = RIFF[i]
V2.update({17: "d,4.-> d,4.->", 18: "d,4. d,4.", 19: "a,4.-> a,4.->", 20: "a,4. a,4.",
           21: "d,8-> d8 d,8 d,8-> d8 d,8", 22: "d,8-> d8 d,8 d,8-> d8 d,8",
           23: "a,8-> a8 a,8 a,8-> a8 a,8", 24: "a,8-> a8 a,8 a,8-> a8 a,8"})
V1[17] = dyn(V1[17], "\\mf")
V2[17] = dyn(V2[17], "\\mf")
V1[21] = dyn(V1[21], "\\f")
V2[21] = dyn(V2[21], "\\f")
# le thème, en mineur, joué au pouce dans les basses ; au-dessus, les trois cordes aiguës à vide
THUMB = ["f4 e8 d4.", "e4 f8 a,4.", "b,4 c8 d4 e8", "f4. a4.", "g4 f8 e4.", "d4 cis8 d4."]
for i in range(6):
    V1[25 + i] = "g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16"
    V2[25 + i] = THUMB[i]
V1[25] = dyn(V1[25], "\\p")
V2[25] = dyn(V2[25], "\\mf")
DM, C_, BB = "<d, a, d a d' f'>", "<c e g c' e'>", "<bes, f bes d' f'>"
A_, A7 = "<a, e a cis' e'>", "<a, e g cis' e'>"
V1.update({
    31: f"{DM}8\\arpeggio->\\f {DM}8 {DM}8 {C_}8\\arpeggio-> {C_}8 {C_}8",
    32: f"{BB}8\\arpeggio-> {BB}8 {BB}8 {A_}8\\arpeggio-> {A_}8 {A_}8",
    33: f"{DM}4\\arpeggio->\\ff {C_}4\\arpeggio-> {BB}4\\arpeggio->",
    34: f"{A7}4.\\arpeggio-> a''16(\\> g''16 f''16 e''16 d''16 cis''16)",
})
for b in range(31, 35):
    V2[b] = "s2."

# ---------------------------------------------------------------- A' (35-50) : la mélodie en trémolo
for b in range(1, 17):
    V1[34 + b] = tremolo(MEL[b])
    V2[34 + b] = thumb(SHAPES[b][0]) + " " + thumb(SHAPES[b][1])
V1[35] = V1[35].replace("fis''32 ", "fis''32\\p ", 1)
V2[35] = dyn(V2[35], "\\pp")

# ---------------------------------------------------------------- Coda (51-56) : la tête du thème en harmoniques
V1.update({
    51: "<fis''\\harmonic>4^\"VII②\" <e''\\harmonic>8^\"XII①\" <d''\\harmonic>4.^\"V④\"",
    52: "<e''\\harmonic>4^\"XII①\" <fis''\\harmonic>8^\"VII②\" <a'\\harmonic>4.^\"V⑤\"",
    53: "<b'\\harmonic>4^\"XII②\" <cis''\\harmonic>8^\"IV⑤\" <d''\\harmonic>4^\"V④\" <e''\\harmonic>8^\"XII①\"",
    54: "<fis''\\harmonic>2.^\"VII②\"",
    55: "<d\\harmonic a\\harmonic d'\\harmonic>2.^\"XII⑥⑤④\"",
    56: "<d, a, d fis' a' d''>2.\\arpeggio\\fermata",
})
V1[51] = dyn(V1[51], "\\p")
V1[56] = dyn(V1[56], "\\pp")
V2.update({51: "d,2.", 52: "a,2.", 53: "d,2.", 54: "d,2.", 55: "s2.", 56: "s2."})

# nuances et soufflets de la voix supérieure au-dessus de la portée, ceux de la basse en dessous
for _b in V1:
    V1[_b] = re.sub(r"(?<![\^_])\\(ppp|pp|mp|mf|ff|sfz|p|f|<|>)(?![a-zA-Z])", r"^\\\1", V1[_b])
