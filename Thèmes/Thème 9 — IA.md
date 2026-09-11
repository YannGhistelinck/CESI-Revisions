---
type: thème
statut: pas vu
---
![[Thème 9 — IA_générative_et_réalités_du_machine_learning.m4a]]
# IA

## Présentation
> Thème autour de l'intelligence artificielle : applications en cybersécurité, enjeux éthiques et juridiques, biais algorithmiques, automatisation. Technologie transversale qui impacte tous les autres thèmes.

## Sujets associés
| ID | Sujet |
|----|-------|
| 50 | IA : Les solutions à l'explosion des Cyber-attaques |
| 51 | IA : Enjeux juridiques, éthiques et de gouvernance ? |
| 52 | IA ou l'injustice algorithmique |
| 53 | L'intelligence artificielle peut-elle assurer la sécurité d'une infrastructure de façon autonome ? |
| 54 | IA, La révolution du marketing |
| 55 | Quelle éthique pour l'intelligence artificielle ? |

## Notions clés

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("IA")
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
- Qu'est-ce qu'un LLM et comment fonctionne l'IA générative ?
- RAG vs fine-tuning : quand utiliser l'un ou l'autre ?
- Quels sont les risques des biais algorithmiques et comment les détecter ?
- Comment l'AI Act classifie-t-il les systèmes d'IA par niveau de risque ?
- IA et cybersécurité : l'IA est-elle plus une menace ou une solution ?
- Comment mettre en place une gouvernance de l'IA dans l'entreprise ?
- Shadow AI : comment contrôler l'usage non autorisé de l'IA générative ?
- Quels KPI pour mesurer le ROI d'un projet IA en entreprise ?
- IA de confiance : que signifie le concept et comment l'appliquer ?
- Comment l'IA transforme-t-elle le marketing et la relation client ?
- AIOps : comment l'IA peut-elle optimiser les opérations IT ?

## Liens transversaux
- Thèmes connexes : [[Thème 2 — Cybersécurité]], [[Thème 4 — Big DATA]], [[Thème 5 — Développement]], [[Thème 7 — Management et stratégie]], [[Thème 10 — Optimisation du SI]]
- Notions partagées avec d'autres thèmes :
  - [[AI Act]] → Cybersécurité, Big DATA
  - [[Biais algorithmiques]] → Big DATA
  - [[AIOps]] → Optimisation du SI
  - [[MLOps - DataOps]] → Développement, Big DATA
  - [[Shadow AI]] → Management
  - [[Edge AI]] → Mobilité
  - [[IA générative et LLM]] → Big DATA
