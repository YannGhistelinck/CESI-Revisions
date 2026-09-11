---
type: notion
thèmes:
  - Management et stratégie
  - Développement
statut: pas vu
dernière_révision: null
---

# SAFe et agilité à l'échelle

## En bref

### Définition
SAFe (Scaled Agile Framework) est le cadre le plus utilisé pour déployer l'agilité à l'échelle d'une organisation (plusieurs équipes Agile travaillant de manière coordonnée). Il synchronise les équipes, les programmes et le portefeuille autour d'un rythme commun via les PI Planning. L'agilité à l'échelle (Scaling Agile) répond à la limite de Scrum et Kanban, conçus pour une seule équipe.

### Pourquoi c'est important
Passer de l'agilité d'équipe à l'agilité organisationnelle est le défi majeur des grandes DSI. SAFe permet de livrer de la valeur en continu à grande échelle tout en alignant les équipes sur la stratégie. C'est un sujet central pour un MAALSI qui pilote des programmes multi-équipes.

### Chiffres clés
- SAFe est le cadre de scaling agile le plus utilisé : 37 % des entreprises (State of Agile Report, 2023)
- Plus de 1 million de professionnels formés SAFe (Scaled Agile, Inc.)
- Les entreprises utilisant SAFe rapportent 35-75 % de gains en time-to-market (Scaled Agile, Inc.)
- SAFe 6.0 publié en 2023 — version courante

---

## Approfondir

### Fonctionnement

#### Structure de SAFe — Les 4 niveaux (SAFe 6.0)
1. **Niveau Équipe** : équipes Agile (Scrum, Kanban) de 5 à 11 personnes, sprints de 2 semaines
2. **Niveau Programme (ART)** : Agile Release Train — 50 à 125 personnes, plusieurs équipes synchronisées sur un Program Increment (PI) de 8 à 12 semaines
3. **Niveau Large Solution** : coordination de plusieurs ART pour des solutions complexes (aérospatiale, défense)
4. **Niveau Portefeuille** : alignement stratégique, budgets Lean, Epic owners

#### PI Planning (Program Increment Planning)
- Événement central de SAFe : réunion de 2 jours en présentiel (ou hybride) toutes les 8-12 semaines
- Objectif : aligner toutes les équipes d'un ART sur les objectifs du PI, identifier les dépendances, planifier les sprints
- Livrables : PI Objectives (par équipe), Program Board (dépendances et risques), Roam the Risks
- Considéré comme "le cœur de SAFe"

#### Rôles clés SAFe
- **Release Train Engineer (RTE)** : coach Agile de l'ART, facilite les cérémonies ART, résout les impediments
- **Product Manager** : vision produit et priorisation du Program Backlog
- **System Architect** : cohérence architecturale de l'ART
- **Business Owner** : représentant métier au PI Planning
- **Scrum Master / Team Coach** : au niveau équipe

#### Flux de valeur (Value Stream)
- Séquence d'étapes qui crée de la valeur pour le client
- SAFe organise les ART autour des value streams (pas des départements)
- Deux types : Operational Value Streams (flux clients), Development Value Streams (flux produit IT)

#### Innovation and Planning (IP) Iteration
- Sprint dédié à la fin de chaque PI
- Objectifs : innovation, formation, préparation du PI Planning suivant, réduction de la dette technique

#### Modèle Spotify
- Alternative à SAFe, développée par Spotify
- Organisation en **Squads** (équipes), **Tribes** (regroupement de squads), **Chapters** (communautés de pratiques par métier), **Guilds** (communautés inter-tribes)
- Philosophie : autonomie maximale des squads, alignement léger
- Attention : Spotify lui-même a abandonné ce modèle en 2021 ; c'est un modèle inspirationnel, pas prescriptif

#### Autres cadres de scaling agile
| Cadre | Description |
|-------|-------------|
| LeSS (Large-Scale Scrum) | Scrum étendu à plusieurs équipes, minimaliste |
| Nexus | Extension Scrum (Scrum.org), 3-9 équipes |
| Disciplined Agile (DA) | Boîte à outils agile contextuelle (PMI) |
| SAFe Lean Portfolio | Sous-ensemble de SAFe pour le portefeuille |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Coordination à grande échelle | Lourd et prescriptif (risque de "wagile") |
| Alignement stratégie/équipes | Coût de formation élevé (certifications SAFe) |
| PI Planning : visibilité et synchronisation | Transformation culturelle profonde nécessaire |
| Compatible Scrum, Kanban, XP | Résistance des managers intermédiaires |
| Amélioration continue intégrée (Inspect & Adapt) | Peut freiner l'autonomie des équipes |

### Acteurs et solutions

| Acteur / Solution | Rôle |
|-------------------|------|
| Scaled Agile, Inc. | Propriétaire de SAFe, certifications (SP, SPC, RTE...) |
| Jira (Atlassian) | Outil de gestion Agile, plugin SAFe |
| Azure DevOps | Gestion backlog et PI à l'échelle Microsoft |
| Miro / MURAL | PI Planning en visuel collaboratif (remote) |
| Agility Health | Évaluation de la maturité agile |

### Cas d'usage concrets

- **Banque en ligne** : déploiement de SAFe sur 8 ART (600 personnes) pour transformer la livraison applicative, PI Planning trimestriel — time-to-market réduit de 6 mois à 6 semaines
- **Constructeur automobile** : SAFe Large Solution pour développer le logiciel embarqué des véhicules électriques avec 15 ART coordonnés
- **Administration publique** : adoption du modèle Spotify (squads/tribes) pour restructurer la DSI de 300 personnes autour des flux de valeur plutôt que des directions métiers
- **Télécoms** : PI Planning hybride (présentiel + distanciel) sur 4 sites internationaux avec Miro — synchronisation de 12 équipes sur la roadmap 5G

### Chiffres et tendances

- 74 % des organisations agile à l'échelle utilisent SAFe comme référentiel principal (State of Agile, 2023)
- SAFe 6.0 (2023) : nouvelles guidance sur l'IA, le travail hybride, la mesure des OKR et des Business Agility
- Tendance 2024-2025 : "Lean Portfolio Management" pour remplacer les budgets projet par des budgets flux de valeur
- OKR (Objectives and Key Results) de plus en plus intégrés à SAFe pour l'alignement stratégique

---

## Flashcards
#flashcards

Qu'est-ce qu'un ART dans SAFe ? :: Agile Release Train : groupe de 50 à 125 personnes (plusieurs équipes Agile) synchronisées sur un rythme commun (PI de 8-12 semaines), organisées autour d'un flux de valeur.

Quel est l'objectif d'un PI Planning ? :: Aligner toutes les équipes d'un ART sur les objectifs du Program Increment (8-12 semaines), identifier les dépendances inter-équipes et planifier les sprints — événement de 2 jours considéré comme le cœur de SAFe.

Quelle est la différence entre SAFe et le modèle Spotify ? :: SAFe est prescriptif (rôles, cérémonies, niveaux définis). Le modèle Spotify est inspirationnel (squads, tribes, chapters, guilds) et prône l'autonomie maximale. Spotify a lui-même abandonné ce modèle en 2021.

Quels sont les 4 niveaux de SAFe 6.0 ? :: Équipe (sprints 2 semaines), Programme/ART (PI 8-12 semaines), Large Solution (plusieurs ART), Portefeuille (alignement stratégique et budgets Lean).

Quel est le rôle du Release Train Engineer (RTE) ? :: Coach Agile de l'ART : facilite les cérémonies du programme (PI Planning, ART Sync, Inspect & Adapt), résout les obstacles inter-équipes et aide l'ART à améliorer ses pratiques.

Qu'est-ce qu'une IP Iteration dans SAFe ? :: Innovation and Planning Iteration : sprint dédié à la fin de chaque PI pour l'innovation, la formation, la réduction de dette technique et la préparation du PI Planning suivant — protège le temps d'amélioration continue.

---

## Sources

- Scaled Agile, Inc., *SAFe 6.0 Framework*, scaledagileframework.com, 2023
- State of Agile Report, *17th Annual State of Agile Report*, Digital.ai, 2023
- Kniberg & Ivarsson, *Scaling Agile @ Spotify*, Spotify Labs, 2012
- PMI, *Disciplined Agile Toolkit*, 2023

---

## Notions liées

- [[Gouvernance IT]]
- [[RACI et outils de gouvernance projet]]
- [[DevOps]]
- [[CI - CD]]
- [[TOGAF et architecture d'entreprise]]
- [[DORA Metrics]]
