---
type: notion
thèmes:
  - Big DATA
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Plateformes cloud Big Data

## En bref
> **Définition** : Les plateformes cloud Big Data sont des ensembles de services managés proposés par les fournisseurs cloud (AWS, Google Cloud, Azure) et des éditeurs spécialisés (Snowflake, Databricks) pour ingérer, stocker, traiter, analyser et visualiser de grandes quantités de données sans avoir à gérer l'infrastructure sous-jacente.
> **Pourquoi c'est important** : Le passage aux plateformes cloud Big Data permet aux DSI d'éliminer les coûts d'infrastructure on-premise, de bénéficier d'une scalabilité élastique, d'accélérer le time-to-market des projets data et d'accéder à des services analytiques et IA managés à la pointe de l'état de l'art.
> **Chiffres clés** :
> - **92 % des entreprises** utilisent le multi-cloud pour leurs workloads data (Flexera, 2024).
> - Google BigQuery traite plus de **110 pétaoctets** de requêtes par jour (Google, 2024).
> - Snowflake dépasse **9 800 clients** dont 590 du Fortune 2000 (Snowflake FY2025).

## Approfondir

### Fonctionnement

#### AWS — Écosystème Big Data Amazon

AWS est le leader du cloud (34 % de parts de marché) et propose l'écosystème Big Data le plus complet.

**Stockage :**
- **Amazon S3 (Simple Storage Service)** : stockage objet de référence pour les Data Lakes. Durabilité 99,999999999 % (11 nines). Formats supportés : Parquet, ORC, JSON, CSV, Avro. Classes de stockage : Standard, Infrequent Access, Glacier (archivage).
- **S3 Select / S3 Object Lambda** : requêtes SQL directement sur les objets S3.

**Traitement et requêtage :**
- **Amazon EMR (Elastic MapReduce)** : cluster Hadoop/Spark/Flink managé. Scalabilité automatique, spot instances pour réduire les coûts (jusqu'à 90 %).
- **Amazon Athena** : moteur de requêtes SQL serverless directement sur S3 (basé sur Presto/Trino). Facturation à la quantité de données scannées. Idéal pour l'exploration ad hoc.
- **AWS Glue** : service ETL/ELT serverless + Data Catalog (métadonnées centralisées pour S3, RDS, Redshift). Supporte Spark et Ray.

**Entrepôt de données :**
- **Amazon Redshift** : Data Warehouse cloud (architecture MPP — Massively Parallel Processing). Stockage colonnaire. Redshift Spectrum : requêtes sur S3 depuis Redshift. Redshift Serverless : scalabilité automatique sans gestion de cluster.

**Streaming :**
- **Amazon Kinesis Data Streams** : ingestion de flux en temps réel (équivalent Kafka managé).
- **Amazon Kinesis Data Firehose** : livraison automatique vers S3, Redshift, OpenSearch.
- **Amazon MSK (Managed Streaming for Apache Kafka)** : Kafka entièrement managé.

**Orchestration et IA :**
- **AWS Step Functions** : orchestration de pipelines de données.
- **Amazon SageMaker** : ML managé (entraînement, déploiement, monitoring de modèles).

#### Google Cloud — BigQuery et Dataflow

**Google BigQuery**
- Data Warehouse serverless à l'architecture révolutionnaire : séparation totale du stockage (Colossus) et du compute (Dremel).
- **SQL ANSI** natif, sans gestion de cluster, scalabilité automatique.
- Facturation à la quantité de données traitées (10 $ / To) ou en capacité dédiée (slots).
- **BigQuery ML** : entraînement de modèles ML directement en SQL.
- **BigQuery Omni** : requêtes multi-cloud (S3, Azure) depuis BigQuery.
- **BigQuery Biglake** : tables sur GCS avec contrôle d'accès unifié.
- Performance : analyse d'1 To en quelques secondes.

**Autres services Google Cloud :**
- **Cloud Storage (GCS)** : stockage objet (équivalent S3).
- **Dataflow** : service de streaming et batch basé sur Apache Beam (modèle unifié batch/streaming).
- **Dataproc** : Hadoop/Spark managé (équivalent EMR).
- **Pub/Sub** : messagerie temps réel (équivalent Kafka managé).
- **Looker** : BI et data exploration (racheté par Google en 2019, 2,6 Md$).
- **Vertex AI** : plateforme ML unifiée (entraînement, MLOps, modèles génératifs).

#### Azure — Synapse Analytics et l'écosystème Microsoft

**Azure Synapse Analytics**
- Plateforme analytique unifiée combinant Data Warehouse (SQL pools), Spark (Spark pools), pipelines ETL et exploration de Data Lakes.
- Synapse Studio : interface unique pour tous les workloads analytiques.
- Intégration native avec Power BI, Azure ML, Purview.
- **Synapse Link** : synchronisation temps réel entre bases opérationnelles (Cosmos DB, Dataverse) et Synapse sans ETL.

**Autres services Azure Big Data :**
- **Azure Data Lake Storage Gen2 (ADLS Gen2)** : stockage objet hiérarchique pour Data Lakes (compatible HDFS).
- **Azure Data Factory (ADF)** : service ETL/orchestration managé (équivalent AWS Glue + Airflow).
- **Azure HDInsight** : Hadoop/Spark/Kafka managé.
- **Azure Event Hubs** : streaming compatible API Kafka.
- **Microsoft Fabric** : plateforme analytique tout-en-un lancée en 2023 (Data Factory + Synapse + Power BI + OneLake unifié). Modèle tarifaire unique par capacity.
- **Azure Databricks** : partenariat Microsoft-Databricks, Spark managé optimisé sur Azure.

#### Snowflake

Fondé en 2012, introduction en bourse en 2020 (la plus grande IPO logicielle de l'histoire à l'époque : 3,4 Md$).

**Architecture distinctive :**
- **Séparation totale** stockage (S3/Azure Blob/GCS) et compute (virtual warehouses).
- **Virtual Warehouses** : clusters de compute indépendants et élastiques, qui peuvent être suspendus en 5 secondes quand inactifs → facturation à la seconde.
- **Multi-cluster** : scalabilité automatique horizontale sous charge.
- **Time Travel** : accès aux données historiques jusqu'à 90 jours.
- **Data Sharing** : partage de données entre organisations Snowflake sans copie des données.
- **Snowpark** : exécution de code Python/Java/Scala directement dans Snowflake.
- **Snowflake Cortex** : fonctions LLM et ML intégrées (résumé, traduction, classification, embeddings).

**Snowflake Marketplace** : place de marché de jeux de données tiers accessibles directement dans Snowflake.

#### Databricks

Fondé en 2013 par les créateurs d'Apache Spark (UC Berkeley). Évalué à **43 milliards de dollars** en 2023.

**Plateforme unifiée Lakehouse :**
- **Delta Lake** : couche transactionnelle ACID sur le stockage objet (S3, ADLS, GCS). Gestion des versions, time travel, schema enforcement.
- **Unity Catalog** : gouvernance unifiée des données et de l'IA (data lineage, contrôle d'accès, audit).
- **Databricks SQL** : moteur SQL analytique optimisé sur Delta Lake (jusqu'à 12x plus rapide que BigQuery selon leurs benchmarks TPC-DS).
- **MLflow** : plateforme MLOps open-source (tracking d'expériences, déploiement de modèles).
- **AutoML** : entraînement automatisé de modèles.
- **Mosaic AI** : fine-tuning et déploiement de LLMs (Llama, DBRX).
- Disponible sur AWS, Azure et Google Cloud.

#### Comparatif synthétique

| Critère | AWS | Google Cloud | Azure | Snowflake | Databricks |
|---------|-----|-------------|-------|-----------|------------|
| Data Warehouse | Redshift | BigQuery | Synapse | Snowflake | Databricks SQL |
| Data Lake | S3 | GCS | ADLS Gen2 | S3/GCS/Azure | Delta Lake |
| ETL/Pipelines | Glue + Step Fns | Dataflow | ADF | Snowpark | Delta Live Tables |
| Streaming | Kinesis / MSK | Pub/Sub + Dataflow | Event Hubs | Snowpipe Streaming | Structured Streaming |
| ML/IA | SageMaker | Vertex AI | Azure ML | Cortex | Mosaic AI + MLflow |
| Modèle tarifaire | Pay-as-you-go | Pay-as-you-go | Pay-as-you-go | Credits (compute) | DBU (Databricks Units) |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Scalabilité élastique, pas d'infrastructure à gérer | Risque de vendor lock-in (formats propriétaires) |
| Time-to-market accéléré | Coûts difficiles à prévoir (pay-as-you-go) |
| Services managés à haute disponibilité (SLA 99,9 %+) | Coûts d'egress (transfert de données sortantes) élevés |
| Accès aux dernières innovations IA/ML sans déploiement | Dépendance à la connectivité Internet |
| Pas de maintenance des clusters | Conformité RGPD : localisation des données à vérifier |
| Intégration native entre services du même fournisseur | Compétences spécialisées nécessaires par plateforme |

### Acteurs et solutions du marché

- **Hyperscalers** : AWS (Amazon), Google Cloud Platform, Microsoft Azure.
- **Spécialistes** : Snowflake, Databricks, Cloudera (hybride/on-prem).
- **BI / Visualisation intégrée** : Looker (Google), Power BI (Microsoft), Tableau (Salesforce), QuickSight (AWS).
- **Orchestration** : Apache Airflow (Amazon MWAA, Google Cloud Composer, Astronomer).

### Cas d'usage concrets

1. **Booking.com — BigQuery pour la personnalisation** : Booking.com analyse des milliards d'événements de navigation quotidiens dans BigQuery pour personnaliser les recommandations d'hôtels en temps quasi réel. L'architecture serverless permet d'absorber les pics de charge saisonniers sans provisionnement.

2. **Capital One — Migration Snowflake** : Capital One a migré ses 4 Data Warehouses Teradata on-premise vers Snowflake, réduisant son TCO de 40 % et son temps de mise à disposition des données de 72 heures à moins de 4 heures. La séparation stockage/compute a permis d'optimiser finement les coûts.

3. **Heineken — Databricks pour la chaîne d'approvisionnement** : Heineken utilise Databricks pour consolider les données de 300 usines dans le monde sur un Lakehouse unifié. Les modèles ML prédictifs sur Delta Lake permettent d'optimiser la production et de réduire les ruptures de stock de 20 %.

### Chiffres et tendances

- AWS contrôle **34 %** du marché cloud mondial, Azure **21 %**, Google Cloud **11 %** (Synergy Research, Q1 2024).
- **Microsoft Fabric** ambitionne de remplacer toute la stack analytique Azure sous une interface unifiée, potentiellement le concurrent le plus direct de Databricks/Snowflake.
- Le modèle **serverless** (Athena, BigQuery, Synapse Serverless) devient dominant pour les requêtes ad hoc : zéro gestion de cluster, facturation à l'usage réel.
- Tendance forte : **convergence IA + Data** — toutes les plateformes intègrent des fonctions LLM nativement (BigQuery Gemini, Snowflake Cortex, Databricks Mosaic AI).
- **Iceberg comme standard ouvert** : AWS, Google, Snowflake, Databricks supportent tous Apache Iceberg pour éviter les silos de formats.

## Flashcards
#flashcards/Big_DATA/Plateformes_cloud_Big_Data #flashcards/Cloud_et_Virtualisation/Plateformes_cloud_Big_Data

Quelle est l'architecture distinctive de Snowflake ? :: Séparation totale du stockage (S3/Azure/GCS) et du compute (virtual warehouses élastiques et indépendants). Les warehouses peuvent être suspendus en quelques secondes, ne facturant que le temps d'utilisation réel.

Quelle est la différence entre Amazon Athena et Amazon Redshift ? :: Athena est un moteur SQL serverless qui interroge directement les fichiers sur S3 sans cluster — idéal pour l'exploration ad hoc, facturation à la donnée scannée. Redshift est un Data Warehouse MPP dédié, optimisé pour les requêtes analytiques répétitives et complexes.

Qu'est-ce que BigQuery et quelle est son innovation architecturale ? :: Data Warehouse serverless de Google basé sur Dremel (compute) et Colossus (stockage), avec séparation totale des deux couches. Pas de cluster à gérer, scalabilité automatique, facturation à la donnée traitée.

Qu'est-ce que Microsoft Fabric ? :: Plateforme analytique tout-en-un lancée en 2023 unifiant Data Factory (ETL), Synapse (analytique), Power BI (BI) et OneLake (stockage) sous une interface et un modèle tarifaire uniques (capacity).

Qu'est-ce que Delta Lake et qui l'a créé ? :: Format de table open-source créé par Databricks, ajoutant des transactions ACID, la gestion de versions (time travel) et l'évolution de schéma sur le stockage objet. Colonne vertébrale de l'architecture Lakehouse.

Citez 3 services AWS pour le Big Data et leur rôle. :: S3 (stockage objet pour Data Lakes), Amazon EMR (Spark/Hadoop managé), Amazon Athena (requêtes SQL serverless sur S3), Amazon Redshift (Data Warehouse MPP), Amazon Kinesis (streaming temps réel).

Qu'est-ce que MLflow et quel éditeur le développe ? :: Plateforme MLOps open-source créée par Databricks pour tracker les expériences ML, gérer les modèles (Model Registry) et orchestrer leur déploiement. Standard de facto pour la gestion du cycle de vie des modèles ML.

## Sources

- Synergy Research Group, *Cloud Infrastructure Market Share Q1 2024*.
- Snowflake, *Annual Report FY2025*.
- Google Cloud, *BigQuery Technical Documentation*, 2024.
- AWS, *AWS Big Data Services Overview*, 2024.
- Flexera, *State of the Cloud Report 2024*.
- Databricks, *The Data + AI Summit Keynote*, 2024.
- Gartner, *Magic Quadrant for Cloud Database Management Systems*, 2023.

## Notions liées

- [[Big Data — fondamentaux]]
- [[Data Lake - Data Warehouse - Lakehouse]]
- [[ETL - ELT et pipelines de données]]
- [[Écosystème Hadoop - Spark - Kafka]]
- [[Bases NoSQL]]
- [[Modèles de déploiement cloud]]
- [[Économie du cloud]]
- [[FinOps]]
- [[Vendor lock-in et réversibilité]]
