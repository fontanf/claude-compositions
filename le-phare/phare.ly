\version "2.26.0"

\header {
  title = "Le Phare"
  subtitle = "pour guitare"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \clef "treble_8" \key e \minor
  \time 4/4 \tempo "Lento, misterioso" 4 = 66 \mark \markup \box "Le phare" s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \mark \markup \box "A" s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  \tempo "accelerando" s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \tempo "Agitato" 4 = 132 \mark \markup \box "B — la tempête" s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8^\markup { \italic "tambora" }
  s8*8
  s8*8
  s8*8
  s8*8^\markup { \italic "rasgueado" }
  s8*8
  s8*8
  s8*8 \bar "||"
  s8*8
  s8*8
  \mark \markup \box "Le phare" s8*8
  s8*8 \bar "||"
  \tempo "Largamente, luminoso" 4 = 60 \mark \markup \box "A’" \key e \major s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8^\markup { \italic "rit." }
  s8*8 \bar "||"
  \tempo "Lontano" 4 = 54 \mark \markup \box "Coda" s8*8
  s8*8
  s8*8^\markup { \italic "rit." }
  s8*8 \bar "|."
}

vUn = {
  r4^\p <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  e'4.^\mf e'8 c''2 |
  b'2. r4 |
  d'4. d'8 bes'2 |
  a'2. r4 |
  c'4. c'8 aes'2 |
  g'2 fis'4 e'4 |
  dis'2^\f fis'4 c''4 |
  b'4^\mp g'4 e'2 |
  e'4.^\mp^\< e'8 c''2 |
  f'4. f'8 des''2 |
  fis'4. fis'8 d''2 |
  g'4.^\f g'8 ees''2 |
  s8^\f s8 <f bes ees'>8-> s8 s8 <f bes ees'>8-> s8 <fis b e'>8-> |
  s8 s8 <f bes ees'>8-> s8 s8 <f bes ees'>8-> s8 <fis b e'>8-> |
  s8 s8 <fis b e'>8-> s8 s8 <fis b e'>8-> s8 <g c' f'>8-> |
  s8 s8 <g c' f'>8-> s8 s8 <g c' f'>8-> s8 <fis b e'>8-> |
  s8^\< s8 <c' f' bes'>8-> s8 s8 <c' f' bes'>8-> s8 <cis' fis' b'>8-> |
  s8 s8 <cis' fis' b'>8-> s8 s8 <cis' fis' b'>8-> s8 <d' g' c''>8-> |
  s8 s8 <d' g' c''>8-> s8 s8 <d' g' c''>8-> s8 <ees' aes' cis''>8-> |
  s8^\ff s8 <ees' aes' cis''>8-> s8 s8 <ees' aes' cis''>8-> s8 <e' a' d''>8-> |
  r4 <f bes ees'>8-> r8 r4 <fis b e'>4-> |
  r4 <b e' a'>8-> r8 r4 <bes ees' aes'>4-> |
  r4 <f bes ees'>8-> r8 r4 <fis b e'>4-> |
  r4 <b e' a'>8-> r8 r4 <bes ees' aes'>4-> |
  <e, b, e g c' f'>8\arpeggio->^\ff <e, b, e g c' f'>8 <e, b, e g c' f'>8 <e, b, e g c' f'>8 <e, b, e g c' f'>4\arpeggio-> <e, b, e g c' f'>4\arpeggio-> |
  <f, c f aes cis'>8\arpeggio-> <f, c f aes cis'>8 <f, c f aes cis'>8 <f, c f aes cis'>8 <f, c f aes cis'>4\arpeggio-> <f, c f aes cis'>4\arpeggio-> |
  <g, d g bes ees'>8\arpeggio-> <g, d g bes ees'>8 <g, d g bes ees'>8 <g, d g bes ees'>8 <g, d g bes ees'>4\arpeggio-> <g, d g bes ees'>4\arpeggio-> |
  <a, e a c' f'>8\arpeggio-> <a, e a c' f'>8 <a, e a c' f'>8 <a, e a c' f'>8 <a, e a c' f'>4\arpeggio-> <a, e a c' f'>4\arpeggio-> |
  <e, b, e g c' f'>1\arpeggio->^\fff\fermata |
  R1\fermata |
  r4^\pp <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  <gis b e'>4.^\f <gis b e'>8 <e gis c''>2 |
  <e gis b'>2. r4 |
  <gis d'>4. <gis d'>8 <f d' bes'>2 |
  <e c' a'>2. r4 |
  <e c'>4. <e c'>8 <e c' gis'>2 |
  <e b gis'>2 <cis' fis'>4 <cis' e'>4 |
  <a dis'>2 <a dis' fis'>4 <a dis' c''>4 |
  <e gis b'>4 <b e' gis'>4 <e gis b e'>2 |
  <e a c''>2^\ff <e gis b'>2 |
  <c f a'>2 <b e' gis'>2 |
  <e gis c''>1^\> |
  <e gis b'>1^\mp |
  r4^\p <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4^\pp <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  <e, b, e gis b e'>1\arpeggio\fermata^\ppp
}

vDeux = {
  s1 |
  s1 |
  e,1\pp |
  e,1 |
  e,8\p b,8 g8 b,8 e,8 g8 e'8 g8 |
  e,8 g8 b8 g8 d8 g8 b8 g8 |
  bes,8 f8 bes8 f8 bes,8 f8 d'8 f8 |
  c8 e8 a8 e8 c8 e8 a8 e8 |
  c8 ees8 aes8 ees8 c8 ees8 aes8 ees8 |
  b,8 d8 g8 d8 a,8 e8 c'8 e8 |
  b,8 fis8 a8 fis8 b,8 dis8 a8 dis8 |
  e,8 g8 b8 g8 e,8 b,8 g8 b,8 |
  e,8\p e,8 e,8 e,8 e,8 e,8 e,8 e,8 |
  e,8 e,8 e,8 e,8 e,8 e,8 e,8 e,8 |
  e,8 e,8 e,8 e,8 e,8 e,8 e,8 e,8 |
  e,8 e,8 e,8 e,8 e,8 e,8 e,8 e,8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,8 e,8 s8 e,8 e,8 s8 e,8 s8 |
  e,4.->\f e,8 c2 |
  bes,4.-> bes,8 fis2 |
  e,4.-> e,8 c2 |
  bes,4.-> bes,8 fis2 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  e,1 |
  e,1 |
  e,2 e,2 |
  e,1 |
  d2 d2 |
  c1 |
  c1 |
  gis,2 a,2 |
  b,1 |
  e,1 |
  a,2 e,2 |
  f,2 e,2 |
  c1 |
  e,1 |
  e,1 |
  e,1 |
  e,1 |
  s1
}

\score {
  \new Staff \with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } << \global \new Voice { \voiceOne \vUn } \new Voice { \voiceTwo \vDeux } >>
  \layout { }
}

\score {
  \new Staff \with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } << \global \new Voice { \voiceOne \vUn } \new Voice { \voiceTwo \vDeux } >>
  \midi { }
}
