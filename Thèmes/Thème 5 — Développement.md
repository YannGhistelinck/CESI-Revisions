---
type: thème
statut: pas vu
---
![[Thème 5 — L_impact_financier_de_l_architecture_logicielle.m4a]]
# Développement

## Présentation
> Thème couvrant les pratiques de développement logiciel : qualité, tests, intégration continue, DevOps, maintenabilité. Inclut aussi les technologies émergentes (RA/RV). Domaine de compétence principal du profil MAALSI.

## Sujets associés
| ID | Sujet |
|----|-------|
| 28 | ISO/CEI 9126, cette norme est nécessaire et suffisante pour garantir la qualité logicielle ? |
| 29 | L'intégration continue : valeur ajoutée/retour sur investissement ? |
| 30 | Apprentissage automatique et automatisation de tests de logiciels |
| 31 | Stratégie de maintenabilité logicielle et les coûts associés ? |
| 32 | En quoi le DevOps peut améliorer la qualité de votre SI et la productivité de vos équipes IT ? |
| 33 | Quels sont les enjeux et le positionnement de la RA/RV pour l'entreprise 4.0 |

## Notions clés

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Développement")
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
- ISO 9126 vs ISO 25010 : pourquoi la norme a-t-elle évolué ?
- Comment mesurer et gérer la dette technique dans un projet ?
- DevOps : quels bénéfices concrets pour la productivité des équipes IT ?
- Comment justifier le ROI de l'intégration continue auprès du CODIR ?
- Quelle stratégie de maintenabilité logicielle adopter et quels coûts prévoir ?
- TDD, BDD : quelles pratiques pour garantir la qualité du code ?
- Comment l'IA transforme-t-elle l'automatisation des tests logiciels ?
- Microservices vs monolithe : comment choisir la bonne architecture ?
- Qu'est-ce que le DevSecOps et pourquoi intégrer la sécurité dès le développement ?
- Quels sont les 4 métriques DORA et comment les utiliser pour piloter la performance ?
- Quels cas d'usage concrets de la RA/RV en entreprise 4.0 ?
- Comment le Platform Engineering améliore-t-il l'expérience développeur ?

## Liens transversaux
- Thèmes connexes : [[Thème 10 — Optimisation du SI]], [[Thème 9 — IA]], [[Thème 3 — Cloud et Virtualisation]], [[Thème 2 — Cybersécurité]], [[Thème 7 — Management et stratégie]]
- Notions partagées avec d'autres thèmes :
  - [[DevOps]] → Optimisation du SI
  - [[CI - CD]] → Cloud, Optimisation du SI
  - [[DevSecOps]] → Cybersécurité, Management
  - [[Infrastructure as Code (IaC)]] → Cloud, Optimisation du SI
  - [[Microservices vs monolithe]] → Cloud
  - [[DORA Metrics]] → Optimisation du SI
  - [[IA et automatisation des tests]] → IA
  - [[Digital Twin]] → IA, Optimisation du SI
  - [[Dette technique]] → Management
  - [[CMMI]] → Management
