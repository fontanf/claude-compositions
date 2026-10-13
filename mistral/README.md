# Mistral

Pièce pour orchestre à plectres : mandoline 1, mandoline 2, mandole ténor et guitare.
68 mesures, noire = 112 (*Meno mosso* à 80 dans la partie centrale), environ 2′40.

- Conducteur : [plectres.pdf](plectres.pdf)
- Parties séparées : [mandoline 1](plectres-mandolineI.pdf), [mandoline 2](plectres-mandolineII.pdf),
  [mandole ténor](plectres-mandole.pdf), [guitare](plectres-guitare.pdf)
- Audio : [plectres.mp3](plectres.mp3) (rendu synthétique)
- MIDI : [plectres.midi](plectres.midi)
- Source LilyPond : [plectres.ly](plectres.ly)

## L'idée

Une pièce au langage plus moderne, qui puisse plaire à des auditeurs non avertis tout en
intéressant des mélomanes familiers de la musique classique.

**Pour tout le monde :** un thème modal en mi mineur, chantant et facile à retenir, porté par un
ostinato de guitare en mesure asymétrique 3+3+2 qui donne l'énergie ; des sections bien contrastées
(une partie centrale lente et lyrique en trémolo, un retour du thème en tutti fortissimo, une fin
franche) ; une cadence do – ré – mi mineur, très « épique ».

**Pour les mélomanes :**
- le 3+3+2 est perturbé dès la 4ᵉ mesure du thème par un groupement 3+2+3, et le développement
  passe par deux mesures à 7/8 (2+2+3) ;
- dans la section centrale, le thème revient en augmentation stricte (valeurs doublées) : les
  liaisons par-dessus la barre recréent le 3+3+2 à l'intérieur du 4/4 ;
- il y est réharmonisé : la tête du thème, avec exactement les mêmes notes, sonne sur un
  do majeur 7 lydien (♯11) ;
- le développement est un fugato : le thème entre successivement en mi, la et si mineur, puis en
  strette ; les accords enchaînent ensuite fa, ré, si, une descente par tierces mineures, avant le retour ;
- la coda reprend la tête du thème en augmentation, puis tout l'ensemble l'énonce à l'unisson.

## Plan

| Mesures | Repère | Section | Contenu |
|---|---|---|---|
| 1–4 | | Introduction | Ostinato de guitare seul, puis entrée de la mandole et de la mandoline 2 |
| 5–12 | A | Thème | Thème à la mandoline 1, accords piqués en contretemps à la mandoline 2 |
| 13–20 | B | Thème varié | Thème à la mandole, contre-chant à la mandoline 1 |
| 21–24 | | Transition | Tête du thème en mi, do, la, sol ; ralenti |
| 25–40 | C | *Meno mosso, cantabile* | Thème en augmentation et réharmonisé, à la mandoline 1 puis à la mandole ; guitare en arpèges |
| 41–52 | D | Développement | Fugato, strette, mesures à 7/8, montée sur la dominante (si 7) |
| 53–60 | E | Reprise | Thème tutti fortissimo, harmonisé en tierces, guitare en accords grattés |
| 61–68 | F | Coda | Tête du thème en augmentation, unisson, cadence do – ré – mi mineur |

## Notes pour les musiciens

- **Mandole ténor** : accord sol-ré-la-mi, notée en clé de sol et sonnant une octave plus bas
  que l'écrit. Les doubles cordes en trémolo de la coda (mi-si, do-sol, ré-la) tombent bien sous
  les doigts, ré-la se jouant sur deux cordes à vide.
- **Mandoline 1** : monte jusqu'au mi aigu (12ᵉ case de la corde de mi) dans l'accord final.
- **Guitare** : notée en clé de sol octaviée ; les accords utilisent des positions ouvertes
  (mi mineur, sol, ré, do, la mineur, si 7).
- Les notes longues des mandolines et de la mandole sont en trémolo.

## Le son

L'audio est produit par `synth_plectres.py`, un modèle de cordes pincées (synthèse dite
Karplus-Strong) écrit pour l'occasion. Il simule les cordes doublées des mandolines et de la
mandole, le trémolo en triples croches, plusieurs musiciens par pupitre, les accords grattés de la
guitare et les résonances de caisse, avec une réverbération de salle. Le rendu est crédible mais
reste synthétique.

## Modifier et régénérer

Les notes sont écrites mesure par mesure dans [`plectres_data.py`](plectres_data.py), en notation
LilyPond avec hauteurs réelles (la mandole est transposée automatiquement pour l'affichage).
Le fichier contient aussi l'harmonie prévue pour chaque mesure : `plectres_tools.py` vérifie que
les notes sur les temps d'appui appartiennent à l'accord, et que chaque mesure a la bonne durée.
Les notes de passage modales qu'il signale sont voulues.

```sh
python3 plectres_tools.py plectres.ly   # vérifie et écrit plectres.ly
lilypond plectres.ly                    # conducteur, parties séparées et MIDI
python3 synth_plectres.py plectres.wav  # rendu audio
ffmpeg -i plectres.wav -b:a 256k plectres.mp3
```
