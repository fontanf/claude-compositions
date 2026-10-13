# Engrenages

Pièce pour orchestre à plectres : mandoline 1, mandoline 2, mandole ténor et guitare.
70 mesures, principalement à 5/8 (2+3), noire = 112, avec une section lente à 5/4 ; environ 2′05.
Musique atonale, écrite sur une série de douze sons.

- Conducteur : [engrenages.pdf](engrenages.pdf)
- Parties séparées : [mandoline 1](engrenages-mandolineI.pdf), [mandoline 2](engrenages-mandolineII.pdf),
  [mandole ténor](engrenages-mandole.pdf), [guitare](engrenages-guitare.pdf)
- Audio : [engrenages.mp3](engrenages.mp3) (rendu synthétique)
- MIDI : [engrenages.midi](engrenages.midi)
- Source LilyPond : [engrenages.ly](engrenages.ly)

## L'idée

Une pièce ni tonale ni modale, mais qui puisse plaire au plus grand nombre. L'accessibilité ne
vient pas de l'harmonie mais du **rythme**, de la **répétition** et d'un **motif très court** :
c'est le principe du fugato « Cool » de *West Side Story*, écrit sur une série de douze sons mais
porté par un rythme irrésistible.

**Le thème** tient en un geste de trois notes, *court-court-long* : un demi-ton, puis un grand saut
(mi – fa – do♯). Il est énoncé quatre fois de suite en séquence, si bien qu'on le retient
immédiatement, alors que ces quatre énoncés parcourent les douze sons.

**Les engrenages** : trois ostinatos tournent en même temps à des vitesses différentes, comme des
roues dentées — la guitare sur un cycle de 5 croches, la mandole sur 3, la mandoline 2 sur 4. Ils
se décalent sans cesse les uns par rapport aux autres et ne retombent ensemble que toutes les
60 croches. Pour l'auditeur, c'est une pulsation mécanique et entraînante ; pour le musicien, une
polyrythmie 5 contre 3 contre 4.

## La série

| | Cellule 1 | Cellule 2 | Cellule 3 | Cellule 4 |
|---|---|---|---|---|
| Série originale (P0) | mi fa do♯ | si si♭ ré | la la♭ do | fa♯ sol mi♭ |

Les quatre cellules sont du même type (un demi-ton et une tierce majeure, l'ensemble de classes
(014)) : la première et la dernière ont le même profil, les deux du milieu le profil inversé. C'est
ce qui rend le thème si reconnaissable : chaque cellule est une variante de la précédente.

La pièce utilise la série sous ses quatre formes classiques : originale (P), rétrograde (R),
renversée (I) et rétrograde du renversement (RI), ainsi que plusieurs transpositions.

## Plan

| Mesures | Repère | Contenu |
|---|---|---|
| 1–4 | | Les engrenages se mettent en route un par un : guitare, mandole, mandoline 2 |
| 5–20 | A | Le thème à la mandoline 1 : série originale, rétrograde (le rythme est lui aussi renversé : long-court-court), renversement, puis une version accélérée en doubles croches |
| 21–36 | B | Le thème à la mandole ; puis canon au triton entre les deux mandolines, à une mesure d'écart |
| 37–44 | C | *Lento, sospeso*, à 5/4 : le thème en augmentation exacte (valeurs doublées), d'abord à la mandoline 1 puis, à rebours, à la mandole ; chaque mesure est harmonisée par une autre cellule de la série, très espacée |
| 45–56 | D | Strette : le thème entre successivement aux quatre pupitres, transposé à chaque fois d'une tierce mineure (mi, sol, si♭, do♯) ; puis tout l'orchestre à l'unisson parcourt ce même cycle jusqu'au sommet |
| 57–64 | E | Retour du thème *ff* aux deux mandolines en octaves, et en même temps son miroir (renversement) à la mandole |
| 65–70 | F | Les engrenages reprennent *pp* puis s'arrêtent un à un ; dernier énoncé du motif *fff* à l'unisson, et accord final contenant les douze sons |

## Vérifications

`engrenages_tools.py` vérifie la durée de chaque mesure et contient un **détecteur d'accords
parfaits** : à chaque attaque, il regarde l'ensemble des notes qui sonnent et signale toute
sonorité formant un accord majeur ou mineur, pour éviter qu'une couleur tonale apparaisse par
hasard. À la composition, les engrenages en produisaient une douzaine en se croisant ; le choix des
notes de l'ostinato de mandole (sol – do♯ – mi♭) a été fait par une recherche automatique parmi
toutes les possibilités, et les quatre cas restants ont été supprimés en remplaçant une seule
croche d'engrenage par un silence (m. 3, 8, 18 et 27). La pièce n'en contient plus aucun.

## Notes pour les musiciens

- Pas d'armure : toutes les altérations sont écrites, avec les rappels nécessaires (par exemple
  quand un même accord contient mi et mi♭).
- **Engrenages** : jouer très régulièrement, *staccato*, sans accentuer les retours de cycle — c'est
  le décalage avec la mesure à 2+3 qui crée l'effet.
- **Mandole ténor** : notée en clé de sol, sonnant une octave plus bas.
- **Guitare** : notée en clé de sol octaviée. L'accord final (mi – si♭ – mi♭ – la – ré – sol, doigté
  0-1-1-2-3-3) se joue en une seule position.
- Les notes d'une noire et plus aux mandolines et à la mandole sont en trémolo.

## Le son

L'audio est produit par `synth_engrenages.py`, le même modèle de cordes pincées que pour les autres
pièces pour plectres (synthèse dite Karplus-Strong, cordes doublées, trémolo, plusieurs musiciens
par pupitre, réverbération). Le rendu est crédible mais reste synthétique.

## Modifier et régénérer

Les notes sont dans [`engrenages_data.py`](engrenages_data.py), en notation LilyPond avec hauteurs
réelles. Les engrenages sont générés par la fonction `gear`, et les formes de la série par
transposition (`tp`) et changement d'octave (`shift`) des phrases du thème.

```sh
python3 engrenages_tools.py engrenages.ly   # vérifie et écrit engrenages.ly
lilypond engrenages.ly                      # conducteur, parties séparées et MIDI
python3 synth_engrenages.py engrenages.wav  # rendu audio
ffmpeg -i engrenages.wav -b:a 256k engrenages.mp3
```
