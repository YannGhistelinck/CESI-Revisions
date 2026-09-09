---
type: thème
statut: pas vu
---

# {{titre}}

## Présentation
> Description du thème en 2-3 phrases. Pourquoi ce thème est important dans le contexte d'une DSI.

## Sujets associés
| ID | Sujet |
|----|-------|
| | |

## Notions clés

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("REMPLACER PAR LE LIBELLÉ EXACT DU FRONTMATTER")
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
- 

## Liens transversaux
- Thèmes connexes : [[]]
