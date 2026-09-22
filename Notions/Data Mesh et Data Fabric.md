---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Data Mesh et Data Fabric

![[N — Data Mesh et Data Fabric.mp3]]
## En bref
> **Définition** : Le **Data Mesh** est une architecture de données décentralisée introduite par Zhamak Dehghani (2019), où chaque domaine métier est responsable de la production, de la qualité et de la publication de ses propres données comme des produits. Le **Data Fabric** est une architecture complémentaire, davantage centrée sur une couche d'intégration intelligente et automatisée (pilotée par l'IA et les métadonnées) qui connecte les données où qu'elles se trouvent. Le **Data-as-a-Service (DaaS)** est le modèle de consommation des données via API, comme des services.
> **Pourquoi c'est important** : Les architectures data centralisées (data lake monolithique, data warehouse unique) atteignent leurs limites à grande échelle : goulot d'étranglement de l'équipe centrale, délais de mise à disposition des données, silos persistants. Data Mesh et Data Fabric proposent deux réponses à ce défi.
> **Chiffres clés** :
> - **72 % des organisations** signalent que leur équipe data centrale est un goulot d'étranglement (Gartner, 2023)
> - L'adoption du Data Mesh a augmenté de **+400 % entre 2021 et 2024** dans les grandes entreprises (ThoughtWorks)
> - Le marché du Data Fabric atteindra **5,9 Md$** en 2027, croissance de **+25 % par an** (MarketsandMarkets)

## Approfondir

### Fonctionnement

#### Les limites des architectures centralisées

**Data Lake centralisé — problèmes** :
- L'équipe data centrale est responsable de l'ingestion de toutes les sources → backlog infini
- Les équipes métier attendent des semaines pour que leurs données soient disponibles
- La qualité des données est mal assurée car l'équipe centrale ne connaît pas le contexte métier
- Résultat : le data lake devient un "data swamp" (marécage de données)

**Symptômes organisationnels** :
- Équipes data surchargées, équipes métier frustrées
- Données de mauvaise qualité car produites par des gens qui ne comprennent pas le métier
- Silos persistants malgré la centralisation technique

#### Data Mesh — les 4 principes fondamentaux (Zhamak Dehghani)

**Principe 1 : Ownership orienté domaine (Domain Ownership)**
Chaque domaine métier (ex. : Commandes, Clients, Finance, Logistique) est responsable de ses propres données. L'équipe du domaine produit, maintient et publie ses données.

```
Domaine Commandes      Domaine Clients       Domaine Finance
   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
   │ Data product│       │ Data product│       │ Data product│
   │ "Commandes" │       │ "Clients"   │       │ "Revenus"   │
   └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
          │                     │                     │
          └─────────────────────┴─────────────────────┘
                         Consommateurs
```

**Principe 2 : Données comme produit (Data as a Product)**
Les données ne sont plus un sous-produit des applications. Elles sont traitées comme des produits avec :
- Une interface stable et documentée (API, schéma versionnné)
- Un SLA de qualité (fraîcheur, complétude, exactitude)
- Un propriétaire (data product owner)
- Des "utilisateurs" et un feedback
- Un data contract formel

**Principe 3 : Infrastructure en libre-service (Self-serve Data Infrastructure)**
Une plateforme data centrale fournit les outils dont les équipes domaines ont besoin pour produire et consommer des données sans friction :
- Ingestion, transformation, stockage
- Catalog, lineage, monitoring qualité
- Sécurité et accès
- Déploiement des data products

**Principe 4 : Gouvernance fédérée (Federated Computational Governance)**
Standards communs définis centralement (schémas, formats, sécurité, RGPD) mais appliqués de manière décentralisée dans chaque domaine. Gouvernance "as code" : les règles sont des configurations automatisées, pas des processus manuels.

#### Data Fabric — l'architecture pilotée par les métadonnées

Le Data Fabric est une couche d'abstraction intelligente qui connecte, découvre et intègre automatiquement les données de sources hétérogènes, partout où elles se trouvent (on-premise, multi-cloud, edge).

**Caractéristiques clés** :
- **Knowledge Graph** : graphe de métadonnées décrivant toutes les données de l'organisation et leurs relations
- **Active Metadata** : métadonnées actives qui alimentent l'IA pour automatiser l'intégration, la qualité et la découverte
- **Intégration universelle** : connecteurs vers toutes les sources (SQL, NoSQL, API, fichiers, streaming)
- **IA-driven** : recommandations automatiques de jointures, détection de similarités, curation des données

**Différence avec le Data Mesh** :

| Critère | Data Mesh | Data Fabric |
|---------|-----------|-------------|
| Approche | Organisationnelle et architecturale | Technologique |
| Gouvernance | Décentralisée par domaine | Centralisée par la couche fabric |
| Pilotage | Par les équipes domaines (humains) | Par les métadonnées et l'IA |
| Scalabilité | Scalabilité organisationnelle | Scalabilité technique |
| Complémentarité | Peuvent coexister | Peuvent coexister |

#### Data-as-a-Service (DaaS)
Modèle de consommation où les données sont exposées via des API standardisées, consommables par n'importe quel applicatif ou outil, comme un service cloud.

**Caractéristiques** :
- API REST ou GraphQL
- Contrat d'interface versionné (data contract)
- SLA défini (disponibilité, fraîcheur)
- Facturation à l'usage possible (interne ou externe)

**Exemples** :
- INSEE Open Data : données statistiques françaises via API
- SIRENE API (données entreprises)
- Refinitiv / Bloomberg : données financières via API (payant)
- Interne : une équipe Finance expose ses données de revenus via API pour toute l'organisation

#### Implémentation concrète d'un Data Mesh

**Stack technologique typique** :
- **Catalogue et discovery** : DataHub (LinkedIn), Atlan
- **Transformation** : dbt (data build tool)
- **Storage** : Delta Lake (Databricks), Apache Iceberg, Apache Hudi
- **Orchestration** : Apache Airflow, Prefect
- **Streaming** : Apache Kafka
- **Data contracts** : YAML + Git + Great Expectations
- **Plateforme** : Databricks Data Intelligence Platform, Starburst, Dremio

### Avantages / Inconvénients

| Data Mesh | |
|---|---|
| **Avantages** | **Inconvénients** |
| Scalabilité organisationnelle : chaque domaine évolue indépendamment | Complexité organisationnelle : nécessite une culture data forte dans chaque domaine |
| Meilleure qualité des données (équipes qui connaissent le contexte) | Coût de la plateforme libre-service (investissement initial élevé) |
| Réduction du backlog de l'équipe data centrale | Risque de fragmentation si la gouvernance fédérée est insuffisante |
| Time-to-data réduit pour les équipes métier | Nécessite des data engineers dans chaque équipe domaine |

| Data Fabric | |
|---|---|
| **Avantages** | **Inconvénients** |
| Intégration transparente de sources hétérogènes | Dépendance forte aux outils des éditeurs (vendor lock-in) |
| Découverte automatique des données | Complexité de la mise en place du knowledge graph |
| Réduit le temps d'intégration de nouvelles sources | Coût élevé des plateformes Data Fabric commerciales |

### Acteurs et solutions du marché
- **Databricks** : Data Intelligence Platform (lakehouse + data mesh)
- **Starburst** : Data Mesh platform basée sur Trino (SQL sur toutes sources)
- **Dremio** : Data lakehouse, SQL sur data lake, approche Data Fabric
- **Informatica** : IDMC (Data Fabric avec active metadata)
- **IBM** : Watson Knowledge Catalog (Data Fabric)
- **Talend** : intégration de données + gouvernance (Data Fabric)
- **DataHub** : open source LinkedIn, catalogue et lineage pour data mesh
- **dbt Labs** : transformation de données, colonne vertébrale du data mesh moderne

### Cas d'usage concrets
1. **Netflix** est l'un des pionniers du data mesh (avant même le terme). Chaque équipe produit possède ses données (recommandations, streaming quality, financials) et les expose comme des produits stables consommés par d'autres équipes. La plateforme Metacat centralise le catalogue.
2. **Intesa Sanpaolo** (3ème banque européenne) a déployé un Data Mesh sur 12 domaines métier (retail banking, corporate, risk, compliance...). Chaque domaine a son data product owner et publie ses données via une plateforme Databricks commune. Résultat : le time-to-data est passé de 6 semaines à 3 jours.
3. **Michelin** a choisi une approche Data Fabric (IBM Watson Knowledge Catalog) pour connecter ses 70 usines mondiales sans refactoriser les systèmes legacy. L'IA du fabric découvre et mappe automatiquement les données industrielles hétérogènes.

### Chiffres et tendances
- **Gartner** prédit que d'ici 2026, **25 % des grandes entreprises** auront adopté une architecture data mesh ou fabric (vs 5 % en 2022)
- **dbt** est utilisé par **40 000 entreprises** dans le monde (2024), devenu l'outil standard de transformation dans les data stacks modernes
- **Delta Lake** (Databricks) a dépassé **10 000 milliards de tables** gérées dans le monde
- L'approche **lakehouse** (data lake + data warehouse) tend à remplacer l'opposition traditionnelle lake vs warehouse

## Flashcards
#flashcards/Big_DATA/Data_Mesh_et_Data_Fabric

Quels sont les 4 principes fondamentaux du Data Mesh selon Zhamak Dehghani ? :: 1) Domain Ownership (chaque domaine possède ses données), 2) Data as a Product (données traitées comme des produits avec SLA et contrats), 3) Self-serve Data Infrastructure (plateforme commune en libre-service), 4) Federated Computational Governance (standards centraux appliqués décentralisés).

Quelle est la différence entre Data Mesh et Data Fabric ? :: Data Mesh est une approche organisationnelle et architecturale qui décentralise la responsabilité des données vers les domaines métier. Data Fabric est une approche technologique qui crée une couche d'intégration intelligente pilotée par les métadonnées et l'IA. Les deux peuvent coexister dans une même organisation.

Pourquoi les data lakes centralisés deviennent-ils des "data swamps" ? :: Car l'équipe centrale ne peut pas traiter tous les flux d'ingestion à temps (backlog), ne connaît pas le contexte métier pour assurer la qualité, et la prolifération de données non documentées et non maintenues rend le lake inutilisable. Résultat : données de mauvaise qualité, documentation absente, confiance inexistante.

Qu'est-ce qu'un "data product" dans le contexte du Data Mesh ? :: Un data product est un ensemble de données traité comme un produit : interface stable et documentée (API/schéma versionné), SLA de qualité défini (fraîcheur, complétude), data contract formel, propriétaire (data product owner) identifié, et utilisateurs avec système de feedback. Le domaine propriétaire en est entièrement responsable.

Qu'est-ce que le DaaS (Data-as-a-Service) ? :: Modèle de consommation où les données sont exposées via des API standardisées (REST, GraphQL), consommables par n'importe quel outil ou applicatif, avec un SLA défini. Permet une consommation découplée des données, indépendante de l'architecture de stockage sous-jacente.

Quel est le rôle de dbt dans un data mesh ? :: dbt (data build tool) est l'outil de transformation SQL qui permet de construire et tester les data products. Il versione les transformations dans Git, génère la documentation et le lineage automatiquement, et permet des tests de qualité sur les données. Il est la colonne vertébrale de la transformation dans les architectures data modernes.

Qu'est-ce que la "gouvernance fédérée" dans le Data Mesh ? :: Standards communs définis centralement (formats, schémas, règles RGPD, sécurité) mais appliqués de manière autonome dans chaque domaine. La gouvernance est "as code" : des configurations automatisées plutôt que des processus manuels. Elle garantit l'interopérabilité entre domaines tout en préservant leur autonomie.

## Sources
- Zhamak Dehghani – "Data Mesh" (O'Reilly, 2022)
- ThoughtWorks – "Data Mesh Principles and Logical Architecture" : https://martinfowler.com/articles/data-mesh-principles.html
- Databricks – "The Data Lakehouse Platform" : https://www.databricks.com
- Gartner – "Innovation Insight for Data Fabric" : https://www.gartner.com
- dbt Labs – Documentation officielle : https://docs.getdbt.com
- Starburst – "Data Mesh in Practice" : https://www.starburst.io

## Notions liées
- [[Data Governance]]
- [[Business Intelligence (BI)]]
- [[Data Maturity et Data Literacy]]
- [[Infrastructure de stockage (SAN - NAS - HCI)]]
- [[Data Lifecycle Management]]
