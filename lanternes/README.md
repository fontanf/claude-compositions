# Lanternes

Chaconne pour orchestre à plectres : mandoline 1, mandoline 2, mandole ténor et guitare.
72 mesures à 3/4 en ré mineur, tempo variable (noire = 58 à 92), environ 3′05.

- Conducteur : [lanternes.pdf](lanternes.pdf)
- Parties séparées : [mandoline 1](lanternes-mandolineI.pdf), [mandoline 2](lanternes-mandolineII.pdf),
  [mandole ténor](lanternes-mandole.pdf), [guitare](lanternes-guitare.pdf)
- Audio : [lanternes.mp3](lanternes.mp3) (rendu synthétique)
- MIDI : [lanternes.midi](lanternes.midi)
- Source LilyPond : [lanternes.ly](lanternes.ly)

## L'idée

Une chaconne : une ligne de basse de huit mesures (le *ground*) se répète tout au long de la pièce,
et chaque répétition est une nouvelle variation. Le ground descend de ré à la (ré – do – si♭ – la),
la descente « lamento » qu'on trouve chez Purcell ou Bach, puis passe par sol et mi avant de se
poser deux mesures sur la dominante.

**Pour tout le monde :** la forme est facile à suivre (on reconnaît la basse à chaque tour), la
pièce monte progressivement en intensité jusqu'à un sommet puis s'éteint, et une mélodie
nostalgique, introduite à la première variation, revient au moment fort.

**Pour les mélomanes :**
- la variation 4 est entièrement en hémioles : deux mesures à 3/4 sonnent comme trois groupes de
  deux temps, les notes enjambant la barre anticipent l'accord suivant ;
- dans la variation 5, le ground passe à la voix la plus aiguë (mandoline 1) et il est
  réharmonisé sur une basse qui monte pendant que le dessus descend : la même ligne sonne soudain
  en fa majeur ;
- au sommet (variation 7), trois couches se superposent : le ground aux deux extrémités de
  l'orchestre (mandoline 1 dans l'aigu, guitare à la basse), la mélodie à la mandole, une
  figuration en doubles croches à la mandoline 2 ;
- la coda brise le ground : au lieu de la deuxième mesure de dominante, il se résout sur un
  accord de ré majeur (tierce picarde), la septième sol de la mandoline 1 descendant sur le fa♯.

Sous la mélodie, la deuxième mesure du ground est harmonisée en fa majeur sur do (fa/do) plutôt
qu'en do majeur, pour que la note longue de la mélodie (fa) soit consonante.

## Plan

| Mesures | Repère | Tempo | Contenu |
|---|---|---|---|
| 1–8 | Thème | *Andante, con nostalgia* | Le ground à la guitare seule, accords sur le 2ᵉ temps (rythme de sarabande) |
| 9–16 | Var. 1 | | La mélodie à la mandoline 1, tenues en trémolo, arpèges de guitare |
| 17–24 | Var. 2 | | La mélodie à la mandole, arpèges à la mandoline 2, contre-chant tenu à la mandoline 1 |
| 25–32 | Var. 3 | *Più mosso, leggero* | Notes piquées : dialogue des deux mandolines, ground arpégé à la mandole, guitare en valse légère |
| 33–40 | Var. 4 | *Con slancio* | Hémioles, guitare en accords grattés, crescendo jusqu'au *ff* |
| 41–48 | Var. 5 | *Tranquillo, dolce* | Le ground à la mandoline 1, basse ascendante, réharmonisation en fa majeur |
| 49–56 | Var. 6 | *Appassionato* | Retour de la mélodie, tutti *f*, harmonisée en tierces |
| 57–64 | Var. 7 | | Sommet : ground aux extrêmes, mélodie à la mandole, doubles croches, *allargando* et silence |
| 65–72 | Coda | *Lento, lontano* | Fragments de la mélodie, le ground à la mandole, fin en ré majeur |

## Notes pour les musiciens

- **Mandole ténor** : notée en clé de sol, sonnant une octave plus bas. Elle descend jusqu'au sol
  grave (corde à vide) aux variations 3 et 4, et porte la mélodie aux variations 2 et 7.
- **Variation 4** : les doubles cordes de la mandole (ré-la, do-mi, si♭-ré, la-mi, sol-si♭, mi-si♭)
  sont toutes sur cordes voisines.
- **Guitare** : notée en clé de sol octaviée ; accords en positions ouvertes ou barrés simples
  (ré mineur, do, si♭ barré en 1ʳᵉ case, la, sol mineur barré en 3ᵉ case, mi demi-diminué 0-1-0-0).
- Les notes d'une noire et plus aux mandolines et à la mandole sont en trémolo, sauf dans la
  variation 3 (notes piquées) et l'ouverture de la coda.

## Le son

L'audio est produit par `synth_lanternes.py`, le même modèle de cordes pincées que pour
[Mistral](../mistral/) (synthèse dite Karplus-Strong, cordes doublées, trémolo, plusieurs musiciens par
pupitre, accords grattés, réverbération). Le rendu est crédible mais reste synthétique.

## Modifier et régénérer

Les notes sont dans [`lanternes_data.py`](lanternes_data.py), en notation LilyPond avec hauteurs
réelles ; le ground, la mélodie et les accords de guitare y sont définis une fois et réutilisés d'une
variation à l'autre. Le fichier contient aussi l'harmonie prévue pour chaque mesure : `lanternes_tools.py`
vérifie la durée des mesures et que les notes sur les temps appartiennent à l'accord. Les signalements
restants (une onzième de passage sur l'accord de mi demi-diminué, une septième sur ré mineur, une
septième sur la) sont voulus.

```sh
python3 lanternes_tools.py lanternes.ly   # vérifie et écrit lanternes.ly
lilypond lanternes.ly                     # conducteur, parties séparées et MIDI
python3 synth_lanternes.py lanternes.wav  # rendu audio
ffmpeg -i lanternes.wav -b:a 256k lanternes.mp3
```
