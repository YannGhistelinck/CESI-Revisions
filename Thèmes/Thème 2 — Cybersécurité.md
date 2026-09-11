---
type: thème
statut: pas vu
---
![[Thème 2 — Cybersécurité.m4a]]
# Cybersécurité

## Présentation
> Thème couvrant la protection des SI contre les menaces cyber : stratégies de défense, gouvernance de la sécurité, sensibilisation des utilisateurs et organisation des équipes sécurité. Sujet central pour tout manager IT.

## Sujets associés
| ID | Sujet |
|----|-------|
| 6 | Cybersécurité et IA, l'avenir d'un SI résilient |
| 7 | PME, les grands oubliés de la Cybersécurité |
| 8 | La Cybersécurité, l'humain reste la clé du problème |
| 9 | Sous-traiter le SOC, la solution des structures de taille moyenne |
| 10 | IA, un passage obligé pour le traitement des menaces |
| 11 | Monter son SOC est-il une bonne réponse aux risques Cyber ? |
| 12 | Comment gérer les risques Cyber quand on est une petite entreprise ? |
| 13 | Cybersécurité : Comment impliquer les utilisateurs ? |

## Notions clés

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
- Quelles sont les principales menaces cyber pour une PME en 2025 ?
- SOC interne ou externalisé : comment choisir pour une ETI ?
- Comment sensibiliser efficacement les collaborateurs à la cybersécurité ?
- Qu'est-ce que le modèle Zero Trust et pourquoi remplace-t-il l'approche périmétrique ?
- Comment l'IA transforme-t-elle la détection des menaces ?
- Quelle est la différence entre un EDR, un XDR et un NDR ?
- Comment réaliser une analyse de risques avec EBIOS RM ?
- Quelles sont les obligations de NIS2 pour les entreprises ?
- PCA/PRA : comment les adapter face aux ransomwares ?
- Quel est le rôle du RSSI face à l'avènement du cloud ?
- Comment justifier le budget cybersécurité auprès du CODIR ?
- Quelle est la valeur ajoutée d'une cyber-assurance ?

## Liens transversaux
- Thèmes connexes : [[Thème 9 — IA]], [[Thème 7 — Management et stratégie]], [[Thème 3 — Cloud et Virtualisation]], [[Thème 6 — Mobilité]]
- Notions partagées avec d'autres thèmes :
  - [[Zero Trust]] → Cloud, Mobilité
  - [[PCA - PRA]] → Management et stratégie
  - [[NIS2]] → Cloud, Mobilité
  - [[Authentification et gestion des accès (IAM)]] → Cloud, Mobilité
  - [[IA en cybersécurité]] → IA
  - [[SOC]] → IA
  - [[Sensibilisation et facteur humain]] → Mobilité
