---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Écosystème Hadoop - Spark - Kafka

![[N — Écosystème Hadoop - Spark - Kafka.mp3]]
## En bref
> **Définition** : Apache Hadoop est un framework open-source de traitement distribué de grandes quantités de données, basé sur le paradigme MapReduce et le système de fichiers distribué HDFS. Apache Spark est son successeur fonctionnel, jusqu'à 100 fois plus rapide grâce au traitement en mémoire. Apache Kafka est une plateforme de streaming distribué permettant le transport de flux de données en temps réel entre systèmes.
> **Pourquoi c'est important** : Ces technologies constituent la colonne vertébrale des architectures Big Data depuis les années 2000. Même si le cloud les abstrait de plus en plus, comprendre leur fonctionnement permet d'appréhender les fondements du traitement distribué, indispensable pour concevoir des systèmes de données à grande échelle.
> **Chiffres clés** :
> - Apache Spark est utilisé par **80 % des entreprises Fortune 500** pour leurs traitements analytiques distribués (Databricks, 2023).
> - Apache Kafka traite plus de **7 000 milliards de messages par jour** chez ses utilisateurs combinés (Confluent, 2023).
> - Hadoop est présent dans des clusters totalisant **plusieurs exaoctets** de données dans les grandes entreprises mondiales.

## Approfondir

### Fonctionnement

#### Apache Hadoop

Lancé par Yahoo! en 2006, inspiré des papiers Google (GFS 2003, MapReduce 2004). Projet Apache depuis 2008.

**Composants fondamentaux :**

**HDFS (Hadoop Distributed File System)**
- Système de fichiers distribué conçu pour stocker de très grands fichiers sur un cluster de machines ordinaires (commodity hardware).
- Architecture maître/esclave : **NameNode** (métadonnées, namespace) + **DataNodes** (blocs de données).
- Réplication des blocs (facteur de réplication par défaut : 3) pour la tolérance aux pannes.
- Taille de bloc par défaut : 128 Mo (optimisé pour les gros fichiers séquentiels).
- Principe : "move computation to data" (évite le transfert massif de données sur le réseau).

**MapReduce**
- Paradigme de programmation distribué en deux phases :
  - **Map** : application d'une fonction sur chaque enregistrement en parallèle sur chaque nœud. Produit des paires (clé, valeur).
  - **Reduce** : agrégation des paires de même clé en un résultat final.
- Shuffle & Sort : étape intermédiaire de redistribution des données entre Map et Reduce.
- Limitation majeure : écriture sur disque entre chaque étape → latence élevée.

**YARN (Yet Another Resource Negotiator)**
- Gestionnaire de ressources du cluster Hadoop.
- Sépare la gestion des ressources (ResourceManager) de l'exécution des tâches (ApplicationMaster).
- Permet à plusieurs frameworks (Spark, Tez, Flink) de coexister sur le même cluster.

**Écosystème Hadoop (outils associés) :**

| Outil | Rôle |
|-------|------|
| **Hive** | SQL analytique sur HDFS (HiveQL → MapReduce/Tez) |
| **HBase** | Base de données NoSQL colonnes sur HDFS (temps réel) |
| **Pig** | Langage de flux de données (Pig Latin) pour ETL |
| **Sqoop** | Import/export entre HDFS et bases relationnelles |
| **Oozie** | Orchestration de workflows Hadoop |
| **ZooKeeper** | Coordination distribuée, gestion de la configuration |
| **Ambari** | Gestion et monitoring du cluster Hadoop |

**Limites de Hadoop :**
- Lenteur due aux écritures disque entre les étapes MapReduce.
- Complexité opérationnelle (configuration, tuning).
- Inadapté au traitement interactif et au machine learning itératif.
- Tendance : remplacement progressif par Spark et par les services cloud managés.

#### Apache Spark

Créé à l'UC Berkeley (AMPLab) en 2009, Apache Spark est aujourd'hui le moteur de traitement distribué de référence.

**Principe fondamental — RDD (Resilient Distributed Dataset) :**
- Collection immuable et distribuée d'objets pouvant être traitée en parallèle.
- **Traitement en mémoire (in-memory)** : les données intermédiaires restent en RAM → jusqu'à **100x plus rapide** que Hadoop MapReduce pour les algorithmes itératifs.
- DAG (Directed Acyclic Graph) d'exécution : Spark optimise le plan d'exécution avant de lancer les calculs (lazy evaluation).
- **Tolérance aux pannes** : lignage (lineage) des RDD → recalcul des partitions perdues.

**APIs de haut niveau :**
- **DataFrame / Dataset API** : abstraction tabulaire avec optimiseur Catalyst (SQL-like).
- **Spark SQL** : requêtes SQL sur des DataFrames distribués.
- **Spark Streaming / Structured Streaming** : traitement en micro-batch ou streaming continu.
- **MLlib** : bibliothèque de machine learning distribué (classification, clustering, régression).
- **GraphX** : traitement de graphes distribués.

**Modes de déploiement :**
- Cluster standalone Spark.
- Sur YARN (Hadoop).
- Sur Kubernetes (tendance cloud native).
- Mode cloud : Databricks (optimisation propriétaire de Spark), AWS EMR, Google Dataproc, Azure HDInsight.

#### Apache Kafka

Créé par LinkedIn en 2011, Kafka est une plateforme de streaming d'événements distribuée, conçue pour le transport de flux de données à haute performance et faible latence.

**Concepts fondamentaux :**

| Concept | Description |
|---------|-------------|
| **Topic** | Canal logique de messages (ex. : "transactions", "logs-serveur") |
| **Partition** | Subdivision d'un topic pour le parallélisme. Les messages d'une partition sont ordonnés. |
| **Producer** | Application qui publie des messages dans un topic |
| **Consumer** | Application qui lit des messages depuis un topic |
| **Consumer Group** | Groupe de consommateurs se répartissant les partitions d'un topic |
| **Broker** | Serveur Kafka stockant et servant les messages |
| **Offset** | Position d'un message dans une partition. Permet le replay. |
| **Zookeeper / KRaft** | Coordination du cluster (ZooKeeper historique, KRaft depuis Kafka 3.x) |

**Garanties de livraison :**
- **At most once** : messages livrés 0 ou 1 fois (risque de perte).
- **At least once** : messages livrés au moins 1 fois (risque de doublon).
- **Exactly once** : garantie forte, messages livrés exactement 1 fois (transactions Kafka depuis 0.11).

**Kafka Streams & Kafka Connect :**
- **Kafka Streams** : bibliothèque Java de traitement de flux directement sur Kafka.
- **Kafka Connect** : framework de connecteurs pour intégrer Kafka avec des sources/destinations externes (JDBC, S3, Elasticsearch...).
- **ksqlDB** : SQL temps réel sur des flux Kafka.

#### Apache Flink

Alternative à Spark pour le streaming, Flink est natif streaming (contrairement au micro-batch de Spark Streaming).
- Traitement événement par événement avec gestion native du temps (event time, watermarks).
- Utilisé par Alibaba (e-commerce temps réel), Lyft, ING Bank.
- Souvent combiné avec Kafka (source) + Flink (traitement) + Cassandra/S3 (destination).

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Hadoop : robustesse, tolérance aux pannes | Hadoop : lenteur MapReduce, complexité opérationnelle |
| Spark : vitesse (in-memory), polyvalence (batch/streaming/ML) | Spark : consommation mémoire élevée, tuning complexe |
| Kafka : débit très élevé, durabilité, replay possible | Kafka : complexité de configuration, courbe d'apprentissage |
| Écosystème open-source, grande communauté | Nécessite des compétences spécialisées (data engineers) |
| Scalabilité horizontale native | Coûts d'infrastructure et d'exploitation significatifs |
| Formats ouverts, interopérabilité | Tendance au remplacement par des services cloud managés |

### Acteurs et solutions du marché

- **Hadoop managé** : Cloudera Data Platform (CDH), Amazon EMR, Azure HDInsight, Google Dataproc.
- **Spark managé** : Databricks (leader), Amazon EMR, Google Dataproc, Azure Synapse Spark.
- **Kafka managé** : Confluent Platform (cloud), Amazon MSK (Managed Streaming for Kafka), Azure Event Hubs (compatible Kafka).
- **Flink managé** : Amazon Kinesis Data Analytics, Ververica Platform (Alibaba), Google Datastream.

### Cas d'usage concrets

1. **LinkedIn — Invention de Kafka** : LinkedIn a créé Kafka pour résoudre un problème de transport de données entre ses microservices à une époque où il traitait plus de 1 milliard d'événements par jour. Kafka est aujourd'hui utilisé par plus de 80 % des entreprises Fortune 100.

2. **Databricks — Spark pour la genomique** : Des instituts de recherche (Broad Institute, BGI Genomics) utilisent Spark sur Databricks pour analyser des génomes complets à grande échelle. L'analyse d'un génome qui prenait des semaines avec des outils séquentiels prend désormais quelques heures.

3. **Uber — Pipeline temps réel avec Kafka + Flink** : Uber traite des milliards d'événements quotidiens (GPS, paiements, comportements app) via Kafka. Flink assure le calcul des prix dynamiques (surge pricing) en temps réel en moins de 100 ms de bout en bout.

### Chiffres et tendances

- **Kafka** est utilisé par plus de **100 000 organisations** dans le monde (Apache Software Foundation, 2024).
- Databricks (Spark) a levé **1,6 milliard de dollars** lors de sa série H en 2023, valorisée à 43 milliards.
- Le marché du streaming de données devrait atteindre **50 milliards de dollars d'ici 2028** (Allied Market Research).
- Tendance : migration progressive vers des services cloud managés (EMR, Dataproc, Confluent Cloud) pour réduire la complexité opérationnelle.
- **Apache Flink** connaît une adoption croissante pour les cas d'usage streaming pur, au détriment du micro-batch Spark.

## Flashcards
#flashcards/Big_DATA/Écosystème_Hadoop_Spark_Kafka

Qu'est-ce que le paradigme MapReduce ? :: Modèle de traitement distribué en deux phases : Map (application d'une fonction en parallèle sur chaque nœud, production de paires clé/valeur) et Reduce (agrégation des paires de même clé en un résultat). Hadoop en est l'implémentation de référence.

Pourquoi Spark est-il jusqu'à 100 fois plus rapide que Hadoop MapReduce ? :: Spark traite les données en mémoire (in-memory) et évite les écritures disque entre les étapes de calcul, contrairement à MapReduce qui écrit sur HDFS à chaque étape intermédiaire.

Qu'est-ce qu'un RDD dans Spark ? :: Resilient Distributed Dataset : collection immuable et distribuée d'objets, tolérante aux pannes par lignage (lineage). C'est l'abstraction fondamentale de Spark.

Qu'est-ce qu'un topic Kafka et comment est-il structuré ? :: Un topic est un canal logique de messages dans Kafka. Il est divisé en partitions (pour le parallélisme), chaque partition étant ordonnée et identifiée par des offsets. Les producteurs y publient, les consommateurs y lisent.

Quelle est la différence entre Spark Streaming et Apache Flink pour le traitement temps réel ? :: Spark Streaming utilise un modèle micro-batch (petits lots). Flink est nativement streaming (traitement événement par événement) avec une gestion avancée du temps (event time, watermarks), offrant une latence plus faible.

Qu'est-ce que YARN dans l'écosystème Hadoop ? :: Yet Another Resource Negotiator : gestionnaire de ressources du cluster Hadoop qui alloue CPU et mémoire aux applications et permet à plusieurs frameworks (Spark, Flink) de coexister sur le même cluster.

Qu'est-ce que Kafka Connect ? :: Framework de connecteurs standardisés permettant d'intégrer Kafka avec des sources et destinations externes (bases de données, S3, Elasticsearch...) sans développement de code personnalisé.

## Sources

- Apache Software Foundation, *Hadoop, Spark, Kafka Documentation*, 2024.
- Databricks, *The Big Book of Data Engineering*, 2023.
- Confluent, *Kafka State of Data Streaming Report*, 2023.
- Zaharia, M. et al., *Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing*, NSDI 2012.
- Kreps, J., Narkhede, N., Rao, J., *Kafka: A Distributed Messaging System for Log Processing*, LinkedIn Engineering, 2011.

## Notions liées

- [[Big Data — fondamentaux]]
- [[Data Lake - Data Warehouse - Lakehouse]]
- [[ETL - ELT et pipelines de données]]
- [[Bases NoSQL]]
- [[Plateformes cloud Big Data]]
