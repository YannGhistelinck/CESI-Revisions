---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Big Data — fondamentaux

![[N — Big Data — fondamentaux.mp3]]
## En bref
> **Définition** : Le Big Data désigne des ensembles de données dont le volume, la variété et la vélocité dépassent les capacités des systèmes de gestion de bases de données traditionnels. Ces données nécessitent des architectures et des outils spécialisés pour être collectées, stockées, traitées et analysées.
> **Pourquoi c'est important** : Pour une DSI, maîtriser le Big Data est un levier stratégique majeur : il permet d'améliorer la prise de décision, de personnaliser les services, d'optimiser les processus opérationnels et de créer de nouveaux modèles d'affaires fondés sur la donnée.
> **Chiffres clés** :
> - Le volume mondial de données créées, capturées et consommées a atteint **120 zettaoctets en 2023** et devrait dépasser **180 ZB d'ici 2025** (IDC, Data Age 2025).
> - **90 % des données mondiales ont été générées lors des deux dernières années** (IBM, 2023).
> - Le marché mondial du Big Data et de l'analytique devrait atteindre **745 milliards de dollars d'ici 2030** (Grand View Research, 2023).

## Approfondir

### Fonctionnement

#### Les 5V du Big Data

Le concept de Big Data est classiquement défini par les 5V, chaque V représentant une dimension caractéristique :

| Dimension | Description | Exemple |
|-----------|-------------|---------|
| **Volume** | Quantité massive de données (téraoctets, pétaoctets, exaoctets) | Logs serveurs, transactions bancaires, données IoT |
| **Vélocité** | Vitesse de génération et de traitement en temps réel ou quasi réel | Flux Twitter, transactions boursières (millions/seconde) |
| **Variété** | Diversité des formats et des sources de données | Texte, images, vidéos, JSON, CSV, XML, audio |
| **Véracité** | Qualité, fiabilité et précision des données | Données incomplètes, bruit, données dupliquées |
| **Valeur** | Capacité à extraire une information utile et exploitable | Insights business, prédictions, recommandations |

Certains auteurs ajoutent d'autres V : **Visualisation** (lisibilité des résultats), **Variabilité** (fluctuation du flux de données), **Vulnérabilité** (sécurité des données).

#### Types de données

**Données structurées**
- Organisées en lignes et colonnes dans un schéma prédéfini (modèle relationnel).
- Facilement interrogeables via SQL.
- Représentent environ **20 % des données mondiales**.
- Exemples : tables de bases de données relationnelles (MySQL, PostgreSQL), fichiers CSV, feuilles de calcul Excel.

**Données semi-structurées**
- Possèdent une structure partielle (balises, marqueurs) mais pas de schéma rigide.
- Auto-descriptives : les métadonnées sont incluses dans les données elles-mêmes.
- Exemples : JSON, XML, YAML, emails, logs applicatifs (Apache, Nginx), données MQTT IoT.

**Données non structurées**
- Aucun modèle de données prédéfini, format libre.
- Représentent environ **80 % des données mondiales** (IDC).
- Nécessitent des techniques de NLP, de vision par ordinateur ou de traitement audio pour être exploitées.
- Exemples : textes libres, images, vidéos, fichiers audio, PDF, publications sur les réseaux sociaux.

#### Métadonnées

Les métadonnées sont des "données sur les données" : elles décrivent, contextualisent et organisent les données principales sans en constituer le contenu.

- **Métadonnées descriptives** : titre, auteur, date de création, mots-clés.
- **Métadonnées structurelles** : organisation interne d'un document (chapitres, pages).
- **Métadonnées administratives** : droits d'accès, version, cycle de vie.
- **Métadonnées techniques** : format de fichier, codec, résolution, taille.

Rôle : indispensables pour la gouvernance des données (data catalog), la recherche, la conformité RGPD et la traçabilité.

#### Small Data

Opposé conceptuel du Big Data : désigne des volumes de données modestes, ciblés, lisibles et immédiatement interprétables par un humain.

- Utilisé pour des décisions locales, de terrain ou personnalisées.
- Ne nécessite pas d'infrastructure distribuée.
- Exemple : un tableau de bord KPI d'une PME, un rapport hebdomadaire de ventes.
- Tendance : le **Smart Small Data** cherche à extraire le maximum de valeur de petits jeux de données de haute qualité (utile dans les contextes où les données sont rares ou coûteuses à collecter).

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Prise de décision basée sur les données (data-driven) | Complexité technique et organisationnelle élevée |
| Détection de patterns invisibles à petite échelle | Coûts d'infrastructure et de compétences importants |
| Personnalisation à grande échelle (marketing, santé) | Risques liés à la qualité des données (garbage in, garbage out) |
| Optimisation des processus en temps réel | Enjeux de gouvernance, conformité RGPD |
| Création de nouveaux modèles économiques (data monetization) | Latence pour la mise en valeur (time to insight) |
| Capacité prédictive et anticipatrice | Risque de surinterprétation ou de biais algorithmiques |

### Acteurs et solutions du marché

- **Stockage et traitement distribué** : Apache Hadoop, Apache Spark, Apache Kafka
- **Bases de données NoSQL** : MongoDB, Cassandra, HBase, Redis
- **Plateformes cloud** : AWS (S3, EMR, Redshift), Google Cloud (BigQuery, Dataflow), Azure (Synapse, HDInsight)
- **Gouvernance et catalogage** : Apache Atlas, Collibra, Alation, DataHub
- **Visualisation** : Tableau, Power BI, Looker, Apache Superset
- **Éditeurs spécialisés** : Cloudera, Databricks, Snowflake

### Cas d'usage concrets

1. **Retail / e-commerce — Amazon** : analyse en temps réel des comportements d'achat de centaines de millions d'utilisateurs pour générer des recommandations personnalisées. Le moteur de recommandation représente environ 35 % du chiffre d'affaires d'Amazon.

2. **Santé — Analyse épidémiologique** : Durant la pandémie de COVID-19, des plateformes Big Data ont permis le suivi en temps réel de la propagation du virus, l'analyse des variants génomiques et l'optimisation de la distribution des vaccins à l'échelle mondiale (ex. : projet Our World in Data, NHS UK).

3. **Industrie — Maintenance prédictive (IIoT)** : General Electric collecte des données de milliers de capteurs sur ses moteurs d'avion (Predix platform). L'analyse de ces flux permet d'anticiper les pannes, réduisant les coûts de maintenance non planifiée de 25 à 30 %.

### Chiffres et tendances

- **2,5 quintillions d'octets** de données sont générés chaque jour dans le monde (Forbes, 2023).
- Seulement **32 % des données disponibles en entreprise** sont réellement analysées (Forrester, 2023).
- Le volume de données IoT devrait représenter **73 ZB d'ici 2025** (IDC).
- Les entreprises data-driven sont **23 fois plus susceptibles** d'acquérir de nouveaux clients (McKinsey).
- Le coût moyen d'un problème de qualité des données pour une organisation est estimé à **12,9 millions de dollars par an** (Gartner, 2022).

## Flashcards
#flashcards/Big_DATA/Big_Data_fondamentaux

Qu'est-ce que le Big Data ? :: Ensemble de données dont le volume, la variété et la vélocité dépassent les capacités des systèmes de gestion traditionnels, nécessitant des outils et architectures spécialisés.

Quels sont les 5V du Big Data ? :: Volume (quantité massive), Vélocité (vitesse de traitement), Variété (diversité des formats), Véracité (qualité des données), Valeur (utilité extractible).

Quelle est la différence entre données structurées et non structurées ? :: Les données structurées suivent un schéma rigide (tables SQL) ; les données non structurées n'ont pas de format prédéfini (textes, images, vidéos) et représentent ~80 % des données mondiales.

Qu'est-ce qu'une métadonnée ? :: Une donnée qui décrit une autre donnée : son auteur, sa date de création, son format, ses droits d'accès. Essentielle pour la gouvernance et la traçabilité.

Qu'est-ce que le Small Data ? :: Volume de données modeste, ciblé et directement interprétable par un humain, sans infrastructure distribuée. Opposé conceptuel du Big Data.

Quel est l'ordre de grandeur du volume de données créées chaque jour dans le monde ? :: Environ 2,5 quintillions d'octets (2,5 × 10^18 octets) par jour.

Pourquoi le Big Data est-il stratégique pour une DSI ? :: Il permet la prise de décision data-driven, la personnalisation des services, l'optimisation des processus et la création de nouveaux modèles économiques fondés sur la donnée.

## Sources

- IDC, *Data Age 2025*, 2023.
- IBM Institute for Business Value, *The Data Differentiator*, 2023.
- Grand View Research, *Big Data & Analytics Market Report*, 2023.
- Gartner, *Data Quality Market Survey*, 2022.
- McKinsey Global Institute, *The Age of Analytics*, 2023.
- Forrester, *The Forrester Data Strategy Report*, 2023.

## Notions liées

- [[Data Lake - Data Warehouse - Lakehouse]]
- [[ETL - ELT et pipelines de données]]
- [[Écosystème Hadoop - Spark - Kafka]]
- [[Bases NoSQL]]
- [[Plateformes cloud Big Data]]
- [[Data Lifecycle Management]]
- [[Sauvegarde et reprise d'activité]]
