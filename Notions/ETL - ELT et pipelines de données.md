---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# ETL - ELT et pipelines de données

![[N — ETL - ELT et pipelines de données.mp3]]
## En bref
> **Définition** : L'ETL (Extract, Transform, Load) est un processus qui extrait des données de sources hétérogènes, les transforme selon des règles métier, puis les charge dans une destination analytique. L'ELT (Extract, Load, Transform) inverse l'ordre : les données brutes sont d'abord chargées, puis transformées à la demande en exploitant la puissance du système cible. Un pipeline de données est l'ensemble des étapes automatisées qui déplacent et transforment la donnée de la source à la destination.
> **Pourquoi c'est important** : Les pipelines de données sont l'artère centrale de tout système analytique. Sans eux, les données restent silotées et inexploitables. Pour une DSI, leur fiabilité, leur performance et leur observabilité conditionnent directement la qualité des décisions business.
> **Chiffres clés** :
> - Les data engineers consacrent en moyenne **40 % de leur temps** à la maintenance des pipelines de données (Stitch Data, 2023).
> - Le marché de l'intégration de données (ETL/ELT, iPaaS) devrait atteindre **28 milliards de dollars d'ici 2027** (MarketsandMarkets, 2023).
> - dbt (data build tool) est utilisé par plus de **30 000 entreprises** dans le monde en 2024.

## Approfondir

### Fonctionnement

#### ETL — Extract, Transform, Load

Processus historique, né avec les premiers Data Warehouses dans les années 1990.

**Étape 1 — Extract (Extraction)**
- Collecte des données depuis des sources hétérogènes : bases relationnelles (Oracle, SQL Server), fichiers plats (CSV, XML), APIs REST/SOAP, ERP (SAP), CRM (Salesforce).
- Extraction complète (full load) ou incrémentale (delta load, CDC — Change Data Capture).
- Techniques CDC : triggers SQL, lecture des journaux de transactions (WAL PostgreSQL, binlog MySQL), timestamps.

**Étape 2 — Transform (Transformation)**
- Réalisée dans un moteur de transformation dédié (staging area), avant le chargement.
- Opérations : nettoyage (suppression des doublons, gestion des valeurs nulles), normalisation des formats (dates, devises), agrégations, jointures, application des règles métier, encodage.
- Qualité de la donnée : contrôles de conformité, profiling.

**Étape 3 — Load (Chargement)**
- Insertion dans la destination : Data Warehouse, Data Mart.
- Chargement complet ou incrémental.
- Gestion des clés, des contraintes d'intégrité référentielle.

**Limites de l'ETL :**
- Transformations rigides, coûteuses à modifier.
- Perte d'information si les transformations ne sont pas prévues a priori.
- Peu adapté aux données non structurées et au temps réel.

#### ELT — Extract, Load, Transform

Approche moderne adaptée aux entrepôts cloud et aux Data Lakes. La transformation est déportée dans le système cible (BigQuery, Snowflake, Redshift) qui dispose d'une puissance de calcul élastique.

**Avantages :**
- Les données brutes sont conservées → possibilité de transformer différemment selon les besoins.
- Exploite la puissance de calcul massivement parallèle des plateformes cloud.
- Time-to-insight réduit : les données sont disponibles immédiatement après le chargement.
- Facilite l'exploration data science et le machine learning sur les données brutes.

**Inconvénients :**
- Stocke des données potentiellement sensibles non nettoyées.
- Complexité de gouvernance accrue.
- Dépendance au système cible pour les transformations (coûts de compute).

#### dbt — data build tool

dbt est devenu le standard de facto pour la couche de transformation dans les architectures ELT modernes.

- Permet d'écrire des transformations en **SQL pur** avec des fonctionnalités de génie logiciel : versionning, tests, documentation, modularité.
- Fonctionne en "transform in place" dans le Data Warehouse (BigQuery, Snowflake, Redshift, DuckDB...).
- Deux versions : **dbt Core** (open-source) et **dbt Cloud** (SaaS avec orchestration, CI/CD intégrée).
- Concepts clés : modèles (models), tests (not_null, unique, relationships), seeds, snapshots (SCD Type 2), macros Jinja.

#### Pipelines de données

Un pipeline de données est une séquence d'étapes automatisées et orchestrées qui déplacent, transforment et enrichissent les données.

**Types de pipelines :**

| Type | Description | Outils |
|------|-------------|--------|
| **Batch** | Traitement périodique de volumes de données accumulés (nuit, heure). | Airflow, dbt, Spark |
| **Streaming (temps réel)** | Traitement des données événement par événement dès leur arrivée. | Apache Kafka, Flink, Spark Streaming, Kinesis |
| **Micro-batch** | Compromis : petits lots traités très fréquemment (toutes les secondes). | Spark Structured Streaming |
| **Lambda** | Architecture hybride combinant une couche batch (haute précision) et une couche streaming (faible latence). | Hadoop + Kafka |
| **Kappa** | Architecture unifiée streaming uniquement, simplifie Lambda. | Apache Kafka + Flink |

**Orchestration des pipelines :**
- **Apache Airflow** : standard open-source, DAG (Directed Acyclic Graph) en Python, scheduling, monitoring, retry.
- **Prefect / Dagster** : alternatives modernes à Airflow, orientées data engineering.
- **AWS Step Functions, Azure Data Factory, Google Cloud Composer** : solutions cloud natives.

**Observabilité des pipelines :**
- Monitoring des SLA (Service Level Agreement sur les délais de livraison).
- Alertes sur les anomalies de volume, de schéma (schema drift), de qualité.
- Outils : Monte Carlo, Great Expectations, Soda, dbt tests.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| ETL : données propres avant chargement, sécurité | ETL : rigidité, coût de re-transformation si règles changent |
| ELT : flexibilité, conservation des données brutes | ELT : coûts de compute dans le data warehouse |
| ELT : rapidité de mise à disposition | ELT : gouvernance plus complexe |
| Streaming : insights en temps réel | Streaming : complexité technique, coût d'infrastructure |
| Automatisation complète des flux de données | Fragilité des pipelines (cascading failures) |
| Traçabilité et reproductibilité (data lineage) | Nécessite des compétences data engineering élevées |

### Acteurs et solutions du marché

- **ETL/ELT clés en main** : Fivetran, Airbyte (open-source), Talend, Informatica, Stitch.
- **Transformation** : dbt (Core / Cloud), Spark, SQL natif cloud.
- **Orchestration** : Apache Airflow, Prefect, Dagster, Mage.ai.
- **Streaming** : Apache Kafka, Apache Flink, Amazon Kinesis, Google Pub/Sub, Confluent Platform.
- **Qualité / Observabilité** : Great Expectations, Monte Carlo, Soda Core, Anomalo.

### Cas d'usage concrets

1. **Retail — Mise à jour nocturne du Data Warehouse** : Une grande chaîne de distribution extrait chaque nuit les données de ventes de ses 500 points de vente (POS), les transforme (consolidation, gestion des retours, calcul des marges) via dbt sur Snowflake, et alimente les tableaux de bord Power BI disponibles à 7h du matin pour les directeurs régionaux.

2. **Finance — Détection de fraude en temps réel** : Une banque utilise un pipeline Kafka + Flink pour analyser en continu les transactions carte bancaire. Chaque transaction est enrichie (historique client, géolocalisation, scoring) et classifiée en moins de 50 ms, déclenchant un blocage automatique si le score de fraude dépasse un seuil.

3. **Uber — Architecture Kappa avec Kafka** : Uber traite des millions d'événements par seconde (positions GPS, demandes de courses, paiements) via Apache Kafka. Un pipeline Flink unifié gère à la fois le temps réel (matching conducteur/passager) et l'analytique différée (optimisation des prix dynamiques).

### Chiffres et tendances

- Apache Airflow est utilisé par plus de **14 millions de fois** d'exécutions de DAG par mois dans les entreprises Fortune 500.
- Fivetran déplace plus de **5 000 milliards d'enregistrements** par mois en 2024.
- **70 % des entreprises** prévoient d'adopter une architecture ELT d'ici 2025 (Gartner, 2023).
- Le CDC (Change Data Capture) devient le standard pour les pipelines temps réel, remplaçant les extractions batch complètes.

## Flashcards
#flashcards/Big_DATA/ETL_ELT_et_pipelines_de_données

Quelle est la différence entre ETL et ELT ? :: ETL : Extract → Transform (dans un moteur dédié) → Load dans la destination. ELT : Extract → Load (données brutes) → Transform directement dans le système cible. L'ELT exploite la puissance des Data Warehouses cloud.

Qu'est-ce que le CDC (Change Data Capture) ? :: Technique d'extraction incrémentale qui capture uniquement les modifications (insertions, mises à jour, suppressions) depuis la dernière extraction, en lisant les journaux de transaction de la base source.

À quoi sert dbt (data build tool) ? :: À écrire les transformations analytiques en SQL avec des pratiques de génie logiciel (tests, documentation, versioning). Il est le standard de la couche Transform dans les architectures ELT modernes.

Quelle est la différence entre une architecture Lambda et Kappa ? :: Lambda combine une couche batch (haute précision, latence élevée) et une couche streaming (faible latence, précision moindre). Kappa simplifie en utilisant uniquement le streaming pour tout traitement.

Qu'est-ce qu'un DAG dans le contexte de l'orchestration de pipelines ? :: Un Directed Acyclic Graph (graphe orienté acyclique) : représentation des dépendances entre les tâches d'un pipeline. Utilisé notamment par Apache Airflow pour orchestrer l'ordre d'exécution.

Qu'est-ce que le schema drift ? :: Modification inattendue du schéma d'une source de données (ajout/suppression de colonnes, changement de type) qui peut casser un pipeline de données. Doit être détecté et alerté par l'observabilité.

Citez 3 outils d'orchestration de pipelines de données. :: Apache Airflow, Prefect, Dagster (et aussi Azure Data Factory, AWS Step Functions, Google Cloud Composer).

## Sources

- Stitch Data, *The State of Data Engineering*, 2023.
- MarketsandMarkets, *Data Integration Market Report*, 2023.
- dbt Labs, *The State of Analytics Engineering*, 2024.
- Kreps, J., *Questioning the Lambda Architecture*, O'Reilly, 2014.
- Databricks, *Data + AI Summit — Pipeline Best Practices*, 2023.
- Gartner, *Data Management Hype Cycle*, 2023.

## Notions liées

- [[Big Data — fondamentaux]]
- [[Data Lake - Data Warehouse - Lakehouse]]
- [[Écosystème Hadoop - Spark - Kafka]]
- [[Plateformes cloud Big Data]]
- [[Data Lifecycle Management]]
