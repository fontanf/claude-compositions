\version "2.26.0"

\header {
  title = "Fontaine"
  subtitle = "pour guitare"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \clef "treble_8" \key d \major
  \time 6/8 \tempo "Andantino, come una fontana" 4. = 56 \mark \markup \box "A" s8*6^\markup { \italic "⑥ = ré" }
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6 \bar "||"
  \tempo "Allegro con fuoco" 4. = 88 \mark \markup \box "B" \key d \minor s8*6^\markup { \italic "liés" }
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6^\markup { \italic "la mélodie au pouce" }
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6^\markup { \italic "rasgueado" }
  s8*6
  s8*6
  s8*6^\markup { \italic "rit." } \bar "||"
  \tempo "Tremolo, cantabile" 4. = 52 \mark \markup \box "A’" \key d \major s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6 \bar "||"
  \tempo "Lontano" 4. = 48 \mark \markup \box "Coda" s8*6
  s8*6
  s8*6
  s8*6
  s8*6^\markup { \italic "rit." }
  s8*6 \bar "|."
}

vUn = {
  fis''4^\p e''8 d''4. |
  e''4 fis''8 a'4. |
  b'4 cis''8 d''4 e''8 |
  fis''4.^\< a''4. |
  g''4^\mp fis''8 e''4. |
  d''4 cis''8 b'4. |
  a'4 b'8 cis''4 e''8 |
  d''2. |
  fis''4 e''8 d''4. |
  e''4^\< fis''8 a''4. |
  gis''4^\mf fis''8 e''4. |
  fis''4 e''8 d''4 b'8 |
  g''4 fis''8 e''4 d''8 |
  cis''4 d''8 e''4. |
  fis''4.^\> e''4. |
  d''4.^\p r4. |
  f'16(^\mf e'16) g'16( e'16) a'16( e'16) bes'16( e'16) a'16( e'16) g'16( e'16) |
  f'16( e'16) g'16( e'16) a'16( e'16) d''16( e'16) c''16( e'16) bes'16( e'16) |
  a'16( e'16) bes'16( e'16) c''16( e'16) d''16( e'16) c''16( e'16) bes'16( e'16) |
  a'16( e'16) g'16( e'16) f'16( e'16) d'16 e'16 f'16 g'16 a'16 bes'16 |
  f'16(^\f e'16) g'16( e'16) a'16( e'16) bes'16( e'16) a'16( e'16) g'16( e'16) |
  f'16( e'16) g'16( e'16) a'16( e'16) d''16( e'16) c''16( e'16) bes'16( e'16) |
  a'16( e'16) bes'16( e'16) c''16( e'16) d''16( e'16) c''16( e'16) bes'16( e'16) |
  a'16( e'16) g'16( e'16) f'16( e'16) d'16 e'16 f'16 g'16 a'16 bes'16 |
  g16^\p b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  <d, a, d a d' f'>8\arpeggio->^\f <d, a, d a d' f'>8 <d, a, d a d' f'>8 <c e g c' e'>8\arpeggio-> <c e g c' e'>8 <c e g c' e'>8 |
  <bes, f bes d' f'>8\arpeggio-> <bes, f bes d' f'>8 <bes, f bes d' f'>8 <a, e a cis' e'>8\arpeggio-> <a, e a cis' e'>8 <a, e a cis' e'>8 |
  <d, a, d a d' f'>4\arpeggio->^\ff <c e g c' e'>4\arpeggio-> <bes, f bes d' f'>4\arpeggio-> |
  <a, e g cis' e'>4.\arpeggio-> a''16(^\> g''16 f''16 e''16 d''16 cis''16) |
  r32 fis''32^\p fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 |
  r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 fis''32 fis''32 fis''32 r32 a'32 a'32 a'32 r32 a'32 a'32 a'32 r32 a'32 a'32 a'32 |
  r32 b'32 b'32 b'32 r32 b'32 b'32 b'32 r32 cis''32 cis''32 cis''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 e''32 e''32 e''32 |
  r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 a''32 a''32 a''32 r32 a''32 a''32 a''32 r32 a''32 a''32 a''32 |
  r32 g''32 g''32 g''32 r32 g''32 g''32 g''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 cis''32 cis''32 cis''32 r32 b'32 b'32 b'32 r32 b'32 b'32 b'32 r32 b'32 b'32 b'32 |
  r32 a'32 a'32 a'32 r32 a'32 a'32 a'32 r32 b'32 b'32 b'32 r32 cis''32 cis''32 cis''32 r32 cis''32 cis''32 cis''32 r32 e''32 e''32 e''32 |
  r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 |
  r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 |
  r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 fis''32 fis''32 fis''32 r32 a''32 a''32 a''32 r32 a''32 a''32 a''32 r32 a''32 a''32 a''32 |
  r32 gis''32 gis''32 gis''32 r32 gis''32 gis''32 gis''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 b'32 b'32 b'32 |
  r32 g''32 g''32 g''32 r32 g''32 g''32 g''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 d''32 d''32 d''32 |
  r32 cis''32 cis''32 cis''32 r32 cis''32 cis''32 cis''32 r32 d''32 d''32 d''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r8 r8 r8 |
  <fis''\harmonic>4^"VII②"^\p <e''\harmonic>8^"XII①" <d''\harmonic>4.^"V④" |
  <e''\harmonic>4^"XII①" <fis''\harmonic>8^"VII②" <a'\harmonic>4.^"V⑤" |
  <b'\harmonic>4^"XII②" <cis''\harmonic>8^"IV⑤" <d''\harmonic>4^"V④" <e''\harmonic>8^"XII①" |
  <fis''\harmonic>2.^"VII②" |
  <d\harmonic a\harmonic d'\harmonic>2.^"XII⑥⑤④" |
  <d, a, d fis' a' d''>2.\arpeggio\fermata^\pp
}

vDeux = {
  d,16\pp d16 fis'16 a'16 fis'16 d16 a,16 d16 fis'16 a'16 fis'16 d16 |
  a,16 cis'16 e'16 a'16 e'16 cis'16 a,16 a16 cis'16 e'16 cis'16 a16 |
  b,16 fis16 d'16 b16 d'16 fis16 g16 d'16 b16 g'16 b16 d'16 |
  d,16 d16 fis'16 a'16 fis'16 d16 d,16 a,16 d'16 b16 d'16 a,16 |
  g16 d'16 b16 g'16 b16 d'16 e16 g16 b16 e'16 b16 g16 |
  b,16 fis16 d'16 b16 d'16 fis16 g16 d'16 b16 g'16 b16 d'16 |
  a,16 d16 g16 e'16 g16 d16 a,16 cis'16 e'16 a'16 e'16 cis'16 |
  d,16 d16 fis'16 a'16 fis'16 d16 d,16 a,16 d16 fis'16 d16 a,16 |
  d,16 d16 fis'16 a'16 fis'16 d16 a,16 d16 fis'16 a'16 fis'16 d16 |
  a,16 cis'16 e'16 a'16 e'16 cis'16 a,16 d16 d'16 b16 d'16 d16 |
  d,16 e'16 gis'16 b'16 gis'16 e'16 d,16 e'16 gis'16 b'16 gis'16 e'16 |
  d,16 d16 fis'16 a'16 fis'16 d16 d,16 d16 fis'16 b16 fis'16 d16 |
  g16 d'16 b16 g'16 b16 d'16 e16 g16 b16 d'16 b16 g16 |
  a,16 cis'16 e'16 g'16 e'16 cis'16 a,16 cis'16 e'16 a'16 e'16 cis'16 |
  a,16 d16 fis'16 a'16 fis'16 d16 a,16 cis'16 e'16 g'16 e'16 cis'16 |
  d,16 d16 fis'16 a'16 fis'16 d16 d,16 a,16 d16 a16 d16 a,16 |
  d,4.->\mf d,4.-> |
  d,4. d,4. |
  a,4.-> a,4.-> |
  a,4. a,4. |
  d,8->\f d8 d,8 d,8-> d8 d,8 |
  d,8-> d8 d,8 d,8-> d8 d,8 |
  a,8-> a8 a,8 a,8-> a8 a,8 |
  a,8-> a8 a,8 a,8-> a8 a,8 |
  f4\mf e8 d4. |
  e4 f8 a,4. |
  bes,4 c8 d4 e8 |
  f4. a4. |
  g4 f8 e4. |
  d4 cis8 d4. |
  s2. |
  s2. |
  s2. |
  s2. |
  d,8\pp d8 fis'8 a,8 d8 fis'8 |
  a,8 cis'8 e'8 a,8 a8 cis'8 |
  b,8 fis8 d'8 g8 d'8 b8 |
  d,8 d8 fis'8 d,8 a,8 d'8 |
  g8 d'8 b8 e8 g8 b8 |
  b,8 fis8 d'8 g8 d'8 b8 |
  a,8 d8 g8 a,8 cis'8 e'8 |
  d,8 d8 fis'8 d,8 a,8 d8 |
  d,8 d8 fis'8 a,8 d8 fis'8 |
  a,8 cis'8 e'8 a,8 d8 d'8 |
  d,8 e'8 gis'8 d,8 e'8 gis'8 |
  d,8 d8 fis'8 d,8 d8 fis'8 |
  g8 d'8 b8 e8 g8 b8 |
  a,8 cis'8 e'8 a,8 cis'8 e'8 |
  a,8 d8 fis'8 a,8 cis'8 e'8 |
  d,8 d8 fis'8 d,8 a,8 d8 |
  d,2. |
  a,2. |
  d,2. |
  d,2. |
  s2. |
  s2.
}

\score {
  \new Staff \with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } << \global \new Voice { \voiceOne \vUn } \new Voice { \voiceTwo \vDeux } >>
  \layout { }
}

\score {
  \new Staff \with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } << \global \new Voice { \voiceOne \vUn } \new Voice { \voiceTwo \vDeux } >>
  \midi { }
}
