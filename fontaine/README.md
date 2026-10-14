# Fontaine

Pièce pour guitare classique seule, **6ᵉ corde accordée en ré**.
56 mesures à 6/8, environ 1′50. Niveau avancé.

- Partition : [fontaine.pdf](fontaine.pdf)
- Audio : [fontaine.mp3](fontaine.mp3) (rendu synthétique)
- MIDI : [fontaine.midi](fontaine.midi)
- Source LilyPond : [fontaine.ly](fontaine.ly)

## L'idée

Une fontaine : de l'eau qui tombe en gouttes, qui ruisselle, qui jaillit, puis qui coule en continu.
Chaque section de la pièce correspond à une manière de faire « couler » le son sur la guitare, et
chacune repose sur une technique propre à l'instrument.

**Pour tout le monde :** une mélodie chantante, en ré majeur, qu'on entend trois fois sous des
éclairages différents ; un contraste net avec une partie centrale rapide et espagnole (cadence
andalouse en rasgueado) ; une fin en harmoniques, comme suspendue.

**Pour les auditeurs avertis :**
- la partie A est écrite en **campanella** : la main gauche joue la mélodie dans l'aigu (positions IX à
  XVII) pendant que les arpèges utilisent au maximum les cordes à vide, qui continuent de sonner sous
  les notes frettées ;
- le ré grave à vide (6ᵉ corde) ne sert de basse que sous les accords de ré, avec une seule exception
  voulue : à la m. 11, un accord de mi majeur sur ce ré grave donne une couleur lydienne, un instant
  en suspens. Les accords de sol et de mi mineur ont leur vraie fondamentale (sol sur la 5ᵉ corde en
  case X, mi sur la 6ᵉ corde en case XIV), pour que cette couleur ressorte ;
- dans la partie B, le thème revient **en mineur, joué au pouce dans les basses** (m. 25–30), tandis
  que les doigts répètent les trois cordes aiguës à vide (sol, si, mi) : la texture de la partie A est
  renversée, la mélodie en bas et la résonance en haut. Ce « plafond » immobile ne suit pas
  l'harmonie : c'est la mélodie du pouce qui, en bougeant dessous, change le sens des trois mêmes
  notes. Le si bécarre fait entendre ré en **dorien** (m. 25), puis la mineur, un accord de fa avec
  quarte augmentée (m. 28), un sol majeur (m. 29), et la septième de dominante de la au moment où le
  pouce passe par do♯ (m. 30) ;
- la reprise (A′) présente la même mélodie et la même harmonie qu'en A, mais en **trémolo** (p a m i) :
  le pouce garde la basse et le début de chaque arpège ;
- la coda rejoue la tête du thème entièrement en **harmoniques naturelles** (cases XII, VII, V et IV) ;
  le *do♯* de la m. 53 est le 5ᵉ harmonique de la corde de la (case IV), le plus délicat à faire sonner.

## Plan

| Mesures | Section | Technique |
|---|---|---|
| 1–16 | A — *Andantino, come una fontana* | Mélodie aiguë sur arpèges en campanella, cordes à vide |
| 17–24 | B — *Allegro con fuoco* | Liés tirés sur la chanterelle à vide (fa–mi, sol–mi, la–mi…), basse au pouce |
| 25–30 | | Le thème en mineur au pouce, sol-si-mi à vide en doubles croches au-dessus |
| 31–34 | | Rasgueado sur la cadence andalouse (ré m – do – si♭ – la), hémiole, trait descendant lié |
| 35–50 | A′ — *Tremolo, cantabile* | La mélodie de A en trémolo |
| 51–56 | Coda — *Lontano* | La tête du thème en harmoniques naturelles, accord final arpégé |

## Doigtés et positions

La jouabilité a été vérifiée automatiquement : pour chaque demi-mesure de A et A′, le programme cherche
une façon de tenir l'arpège et la note de mélodie sur six cordes distinctes, avec un écart d'au plus
quatre cases (cinq au-delà de la case VII), au plus quatre doigts, et des barrés qui ne passent pas
sur une corde à vide devant sonner. Pour B et la coda, il vérifie chaque attaque avec ce qui sonne
déjà. Parmi les solutions possibles, il préfère un écart réduit, une position basse, et évite les
cases au-delà de XII sur les trois cordes graves. Les positions principales qu'il propose :

| Mesures | Position | Remarque |
|---|---|---|
| 1, 8, 9, 12, 16 | X | ré, fa♯ et la sur cordes 3 et 2 (cases X–XI), ré grave et ré à vide |
| 2 (1ʳᵉ moitié), 7 (2ᵉ moitié), 14 | IX | la majeur : do♯ (4ᵉ corde), mi (3ᵉ), la (2ᵉ) |
| 2 (2ᵉ moitié), 7 (1ʳᵉ moitié) | V | la majeur en position V, mélodie sur la chanterelle case V |
| 3, 6 (1ʳᵉ moitié) | VII–IX | si grave sur la **6ᵉ corde case IX** (grâce à l'accord en ré), si à vide au milieu |
| 3, 5, 6, 13 (sol) | X–XII | sol sur la 5ᵉ corde case X, ré (4ᵉ) et sol (3ᵉ) case XII, si à vide |
| 4, 10 (2ᵉ moitié) | XIV–XVII | le sommet : accord de ré complet sous le la aigu (case XVII) — fa♯ sur la 4ᵉ corde case XVI, la (3ᵉ) XIV, ré (2ᵉ) XV |
| 5 (2ᵉ moitié) | XII–XIV | mi mineur : mi grave sur la 6ᵉ corde case XIV, mi (4ᵉ) case XIV, sol et si à vide |
| 11 | XII–XVI | mi majeur sur basse de ré : mi (4ᵉ case XIV), sol♯ (3ᵉ case XIII), si (2ᵉ case XII) |

Points délicats :
- **Sommet des m. 4, 10 et de leurs reprises en trémolo (m. 38, 44)** : position XIV–XVII, avec le fa♯ en
  case XVI de la 4ᵉ corde, au-dessus de la caisse. C'est la position la plus inconfortable de la pièce,
  mais c'est le seul moyen de garder un accord complet sous la note la plus haute de la mélodie.
- **Trémolo (m. 35–50)** : à noire pointée = 52, soit environ dix notes par seconde ; la mélodie reste sur
  la chanterelle, le pouce joue les basses et les cordes graves de l'arpège.
- **Liés de B** : tous les liés tirent vers la chanterelle à vide, la main gauche monte jusqu'à la case X
  (ré) ; garder la basse au pouce bien régulière.
- **Harmonique case IV** (m. 53, 5ᵉ corde) : effleurer très légèrement, un peu avant la frette.
- **m. 34** : le trait descendant (la – sol – fa – mi – ré – do♯) se joue lié sur la chanterelle,
  en ralentissant vers le trémolo.

## Le son

L'audio est produit par `synth_fontaine.py`, un modèle de corde pincée (synthèse dite Karplus-Strong)
adapté à la guitare seule : chaque note est placée sur la corde choisie par le vérificateur de doigté,
et sonne jusqu'à ce que cette corde soit rejouée ou que la main gauche quitte la position. Les liés
sont rendus sans nouvelle attaque, les rasgueados égrenés, les harmoniques avec un timbre pur. Le
rendu est crédible mais reste synthétique.

## Modifier et régénérer

Les notes sont dans [`fontaine_data.py`](fontaine_data.py) : la mélodie (`MEL`) et les formes
d'arpège (`SHAPES`) de la partie A sont réutilisées pour le trémolo de A′ par les fonctions `tremolo`
et `thumb`. `fontaine_tools.py -v` affiche, pour chaque demi-mesure, la répartition corde/case trouvée.

```sh
python3 fontaine_tools.py fontaine.ly   # vérifie la jouabilité et écrit fontaine.ly
python3 fontaine_tools.py -v            # affiche les positions trouvées (corde, case)
lilypond fontaine.ly                    # partition PDF et MIDI
python3 synth_fontaine.py fontaine.wav  # rendu audio
ffmpeg -i fontaine.wav -b:a 256k fontaine.mp3
```
