---
type: notion
thèmes:
  - Optimisation du SI
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# KPI et pilotage de la performance

![[N — KPI et pilotage de la performance.mp3]]
## En bref

### Définition
Un **KPI (Key Performance Indicator)** est un indicateur quantifiable permettant d'évaluer l'atteinte d'un objectif stratégique ou opérationnel. Le pilotage de la performance s'appuie sur un ensemble cohérent d'indicateurs pour aligner les actions de l'organisation sur sa stratégie, en utilisant des cadres comme les OKR, le Balanced Scorecard ou les KRI.

### Pourquoi c'est important
Sans indicateurs bien définis, la prise de décision repose sur des intuitions. Les KPI transforment la stratégie en mesures actionnables, permettent de détecter les dérives, d'allouer les ressources efficacement et de démontrer la valeur de l'IT au métier.

### Chiffres clés
- **74 % des entreprises** affirment que leurs données analytiques ne sont pas exploitées de façon optimale (Forrester, 2023)
- Les entreprises "data-driven" sont **23 fois plus susceptibles** d'acquérir des clients et **6 fois plus susceptibles** de les fidéliser (McKinsey)
- La loi de Goodhart s'applique dans **90 % des cas** où un indicateur devient une cible fixe (phénomène de gaming des métriques)
- Les OKR augmentent l'alignement des équipes de **55 %** en moyenne (Betterworks, 2023)

---

## Approfondir

### Fonctionnement

#### Taxonomie des indicateurs

| Type | Définition | Exemple SI |
|---|---|---|
| **KPI** (Key Performance Indicator) | Mesure l'atteinte d'un objectif | Taux de disponibilité du SI : 99,9 % |
| **KRI** (Key Risk Indicator) | Mesure le niveau d'exposition à un risque | Nombre de vulnérabilités critiques non patchées |
| **OKR** (Objective & Key Result) | Objectif ambitieux + résultats mesurables | O: "Améliorer l'expérience utilisateur" / KR: "NPS > 50" |
| **Vanity Metric** | Chiffre flatteur sans valeur décisionnelle | Nombre de pages vues sans conversion |
| **Leading Indicator** | Prédit une performance future | Nombre de tests automatisés écrits |
| **Lagging Indicator** | Constate une performance passée | Chiffre d'affaires du trimestre |

#### Le Balanced Scorecard (BSC) — Kaplan & Norton (1992)

Le BSC équilibre 4 axes pour éviter de piloter uniquement par les finances :

| Axe | Question clé | Exemple IT |
|---|---|---|
| **Financier** | Comment nous perçoivent nos actionnaires ? | Coût moyen par ticket IT |
| **Client** | Comment nous perçoivent nos clients ? | NPS, taux de satisfaction utilisateur |
| **Processus internes** | En quoi excellons-nous ? | Taux d'automatisation des processus |
| **Apprentissage** | Comment améliorer et innover ? | % d'équipes formées aux nouvelles technos |

#### OKR — Objectives & Key Results

Popularisé par Intel (Andy Grove), adopté par Google dès 1999 :
- **Objective** : ambitieux, qualitatif, inspirant
- **Key Results** : 3 à 5 mesures vérifiables, binaires ou graduelles
- Cycle : trimestriel (quarterly OKRs) + annuel
- Score cible : **0,6 à 0,7** (100 % = objectif pas assez ambitieux)

**Exemple OKR DSI :**
- O : "Garantir la résilience du SI"
- KR1 : MTTR < 30 min pour les incidents P1
- KR2 : Taux de disponibilité > 99,95 %
- KR3 : 0 incident de sécurité critique non détecté en < 4h

#### La loi de Goodhart

> "Lorsqu'une mesure devient une cible, elle cesse d'être une bonne mesure."
> — Charles Goodhart (économiste, 1975)

Exemples de dérive :
- Un développeur optimise son KPI "nombre de commits" en faisant des micro-commits inutiles
- Un centre d'appels réduit son KPI "durée d'appel" en raccrochant plutôt qu'en résolvant

**Remède** : diversifier les indicateurs, mesurer les résultats (outcomes) plutôt que les activités (outputs).

#### Vanity Metrics vs Actionable Metrics

| Vanity Metric | Actionable Metric |
|---|---|
| Nombre de visiteurs du site | Taux de conversion visiteur → client |
| Nombre de tickets créés | Taux de résolution au premier contact |
| Nombre de déploiements | Taux de succès des déploiements |
| Nombre d'utilisateurs inscrits | Taux d'utilisateurs actifs à 30 jours |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Alignement stratégie-opérations | Risque de gaming (loi de Goodhart) |
| Objectivation des décisions | Coût de collecte et maintenance des données |
| Détection précoce des dérives | Illusion de précision (fausse confiance) |
| Communication simplifiée vers le management | Indicateurs mal choisis = comportements contre-productifs |
| Moteur de motivation avec les OKR | Complexité de déploiement des OKR dans les grandes structures |

### Acteurs

- **Cadres** : OKR (Andy Grove / Google), BSC (Kaplan & Norton), MBO (Peter Drucker)
- **Outils** : Tableau, Power BI, Looker, Datadog, Dynatrace, Jira Align
- **OKR Platforms** : Betterworks, Lattice, Perdoo, Weekdone
- **Référentiels** : COBIT 2019, ITIL 4 (SLA/OLA), ISO 9001

### Cas d'usage

- **DSI** : tableau de bord de disponibilité, MTTR, NPS IT, coût par utilisateur
- **Scrum** : vélocité de sprint, taux de story points livrés vs estimés
- **Cybersécurité** : KRI sur les vulnérabilités, temps de patching
- **Cloud** : FinOps KPIs (coût par feature, unit economics)
- **RH IT** : taux de turnover, satisfaction des développeurs (Developer Experience)

### Chiffres complémentaires

- Google utilise les OKR depuis **1999** (introduits par John Doerr, investisseur de Kleiner Perkins)
- Un tableau de bord efficace ne doit pas dépasser **5 à 7 KPI** par niveau de management
- Le NPS (Net Promoter Score) est calculé comme : **% Promoteurs − % Détracteurs** (échelle 0-10)

---

## Flashcards
#flashcards/Optimisation_du_SI/KPI_et_pilotage_de_la_performance #flashcards/Management_et_stratégie/KPI_et_pilotage_de_la_performance

Quelle est la différence entre un KPI et un KRI ? :: Le KPI mesure l'atteinte d'un objectif (performance), le KRI mesure l'exposition à un risque. L'un est orienté résultat, l'autre est orienté prévention.

Qu'est-ce que la loi de Goodhart et pourquoi est-elle critique ? :: "Quand une mesure devient une cible, elle cesse d'être une bonne mesure." Elle explique les comportements de gaming des métriques : les individus optimisent l'indicateur plutôt que l'objectif réel.

Quels sont les 4 axes du Balanced Scorecard ? :: Financier, Client, Processus internes, Apprentissage et croissance.

Quelle est la structure d'un OKR ? :: Un Objective qualitatif et ambitieux, accompagné de 3 à 5 Key Results quantifiables et vérifiables. Le score cible est 0,6-0,7 (pas 1,0).

Qu'est-ce qu'une vanity metric ? Donnez un exemple. :: Un indicateur flatteur qui ne reflète pas la réalité de la performance business. Ex : nombre de visiteurs sans taux de conversion, nombre de déploiements sans taux de succès.

Quelle est la différence entre un leading et un lagging indicator ? :: Le leading indicator prédit la performance future (ex : nombre de tests écrits) ; le lagging indicator constate la performance passée (ex : nombre de bugs en production).

Pourquoi un tableau de bord ne doit-il pas dépasser 5 à 7 KPI par niveau ? :: Au-delà, l'attention se dilue, les indicateurs perdent leur pouvoir d'action, et la prise de décision devient paralysée par l'excès d'information (infobésité décisionnelle).

---

## Sources

- Kaplan & Norton — "The Balanced Scorecard" (Harvard Business Review, 1992)
- John Doerr — "Measure What Matters" (2018)
- Forrester — "Insights-Driven Businesses" (2023)
- McKinsey — "Analytics and data-driven organizations" (2022)
- Goodhart, C. — "Monetary relationships: A view from Threadneedle Street" (1975)

---

## Notions liées

[[Métriques de pilotage projet]] · [[Frameworks de gestion de projet]] · [[SLA - SLO - SLI]] · [[MTTR - MTBF]] · [[DORA Metrics]] · [[Observabilité]] · [[Business Intelligence (BI)]] · [[Gouvernance IT]] · [[Système d'Information (SI)]]
