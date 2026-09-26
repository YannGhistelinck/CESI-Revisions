---
type: index
---

# Référentiels

Index automatique des fiches de notions classées par catégorie. Les fiches apparaissent ici dès qu'elles ont un champ `catégorie` dans leur frontmatter.

---

## Frameworks et cadres de gouvernance
> Cadres méthodologiques pour structurer la gouvernance, le management et les processus IT.

```dataview
TABLE thèmes AS "Thèmes", statut AS "Statut", dernière_révision AS "Dernière révision"
FROM "Notions"
WHERE catégorie = "framework"
SORT file.name ASC
```

---

## Normes et standards
> Référentiels normatifs (ISO, NIST, OWASP…) définissant des exigences ou des bonnes pratiques.

```dataview
TABLE thèmes AS "Thèmes", statut AS "Statut", dernière_révision AS "Dernière révision"
FROM "Notions"
WHERE catégorie = "norme"
SORT file.name ASC
```

---

## Réglementations
> Textes législatifs et réglementaires encadrant les activités numériques.

```dataview
TABLE thèmes AS "Thèmes", statut AS "Statut", dernière_révision AS "Dernière révision"
FROM "Notions"
WHERE catégorie = "réglementation"
SORT file.name ASC
```
