\version "2.26.0"

\header {
  title = "Accord"
  subtitle = "pour guitare"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

ord = <>^\markup \italic "ord."
pont = <>^\markup \italic "sul pont."
tasto = <>^\markup \italic "sul tasto"
pizz = <>^\markup \italic "pizz."
tamb = <>^\markup \italic "tamb."

global = {
  \clef "treble_8" 
  \time 4/4 \accidentalStyle Score.modern \tempo "Lento, sospeso" 4 = 60 \mark \markup \box "I. Une note" s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \mark \markup \box "II. Diffraction" s8*8^\markup { \italic "laisser vibrer chaque mesure" }
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \tempo 4 = 54 \mark \markup \box "III. Halo" s8*8^\markup { \italic "harm. XII" }
  s8*8
  s8*8^\markup { \italic "harm. VII" }
  s8*8
  s8*8^\markup { \italic "harm. V et IV" }
  s8*8
  s8*8^\markup { \italic "harm. IV" }
  s8*8 \bar "||"
  \tempo "Secco, energico" 4 = 96 \mark \markup \box "IV. Matière" s8*8^\markup { \italic "golpe : frappe sur la table" }
  s8*8
  s8*8
  s8*8
  s8*8^\markup { \italic "rasgueado" }
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \tempo "Lento" 4 = 50 \mark \markup \box "V. Une note" s8*8
  s8*8
  s8*8
  s8*8 \bar "|."
}

vUn = {
  \ord e'2\1^\p e'2-1\2 |
  e'2-1\3 e'2-1\4 |
  <e'\1 e'\2-1>1 |
  \pont <e'\1 e'\2-1 e'\3-4>2^\p \tasto <e'\1 e'\2 e'\3>2 |
  \ord <e'\2-4 f'\1-1>1 |
  <dis'\3-3 e'\1 f'\2-1>1^\mp |
  dis'8.-3\3^\p e'16 f'4-1\2 e'8 dis'8-3\3 f'4-1\2 |
  c'8-4\4 d'8-1\3 fis'4-1\2 e'8 c'8-4\4 d'8.-1\3 fis'16-1\2 |
  d'16-4\4^\< e'16 fis'8-3\3 gis'4-1\2 e'8 d'8-4\4 gis'8-1\2 fis'8-3\3 |
  c'8-4\4 e'8-3\3 gis'8-3\2 b'4-1\1 gis'8-3\2 e'8-3\3 c'8-4\4 |
  a8-1\4^\mf d'8-1\3 g'8-2\2 c''8-2\1 g'8-2\2 d'8-1\3 a4-1\4 |
  e,8^\> a,8 d8 g8 b8 e'8 r4 |
  <e\harmonic\6>4^\p <a\harmonic\5>4 <d'\harmonic\4>4 <g'\harmonic\3>4 |
  <b'\harmonic\2>4 <e''\harmonic\1>4 r2 |
  <b''\harmonic\1>4 <fis''\harmonic\2>4 <d''\harmonic\3>4 <a'\harmonic\4>4 |
  <e'\harmonic\5>4 <b\harmonic\6>4 r2 |
  <e'\harmonic\6>8 <gis'\harmonic\6>8 <a'\harmonic\5>8 <cis''\harmonic\5>8 <d''\harmonic\4>8 <fis''\harmonic\4>8 <g''\harmonic\3>8 <b''\harmonic\3>8 |
  <b''\harmonic\2>8 <dis'''\harmonic\2>8 <e'''\harmonic\1>8 <gis'''\harmonic\1>8 r2 |
  <gis'\harmonic\6>4^\pp <cis''\harmonic\5>4 <fis''\harmonic\4>4 <b''\harmonic\3>4 |
  <dis'''\harmonic\2>4 <gis'''\harmonic\1>2. |
  \pizz <dis'\3-3 e'\1 f'\2-1>16->^\mf r16 <dis'\3 e'\1 f'\2>16 r16 r8 <dis'\3 e'\1 f'\2>16-> r16 r16 <dis'\3 e'\1 f'\2>16 r8 <dis'\3 e'\1 f'\2>8-> r8 |
  <dis'\3-3 e'\1 f'\2-1>16-> r16 r16 <dis'\3 e'\1 f'\2>16 r8 <dis'\3 e'\1 f'\2>16-> <dis'\3 e'\1 f'\2>16 r8 <dis'\3 e'\1 f'\2>8-> r16 <dis'\3 e'\1 f'\2>16 r8 |
  \tamb <e, a, d g b e'>4 \pizz <dis'\3-3 e'\1 f'\2-1>8 r8 \tamb <e, a, d g b e'>8 r8 \pizz <dis'\3-3 e'\1 f'\2-1>16 r16 <dis'\3 e'\1 f'\2>8 |
  \tamb <e, a, d g b e'>4 \pizz <dis'\3-3 e'\1 f'\2-1>8 <dis'\3 e'\1 f'\2>8 \tamb <e, a, d g b e'>8 r8 \pizz <dis'\3-3 e'\1 f'\2-1>16 <dis'\3 e'\1 f'\2>16 <dis'\3 e'\1 f'\2>8-> |
  \ord <f, ais, dis gis c' f'>8\arpeggio->^\f <f, ais, dis gis c' f'>8 <f, ais, dis gis c' f'>16 <f, ais, dis gis c' f'>16 <f, ais, dis gis c' f'>8\arpeggio-> <f, ais, dis gis c' f'>8 r8 <f, ais, dis gis c' f'>8\arpeggio-> <f, ais, dis gis c' f'>8 |
  <fis, b, e a cis' fis'>8\arpeggio-> <fis, b, e a cis' fis'>8 <fis, b, e a cis' fis'>16 <fis, b, e a cis' fis'>16 <fis, b, e a cis' fis'>8\arpeggio-> <fis, b, e a cis' fis'>8 r8 <fis, b, e a cis' fis'>8\arpeggio-> <fis, b, e a cis' fis'>8 |
  <g, c f ais d' g'>8\arpeggio-> <g, c f ais d' g'>8 <g, c f ais d' g'>16 <g, c f ais d' g'>16 <g, c f ais d' g'>8\arpeggio-> <g, c f ais d' g'>8 r8 <g, c f ais d' g'>8\arpeggio-> <g, c f ais d' g'>8 |
  <a, d g c' e' a'>8\arpeggio-> <a, d g c' e' a'>8 <a, d g c' e' a'>16 <a, d g c' e' a'>16 <a, d g c' e' a'>8\arpeggio-> <a, d g c' e' a'>8 r8 <a, d g c' e' a'>8\arpeggio-> <a, d g c' e' a'>8 |
  <e, a, d g b e'>16\arpeggio->^\fff <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16\arpeggio-> <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16\arpeggio-> <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16\arpeggio-> <e, a, d g b e'>16 <e, a, d g b e'>16 <e, a, d g b e'>16 |
  <e, a, d g b e'>2\arpeggio-> r2 |
  R1 |
  R1\fermata |
  <e''\harmonic\1>1^\p |
  <e'\1 e'\2-1>1 |
  \tasto e'1-1\4^\pp |
  r1\fermata
}

vDeux = {
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  \xNotesOn c4\mf r4 c4 r4 \xNotesOff |
  \xNotesOn c4 r8 c8 r4 c4 \xNotesOff |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  \xNotesOn c4\p r2. \xNotesOff |
  s1 |
  s1 |
  s1 |
  s1 |
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
