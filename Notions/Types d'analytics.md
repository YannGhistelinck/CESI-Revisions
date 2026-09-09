---
type: notion
thèmes:
  - Big DATA
  - IA
statut: pas vu
dernière_révision: 
---

# Types d'analytics

## En bref
> **Définition** : L'analytics désigne l'analyse systématique des données pour produire des insights et éclairer les décisions. On distingue quatre types progressifs : l'analytics **descriptive** (que s'est-il passé ?), **diagnostique** (pourquoi ?), **prédictive** (que va-t-il se passer ?) et **prescriptive** (que doit-on faire ?). Ensemble, ils constituent le socle du **data-driven decision making** — la prise de décision basée sur les données.
> **Pourquoi c'est important** : La valeur créée par l'analytics croît exponentiellement avec le niveau de sophistication. Mais chaque niveau requiert des prérequis en données, en compétences et en maturité organisationnelle. Comprendre ces quatre niveaux permet de situer la maturité analytique d'une organisation et d'identifier les investissements prioritaires.
> **Chiffres clés** :
> - **80 % des organisations** utilisent l'analytics descriptive, contre seulement **35 %** l'analytics prédictive et **17 %** le prescriptif (Gartner)
> - Le marché de l'analytics prédictif atteindra **41,5 Md$** en 2028, croissance de **+23 % par an** (MarketsandMarkets)
> - Les entreprises adoptant le data-driven decision making sont **19 fois plus rentables** que celles qui ne le font pas (McKinsey)

## Approfondir

### Fonctionnement

#### La hiérarchie des 4 types d'analytics

```
                        ↑ Valeur ajoutée
Prescriptive  ─────────────────────────────  "Que doit-on faire ?"
              Optimisation, simulation, IA   → Complexité maximale
              
Prédictive    ─────────────────────────────  "Que va-t-il se passer ?"
              Machine learning, scoring,     → Nécessite des modèles ML
              prévisions
              
Diagnostique  ─────────────────────────────  "Pourquoi cela s'est-il passé ?"
              Drill-down, root cause,        → Nécessite données riches
              corrélation
              
Descriptive   ─────────────────────────────  "Que s'est-il passé ?"
              Rapports, dashboards, KPIs     → Point d'entrée universel
                        ↓ Accessibilité
```

#### 1. Analytics Descriptive
**Question** : Que s'est-il passé ?

**Méthodes et outils** :
- Tableaux de bord (KPIs, métriques)
- Rapports récurrents (hebdomadaires, mensuels)
- Agrégations simples : SUM, AVG, COUNT, GROUP BY
- Visualisations : bar charts, line charts, pie charts

**Exemples concrets** :
- "Notre CA du mois de mars est de 2,3 M€, en hausse de 8 % vs mars N-1"
- "Le taux de disponibilité de notre système est de 99,7 % ce trimestre"
- "Les retours produit représentent 2,1 % des ventes"

**Outils** : Power BI, Tableau, Looker, Google Analytics, Excel

**Limite** : décrit le passé mais n'explique pas les causes ni ne prédit l'avenir.

#### 2. Analytics Diagnostique
**Question** : Pourquoi cela s'est-il passé ?

**Méthodes et outils** :
- **Drill-down** : décomposition d'une métrique agrégée en ses composantes (ex. : CA global → CA par région → CA par produit → CA par canal)
- **Root cause analysis** : analyse des causes racines d'une anomalie
- **Corrélation** : identification de variables liées statistiquement
- **Analyse de cohortes** : comportement de groupes d'utilisateurs dans le temps
- **A/B Testing** : comparaison d'une variable entre deux groupes

**Exemples concrets** :
- "Le CA a baissé en mars car les ventes de la catégorie Électronique ont chuté de 23 % suite à une rupture de stock fournisseur"
- "Le taux de churn a augmenté chez les clients ayant attendu plus de 48h pour leur première livraison"

**Outils** : Power BI (drill-through), Tableau, Python (pandas, scipy), SQL avancé

**Limite** : identifie les corrélations mais ne garantit pas la causalité (attention : corrélation ≠ causalité).

#### 3. Analytics Prédictive
**Question** : Que va-t-il se passer ?

**Méthodes et outils** :
- **Machine Learning supervisé** : régression (valeur numérique), classification (catégorie), arbres de décision, forêts aléatoires, gradient boosting (XGBoost, LightGBM)
- **Séries temporelles** : ARIMA, Prophet (Facebook/Meta), LSTM
- **Scoring** : probabilité qu'un événement se produise (churn score, credit score)
- **Feature engineering** : construction des variables explicatives

**Exemples concrets** :
- Prévision de la demande (retail, e-commerce) : anticiper les stocks nécessaires par produit/région
- Score de crédit : probabilité qu'un client ne rembourse pas son prêt (LCL, BNP)
- Prédiction du churn : identifier les clients susceptibles de partir dans les 30 prochains jours
- Maintenance prédictive : anticiper la panne d'une machine industrielle

**Outils** : Python (scikit-learn, TensorFlow, PyTorch), R, Dataiku, Azure ML, AWS SageMaker, Google Vertex AI

**Limite** : "garbage in, garbage out" — la qualité des prédictions dépend entièrement de la qualité et de la représentativité des données d'entraînement.

#### 4. Analytics Prescriptive
**Question** : Que doit-on faire ?

**Méthodes et outils** :
- **Optimisation mathématique** : programmation linéaire, algorithmes génétiques (ex. : optimisation des tournées de livraison)
- **Simulation Monte Carlo** : modélisation de scénarios probabilistes
- **Reinforcement Learning** : apprentissage par renforcement (l'algorithme apprend à maximiser une récompense)
- **Decision Intelligence** : combinaison de l'analytics prédictif avec des règles métier pour automatiser les décisions

**Exemples concrets** :
- **Yield management** : prix dynamiques en temps réel (compagnies aériennes, hôtels, Uber)
- **Optimisation logistique** : Amazon optimise chaque tournée de livraison en temps réel (economics du "dernier kilomètre")
- **Trading algorithmique** : exécution automatique d'ordres boursiers en fonction de signaux de marché
- **Allocation budgétaire** : optimisation de la répartition du budget marketing entre canaux

**Outils** : Python (SciPy Optimize, OR-Tools de Google), IBM CPLEX, Gurobi, AWS Personalize

**Limite** : Très complexe à implémenter correctement. Les décisions entièrement automatisées soulèvent des questions éthiques (explicabilité, responsabilité).

#### Data-Driven Decision Making (DDDM)
Approche de management consistant à fonder toutes les décisions stratégiques et opérationnelles sur l'analyse des données plutôt que sur l'intuition ou l'expérience seule.

**Principes** :
1. Définir les questions avant de collecter les données (éviter le "data fishing")
2. Garantir la qualité des données (gouvernance)
3. Combiner analytics quantitatif et expertise métier qualitative
4. Tester et mesurer (culture A/B testing, expérimentation)
5. Accepter que les données remettent en question les intuitions

**Limites et biais** :
- **Biais de confirmation** : chercher les données qui confirment une idée préconçue
- **Goodhart's Law** : "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure" (ex. : optimiser le NPS en récompensant les promoteurs plutôt qu'en améliorant le service)
- **Données historiques limitées** : les données du passé ne capturent pas les ruptures (COVID, chocs géopolitiques)

### Avantages / Inconvénients

| Type | Valeur ajoutée | Complexité / Coût |
|------|---------------|-------------------|
| Descriptive | Visibilité sur le passé | Faible — accessible à tous |
| Diagnostique | Compréhension des causes | Moyen — nécessite des données riches |
| Prédictive | Anticipation, avantage compétitif | Élevé — data scientists, ML ops |
| Prescriptive | Automatisation des décisions, optimisation | Très élevé — mathématiques avancées, IA |

### Acteurs et solutions du marché
- **SAS** : historiquement leader de l'analytics prédictif en entreprise (secteur bancaire/assurance)
- **Dataiku** : plateforme end-to-end couvrant les 4 types d'analytics, très présente en France
- **DataRobot** : AutoML, automatise la création de modèles prédictifs
- **AWS SageMaker / Azure ML / Google Vertex AI** : plateformes cloud ML
- **Google OR-Tools** : bibliothèque open source d'optimisation (prescriptif)
- **Palantir** : analytics avancé pour la défense, le renseignement et les grandes entreprises

### Cas d'usage concrets
1. **Renault** utilise les 4 niveaux : descriptif (tableau de bord qualité usine), diagnostique (analyse des causes de défauts), prédictif (prévision de la demande par modèle et pays), prescriptif (optimisation de l'affectation des capacités de production entre usines).
2. **Crédit Agricole** a déployé un modèle prédictif de churn détectant les clients risquant de clôturer leur compte 3 mois à l'avance avec 78 % de précision, permettant des actions de rétention ciblées et une économie estimée à 45 M€/an.
3. **DHL** utilise l'analytics prescriptif pour optimiser en temps réel ses 30 000 tournées de livraison quotidiennes en Europe, réduisant le kilométrage parcouru de 15 % et les émissions CO₂ associées.

### Chiffres et tendances
- **L'analytics prédictif** est le principal use case qui justifie les investissements Big Data selon **61 % des CDO** (NewVantage Partners, 2023)
- Le **reinforcement learning** (analytics prescriptif) a multiplié par 10 les performances du trading algorithmique chez les hedge funds quantitatifs (Renaissance, Two Sigma)
- **70 % des projets d'analytics prédictif** ne passent jamais en production (Gartner) — problème de MLOps et de gouvernance des modèles
- L'essor des **LLM** (ChatGPT, Claude) redéfinit l'analytics descriptive et diagnostique : on peut désormais interroger ses données en langage naturel

## Flashcards
#flashcards

Quels sont les 4 types d'analytics et les questions auxquelles ils répondent ? :: Descriptive ("Que s'est-il passé ?"), Diagnostique ("Pourquoi ?"), Prédictive ("Que va-t-il se passer ?"), Prescriptive ("Que doit-on faire ?"). Chaque niveau apporte plus de valeur mais nécessite plus de complexité et de maturité data.

Quelle est la différence entre corrélation et causalité en analytics diagnostique ? :: La corrélation indique que deux variables évoluent de concert (ex. : ventes de glaces et noyades augmentent en été). La causalité établit qu'une variable en provoque une autre. En analytics diagnostique, on identifie des corrélations, mais la causalité nécessite des expérimentations contrôlées (A/B test, études randomisées).

Quels algorithmes sont typiquement utilisés en analytics prédictive ? :: Machine learning supervisé : régression (valeur continue), classification (catégorie), forêts aléatoires, gradient boosting (XGBoost, LightGBM). Pour les séries temporelles : ARIMA, Prophet. Pour les textes : NLP. Le choix dépend du type de variable à prédire et du volume de données.

Qu'est-ce que la maintenance prédictive et en quoi relève-t-elle de l'analytics prédictive ? :: Utilisation de données de capteurs (IoT) pour anticiper les pannes d'équipements industriels avant qu'elles surviennent. Les modèles ML apprennent les signatures de défaillance dans les données historiques. Relève de l'analytics prédictive car on prédit un événement futur (la panne) à partir de données présentes.

Qu'est-ce que le yield management et à quel type d'analytics appartient-il ? :: Optimisation dynamique des prix en temps réel en fonction de la demande, des stocks disponibles et du profil des acheteurs. Exemple : prix des billets d'avion qui varient selon le moment d'achat et le taux de remplissage. Relève de l'analytics prescriptive (décision automatique d'optimisation).

Qu'est-ce que la loi de Goodhart et pourquoi est-elle un risque pour le DDDM ? :: "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure." Risque : optimiser un KPI au détriment de l'objectif réel (ex. : augmenter le NPS en distribuant des récompenses aux promoteurs plutôt qu'en améliorant le service). Le data-driven decision making nécessite de choisir des métriques robustes et de les réviser régulièrement.

Pourquoi 70 % des projets d'analytics prédictif ne passent jamais en production ? :: Problèmes de MLOps (déploiement, monitoring, réentraînement des modèles), manque de gouvernance des modèles (qui est responsable si le modèle se trompe ?), données de production différentes des données d'entraînement (data drift), et déficit de confiance des équipes métier envers les modèles "boîte noire".

## Sources
- Gartner – "Augmented Analytics Is the Future of Data and Analytics" : https://www.gartner.com
- McKinsey – "The age of analytics: competing in a data-driven world" : https://www.mckinsey.com
- MarketsandMarkets – "Predictive Analytics Market" : https://www.marketsandmarkets.com
- Dataiku – "Introduction to Predictive Analytics" : https://www.dataiku.com
- SAS – "Analytics Overview" : https://www.sas.com/analytics
- NewVantage Partners – "Big Data and AI Executive Survey 2023" : https://www.newvantage.com

## Notions liées
- [[Business Intelligence (BI)]]
- [[Data Maturity et Data Literacy]]
- [[Data Governance]]
- [[IA en cybersécurité]]
- [[Monétisation des données]]
