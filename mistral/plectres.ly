\version "2.26.0"

\header {
  title = "Mistral"
  subtitle = "pour orchestre à plectres"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \time 3,3,2 8/8 \tempo "Con energia" 4 = 112 s1
  s1
  s1
  s1
  \mark \default s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  \mark \default s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1^\markup { \italic "rit." }
  s1 \bar "||"
  \time 4/4 \tempo "Meno mosso, cantabile" 4 = 80 \mark \default s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1^\markup { \italic "poco rit." } \bar "||"
  \time 3,3,2 8/8 \tempo "Tempo I" 4 = 112 \mark \default s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  \time 2,2,3 7/8 s8*7
  s8*7
  \time 3,3,2 8/8 s1
  s1 \bar "||"
  \mark \default s1
  s1
  s1
  s1
  s1
  s1
  s1
  s1
  \mark \default s1
  s1
  s1
  s1
  s1
  s1
  s1^\markup { \italic "allargando" }
  s1 \bar "|."
}

mandolineI = {
  \clef "treble" \key e \minor
  R1 |
  R1 |
  R1 |
  R1 |
  b'8\mf e''8 fis''8 g''4.:32 fis''8 e''8 |
  d''4.:32 b'4.:32 a'8 b'8 |
  b'8 e''8 fis''8 g''4.:32 a''8 b''8 |
  a''4.:32 fis''4:32 d''4.:32 |
  b'8 e''8 fis''8 g''4.:32 fis''8 e''8 |
  d''4.:32 b'4.:32 e''8 fis''8 |
  g''4.:32 fis''4.:32 e''8 d''8 |
  e''2.:32 r4 |
  b''1:32\p |
  b''2:32 a''2:32 |
  g''1:32 |
  fis''1:32 |
  g''4.:32 b''4.:32 a''8 g''8 |
  e''4.:32 b''4.:32 g''8 a''8 |
  c'''4.:32 a''4.:32 fis''8 a''8 |
  g''2.:32 r4 |
  b'8\mf e''8 fis''8 g''4.:32 r4 |
  g''1:32\p |
  e''1:32 |
  d''8\mp g''8 a''8 b''4.:32 r4 |
  b'4:32\p e''4:32 fis''4:32 g''4:32~ |
  g''2:32 fis''4:32 e''4:32 |
  d''2.:32 b'4:32~ |
  b'2:32 a'4:32 b'4:32 |
  b'4:32\< e''4:32 fis''4:32 g''4:32~ |
  g''2:32 a''4:32 b''4:32 |
  a''2.:32\mf fis''4:32~ |
  fis''4:32\> d''2.:32 |
  a''1:32\p |
  g''1:32 |
  g''2:32 fis''2:32 |
  e''1:32 |
  e''2.:32 fis''4:32 |
  fis''1:32 |
  g''1:32 |
  fis''1:32 |
  R1 |
  R1 |
  R1 |
  R1 |
  fis'8\mf b'8 cis''8 d''4.:32 cis''8 b'8 |
  a'4.:32 fis'4.:32 e'8 fis'8 |
  b'8\f e''8 fis''8 g''4.:32 r4 |
  r4. c''8 f''8 g''8 a''4:32 |
  a''8->\f fis''8 a''8-> fis''8 a''8-> fis''8 d''8 |
  fis''8-> dis''8 fis''8-> dis''8 fis''8-> dis''8 b'8 |
  fis''4.:32\< a''4.:32 b''4:32 |
  b''4.:32 a''4.:32 fis''8 dis''8 |
  b'8\ff e''8 fis''8 g''4.:32 fis''8 e''8 |
  d''4.:32 b'4.:32 a'8 b'8 |
  b'8 e''8 fis''8 g''4.:32 a''8 b''8 |
  a''4.:32 fis''4:32 d''4.:32 |
  b'8 e''8 fis''8 g''4.:32 fis''8 e''8 |
  d''4.:32 b'4.:32 e''8 fis''8 |
  g''4.:32 fis''4.:32 e''8 d''8 |
  e''2.:32 r4 |
  b'4.:32\f e''4.:32 fis''4:32 |
  g''1:32 |
  b'4.:32 e''4.:32 fis''4:32 |
  g''2:32 a''2:32\< |
  b''1:32\ff |
  b'8 e''8 fis''8 g''4.-> fis''8 e''8 |
  g''4.:32 a''4.:32 a''4:32 |
  <g'' e'''>4->\sfz r8 r4. r4
}

mandolineII = {
  \clef "treble" \key e \minor
  R1 |
  R1 |
  R1 |
  r8\mp <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <fis' a'>8-. <fis' a'>8-. r8 <fis' a'>8-. <fis' a'>8-. r8 <fis' a'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <e' g'>8-. <e' g'>8-. r8 <e' g'>8-. <e' g'>8-. r8 <e' g'>8-. |
  r8 <e' g'>8-. <e' g'>8-. r8 <fis' a'>8-. <fis' a'>8-. r8 <fis' a'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8\mp <b' e''>8-. <b' e''>8-. r8 <b' e''>8-. <b' e''>8-. <b' e''>4-> |
  r8 <b' d''>8-. <b' d''>8-. r8 <b' d''>8-. <b' d''>8-. <b' d''>4-> |
  r8 <b' e''>8-. <b' e''>8-. r8 <b' e''>8-. <b' e''>8-. <b' e''>4-> |
  r8 <a' d''>8-. <a' d''>8-. r8 <a' d''>8-. <a' d''>8-. <a' d''>4-> |
  r8 <b' e''>8-. <b' e''>8-. r8 <b' e''>8-. <b' e''>8-. <b' e''>4-> |
  r8 <b' e''>8-. <b' e''>8-. r8 <b' e''>8-. <b' e''>8-. <b' e''>4-> |
  r8 <c'' e''>8-. <c'' e''>8-. r8 <a' d''>8-. <a' d''>8-. <a' d''>4-> |
  r8 <b' e''>8-. <b' e''>8-. r8 <b' e''>8-. <b' e''>8-. <b' e''>4-> |
  R1 |
  g'8\mf c''8 d''8 e''4.:32 r4 |
  c''1:32\p |
  b'2.:32 r4 |
  e'1:32\pp |
  e'1:32 |
  fis'1:32 |
  g'1:32 |
  e'1:32 |
  g'1:32 |
  fis'1:32 |
  e'1:32 |
  c''1:32\pp |
  b'1:32 |
  d''1:32 |
  b'1:32 |
  c''2.:32 a'4:32 |
  b'1:32 |
  c''1:32 |
  b'2:32 a'2:32 |
  R1 |
  R1 |
  e'8\mp a'8 b'8 c''4.:32 b'8 a'8 |
  g'4.:32 e'4.:32 d'8 e'8 |
  d'4.:32 fis'4.:32 e'8 d'8 |
  fis'4.:32 d'4.:32 cis'8 d'8 |
  r4. g'8\f c''8 d''8 e''4:32 |
  e''4.:32 a'4.:32 a'4:32 |
  d''8-> a'8 d''8-> a'8 d''8-> a'8 fis'8 |
  b'8-> fis'8 b'8-> fis'8 b'8-> fis'8 dis'8 |
  a'4.:32\< b'4.:32 dis''4:32 |
  dis''4.:32 fis''4.:32 dis''8 b'8 |
  g'8\ff b'8 d''8 e''4.:32 d''8 b'8 |
  b'4.:32 g'4.:32 fis'8 g'8 |
  g'8 b'8 d''8 e''4.:32 fis''8 g''8 |
  fis''4.:32 d''4:32 a'4.:32 |
  g'8 b'8 d''8 e''4.:32 d''8 b'8 |
  b'4.:32 g'4.:32 c''8 d''8 |
  e''4.:32 d''4.:32 c''8 a'8 |
  b'2.:32 r4 |
  r8\f <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. <g' b'>8-. r8 <g' b'>8-. |
  r8 <fis' a'>8-. <fis' a'>8-. r8 <fis' a'>8-. <fis' a'>8-. r8 <fis' a'>8-. |
  <e'' g''>1:32\ff |
  b8 e'8 fis'8 g'4.-> fis'8 e'8 |
  e''4.:32 fis''4.:32 fis''4:32 |
  <b' e''>4->\sfz r8 r4. r4
}

mandole = {
  \clef "treble_8" \key e \minor
  R1 |
  R1 |
  b1:32\pp~ |
  b1:32\< |
  b1:32\mp |
  b1:32 |
  b1:32 |
  a1:32 |
  b1:32 |
  c'1:32 |
  c'4.:32 a2:32 r8 |
  b1:32 |
  b8\mf e'8 fis'8 g'4.:32 fis'8 e'8 |
  d'4.:32 b4.:32 a8 b8 |
  b8 e'8 fis'8 g'4.:32 a'8 b'8 |
  a'4.:32 fis'4:32 d'4.:32 |
  b8 e'8 fis'8 g'4.:32 fis'8 e'8 |
  d'4.:32 b4.:32 e'8 fis'8 |
  g'4.:32 fis'4.:32 e'8 d'8 |
  e'2.:32 r4 |
  b1:32\p |
  c'1:32 |
  e8\mf a8 b8 c'4.:32 r4 |
  g2.:32\p r4 |
  g1:32\pp |
  g1:32 |
  a1:32 |
  b1:32 |
  g1:32 |
  b1:32 |
  a1:32 |
  b1:32 |
  b4:32\mp e'4:32 fis'4:32 g'4:32~ |
  g'2:32 fis'4:32 e'4:32 |
  d'2.:32 b4:32~ |
  b2:32 e'4:32 fis'4:32 |
  g'2.:32 fis'4:32~ |
  fis'2:32 e'4:32 d'4:32 |
  e'1:32~ |
  e'2:32 dis'2:32 |
  b8\p e'8 fis'8 g'4.:32 fis'8 e'8 |
  d'4.:32 b4.:32 a8 b8 |
  c'4.:32 e'4.:32 d'8 c'8 |
  e'8 d'8 c'8 g4.:32 b8 c'8 |
  b4.:32 a4.:32 g8 fis8 |
  d4.:32 d'4.:32 a8 d8 |
  <e b>4.:32\f <c g>4.:32 <c g>4:32 |
  e8 a8 b8 c'4.:32 r4 |
  fis'8-> d'8 fis'8-> d'8 fis'8-> d'8 a8 |
  dis'8-> b8 dis'8-> b8 dis'8-> b8 fis8 |
  b4.:32\< dis'4.:32 fis'4:32 |
  a4.:32 b4.:32 a8 fis8 |
  b1:32\ff |
  b2:32 a2:32 |
  g1:32 |
  fis1:32 |
  g4.:32 b4.:32 a8 g8 |
  e4.:32 b4.:32 g8 a8 |
  c'4.:32 a4.:32 fis8 a8 |
  g2.:32 r4 |
  <e b>1:32\f |
  <e b>1:32 |
  <c g>1:32 |
  <d a>1:32 |
  <e b>1:32\ff |
  b8 e'8 fis'8 g'4.-> fis'8 e'8 |
  <c g>4.:32 <d a>4.:32 <d a>4:32 |
  <e b>4->\sfz r8 r4. r4
}

guitare = {
  \clef "treble_8" \key e \minor
  e,8->\p b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  e,8->\< b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  e,8->\mf b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  g,8-> d8 b8 g,8-> d8 a8 g,8-> d8 |
  e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  d8-> a8 fis'8 d8-> a8 e'8 d8-> a8 |
  e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  c8-> g8 b8 c8-> g8 e'8 c8-> g8 |
  a,8-> e8 g8 d8-> a8 fis'8 d8-> a8 |
  e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  <e, b, e g b>8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  <g, d g b>8-> d8 b8 g,8-> d8 a8 g,8-> d8 |
  <e, b, e g b>8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  <d a d' fis'>8-> a8 fis'8 d8-> a8 e'8 d8-> a8 |
  <e, b, e g b>8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  <c g c' e'>8-> g8 b8 c8-> g8 e'8 c8-> g8 |
  <a, e a c'>8-> e8 g8 d8-> a8 fis'8 d8-> a8 |
  <e, b, e g b>8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  e,8->\mp b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  c8-> g8 b8 c8-> g8 e'8 c8-> g8 |
  <a, e a c' e'>1\p |
  b,2. r4 |
  c8\p g8 b8 e'8 g'8 e'8 b8 g8 |
  a,8 e8 g8 c'8 e'8 c'8 g8 e8 |
  b,8 fis8 a8 d'8 fis'8 d'8 a8 fis8 |
  e,8 b,8 g8 d'8 e'8 d'8 g8 b,8 |
  c8 g8 b8 e'8 fis'8 e'8 b8 g8 |
  b,8 g8 d'8 g'8 a'8 g'8 d'8 g8 |
  a,8 fis8 a8 d'8 e'8 d'8 a8 fis8 |
  g,8 e8 b8 d'8 fis'8 d'8 b8 e8 |
  a,8 e8 g8 c'8 e'8 c'8 g8 e8 |
  e,8 b,8 g8 b8 fis'8 b8 g8 b,8 |
  g,8 d8 g8 b8 d'8 b8 g8 d8 |
  c8 g8 b8 e'8 fis'8 e'8 b8 g8 |
  a,8 e8 g8 c'8 e'8 c'8 d8 a8 |
  b,8 fis8 a8 d'8 fis'8 d'8 a8 fis8 |
  c8 g8 b8 e'8 g'8 e'8 b8 g8 |
  b,8 fis8 a8 e'8 b,8 fis8 a8 dis'8 |
  e,8->\pp b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  g,8-> d8 b8 g,8-> d8 a8 g,8-> d8 |
  a,8-> e8 c'8 a,8-> e8 b8 a,8-> g8 |
  c8-> g8 b8 c8-> g8 e'8 c8-> g8 |
  b,8->\mp fis8 d'8 b,8-> fis8 cis'8 b,8-> a8 |
  d8-> a8 fis'8 d8-> a8 e'8 d8-> a8 |
  e,8->\mf b,8 g8 c8-> g8 e'8 c8-> g8 |
  a,8-> e8 c'8 f,8-> c8 a8 f,8-> c8 |
  <d a d' fis'>8->\f d8 <d a d' fis'>8-> d8 <d a d' fis'>8-> d8 d8 |
  <b, fis b dis'>8-> b,8 <b, fis b dis'>8-> b,8 <b, fis b dis'>8-> b,8 b,8 |
  b,8\mf\< b,8 b,8 b,8 b,8 b,8 b,8 b,8 |
  <b, dis a b fis'>8-> b,8 b,8 <b, dis a b fis'>8-> b,8 b,8 <b, dis a b fis'>8-> <b, dis a b fis'>8-> |
  <e, b, e g b e'>8->\ff <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 |
  <g, b, d g b g'>8-> <g, b, d g b g'>8 <g, b, d g b g'>8 <g, b, d g b g'>8-> <g, b, d g b g'>8 <g, b, d g b g'>8 <g, b, d g b g'>8-> <g, b, d g b g'>8 |
  <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 |
  <d a d' fis'>8-> <d a d' fis'>8 <d a d' fis'>8 <d a d' fis'>8-> <d a d' fis'>8 <d a d' fis'>8 <d a d' fis'>8-> <d a d' fis'>8 |
  <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 |
  <c e g c' e'>8-> <c e g c' e'>8 <c e g c' e'>8 <c e g c' e'>8-> <c e g c' e'>8 <c e g c' e'>8 <c e g c' e'>8-> <c e g c' e'>8 |
  <a, e a c' e'>8-> <a, e a c' e'>8 <a, e a c' e'>8 <d a d' fis'>8-> <d a d' fis'>8 <d a d' fis'>8 <d a d' fis'>8-> <d a d' fis'>8 |
  <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 |
  e,8->\f b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  e,8-> b,8 g8 e,8-> b,8 fis8 e,8-> d8 |
  c8-> g8 b8 c8-> g8 e'8 c8-> g8 |
  d8-> a8 fis'8 d8-> a8 e'8 d8-> a8 |
  <e, b, e g b e'>8->\ff <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 <e, b, e g b e'>8 <e, b, e g b e'>8-> <e, b, e g b e'>8 |
  b,8 e8 fis8 g4.-> fis8 e8 |
  <c e g c' e'>4.-> <d a d' fis'>4.-> <d a d' fis'>4-> |
  <e, b, e g b e'>4->\sfz r8 r4. r4
}

\book {
  \score {
    \new StaffGroup <<
      \new Staff \with { instrumentName = "Mandoline 1" shortInstrumentName = "Md. 1" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineI >>
      \new Staff \with { instrumentName = "Mandoline 2" shortInstrumentName = "Md. 2" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineII >>
      \new Staff \with { instrumentName = "Mandole" shortInstrumentName = "Mdl." midiInstrument = "acoustic guitar (steel)" } << \global \mandole >>
      \new Staff \with { instrumentName = "Guitare" shortInstrumentName = "Gt." midiInstrument = "acoustic guitar (nylon)" } << \global \guitare >>
    >>
    \layout { }
  }
  \score {
    \new StaffGroup <<
      \new Staff \with { instrumentName = "Mandoline 1" shortInstrumentName = "Md. 1" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineI >>
      \new Staff \with { instrumentName = "Mandoline 2" shortInstrumentName = "Md. 2" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineII >>
      \new Staff \with { instrumentName = "Mandole" shortInstrumentName = "Mdl." midiInstrument = "acoustic guitar (steel)" } << \global \mandole >>
      \new Staff \with { instrumentName = "Guitare" shortInstrumentName = "Gt." midiInstrument = "acoustic guitar (nylon)" } << \global \guitare >>
    >>
    \midi { }
  }
}

\book {
  \bookOutputSuffix "mandolineI"
  \header { instrument = "Mandoline 1" }
  \score {
    \new Staff << \global \compressMMRests \mandolineI >>
    \layout { }
  }
}

\book {
  \bookOutputSuffix "mandolineII"
  \header { instrument = "Mandoline 2" }
  \score {
    \new Staff << \global \compressMMRests \mandolineII >>
    \layout { }
  }
}

\book {
  \bookOutputSuffix "mandole"
  \header { instrument = "Mandole" }
  \score {
    \new Staff << \global \compressMMRests \mandole >>
    \layout { }
  }
}

\book {
  \bookOutputSuffix "guitare"
  \header { instrument = "Guitare" }
  \score {
    \new Staff << \global \compressMMRests \guitare >>
    \layout { }
  }
}
