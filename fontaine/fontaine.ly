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
  fis''4-4^\p e''8-3 d''4.-1^"½C X" |
  e''4-4 fis''8-4 a'4.-4^"½C II" |
  b'4-2 cis''8-4 d''4-2 e''8-4 |
  fis''4.-4^\< a''4.-4 |
  g''4-4^\mp fis''8-4 e''4.-1 |
  d''4-4 cis''8-4 b'4.-1^"½C VII" |
  a'4-1^"½C V" b'8-3 cis''4-1^"½C IX" e''8-4 |
  d''2.-1^"½C X" |
  fis''4-4 e''8-3 d''4.-1^"½C X" |
  e''4-4^\< fis''8-4 a''4.-4 |
  gis''4-4^\mf fis''8-4 e''4.-1^"½C XII" |
  fis''4-4 e''8-3 d''4-4 b'8-1 |
  g''4-4 fis''8-4 e''4-4 d''8-4 |
  cis''4-3 d''8-4 e''4.-4 |
  fis''4.-4^\> e''4.-4 |
  d''4.-1^\p^"½C X" r4. |
  f'16-1(^\mf e'16) g'16-3( e'16) a'16-3( e'16) bes'16-4( e'16) a'16-3( e'16) g'16-1( e'16) |
  f'16-1( e'16) g'16-3( e'16) a'16-1( e'16) d''16-3( e'16) c''16-1( e'16) bes'16-1( e'16) |
  a'16-1( e'16) bes'16-2( e'16) c''16-4( e'16) d''16-3( e'16) c''16-1( e'16) bes'16-1( e'16) |
  a'16-3( e'16) g'16-1( e'16) f'16-1( e'16) d'16-3 e'16 f'16-1 g'16-3 a'16-1 bes'16-2 |
  f'16-1(^\f e'16) g'16-3( e'16) a'16-3( e'16) bes'16-4( e'16) a'16-3( e'16) g'16-1( e'16) |
  f'16-1( e'16) g'16-3( e'16) a'16-1( e'16) d''16-3( e'16) c''16-1( e'16) bes'16-1( e'16) |
  a'16-1( e'16) bes'16-2( e'16) c''16-4( e'16) d''16-3( e'16) c''16-1( e'16) bes'16-1( e'16) |
  a'16-3( e'16) g'16-1( e'16) f'16-1( e'16) d'16-3 e'16 f'16-1 g'16-3 a'16-1 bes'16-2 |
  g16^\p b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  g16 b16 e'16 b16 g16 b16 g16 b16 e'16 b16 g16 b16 |
  <d, a, d a-2 d'-3 f'-1>8\arpeggio->^\f <d, a, d a d' f'>8 <d, a, d a d' f'>8 <c-3 e-2 g c'-1 e'>8\arpeggio-> <c e g c' e'>8 <c e g c' e'>8 |
  <bes,-1 f-3 bes-4 d'-4 f'-1>8\arpeggio->^"C I" <bes, f bes d' f'>8 <bes, f bes d' f'>8 <a, e-1 a-1 cis'-1 e'>8\arpeggio->^"½C II" <a, e a cis' e'>8 <a, e a cis' e'>8 |
  <d, a, d a-2 d'-3 f'-1>4\arpeggio->^\ff <c-3 e-2 g c'-1 e'>4\arpeggio-> <bes,-1 f-3 bes-4 d'-4 f'-1>4\arpeggio->^"C I" |
  <a, e-1 g cis'-2 e'>4.\arpeggio-> a''16-3(^\> g''16-1 f''16-4 e''16-3 d''16-1 cis''16-1) |
  r32 fis''32-4^\p fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32-2 e''32 e''32 r32 d''32-1 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 |
  r32 e''32-4 e''32 e''32 r32 e''32 e''32 e''32 r32 fis''32-4 fis''32 fis''32 r32 a'32-4^"½C II" a'32 a'32 r32 a'32 a'32 a'32 r32 a'32 a'32 a'32 |
  r32 b'32-1^"½C VII" b'32 b'32 r32 b'32 b'32 b'32 r32 cis''32-4 cis''32 cis''32 r32 d''32-4 d''32 d''32 r32 d''32 d''32 d''32 r32 e''32-4 e''32 e''32 |
  r32 fis''32-4 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 a''32-4 a''32 a''32 r32 a''32 a''32 a''32 r32 a''32 a''32 a''32 |
  r32 g''32-4 g''32 g''32 r32 g''32 g''32 g''32 r32 fis''32-3 fis''32 fis''32 r32 e''32-4 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 d''32-4 d''32 d''32 r32 d''32 d''32 d''32 r32 cis''32-4 cis''32 cis''32 r32 b'32-4 b'32 b'32 r32 b'32 b'32 b'32 r32 b'32 b'32 b'32 |
  r32 a'32-1 a'32 a'32 r32 a'32 a'32 a'32 r32 b'32-3 b'32 b'32 r32 cis''32-1^"½C IX" cis''32 cis''32 r32 cis''32 cis''32 cis''32 r32 e''32-4 e''32 e''32 |
  r32 d''32-1 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32-1 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 |
  r32 fis''32-4 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32-2 e''32 e''32 r32 d''32-1 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 |
  r32 e''32-4 e''32 e''32 r32 e''32 e''32 e''32 r32 fis''32-4 fis''32 fis''32 r32 a''32-4 a''32 a''32 r32 a''32 a''32 a''32 r32 a''32 a''32 a''32 |
  r32 gis''32-4 gis''32 gis''32 r32 gis''32 gis''32 gis''32 r32 fis''32-3 fis''32 fis''32 r32 e''32-4^"½C IX" e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 fis''32-4 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32-2 e''32 e''32 r32 d''32-1 d''32 d''32 r32 d''32 d''32 d''32 r32 b'32-3-\2 b'32 b'32 |
  r32 g''32-4 g''32 g''32 r32 g''32 g''32 g''32 r32 fis''32-3 fis''32 fis''32 r32 e''32-4 e''32 e''32 r32 e''32 e''32 e''32 r32 d''32-4 d''32 d''32 |
  r32 cis''32-1^"½C IX" cis''32 cis''32 r32 cis''32 cis''32 cis''32 r32 d''32-2 d''32 d''32 r32 e''32-4 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 fis''32-4 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 fis''32 fis''32 fis''32 r32 e''32-4 e''32 e''32 r32 e''32 e''32 e''32 r32 e''32 e''32 e''32 |
  r32 d''32-1 d''32 d''32 r32 d''32 d''32 d''32 r32 d''32 d''32 d''32 r8 r8 r8 |
  <fis''\harmonic>4^"VII②"^\p <e''\harmonic>8^"XII①" <d''\harmonic>4.^"V④" |
  <e''\harmonic>4^"XII①" <fis''\harmonic>8^"VII②" <a'\harmonic>4.^"V⑤" |
  <b'\harmonic>4^"XII②" <cis''\harmonic>8^"IV⑤" <d''\harmonic>4^"V④" <e''\harmonic>8^"XII①" |
  <fis''\harmonic>2.^"VII②" |
  <d\harmonic a\harmonic d'\harmonic>2.^"XII⑥⑤④" |
  <d, a, d fis'-2-\3 a'-1-\2 d''-1>2.\arpeggio\fermata^\pp^"½C X"
}

vDeux = {
  d,16\pp d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 a,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 |
  a,16 cis'16_3_\4 e'16_1_\3 a'16_2_\2 e'16 cis'16 cis16_3 e16_1 a16_1 e'16_4_\2 a16 e16 |
  b,16_3_\6 fis16_4_\5 d'16_1_\3 b16 d'16 fis16 g16_1_\5 d'16_3_\4 b16 g'16_4_\3 b16 d'16 |
  d,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 d,16 fis'16_3_\4 a'16_1_\3 d''16_2_\2 a'16 fis'16 |
  g16_1_\5 d'16_3_\4 b16 g'16_4_\3 b16 d'16 e16_3_\6 g16 b16 e'16_4_\4 b16 g16 |
  b,16_3_\6 fis16_4_\5 d'16_1_\3 b16 d'16 fis16 g16_4_\5 d'16_1_\3 b16_3_\4 g'16_2_\2 b16 d'16 |
  a,16 d16 g16 e'16_1_\2 g16 d16 a,16 cis'16_3_\4 e'16_1_\3 a'16_2_\2 e'16 cis'16 |
  d,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 d,16 a,16 d16 fis'16_2_\3 d16 a,16 |
  d,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 a,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 |
  a,16 cis'16_3_\4 e'16_1_\3 a'16_2_\2 e'16 cis'16 a,16 fis'16_3_\4 a'16_1_\3 d''16_2_\2 a'16 fis'16 |
  d,16 e'16_3_\4 gis'16_2_\3 b'16_1_\2 gis'16 e'16 d,16 e'16_3_\4 gis'16_2_\3 b'16_1_\2 gis'16 e'16 |
  d,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 d,16 d16 fis'16_4_\3 b16 fis'16 d16 |
  g16_1_\5 d'16_3_\4 b16 g'16_4_\3 b16 d'16 e16_1_\5 g16 b16 d'16_4_\4 b16 g16 |
  a,16 cis'16_4_\4 e'16_2_\3 g'16_1_\2 e'16 cis'16 a,16 cis'16_3_\4 e'16_1_\3 a'16_2_\2 e'16 cis'16 |
  a,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 a,16 cis'16_4_\4 e'16_2_\3 g'16_1_\2 e'16 cis'16 |
  d,16 d16 fis'16_2_\3 a'16_1_\2 fis'16 d16 d,16 a,16 d16 a16_1 d16 a,16 |
  d,4.->\mf d,4.-> |
  d,4. d,4. |
  a,4.-> a,4.-> |
  a,4. a,4. |
  d,8->\f d8 d,8 d,8-> d8 d,8 |
  d,8-> d8 d,8 d,8-> d8 d,8 |
  a,8-> a8_1_\4 a,8 a,8-> a8_1_\4 a,8 |
  a,8-> a8_1 a,8 a,8-> a8_1 a,8 |
  f4_2\mf e8_1 d4. |
  e4_1 f8_2 a,4. |
  b,4_1 c8_2 d4 e8_1 |
  f4._1 a4._1_\4 |
  g4 f8_2 e4._1 |
  d4 cis8_1 d4. |
  s2. |
  s2. |
  s2. |
  s2. |
  d,8\pp d8 fis'8_1_\3 a,8 d8 fis'8_2_\3 |
  a,8 cis'8_3_\4 e'8_1_\3 cis8_3 e8_1 a8_1 |
  b,8_3_\6 fis8_4_\5 d'8_1_\3 g8_4_\5 d'8_1_\3 b8 |
  d,8 d8 fis'8_1_\3 d,8 fis'8_3_\4 a'8_1_\3 |
  g8 d'8_1_\4 b8 e8_1_\5 g8 b8 |
  b,8_3_\6 fis8_4_\5 d'8_1_\3 g8_1_\4 d'8_3_\3 b8 |
  a,8 d8 g8 a,8 cis'8_3_\4 e'8_1_\3 |
  d,8 d8 fis'8_2_\3 d,8 d8 fis'8_2_\3 |
  d,8 d8 fis'8_1_\3 a,8 d8 fis'8_2_\3 |
  a,8 cis'8_3_\4 e'8_1_\3 a,8 fis'8_3_\4 a'8_1_\3 |
  d,8 e'8_2_\4 gis'8_1_\3 d,8 e'8_1_\3 gis'8_1_\2 |
  d,8 d8 fis'8_1_\3 d,8 d8 fis'8_2_\3 |
  g8 d'8_1_\4 b8 e8_1_\5 g8 b8 |
  a,8 cis'8_3_\4 e'8_1_\3 a,8 cis'8_3_\4 e'8_1_\3 |
  a,8 d8 fis'8_1_\3 a,8 cis'8_3_\4 e'8_1_\3 |
  d,8 d8 fis'8_2_\3 d,8 a,8 fis8_1 |
  d,2. |
  d,2. |
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
