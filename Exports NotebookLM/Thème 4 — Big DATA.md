# Thème 4 — Big DATA
## Export consolidé NotebookLM — Révisions Grand Oral CESI

---

## Introduction

Le Big Data désigne l'ensemble des données dont le volume, la variété et la vélocité dépassent les capacités des systèmes de gestion traditionnels, nécessitant des outils et des architectures spécialisés pour être collectées, stockées, traitées et analysées. Pour une Direction des Systèmes d'Information, maîtriser le Big Data est devenu un levier stratégique incontournable : il permet d'améliorer la prise de décision, de personnaliser les services à grande échelle, d'optimiser les processus opérationnels et de créer de nouveaux modèles économiques fondés sur la donnée.

Le volume mondial de données créées, capturées et consommées a atteint cent vingt zettaoctets en 2023 et devrait dépasser cent quatre-vingts zettaoctets d'ici 2025. Seulement trente-deux pour cent des données disponibles en entreprise sont réellement analysées, et le coût moyen d'un problème de qualité des données est estimé à presque treize millions de dollars par an pour une organisation. Le marché mondial du Big Data et de l'analytique devrait atteindre sept cent quarante-cinq milliards de dollars d'ici 2030.

Ce document couvre l'ensemble du thème Big DATA en vingt et une notions : des fondamentaux technologiques aux architectures de stockage et de traitement, en passant par la gouvernance, la valorisation, la protection de la vie privée, et les cadres réglementaires européens et internationaux.

---

## Notions clés

### 1. Big Data — Fondamentaux et les cinq V

Le concept de Big Data est classiquement défini par cinq dimensions appelées les cinq V. Le premier V est le Volume, qui désigne les quantités massives de données allant des téraoctets aux exaoctets. Le deuxième V est la Vélocité, c'est-à-dire la vitesse de génération et de traitement des données en temps réel ou quasi réel. Le troisième V est la Variété, qui traduit la diversité des formats : texte, images, vidéos, fichiers JSON ou XML, données audio. Le quatrième V est la Véracité, soit la qualité et la fiabilité des données, car des données incomplètes ou dupliquées produisent des analyses erronées. Le cinquième V est la Valeur, autrement dit la capacité à extraire une information utile et exploitable.

On distingue trois grandes catégories de données. Les données structurées, organisées en lignes et colonnes dans un schéma prédéfini, représentent environ vingt pour cent des données mondiales et sont facilement interrogeables en langage SQL. Les données semi-structurées, comme le JSON ou le XML, possèdent une structure partielle mais restent auto-descriptives. Les données non structurées, qui représentent environ quatre-vingts pour cent des données mondiales, n'ont pas de format prédéfini et comprennent les textes libres, les images, les vidéos et les publications sur les réseaux sociaux.

Les métadonnées, c'est-à-dire les données sur les données, jouent un rôle fondamental. Elles décrivent, contextualisent et organisent les données principales : titre, auteur, date de création, format de fichier, droits d'accès. Elles sont indispensables pour la gouvernance des données, la traçabilité et la conformité réglementaire. À l'opposé du Big Data, le concept de Small Data désigne des volumes modestes, ciblés et immédiatement interprétables par un humain, sans nécessiter d'infrastructure distribuée.

Les entreprises pilotées par les données sont vingt-trois fois plus susceptibles d'acquérir de nouveaux clients selon McKinsey, mais seulement vingt-six pour cent des organisations sont considérées comme véritablement matures sur le plan data selon Forrester.

### 2. Architectures de stockage : Data Lake, Data Warehouse et Lakehouse

Le Data Warehouse, ou entrepôt de données, est un concept né dans les années 1990. C'est une base de données analytique centralisée, conçue pour le reporting et la Business Intelligence. Il fonctionne sur le principe du schema-on-write : le schéma de données est défini avant l'ingestion, ce qui garantit une qualité élevée des données mais impose une rigidité structurelle. La modélisation en étoile, avec une table de faits centrale entourée de tables de dimensions, est le modèle de référence. Les solutions leaders sont Snowflake, Google BigQuery et Amazon Redshift.

Le Data Lake, popularisé par James Dixon en 2010, stocke les données brutes dans leur format natif, sans transformation préalable. Il fonctionne sur le principe du schema-on-read : le schéma n'est appliqué qu'au moment de la lecture, selon le besoin. Il accepte tout type de données à un coût de stockage très bas, ce qui en fait un outil idéal pour le machine learning et l'exploration de données. Son risque majeur est le Data Swamp, c'est-à-dire le marécage de données : sans gouvernance rigoureuse, le lac devient un dépôt opaque où les données sont introuvables et inutilisables.

Le Data Lakehouse est une architecture hybride émergente popularisée par Databricks à partir de 2020. Il combine la flexibilité et le faible coût du Data Lake avec les fonctionnalités analytiques du Data Warehouse, notamment les transactions ACID, le contrôle de schéma et l'indexation. Les technologies clés sont Delta Lake de Databricks, Apache Iceberg créé par Netflix et Apple, et Apache Hudi développé par Uber. Le Lakehouse supprime la duplication entre le lac et l'entrepôt, supporte à la fois le SQL analytique et le machine learning sur les mêmes données, et utilise des formats ouverts comme Parquet pour éviter l'enfermement propriétaire. Les entreprises utilisant un Lakehouse réduisent leur coût total de possession analytique de trente à quarante pour cent par rapport aux architectures dupliquées.

### 3. ETL, ELT et pipelines de données

L'ETL, qui signifie Extract, Transform, Load, est le processus historique né avec les premiers Data Warehouses. La phase d'extraction collecte les données depuis des sources hétérogènes : bases relationnelles, fichiers plats, API, ERP ou CRM. La transformation est réalisée dans un moteur dédié avant le chargement et comprend le nettoyage, la normalisation des formats, les agrégations et l'application des règles métier. Le chargement insère ensuite les données transformées dans la destination analytique.

L'ELT, qui signifie Extract, Load, Transform, est l'approche moderne adaptée aux entrepôts cloud. Les données brutes sont d'abord chargées, puis transformées directement dans le système cible qui dispose d'une puissance de calcul élastique. Cela permet de conserver les données brutes pour les transformer différemment selon les besoins et d'exploiter la puissance massivement parallèle des plateformes cloud. La différence fondamentale est que dans l'ETL, la transformation précède le chargement, tandis que dans l'ELT, c'est l'inverse.

L'outil dbt, acronyme de data build tool, est devenu le standard de facto pour la couche de transformation dans les architectures ELT modernes. Il permet d'écrire des transformations en SQL pur avec des pratiques de génie logiciel comme le versionnage, les tests et la documentation automatique. Plus de trente mille entreprises l'utilisent dans le monde.

Les pipelines de données se déclinent en plusieurs types. Le traitement en batch traite périodiquement des volumes accumulés de données. Le streaming traite les données événement par événement dès leur arrivée avec des outils comme Apache Kafka ou Apache Flink. L'architecture Lambda combine une couche batch à haute précision et une couche streaming à faible latence. L'architecture Kappa simplifie cela en utilisant uniquement le streaming. L'orchestration des pipelines est assurée par des outils comme Apache Airflow, qui est le standard open source avec ses graphes acycliques orientés, aussi appelés DAG en anglais.

### 4. Écosystème Hadoop, Spark et Kafka

Apache Hadoop, lancé par Yahoo en 2006, est le framework open source fondateur du traitement distribué de données massives. Son composant HDFS, pour Hadoop Distributed File System, stocke les très grands fichiers sur un cluster de machines ordinaires avec une réplication par défaut sur trois nœuds pour assurer la tolérance aux pannes. Le paradigme MapReduce divise le traitement en deux phases : la phase Map applique une fonction en parallèle sur chaque nœud pour produire des paires clé-valeur, puis la phase Reduce agrège les paires de même clé en un résultat final. La limite principale de Hadoop est que les écritures disque entre chaque étape engendrent une latence élevée.

Apache Spark, créé à l'UC Berkeley en 2009, est aujourd'hui le moteur de traitement distribué de référence et est utilisé par quatre-vingts pour cent des entreprises du Fortune 500. Sa différence fondamentale avec Hadoop est le traitement en mémoire vive, appelé in-memory processing : les données intermédiaires restent en RAM, ce qui le rend jusqu'à cent fois plus rapide que MapReduce pour les algorithmes itératifs. L'abstraction fondamentale de Spark est le RDD, pour Resilient Distributed Dataset, une collection immuable et distribuée d'objets tolérante aux pannes. Spark propose des API de haut niveau comme DataFrame, Spark SQL, Spark Streaming pour le temps réel, et MLlib pour le machine learning distribué.

Apache Kafka, créé par LinkedIn en 2011, est une plateforme de streaming d'événements distribuée conçue pour le transport de flux de données à haute performance et faible latence. Elle traite plus de sept mille milliards de messages par jour chez ses utilisateurs combinés. Les concepts fondamentaux sont les topics, qui sont des canaux logiques de messages divisés en partitions pour le parallélisme, les producteurs qui publient des messages, et les consommateurs qui les lisent. Kafka garantit trois niveaux de livraison : at most once avec risque de perte, at least once avec risque de doublon, et exactly once avec une garantie forte.

Apache Flink est une alternative à Spark pour le streaming pur. Contrairement au micro-batch de Spark Streaming, Flink traite chaque événement individuellement avec une gestion native du temps, ce qui lui confère une latence plus faible pour les cas d'usage les plus exigeants.

### 5. Bases NoSQL

Les bases de données NoSQL, pour Not Only SQL, renoncent au modèle relationnel strict pour offrir flexibilité de schéma, scalabilité horizontale et performances adaptées à des types de données spécifiques. On distingue cinq grandes familles.

Les bases documentaires stockent des documents semi-structurés au format JSON ou BSON. MongoDB est la plus populaire au monde, avec un schéma flexible, des requêtes riches et une scalabilité automatique via le sharding. Les bases clé-valeur associent une clé à une valeur opaque. Redis est la référence pour le cache applicatif avec une latence sub-milliseconde grâce à son traitement en mémoire vive. Amazon DynamoDB est la solution managée par AWS avec une disponibilité de 99,999 pour cent. Les bases à colonnes larges organisent les données par colonnes pour optimiser les lectures et écritures massives. Apache Cassandra, avec son architecture peer-to-peer sans maître unique, élimine le Single Point of Failure et gère des millions d'écritures par seconde. Les bases de graphes représentent les données sous forme de nœuds et d'arêtes. Neo4j, avec son langage de requête Cypher, est idéal pour la détection de fraude, les réseaux sociaux et les moteurs de recommandation. Enfin, les bases vectorielles, en pleine explosion avec l'essor des modèles de langage, stockent et recherchent des vecteurs d'embedding pour la recherche sémantique et le RAG, pour Retrieval-Augmented Generation.

Le théorème CAP, formulé par Brewer en 2000, stipule qu'un système distribué ne peut garantir simultanément que deux des trois propriétés suivantes : la cohérence, la disponibilité et la tolérance au partitionnement réseau. Les bases NoSQL choisissent généralement les propriétés AP ou CP, au détriment de la cohérence forte ou de la disponibilité totale. Elles s'appuient sur le modèle BASE, pour Basically Available, Soft state, Eventually consistent, par opposition au modèle ACID des bases relationnelles.

### 6. Plateformes cloud Big Data

Les trois hyperscalers proposent des écosystèmes Big Data complets. AWS, qui détient trente-quatre pour cent du marché cloud mondial, propose Amazon S3 pour le stockage objet des Data Lakes, Amazon EMR pour les clusters Hadoop et Spark managés, Amazon Athena pour les requêtes SQL serverless directement sur S3, Amazon Redshift comme Data Warehouse MPP pour le traitement massivement parallèle, et Amazon Kinesis pour l'ingestion de flux en temps réel.

Google Cloud se distingue par BigQuery, son Data Warehouse serverless dont l'innovation architecturale réside dans la séparation totale du stockage via Colossus et du calcul via le moteur Dremel. Sans cluster à gérer, avec une scalabilité automatique et une facturation à la donnée traitée, BigQuery peut analyser un téraoctet en quelques secondes.

Microsoft Azure propose Azure Synapse Analytics comme plateforme analytique unifiée combinant Data Warehouse, Spark et pipelines ETL sous une interface unique. Microsoft Fabric, lancé en 2023, va plus loin en unifiant Data Factory, Synapse, Power BI et OneLake sous un modèle tarifaire unique par capacité.

Snowflake, fondé en 2012, se distingue par la séparation totale de son stockage sur S3 ou Azure Blob et de son calcul sur des virtual warehouses élastiques pouvant être suspendus en cinq secondes. Son Time Travel permet d'accéder aux données historiques jusqu'à quatre-vingt-dix jours. Databricks, créé par les inventeurs d'Apache Spark, propulse l'architecture Lakehouse avec Delta Lake, Unity Catalog pour la gouvernance unifiée, et MLflow comme plateforme MLOps open source standard.

Quatre-vingt-douze pour cent des entreprises utilisent le multi-cloud pour leurs workloads data. La tendance forte est la convergence IA et data : toutes les plateformes intègrent désormais des fonctions de modèles de langage nativement.

### 7. Infrastructure de stockage : SAN, NAS et HCI

L'infrastructure de stockage conditionne les performances, la scalabilité, le coût et la résilience du système d'information. Le SAN, pour Storage Area Network, est un réseau dédié haute performance reliant les serveurs à un pool de stockage centralisé via des protocoles spécialisés comme Fibre Channel ou iSCSI. Les serveurs voient le stockage SAN comme un disque local, ce qui offre des performances maximales pour les bases de données critiques, mais au prix d'une complexité et d'un coût très élevés.

Le NAS, pour Network Attached Storage, est un serveur de fichiers connecté au réseau local accessible via les protocoles SMB et NFS. Simple à administrer et peu coûteux, il est moins performant que le SAN pour les charges transactionnelles intensives mais convient parfaitement au partage de fichiers et à l'archivage.

L'HCI, pour Hyperconverged Infrastructure, intègre calcul, stockage et réseau sur des nœuds x86 standard gérés par une couche logicielle unifiée. La scalabilité est horizontale : on ajoute un nœud pour augmenter simultanément la capacité de calcul et de stockage. Nutanix, VMware vSAN et Dell VxRail sont les acteurs leaders. L'HCI représente trente pour cent des dépenses d'infrastructure de datacenter.

Le stockage objet est le paradigme clé pour le Big Data. Les données sont stockées sous forme d'objets avec un identifiant unique dans un espace d'adressage plat. Le protocole S3 d'Amazon est devenu le standard de facto. Ce type de stockage offre une scalabilité quasi illimitée à des coûts très bas et représente désormais soixante-cinq pour cent des nouvelles capacités déployées en datacenter. MinIO et Ceph permettent de déployer du stockage objet compatible S3 en mode on-premise.

### 8. Sauvegarde et reprise d'activité

La sauvegarde est la copie périodique des données pour permettre leur restauration. La reprise d'activité, aussi appelée Disaster Recovery, couvre l'ensemble des processus permettant de rétablir les systèmes après un sinistre. Ces deux disciplines s'inscrivent dans le cadre du PCA et du PRA, pour Plan de Continuité et Plan de Reprise d'Activité.

Trois types de sauvegardes existent. La sauvegarde complète copie l'intégralité des données et permet une restauration rapide mais consomme beaucoup d'espace. La sauvegarde incrémentale ne sauvegarde que les données modifiées depuis la dernière sauvegarde, qu'elle soit complète ou incrémentale : elle est rapide mais la restauration est complexe car elle nécessite toute la chaîne. La sauvegarde différentielle sauvegarde les données modifiées depuis la dernière complète : la restauration est plus simple, nécessitant seulement la complète et une différentielle.

La règle 3-2-1-1-0 est le standard moderne recommandé pour résister aux ransomwares. Elle prescrit trois copies des données, sur deux supports de stockage différents, dont une copie hors site, une copie hors ligne ou air-gapped déconnectée du réseau, et zéro erreur vérifiée par des tests réguliers de restauration. La sauvegarde immuable, basée sur le principe WORM pour Write Once Read Many, ne peut être ni modifiée, ni chiffrée, ni supprimée pendant une période définie, même par un attaquant ayant compromis les accès administrateur.

Les deux métriques fondamentales sont le RPO, pour Recovery Point Objective, qui désigne la perte de données maximale acceptable en temps, et le RTO, pour Recovery Time Objective, qui désigne la durée maximale d'indisponibilité acceptable. Les services BaaS, pour Backup as a Service, et DRaaS, pour Disaster Recovery as a Service, permettent d'externaliser ces fonctions dans le cloud en transformant des investissements en capital en charges d'exploitation.

Soixante pour cent des sauvegardes présentent des défauts qui les rendent partiellement ou totalement inutilisables lors de la restauration selon le rapport Veeam 2024, et quatre-vingt-treize pour cent des entreprises sans PRA robuste font faillite dans l'année suivant un sinistre majeur.

### 9. Data Governance

La gouvernance des données désigne l'ensemble des politiques, processus, rôles et standards qui garantissent que les données d'une organisation sont fiables, sécurisées, conformes et utilisables. Sans gouvernance, soixante pour cent des projets Big Data échouent selon Gartner, principalement à cause de problèmes de qualité et de cohérence des données.

La qualité des données se mesure selon six dimensions : l'exactitude, qui signifie que la donnée reflète la réalité ; la complétude, c'est-à-dire l'absence de valeurs manquantes ; la cohérence, qui implique la même valeur dans tous les systèmes ; l'actualité ou fraîcheur, soit la mise à jour selon la fréquence attendue ; l'unicité, c'est-à-dire l'absence de doublons ; et la validité, soit le respect des formats et règles métier.

Le data lineage est la capacité à tracer l'origine d'une donnée, ses transformations et ses destinations tout au long de son cycle de vie. Il est essentiel pour déboguer des valeurs erronées dans les rapports, assurer la conformité RGPD et réaliser des analyses d'impact avant de modifier une source de données.

Le data catalog est l'inventaire centralisé de tous les actifs de données d'une organisation avec leurs métadonnées techniques et métier. Les outils leaders sont Alation, centré sur la découverte collaborative, Collibra, orienté conformité et stewardship, Microsoft Purview intégré à l'écosystème Azure, et DataHub, créé par LinkedIn et très adopté en open source.

Un data contract est un accord formel entre le producteur et le consommateur d'une donnée, spécifiant le schéma, le niveau de service de fraîcheur, les règles de qualité et les responsabilités. Le MDM, pour Master Data Management, crée un enregistrement de référence unique appelé Golden Record pour les données maîtres partagées comme les clients, les produits et les fournisseurs, résolvant le problème des incohérences entre systèmes.

Les rôles clés sont le Chief Data Officer pour la stratégie data globale, le Data Owner responsable métier d'un domaine, et le Data Steward garant opérationnel de la qualité au quotidien.

### 10. Maturité data et Data Literacy

Le modèle de maturité data permet d'évaluer le niveau d'une organisation dans son usage des données. Le modèle Gartner en cinq niveaux progresse de Aware, où l'on reconnaît la valeur des données, jusqu'à Effective, où les données pilotent chaque décision avec l'IA et le machine learning opérationnels, en passant par Reactive, Proactive et Managed.

La data literacy, ou littératie des données, désigne la capacité des collaborateurs à lire, comprendre, questionner, créer et communiquer avec des données dans leur contexte. Soixante-quatorze pour cent des employés se déclarent dépassés ou anxieux face aux données, et seulement vingt-six pour cent des organisations sont véritablement pilotées par les données. Les déficits les plus fréquents sont la confusion entre corrélation et causalité, la surconfiance dans les visualisations et l'ignorance des limites des modèles selon le principe du garbage in, garbage out.

La démocratisation des données vise à rendre celles-ci accessibles à tous les collaborateurs au-delà des équipes IT, notamment via le self-service BI avec des outils comme Power BI ou Tableau. Mais sans gouvernance, elle engendre des rapports contradictoires, des violations de confidentialité et une paralysie par excès d'informations.

Les silos de données sont l'obstacle principal. Ils naissent des organisations fonctionnelles avec leurs propres outils, des systèmes legacy non intégrés et d'une culture de rétention de l'information. Les entreprises avec une forte data literacy ont une valorisation boursière trois à cinq pour cent supérieure à leurs pairs selon Gartner.

### 11. Business Intelligence

La Business Intelligence, abrégée BI, désigne l'ensemble des technologies permettant de collecter, transformer et visualiser les données pour faciliter la prise de décision. Elle transforme les données brutes en informations actionnables à travers des tableaux de bord, des rapports automatisés et des analyses exploratoires.

L'architecture BI classique suit la chaîne : sources de données, ETL ou ELT, Data Warehouse, couche sémantique, outil BI, utilisateur final. La distinction fondamentale est entre l'OLTP, pour Online Transaction Processing, optimisé pour les transactions unitaires rapides, et l'OLAP, pour Online Analytical Processing, optimisé pour les requêtes analytiques agrégées comme les sommes, comptages et regroupements.

La modélisation dimensionnelle formalisée par Ralph Kimball repose sur des tables de faits contenant les métriques mesurables et des tables de dimensions apportant le contexte. Le self-service BI permet aux utilisateurs métier de créer leurs propres analyses sans dépendre de l'équipe IT, mais il exige une couche sémantique bien conçue et une data literacy suffisante pour éviter la prolifération de rapports contradictoires.

L'augmented analytics intègre l'IA dans les outils BI pour automatiser l'analyse : les requêtes en langage naturel permettent de poser des questions comme on parlerait à un collègue, la détection automatique d'anomalies et l'explication automatique des variations accélèrent la compréhension.

Power BI de Microsoft est le leader en volume avec deux cent cinquante mille organisations clientes. Tableau de Salesforce est la référence en visualisation de données. Looker de Google est fort sur les données BigQuery. Apache Superset est devenu le standard des stacks data modernes en open source. Le retour sur investissement moyen de la BI est estimé à treize dollars pour chaque dollar investi selon Nucleus Research.

### 12. Types d'analytics

L'analytics se décline en quatre niveaux progressifs dont la valeur créée augmente avec la sophistication. L'analytics descriptive répond à la question : que s'est-il passé ? Elle produit des rapports, des tableaux de bord et des indicateurs clés. Elle est le point d'entrée universel, utilisé par quatre-vingts pour cent des organisations. L'analytics diagnostique répond à : pourquoi cela s'est-il passé ? Elle utilise le drill-down pour décomposer une métrique, l'analyse des causes racines et la corrélation. Elle identifie des corrélations mais ne garantit pas la causalité : c'est l'une des erreurs les plus fréquentes. L'analytics prédictive répond à : que va-t-il se passer ? Elle mobilise le machine learning supervisé comme la régression et la classification, les modèles de séries temporelles et le scoring prédictif pour anticiper la demande, les pannes ou le churn client. Elle n'est adoptée que par trente-cinq pour cent des organisations. L'analytics prescriptive répond à : que doit-on faire ? Elle utilise l'optimisation mathématique, la simulation Monte Carlo et le reinforcement learning pour automatiser des décisions complexes comme la tarification dynamique ou la logistique. Seules dix-sept pour cent des organisations l'utilisent.

Le data-driven decision making, c'est-à-dire la prise de décision fondée sur les données, impose de définir les questions avant de collecter les données, de garantir leur qualité et de combiner l'analytique quantitatif avec l'expertise métier qualitative. Les biais à éviter sont le biais de confirmation, qui consiste à chercher les données confirmant une idée préconçue, et la loi de Goodhart, selon laquelle quand une mesure devient un objectif, elle cesse d'être une bonne mesure. Les entreprises adoptant cette approche sont dix-neuf fois plus rentables selon McKinsey, mais soixante-dix pour cent des projets d'analytics prédictive ne passent jamais en production en raison de problèmes de MLOps et de gouvernance.

### 13. Data Mesh et Data Fabric

Le Data Mesh est une architecture de données décentralisée introduite par Zhamak Dehghani en 2019 pour résoudre les limites des architectures centralisées. Soixante-douze pour cent des organisations signalent que leur équipe data centrale est un goulot d'étranglement, ce qui engendre des délais de mise à disposition des données et une mauvaise qualité car l'équipe centrale ne connaît pas les contextes métier.

Le Data Mesh repose sur quatre principes fondamentaux. Premièrement, l'ownership orienté domaine : chaque domaine métier est responsable de ses propres données. Deuxièmement, les données comme produit : les données sont traitées comme des produits avec une interface stable, un niveau de service défini, un data contract formel et un propriétaire identifié. Troisièmement, l'infrastructure en libre-service : une plateforme commune fournit les outils d'ingestion, transformation, catalogage et qualité sans friction. Quatrièmement, la gouvernance fédérée : des standards communs définis centralement sont appliqués de manière décentralisée dans chaque domaine, sous forme de configurations automatisées plutôt que de processus manuels.

Le Data Fabric est une approche complémentaire et davantage technologique. C'est une couche d'abstraction intelligente pilotée par les métadonnées et l'IA qui connecte, découvre et intègre automatiquement les données de sources hétérogènes partout où elles se trouvent. Un knowledge graph de métadonnées décrit toutes les données et leurs relations, et l'IA recommande automatiquement des jointures et détecte des similarités.

Le Data-as-a-Service, ou DaaS, est le modèle de consommation où les données sont exposées via des API REST ou GraphQL standardisées, consommables par n'importe quel outil avec un niveau de service défini. Gartner prévoit que d'ici 2026, vingt-cinq pour cent des grandes entreprises auront adopté une architecture Data Mesh ou Data Fabric.

### 14. Monétisation des données

La monétisation des données désigne les mécanismes par lesquels des acteurs économiques tirent de la valeur financière des données personnelles ou comportementales. Elle prend deux formes. La monétisation directe consiste à vendre ou louer les données à des tiers, comme le font les data brokers. La monétisation indirecte utilise les données pour améliorer des produits ou services qui génèrent des revenus, comme la publicité ciblée de Google et Meta ou la personnalisation d'Amazon.

Les data brokers sont des entreprises dont le modèle économique repose entièrement sur la collecte, l'agrégation et la revente de données sur des individus sans relation directe avec eux. Acxiom détient des profils sur deux virgule cinq milliards de personnes dans le monde. Le marché mondial des data brokers pèse trois cent soixante-cinq milliards de dollars. En Europe, le RGPD impose un consentement explicite et le droit à l'effacement, contrairement aux États-Unis qui disposent d'une régulation très limitée en dehors de la Californie.

Le capitalisme de surveillance est un concept théorisé par Shoshana Zuboff dans son ouvrage The Age of Surveillance Capitalism publié en 2019. Sa thèse centrale est que le comportement humain est la matière première gratuite transformée en données comportementales, vendues comme produits de prédiction aux marchés publicitaires. Le surplus comportemental désigne les données collectées au-delà de ce qui est nécessaire à l'amélioration du service.

Le scandale Cambridge Analytica en 2018 a illustré les risques de la monétisation des données à grande échelle. Une application Facebook a collecté les données de deux cent soixante-dix mille utilisateurs ayant consenti, mais aussi celles de leurs amis via les permissions de l'API, exposant au total quatre-vingt-sept millions de profils. Ces profils ont été utilisés pour construire des profils psychologiques selon le modèle OCEAN et cibler des messages politiques lors des campagnes du Brexit et de Donald Trump en 2016. Facebook a été condamné à une amende de cinq milliards de dollars par la FTC américaine.

### 15. Privacy by Design

Le Privacy by Design, ou vie privée dès la conception, est une approche méthodologique consistant à intégrer la protection de la vie privée dès la conception d'un système, d'un produit ou d'un processus, et non en correctif après coup. Il est consacré à l'article 25 du RGPD. Ses sept principes fondateurs définis par Ann Cavoukian en 1995 sont les suivants : être proactif et non réactif, garantir la vie privée par défaut, intégrer la protection à la conception, maintenir une fonctionnalité totale sans compromis, assurer la sécurité de bout en bout sur tout le cycle de vie, garantir la visibilité et la transparence, et centrer la démarche sur le respect de la vie privée des utilisateurs.

Le Privacy by Default impose que les paramètres par défaut soient les plus protecteurs possible, sans action de l'utilisateur. Un formulaire ne collecte pas le numéro de téléphone si ce n'est pas nécessaire au service.

L'anonymisation rend irréversiblement impossible la ré-identification d'une personne. Une donnée véritablement anonymisée échappe au champ d'application du RGPD. Les techniques incluent la généralisation, la suppression, l'agrégation statistique et la differential privacy, qui ajoute du bruit statistique pour protéger l'identité individuelle tout en préservant la précision des statistiques agrégées. Apple utilise cette technique depuis 2016 pour iOS.

La pseudonymisation remplace les identifiants directs par des pseudonymes, mais la ré-identification reste possible avec la table de correspondance. La donnée pseudonymisée reste une donnée personnelle au sens du RGPD. Le DPIA, pour Data Protection Impact Assessment, est l'étude d'impact sur la protection des données obligatoire avant tout traitement à risque élevé selon l'article 35 du RGPD. Si les risques résiduels restent élevés après les mesures, la consultation préalable de la CNIL est obligatoire.

La ré-identification est un risque particulièrement élevé en Big Data : Latanya Sweeney a montré en 1997 que quatre-vingt-sept pour cent des Américains peuvent être ré-identifiés uniquement avec le code postal, la date de naissance et le sexe.

### 16. Profilage et surveillance

Le profilage automatisé est défini à l'article 4 alinéa 4 du RGPD comme tout traitement automatisé de données personnelles visant à évaluer des aspects personnels d'un individu : comportement, préférences, solvabilité, santé, localisation. Les techniques incluent la segmentation comportementale, le scoring prédictif, l'analyse de sentiment et l'analyse de graphes de relations sociales.

La bulle de filtre est le phénomène conceptualisé par Eli Pariser en 2011 par lequel les algorithmes de recommandation de plateformes comme YouTube, Facebook ou TikTok enferment l'utilisateur dans un espace informationnel homogène. En filtrant les contenus selon son profil pour maximiser l'engagement, ces algorithmes réduisent l'exposition à des points de vue divergents et peuvent conduire à la polarisation politique et à la radicalisation progressive. Une étude du MIT de 2018 montre que les fausses nouvelles se propagent six fois plus vite que les vraies sur Twitter, favorisées par les algorithmes d'engagement.

L'article 22 du RGPD donne aux personnes le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou significatifs. Cela concerne le scoring de crédit, la sélection de candidats ou la tarification dynamique. L'organisation doit prévoir une intervention humaine sur demande, un droit à l'explication et un droit de contester la décision. Le Digital Services Act impose depuis 2024 aux très grandes plateformes de proposer aux utilisateurs européens au moins une option de recommandation non basée sur le profilage comportemental.

### 17. RGPD

Le RGPD, pour Règlement Général sur la Protection des Données, aussi connu comme Règlement UE 2016/679, est le cadre réglementaire européen régissant le traitement des données à caractère personnel, applicable depuis le 25 mai 2018. Il s'applique à toute organisation traitant des données de résidents européens, quel que soit le pays d'établissement de l'organisation, ce qui constitue le principe d'extraterritorialité.

Les sept principes fondamentaux de l'article 5 sont la licéité, la loyauté et la transparence ; la limitation des finalités ; la minimisation des données ; l'exactitude ; la limitation de la conservation ; l'intégrité et la confidentialité ; et la responsabilité, aussi appelée accountability, qui oblige le responsable de traitement à démontrer son respect du règlement.

Les six bases légales de l'article 6 sont le consentement, l'exécution d'un contrat, l'obligation légale, la sauvegarde des intérêts vitaux, la mission d'intérêt public et les intérêts légitimes du responsable de traitement. Les droits des personnes couvrent l'accès, la rectification, l'effacement aussi appelé droit à l'oubli, la limitation, la portabilité, l'opposition et le droit de ne pas faire l'objet d'une décision automatisée.

La désignation d'un DPO, pour Délégué à la Protection des Données, est obligatoire pour les autorités publiques, les organisations dont l'activité principale nécessite un suivi régulier et à grande échelle des personnes, ou le traitement à grande échelle de données sensibles. Le délai de notification d'une violation de données à l'autorité de contrôle est de soixante-douze heures. La sanction maximale est de vingt millions d'euros ou quatre pour cent du chiffre d'affaires mondial annuel. Le bilan 2023 du CEPD recense plus de mille six cents amendes pour un total supérieur à quatre virgule deux milliards d'euros, dont un milliard deux cents millions d'euros infligés à Meta pour transferts illicites vers les États-Unis.

### 18. Réglementations internationales sur les données

Face à la fragmentation réglementaire mondiale, plusieurs grandes lois coexistent avec le RGPD. Plus de cent soixante pays ont adopté une législation de protection des données personnelles en 2023.

Le CCPA, pour California Consumer Privacy Act, entré en vigueur en janvier 2020 et renforcé par le CPRA en 2023, s'applique aux entreprises dépassant certains seuils : chiffre d'affaires annuel supérieur à vingt-cinq millions de dollars, traitement des données de plus de cent mille consommateurs californiens par an, ou plus de cinquante pour cent des revenus issus de la vente de données. Contrairement au RGPD qui fonctionne sur le principe de l'opt-in, le CCPA est fondé sur l'opt-out : la collecte est autorisée par défaut mais le consommateur peut s'y opposer.

La LGPD, pour Lei Geral de Proteção de Dados, est la loi brésilienne entrée en vigueur en septembre 2020. Fortement inspirée du RGPD, elle prévoit dix bases légales, des droits similaires aux personnes, un équivalent du DPO appelé Encarregado et une autorité de contrôle, l'ANPD.

La PIPL, pour Personal Information Protection Law, est la première loi globale de protection des données en Chine, entrée en vigueur en novembre 2021. Elle place le consentement comme base légale centrale et impose des conditions très strictes pour les transferts internationaux, nécessitant une certification de sécurité par l'autorité chinoise, la CAC. Elle s'inscrit dans un cadre plus large incluant la loi sur la cybersécurité et la loi sur la sécurité des données, qui imposent des exigences de localisation des données critiques sur le territoire chinois.

La fragmentation réglementaire engendre un coût estimé à deux à quatre pour cent du budget IT pour la conformité multi-juridictionnelle dans les grandes organisations.

### 19. DSA et DMA

Le Digital Services Act, ou DSA, et le Digital Markets Act, ou DMA, sont deux règlements européens formant le paquet numérique adopté en 2022. Ils s'appliquent respectivement depuis 2024 pour tous les opérateurs. Le DSA régule la responsabilité des plateformes pour les contenus illicites, impose la transparence des algorithmes et protège les utilisateurs. Le DMA vise à contester le pouvoir de marché des grandes plateformes désignées gatekeepers pour garantir des marchés numériques équitables et contestables.

Un gatekeeper est désigné si son chiffre d'affaires européen annuel dépasse sept virgule cinq milliards d'euros ou si sa valorisation dépasse soixante-quinze milliards d'euros, avec plus de quarante-cinq millions d'utilisateurs mensuels actifs dans l'Union européenne. Sept gatekeepers ont été désignés fin 2023 : Alphabet, Amazon, Apple, ByteDance, Meta, Microsoft et Booking.com.

Le DMA interdit aux gatekeepers de combiner les données personnelles issues de différents services sans consentement explicite : Meta ne peut plus croiser les données de Facebook, Instagram et WhatsApp sans accord de l'utilisateur. Il impose l'interopérabilité des messageries : WhatsApp doit permettre aux utilisateurs de Signal ou Telegram de lui envoyer des messages. Il interdit aussi la favorisation de ses propres services dans les classements, dit auto-préférence.

Le DSA impose aux très grandes plateformes, désignées VLOP pour Very Large Online Platform, une évaluation annuelle des risques systémiques, un audit indépendant et l'accès des chercheurs aux données. Il interdit la publicité ciblée pour les mineurs et basée sur des données sensibles. Les sanctions atteignent six pour cent du chiffre d'affaires mondial annuel pour le DSA et dix pour cent pour le DMA, avec possibilité de démantèlement structurel en cas de violation systémique.

### 20. Normes ISO liées aux données

Plusieurs normes ISO encadrent la protection des données personnelles et du stockage. L'ISO 27701, publiée en 2019, est une extension de l'ISO 27001 qui ajoute un système de management de la protection des données personnelles, ou PIMS pour Privacy Information Management System. Elle fournit un cadre applicable au responsable de traitement comme au sous-traitant et fait un mapping explicite avec le RGPD dans son annexe D. Une organisation certifiée peut utiliser ce certificat comme élément de preuve d'accountability au sens du RGPD. La certification ISO 27701 requiert d'avoir déjà l'ISO 27001 en place.

L'ISO 27018, publiée en 2019, est un code de conduite pour la protection des données personnelles dans le cloud public. Elle s'adresse aux fournisseurs de services cloud agissant comme sous-traitants. Ses principes clés sont l'interdiction d'utiliser les données à des fins publicitaires sans consentement, le contrôle conservé par le client, la transparence et la notification des violations. AWS, Microsoft Azure et Google Cloud sont certifiés ISO 27018 depuis 2014-2015, mais cette certification ne protège pas contre le CLOUD Act qui peut contraindre un opérateur américain à divulguer des données malgré tout.

L'ISO 27040, révisée en 2024, définit les lignes directrices pour la sécurité des dispositifs et systèmes de stockage. Elle couvre la classification des données, les contrôles de sécurité, la sanitisation des supports avant réutilisation ou destruction, et la sécurité des sauvegardes. L'ISO 29134 fournit les lignes directrices pour les évaluations d'impact sur la vie privée, alignées avec les exigences du DPIA de l'article 35 du RGPD. L'ISO 31700, publiée en 2023, est le premier standard international formalisant le Privacy by Design pour les produits de consommation.

### 21. Souveraineté numérique

La souveraineté numérique désigne la capacité d'un État, d'une organisation ou d'un individu à exercer un contrôle effectif sur ses systèmes numériques, ses infrastructures, ses données et ses technologies. Elle se distingue de la simple localisation physique des données, appelée data residency : un opérateur américain peut héberger des données en France tout en restant soumis au CLOUD Act, ce qui rend la souveraineté insuffisante.

Les enjeux géopolitiques sont structurants. La rivalité technologique entre les États-Unis et la Chine porte sur les semiconducteurs, les réseaux 5G, les modèles d'intelligence artificielle et les données des citoyens. L'extraterritorialité américaine constitue un risque direct : le CLOUD Act de 2018 permet aux autorités américaines d'accéder aux données détenues par des opérateurs américains quel que soit le pays de stockage. Soixante-treize pour cent du marché mondial du cloud est détenu par trois acteurs américains, AWS, Azure et Google Cloud, ce qui crée une dépendance structurelle.

Le label SecNumCloud de l'ANSSI définit les exigences d'un cloud souverain en France : opérateur de droit européen à capital majoritairement européen, données chiffrées avec clés gérées en Europe, aucune donnée accessible à des entités hors Union européenne. Moins de dix fournisseurs l'ont obtenu en 2024, dont OVHcloud et Outscale.

Deux approches de cloud souverain coexistent. Le cloud de confiance hybride, comme S3NS de Thales avec Google Cloud ou Bleu d'Orange et Capgemini avec Microsoft Azure, opère une infrastructure sur technologie américaine sans que l'éditeur ait accès aux données. Le cloud natif souverain repose sur une infrastructure entièrement européenne sans composant américain.

Les stratégies organisationnelles BYOK, pour Bring Your Own Key, permettent à l'organisation de conserver ses propres clés de chiffrement séparées de l'opérateur cloud. Même un opérateur américain ne peut lire les données chiffrées avec des clés BYOK qu'il ne détient pas. La variante HYOK, pour Hold Your Own Key, va plus loin en conservant les clés dans un équipement de sécurité on-premise, de sorte qu'elles ne quittent jamais le périmètre de l'organisation.

L'initiative Gaia-X, lancée en 2020 par la France et l'Allemagne, vise à créer un cadre de confiance pour un écosystème de données souverain et interopérable en Europe. Elle compte plus de trois cent cinquante membres en 2024 mais est critiquée pour sa lenteur et l'adhésion de membres américains qui diluent son caractère souverain.

---

## Questions jury

Les questions suivantes ont été identifiées comme représentatives des sujets examinés par le jury sur ce thème.

Qu'est-ce que les cinq V du Big Data et pourquoi sont-ils importants ? Il faut présenter les cinq dimensions, expliquer pourquoi elles représentent un défi technique et organisationnel, et illustrer avec des exemples concrets comme le volume des données IoT ou la vélocité des transactions boursières.

Quelle est la différence entre Data Lake et Data Warehouse, et quand utiliser l'un ou l'autre ? La réponse clé tourne autour du schema-on-write contre schema-on-read, du niveau de qualité des données, du coût de stockage, et du type d'usage : reporting structuré pour le Data Warehouse, exploration et machine learning pour le Data Lake, les deux avec le Lakehouse.

Comment mettre en place une gouvernance des données dans une PME ? Il faut aborder la proportionnalité de la démarche, en commençant par un inventaire des données, la désignation d'un responsable, la mise en place d'un catalogue simple et des règles de qualité, avant d'envisager des outils plus sophistiqués.

Quels outils Big Data sont adaptés aux petites entreprises ? La réponse doit mentionner des outils accessibles comme Power BI, Metabase, Google BigQuery en mode serverless, dbt Core en open source, et des solutions SaaS comme Fivetran ou Airbyte pour l'intégration.

Comment le RGPD impacte-t-il un projet Big Data ? Les points clés sont la minimisation des données, la gestion du consentement, l'anonymisation et la pseudonymisation, le droit à l'effacement dans les Data Lakes et les sauvegardes, et l'obligation de réaliser un DPIA pour les traitements à risque élevé.

Quelle est la différence entre analytics descriptive, prédictive et prescriptive ? Il faut bien maîtriser les quatre niveaux, les questions auxquelles ils répondent, les outils correspondants et la complexité croissante, en montrant pourquoi la majorité des organisations reste bloquée au niveau descriptif.

Data Mesh contre Data Fabric : quelle architecture choisir ? La réponse doit distinguer l'approche organisationnelle décentralisée du Data Mesh de l'approche technologique centralisée du Data Fabric, et expliquer que les deux peuvent coexister selon la maturité et la taille de l'organisation.

Comment justifier le retour sur investissement d'un projet Big Data auprès du comité de direction ? Il faut aborder les indicateurs de valeur comme la réduction des coûts opérationnels, l'augmentation du chiffre d'affaires par la personnalisation, la réduction des risques et les économies sur la qualité des données, en s'appuyant sur des études comme McKinsey ou Gartner.

Quels sont les risques du Big Data en termes de surveillance et de vie privée ? La réponse doit couvrir le profilage automatisé, les bulles de filtre, le capitalisme de surveillance, les dark patterns et les cadres réglementaires comme le RGPD, l'article 22, le DSA et l'AI Act qui encadrent ces pratiques.

Comment assurer la qualité des données ? Les six dimensions de la qualité, les outils comme Great Expectations et Monte Carlo, les data contracts, la gouvernance via le data catalog et le rôle du Data Steward sont les éléments attendus.

Quel est l'impact du DSA et du DMA sur les entreprises qui exploitent des données ? Il faut distinguer les obligations pour les gatekeepers, les contraintes sur le profilage des mineurs, l'interopérabilité, la transparence algorithmique et les nouvelles opportunités d'accès aux données des grandes plateformes pour les chercheurs et les concurrents.

---

## Points de vigilance

Ces points représentent les erreurs fréquentes ou les nuances importantes à maîtriser pour l'oral.

Ne pas confondre anonymisation et pseudonymisation. L'anonymisation est irréversible et sort les données du champ du RGPD. La pseudonymisation est réversible et les données restent personnelles au sens du règlement.

Ne pas confondre data residency et souveraineté des données. Stocker des données en France chez AWS ne suffit pas à garantir la souveraineté si l'opérateur reste soumis au CLOUD Act.

Ne pas confondre corrélation et causalité en analytics diagnostique. Une corrélation identifie des variables liées statistiquement, mais la causalité nécessite des expérimentations contrôlées.

Ne pas affirmer que le RGPD s'arrête aux frontières de l'Union européenne. Son extraterritorialité signifie qu'il s'applique à toute organisation traitant des données de résidents européens, quel que soit son pays d'établissement.

Ne pas confondre ETL et ELT. Dans l'ETL, la transformation précède le chargement dans une zone de préparation externe. Dans l'ELT, les données brutes sont d'abord chargées, puis transformées dans le système cible.

Ne pas présenter le Data Mesh comme une simple solution technique. Il s'agit avant tout d'un changement organisationnel : sans culture data forte dans chaque domaine métier et sans sponsor au niveau direction, l'architecture échoue.

Ne pas minimiser les risques du Data Lake. Sans gouvernance rigoureuse, catalogage et métadonnées, tout Data Lake risque de devenir un Data Swamp où les données sont introuvables et inutilisables, ce qui représente soixante pour cent des cas selon Gartner.

Ne pas oublier que l'ISO 27018 ne protège pas contre le CLOUD Act. Un fournisseur cloud américain certifié peut toujours être contraint par les autorités américaines de divulguer des données.

Ne pas confondre RPO et RTO. Le RPO mesure la perte de données maximale acceptable en temps, le RTO mesure la durée maximale d'indisponibilité acceptable. Ce sont deux dimensions complémentaires et distinctes du Plan de Reprise d'Activité.

Ne pas présenter le CCPA comme un équivalent du RGPD. Le CCPA fonctionne sur le principe de l'opt-out contrairement au RGPD fondé sur l'opt-in, il ne requiert pas de base légale pour la collecte et son champ d'application est limité aux entreprises dépassant certains seuils de taille.

Attention à la loi de Goodhart en analytics : quand une mesure devient un objectif, elle cesse d'être une bonne mesure. Optimiser le Net Promoter Score en récompensant les promoteurs plutôt qu'en améliorant réellement le service est un piège classique du data-driven decision making.

---

*Document généré pour une utilisation avec NotebookLM — Format optimisé pour la génération audio. 21 notions couvrant l'intégralité du thème Big DATA.*
