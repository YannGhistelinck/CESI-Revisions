---
type: notion
thèmes:
  - Big DATA
  - IA
statut: pas vu
dernière_révision: 
---

# Bases NoSQL

![[N — Bases NoSQL.mp3]]
## En bref
> **Définition** : Les bases de données NoSQL (Not Only SQL) sont des systèmes de gestion de données qui renoncent au modèle relationnel strict pour offrir une flexibilité de schéma, une scalabilité horizontale et des performances adaptées à des types de données spécifiques. Elles se déclinent en plusieurs familles : documentaires, clé-valeur, colonnes larges, graphes et vectorielles.
> **Pourquoi c'est important** : Les bases relationnelles traditionnelles montrent leurs limites face aux volumes, à la variété et à la vélocité du Big Data. Les DSI doivent maîtriser les différentes familles NoSQL pour choisir le bon outil selon le cas d'usage : haute disponibilité, faible latence, données de graphe ou recherche par similarité pour l'IA.
> **Chiffres clés** :
> - Le marché mondial des bases NoSQL devrait atteindre **82 milliards de dollars d'ici 2028** (MarketsandMarkets, 2023).
> - MongoDB est utilisé par plus de **47 000 entreprises** dans le monde, dont 40 % du Fortune 100 (MongoDB, 2024).
> - Les bases vectorielles connaissent une croissance de **300 % en 2023** avec l'essor des LLMs (Gartner, 2024).

## Approfondir

### Fonctionnement

#### Le théorème CAP

Fondamental pour comprendre les compromis NoSQL, le théorème CAP (Brewer, 2000) stipule qu'un système distribué ne peut garantir simultanément que 2 des 3 propriétés suivantes :

- **Consistency (Cohérence)** : tous les nœuds voient les mêmes données au même instant.
- **Availability (Disponibilité)** : chaque requête reçoit une réponse (sans garantie que ce soit la version la plus récente).
- **Partition tolerance (Tolérance au partitionnement)** : le système fonctionne malgré la perte de communication entre nœuds.

Les bases NoSQL choisissent généralement AP (disponibilité + tolérance partition) ou CP (cohérence + tolérance partition), au détriment de la cohérence forte ou de la disponibilité totale.

**Modèle BASE vs ACID :**
- **ACID** (Atomicité, Cohérence, Isolation, Durabilité) : garanties des bases relationnelles.
- **BASE** (Basically Available, Soft state, Eventually consistent) : modèle de cohérence éventuelle des bases NoSQL distribuées.

#### Bases documentaires

**Modèle** : stockage de documents semi-structurés (JSON, BSON, XML). Chaque document est auto-décrit et peut avoir une structure différente.

**MongoDB**
- La base documentaire la plus populaire au monde.
- Documents BSON (Binary JSON) dans des collections (équivalent des tables).
- Schéma flexible : pas de schéma fixe obligatoire.
- Requêtes riches : filtres, agrégations (Aggregation Pipeline), recherche full-text.
- Scalabilité : sharding automatique, réplication via Replica Sets.
- Transactions ACID multi-documents depuis la version 4.0.
- Atlas : service cloud managé (AWS, GCP, Azure).
- Cas d'usage : catalogues produits, profils utilisateurs, CMS, IoT.

**CouchDB / CouchBase**
- CouchDB : base documentaire HTTP-native, réplication peer-to-peer, offline-first.
- Couchbase : hybride documentaire + clé-valeur, optimisé pour les applications mobiles et temps réel.

#### Bases clé-valeur

**Modèle** : association simple clé → valeur. La valeur est opaque (la base ne connaît pas sa structure interne).

**Redis (Remote Dictionary Server)**
- Base clé-valeur en mémoire (in-memory), latence sub-milliseconde.
- Structures de données riches : strings, listes, sets, sorted sets, hashmaps, streams, HyperLogLog.
- Cas d'usage : cache (session, résultats de requêtes), leaderboards, pub/sub, files de messages.
- Persistance optionnelle : RDB (snapshot) et AOF (append-only file).
- Redis Cluster pour la scalabilité horizontale.
- Redis Stack : extensions pour recherche full-text, vecteurs, graphes, séries temporelles.

**Amazon DynamoDB**
- Service clé-valeur + documentaire managé par AWS.
- Scalabilité automatique, disponibilité 99,999 %, latence single-digit milliseconde.
- Modèle de capacité : provisionné ou à la demande (on-demand).
- Utilisé par des applications à très haute charge : Amazon.com, Lyft, Duolingo.

#### Bases colonnes larges (Wide Column)

**Modèle** : données organisées par colonnes plutôt que par lignes. Chaque ligne peut avoir un ensemble de colonnes différent. Optimisé pour les lectures/écritures de grandes quantités de colonnes.

**Apache Cassandra**
- Créée par Facebook (2008), open-source depuis 2009.
- Architecture peer-to-peer sans maître (tous les nœuds sont égaux) → pas de SPOF (Single Point of Failure).
- Partition ring : données distribuées par hachage de la clé de partition (consistent hashing).
- Tunable consistency : choix du niveau de cohérence par requête (ONE, QUORUM, ALL).
- CQL (Cassandra Query Language) : syntaxe proche de SQL.
- Cas d'usage : séries temporelles, IoT (millions d'écritures/seconde), logs, messagerie (Discord : milliards de messages).
- Limites : pas de jointures, pas de requêtes ad hoc efficaces (modélisation guidée par les requêtes).

**HBase**
- Implémentation Hadoop de BigTable (Google, 2006).
- Stocké sur HDFS, intégré à l'écosystème Hadoop.
- Accès aléatoire en lecture/écriture sur des données de type Big Data.
- Cas d'usage : tables de correspondances à grande échelle, historiques de logs.

**Google Bigtable**
- Service cloud managé (Google Cloud), base de HBase.
- Utilisé en interne par Google pour Gmail, Google Maps, Google Search.

#### Bases de graphes

**Modèle** : données représentées sous forme de nœuds (entités) et d'arêtes (relations), avec des propriétés associées aux deux. Optimisé pour les traversées de graphes (requêtes de proximité, chemins, communautés).

**Neo4j**
- La base de graphes la plus répandue.
- Langage de requête : **Cypher** (déclaratif, intuitif pour les patterns de graphe).
- Architecture native graphe : stockage optimisé pour les traversées.
- Cas d'usage : détection de fraude (graphes de transactions), réseaux sociaux (graphes d'amis), moteurs de recommandation, knowledge graphs, gestion d'identité (IAM).
- Neo4j AuraDB : version cloud managée.

**Amazon Neptune**
- Service cloud managé (AWS) supportant les modèles de graphe RDF (SPARQL) et Property Graph (Gremlin, openCypher).

**Autres** : TigerGraph, ArangoDB (multi-modèle), JanusGraph (distribué).

#### Bases vectorielles

**Modèle** : stockage et recherche de vecteurs d'embedding (représentations numériques haute dimension de textes, images, sons). Optimisé pour la recherche par similarité (ANN — Approximate Nearest Neighbor).

**Pourquoi les bases vectorielles sont essentielles pour l'IA :**
- Les LLMs (GPT, Llama, Gemini) produisent des embeddings vectoriels pour représenter la sémantique des textes.
- La recherche vectorielle permet le **RAG (Retrieval-Augmented Generation)** : enrichissement des réponses d'un LLM avec des documents pertinents retrouvés par similarité sémantique.
- Remplace la recherche par mot-clé (TF-IDF, BM25) par une recherche par sens.

**Solutions principales :**

| Solution | Type | Points forts |
|----------|------|--------------|
| **Pinecone** | SaaS managé | Simplicité, performance, intégration LLM |
| **Weaviate** | Open-source / Cloud | Multi-modal, modules IA intégrés |
| **Qdrant** | Open-source (Rust) | Performance, filtrage avancé |
| **Milvus** | Open-source | Scale, LF AI Foundation |
| **Chroma** | Open-source (Python) | Idéal pour le prototypage IA |
| **pgvector** | Extension PostgreSQL | Intégration dans une BDD existante |
| **Redis Stack** | Extension Redis | Faible latence, ecosystème Redis |

**Algorithmes ANN courants :** HNSW (Hierarchical Navigable Small World), IVF (Inverted File Index), ScaNN (Google).

#### Tableau comparatif des familles NoSQL

| Famille | Modèle | Cas d'usage | Exemple |
|---------|--------|-------------|---------|
| Documentaire | JSON/BSON | Catalogues, profils, CMS | MongoDB, CouchDB |
| Clé-valeur | Clé → valeur | Cache, sessions, temps réel | Redis, DynamoDB |
| Colonnes larges | Colonnes par ligne | IoT, séries temporelles, logs | Cassandra, HBase |
| Graphe | Nœuds + arêtes | Fraude, réseaux sociaux, IAM | Neo4j, Neptune |
| Vectorielle | Vecteurs d'embedding | RAG, recherche sémantique, IA | Pinecone, Weaviate |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Scalabilité horizontale native | Absence de jointures complexes (selon le type) |
| Flexibilité du schéma | Cohérence éventuelle (BASE) vs ACID relationnel |
| Performances élevées pour des patterns d'accès spécifiques | Nécessite une modélisation guidée par les requêtes |
| Haute disponibilité, tolérance aux pannes | Écosystème plus fragmenté, moins de compétences disponibles |
| Adapté aux données non structurées et semi-structurées | Migration et évolution de schéma parfois délicates |
| Langages de requête adaptés à chaque modèle | Pas de standard universel (contrairement à SQL) |

### Acteurs et solutions du marché

- **Cloud managé** : MongoDB Atlas, Amazon DynamoDB, Google Firestore, Amazon Neptune, Google Bigtable, Amazon MemoryDB (Redis).
- **Open-source** : MongoDB Community, Redis, Apache Cassandra, Neo4j Community, Weaviate, Milvus, Qdrant.
- **Multi-modèle** : ArangoDB, Couchbase, FaunaDB.
- **Vectorielle SaaS** : Pinecone, Weaviate Cloud, Zilliz Cloud (Milvus).

### Cas d'usage concrets

1. **Discord — Cassandra pour les messages** : Discord stocke des milliards de messages sur Apache Cassandra. La base gère des millions d'écritures par seconde avec une disponibilité 99,99 % en exploitant la réplication multi-datacenter de Cassandra. En 2023, Discord a migré une partie vers ScyllaDB (compatible Cassandra, plus performant).

2. **Amazon — DynamoDB à l'échelle mondiale** : Le Prime Day 2023 a généré un pic de **89,2 millions de requêtes par seconde** sur DynamoDB. La base gère en temps réel les paniers, sessions et états de commande de centaines de millions de clients.

3. **LinkedIn — Détection de fraude avec Neo4j** : LinkedIn utilise un graphe de connexions pour détecter les comptes frauduleux, faux profils et spammeurs en analysant les patterns de connexions et les communautés suspectes dans le graphe de son réseau social.

### Chiffres et tendances

- **Redis** est la base de données la plus populaire pour le caching, utilisée par plus de **40 % des entreprises** du Fortune 500.
- **Cassandra** gère **Instagram** : plus de 1 milliard d'actifs mensuels, des milliards de photos.
- Les bases vectorielles ont connu une croissance de **10x** en nombre de déploiements entre 2022 et 2024 (Gartner, 2024).
- Tendance : **convergence** des bases de données (PostgreSQL + pgvector, Redis Stack, MongoDB Atlas Vector Search) → les bases relationnelles et NoSQL absorbent les fonctionnalités vectorielles.

## Flashcards
#flashcards/Big_DATA/Bases_NoSQL #flashcards/IA/Bases_NoSQL

Quelles sont les 5 grandes familles de bases NoSQL ? :: Documentaire (MongoDB), Clé-valeur (Redis, DynamoDB), Colonnes larges (Cassandra, HBase), Graphe (Neo4j, Neptune), Vectorielle (Pinecone, Weaviate, Qdrant).

Qu'est-ce que le théorème CAP ? :: Un système distribué ne peut garantir simultanément que 2 des 3 propriétés : Consistency (cohérence), Availability (disponibilité), Partition tolerance (tolérance au partitionnement réseau).

Quelle est la différence entre ACID et BASE ? :: ACID (transactions relationnelles) : Atomicité, Cohérence, Isolation, Durabilité — garanties fortes. BASE (NoSQL distribué) : Basically Available, Soft state, Eventually consistent — cohérence éventuelle acceptée pour la scalabilité.

Pourquoi Cassandra n'a-t-elle pas de maître (SPOF) ? :: Architecture peer-to-peer : tous les nœuds sont identiques. Les données sont distribuées par consistent hashing. L'absence de maître unique élimine le Single Point of Failure et facilite la scalabilité horizontale.

Qu'est-ce qu'une base vectorielle et à quoi sert-elle ? :: Base optimisée pour stocker et rechercher des vecteurs d'embedding (représentations numériques haute dimension). Utilisée pour la recherche sémantique et le RAG (Retrieval-Augmented Generation) avec les LLMs.

Quel est le langage de requête de Neo4j ? :: Cypher : langage déclaratif de requête de graphes. Exemple : MATCH (a:Person)-[:KNOWS]->(b:Person) WHERE a.name='Alice' RETURN b.

Qu'est-ce que Redis et quels sont ses principaux cas d'usage ? :: Base clé-valeur in-memory, latence sub-milliseconde. Cas d'usage : cache applicatif, gestion de sessions, leaderboards, pub/sub, files de messages, compteurs temps réel.

## Sources

- MarketsandMarkets, *NoSQL Database Market Report*, 2023.
- MongoDB, *Annual Report FY2024*.
- Gartner, *Hype Cycle for Data Management*, 2024.
- Brewer, E., *Towards Robust Distributed Systems (CAP Theorem)*, PODC 2000.
- Discord Engineering Blog, *How Discord Stores Billions of Messages*, 2023.
- AWS, *DynamoDB at Amazon Prime Day*, 2023.

## Notions liées

- [[Big Data — fondamentaux]]
- [[Data Lake - Data Warehouse - Lakehouse]]
- [[Écosystème Hadoop - Spark - Kafka]]
- [[Plateformes cloud Big Data]]
- [[IA en cybersécurité]]
- [[ETL - ELT et pipelines de données]]
