# Accord

Pièce pour guitare classique seule, accord standard.
36 mesures, environ 2′10. Niveau avancé.

- Partition (avec doigtés) : [accord.pdf](accord.pdf)
- Audio : [accord.mp3](accord.mp3) (rendu synthétique)
- MIDI : [accord.midi](accord.midi)
- Source LilyPond : [accord.ly](accord.ly)

## L'idée

Le titre joue sur les deux sens du mot : un *accord*, plusieurs notes qui sonnent ensemble, et l'*accord*
de la guitare, la façon dont ses six cordes sont tendues (mi, la, ré, sol, si, mi : une pile de quartes,
avec une tierce). La pièce n'est pas pensée en tonalité, mais en **sonorités** que l'instrument sait
produire, et elle suit un seul fil : partir d'une note et aller jusqu'à l'instrument entier.

**I. Une note.** Le mi au milieu de la portée (mi4) existe sur quatre cordes : à vide sur la
chanterelle, en case V sur la 2ᵉ corde, en case IX sur la 3ᵉ, en case XIV sur la 4ᵉ. C'est la même
hauteur, mais pas le même son : plus la corde est grave et la case haute, plus il est sombre et
court. On entend ces quatre mi l'un après l'autre, puis deux et trois à la fois (ils ne sont jamais
parfaitement accordés entre eux : ils battent légèrement), joués près du chevalet (*sul ponticello*,
métallique) puis sur la touche (*sul tasto*, rond). Enfin ses deux voisines, ré♯ et fa, s'ajoutent sur
d'autres cordes et résonnent avec lui.

**II. Diffraction.** Autour du mi qui reste à vide, les notes voisines s'écartent : demi-tons, puis tons
entiers, puis tierces, puis quartes, jusqu'à ce qu'il ne reste que les six cordes à vide. Chaque mesure
est une seule position de main gauche, jouée en arpège et laissée résonner : on entend l'agrégat se
desserrer jusqu'à devenir l'accord de la guitare.

**III. Halo.** Cette même pile de quartes, rejouée en harmoniques naturelles à quatre hauteurs : à
l'octave (case XII), à la quinte au-dessus (case VII), à deux octaves (case V), et à la tierce majeure
au-dessus de deux octaves (case IV). Chaque série reproduit l'accord des cordes, transposé et
légèrement « faux » (les harmoniques suivent les rapports naturels, pas le tempérament), de plus en
plus haut, jusqu'à disparaître.

**IV. Matière.** Le corps de l'instrument. L'agrégat ré♯–mi–fa du début, joué étouffé (*pizz.*), contre
des frappes sur la table (*golpe*) ; l'accord des cordes à vide frappé sur le chevalet (*tambora*) ;
puis l'accord de la guitare entier, barré et déplacé (cases I, II, III, V), en rasgueado, jusqu'aux
six cordes à vide *fff*. Silence.

**V. Une note.** Il ne reste que le mi : en harmonique, puis sur deux cordes, puis seul sur la corde
la plus sombre (case XIV de la 4ᵉ corde), qui s'éteint.

## Plan

| Mesures | Section | Sonorité |
|---|---|---|
| 1–6 | I. Une note | mi4 sur quatre cordes ; unissons ; *sul pont.* / *sul tasto* ; ré♯–mi–fa |
| 7–12 | II. Diffraction | demi-tons → tons → tierces → quartes → cordes à vide, laissés résonner |
| 13–20 | III. Halo | harmoniques XII, VII, V et IV des six cordes |
| 21–32 | IV. Matière | *pizz.*, *golpe*, *tambora*, accord des cordes barré et déplacé, silence |
| 33–36 | V. Une note | mi en harmonique, unisson, puis la corde la plus sombre |

## Notes pour les musiciens

- **Cordes imposées** : dans cette pièce, la corde fait partie du son. Les chiffres cerclés écrits dans
  la partition (mesures 1 à 11, 21 à 24, 33 à 35) sont à respecter.
- **II (m. 7–12)** : chaque mesure est une seule position ; ne pas étouffer, laisser tout résonner
  jusqu'à la mesure suivante. Positions : ré♯–mi–fa (cases VI–VIII), do–ré–mi–fa♯ (VII–X),
  ré–mi–fa♯–sol♯ (IX–XII), do–mi–sol♯–si (VII–X), la–ré–sol–do (VII–VIII).
- **Harmoniques** : la case et la corde sont indiquées ; celles de la case IV (5ᵉ harmonique) sont les
  plus délicates : effleurer très légèrement, un peu avant la frette.
- **pizz.** : étouffer avec le tranchant de la main droite près du chevalet. **tamb.** : frapper les
  cordes avec le côté du pouce, près du chevalet. **golpe** (notes en croix) : frapper la table avec les
  doigts de la main droite.
- **m. 25–28** : l'accord des cordes à vide, barré en cases I, II, III puis V (tout le barré, six cordes).

## Vérifications

`accord_tools.py` vérifie chaque attaque (ou chaque mesure résonante de la partie II, comme une seule
position) : répartition corde/case en respectant les cordes imposées, écart, nombre de doigts, barrés.
Deux erreurs ont été trouvées pendant l'écriture : une mesure de la partie II où les cordes imposées
demandaient un écart de huit cases (corrigée en position IX), et une erreur de l'outil lui-même, qui
confondait les deux mi d'un unisson ; il repère maintenant chaque son d'un accord par son rang.

## Le son

`synth_accord.py` modélise ce qui fait la pièce : la même note est plus sombre sur une corde grave
et en case haute ; *sul ponticello* attaque près du chevalet (brillant), *sul tasto* sur la touche
(rond) ; les cordes étouffées, la tambora (avec le choc sur le chevalet) et le golpe (choc sur la
table) ont leur propre rendu ; dans la partie II, chaque note résonne jusqu'à ce que sa corde soit
rejouée. Les différences de couleur ont été mesurées (centre de gravité spectral des quatre mi du
début : 1 240, 1 100, 955 et 950 Hz ; *sul pont.* 1 780 Hz, ordinaire 1 080 Hz, *sul tasto* 710 Hz).
L'enregistrement est légèrement compressé pour que les passages très doux restent audibles. Le rendu
est crédible mais reste synthétique : les battements des unissons, en particulier, seront bien plus
riches sur un vrai instrument.

## Modifier et régénérer

```sh
python3 accord_tools.py accord.ly     # vérifie et écrit accord.ly avec doigtés
python3 accord_tools.py -v            # positions trouvées
lilypond accord.ly                    # partition PDF et MIDI
python3 synth_accord.py accord.wav    # rendu audio
ffmpeg -i accord.wav -af "acompressor=threshold=-30dB:ratio=2.5:attack=20:release=500:makeup=3,loudnorm=I=-18:TP=-1.5:LRA=16" -b:a 256k accord.mp3
```
