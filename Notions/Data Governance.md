---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Data Governance

## En bref
> **Définition** : La Data Governance (gouvernance des données) désigne l'ensemble des politiques, processus, rôles et standards qui garantissent que les données d'une organisation sont fiables, sécurisées, conformes et utilisables. Elle couvre la qualité des données, leur traçabilité (lineage), leur catalogage, les contrats de données et la gestion des données maîtres (MDM).
> **Pourquoi c'est important** : Sans gouvernance, les organisations souffrent de données incohérentes entre systèmes, de silos, de non-conformité RGPD et de décisions prises sur des données erronées. Une étude IBM estime que la mauvaise qualité des données coûte **3 100 Md$** par an à l'économie américaine.
> **Chiffres clés** :
> - **60 % des projets Big Data** échouent à cause de problèmes de qualité de données (Gartner)
> - **2,5 Md$ de pertes** annuelles pour les entreprises du Fortune 1000 liées aux mauvaises données (IBM)
> - Seulement **27 % des entreprises** se déclarent "data-driven" avec une gouvernance mature (NewVantage Partners, 2023)

## Approfondir

### Fonctionnement

#### Les piliers de la Data Governance

**1. Data Quality (qualité des données)**
Ensemble de dimensions mesurant la fiabilité d'une donnée :
- **Exactitude** : la donnée reflète la réalité (ex. : adresse client correcte)
- **Complétude** : absence de valeurs manquantes
- **Cohérence** : même valeur dans tous les systèmes (ex. : même CA dans l'ERP et le datawarehouse)
- **Actualité (Freshness)** : donnée à jour selon la fréquence attendue
- **Unicité** : absence de doublons
- **Validité** : respect des formats et règles métier (ex. : SIREN à 9 chiffres)

Outils : **Great Expectations** (open source), **Soda**, **Monte Carlo** (data observability)

**2. Data Lineage (traçabilité des données)**
Capacité à tracer l'origine d'une donnée, ses transformations et ses destinations tout au long de son cycle de vie.

```
Source (ERP SAP) → ETL (Talend) → Data Warehouse → Rapport Power BI
     ↑ quelle table ?   ↑ quelles règles ?   ↑ quelle agrégation ?
```

Utilité :
- Débogage : identifier d'où vient une valeur erronée dans un rapport
- Conformité RGPD : savoir où transitent les données personnelles
- Impact analysis : avant de modifier une table source, identifier tous les rapports impactés

Outils : **Apache Atlas**, **OpenLineage**, **Marquez**, intégré dans Alation et Collibra

**3. Data Catalog (catalogue de données)**
Inventaire centralisé de tous les actifs de données d'une organisation, avec leurs métadonnées techniques et métier.

Un data catalog contient :
- Description métier des tables et colonnes ("que contient ce champ ?")
- Propriétaire de la donnée (data owner)
- Classification (donnée sensible, personnelle, publique…)
- Lineage automatiquement tracé
- Popularité (qui utilise cette donnée ?)
- Glossaire métier unifié

**Principaux acteurs** :
| Outil | Positionnement |
|-------|---------------|
| **Alation** | Leader data catalog entreprise, fort sur la découverte et la collaboration |
| **Collibra** | Leader data governance, axé conformité et data stewardship |
| **Atlan** | Challenger moderne, UX collaborative type Notion |
| **Apache Atlas** | Open source, intégré à l'écosystème Hadoop |
| **Microsoft Purview** | Solution Microsoft, intégrée Azure Data Factory / Synapse |
| **DataHub** | Open source créé par LinkedIn, très adopté dans les data mesh |

**4. Data Contracts (contrats de données)**
Accord formel entre le producteur et le consommateur d'une donnée, spécifiant :
- Schéma (noms de colonnes, types)
- SLA de fraîcheur (ex. : mise à jour toutes les heures)
- Règles de qualité attendues
- Responsabilités en cas de rupture

Concept popularisé par Mehdi Ouazza (2022), très utilisé dans les architectures data mesh. Implémentation : fichiers YAML versionnés dans Git.

**5. Master Data Management (MDM)**
Gestion des données de référence partagées par tous les systèmes de l'entreprise : clients, produits, fournisseurs, employés, géographies.

Problème : un même client peut avoir 3 enregistrements différents dans le CRM, l'ERP et l'e-commerce. Le MDM crée un **"Golden Record"** unique, faisant autorité pour toute l'organisation.

Acteurs : **Informatica MDM**, **Stibo Systems**, **IBM InfoSphere**, **Semarchy**

#### Rôles de la gouvernance des données
| Rôle | Responsabilité |
|------|---------------|
| **Chief Data Officer (CDO)** | Stratégie data globale de l'organisation |
| **Data Owner** | Responsable métier d'un domaine de données |
| **Data Steward** | Garant opérationnel de la qualité et des règles de gouvernance |
| **Data Engineer** | Implémentation technique des pipelines et règles de qualité |
| **Data Consumer** | Utilisateur final des données (analyste, data scientist) |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Décisions basées sur des données fiables et cohérentes | Mise en place longue et coûteuse (18-36 mois pour une gouvernance mature) |
| Conformité RGPD et réglementaire assurée | Résistance organisationnelle (politique des données, propriété des silos) |
| Réduction du temps passé à déboguer des données | Risque de bureaucratie excessive ("gouvernance pour la gouvernance") |
| Meilleure collaboration entre équipes métier et IT | Nécessite un sponsorship C-level fort (CDO) |
| Valorisation du patrimoine data de l'entreprise | Outils coûteux (Collibra, Alation : plusieurs centaines de k€/an) |

### Acteurs et solutions du marché
- **Collibra** : plateforme de data governance leader, forte sur data stewardship et conformité
- **Alation** : data catalog avec IA pour la découverte automatique des données
- **Informatica** : IDMC (Intelligent Data Management Cloud), MDM et qualité
- **Microsoft Purview** : gouvernance intégrée à l'écosystème Azure
- **Atlan** : data catalog nouvelle génération, UX moderne
- **DataHub** : open source LinkedIn, très populaire dans les startups data
- **Great Expectations** : open source, tests de qualité de données dans les pipelines

### Cas d'usage concrets
1. **Société Générale** a déployé Collibra pour gouverner ses données réglementaires (BCBS 239, FRTB). Le data catalog recense plus de 500 000 actifs de données avec leur lineage complet, permettant de répondre aux exigences de reporting prudentiel en heures plutôt qu'en semaines.
2. **Carrefour** a mis en place un MDM produit unifiant les données de 40 pays sur une référence unique. Avant le MDM, un même article pouvait avoir 15 références différentes selon les systèmes locaux — problème critique pour l'e-commerce omnicanal.
3. **Airbus** utilise Apache Atlas pour tracer le lineage de ses données de production aéronautique, soumises aux exigences de traçabilité de l'EASA sur 30 ans.

### Chiffres et tendances
- Le marché de la data governance pèse **5,3 Md$ en 2024**, croissance de **+22 % par an** (MarketsandMarkets)
- **73 % des données** d'une entreprise ne sont jamais analysées faute de catalogage (Forrester)
- Les entreprises avec une gouvernance mature ont un ROI data **3,5x supérieur** aux autres (McKinsey)
- L'adoption des data contracts croît de **+300 %** par an dans les communautés data engineering (2023-2024)

## Flashcards
#flashcards

Quelles sont les 6 dimensions de la qualité des données ? :: Exactitude (reflète la réalité), Complétude (pas de valeurs manquantes), Cohérence (même valeur dans tous les systèmes), Actualité/Freshness (donnée à jour), Unicité (pas de doublons), Validité (respect des formats et règles métier).

Qu'est-ce que le data lineage et à quoi sert-il ? :: Traçabilité de l'origine d'une donnée, ses transformations et destinations. Utilisé pour déboguer des valeurs erronées dans les rapports, assurer la conformité RGPD (traçage des données personnelles) et réaliser des analyses d'impact avant modification d'une source.

Quelle est la différence entre Alation et Collibra ? :: Alation est centré sur la découverte et la collaboration autour des données (data catalog). Collibra est davantage orienté gouvernance formelle et conformité (data stewardship, politiques, conformité réglementaire). Les deux sont leaders du marché sur des positionnements complémentaires.

Qu'est-ce qu'un data contract ? :: Accord formel (fichier YAML versionné en Git) entre le producteur et le consommateur d'une donnée, spécifiant le schéma, le SLA de fraîcheur, les règles de qualité et les responsabilités. Concept clé du data mesh pour garantir la fiabilité des données entre domaines.

Qu'est-ce que le MDM (Master Data Management) et quel problème résout-il ? :: Gestion des données de référence partagées (clients, produits, fournisseurs). Il résout le problème des "golden records" : un même client peut avoir plusieurs enregistrements incohérents dans différents systèmes. Le MDM crée une référence unique faisant autorité pour toute l'organisation.

Quel est le rôle du Data Steward ? :: Garant opérationnel de la qualité des données et de l'application des règles de gouvernance dans un domaine métier. Intermédiaire entre les équipes métier (data owner) et les équipes techniques (data engineers). Acteur clé du programme de gouvernance au quotidien.

Pourquoi 60 % des projets Big Data échouent-ils selon Gartner ? :: Principalement à cause de problèmes de qualité et de gouvernance des données : données incohérentes entre systèmes, silos non réconciliés, absence de définitions communes des métriques métier, et manque de confiance des utilisateurs dans les données.

## Sources
- Gartner – "Data Quality Market Guide" : https://www.gartner.com
- IBM – "The Cost of Bad Data" : https://www.ibm.com
- Collibra – Documentation officielle : https://docs.collibra.com
- Alation – "State of Data Culture" : https://www.alation.com
- Mehdi Ouazza – "Data Contracts" (blog) : https://medium.com/@mehdiouss_a
- NewVantage Partners – "Big Data and AI Executive Survey 2023" : https://www.newvantage.com

## Notions liées
- [[Data Lifecycle Management]]
- [[Data Maturity et Data Literacy]]
- [[Data Mesh et Data Fabric]]
- [[CLOUD Act et transferts de données]]
- [[Types d'analytics]]
