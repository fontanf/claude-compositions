# Compositions de Claude

Pièces originales composées par Claude (Anthropic), gravées avec [LilyPond](https://lilypond.org)
et rendues en audio par des synthétiseurs écrits en Python.

Chaque pièce est dans son propre dossier, avec la partition (PDF), un enregistrement synthétique (MP3),
le fichier MIDI, la source LilyPond et les scripts qui permettent de tout régénérer.

## Pièces

| Pièce | Effectif | Durée | Partition | Audio |
|---|---|---|---|---|
| [Fugue en do mineur](fugue-do-mineur/) | clavier (3 voix) | 1′40 | [PDF](fugue-do-mineur/fugue.pdf) | [MP3](fugue-do-mineur/fugue.mp3) |
| [Mistral](mistral/) | orchestre à plectres : mandolines 1 et 2, mandole, guitare | 2′40 | [conducteur](mistral/plectres.pdf) · parties : [Md. 1](mistral/plectres-mandolineI.pdf), [Md. 2](mistral/plectres-mandolineII.pdf), [mandole](mistral/plectres-mandole.pdf), [guitare](mistral/plectres-guitare.pdf) | [MP3](mistral/plectres.mp3) |

### Fugue en do mineur

Fugue à trois voix dans le style de J.-S. Bach. Exposition (alto, soprano à la dominante, basse),
épisodes en marches harmoniques, entrées en mi♭ majeur, fa mineur et do mineur, coda sur pédale
de tonique avec tierce picarde. Rendu audio : orgue synthétique (synthèse additive) avec réverbération.

### Mistral

Pièce pour orchestre à plectres en mi dorien/éolien, sur un ostinato de guitare en 3+3+2.
Forme : introduction – A (thème à la mandoline 1) – A′ (thème à la mandole) – B *Meno mosso*
(thème en augmentation, réharmonisé en do lydien) – développement en fugato avec mesures à 7/8 –
reprise tutti – coda. Écrite pour mandole ténor (accord sol-ré-la-mi), notée en clé de sol et sonnant une octave plus bas.
Rendu audio : cordes pincées (Karplus-Strong) avec chœurs doublés, trémolo et pupitres de plusieurs musiciens.

## Régénérer une pièce

Prérequis : LilyPond ≥ 2.26 dans le `PATH`, Python 3 avec NumPy et SciPy, ffmpeg.

```sh
cd mistral
python3 plectres_tools.py plectres.ly   # vérifie les mesures et l'harmonie, écrit le .ly
lilypond plectres.ly                    # conducteur, parties séparées et MIDI
python3 synth_plectres.py plectres.wav  # rendu audio
ffmpeg -i plectres.wav -b:a 256k plectres.mp3
```

```sh
cd fugue-do-mineur
python3 fugue_tools.py fugue.ly         # vérifie quintes/octaves parallèles, écrit le .ly
lilypond fugue.ly
python3 synth.py fugue.wav
ffmpeg -i fugue.wav -b:a 256k fugue.mp3
```

Les notes sont écrites mesure par mesure dans `*_data.py` (notation LilyPond, hauteurs absolues) :
c'est le fichier à modifier pour retoucher une pièce.
