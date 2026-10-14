# Vertige

Toccata pour guitare classique seule, **en fa♯ mineur**, accord standard.
86 mesures à 2/4, noire = 120 (trio à 84), environ 1′35. Niveau avancé.

- Partition (avec doigtés) : [vertige.pdf](vertige.pdf)
- Audio : [vertige.mp3](vertige.mp3) (rendu synthétique)
- MIDI : [vertige.midi](vertige.midi)
- Source LilyPond : [vertige.ly](vertige.ly)

## L'idée

Un thème mineur rapide et obstiné, dans une tonalité peu jouée à la guitare. Fa♯ mineur a une
particularité précieuse : **si et mi, deux cordes à vide, appartiennent à tous les accords de la
gamme** (comme quarte et septième de fa♯ mineur, fondamentale et quinte de mi, quinte et septième de
do♯ mineur, sixte et neuvième de ré…). Elles peuvent donc sonner en continu au-dessus de n'importe
quelle harmonie.

**Le thème** est joué **au pouce**, dans les basses, en rythme **3+3+2** (doubles croches groupées
par trois, trois et deux) ; dans les trous de ce rythme, l'index et le majeur répètent si et mi à
vide, au-dessus. C'est le principe d'*Asturias*, mais renversé : la pédale est en haut, la mélodie en
bas. Le résultat est une pulsation qui ne s'arrête jamais, sur laquelle une mélodie très simple
(fa♯ – la – do♯, si – la – sol♯…) s'imprime immédiatement.

**Pour tout le monde :** un thème qu'on retient, une énergie continue, un passage de rasgueado, un
trio chantant pour respirer, et un retour en force du thème, doublé à l'octave.

**Pour les auditeurs avertis :**
- la pédale si–mi fait entendre fa♯ en **éolien** (mineur naturel) : la dominante est do♯ *mineur*,
  sans sensible, jusqu'à ce que la gamme descendante des m. 61–62 fasse enfin entendre le **mi♯** et
  amène un vrai do♯7 ;
- le développement (B) parcourt un **cycle de tierces mineures** (fa♯ m – la m – do m – mi♭ m) :
  chaque accord est tonal, mais l'enchaînement est symétrique (il divise l'octave en quatre parts
  égales) et fait perdre tout ancrage ; puis la tête du thème est transposée sur chacun de ces accords,
  avec sa propre pédale (do–mi pour la mineur, mi♭–sol pour do mineur…) ;
- le trio, en la majeur (relatif), est écrit **en tierces** sur les deux premières cordes, avec un
  vrai mouvement harmonique (la – si m7 – mi – la…) ;
- dans le retour, la mélodie est **doublée à l'octave** (pouce et index), sans pédale.

## Plan

| Mesures | Section | Contenu |
|---|---|---|
| 1–16 | A — *Presto, con fuoco* | Le thème au pouce, pédale si–mi à vide |
| 17–32 | A2 | Le thème une octave plus bas, pédale inversée (mi–si) |
| 33–40 | B | Rasgueado sur le cycle fa♯ m – la m – do m – mi♭ m |
| 41–48 | | La tête du thème sur chaque accord du cycle, puis mi majeur |
| 49–60 | Trio — *Meno mosso, cantabile* | La majeur, en tierces |
| 61–64 | | Gamme descendante liée de fa♯ mineur harmonique, do♯7 en rasgueado, point d'orgue |
| 65–80 | A′ | Le thème, puis la mélodie en octaves |
| 81–86 | Coda | Fa♯ m – ré – do♯7 – fa♯ m en rasgueado |

## Notes pour les musiciens

- **Thème (A, A2, A′)** : le pouce (accentué) et la pédale i–m (légère) ne se superposent jamais ;
  garder la pédale très régulière, plus douce que le pouce. Les notes du pouce restent sur les cordes 3
  à 6, en positions I à VII.
- **Rasgueado** (m. 33–40, 63, 81–86) : fa♯ m barré II, la m en position ouverte, do m barré III
  (x3554x, tierce en haut), mi♭ m barré VI (x6887x), do♯7 en x4342x, ré en position ouverte.
- **Trio** : tierces sur les cordes 1 et 2, positions VII à XIV ; basses sur les cordes 5 et 6.
- **Octaves** (m. 73–80) : pouce et index sur des cordes séparées d'une corde (6 et 4, 5 et 3).

## Vérifications

`vertige_tools.py` vérifie que chaque attaque est jouable (répartition corde/case, écart, nombre de
doigts, barrés), cherche les quintes et octaves parallèles entre le dessus et la basse, et
`--relecture` affiche l'accord réellement entendu à chaque temps. À la composition, ces contrôles ont
conduit à :
- revoicer do m et mi♭ m dans le cycle (tierce en haut), car l'accord glissé tel quel produisait des
  quintes parallèles ;
- changer deux basses du trio : m. 50 (si au lieu de ré, qui laissait un accord de ré sans fa♯) et
  m. 51 (mi au lieu de do♯, qui doublait la mélodie à l'octave) ;
- ajouter la tierce à l'accord final du trio (m. 60), qui sonnait en quinte vide.

Les signalements restants sont voulus : doublure de la mélodie à l'octave (m. 73–80), et sonorités
« sans tierce » dans le thème, où la pédale si–mi colore une mélodie qui porte elle-même la tierce.

## Doigtés

Mêmes conventions que pour [Fontaine](../fontaine/) et [Le Phare](../le-phare/) : doigts 1 à 4,
cordes en chiffres cerclés (seulement quand la note n'est pas à sa case la plus basse), barrés en
« C » ou « ½C ». Ils sont calculés à partir du vérificateur (`doigtes.py`), pas éprouvés à
l'instrument. La main droite n'est pas indiquée, sauf le principe pouce / i–m du thème.

## Modifier et régénérer

```sh
python3 vertige_tools.py vertige.ly       # vérifie, écrit vertige.ly avec doigtés
python3 vertige_tools.py --relecture      # accord entendu à chaque temps
lilypond vertige.ly                       # partition PDF et MIDI
python3 synth_vertige.py vertige.wav      # rendu audio
ffmpeg -i vertige.wav -b:a 256k vertige.mp3
```
