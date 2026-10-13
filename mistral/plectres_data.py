"""« Mistral » pour orchestre à plectres -- notes en notation LilyPond absolue (hauteurs réelles)."""

import re

NBARS = 68

# mesure : (longueur en rondes, signature LilyPond)
METER = {b: (1, "\\time 3,3,2 8/8") for b in range(1, NBARS + 1)}
for b in range(25, 41):
    METER[b] = (1, "\\time 4/4")
for b in (49, 50):
    METER[b] = (7 / 8, "\\time 2,2,3 7/8")

# tempo (noire = ...) par mesure
TEMPO = {b: 112 for b in range(1, NBARS + 1)}
TEMPO.update({23: 100, 24: 88, 40: 72})
TEMPO.update({b: 80 for b in range(25, 40)})
TEMPO.update({67: 104, 68: 96})

# indications pour la partition
MARKS = {
    1: '\\tempo "Con energia" 4 = 112',
    5: "\\mark \\default",
    13: "\\mark \\default",
    25: '\\tempo "Meno mosso, cantabile" 4 = 80 \\mark \\default',
    41: '\\tempo "Tempo I" 4 = 112 \\mark \\default',
    53: "\\mark \\default",
    61: "\\mark \\default",
}
TEXTS = {23: "rit.", 40: "poco rit.", 67: "allargando"}
BARLINES = {24: "||", 40: "||", 52: "||", 68: "|."}


def CH(x, end="r8 {x}8-."):
    """accords piqués en contretemps, calés sur 3+3+2"""
    return f"r8 {x}8-. {x}8-. r8 {x}8-. {x}8-. " + end.format(x=x)


def CH2(x):
    return CH(x, "{x}4->")


def dyn(s, mark):
    first = re.match(r"<[^>]+>\S*|\S+", s).group(0)
    return f"{first}{mark}{s[len(first):]}"


def Q(s, chord):
    """remplace la première note de basse par un accord"""
    first, rest = s.split(" ", 1)
    return f"{chord}8-> {rest}"


def GARP(b, w, x, y, z):
    return f"{b}8 {w}8 {x}8 {y}8 {z}8 {y}8 {x}8 {w}8"


def STRUM(ch):
    return f"{ch}8-> {ch}8 {ch}8 {ch}8-> {ch}8 {ch}8 {ch}8-> {ch}8"


P_Em = "e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8"
P_G = "g,8-> d8 b8 g,8-> d8 a8 g,8-> d8"
P_D = "d8-> a8 fis'8 d8-> a8 e'8 d8-> a8"
P_C = "c8-> g8 b8 c8-> g8 e'8 c8-> g8"
P_AmD = "a,8-> e8 g8 d8-> a8 fis'8 d8-> a8"
P_Am = "a,8-> e8 c'8 a,8-> e8 b8 a,8-> g8"
P_Bm = "b,8-> fis8 d'8 b,8-> fis8 cis'8 b,8-> a8"
EM, G_, D_ = "<e, b, e g b e'>", "<g, b, d g b g'>", "<d a d' fis'>"
C_, AM = "<c e g c' e'>", "<a, e a c' e'>"

# ---------------------------------------------------------------------------
THEME_M1 = [
    "b'8 e''8 fis''8 g''4.:32 fis''8 e''8",
    "d''4.:32 b'4.:32 a'8 b'8",
    "b'8 e''8 fis''8 g''4.:32 a''8 b''8",
    "a''4.:32 fis''4:32 d''4.:32",
    "b'8 e''8 fis''8 g''4.:32 fis''8 e''8",
    "d''4.:32 b'4.:32 e''8 fis''8",
    "g''4.:32 fis''4.:32 e''8 d''8",
    "e''2.:32 r4",
]

M1 = {b: "R1" for b in range(1, 5)}
for i, s in enumerate(THEME_M1):
    M1[5 + i] = s
M1[5] = dyn(M1[5], "\\mf")
M1.update({
    13: "b''1:32\\p", 14: "b''2:32 a''2:32", 15: "g''1:32", 16: "fis''1:32",
    17: "g''4.:32 b''4.:32 a''8 g''8", 18: "e''4.:32 b''4.:32 g''8 a''8",
    19: "c'''4.:32 a''4.:32 fis''8 a''8", 20: "g''2.:32 r4",
    21: "b'8\\mf e''8 fis''8 g''4.:32 r4", 22: "g''1:32\\p", 23: "e''1:32",
    24: "d''8\\mp g''8 a''8 b''4.:32 r4",
    # B : thème en augmentation, réharmonisé
    25: "b'4:32\\p e''4:32 fis''4:32 g''4:32~", 26: "g''2:32 fis''4:32 e''4:32",
    27: "d''2.:32 b'4:32~", 28: "b'2:32 a'4:32 b'4:32",
    29: "b'4:32\\< e''4:32 fis''4:32 g''4:32~", 30: "g''2:32 a''4:32 b''4:32",
    31: "a''2.:32\\mf fis''4:32~", 32: "fis''4:32\\> d''2.:32",
    33: "a''1:32\\p", 34: "g''1:32", 35: "g''2:32 fis''2:32", 36: "e''1:32",
    37: "e''2.:32 fis''4:32", 38: "fis''1:32", 39: "g''1:32", 40: "fis''1:32",
    # développement
    41: "R1", 42: "R1", 43: "R1", 44: "R1",
    45: "fis'8\\mf b'8 cis''8 d''4.:32 cis''8 b'8", 46: "a'4.:32 fis'4.:32 e'8 fis'8",
    47: "b'8\\f e''8 fis''8 g''4.:32 r4", 48: "r4. c''8 f''8 g''8 a''4:32",
    49: "a''8->\\f fis''8 a''8-> fis''8 a''8-> fis''8 d''8",
    50: "fis''8-> dis''8 fis''8-> dis''8 fis''8-> dis''8 b'8",
    51: "fis''4.:32\\< a''4.:32 b''4:32", 52: "b''4.:32 a''4.:32 fis''8 dis''8",
})
for i, s in enumerate(THEME_M1):
    M1[53 + i] = s
M1[53] = dyn(M1[53], "\\ff")
M1.update({
    61: "b'4.:32\\f e''4.:32 fis''4:32", 62: "g''1:32",
    63: "b'4.:32 e''4.:32 fis''4:32", 64: "g''2:32 a''2:32\\<",
    65: "b''1:32\\ff", 66: "b'8 e''8 fis''8 g''4.-> fis''8 e''8",
    67: "g''4.:32 a''4.:32 a''4:32", 68: "<g'' e'''>4->\\sfz r8 r4. r4",
})

# ---------------------------------------------------------------------------
M2 = {1: "R1", 2: "R1", 3: "R1"}
M2.update({
    4: dyn(CH("<g' b'>"), "\\mp"), 5: CH("<g' b'>"), 6: CH("<g' b'>"), 7: CH("<g' b'>"),
    8: CH("<fis' a'>"), 9: CH("<g' b'>"), 10: CH("<e' g'>"),
    11: "r8 <e' g'>8-. <e' g'>8-. r8 <fis' a'>8-. <fis' a'>8-. r8 <fis' a'>8-.",
    12: CH("<g' b'>"),
    13: dyn(CH2("<b' e''>"), "\\mp"), 14: CH2("<b' d''>"), 15: CH2("<b' e''>"),
    16: CH2("<a' d''>"), 17: CH2("<b' e''>"), 18: CH2("<b' e''>"),
    19: "r8 <c'' e''>8-. <c'' e''>8-. r8 <a' d''>8-. <a' d''>8-. <a' d''>4->",
    20: CH2("<b' e''>"),
    21: "R1", 22: "g'8\\mf c''8 d''8 e''4.:32 r4", 23: "c''1:32\\p", 24: "b'2.:32 r4",
    25: "e'1:32\\pp", 26: "e'1:32", 27: "fis'1:32", 28: "g'1:32",
    29: "e'1:32", 30: "g'1:32", 31: "fis'1:32", 32: "e'1:32",
    33: "c''1:32\\pp", 34: "b'1:32", 35: "d''1:32", 36: "b'1:32",
    37: "c''2.:32 a'4:32", 38: "b'1:32", 39: "c''1:32", 40: "b'2:32 a'2:32",
    41: "R1", 42: "R1",
    43: "e'8\\mp a'8 b'8 c''4.:32 b'8 a'8", 44: "g'4.:32 e'4.:32 d'8 e'8",
    45: "d'4.:32 fis'4.:32 e'8 d'8", 46: "fis'4.:32 d'4.:32 cis'8 d'8",
    47: "r4. g'8\\f c''8 d''8 e''4:32", 48: "e''4.:32 a'4.:32 a'4:32",
    49: "d''8-> a'8 d''8-> a'8 d''8-> a'8 fis'8",
    50: "b'8-> fis'8 b'8-> fis'8 b'8-> fis'8 dis'8",
    51: "a'4.:32\\< b'4.:32 dis''4:32", 52: "dis''4.:32 fis''4.:32 dis''8 b'8",
    # retour : le thème harmonisé en tierces
    53: "g'8\\ff b'8 d''8 e''4.:32 d''8 b'8", 54: "b'4.:32 g'4.:32 fis'8 g'8",
    55: "g'8 b'8 d''8 e''4.:32 fis''8 g''8", 56: "fis''4.:32 d''4:32 a'4.:32",
    57: "g'8 b'8 d''8 e''4.:32 d''8 b'8", 58: "b'4.:32 g'4.:32 c''8 d''8",
    59: "e''4.:32 d''4.:32 c''8 a'8", 60: "b'2.:32 r4",
    61: dyn(CH("<g' b'>"), "\\f"), 62: CH("<g' b'>"), 63: CH("<g' b'>"), 64: CH("<fis' a'>"),
    65: "<e'' g''>1:32\\ff", 66: "b8 e'8 fis'8 g'4.-> fis'8 e'8",
    67: "e''4.:32 fis''4.:32 fis''4:32", 68: "<b' e''>4->\\sfz r8 r4. r4",
})

# ---------------------------------------------------------------------------
MA = {1: "R1", 2: "R1", 3: "b1:32\\pp~", 4: "b1:32\\<"}
MA.update({
    5: "b1:32\\mp", 6: "b1:32", 7: "b1:32", 8: "a1:32", 9: "b1:32", 10: "c'1:32",
    11: "c'4.:32 a2:32 r8", 12: "b1:32",
    13: "b8\\mf e'8 fis'8 g'4.:32 fis'8 e'8", 14: "d'4.:32 b4.:32 a8 b8",
    15: "b8 e'8 fis'8 g'4.:32 a'8 b'8", 16: "a'4.:32 fis'4:32 d'4.:32",
    17: "b8 e'8 fis'8 g'4.:32 fis'8 e'8", 18: "d'4.:32 b4.:32 e'8 fis'8",
    19: "g'4.:32 fis'4.:32 e'8 d'8", 20: "e'2.:32 r4",
    21: "b1:32\\p", 22: "c'1:32", 23: "e8\\mf a8 b8 c'4.:32 r4", 24: "g2.:32\\p r4",
    25: "g1:32\\pp", 26: "g1:32", 27: "a1:32", 28: "b1:32",
    29: "g1:32", 30: "b1:32", 31: "a1:32", 32: "b1:32",
    33: "b4:32\\mp e'4:32 fis'4:32 g'4:32~", 34: "g'2:32 fis'4:32 e'4:32",
    35: "d'2.:32 b4:32~", 36: "b2:32 e'4:32 fis'4:32",
    37: "g'2.:32 fis'4:32~", 38: "fis'2:32 e'4:32 d'4:32",
    39: "e'1:32~", 40: "e'2:32 dis'2:32",
    41: "b8\\p e'8 fis'8 g'4.:32 fis'8 e'8", 42: "d'4.:32 b4.:32 a8 b8",
    43: "c'4.:32 e'4.:32 d'8 c'8", 44: "e'8 d'8 c'8 g4.:32 b8 c'8",
    45: "b4.:32 a4.:32 g8 fis8", 46: "d4.:32 d'4.:32 a8 d8",
    47: "<e b>4.:32\\f <c g>4.:32 <c g>4:32", 48: "e8 a8 b8 c'4.:32 r4",
    49: "fis'8-> d'8 fis'8-> d'8 fis'8-> d'8 a8",
    50: "dis'8-> b8 dis'8-> b8 dis'8-> b8 fis8",
    51: "b4.:32\\< dis'4.:32 fis'4:32", 52: "a4.:32 b4.:32 a8 fis8",
    53: "b1:32\\ff", 54: "b2:32 a2:32", 55: "g1:32", 56: "fis1:32",
    57: "g4.:32 b4.:32 a8 g8", 58: "e4.:32 b4.:32 g8 a8",
    59: "c'4.:32 a4.:32 fis8 a8", 60: "g2.:32 r4",
    61: "<e b>1:32\\f", 62: "<e b>1:32", 63: "<c g>1:32", 64: "<d a>1:32",
    65: "<e b>1:32\\ff", 66: "b8 e'8 fis'8 g'4.-> fis'8 e'8",
    67: "<c g>4.:32 <d a>4.:32 <d a>4:32", 68: "<e b>4->\\sfz r8 r4. r4",
})

# ---------------------------------------------------------------------------
GT = {
    1: dyn(P_Em, "\\p"), 2: P_Em, 3: P_Em, 4: dyn(P_Em, "\\<"),
    5: dyn(P_Em, "\\mf"), 6: P_G, 7: P_Em, 8: P_D, 9: P_Em, 10: P_C, 11: P_AmD, 12: P_Em,
    13: Q(P_Em, "<e, b, e g b>"), 14: Q(P_G, "<g, d g b>"), 15: Q(P_Em, "<e, b, e g b>"),
    16: Q(P_D, D_), 17: Q(P_Em, "<e, b, e g b>"), 18: Q(P_C, "<c g c' e'>"),
    19: Q(P_AmD, "<a, e a c'>"), 20: Q(P_Em, "<e, b, e g b>"),
    21: dyn(P_Em, "\\mp"), 22: P_C, 23: "<a, e a c' e'>1\\p", 24: "b,2. r4",
    25: dyn(GARP("c", "g", "b", "e'", "g'"), "\\p"), 26: GARP("a,", "e", "g", "c'", "e'"),
    27: GARP("b,", "fis", "a", "d'", "fis'"), 28: GARP("e,", "b,", "g", "d'", "e'"),
    29: GARP("c", "g", "b", "e'", "fis'"), 30: GARP("b,", "g", "d'", "g'", "a'"),
    31: GARP("a,", "fis", "a", "d'", "e'"), 32: GARP("g,", "e", "b", "d'", "fis'"),
    33: GARP("a,", "e", "g", "c'", "e'"), 34: GARP("e,", "b,", "g", "b", "fis'"),
    35: GARP("g,", "d", "g", "b", "d'"), 36: GARP("c", "g", "b", "e'", "fis'"),
    37: "a,8 e8 g8 c'8 e'8 c'8 d8 a8", 38: GARP("b,", "fis", "a", "d'", "fis'"),
    39: GARP("c", "g", "b", "e'", "g'"), 40: "b,8 fis8 a8 e'8 b,8 fis8 a8 dis'8",
    41: dyn(P_Em, "\\pp"), 42: P_G, 43: P_Am, 44: P_C, 45: dyn(P_Bm, "\\mp"), 46: P_D,
    47: "e,8->\\mf b,8 g8 c8-> g8 e'8 c8-> g8",
    48: "a,8-> e8 c'8 f,8-> c8 a8 f,8-> c8",
    49: f"{D_}8->\\f d8 {D_}8-> d8 {D_}8-> d8 d8",
    50: "<b, fis b dis'>8-> b,8 <b, fis b dis'>8-> b,8 <b, fis b dis'>8-> b,8 b,8",
    51: "b,8\\mf\\< b,8 b,8 b,8 b,8 b,8 b,8 b,8",
    52: "<b, dis a b fis'>8-> b,8 b,8 <b, dis a b fis'>8-> b,8 b,8 "
        "<b, dis a b fis'>8-> <b, dis a b fis'>8->",
    53: dyn(STRUM(EM), "\\ff"), 54: STRUM(G_), 55: STRUM(EM), 56: STRUM(D_),
    57: STRUM(EM), 58: STRUM(C_), 59: f"{AM}8-> {AM}8 {AM}8 {D_}8-> {D_}8 {D_}8 {D_}8-> {D_}8",
    60: STRUM(EM),
    61: dyn(P_Em, "\\f"), 62: P_Em, 63: P_C, 64: P_D, 65: dyn(STRUM(EM), "\\ff"),
    66: "b,8 e8 fis8 g4.-> fis8 e8", 67: f"{C_}4.-> {D_}4.-> {D_}4->",
    68: f"{EM}4->\\sfz r8 r4. r4",
}

PARTS = [  # (identifiant, nom, nom court, clé, musique, son)
    ("mandolineI", "Mandoline 1", "Md. 1", "treble", M1, "mandoline"),
    ("mandolineII", "Mandoline 2", "Md. 2", "treble", M2, "mandoline"),
    ("mandole", "Mandole", "Mdl.", "treble_8", MA, "mandole"),
    ("guitare", "Guitare", "Gt.", "treble_8", GT, "guitare"),
]

# harmonie prévue (pour la vérification) : mesure -> [(croche de départ, notes permises)]
_A = {0: "e g b d fis", 1: "g b d a", 2: "e g b d fis", 3: "d fis a e", 4: "e g b d fis",
      5: "c e g b d fis", 7: "e g b d fis"}
CHORDS = {b: [(0, "e g b d fis")] for b in range(1, 5)}
for base in (5, 13, 53):
    for i, c in _A.items():
        CHORDS[base + i] = [(0, c)]
    CHORDS[base + 6] = [(0, "a c e g"), (3, "d fis a e")]
CHORDS.update({
    21: [(0, "e g b d fis")], 22: [(0, "c e g b d")], 23: [(0, "a c e g b")], 24: [(0, "g b d a")],
    25: [(0, "c e g b d fis")], 26: [(0, "a c e g")], 27: [(0, "b d fis a")], 28: [(0, "e g b d")],
    29: [(0, "c e g b d fis")], 30: [(0, "g b d a")], 31: [(0, "a d fis e")], 32: [(0, "g e b d fis")],
    33: [(0, "a c e g b")], 34: [(0, "e g b fis d")], 35: [(0, "g b d")], 36: [(0, "c e g b fis")],
    37: [(0, "a c e g"), (6, "d fis a")], 38: [(0, "b d fis a")], 39: [(0, "c e g b")],
    40: [(0, "b e fis a"), (4, "b dis fis a")],
    41: [(0, "e g b d fis")], 42: [(0, "g b d a")], 43: [(0, "a c e g b")], 44: [(0, "c e g d")],
    45: [(0, "b d fis a cis")], 46: [(0, "d fis a e cis")],
    47: [(0, "e g b fis"), (3, "c e g d")], 48: [(0, "a c e b"), (3, "f a c g")],
    49: [(0, "d fis a")], 50: [(0, "b dis fis")], 51: [(0, "b dis fis a")], 52: [(0, "b dis fis a")],
    61: [(0, "e g b d fis")], 62: [(0, "e g b d fis")], 63: [(0, "c e g b fis")],
    64: [(0, "d fis a g")], 65: [(0, "e g b d fis")], 66: [(0, "e fis g b d")],
    67: [(0, "c e g"), (3, "d fis a")], 68: [(0, "e g b d fis")],
})
