\version "2.26.0"

\header {
  title = "Fugue en do mineur"
  subtitle = "à trois voix, dans le style de J.-S. Bach"
  composer = "Claude"
  tagline = ##f
}

global = {
  \key c \minor
  \time 4/4
}

soprano = {
  \global \voiceOne
  r1 |
  r1 |
  g'8 bes'8 d''8 g''8 fis''8 g''16 a''16 g''8 d''8 |
  ees''16 d''16 c''16 bes'16 c''16 bes'16 a'16 g'16 fis'8 d'8 g'8 d''8 |
  ees''16 d''16 c''16 bes'16 aes'16 g'16 f'16 aes'16 g'8 b'8 d''8 f''8 |
  ees''8. f''16 ees''8 g''8 d''8 f''8 ees''16 d''16 ees''16 g''16 |
  f''4 d''8 f''8 d''8 b'8 c''8 ees''8 |
  aes''16 g''16 f''16 ees''16 f''16 ees''16 d''16 c''16 bes'8 d''8 f''8 aes''8 |
  g''16 f''16 ees''16 d''16 ees''16 d''16 c''16 bes'16 aes'8 c''8 ees''8 g''8 |
  f''16 c''16 aes'16 c''16 f''16 ees''16 d''16 c''16 bes'8 d''8 f''8 aes''8 |
  g''8. aes''16 g''8 bes''8 f''8 aes''8 g''16 f''16 ees''16 g''16 |
  aes''4 f''8 aes''8 f''8 d''8 ees''8 g''8 |
  ees''16 d''16 ees''16 g''16 c''16 g''16 ees''16 c''16 d''16 c''16 b'16 d''16 f''16 d''16 b'16 d''16 |
  c''16 bes'16 c''16 ees''16 aes'16 ees''16 c''16 aes'16 bes'16 aes'16 g'16 bes'16 des''16 bes'16 g'16 bes'16 |
  c''16 bes'16 aes'16 g'16 bes'16 des''16 f''16 bes''16 g''16 e''16 c''16 bes'16 g'8 e'8 |
  f'8 aes'8 c''8 f''8 e''8 f''16 g''16 f''8 c''8 |
  des''16 c''16 bes'16 aes'16 bes'16 aes'16 g'16 f'16 e'8 c'8 f'4 |
  aes'8 c''8 f''8 aes''8~ aes''4 f''16 ees''16 d''16 c''16 |
  b'16 d''16 g''16 f''16 ees''16 d''16 c''16 b'16 f''4 d''4 |
  ees''8. f''16 ees''8 g''8 d''8 f''8 ees''16 d''16 ees''16 g''16 |
  f''4 d''8 f''8 d''8 b'8 c''8 ees''8 |
  ees''16 d''16 ees''16 g''16 c''16 g''16 ees''16 c''16 d''16 c''16 b'16 d''16 f''16 d''16 b'16 d''16 |
  c''16 bes'16 c''16 ees''16 aes'16 ees''16 c''16 aes'16 c''4 b'8 r8 |
  c''8 ees''8 g''8 c'''8 b''8 c'''16 d'''16 c'''8 g''8 |
  aes''16 g''16 f''16 ees''16 f''16 ees''16 d''16 c''16 b'8 g'8 c''4 |
  ees''4. f''16 g''16 aes''4. g''16 f''16 |
  d''4 aes''4 g''4 f''4 |
  e''1 \fermata
  \bar "|."
}

alto = {
  \global \voiceTwo
  c'8 ees'8 g'8 c''8 b'8 c''16 d''16 c''8 g'8 |
  aes'16 g'16 f'16 ees'16 f'16 ees'16 d'16 c'16 b8 g8 c'4 |
  bes8. c'16 bes8 d'8 a8 c'8 bes16 a16 g16 bes16 |
  c'4 a8 c'8 a8 fis8 g8 bes8 |
  c'8 ees'8 f'8 d'8 b8 d'8 f'8 d'8 |
  g'8 c''8 c''8 bes'8 aes'8 g'8 g'4 |
  c''4 b'4 g'8 f'8 ees'4~ |
  ees'2 d'2~ |
  d'2 c'2~ |
  c'2 d'4 r4 |
  ees'8 g'8 bes'8 ees''8 d''8 ees''16 f''16 ees''8 bes'8 |
  c''16 bes'16 aes'16 g'16 aes'16 g'16 f'16 ees'16 d'8 bes8 ees'4 |
  g'8 c''8 g'4 g'8 f'8 d'8 f'8 |
  ees'8 aes'8 ees'4 ees'8 des'8 bes8 des'8 |
  c'8 f'8 des'4 c'4 bes4 |
  aes8. bes16 aes8 c'8 g8 bes8 aes16 g16 f16 aes16 |
  bes4 g8 bes8 g8 e8 f8 aes8 |
  c'8 f'8 aes'4 f'16 g'16 aes'16 f'16 d'8 f'8 |
  g'2 b'4 aes'4 |
  g'8 c''8 c''8 bes'8 aes'8 g'8 g'4 |
  c''4 b'4 g'8 f'8 ees'4 |
  g'8 c''8 g'4 g'8 f'8 d'8 f'8 |
  ees'8 aes'8 ees'4 aes'4 f'4 |
  ees'8. f'16 ees'8 g'8 d'8 f'8 ees'16 d'16 c'16 ees'16 |
  f'4 d'8 f'8 d'8 b8 c'8 ees'8 |
  c''4 bes'4 aes'4 c''4 |
  aes'4 f'4 g'4 b'4 |
  <g' c''>1 \fermata
}

basse = {
  \global \clef bass
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  c8 ees8 g8 c'8 b8 c'16 d'16 c'8 g8 |
  aes16 g16 f16 ees16 f16 ees16 d16 c16 b,8 g,8 c4 |
  f4 aes4 bes4 bes,4 |
  ees4 g4 aes4 aes,4 |
  f4 aes4 bes4 bes,4 |
  ees4 g4 bes4 g4 |
  f4 aes,4 bes,4 c4 |
  c4 ees4 g,2 |
  aes,4 c4 ees,2 |
  aes,4 bes,4 c4 c,4 |
  f,4 aes,4 c4 f,4 |
  des4 bes,4 c4 f,4 |
  f,8 aes,8 c8 f8 d8 f8 aes8 d8 |
  g,2 g4 f8 d8 |
  c8 ees8 g8 c'8 b8 c'16 d'16 c'8 g8 |
  aes16 g16 f16 ees16 f16 ees16 d16 c16 b,8 g,8 c4 |
  c4 ees4 g,2 |
  aes,4 c4 f,4 g,4 |
  c4 ees4 g,4 c4 |
  aes,4 f,4 g,4 c,4~ |
  c,1~ |
  c,1~ |
  c,1 \fermata
}

tempi = {
  \tempo "Allegro moderato" 4 = 72
  s1*26
  \tempo 4 = 63 s2 \tempo 4 = 56 s2
  \tempo 4 = 46 s1
}

tempiPartition = {
  \tempo "Allegro moderato" 4 = 72
  s1*26 s1^\markup { \italic "rit." } s1
}

\score {
  \new PianoStaff <<
    \new Staff = "haut" << \tempiPartition \new Voice \soprano \new Voice \alto >>
    \new Staff = "bas" \new Voice \basse
  >>
  \layout { }
}

\score {
  \unfoldRepeats
  \new PianoStaff <<
    \new Staff << \tempi \new Voice \soprano \new Voice \alto >>
    \new Staff \new Voice \basse
  >>
  \midi { }
}
