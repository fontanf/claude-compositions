\version "2.26.0"

\header {
  title = "Ce qui reste"
  subtitle = "pour orchestre à plectres"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \time 4/4 \tempo "Calme, chantant" 4 = 66 \mark \markup \box "I. Le souvenir" s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \mark \markup \box "II. Résumé" s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \mark \markup \box "III. Une note par mesure" s8*8^\markup { \italic "sans trémolo, laisser vibrer" }
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8
  s8*8 \bar "||"
  \mark \markup \box "IV. Le rythme seul" s8*8^\markup { \italic "cordes étouffées" }
  s8*8
  s8*8
  s8*8 \bar "||"
  \mark \markup \box "V. Un geste" s8*8
  s8*8 \bar "||"
  \time 3/4 \once \override Score.MetronomeMark.X-offset = #4 \tempo "Reconstruction" 4 = 72 \mark \markup \box "VI. Ce qui revient" s8*6
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
  s8*6
  s8*6^\markup { \italic "rit." }
  s8*6 \bar "|."
}

mandolineI = {
  \clef "treble" \key d \major
  a'4:32\mf d'4:32 e'8 fis'8 a'4:32 |
  b'2.:32 a'8 fis'8 |
  e''4:32 a'4:32 b'8 cis''8 e''4:32 |
  fis''2.:32 e''8 cis''8 |
  d''4:32 g'4:32 a'8 b'8 d''4:32 |
  e''2:32 d''4:32 b'4:32 |
  a'4:32 d'4:32 fis'4:32 e'4:32 |
  d'1:32 |
  a'2:32\p e'2:32 |
  b'1:32 |
  e''2:32 b'2:32 |
  fis''1:32 |
  d''2:32 a'2:32 |
  e''2:32 d''2:32 |
  a'2:32 fis'2:32 |
  d'1:32 |
  a'1\p |
  R1 |
  R1 |
  R1 |
  d''1 |
  R1 |
  R1 |
  d'1\pp |
  \xNotesOn b'8\p b'8 b'16 b'16 b'8 b'4. b'16 b'16 |
  b'8 b'8 b'16 b'16 b'8 b'4. b'16 b'16 |
  b'8\pp b'8 b'16 b'16 b'8 b'4 b'8 b'8 |
  b'8 b'8 b'8 b'8 b'2 \xNotesOff |
  a'2\pp\open d'2\open |
  R1\fermata |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  a'2:32\mf\< e''4:32 |
  d''4:32 cis''4:32 b'4:32 |
  e''2:32 b''4:32 |
  a''4:32 g''4:32 fis''4:32 |
  d''2:32\f a''4:32 |
  g''4:32 fis''4:32 e''4:32 |
  a'2:32\> e''4:32 |
  d''2.:32\mp |
  e''2.:32\pp\> |
  a'4\ppp\open d'2\open\fermata
}

mandolineII = {
  \clef "treble" \key d \major
  fis'1:32\p |
  d'1:32 |
  cis'1:32 |
  cis'1:32 |
  d'1:32 |
  b1:32 |
  a'1:32 |
  fis'1:32 |
  R1 |
  R1 |
  R1 |
  R1 |
  R1 |
  R1 |
  R1 |
  R1 |
  R1 |
  b'1\p |
  R1 |
  R1 |
  R1 |
  e''1 |
  R1 |
  R1 |
  \xNotesOn g'8\p g'8 g'16 g'16 g'8 g'4. g'16 g'16 |
  g'8 g'8 g'16 g'16 g'8 g'4. g'16 g'16 |
  g'8\pp g'8 g'16 g'16 g'8 g'4 g'8 g'8 |
  g'8 g'8 g'8 g'8 g'2 \xNotesOff |
  R1 |
  R1\fermata |
  R2. |
  R2. |
  R2. |
  R2. |
  e'2.:32\pp |
  d'2.:32 |
  e'2.:32 |
  fis'2.:32 |
  r4\mp a2:32 |
  r4 b2:32 |
  r4 e'2:32 |
  r4 fis'2:32 |
  r4 d'2:32 |
  r4 e'2:32 |
  r4 a2:32 |
  r4 d'2:32 |
  fis'2.:32\pp |
  R2.\fermata
}

mandole = \transpose c c' {
  \clef "treble" \key d \major
  <d a>1:32\p |
  <b, fis>1:32 |
  <a, e>1:32 |
  <fis cis'>1:32 |
  <g, d>1:32 |
  <e b>1:32 |
  <a, e>1:32 |
  <d a>1:32 |
  d1:32\pp |
  b,1:32 |
  a,1:32 |
  fis1:32 |
  g,1:32 |
  e1:32 |
  a,1:32 |
  d1:32 |
  R1 |
  R1 |
  e'1\p |
  R1 |
  R1 |
  R1 |
  a1 |
  R1 |
  \xNotesOn d'8\p d'8 d'16 d'16 d'8 d'4. d'16 d'16 |
  d'8 d'8 d'16 d'16 d'8 d'4. d'16 d'16 |
  d'8\pp d'8 d'16 d'16 d'8 d'4 d'8 d'8 |
  d'8 d'8 d'8 d'8 d'2 \xNotesOff |
  R1 |
  R1\fermata |
  a2\p e'4 |
  d'4 cis'4 b4 |
  e'2 b'4 |
  a'4 g'4 fis'4 |
  d'2:32 a'4:32 |
  g'4:32 fis'4:32 e'4:32 |
  a2:32 e'4:32 |
  d'2.:32 |
  d2.:32\mp |
  e2.:32 |
  fis2.:32 |
  g2.:32 |
  a2.:32 |
  b2.:32 |
  cis2.:32 |
  d2.:32 |
  <d a>2.:32\pp |
  R2.\fermata
}

guitare = {
  \clef "treble_8" \key d \major
  d8\mp a8 d'8 a8 e'8 a8 d'8 a8 |
  b,8 fis8 b8 fis8 d'8 fis8 b8 fis8 |
  a,8 e8 a8 e8 b8 e8 a8 e8 |
  fis,8 cis8 fis8 cis8 a8 cis8 fis8 cis8 |
  g,8 b,8 d8 b,8 a8 b,8 d8 b,8 |
  e,8 b,8 fis8 b,8 g8 b,8 fis8 b,8 |
  a,8 d8 a8 d8 fis'8 d8 a8 d8 |
  d8 a8 d'8 a8 e'8 a8 d'8 a8 |
  <d a d' e'>1\p |
  <b, fis b d'>1 |
  <a, e a b>1 |
  <fis, cis fis a>1 |
  <g, b, d a>1 |
  <e, b, fis g>1 |
  <a, d a fis'>1 |
  <d a d' e'>1 |
  d1\pp |
  R1 |
  a,1 |
  fis'1\p |
  g,1 |
  R1 |
  a,1 |
  R1 |
  \xNotesOn g8\p g8 g16 g16 g8 g4. g16 g16 |
  g8 g8 g16 g16 g8 g4. g16 g16 |
  g8\pp g8 g16 g16 g8 g4 g8 g8 |
  g8 g8 g8 g8 g2 \xNotesOff |
  R1 |
  R1\fermata |
  d8\pp a8 e'8 a8 e'8 a8 |
  e8 b8 d'8 b8 d'8 b8 |
  fis8 cis'8 e'8 cis'8 e'8 cis'8 |
  g8 b8 fis'8 b8 fis'8 b8 |
  a8 d'8 e'8 d'8 e'8 d'8 |
  b8 d'8 fis'8 d'8 fis'8 d'8 |
  cis8 e'8 a8 e'8 a8 e'8 |
  d8 a8 fis'8 a8 fis'8 a8 |
  d8\mf a8 e'8 a8 e'8 a8 |
  e8 b8 d'8 b8 d'8 b8 |
  fis8 cis'8 e'8 cis'8 e'8 cis'8 |
  g8 b8 fis'8 b8 fis'8 b8 |
  a8 d'8 e'8 d'8 e'8 d'8 |
  b8 d'8 fis'8 d'8 fis'8 d'8 |
  cis8 e'8 a8 e'8 a8 e'8 |
  d8 a8 fis'8 a8 fis'8 a8 |
  <d a d' fis'>2.\pp |
  R2.\fermata
}

\book {
  \score {
    \new StaffGroup <<
      \new Staff \with { instrumentName = "Mandoline 1" shortInstrumentName = "Md. 1" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineI >>
      \new Staff \with { instrumentName = "Mandoline 2" shortInstrumentName = "Md. 2" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineII >>
      \new Staff \with { instrumentName = "Mandole ténor" shortInstrumentName = "Mdl." midiInstrument = "acoustic guitar (steel)" } << \global { \transposition c \mandole } >>
      \new Staff \with { instrumentName = "Guitare" shortInstrumentName = "Gt." midiInstrument = "acoustic guitar (nylon)" } << \global \guitare >>
    >>
    \layout { }
  }
  \score {
    \new StaffGroup <<
      \new Staff \with { instrumentName = "Mandoline 1" shortInstrumentName = "Md. 1" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineI >>
      \new Staff \with { instrumentName = "Mandoline 2" shortInstrumentName = "Md. 2" midiInstrument = "acoustic guitar (steel)" } << \global \mandolineII >>
      \new Staff \with { instrumentName = "Mandole ténor" shortInstrumentName = "Mdl." midiInstrument = "acoustic guitar (steel)" } << \global { \transposition c \mandole } >>
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
  \header { instrument = "Mandole ténor" }
  \score {
    \new Staff << \global \compressMMRests { \transposition c \mandole } >>
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
