---
type: notion
thèmes:
  - IA
  - Développement
  - Big DATA
statut: pas vu
dernière_révision: 
---

# MLOps - DataOps

## En bref

### Définition
Le **MLOps** (Machine Learning Operations) est l'ensemble des pratiques, outils et processus qui industrialisent le cycle de vie des modèles ML : du développement au déploiement, en passant par le monitoring et le ré-entraînement. Le **DataOps** est son équivalent pour les données : il applique les principes DevOps aux pipelines de données pour garantir qualité, disponibilité et fiabilité des données. Les deux sont interdépendants : sans DataOps, pas de MLOps robuste.

### Pourquoi c'est important
87 % des projets ML n'atteignent jamais la production (VentureBeat). Le MLOps résout cet échec en traitant les modèles comme du logiciel : versioning, CI/CD, tests, monitoring. Pour le MAALSI, c'est la discipline qui rend l'IA opérationnelle et maintenable en entreprise.

### Chiffres clés
- **87 %** des projets ML n'atteignent jamais la production (VentureBeat, 2019 — toujours cité)
- Marché MLOps : **~4,5 Md$ en 2024** → **75 Md$ en 2033** (CAGR 43 %)
- Un modèle ML dérive en moyenne au bout de **3 à 6 mois** sans monitoring (data drift)
- Coût d'un incident de data drift non détecté : pertes business pouvant atteindre **millions d'euros**

---

## Approfondir

### Fonctionnement

#### Cycle de vie MLOps (ML Lifecycle)

```
1. DÉFINITION DU PROBLÈME
   ↓
2. COLLECTE & PRÉPARATION DES DONNÉES (DataOps)
   ↓
3. FEATURE ENGINEERING & EXPÉRIMENTATION
   ↓
4. ENTRAÎNEMENT DU MODÈLE
   ↓
5. ÉVALUATION & VALIDATION
   ↓
6. DÉPLOIEMENT (serving)
   ↓
7. MONITORING (performance, drift, biais)
   ↓
8. RÉ-ENTRAÎNEMENT (si dérive détectée) → retour à l'étape 2 ou 4
```

#### MLOps — Composants clés

| Composant | Rôle | Outils |
|---|---|---|
| **Versioning des données** | Traçabilité des datasets d'entraînement | DVC, Delta Lake, LakeFS |
| **Versioning des modèles** | Registre de modèles, gestion des versions | MLflow, W&B, SageMaker Registry |
| **Tracking d'expériences** | Comparaison des runs (hyperparamètres, métriques) | MLflow, Weights & Biases, Neptune |
| **Feature Store** | Stockage centralisé des features, réutilisable | Feast, Hopsworks, Tecton |
| **CI/CD ML** | Tests automatiques, intégration continue du modèle | Jenkins, GitLab CI, GitHub Actions |
| **Serving** | Exposition du modèle en API/endpoint | BentoML, TorchServe, Triton, FastAPI |
| **Monitoring** | Détection de dérive, qualité des prédictions | Evidently, WhyLabs, Grafana |

#### DataOps — Composants clés

| Composant | Rôle | Outils |
|---|---|---|
| **Ingestion** | Collecte des données (batch/streaming) | Kafka, Airbyte, Fivetran |
| **Transformation** | Nettoyage, enrichissement, agrégation | dbt, Spark, Flink |
| **Orchestration** | Scheduling des pipelines | Airflow, Prefect, Dagster |
| **Qualité des données** | Contrôle, validation, alertes | Great Expectations, Soda |
| **Catalogage** | Découverte et gouvernance des données | Datahub, Apache Atlas, Alation |
| **Stockage** | Data lake, data warehouse | S3/GCS, Snowflake, BigQuery, Databricks |

#### Types de dérive (Drift)

| Type de dérive | Description | Exemple |
|---|---|---|
| **Data drift** | Distribution des données d'entrée change | Les revenus des clients augmentent → le modèle de scoring est désalibré |
| **Concept drift** | La relation entre features et target change | Comportement d'achat post-COVID vs pré-COVID |
| **Model drift** | Dégradation progressive des performances | F1-score du modèle de fraude descend de 95 % à 80 % |
| **Infrastructure drift** | Changement d'environnement d'exécution | Mise à jour Python, changement de lib |

#### Déploiement — Stratégies

| Stratégie | Description | Avantage |
|---|---|---|
| **Blue/Green** | Deux environnements, bascule instantanée | Rollback immédiat |
| **Canary** | 5-10 % du trafic vers le nouveau modèle | Test en production contrôlé |
| **Shadow** | Nouveau modèle en parallèle, résultats non utilisés | Test sans risque |
| **A/B Testing** | Comparaison de deux modèles sur populations distinctes | Mesure d'impact business |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Industrialisation et reproductibilité des modèles | Investissement initial en outillage et formation |
| Détection précoce de la dérive des modèles | Courbe d'apprentissage élevée (DataOps + MLOps) |
| Réduction du time-to-market des modèles IA | Complexité organisationnelle (Data Scientists + Ops) |
| Traçabilité et auditabilité (RGPD, AI Act) | Risque de sur-ingénierie pour les petits projets |
| Collaboration Data Science / Engineering / Ops | Gestion de la dette technique des pipelines |
| Scalabilité du serving de modèles | Coût des outils (plateformes MLOps cloud) |

### Acteurs
- **Plateformes MLOps complètes** : MLflow (open-source), Kubeflow, AWS SageMaker, Azure ML, Google Vertex AI, Weights & Biases, DataRobot
- **DataOps** : dbt Labs, Apache Airflow, Databricks, Snowflake, Prefect, Great Expectations
- **Feature Stores** : Feast (open-source), Hopsworks, Tecton, SageMaker Feature Store
- **Serving** : BentoML, NVIDIA Triton, TorchServe, Seldon

### Cas d'usage
- **Banque/Assurance** : modèle de scoring crédit → monitoring du taux d'acceptation + drift mensuel
- **E-commerce** : modèle de recommandation → ré-entraînement hebdomadaire sur nouveaux comportements
- **Industrie** : modèle de maintenance prédictive → pipeline DataOps sur données capteurs IoT
- **Santé** : modèle de diagnostic → auditabilité complète requise (régulation)

### Chiffres complémentaires
- 60 % du temps d'un Data Scientist est consacré à la préparation des données (IBM, 2023)
- MLflow : plus de **17 000 stars GitHub**, standard de facto pour le tracking
- Un Feature Store réduit de **50-80 %** le temps de feature engineering entre projets

---

## Flashcards
#flashcards

Qu'est-ce que le MLOps et pourquoi est-il nécessaire ? :: Le MLOps applique les pratiques DevOps au cycle de vie des modèles ML (développement, déploiement, monitoring, ré-entraînement) pour industrialiser l'IA. Il est nécessaire car 87 % des projets ML n'atteignent pas la production sans ces pratiques.

Qu'est-ce que le data drift et comment le détecter ? :: Le data drift est le changement de distribution des données d'entrée du modèle au fil du temps, rendant ses prédictions moins fiables. Détection : monitoring statistique (KL divergence, PSI, tests de Kolmogorov-Smirnov) avec des outils comme Evidently ou WhyLabs.

Quelle est la différence entre MLOps et DataOps ? :: DataOps concerne les pipelines de données (ingestion, qualité, gouvernance). MLOps concerne le cycle de vie des modèles ML (entraînement, versioning, déploiement, monitoring). Les deux sont complémentaires : le DataOps fournit les données fiables dont le MLOps a besoin.

Qu'est-ce qu'un Feature Store ? :: Base de données centralisée qui stocke, gère et sert les features (variables) utilisées pour l'entraînement et l'inférence des modèles ML. Permet la réutilisabilité des features entre projets et garantit la cohérence entre entraînement et production.

Décrivez la stratégie de déploiement Canary. :: Le déploiement Canary dirige un faible pourcentage du trafic réel (ex : 5 %) vers le nouveau modèle, pendant que le reste utilise l'ancien. Si les métriques sont satisfaisantes, le trafic est progressivement basculé, permettant de tester en production sans risque massif.

Qu'est-ce que le tracking d'expériences MLOps ? :: Enregistrement systématique de chaque run d'entraînement : hyperparamètres, métriques (F1, AUC…), artefacts (modèle, graphiques), code utilisé. Permet de comparer les runs, reproduire les résultats et choisir le meilleur modèle. Outil standard : MLflow.

Citez 3 types de dérive (drift) en MLOps. :: Data drift (distribution des inputs change), concept drift (relation features/target change), model drift (performances globales se dégradent), infrastructure drift (environnement d'exécution change).

---

## Sources
- VentureBeat — *Why 87% of data science projects never make it into production* (2019)
- Google — *MLOps: Continuous delivery and automation pipelines in machine learning* (2021)
- MLflow Documentation — mlflow.org
- Databricks — The Big Book of MLOps, 2023
- Gartner — Magic Quadrant for Data Science and Machine Learning Platforms, 2024

---

## Notions liées
- [[Intelligence Artificielle — fondamentaux]]
- [[IA générative et LLM]]
- [[RAG (Retrieval-Augmented Generation)]]
- [[Fine-tuning et prompt engineering]]
- [[AIOps]]
