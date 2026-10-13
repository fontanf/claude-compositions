\version "2.26.0"

\header {
  title = "Lanternes"
  subtitle = "chaconne pour orchestre à plectres"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \time 3/4 \tempo "Andante, con nostalgia" 4 = 69 \mark \markup \box "Thème" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  \mark \markup \box "Var. 1" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  \mark \markup \box "Var. 2" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6 \bar "||"
  \once \override Score.MetronomeMark.X-offset = #3 \tempo "Più mosso, leggero" 4 = 84 \mark \markup \box "Var. 3" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6 \bar "||"
  \once \override Score.MetronomeMark.X-offset = #3 \tempo "Con slancio" 4 = 92 \mark \markup \box "Var. 4" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6 \bar "||"
  \once \override Score.MetronomeMark.X-offset = #3 \tempo "Tranquillo, dolce" 4 = 66 \mark \markup \box "Var. 5" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6 \bar "||"
  \once \override Score.MetronomeMark.X-offset = #3 \tempo "Appassionato" 4 = 76 \mark \markup \box "Var. 6" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  \mark \markup \box "Var. 7" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6^\markup { \italic "allargando" }
  s8*6 \bar "||"
  \once \override Score.MetronomeMark.X-offset = #3 \tempo "Lento, lontano" 4 = 58 \mark \markup \box "Coda" s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6
  s8*6^\markup { \italic "rit." }
  s8*6 \bar "|."
}

mandolineI = {
  \clef "treble" \key d \minor
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  a'4:32\mp d''4:32 e''4:32 |
  f''2:32 e''4:32 |
  d''4:32 f''4:32 a''4:32 |
  g''4.:32 f''8 e''8 cis''8 |
  d''4:32 g''4:32 a''4:32 |
  bes''2:32 a''4:32 |
  g''4:32 e''4:32 d''4:32 |
  cis''2.:32 |
  f''2.:32\p |
  g''2.:32 |
  a''2.:32 |
  a''2.:32 |
  bes''2.:32 |
  g''2.:32 |
  a''2.:32 |
  g''2.:32 |
  a''8-.\mp f''8-. e''8-. f''8-. d''4-. |
  g''8-. e''8-. d''8-. e''8-. c''4-. |
  R2. |
  R2. |
  bes''8-. g''8-. f''8-. g''8-. d''4-. |
  bes''8-. g''8-. e''8-. g''8-. d''4-. |
  a''8-. g''8-. e''8-. d''8-. e''4-. |
  cis'''8-. a''8-. g''8-. e''8-. cis''4-. |
  a''2:32\f g''4:32~ |
  g''4:32 e''2:32 |
  f''2:32 e''4:32~ |
  e''4:32 cis''2:32 |
  bes''2:32 a''4:32~ |
  a''4:32 g''2:32 |
  a''4:32\< d'''4:32 e'''4:32 |
  cis'''2.:32\ff |
  d'''2.:32\p |
  c'''2.:32 |
  bes''2.:32 |
  a''2.:32 |
  g''2.:32 |
  e''2.:32 |
  a''2.:32 |
  a''2.:32 |
  a'4:32\f d''4:32 e''4:32 |
  f''2:32 e''4:32 |
  d''4:32 f''4:32 a''4:32 |
  g''4.:32 f''8 e''8 cis''8 |
  d''4:32 g''4:32 a''4:32 |
  bes''2:32 a''4:32 |
  g''4:32 e''4:32 d''4:32 |
  cis''2.:32 |
  d'''2.:32\ff |
  c'''2.:32 |
  bes''2.:32 |
  a''2.:32 |
  g''2.:32 |
  e''2.:32 |
  a''2.:32 |
  a''2:32 r4 |
  a'4\pp d''4 e''4 |
  f''2:32 e''4:32 |
  R2. |
  R2. |
  d''4:32 g''4:32 a''4:32 |
  bes''2:32 a''4:32 |
  g''2.:32 |
  fis''2.:32\fermata
}

mandolineII = {
  \clef "treble" \key d \minor
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  a'2.:32\pp |
  a'2.:32 |
  a'2.:32 |
  a'2.:32 |
  bes'2.:32 |
  bes'2.:32 |
  a'2.:32 |
  g'2.:32 |
  a'8\mp d''8 f''8 d''8 e''8 d''8 |
  a'8 c''8 f''8 c''8 c''8 c''8 |
  f'8 bes'8 d''8 bes'8 a'8 bes'8 |
  e'8 a'8 cis''8 a'8 e''8 a'8 |
  bes'8 d''8 g''8 d''8 f''8 d''8 |
  d'8 g'8 bes'8 g'8 e''8 g'8 |
  e'8 a'8 d''8 a'8 e''8 a'8 |
  e'8 g'8 cis''8 g'8 e''8 g'8 |
  R2. |
  R2. |
  f''8-.\mp d''8-. c''8-. d''8-. bes'4-. |
  e''8-. cis''8-. b'8-. cis''8-. a'4-. |
  d''8-. bes'8-. a'8-. bes'8-. f'4-. |
  d''8-. bes'8-. g'8-. bes'8-. e'4-. |
  e''4-. d''4-. a'4-. |
  e''8-. cis''8-. a'8-. g'8-. e'4-. |
  f''2:32\f e''4:32~ |
  e''4:32 c''2:32 |
  d''2:32 a'4:32~ |
  a'4:32 a'2:32 |
  g''2:32 e''4:32~ |
  e''4:32 d''2:32 |
  e''4:32\< a''4:32 g''4:32 |
  g''2.:32\ff |
  f'2.:32\pp |
  g'2.:32 |
  d''2.:32 |
  c''2.:32 |
  a'2.:32 |
  g'2.:32 |
  a'2.:32 |
  g'2.:32 |
  f'4:32\f a'4:32 c''4:32 |
  a'2:32 a'4:32 |
  bes'4:32 d''4:32 d''4:32 |
  e''4.:32 d''8 a'4:32 |
  bes'4:32 d''4:32 f''4:32 |
  g''2:32 e''4:32 |
  e''4:32 g'4:32 a'4:32 |
  g'2.:32 |
  a'16\f d''16 f''16 a''16 f''16 d''16 a'16 d''16 f''16 a''16 f''16 d''16  |
  a'16 c''16 f''16 a''16 f''16 c''16 a'16 c''16 f''16 a''16 f''16 c''16  |
  f'16 bes'16 d''16 f''16 d''16 bes'16 f'16 bes'16 d''16 f''16 d''16 bes'16  |
  e'16 a'16 cis''16 e''16 cis''16 a'16 e'16 a'16 cis''16 e''16 cis''16 a'16  |
  d'16 g'16 bes'16 d''16 bes'16 g'16 d'16 g'16 bes'16 d''16 bes'16 g'16  |
  e'16 g'16 bes'16 d''16 bes'16 g'16 e'16 g'16 bes'16 d''16 bes'16 g'16  |
  e'16 a'16 d''16 e''16 d''16 a'16 e'16 a'16 d''16 e''16 d''16 a'16  |
  e'16 a'16 cis''16 e''16 g''16 e''16 cis''16 a'16 r4 |
  f'2.:32\ppp |
  a'2.:32 |
  d'4:32\pp f'4:32 a'4:32 |
  g'4.:32 f'8:32 e'4:32 |
  bes'2.:32 |
  g'2.:32 |
  cis''2.:32 |
  d''2.:32\fermata
}

mandole = \transpose c c' {
  \clef "treble" \key d \minor
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  R2. |
  f2.:32\pp |
  c2.:32 |
  d2.:32 |
  cis2.:32 |
  d2.:32 |
  d2.:32 |
  e2.:32 |
  cis2.:32 |
  a4:32\mf d'4:32 e'4:32 |
  f'2:32 e'4:32 |
  d'4:32 f'4:32 a'4:32 |
  g'4.:32 f'8 e'8 cis'8 |
  d'4:32 g'4:32 a'4:32 |
  bes'2:32 a'4:32 |
  g'4:32 e'4:32 d'4:32 |
  cis'2.:32 |
  d4-.\mp f4-. a4-. |
  c4-. e4-. g4-. |
  bes,4-. d4-. f4-. |
  a,4-. cis4-. e4-. |
  g,4-. bes,4-. d4-. |
  e4-. g4-. bes4-. |
  a,4-. d4-. e4-. |
  a,4-. cis4-. g4-. |
  <d a>2:32\f <c e>4:32~ |
  <c e>4:32 <c e>2:32 |
  <bes, d>2:32 <a, e>4:32~ |
  <a, e>4:32 <a, e>2:32 |
  <g, bes>2:32 <e bes>4:32~ |
  <e bes>4:32 <e bes>2:32 |
  <a, e>2.:32\< |
  <a, e>2.:32\ff |
  d'2.:32\pp |
  e'2.:32 |
  f'2.:32 |
  e'2.:32 |
  c'2.:32 |
  c'2.:32 |
  e'2.:32 |
  cis'2.:32 |
  f2.:32\f |
  g2.:32 |
  a2.:32 |
  a2.:32 |
  d2.:32 |
  bes2.:32 |
  a2.:32 |
  cis2.:32 |
  a4:32\ff d'4:32 e'4:32 |
  f'2:32 e'4:32 |
  d'4:32 f'4:32 a'4:32 |
  g'4.:32 f'8 e'8 cis'8 |
  d'4:32 g'4:32 a'4:32 |
  bes'2:32 a'4:32 |
  g'4:32 e'4:32 d'4:32 |
  cis'2:32 r4 |
  d2.:32\pp |
  c2.:32 |
  bes,2.:32 |
  a,2.:32 |
  g,2.:32 |
  e2.:32 |
  a,2.:32 |
  d2.:32\fermata
}

guitare = {
  \clef "treble_8" \key d \minor
  d4\mf <a d' f'>2 |
  c4 <g c' e'>2 |
  bes,4 <f a d'>2 |
  a,4 <e a cis'>2 |
  g,4 <d g bes>2 |
  e,4 <bes, d g>2 |
  a,4 <e a d'>2 |
  a,4 <e g cis'>2 |
  d8\p a8 f'8 a8 e'8 a8 |
  c8 f8 a8 f8 c'8 f8 |
  bes,8 f8 a8 f8 d'8 f8 |
  a,8 e8 cis'8 e8 g8 e8 |
  g,8 d8 bes8 d8 f8 d8 |
  e,8 bes,8 g8 bes,8 d'8 bes,8 |
  a,8 e8 d'8 e8 g8 e8 |
  a,8 e8 cis'8 e8 g8 e8 |
  d4\mp <a d' f'>2 |
  c4 <a c' f'>2 |
  bes,4 <f a d'>2 |
  a,4 <e a cis'>2 |
  g,4 <d g bes>2 |
  e,4 <bes, d g>2 |
  a,4 <e a d'>2 |
  a,4 <e g cis'>2 |
  r4\p <d' f' a'>4-. <d' f' a'>4-. |
  r4 <c' e' g'>4-. <c' e' g'>4-. |
  r4 <d' f' a'>4-. <d' f' a'>4-. |
  r4 <cis' e' a'>4-. <cis' e' a'>4-. |
  r4 <d' f' bes'>4-. <d' f' bes'>4-. |
  r4 <d' g' bes'>4-. <d' g' bes'>4-. |
  r4 <d' e' a'>4-. <d' e' a'>4-. |
  r4 <cis' e' g'>4-. <cis' e' g'>4-. |
  <d a d' f'>8->\f <d a d' f'>8 <d a d' f'>8 <d a d' f'>8 <d a d' f'>8-> <d a d' f'>8 |
  <c e g c' e'>8 <c e g c' e'>8 <c e g c' e'>8-> <c e g c' e'>8 <c e g c' e'>8 <c e g c' e'>8 |
  <bes, f bes d' f'>8-> <bes, f bes d' f'>8 <bes, f bes d' f'>8 <bes, f bes d' f'>8 <bes, f bes d' f'>8-> <bes, f bes d' f'>8 |
  <a, e a cis' e'>8 <a, e a cis' e'>8 <a, e a cis' e'>8-> <a, e a cis' e'>8 <a, e a cis' e'>8 <a, e a cis' e'>8 |
  <g, d g bes d' g'>8-> <g, d g bes d' g'>8 <g, d g bes d' g'>8 <g, d g bes d' g'>8 <g, d g bes d' g'>8-> <g, d g bes d' g'>8 |
  <e, bes, d g>8 <e, bes, d g>8 <e, bes, d g>8-> <e, bes, d g>8 <e, bes, d g>8 <e, bes, d g>8 |
  <a, e g d' e'>8->\< <a, e g d' e'>8 <a, e g d' e'>8-> <a, e g d' e'>8 <a, e g d' e'>8-> <a, e g d' e'>8 |
  <a, e g cis' e'>8->\ff <a, e g cis' e'>8 <a, e g cis' e'>8-> <a, e g cis' e'>8 <a, e g cis' e'>8-> <a, e g cis' e'>8 |
  bes,8\pp f8 d'8 f8 a8 f8 |
  c8 g8 a8 g8 e'8 g8 |
  d8 f8 bes8 f8 d'8 f8 |
  e8 a8 c'8 a8 e'8 a8 |
  f8 c'8 a8 c'8 g'8 c'8 |
  g8 c'8 e'8 c'8 g'8 c'8 |
  a,8 e8 d'8 e8 a8 e8 |
  a,8 e8 cis'8 e8 g8 e8 |
  <d a d' f'>4->\f <d a d' f'>8 <d a d' f'>8 <d a d' f'>8 <d a d' f'>8 |
  <c f a c' f'>4-> <c f a c' f'>8 <c f a c' f'>8 <c f a c' f'>8 <c f a c' f'>8 |
  <bes, f bes d' f'>4-> <bes, f bes d' f'>8 <bes, f bes d' f'>8 <bes, f bes d' f'>8 <bes, f bes d' f'>8 |
  <a, e a cis' e'>4-> <a, e a cis' e'>8 <a, e a cis' e'>8 <a, e a cis' e'>8 <a, e a cis' e'>8 |
  <g, d g bes d' g'>4-> <g, d g bes d' g'>8 <g, d g bes d' g'>8 <g, d g bes d' g'>8 <g, d g bes d' g'>8 |
  <e, bes, d g>4-> <e, bes, d g>8 <e, bes, d g>8 <e, bes, d g>8 <e, bes, d g>8 |
  <a, e g d' e'>4-> <a, e g d' e'>8 <a, e g d' e'>8 <a, e g d' e'>8 <a, e g d' e'>8 |
  <a, e g cis' e'>4-> <a, e g cis' e'>8 <a, e g cis' e'>8 <a, e g cis' e'>8 <a, e g cis' e'>8 |
  <d a d' f'>4->\ff <d a d' f'>8 <d a d' f'>8 <d a d' f'>8 <d a d' f'>8 |
  <c f a c' f'>4-> <c f a c' f'>8 <c f a c' f'>8 <c f a c' f'>8 <c f a c' f'>8 |
  <bes, f bes d' f'>4-> <bes, f bes d' f'>8 <bes, f bes d' f'>8 <bes, f bes d' f'>8 <bes, f bes d' f'>8 |
  <a, e a cis' e'>4-> <a, e a cis' e'>8 <a, e a cis' e'>8 <a, e a cis' e'>8 <a, e a cis' e'>8 |
  <g, d g bes d' g'>4-> <g, d g bes d' g'>8 <g, d g bes d' g'>8 <g, d g bes d' g'>8 <g, d g bes d' g'>8 |
  <e, bes, d g>4-> <e, bes, d g>8 <e, bes, d g>8 <e, bes, d g>8 <e, bes, d g>8 |
  <a, e g d' e'>4-> <a, e g d' e'>8 <a, e g d' e'>8 <a, e g d' e'>8 <a, e g d' e'>8 |
  <a, e g cis' e'>4-> <a, e g cis' e'>4-> r4 |
  <f a d' e'>2.\pp |
  <f a c' e'>2. |
  <d' f' a'>2. |
  <e a cis'>2. |
  <g bes d' e'>2. |
  <g bes d'>2. |
  <g cis' e'>2. |
  <d a d' fis'>2.\fermata
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
