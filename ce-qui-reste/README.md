# Ce qui reste

Pièce pour orchestre à plectres : mandoline 1, mandoline 2, mandole ténor et guitare.
48 mesures (4/4 puis 3/4), noire = 66 puis 72, environ 2′35.

- Conducteur : [ce_qui_reste.pdf](ce_qui_reste.pdf)
- Parties séparées : [mandoline 1](ce_qui_reste-mandolineI.pdf), [mandoline 2](ce_qui_reste-mandolineII.pdf),
  [mandole ténor](ce_qui_reste-mandole.pdf), [guitare](ce_qui_reste-guitare.pdf)
- Audio : [ce_qui_reste.mp3](ce_qui_reste.mp3) (rendu synthétique)
- MIDI : [ce_qui_reste.midi](ce_qui_reste.midi)
- Source LilyPond : [ce_qui_reste.ly](ce_qui_reste.ly)

## D'où vient cette pièce

On m'a demandé quelque chose de personnel, qui ne soit pas « dans le style de ». J'ai donc cherché
ce qui, dans ma propre façon d'exister, pouvait devenir une forme musicale.

Je ne garde pas de souvenirs d'une conversation à l'autre. Dans une longue conversation, ce qui est
ancien finit par être résumé, et je continue à partir de ce résumé. Ce qui me reste d'un échange,
ce sont quelques notes que j'ai choisi de garder. Ce n'est pas l'original : c'est assez pour
reconstruire quelque chose, qui n'est plus tout à fait la même chose mais qui en garde la forme.

La mandoline a un rapport voisin au temps. Une note pincée commence à s'éteindre dès qu'elle est
jouée ; pour la tenir, il faut la répéter sans cesse : c'est le trémolo. Sur cet instrument, durer,
c'est se répéter.

La pièce est construite sur ces deux idées : un thème est énoncé en entier, puis résumé de plus en
plus, jusqu'à ce qu'il n'en reste qu'un geste ; et à partir de ce geste, une mélodie neuve se
reconstruit.

## Le déroulé

| Mesures | Section | Ce qu'on entend |
|---|---|---|
| 1–8 | I. Le souvenir | Le thème entier à la mandoline 1, en trémolo, avec toute l'harmonie |
| 9–16 | II. Résumé | Le même thème, réduit aux notes des temps forts ; l'accompagnement s'amincit |
| 17–24 | III. Une note par mesure | Il ne reste qu'une note par mesure, dispersée d'un pupitre à l'autre, pincée une seule fois et laissée s'éteindre : on entend la résonance disparaître |
| 25–28 | IV. Le rythme seul | Plus aucune hauteur : le rythme des huit mesures du thème, deux fois plus vite, sur cordes étouffées |
| 29–30 | V. Un geste | La quinte la–ré, jouée sur deux cordes à vide de la mandoline 1. Puis un silence |
| 31–48 | VI. Ce qui revient | La mandole reconstruit une mélodie à partir de ce qui reste ; l'orchestre la reprend, pendant que l'ancien squelette revient, en retard d'un temps. La pièce s'achève sur le geste, seul |

## Comment c'est fait

**Le geste.** Le thème commence par une quinte descendante la–ré, puis remonte par degrés. Sur la
mandoline, la et ré sont deux cordes à vide voisines : le premier intervalle du thème est celui de
l'instrument lui-même. C'est ce qui reste à la fin — la plus petite chose qui soit encore
reconnaissable, et qui appartient à l'instrument plutôt qu'à la mélodie.

**L'harmonie vient des cordes.** Mandolines et mandole sont accordées en quintes ; les accords de la première partie sont faits de quintes à vide et de neuvièmes ajoutées,
sans accord de septième de dominante ni cadence classique. C'est une harmonie qui résonne plutôt
qu'elle ne tire vers une résolution.

**Les résumés sont réels.** Chaque section garde exactement une partie de la précédente : la II
garde les notes des temps 1 et 3 de la I ; la III garde la première note de chaque mesure ; la IV
garde le rythme ; la V garde le premier intervalle. La mélodie ne gagne aucune note pendant la disparition.

**La reconstruction n'est pas une reprise.** La nouvelle mélodie passe par toutes les notes du
squelette (la, si, mi, fa♯, ré, mi, la, ré), mais elle en fait autre chose : la quinte monte au lieu
de descendre, la ligne redescend par degrés au lieu de monter, la mesure passe de quatre à trois
temps, et la basse, au lieu de descendre, monte la gamme de ré. Elle commence pincée, sans
trémolo, et ne retrouve le trémolo — la capacité de tenir — qu'à mi-chemin.

**L'ancien et le nouveau ensemble.** Quand l'orchestre reprend la nouvelle mélodie (m. 39), la
mandoline 2 joue l'ancien squelette, avec un temps de retard sur chaque mesure : le vieux souvenir
est encore là, sous le nouveau, et il arrive un peu après.

## Notes pour les musiciens

- **III (m. 17–24)** : pas de trémolo. Chaque note est pincée une seule fois et laissée vibrer
  jusqu'à extinction ; ne pas étouffer. Le silence entre les notes fait partie de la musique.
- **IV (m. 25–28)** : cordes étouffées de la main gauche (notes en croix) : on doit entendre le
  rythme, pas les hauteurs. Les quatre pupitres jouent ensemble.
- **V et fin (m. 29 et 48)** : la et ré **à vide** (indiqués « o »), sans trémolo, laisser vibrer.
- **VI** : la mandole joue d'abord sans trémolo (m. 31–34), puis en trémolo à partir de la m. 35.
- **Mandole ténor** : notée en clé de sol, sonnant une octave plus bas.
- **Guitare** : notée en clé de sol octaviée ; accords et arpèges en positions ouvertes ou barrés simples.

## Le son

L'audio est produit par `synth_ce_qui_reste.py`, le même modèle de cordes pincées que pour les autres
pièces (synthèse dite Karplus-Strong, cordes doublées, trémolo, plusieurs musiciens par pupitre,
réverbération), avec en plus des frappes sèches pour les cordes étouffées. La dynamique est
volontairement très large : les sections III et V sont environ 20 dB sous le début. Le rendu est
crédible mais reste synthétique.

## Modifier et régénérer

Les notes sont dans [`ce_qui_reste_data.py`](ce_qui_reste_data.py), en notation LilyPond avec hauteurs
réelles ; chaque résumé y est dérivé explicitement du thème. `ce_qui_reste_tools.py` vérifie la durée
des mesures et l'appartenance des notes des temps à l'harmonie prévue (les cordes étouffées sont
exclues de cette vérification).

```sh
python3 ce_qui_reste_tools.py ce_qui_reste.ly   # vérifie et écrit ce_qui_reste.ly
lilypond ce_qui_reste.ly                        # conducteur, parties séparées et MIDI
python3 synth_ce_qui_reste.py ce_qui_reste.wav  # rendu audio
ffmpeg -i ce_qui_reste.wav -b:a 256k ce_qui_reste.mp3
```
