---
type: thème
statut: pas vu
---
![[Thème 4 — Architecture_et_gouvernance_des_données_modernes.m4a]]
# Big DATA

## Présentation
> Thème autour de la collecte, du traitement et de la valorisation des données massives. Couvre les enjeux business, les outils, la législation (RGPD) et les liens avec l'IA. Sujet stratégique pour la prise de décision en entreprise.

## Sujets associés
| ID | Sujet |
|----|-------|
| 21 | Big Data, une masse d'opportunités mais une masse de risques |
| 22 | Big Data, des outils inadaptés aux petites entreprises |
| 23 | Big Data et IA : un réel enjeu business |
| 24 | Data Analytics ou comment donner de la valeur aux données |
| 25 | Big Data, surveillance et confiance |
| 26 | Big Data et législation |
| 27 | La gestion des données dans un SI |

## Notions clés

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Big DATA")
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
- Qu'est-ce que les 5V du Big Data et pourquoi sont-ils importants ?
- Data Lake vs Data Warehouse : quand utiliser l'un ou l'autre ?
- Comment mettre en place une gouvernance des données dans une PME ?
- Quels outils Big Data sont adaptés aux petites entreprises ?
- Comment le RGPD impacte-t-il un projet Big Data ?
- Quelle est la différence entre analytics descriptive, prédictive et prescriptive ?
- Data Mesh vs Data Fabric : quelle architecture choisir ?
- Comment justifier le ROI d'un projet Big Data auprès du CODIR ?
- Quels sont les risques du Big Data en termes de surveillance et de vie privée ?
- Comment assurer la qualité des données (data quality) ?
- Quel est l'impact du DSA/DMA sur les entreprises qui exploitent des données ?

## Liens transversaux
- Thèmes connexes : [[Thème 9 — IA]], [[Thème 2 — Cybersécurité]], [[Thème 3 — Cloud et Virtualisation]], [[Thème 7 — Management et stratégie]]
- Notions partagées avec d'autres thèmes :
  - [[RGPD]] → Cybersécurité, Cloud, Mobilité, IA
  - [[Souveraineté numérique]] → Cloud, Management
  - [[Privacy by Design]] → Cybersécurité
  - [[Bases NoSQL]] → IA
  - [[Types d'analytics]] → IA
  - [[Data Lake - Data Warehouse - Lakehouse]] → Cloud
  - [[CLOUD Act et transferts de données]] → Cloud, Mobilité
  - [[Data Act]] → Cloud
