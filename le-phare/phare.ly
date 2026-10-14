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
  e'4.^\mf e'8 c''2-4 |
  b'2.-1 r4 |
  d'4.-4 d'8 bes'2-4^"½C III" |
  a'2.-4^"½C II" r4 |
  c'4.-1^"½C I" c'8 aes'2-4 |
  g'2-2 fis'4-3 e'4 |
  dis'2-4^\f^"½C II" fis'4-4 c''4 |
  b'4-4^\mp g'4-1 e'2 |
  e'4.^\mp^\< e'8 c''2-1 |
  f'4.-1 f'8 des''2-1 |
  fis'4.-1 fis'8 d''2-1 |
  g'4.-1^\f g'8 ees''2-1 |
  s8^\f s8 <f-1 bes-1 ees'-2>8->^"½C III" s8 s8 <f bes ees'>8-> s8 <fis-1 b e'>8-> |
  s8 s8 <f-1 bes-1 ees'-2>8->^"½C III" s8 s8 <f bes ees'>8-> s8 <fis-1 b e'>8-> |
  s8 s8 <fis-1 b e'>8-> s8 s8 <fis b e'>8-> s8 <g c'-1 f'-1>8->^"½C I" |
  s8 s8 <g c'-1 f'-1>8-> s8 s8 <g c' f'>8-> s8 <fis-1 b e'>8-> |
  s8^\< s8 <c'-1-\3 f'-2-\2 bes'-3>8-> s8 s8 <c' f' bes'>8-> s8 <cis'-1-\3 fis'-2-\2 b'-3>8-> |
  s8 s8 <cis'-1-\3 fis'-2-\2 b'-3>8-> s8 s8 <cis' fis' b'>8-> s8 <d'-1-\3 g'-2-\2 c''-3>8-> |
  s8 s8 <d'-1-\3 g'-2-\2 c''-3>8-> s8 s8 <d' g' c''>8-> s8 <ees'-1-\3 aes'-2-\2 cis''-3>8-> |
  s8^\ff s8 <ees'-1-\3 aes'-2-\2 cis''-3>8-> s8 s8 <ees' aes' cis''>8-> s8 <e'-1-\3 a'-2-\2 d''-3>8-> |
  r4 <f-1 bes-1 ees'-2>8->^"½C III" r8 r4 <fis-2 b e'>4-> |
  r4 <b-4-\3 e'-4-\2 a'-4>8-> r8 r4 <bes-1 ees'-3 aes'-4>4-> |
  r4 <f-1 bes-1 ees'-2>8->^"½C III" r8 r4 <fis-2 b e'>4-> |
  r4 <b-4-\3 e'-4-\2 a'-4>8-> r8 r4 <bes-1 ees'-3 aes'-4>4-> |
  <e, b,-2 e-3 g c'-1 f'-1>8\arpeggio->^\ff^"½C I" <e, b, e g c' f'>8 <e, b, e g c' f'>8 <e, b, e g c' f'>8 <e, b, e g c' f'>4\arpeggio-> <e, b, e g c' f'>4\arpeggio-> |
  <f,-1 c-3 f-4 aes-1 cis'-2>8\arpeggio->^"C I" <f, c f aes cis'>8 <f, c f aes cis'>8 <f, c f aes cis'>8 <f, c f aes cis'>4\arpeggio-> <f, c f aes cis'>4\arpeggio-> |
  <g,-1 d-3-\5 g-4-\4 bes-1 ees'-2>8\arpeggio->^"C III" <g, d g bes ees'>8 <g, d g bes ees'>8 <g, d g bes ees'>8 <g, d g bes ees'>4\arpeggio-> <g, d g bes ees'>4\arpeggio-> |
  <a, e-2 a-3 c'-1 f'-1>8\arpeggio->^"½C I" <a, e a c' f'>8 <a, e a c' f'>8 <a, e a c' f'>8 <a, e a c' f'>4\arpeggio-> <a, e a c' f'>4\arpeggio-> |
  <e, b,-2 e-3 g c'-1 f'-1>1\arpeggio->^\fff\fermata |
  R1\fermata |
  r4^\pp <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  <gis-1 b e'>4.^\f <gis b e'>8 <e-2-\5 gis-1-\4 c''-3>2 |
  <e-2-\5 gis-1-\4 b'-3>2. r4 |
  <gis-1 d'-3>4. <gis d'>8 <f-1 d'-1 bes'-4>2^"½C III" |
  <e-1 c'-4-\3 a'-4>2. r4 |
  <e-2 c'-1>4. <e c'>8 <e-2 c'-1 gis'-4>2 |
  <e-1 b gis'-4>2 <cis'-1 fis'-1>4^"½C II" <cis'-1 e'>4 |
  <a-1 dis'-3>2^"½C II" <a-1 dis'-3 fis'-1>4^"C II" <a-4-\4 dis'-4-\3 c''-4>4 |
  <e-2-\5 gis-1-\4 b'-3>4 <b-1-\3 e'-2-\2 gis'-1>4^"½C IV" <e-2 gis-1 b e'>2 |
  <e-3-\5 a-4-\4 c''-4>2^\ff <e-2-\5 gis-1-\4 b'-3>2 |
  <c-3 f-4 a'-4>2 <b-1-\3 e'-2-\2 gis'-1>2^"½C IV" |
  <e-2-\5 gis-1-\4 c''-4>1^\> |
  <e-2-\5 gis-1-\4 b'-3>1^\mp |
  r4^\p <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4 <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  r4^\pp <b'\harmonic>4^"XII②" <e''\harmonic>2^"XII①" |
  <e, b,-2 e-3 gis-1 b e'>1\arpeggio\fermata^\ppp
}

vDeux = {
  s1 |
  s1 |
  e,1\pp |
  e,1 |
  e,8\p b,8_1 g8 b,8 e,8 g8 e'8_1_\2 g8 |
  e,8 g8 b8 g8 d8 g8 b8 g8 |
  bes,8_1 f8_3 bes8_4 f8 bes,8_4_\6 f8_1 d'8_1 f8 |
  c8_2 e8_1 a8_1 e8 c8_2 e8_1 a8_1 e8 |
  c8_3 ees8_1 aes8_1 ees8 c8_3 ees8_1 aes8_1 ees8 |
  b,8_1 d8 g8 d8 a,8 e8_2 c'8_1 e8 |
  b,8_1 fis8_3 a8_1 fis8 b,8_2 dis8_1 a8_3 dis8 |
  e,8 g8 b8 g8 e,8 b,8_1 g8 b,8 |
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
  e,4.->\f e,8 c2_1 |
  bes,4._1-> bes,8_1 fis2_4 |
  e,4.-> e,8 c2_1 |
  bes,4._1-> bes,8_1 fis2_4 |
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
  d2 d2_1_\5 |
  c1_1 |
  c1_1 |
  gis,2_1 a,2 |
  b,1_1 |
  e,1 |
  a,2_1_\6 e,2 |
  f,2_1 e,2 |
  c1_1_\6 |
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
