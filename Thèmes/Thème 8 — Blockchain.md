---
type: thème
statut: pas vu
---
![[Thème 8 — L_architecture_blockchain_au-delà_du_Bitcoin.m4a]]
# Blockchain

## Présentation
> Thème couvrant la technologie blockchain : fonctionnement, smart contracts, traçabilité, enjeux éthiques/juridiques et impact énergétique. Applications au-delà des cryptomonnaies, notamment en supply chain et services.

## Sujets associés
| ID | Sujet |
|----|-------|
| 45 | Pourquoi la blockchain est considérée comme la nouvelle révolution numérique ? |
| 46 | La blockchain, un outil permettant la gestion de la traçabilité |
| 47 | Les problématiques éthiques et juridiques de la blockchain |
| 48 | Le droit face aux technologies tel que la blockchain ? |
| 49 | Blockchain et empreinte énergétique |

## Notions clés

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Blockchain")
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
- Qu'est-ce que la blockchain et comment fonctionne-t-elle concrètement ?
- Proof of Work vs Proof of Stake : quelles différences et quel impact environnemental ?
- Comment la blockchain peut-elle améliorer la traçabilité en supply chain ?
- Smart contracts : quels cas d'usage concrets en entreprise ?
- Blockchain permissionnée vs publique : laquelle choisir pour une entreprise ?
- Quels sont les enjeux juridiques de la blockchain (MiCA, PACTE, droit à l'oubli) ?
- Comment la blockchain répond-elle aux enjeux de la confiance numérique ?
- DeFi : opportunité ou menace pour le système financier traditionnel ?
- Quel est le bilan environnemental de la blockchain et comment l'améliorer ?
- Identité décentralisée (SSI) : comment ça fonctionne et quel intérêt pour l'entreprise ?

## Liens transversaux
- Thèmes connexes : [[Thème 2 — Cybersécurité]], [[Thème 1 — SI et environnement]], [[Thème 4 — Big DATA]]
- Notions partagées avec d'autres thèmes :
  - [[Impact environnemental de la blockchain]] → SI et environnement
  - [[Zero-Knowledge Proof (ZKP)]] → Cybersécurité
  - [[RFID - NFC et IoT pour la traçabilité]] → Développement
