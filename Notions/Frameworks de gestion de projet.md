---
type: notion
thèmes:
  - Optimisation du SI
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Frameworks de gestion de projet

![[N — Frameworks de gestion de projet.mp3]]
## En bref

### Définition
Un framework de gestion de projet est un cadre structuré de méthodes, processus et bonnes pratiques guidant la planification, l'exécution et le contrôle de projets. Les principaux référentiels sont PMBOK (PMI), PRINCE2, SAFe (Agile à l'échelle), et ISO 21500. La gestion de portefeuille agrège plusieurs projets sous un prisme stratégique.

### Pourquoi c'est important
Les frameworks permettent de standardiser les pratiques, réduire les risques, améliorer la prévisibilité des livraisons et aligner les projets sur la stratégie de l'entreprise. Dans les SI complexes, ils fournissent un langage commun entre les équipes IT, métier et la direction.

### Chiffres clés
- **70 % des projets IT** échouent ou dépassent le budget/délais initiaux (Standish Group Chaos Report 2023)
- Les organisations matures en gestion de projet livrent **2,5x plus de valeur** par projet (PMI, 2022)
- L'adoption de SAFe dans les grandes entreprises réduit le **time-to-market de 20 à 50 %**
- **PRINCE2** est le standard le plus adopté en Europe, présent dans **150+ pays**
- Le coût moyen d'un projet IT raté dépasse **1 M€** pour les grandes entreprises (McKinsey)

---

## Approfondir

### Fonctionnement

#### PMBOK — Project Management Body of Knowledge

- **Éditeur** : PMI (Project Management Institute)
- **Version actuelle** : PMBOK 7 (2021) — orienté principes vs processus (PMBOK 6)
- **Structure PMBOK 6** : 10 domaines de connaissance, 5 groupes de processus, 49 processus
- **Certification** : PMP (Project Management Professional) — 1 M+ certifiés dans le monde

| Groupe de processus | Activités clés |
|---|---|
| **Démarrage** | Charte de projet, identification des parties prenantes |
| **Planification** | WBS, planning, budget, gestion des risques |
| **Exécution** | Coordination des équipes, gestion de la qualité |
| **Surveillance & Contrôle** | EVM, gestion des changements, rapports d'avancement |
| **Clôture** | Livraison, retour d'expérience, clôture administrative |

**PMBOK 7 — 12 Principes** (shift majeur vers l'Agile) :
Intendance, collaboration, parties prenantes, valeur, pensée systémique, leadership, tailoring, qualité, complexité, risques, adaptabilité, changement.

#### PRINCE2 — PRojects IN Controlled Environments

- **Éditeur** : AXELOS (Royaume-Uni), désormais PeopleCert
- **Structure** : 7 principes, 7 thèmes, 7 processus
- **Approche** : management par exception, justification business continue (Business Case)
- **Certification** : PRINCE2 Foundation / Practitioner

| 7 Principes | Description |
|---|---|
| Justification business continue | Un projet doit toujours avoir un Business Case valide |
| Apprendre de l'expérience | Leçons apprises tout au long du projet |
| Rôles définis | Responsabilités claires (RACI) |
| Management par séquences | Découpage en étapes gérables |
| Management par exception | Délégation avec seuils de tolérance |
| Focus sur les produits | Livraisons définies, pas les activités |
| Adaptation | Tailoring selon le contexte |

#### SAFe — Scaled Agile Framework

- **Éditeur** : Scaled Agile, Inc. (Dean Leffingwell, 2011)
- **Objectif** : appliquer Agile/Lean à grande échelle (équipes, programmes, portefeuille)
- **Version actuelle** : SAFe 6.0 (2023)

**Niveaux SAFe :**

| Niveau | Périmètre | Cadence |
|---|---|---|
| **Team** | Équipes Scrum/Kanban | Sprint (2 semaines) |
| **Program** | Agile Release Train (ART) | PI (Program Increment = 5 sprints) |
| **Large Solution** | Solution Train (multi-ART) | PI Planning |
| **Portfolio** | Épics stratégiques, budget Lean | Lean Portfolio Management |

**PI Planning** : événement SAFe de 2 jours où toutes les équipes d'un ART planifient ensemble le prochain PI (10 semaines).

#### ISO 21500 — Guide de management de projet

- Norme internationale publiée en 2012, révisée en 2021 (ISO 21502)
- Compatible avec PMBOK, fournit un référentiel commun universel
- Applicable à tout type de projet (IT, construction, R&D)
- Complétée par ISO 21503 (programme), ISO 21504 (portefeuille)

#### Gestion de portefeuille de projets (PPM)

- **Définition** : gouvernance et optimisation d'un ensemble de projets alignés sur la stratégie
- **Objectif** : maximiser la valeur globale, équilibrer risques/opportunités, allouer les ressources
- **Outils** : Planview, MS Project Online, ServiceNow PPM, Clarity (Broadcom)
- **Matrices** : matrice BCG, scoring multicritères, roadmaps stratégiques

#### Comparatif des frameworks

| Critère | PMBOK | PRINCE2 | SAFe | ISO 21500 |
|---|---|---|---|---|
| **Approche** | Best practices | Processus prescriptif | Agile à l'échelle | Référentiel générique |
| **Périmètre** | Projet | Projet | Programme/Portefeuille | Projet |
| **Agilité** | Partielle (PMBOK 7) | Faible (PRINCE2 Agile) | Forte | Faible |
| **Certification** | PMP | Foundation/Practitioner | SA, SP, SPC | Aucune propre |
| **Adoption** | Mondiale | Europe/UK | IT/Software | Internationale |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Standardisation et langage commun | Rigidité des frameworks prescriptifs face à l'incertitude |
| Réduction des risques de dérive | Surcharge administrative (reporting, documentation) |
| Alignement stratégie-projets | Adoption longue et coûteuse (formation, certification) |
| Scalabilité (SAFe pour grandes orgs) | SAFe perçu comme trop lourd par les équipes Agile |
| Reconnaissance internationale (PMP, PRINCE2) | Aucun framework n'est universel |

### Acteurs

- **PMI** (Project Management Institute) — PMBOK, PMP
- **PeopleCert/AXELOS** — PRINCE2
- **Scaled Agile, Inc.** — SAFe
- **ISO** — ISO 21500/21502
- **Outils PPM** : Planview, Jira Align, MS Project, Primavera P6

### Cas d'usage

- **PMBOK** : projets d'infrastructure complexes (migration datacenter, ERP), secteurs régulés
- **PRINCE2** : projets gouvernementaux, grandes ESN européennes
- **SAFe** : transformation Agile d'une DSI avec 10+ équipes, déploiements bancaires
- **ISO 21500** : cadre de référence pour des appels d'offres internationaux
- **PPM** : arbitrage budgétaire entre 50 projets IT d'une grande entreprise

### Chiffres complémentaires

- Le PMI certifie **1 million+** de PMP dans le monde
- SAFe est utilisé par **70 % des entreprises Fortune 100** pratiquant l'Agile à l'échelle
- PRINCE2 est utilisé dans **150 pays** et imposé dans les marchés publics britanniques

---

## Flashcards
#flashcards/Optimisation_du_SI/Frameworks_de_gestion_de_projet #flashcards/Management_et_stratégie/Frameworks_de_gestion_de_projet

Quels sont les 5 groupes de processus PMBOK 6 ? :: Démarrage, Planification, Exécution, Surveillance & Contrôle, Clôture.

Quel est le principe central de PRINCE2 qui le distingue des autres frameworks ? :: Le management par exception : les décisions sont déléguées avec des seuils de tolérance ; on ne remonte à l'échelon supérieur qu'en cas de dépassement de ces tolérances.

Qu'est-ce qu'un PI Planning dans SAFe ? :: Un événement de 2 jours regroupant toutes les équipes d'un Agile Release Train pour planifier ensemble le prochain Program Increment (cycle de 10 semaines / 5 sprints).

Quelle est la différence entre gestion de projet et gestion de portefeuille ? :: La gestion de projet pilote un projet individuel (coût, délai, périmètre). La gestion de portefeuille arbitre entre plusieurs projets pour maximiser la valeur stratégique globale et optimiser l'allocation des ressources.

Quel est le changement majeur entre PMBOK 6 et PMBOK 7 ? :: PMBOK 6 est centré sur 49 processus prescrits ; PMBOK 7 passe à 12 principes de management plus flexibles, intégrant mieux l'approche Agile et la notion de valeur.

Qu'est-ce que l'Agile Release Train (ART) dans SAFe ? :: Une équipe d'équipes (50 à 125 personnes) qui planifient, s'engagent et livrent ensemble selon une cadence commune (PI = 5 sprints), formant le coeur de SAFe au niveau Programme.

Pourquoi ISO 21500 est-elle différente de PMBOK et PRINCE2 ? :: ISO 21500 est une norme internationale générique et non propriétaire, sans certification propre, compatible avec PMBOK et servant de référentiel commun pour les projets internationaux dans tout secteur.

---

## Sources

- PMI — PMBOK Guide 7e édition (2021)
- PeopleCert — PRINCE2 6th Edition (2023)
- Scaled Agile, Inc. — SAFe 6.0 Framework (scaledagileframework.com)
- ISO 21502:2020 — Project Management
- Standish Group — CHAOS Report 2023

---

## Notions liées

[[KPI et pilotage de la performance]] · [[Métriques de pilotage projet]] · [[DORA Metrics]] · [[DevOps]] · [[GitOps]] · [[CI - CD]] · [[Gouvernance IT]] · [[Système d'Information (SI)]] · [[SLA - SLO - SLI]]
