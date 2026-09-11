---
type: suivi
---

# Suivi par notion

> Vue à plat de toutes les notions, générée automatiquement depuis le frontmatter.
> Permet d'identifier rapidement les trous dans la préparation.
> Mettez à jour `statut` et `dernière_révision` dans la note elle-même : le tableau suit.

```base
filters:
  and:
    - file.inFolder("Notions")
properties:
  file.name:
    displayName: Notion
  thèmes:
    displayName: Thème(s)
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Toutes les notions
    order:
      - file.name
      - thèmes
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

> **Légende statuts** : `pas vu` | `vu` | `maîtrisé`
