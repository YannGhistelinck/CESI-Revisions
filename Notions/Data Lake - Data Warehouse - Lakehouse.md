---
type: notion
thèmes:
  - Big DATA
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Data Lake - Data Warehouse - Lakehouse

![[N — Data Lake - Data Warehouse - Lakehouse.mp3]]
## En bref
> **Définition** : Un Data Warehouse est un entrepôt de données structurées optimisé pour l'analyse décisionnelle (schema-on-write) ; un Data Lake est un référentiel de données brutes dans leur format natif, structurées ou non (schema-on-read) ; un Data Lakehouse combine les deux approches pour offrir à la fois la flexibilité du lac et les performances analytiques de l'entrepôt.
> **Pourquoi c'est important** : Le choix de l'architecture de stockage analytique conditionne la capacité d'une DSI à exploiter ses données à grande échelle, à maîtriser les coûts et à répondre aux besoins des équipes Data, BI et IA.
> **Chiffres clés** :
> - Le marché mondial du Data Warehouse cloud devrait atteindre **51 milliards de dollars d'ici 2028** (MarketsandMarkets, 2023).
> - Snowflake, leader du Data Warehouse cloud, affiche une croissance annuelle de **40 %** de son revenu (FY2024).
> - Les entreprises utilisant un Data Lakehouse réduisent leur coût total de possession (TCO) analytique de **30 à 40 %** par rapport aux architectures dupliquées Lac + Entrepôt (Databricks, 2023).

## Approfondir

### Fonctionnement

#### Data Warehouse (Entrepôt de données)

Concept né dans les années 1990 (Bill Inmon, Ralph Kimball), le Data Warehouse est une base de données analytique centralisée, conçue pour le reporting et la Business Intelligence.

**Caractéristiques principales :**
- **Schema-on-write** : le schéma de données est défini avant l'ingestion (modélisation en étoile ou en flocon).
- Données **propres, transformées et intégrées** via des processus ETL.
- Optimisé pour les requêtes analytiques complexes (agrégations, jointures).
- Sources hétérogènes consolidées dans un référentiel unique.
- **OLAP** (Online Analytical Processing) vs OLTP (transactionnel).

**Modèles de modélisation :**
- **Schéma en étoile** (star schema) : une table de faits centrale entourée de tables de dimensions.
- **Schéma en flocon** (snowflake schema) : normalisation des dimensions.
- **Data Mart** : sous-ensemble thématique du Data Warehouse (ex. : Data Mart Finance).

**Limites :** coûteux à l'échelle, difficile à adapter aux données non structurées, cycle de transformation long.

#### Data Lake (Lac de données)

Popularisé par James Dixon (Pentaho) en 2010, le Data Lake stocke les données brutes dans leur format natif sans transformation préalable.

**Caractéristiques principales :**
- **Schema-on-read** : le schéma est appliqué au moment de la lecture, selon le besoin.
- Accepte tout type de données : structurées, semi-structurées, non structurées.
- Stockage bas coût (systèmes de fichiers distribués : HDFS, Amazon S3, Azure Data Lake Storage).
- Idéal pour le machine learning et l'exploration de données.
- Accès par des data scientists, ingénieurs data, analystes.

**Risque majeur — le "Data Swamp" (marécage de données) :** sans gouvernance rigoureuse (catalogage, métadonnées, qualité), le Data Lake devient un dépôt opaque où les données sont introuvables et inutilisables.

**Technologies associées :** Apache Hadoop/HDFS, Amazon S3, Azure ADLS Gen2, Google Cloud Storage, Delta Lake, Apache Iceberg, Apache Hudi.

#### Data Lakehouse

Architecture hybride émergente (popularisée par Databricks à partir de 2020) qui combine :
- Le **stockage économique et flexible** du Data Lake (format ouvert, objet cloud).
- Les **fonctionnalités analytiques** du Data Warehouse (transactions ACID, contrôle de schéma, indexation, optimisation des requêtes).

**Technologies clés :**
- **Delta Lake** (Databricks) : couche transactionnelle ACID sur un Data Lake, gestion des versions (time travel).
- **Apache Iceberg** (Netflix, Apple) : format de table ouvert pour les grands ensembles analytiques.
- **Apache Hudi** (Uber) : gestion des mises à jour et suppressions en streaming.

**Avantages du Lakehouse :**
- Supprime la duplication données Lac → Entrepôt.
- Support du SQL analytique et du machine learning sur les mêmes données.
- Formats ouverts (Parquet, ORC) : pas de vendor lock-in.
- Gestion du streaming et du batch sur la même plateforme.

#### Comparatif synthétique

| Critère | Data Warehouse | Data Lake | Data Lakehouse |
|---------|---------------|-----------|----------------|
| Type de données | Structurées uniquement | Tous types | Tous types |
| Schéma | Schema-on-write | Schema-on-read | Hybride |
| Qualité des données | Haute (ETL en amont) | Variable | Haute (gouvernance intégrée) |
| Coût de stockage | Élevé | Faible | Faible |
| Performances analytiques | Très élevées | Moyennes | Élevées |
| Usage ML/IA | Limité | Natif | Natif |
| Maturité | Très mature | Mature | Émergent |
| Exemples | Snowflake, Redshift, BigQuery | S3 + Hadoop, ADLS | Databricks, Delta Lake |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Data Warehouse : performances SQL optimales | Data Warehouse : coût élevé, rigidité schématique |
| Data Lake : flexibilité et bas coût de stockage | Data Lake : risque de Data Swamp sans gouvernance |
| Data Lake : support natif ML/IA | Data Lake : performances analytiques inférieures |
| Lakehouse : unification des usages (BI + ML) | Lakehouse : écosystème encore en maturation |
| Lakehouse : formats ouverts, évite le lock-in | Lakehouse : complexité opérationnelle |
| Architecture mutualisée, réduction TCO | Nécessite des compétences data engineering avancées |

### Acteurs et solutions du marché

- **Data Warehouse cloud** : Snowflake, Google BigQuery, Amazon Redshift, Azure Synapse Analytics, Teradata Vantage.
- **Data Lake** : Amazon S3 (+ AWS Glue), Azure Data Lake Storage Gen2, Google Cloud Storage, Cloudera Data Platform.
- **Lakehouse** : Databricks (Delta Lake), Apache Iceberg (catalysé par Apple/Netflix), Apache Hudi (Uber), Starburst (Trino).
- **Gouvernance / Data Catalog** : Apache Atlas, Collibra, Alation, DataHub, AWS Glue Data Catalog.

### Cas d'usage concrets

1. **Airbnb — Migration vers un Data Lakehouse** : Airbnb a migré son architecture de Hadoop/Hive vers Apache Iceberg pour gérer ses pétaoctets de données de logs et de transactions. Résultat : réduction de 50 % des temps de requête et simplification de la gestion des mises à jour.

2. **Netflix — Apache Iceberg** : Netflix, co-créateur d'Apache Iceberg, gère des exaoctets de données de comportement utilisateur. Le format Iceberg permet des opérations ACID à grande échelle et le time travel pour le débogage des pipelines.

3. **Banque — Data Warehouse réglementaire** : Les grandes banques (BNP Paribas, Société Générale) maintiennent des Data Warehouses structurés pour les reportings BCBS 239, IFRS 9 et Bâle III, où la précision, la traçabilité et la qualité des données sont non négociables.

### Chiffres et tendances

- **62 % des entreprises** ont adopté ou planifient un Data Lake dans les 2 ans (Gartner, 2023).
- **Delta Lake** dépasse **10 000 organisations utilisatrices** dans le monde (Databricks, 2023).
- Le coût moyen de stockage dans un Data Lake (S3) est **23 fois inférieur** à celui d'un entrepôt traditionnel on-premise (AWS, 2023).
- Tendance forte : **Data Mesh** (approche décentralisée par domaine) comme évolution architecturale au-delà du Lakehouse.

## Flashcards
#flashcards/Big_DATA/Data_Lake_Data_Warehouse_Lakehouse #flashcards/Cloud_et_Virtualisation/Data_Lake_Data_Warehouse_Lakehouse

Quelle est la différence fondamentale entre schema-on-write et schema-on-read ? :: Schema-on-write (Data Warehouse) : le schéma est défini avant l'ingestion, les données sont transformées en amont. Schema-on-read (Data Lake) : le schéma est appliqué au moment de la lecture, les données brutes sont stockées telles quelles.

Qu'est-ce qu'un Data Swamp ? :: Un Data Lake mal gouverné, sans catalogage ni métadonnées, où les données deviennent introuvables et inutilisables. Risque majeur d'un lac sans gouvernance.

Quelles technologies permettent de créer un Data Lakehouse ? :: Delta Lake (Databricks), Apache Iceberg (Netflix/Apple), Apache Hudi (Uber). Elles ajoutent des transactions ACID et un contrôle de schéma sur le stockage objet.

Qu'est-ce qu'un star schema (schéma en étoile) ? :: Modèle de modélisation d'un Data Warehouse avec une table de faits centrale (métriques) entourée de tables de dimensions (contextes). Optimisé pour les requêtes analytiques OLAP.

Quelle est la promesse principale du Data Lakehouse ? :: Combiner la flexibilité et le faible coût de stockage du Data Lake avec les performances analytiques et la gouvernance du Data Warehouse, sur une seule architecture.

Citez 3 solutions de Data Warehouse cloud. :: Snowflake, Google BigQuery, Amazon Redshift (et Azure Synapse Analytics).

Qu'est-ce que le Data Mesh ? :: Approche architecturale décentralisée qui distribue la propriété des données par domaine métier, en opposition aux architectures centralisées Lac/Entrepôt. Chaque domaine gère ses propres pipelines et produits de données.

## Sources

- Databricks, *The Data Lakehouse Platform*, 2023.
- Gartner, *Magic Quadrant for Cloud Database Management Systems*, 2023.
- MarketsandMarkets, *Cloud Data Warehouse Market Report*, 2023.
- Armbrust, M. et al., *Lakehouse: A New Generation of Open Platforms*, CIDR 2021.
- Snowflake, *Annual Report FY2024*.
- AWS, *Big Data Analytics Options on AWS*, 2023.

## Notions liées

- [[Big Data — fondamentaux]]
- [[ETL - ELT et pipelines de données]]
- [[Écosystème Hadoop - Spark - Kafka]]
- [[Plateformes cloud Big Data]]
- [[Bases NoSQL]]
- [[Data Lifecycle Management]]
- [[Modèles de déploiement cloud]]
