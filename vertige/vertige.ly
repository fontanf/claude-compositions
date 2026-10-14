\version "2.26.0"

\header {
  title = "Vertige"
  subtitle = "toccata pour guitare"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \clef "treble_8" \key fis \minor
  \time 2/4 \tempo "Presto, con fuoco" 4 = 120 \mark \markup \box "A" s8*4^\markup { \italic "pouce marcato, pédale i-m légère" }
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4 \bar "||"
  \mark \markup \box "A2" s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4 \bar "||"
  \mark \markup \box "B" s8*4^\markup { \italic "rasgueado" }
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4 \bar "||"
  \tempo "Meno mosso, cantabile" 4 = 84 \mark \markup \box "Trio" \key a \major s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4^\markup { \italic "rit." } \bar "||"
  \tempo "Tempo I" 4 = 120 \key fis \minor s8*4
  s8*4
  s8*4
  s8*4 \bar "||"
  \mark \markup \box "A’" s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4
  s8*4 \bar "||"
  \mark \markup \box "Coda" s8*4
  s8*4
  s8*4
  s8*4
  s8*4^\markup { \italic "allargando" }
  s8*4 \bar "|."
}

vUn = {
  r16^\p b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16-1-\3 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16-1-\3 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16-1-\3 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  r16 e'16 b16 r16 e'16 b16 r16 b16 |
  <fis,-1 cis-3 fis-4 a-1 cis'-1 fis'-1>16\arpeggio->^\ff^"C II" <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16\arpeggio-> <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>8\arpeggio-> |
  <fis,-1 cis-3 fis-4 a-1 cis'-1 fis'-1>16\arpeggio-> <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16\arpeggio-> <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>8\arpeggio-> |
  <a, e-2 a-3 c'-1 e'>16\arpeggio-> <a, e a c' e'>16 <a, e a c' e'>16 <a, e a c' e'>16\arpeggio-> <a, e a c' e'>16 <a, e a c' e'>16 <a, e a c' e'>8\arpeggio-> |
  <a, e-2 a-3 c'-1 e'>16\arpeggio-> <a, e a c' e'>16 <a, e a c' e'>16 <a, e a c' e'>16\arpeggio-> <a, e a c' e'>16 <a, e a c' e'>16 <a, e a c' e'>8\arpeggio-> |
  <c-1 g-3-\4 c'-4-\3 ees'-2>16\arpeggio-> <c g c' ees'>16 <c g c' ees'>16 <c g c' ees'>16\arpeggio-> <c g c' ees'>16 <c g c' ees'>16 <c g c' ees'>8\arpeggio-> |
  <c-1 g-3-\4 c'-4-\3 ees'-2>16\arpeggio-> <c g c' ees'>16 <c g c' ees'>16 <c g c' ees'>16\arpeggio-> <c g c' ees'>16 <c g c' ees'>16 <c g c' ees'>8\arpeggio-> |
  <ees-1 bes-3 ees'-4 ges'-2>16\arpeggio-> <ees bes ees' ges'>16 <ees bes ees' ges'>16 <ees bes ees' ges'>16\arpeggio-> <ees bes ees' ges'>16 <ees bes ees' ges'>16 <ees bes ees' ges'>8\arpeggio-> |
  <ees-1 bes-3 ees'-4 ges'-2>16\arpeggio-> <ees bes ees' ges'>16 <ees bes ees' ges'>16 <ees bes ees' ges'>16\arpeggio-> <ees bes ees' ges'>16 <ees bes ees' ges'>16 <ees bes ees' ges'>8\arpeggio-> |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 c'16-1 e'16 r16 c'16-1 e'16 r16 e'16 |
  r16 ees'16-2 g'16-1 r16 ees'16-2 g'16-1 r16 g'16-1 |
  r16 ges'16-1 bes'16-1 r16 ges'16-1 bes'16-1 r16 bes'16-1 |
  r16 ees'16-2 g'16-1 r16 ees'16-2 g'16-1 r16 g'16-1 |
  r16 c'16-1 e'16 r16 c'16-1 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 e'16 b16 r16 e'16 b16 r16 gis'16-1 |
  <cis''-3-\2 e''-1>4^\p <a'-4-\2 cis''-3>4 |
  <b'-4-\2 d''-4>8 <a'-4-\2 cis''-3>8 <gis'-3-\2 b'-1>4^"C VII" |
  <fis'-3-\2 a'-1>4 <a'-4-\2 cis''-3>4 |
  <gis'-3-\2 b'-1>2^"C VII" |
  <cis''-3-\2 e''-1>4 <d''-2-\2 fis''-1>4 |
  <cis''-4-\2 e''-4>8 <b'-4-\2 d''-2>8 <a'-2-\2 cis''-1>4 |
  <gis'-3-\2 b'-1>4 <b'-4-\2 d''-4>4 |
  <a'-4-\2 cis''-3>2 |
  <d''-2-\2 fis''-1>4^\mp <cis''-4-\2 e''-1>4 |
  <b'-4-\2 d''-4>8 <a'-4-\2 cis''-3>8 <gis'-3-\2 b'-1>4^"C VII" |
  <fis'-4-\2 a'-1>4 <e'-2-\2 gis'-1>4 |
  <cis'-2-\3 a'-1>2^\p |
  fis''16-2(^\mf^\< eis''16-1) d''16-4( cis''16-3) b'16-1( a'16-4) gis'16-3( fis'16-1) |
  eis'16-1( d'16-3) cis'16-2( b16) a16-2( gis16-1) fis16-4( eis16-3) |
  <cis-3 eis-2 b-4-\3 cis'-1>16\arpeggio->^\ff <cis eis b cis'>16 <cis eis b cis'>16 <cis eis b cis'>16\arpeggio-> <cis eis b cis'>16 <cis eis b cis'>16 <cis eis b cis'>8\arpeggio-> |
  <cis-3 eis-2 b-4-\3 cis'-1>8\arpeggio-> r8 r4\fermata |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16-1-\3 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  r16 b16 e'16 r16 b16 e'16 r16 e'16 |
  fis8.-3->^\ff a8.-1 cis'8-1 |
  b8.-> a8.-2 gis8-1 |
  fis8.-3-> a8.-1 d'8-2 |
  cis'8.-1-> d'8.-2 cis'8-1 |
  b8.-> a8.-2 gis8-1 |
  a8.-1-> b8. cis'8-1 |
  d'8.-2-> cis'8.-1 b8 |
  fis8.-3-> cis'8.-1 fis8-3 |
  <fis,-1 cis-3 fis-4 a-1 cis'-1 fis'-1>16\arpeggio->^\fff^"C II" <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16\arpeggio-> <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>8\arpeggio-> |
  <d a-1 d'-2 fis'-1>16\arpeggio->^"½C II" <d a d' fis'>16 <d a d' fis'>16 <d a d' fis'>16\arpeggio-> <d a d' fis'>16 <d a d' fis'>16 <d a d' fis'>8\arpeggio-> |
  <cis-3 eis-2 b-4-\3 cis'-1>16\arpeggio-> <cis eis b cis'>16 <cis eis b cis'>16 <cis eis b cis'>16\arpeggio-> <cis eis b cis'>16 <cis eis b cis'>16 <cis eis b cis'>8\arpeggio-> |
  <fis,-1 cis-3 fis-4 a-1 cis'-1 fis'-1>16\arpeggio->^"C II" <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16\arpeggio-> <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>16 <fis, cis fis a cis' fis'>8\arpeggio-> |
  <d a-1 d'-2 fis'-1>8\arpeggio->^"½C II" <d a d' fis'>8\arpeggio-> <cis-3 eis-2 b-4-\3 cis'-1>8\arpeggio-> <cis eis b cis'>8\arpeggio-> |
  <fis,-1 cis-3 fis-4 a-1 cis'-1 fis'-1>8\arpeggio->^\sfz^"C II" r8 r4\fermata
}

vDeux = {
  fis8._3->\mf a8._1 cis'8_1 |
  b8.-> a8._2 gis8_1 |
  fis8._3-> a8._1 d'8_2 |
  cis'8._1-> b8. cis'8_1 |
  fis8._3-> a8._1 cis'8_1 |
  d'8._2-> cis'8._1 b8 |
  a8._2-> gis8._1 fis8_4 |
  cis8._1-> gis,8._1 cis8_1 |
  fis8._3-> a8._1 cis'8_1 |
  b8.-> a8._2 gis8_1 |
  fis8._3-> a8._1 d'8_2 |
  cis'8._1-> d'8._2 cis'8_1 |
  b8.-> a8._2 gis8_1 |
  a8._1-> b8. cis'8_1 |
  d'8._2-> cis'8._1 b8 |
  fis8._3-> cis8._3 fis,8_1 |
  fis,8._1->\f a,8. cis8_3 |
  b,8._1-> a,8. gis,8_3 |
  fis,8._1-> a,8. d8 |
  cis8._3-> b,8._1 cis8_3 |
  fis,8._1-> a,8. cis8_3 |
  d8.-> cis8._3 b,8_1 |
  a,8.-> gis,8._3 fis,8_1 |
  cis8._1-> gis,8._1 cis8_1 |
  fis,8._1-> a,8. cis8_3 |
  b,8._1-> a,8. gis,8_3 |
  fis,8._1-> a,8. d8 |
  cis8._1-> d8. cis8_1 |
  b,8._1-> a,8. gis,8_3 |
  a,8.-> b,8._1 cis8_3 |
  d8.-> cis8._3 b,8_1 |
  fis8._3-> cis8._3 fis,8_1 |
  s2 |
  s2 |
  s2 |
  s2 |
  s2 |
  s2 |
  s2 |
  s2 |
  fis8._3->\f a8._1 cis'8_1 |
  a,8.-> c8._2 e8_1 |
  c8._3-> ees8._1 g8 |
  ees8._1-> ges8._4 bes8_3 |
  c8._3-> ees8._1 g8 |
  a,8.-> c8._2 e8_1 |
  fis8._3-> a8._1 cis'8_1 |
  e8._2-> gis8._1 b8 |
  a,4 e4_1_\5 |
  b,4_1_\6 e4_1_\5 |
  a,4 e4_1_\5 |
  e2_1_\5 |
  a,4 d4 |
  cis4_1_\6 a,4 |
  d4 b,4_1_\6 |
  e2_1_\5 |
  d4 fis4_1_\6 |
  b,4_1_\6 e4_1_\5 |
  e4_1_\5 e,4 |
  a,2 |
  s2 |
  s2 |
  s2 |
  s2 |
  fis8._3->\ff a8._1 cis'8_1 |
  b8.-> a8._2 gis8_1 |
  fis8._3-> a8._1 d'8_2 |
  cis'8._1-> b8. cis'8_1 |
  fis8._3-> a8._1 cis'8_1 |
  d'8._2-> cis'8._1 b8 |
  a8._2-> gis8._1 fis8_4 |
  cis8._1-> gis,8._1 cis8_1 |
  fis,8._1 a,8. cis8_3 |
  b,8._1 a,8. gis,8_3 |
  fis,8._1 a,8. d8 |
  cis8._1 d8. cis8_1 |
  b,8._1 a,8. gis,8_3 |
  a,8. b,8._1 cis8_3 |
  d8. cis8._3 b,8_1 |
  fis,8._1 cis8._3 fis,8_1 |
  s2 |
  s2 |
  s2 |
  s2 |
  s2 |
  s2
}

\score {
  \new Staff \with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } << \global \new Voice { \voiceOne \vUn } \new Voice { \voiceTwo \vDeux } >>
  \layout { }
}

\score {
  \new Staff \with { instrumentName = "Guitare" midiInstrument = "acoustic guitar (nylon)" } << \global \new Voice { \voiceOne \vUn } \new Voice { \voiceTwo \vDeux } >>
  \midi { }
}
