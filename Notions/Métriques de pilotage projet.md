---
type: notion
thèmes:
  - Optimisation du SI
  - Développement
statut: pas vu
dernière_révision: 
---

# Métriques de pilotage projet

## En bref

### Définition
Les métriques de pilotage projet sont des indicateurs quantifiables permettant de mesurer et d'optimiser la performance des équipes de développement logiciel. Elles couvrent le flux (vélocité, lead time, cycle time, throughput), la valeur acquise (EVM) et la vision systémique des livraisons (Value Stream Management).

### Pourquoi c'est important
Sans métriques de flux, les équipes naviguent à l'aveugle. Ces indicateurs permettent de détecter les goulots d'étranglement, de prévoir les livraisons avec fiabilité, de mesurer les améliorations continues et de justifier les investissements projet auprès des parties prenantes.

### Chiffres clés
- Les équipes mesurant leur **lead time** livrent **2x plus vite** que celles qui ne le font pas (DORA Report 2023)
- Un écart de **vélocité > 20 %** d'un sprint à l'autre signale un problème de planification ou de dette technique
- L'EVM permet de prédire le coût final d'un projet avec une précision de **±10 %** dès le premier tiers d'avancement
- Les équipes pratiquant le Value Stream Management réduisent leur lead time de **30 à 60 %** (Tasktop, 2022)

---

## Approfondir

### Fonctionnement

#### Métriques de flux (Flow Metrics)

##### Vélocité (Agile/Scrum)
- **Définition** : nombre de story points livrés par sprint (généralement 2 semaines)
- **Usage** : planification des sprints futurs, capacité de l'équipe
- **Limite** : non comparable entre équipes (story points arbitraires par équipe)
- **Bonne pratique** : moyenne glissante sur les 3 derniers sprints

##### Lead Time
- **Définition** : temps écoulé entre la création d'une demande et sa livraison en production
- **Mesure** : du moment où un ticket entre dans le backlog jusqu'au déploiement
- **Inclut** : temps d'attente + temps de traitement actif
- **Objectif** : le réduire au maximum pour répondre plus vite au marché

##### Cycle Time
- **Définition** : temps écoulé entre le début du travail sur une tâche et sa livraison
- **Différence avec Lead Time** : le cycle time exclut l'attente en backlog
- **Formule** : Cycle Time = Lead Time − Temps d'attente (queue time)
- **Usage** : mesure de l'efficacité du processus de développement

```
Création ticket → [ATTENTE BACKLOG] → Début travail → [CYCLE TIME] → Livraison prod
|←────────────────────── LEAD TIME ──────────────────────────────────────────────→|
```

##### Throughput
- **Définition** : nombre d'éléments (stories, tickets) livrés par unité de temps
- **Usage** : capacité réelle de l'équipe, prévision de livraison
- **Avantage sur la vélocité** : agnostique à la taille des stories, plus fiable

#### EVM — Earned Value Management

L'EVM est un cadre de contrôle de projet combinant périmètre, coût et délais.

| Indicateur | Formule | Interprétation |
|---|---|---|
| **PV** (Planned Value) | Budget planifié à date | Ce qu'on devait avoir fait |
| **EV** (Earned Value) | % avancement × Budget total | Ce qu'on a réellement produit |
| **AC** (Actual Cost) | Coûts réellement dépensés | Ce qu'on a dépensé |
| **SV** (Schedule Variance) | EV − PV | <0 = en retard |
| **CV** (Cost Variance) | EV − AC | <0 = dépassement budget |
| **SPI** (Schedule Performance Index) | EV / PV | <1 = en retard |
| **CPI** (Cost Performance Index) | EV / AC | <1 = sur-budget |
| **EAC** (Estimate at Completion) | BAC / CPI | Prévision du coût final |

**Exemple :** Projet à 100k€, 50 % avancé, dépensé 60k€
- EV = 50k€, AC = 60k€ → CV = −10k€ (dépassement)
- CPI = 0,83 → EAC = 120k€ (coût final prévu)

#### Value Stream Management (VSM)

- **Définition** : approche systémique mesurant le flux de valeur de l'idée à la production
- **Value Stream** : ensemble des étapes nécessaires pour transformer une demande en valeur livrée
- **Flow Efficiency** : Temps de travail actif / Lead Time total (objectif > 15-20 %)
- **Goulots d'étranglement** : étapes où les tickets s'accumulent (WIP trop élevé)
- **Outils** : Tasktop (now Planview), ConnectALL, LeanKit

#### Loi de Little (Lean)

> **Lead Time = WIP (Work in Progress) / Throughput**

Implication : réduire le WIP est le levier le plus puissant pour réduire le lead time.

#### Cumulative Flow Diagram (CFD)

- Représentation visuelle du flux de tickets par état au fil du temps
- Permet de visualiser les accumulations (goulots) et la stabilité du flux
- Pente de la courbe "Done" = throughput

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Objectivation de la performance des équipes | Risque de Goodhart (optimiser la métrique, pas la valeur) |
| Prévision fiable des livraisons (EVM, throughput) | Effort de collecte et d'outillage non négligeable |
| Détection précoce des goulots (VSM, CFD) | Vélocité incomparable entre équipes différentes |
| Alignement métier-IT sur la valeur livrée | EVM inadapté aux projets Agile purs sans périmètre fixe |
| Base de l'amélioration continue (Kaizen) | Risque de sur-mesure (indicator fatigue) |

### Acteurs

- **Outils Agile** : Jira, Azure DevOps, Linear, Shortcut
- **VSM / Flow** : Tasktop (Planview), ConnectALL, Allstacks
- **EVM** : MS Project, Primavera P6, Wrike
- **Référentiels** : PMBOK (EVM), SAFe (PI Metrics), DORA (4 Key Metrics)

### Cas d'usage

- **Sprint Review** : analyse de la vélocité pour ajuster la capacité du prochain sprint
- **Contrôle de projet** : CPI < 0,9 déclenche une révision de scope ou de budget
- **Amélioration continue** : rétrospective Lean basée sur le cycle time et la flow efficiency
- **Planification SAFe** : PI Planning utilisant la vélocité des équipes pour allouer les features
- **DevOps** : DORA metrics (deployment frequency, lead time for changes, MTTR, change failure rate)

### Chiffres complémentaires

- Les **4 métriques DORA** sont : Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR
- Les équipes "Elite" DORA déploient **plusieurs fois par jour** avec un lead time < 1 heure
- Flow Efficiency moyenne dans l'industrie logicielle : **15 à 25 %** (85 % du temps est de l'attente)

---

## Flashcards
#flashcards

Quelle est la différence entre Lead Time et Cycle Time ? :: Le Lead Time court de la création du ticket à la livraison (inclut l'attente backlog). Le Cycle Time court du début du travail actif à la livraison. Cycle Time = Lead Time − temps d'attente en backlog.

Quelle est la loi de Little et son implication concrète ? :: Lead Time = WIP / Throughput. Implication : limiter le Work in Progress est le levier le plus efficace pour réduire le lead time sans augmenter la capacité.

Qu'est-ce que le CPI en EVM et que signifie un CPI de 0,8 ? :: Cost Performance Index = EV/AC. Un CPI de 0,8 signifie qu'on obtient 0,80€ de valeur pour chaque 1€ dépensé — le projet est en dépassement budgétaire de 20 %.

Pourquoi la vélocité est-elle une métrique dangereuse si mal utilisée ? :: Elle est arbitraire et non comparable entre équipes (story points calibrés différemment). Elle peut inciter à gonfler les estimations. Elle mesure l'output, pas l'outcome (valeur livrée).

Qu'est-ce que la Flow Efficiency et quel est son objectif ? :: Ratio entre temps de travail actif et lead time total. Dans l'industrie logicielle, elle est souvent de 15-25 %, signifiant que 75-85 % du temps est de l'attente. L'objectif est de l'augmenter via la réduction du WIP.

Quelles sont les 4 métriques DORA ? :: Deployment Frequency, Lead Time for Changes, Change Failure Rate (CFR), Mean Time to Recover (MTTR).

Qu'est-ce qu'un Cumulative Flow Diagram ? :: Un graphique montrant le nombre de tickets par état (To Do, In Progress, Done) au fil du temps. Une accumulation dans un état révèle un goulot d'étranglement.

---

## Sources

- DORA — "Accelerate State of DevOps Report" 2023
- Tasktop — "Flow Framework" (Mik Kersten, 2018)
- PMI — PMBOK 7e édition (EVM)
- Nicole Forsgren, Jez Humble, Gene Kim — "Accelerate" (2018)
- Tonianne DeMaria Barry & Jim Benson — "Personal Kanban" (Loi de Little)

---

## Notions liées

[[KPI et pilotage de la performance]] · [[Frameworks de gestion de projet]] · [[DORA Metrics]] · [[CI - CD]] · [[DevOps]] · [[SRE (Site Reliability Engineering)]] · [[MTTR - MTBF]] · [[Observabilité]] · [[TDD - BDD]]
