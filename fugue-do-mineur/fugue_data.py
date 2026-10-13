"""Fugue a 3 voix en do mineur -- notes en notation LilyPond absolue, mesure par mesure."""

S, A, B = {}, {}, {}

# --- Exposition -------------------------------------------------------------
A[1] = "c'8 ees'8 g'8 c''8 b'8 c''16 d''16 c''8 g'8"
A[2] = "aes'16 g'16 f'16 ees'16 f'16 ees'16 d'16 c'16 b8 g8 c'4"
S[1] = S[2] = "r1"
B[1] = B[2] = "r1"

S[3] = "g'8 bes'8 d''8 g''8 fis''8 g''16 a''16 g''8 d''8"
S[4] = "ees''16 d''16 c''16 bes'16 c''16 bes'16 a'16 g'16 fis'8 d'8 g'8 d''8"
A[3] = "bes8. c'16 bes8 d'8 a8 c'8 bes16 a16 g16 bes16"
A[4] = "c'4 a8 c'8 a8 fis8 g8 bes8"
B[3] = B[4] = "r1"

# codetta
S[5] = "ees''16 d''16 c''16 bes'16 aes'16 g'16 f'16 aes'16 g'8 b'8 d''8 f''8"
A[5] = "c'8 ees'8 f'8 d'8 b8 d'8 f'8 d'8"
B[5] = "r1"

S[6] = "ees''8. f''16 ees''8 g''8 d''8 f''8 ees''16 d''16 ees''16 g''16"
S[7] = "f''4 d''8 f''8 d''8 b'8 c''8 ees''8"
A[6] = "g'8 c''8 c''8 bes'8 aes'8 g'8 g'4"
A[7] = "c''4 b'4 g'8 f'8 ees'4~"
B[6] = "c8 ees8 g8 c'8 b8 c'16 d'16 c'8 g8"
B[7] = "aes16 g16 f16 ees16 f16 ees16 d16 c16 b,8 g,8 c4"

# --- Episode 1 (vers mi bemol majeur) ---------------------------------------
S[8] = "aes''16 g''16 f''16 ees''16 f''16 ees''16 d''16 c''16 bes'8 d''8 f''8 aes''8"
S[9] = "g''16 f''16 ees''16 d''16 ees''16 d''16 c''16 bes'16 aes'8 c''8 ees''8 g''8"
S[10] = "f''16 c''16 aes'16 c''16 f''16 ees''16 d''16 c''16 bes'8 d''8 f''8 aes''8"
A[8] = "ees'2 d'2~"
A[9] = "d'2 c'2~"
A[10] = "c'2 d'4 r4"
B[8] = "f4 aes4 bes4 bes,4"
B[9] = "ees4 g4 aes4 aes,4"
B[10] = "f4 aes4 bes4 bes,4"

# --- Entree en mi bemol majeur (alto) ---------------------------------------
A[11] = "ees'8 g'8 bes'8 ees''8 d''8 ees''16 f''16 ees''8 bes'8"
A[12] = "c''16 bes'16 aes'16 g'16 aes'16 g'16 f'16 ees'16 d'8 bes8 ees'4"
S[11] = "g''8. aes''16 g''8 bes''8 f''8 aes''8 g''16 f''16 ees''16 g''16"
S[12] = "aes''4 f''8 aes''8 f''8 d''8 ees''8 g''8"
B[11] = "ees4 g4 bes4 g4"
B[12] = "f4 aes,4 bes,4 c4"

# --- Episode 2 (vers fa mineur) ----------------------------------------------
S[13] = "ees''16 d''16 ees''16 g''16 c''16 g''16 ees''16 c''16 d''16 c''16 b'16 d''16 f''16 d''16 b'16 d''16"
A[13] = "g'8 c''8 g'4 g'8 f'8 d'8 f'8"
B[13] = "c4 ees4 g,2"
S[14] = "c''16 bes'16 c''16 ees''16 aes'16 ees''16 c''16 aes'16 bes'16 aes'16 g'16 bes'16 des''16 bes'16 g'16 bes'16"
A[14] = "ees'8 aes'8 ees'4 ees'8 des'8 bes8 des'8"
B[14] = "aes,4 c4 ees,2"
S[15] = "c''16 bes'16 aes'16 g'16 bes'16 des''16 f''16 bes''16 g''16 e''16 c''16 bes'16 g'8 e'8"
A[15] = "c'8 f'8 des'4 c'4 bes4"
B[15] = "aes,4 bes,4 c4 c,4"

# --- Entree en fa mineur (soprano) -------------------------------------------
S[16] = "f'8 aes'8 c''8 f''8 e''8 f''16 g''16 f''8 c''8"
S[17] = "des''16 c''16 bes'16 aes'16 bes'16 aes'16 g'16 f'16 e'8 c'8 f'4"
A[16] = "aes8. bes16 aes8 c'8 g8 bes8 aes16 g16 f16 aes16"
A[17] = "bes4 g8 bes8 g8 e8 f8 aes8"
B[16] = "f,4 aes,4 c4 f,4"
B[17] = "des4 bes,4 c4 f,4"

# --- Episode 3 (retour vers do mineur) ---------------------------------------
S[18] = "aes'8 c''8 f''8 aes''8~ aes''4 f''16 ees''16 d''16 c''16"
A[18] = "c'8 f'8 aes'4 f'16 g'16 aes'16 f'16 d'8 f'8"
B[18] = "f,8 aes,8 c8 f8 d8 f8 aes8 d8"
S[19] = "b'16 d''16 g''16 f''16 ees''16 d''16 c''16 b'16 f''4 d''4"
A[19] = "g'2 b'4 aes'4"
B[19] = "g,2 g4 f8 d8"

# --- Entree en do mineur (basse) ---------------------------------------------
S[20], A[20], B[20] = S[6], A[6], B[6]
S[21], A[21], B[21] = S[7], A[7].replace("~", ""), B[7]

# --- Episode 4 (demi-cadence) ------------------------------------------------
S[22], A[22], B[22] = S[13], A[13], B[13]
S[23] = "c''16 bes'16 c''16 ees''16 aes'16 ees''16 c''16 aes'16 c''4 b'8 r8"
A[23] = "ees'8 aes'8 ees'4 aes'4 f'4"
B[23] = "aes,4 c4 f,4 g,4"

# --- Entree finale en do mineur (soprano) ------------------------------------
S[24] = "c''8 ees''8 g''8 c'''8 b''8 c'''16 d'''16 c'''8 g''8"
S[25] = "aes''16 g''16 f''16 ees''16 f''16 ees''16 d''16 c''16 b'8 g'8 c''4"
A[24] = "ees'8. f'16 ees'8 g'8 d'8 f'8 ees'16 d'16 c'16 ees'16"
A[25] = "f'4 d'8 f'8 d'8 b8 c'8 ees'8"
B[24] = "c4 ees4 g,4 c4"
B[25] = "aes,4 f,4 g,4 c,4~"

# --- Coda sur pedale de tonique, tierce picarde -------------------------------
S[26] = "ees''4. f''16 g''16 aes''4. g''16 f''16"
S[27] = "d''4 aes''4 g''4 f''4"
S[28] = "e''1"
A[26] = "c''4 bes'4 aes'4 c''4"
A[27] = "aes'4 f'4 g'4 b'4"
A[28] = "<g' c''>1"
B[26] = "c,1~"
B[27] = "c,1~"
B[28] = "c,1"

NBARS = 28
VOICES = {"soprano": S, "alto": A, "basse": B}
