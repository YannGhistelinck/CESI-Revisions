---
type: suivi
---

# Suivi par thème

> Progression de la révision, dérivée automatiquement du frontmatter des notions.
> Le statut se met à jour dans la note elle-même (`statut: pas vu | vu | maîtrisé`).
> Une notion rattachée à plusieurs thèmes apparaît dans chacun d'eux.

## Progression globale

```base
filters:
  - file.inFolder("Notions")
properties:
  file.name:
    displayName: Notion
  thèmes:
    displayName: Thème(s)
views:
  - type: table
    name: Progression globale
    groupBy:
      property: statut
      direction: ASC
    order:
      - file.name
      - thèmes
    summaries:
      file.name: Count
```

---

## SI et environnement

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("SI et environnement")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: SI et environnement
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Cybersécurité

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Cybersécurité")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Cybersécurité
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Cloud et Virtualisation

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
    name: Cloud et Virtualisation
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Big DATA

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
    name: Big DATA
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Développement

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
    name: Développement
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Mobilité

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Mobilité")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Mobilité
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Management et stratégie

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Management et stratégie")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Management et stratégie
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Blockchain

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
    name: Blockchain
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## IA

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
    name: IA
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Optimisation du SI

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Optimisation du SI")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Optimisation du SI
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```

---

## Transversal

```base
filters:
  and:
    - file.inFolder("Notions")
    - thèmes.contains("Transversal")
properties:
  file.name:
    displayName: Notion
  statut:
    displayName: Statut
  dernière_révision:
    displayName: Dernière révision
views:
  - type: table
    name: Transversal
    order:
      - file.name
      - statut
      - dernière_révision
    sort:
      - property: file.name
        direction: ASC
```
