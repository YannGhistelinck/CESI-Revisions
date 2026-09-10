---
type: suivi
---

# Suivi par thème

> Progression de la révision, dérivée automatiquement du frontmatter des notions.
> Le statut se met à jour dans la note elle-même (`statut: pas vu | vu | maîtrisé`).
> Une notion rattachée à plusieurs thèmes est comptée dans chacun d'eux.

## Progression globale

> Une ligne par thème. La colonne `%` compte une notion `vu` pour moitié et `maîtrisé` pour 1.
> Ce tableau utilise Dataview : Bases ne sait pas encore éclater une propriété de type liste
> en une ligne par valeur (une ligne = un fichier).

```dataview
TABLE
  length(rows) AS "Notions",
  length(filter(rows, (r) => r.statut = "maîtrisé")) AS "Maîtrisé",
  length(filter(rows, (r) => r.statut = "vu")) AS "Vu",
  length(filter(rows, (r) => r.statut = "pas vu")) AS "Pas vu",
  round(100 * (length(filter(rows, (r) => r.statut = "maîtrisé"))
             + 0.5 * length(filter(rows, (r) => r.statut = "vu")))
        / length(rows)) + " %" AS "%"
FROM "Notions"
FLATTEN thèmes AS theme
GROUP BY theme AS "Thème"
SORT key ASC
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
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
    summaries:
      file.name: Count
```
