# Fugue en do mineur

Fugue à trois voix (soprano, alto, basse) dans le style de J.-S. Bach, pour clavier.
28 mesures à 4/4, noire = 72, environ 1′40.

- Partition : [fugue.pdf](fugue.pdf)
- Audio : [fugue.mp3](fugue.mp3) (rendu synthétique d'orgue)
- MIDI : [fugue.midi](fugue.midi)
- Source LilyPond : [fugue.ly](fugue.ly)

## Le sujet

Le sujet tient en deux mesures : un arpège ascendant de do mineur (do–mi♭–sol–do), une broderie
autour du do aigu, puis une descente en doubles croches qui retombe sur la tonique par la sensible.
Le contre-sujet, qui accompagne chaque nouvelle entrée, avance par croches pointées et croches,
en rythme complémentaire du sujet.

## Plan

| Mesures | Section | Contenu |
|---|---|---|
| 1–2 | Exposition | Sujet à l'alto (do mineur) |
| 3–4 | | Réponse au soprano (sol mineur), contre-sujet à l'alto |
| 5 | Codetta | Retour vers do mineur, sur le motif de doubles croches du sujet |
| 6–7 | | Sujet à la basse (do mineur) |
| 8–10 | Épisode 1 | Marche harmonique avec retards préparés, modulation vers mi♭ majeur |
| 11–12 | Entrée | Sujet en mi♭ majeur à l'alto, cadence rompue sur do mineur |
| 13–15 | Épisode 2 | Imitations entre soprano et alto, modulation vers fa mineur |
| 16–17 | Entrée | Sujet en fa mineur au soprano |
| 18–19 | Épisode 3 | Retour vers do mineur par la dominante |
| 20–21 | Entrée | Sujet en do mineur à la basse |
| 22–23 | Épisode 4 | Demi-cadence sur sol |
| 24–25 | Entrée finale | Sujet au soprano, dans l'aigu |
| 26–28 | Coda | Pédale de tonique, ralenti, accord final en do majeur (tierce picarde) |

## Vérification du contrepoint

`fugue_tools.py` contient un petit vérificateur qui détecte les quintes et octaves parallèles
entre chaque paire de voix et signale les dissonances sur les temps forts avec la basse.
Il a trouvé deux fautes de parallèles lors de la composition (m. 12 et 19), corrigées depuis.
Les dissonances qu'il signale encore sont voulues : retards préparés, septièmes de dominante,
notes étrangères au-dessus de la pédale finale.

## Le son

L'audio est produit par `synth.py`, un synthétiseur écrit pour l'occasion : timbre d'orgue
(montre 8′ et prestant 4′ en synthèse additive, bourdon 16′ à la basse), légère attaque,
articulation un peu détachée, voix réparties en stéréo et réverbération d'église synthétique.
Le résultat est correct mais moins réaliste qu'un orgue échantillonné ; un rendu du MIDI avec
une banque de sons (FluidSynth, par exemple) donnerait un son plus naturel.

## Modifier et régénérer

Les notes sont écrites mesure par mesure dans [`fugue_data.py`](fugue_data.py), en notation
LilyPond avec hauteurs absolues.

```sh
python3 fugue_tools.py fugue.ly   # vérifie le contrepoint et écrit fugue.ly
lilypond fugue.ly                 # partition PDF et MIDI
python3 synth.py fugue.wav        # rendu audio
ffmpeg -i fugue.wav -b:a 256k fugue.mp3
```
