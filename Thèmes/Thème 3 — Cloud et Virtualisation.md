---
type: thème
statut: pas vu
---
![[Thème 3 — Cloud et Virtualisation.m4a]]
# Cloud et Virtualisation

## Présentation
> Thème traitant des infrastructures cloud (IaaS, PaaS, SaaS), de la virtualisation, de la conteneurisation et des enjeux de migration. Transformation majeure des SI avec des implications en termes de coûts, sécurité et souveraineté.

## Sujets associés
| ID | Sujet |
|----|-------|
| 14 | Cloud, la solution pour réduire sa facture IT |
| 15 | Cloud souverain, une garantie pour mes données hébergées |
| 16 | Cloud et Sécurité, qui est responsable ? |
| 17 | Migration dans le cloud : Des blocages existent encore... |
| 18 | La conteneurisation et la virtualisation : enjeux, avantages, limites ? |
| 19 | La migration Cloud n'est pas viable, vive le Cloud Native |
| 20 | Le Cloud : la réponse aux problèmes de sécurité des données |

## Notions clés

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Cloud et Virtualisation")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Notions clés
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

## Questions types du jury
- Quelle différence entre IaaS, PaaS et SaaS ? Dans quel cas choisir l'un ou l'autre ?
- Qu'est-ce que le modèle de responsabilité partagée et quelles en sont les implications ?
- Cloud souverain : pourquoi est-ce un enjeu pour les entreprises françaises ?
- Comment évaluer le coût réel du cloud vs une infrastructure on-premise ?
- Quels sont les risques du vendor lock-in et comment les atténuer ?
- Quel impact du CLOUD Act sur les entreprises européennes ?
- Comment sécuriser une infrastructure multi-cloud ?
- Quels sont les 7R de la migration cloud et comment choisir la bonne stratégie ?
- Conteneurisation vs virtualisation : quand privilégier l'un ou l'autre ?
- Qu'est-ce que le Cloud Native et pourquoi migrer ne suffit pas ?
- Comment justifier un projet de migration cloud auprès du CODIR ?

## Liens transversaux
- Thèmes connexes : [[Thème 2 — Cybersécurité]], [[Thème 10 — Optimisation du SI]], [[Thème 1 — SI et environnement]], [[Thème 6 — Mobilité]], [[Thème 4 — Big DATA]]
- Notions partagées avec d'autres thèmes :
  - [[CLOUD Act et transferts de données]] → Big DATA, Mobilité
  - [[Sécurité cloud (CSPM - CASB - CNAPP)]] → Management et stratégie
  - [[SASE - SD-WAN]] → Mobilité, Management et stratégie
  - [[Legacy et dette technique]] → Développement
  - [[Conteneurisation (Docker - Kubernetes)]] → Développement
  - [[Cloud Native et 12-Factor App]] → Développement
  - [[Chiffrement et gestion des clés]] → Cybersécurité
  - [[Data Act]] → Big DATA
