\version "2.26.0"

\header {
  title = "Engrenages"
  subtitle = "pour orchestre à plectres"
  composer = "Claude"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \time 2,3 5/8 \accidentalStyle Score.modern \tempo "Meccanico" 4 = 112 s8*5
  s8*5
  s8*5
  s8*5
  \mark \default s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  \mark \default s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5 \bar "||"
  \time 2,3 5/4 \once \override Score.MetronomeMark.X-offset = #3 \tempo "Lento, sospeso" 4 = 60 \mark \default s8*10
  s8*10
  s8*10
  s8*10
  s8*10
  s8*10
  s8*10
  s8*10^\markup { \italic "rit." } \bar "||"
  \time 2,3 5/8 \once \override Score.MetronomeMark.X-offset = #3 \tempo "Tempo I" 4 = 112 \mark \default s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  \mark \default s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  \mark \default s8*5
  s8*5
  s8*5
  s8*5
  s8*5
  s8*5 \bar "|."
}

mandolineI = {
  \clef "treble" 
  R8*5 |
  R8*5 |
  R8*5 |
  R8*5 |
  e'8\mf f'8 cis''4.:32 |
  b'8 bes'8 d''4.:32 |
  a'8 aes'8 c''4.:32 |
  fis'8 g'8 ees''4.:32 |
  ees''4.:32 g'8 fis'8 |
  c''4.:32 aes'8 a'8 |
  d''4.:32 bes'8 b'8 |
  cis''4.:32 f'8 e'8 |
  e''8 ees''8 g''4.:32 |
  a'8 bes'8 fis''4.:32 |
  b'8 c''8 aes''4.:32 |
  d''8 cis''8 f''4.:32 |
  b'16\< c''16 aes''8 fis''16 f''16 a''4:32 |
  e''16 ees''16 g''8 cis''16 d''16 bes''4:32 |
  e''8\f f''8 cis'''4.:32 |
  cis'''4.:32~ cis'''4:32 |
  g'8-.\p cis''8-. ees''8-. g'8-. cis''8-. |
  ees''8-. g'8-. cis''8-. ees''8-. g'8-. |
  cis''8-. ees''8-. g'8-. cis''8-. ees''8-. |
  g'8-. cis''8-. ees''8-. g'8-. cis''8-. |
  ees''8-. g'8-. cis''8-. ees''8-. g'8-. |
  cis''8-. ees''8-. g'8-. cis''8-. ees''8-. |
  r8 cis''8-. ees''8-. g'8-. cis''8-. |
  ees''8-. g'8-. cis''8-. ees''8-. g'8-. |
  e''8\mf f''8 cis'''4.:32 |
  b''8 bes''8 d'''4.:32 |
  a''8 aes''8 c'''4.:32 |
  fis''8 g''8 ees'''4.:32 |
  e''8 ees''8 g''4.:32 |
  a'8 bes'8 fis''4.:32 |
  b'8 c''8 aes''4.:32 |
  d''8 cis''8 f''4.:32 |
  e'4:32\p f'4:32 cis''2.:32 |
  b'4:32 bes'4:32 d''2.:32 |
  a'4:32 aes'4:32 c''2.:32 |
  fis'4:32 g'4:32 ees''2.:32 |
  cis'''2:32~\pp cis'''2.:32 |
  bes''2:32~ bes''2.:32 |
  aes''2:32~ aes''2.:32 |
  ees''2:32~ ees''2.:32 |
  R8*5 |
  R8*5 |
  e''8\mf f''8 cis'''4.:32 |
  b''8 bes''8 d'''4.:32 |
  a''8 aes''8 c'''4.:32 |
  fis''8 g''8 ees'''4.:32 |
  a''4.:32\< bes''4:32 |
  b''4.:32 c'''4:32 |
  cis'''4.:32 d'''4:32 |
  g''8->\f aes''8-> e'''4.:32-> |
  bes''8->\f b''8-> g'''4.:32-> |
  cis''8->\ff d''8-> bes''4.:32-> |
  e''8\ff f''8 cis'''4.:32 |
  b''8 bes''8 d'''4.:32 |
  a''8 aes''8 c'''4.:32 |
  fis''8 g''8 ees'''4.:32 |
  ees'''4.:32 g''8 fis''8 |
  c'''4.:32 aes''8 a''8 |
  d'''4.:32 bes''8 b''8 |
  cis'''4.:32 f''8 e''8 |
  e''8\pp f''8 cis'''4.:32 |
  R8*5 |
  R8*5 |
  R8*5 |
  e''8->\fff f''8-> cis'''4.:32-> |
  <cis'' aes''>8->\sfz r8 r4.\fermata
}

mandolineII = {
  \clef "treble" 
  R8*5 |
  R8*5 |
  c''8-.\pp r8 r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-. c''8-. b'8-. r8 f''8-. |
  c''8-. b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. r8 b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-. c''8-. b'8-. r8 f''8-. |
  c''8-. b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-. c''8-. b'8-. r8 f''8-. |
  c''8-. b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-. r8 b'8-. r8 f''8-. |
  c''8-. b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  c''8-.\p b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-. c''8-. b'8-. r8 f''8-. |
  c''8-. b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-. c''8-. b'8-. r8 f''8-. |
  c''8-. b'8-. r8 f''8-. c''8-. |
  bes8\mf b8 g'4.:32 |
  f'8 e'8 aes'4.:32 |
  ees'8 d'8 fis'4.:32 |
  c'8 cis'8 a'4.:32 |
  bes'8 a'8 cis''4.:32 |
  ees'8 e'8 c''4.:32 |
  f'8 fis'8 d''4.:32 |
  ees''2:32~\pp ees''2.:32 |
  a''2:32~ a''2.:32 |
  b''2:32~ b''2.:32 |
  cis'''2:32~ cis'''2.:32 |
  f'2:32~ f'2.:32 |
  b'2:32~ b'2.:32 |
  c''2:32~ c''2.:32 |
  fis'2:32~ fis'2.:32 |
  c''8-.\p b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  g'8\mf aes'8 e''4.:32 |
  d''8 cis''8 f''4.:32 |
  c''8 b'8 ees''4.:32 |
  a'8 bes'8 fis''4.:32 |
  fis''4.:32\< g''4:32 |
  gis''4.:32 a''4:32 |
  g'8->\f aes'8-> e''4.:32-> |
  bes'8->\f b'8-> g''4.:32-> |
  cis'8->\ff d'8-> bes'4.:32-> |
  e'8\ff f'8 cis''4.:32 |
  b'8 bes'8 d''4.:32 |
  a'8 aes'8 c''4.:32 |
  fis'8 g'8 ees''4.:32 |
  ees''4.:32 g'8 fis'8 |
  c''4.:32 aes'8 a'8 |
  d''4.:32 bes'8 b'8 |
  cis''4.:32 f'8 e'8 |
  c''8-.\pp b'8-. r8 f''8-. c''8-. |
  b'8-. r8 f''8-. c''8-. b'8-. |
  r8 f''8-. c''8-. b'8-. r8 |
  f''8-.\ppp c''8-. b'8-. r8 f''8-. |
  e'8->\fff f'8-> cis''4.:32-> |
  <b' f''>8->\sfz r8 r4.\fermata
}

mandole = \transpose c c' {
  \clef "treble" 
  R8*5 |
  g8-.\pp cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  e8\mf f8 cis'4.:32 |
  b8 bes8 d'4.:32 |
  a8 aes8 c'4.:32 |
  fis8 g8 ees'4.:32 |
  ees'4.:32 g8 fis8 |
  c'4.:32 aes8 a8 |
  d'4.:32 bes8 b8 |
  cis'4.:32 f8 e8 |
  g8-.\p cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  fis2:32~\pp fis2.:32 |
  c'2:32~ c'2.:32 |
  d'2:32~ d'2.:32 |
  f2:32~ f2.:32 |
  ees'2.:32\p g4:32 fis4:32 |
  c'2.:32 aes4:32 a4:32 |
  d'2.:32 bes4:32 b4:32 |
  cis'2.:32 f4:32 e4:32 |
  g8-.\p cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  cis'8-. ees'8-. g8-. cis'8-. ees'8-. |
  g8-. cis'8-. ees'8-. g8-. cis'8-. |
  bes8\mf b8 g'4.:32 |
  f'8 e'8 aes'4.:32 |
  ees'8 d'8 fis'4.:32 |
  c'8 cis'8 a'4.:32 |
  g'4.:32\< aes'4:32 |
  g8->\f aes8-> e'4.:32-> |
  bes8->\f b8-> g'4.:32-> |
  cis8->\ff d8-> bes4.:32-> |
  e'8\ff ees'8 g'4.:32 |
  a8 bes8 fis'4.:32 |
  b8 c'8 aes'4.:32 |
  d'8 cis'8 f'4.:32 |
  f'4.:32 cis'8 d'8 |
  aes4.:32 c'8 b8 |
  fis'4.:32 bes8 a8 |
  g4.:32 ees'8 e'8 |
  g8-.\pp cis'8-. ees'8-. g8-. cis'8-. |
  ees'8-. g8-. cis'8-. ees'8-. g8-. |
  R8*5 |
  R8*5 |
  e8->\fff f8-> cis'4.:32-> |
  <fis c'>8->\sfz r8 r4.\fermata
}

guitare = {
  \clef "treble_8" 
  bes,8->\mp e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8->\p e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  g,2\pp g,2. |
  aes,2 aes,2. |
  bes,2 bes,2. |
  e,2 e,2. |
  e,2 e,2. |
  d2 d2. |
  a,2 a,2. |
  g,2 g,2. |
  bes,8->\p\< e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  cis8\mf d8 bes4. |
  aes8 g8 b4. |
  fis8 f8 a4. |
  ees8 e8 c'4. |
  g,8->\f aes,8-> e4.-> |
  bes,8->\f b,8-> g4.-> |
  cis8->\ff d8-> bes4.-> |
  <bes, e a ees'>8->\ff <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8-> <bes, e a ees'>8 <bes, e a ees'>8 |
  bes,8->\p e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  bes,8-> e8 a8-> ees'8 a8 |
  R8*5 |
  e,8->\fff f,8-> cis4.-> |
  <e, bes, ees a d' g'>8->\sfz r8 r4.\fermata
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
