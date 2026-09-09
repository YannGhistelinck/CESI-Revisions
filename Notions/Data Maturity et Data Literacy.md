---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Data Maturity et Data Literacy

## En bref
> **Définition** : Le **data maturity model** est un cadre d'évaluation du niveau de maturité d'une organisation dans son usage des données, allant de la collecte basique à l'optimisation pilotée par l'IA. La **data literacy** désigne la capacité des collaborateurs à lire, comprendre, questionner et communiquer avec des données. La **data democratization** vise à rendre les données accessibles à tous, au-delà des seules équipes IT. Les **silos de données** sont l'obstacle principal à cet objectif.
> **Pourquoi c'est important** : Une organisation avec une faible maturité data prend des décisions sur l'intuition plutôt que sur les faits. Seules les organisations atteignant les niveaux supérieurs de maturité tirent un avantage concurrentiel durable de leurs données.
> **Chiffres clés** :
> - Seulement **26 % des organisations** sont considérées comme "data-driven" avec une maturité avancée (Forrester, 2023)
> - **74 % des employés** déclarent se sentir dépassés ou anxieux face aux données (Qlik Data Literacy Report)
> - Les entreprises avec une forte data literacy ont une valorisation boursière **3 à 5 % supérieure** à leurs pairs (Gartner)

## Approfondir

### Fonctionnement

#### Les modèles de maturité data

Plusieurs frameworks coexistent ; les plus utilisés sont :

**1. Le modèle Gartner (5 niveaux)**
```
Niveau 1 : Aware      → On reconnaît que les données ont de la valeur
Niveau 2 : Reactive   → On exploite les données quand un problème survient
Niveau 3 : Proactive  → On anticipe avec les données (rapports réguliers, KPIs)
Niveau 4 : Managed    → Gouvernance formelle, qualité mesurée, culture data établie
Niveau 5 : Effective  → Données au cœur de chaque décision, IA et ML opérationnels
```

**2. Le modèle DCAM (Data Management Capability Assessment Model)**
Framework de l'EDM Council, très utilisé dans la finance et les industries régulées. Évalue 8 capacités : stratégie data, architecture, qualité, gouvernance, opérations, technologie, organisation, communication.

**3. Le modèle en 5 stades de Harvard Business Review**
- Stade 1 : Data-resistant (rejet des données)
- Stade 2 : Data-informed (données utilisées ponctuellement)
- Stade 3 : Data-driven (données utilisées systématiquement)
- Stade 4 : Data-predictive (usage de modèles prédictifs)
- Stade 5 : Data-autonomous (décisions automatisées pilotées par IA)

#### Data Literacy — la littératie des données

**Définition** : Capacité à lire, comprendre, questionner, créer et communiquer avec des données dans leur contexte.

**Les 4 niveaux de data literacy** :
| Niveau | Compétence |
|--------|------------|
| **Basique** | Lire un graphique, interpréter un tableau, comprendre une moyenne |
| **Intermédiaire** | Identifier un biais dans une visualisation, comprendre une corrélation vs causalité |
| **Avancé** | Réaliser des analyses exploratoires (SQL, Excel avancé, Power BI) |
| **Expert** | Modélisation statistique, machine learning, ingénierie des données |

**Principaux déficits de data literacy** observés en entreprise :
- Confusion entre corrélation et causalité
- Interprétation erronée des probabilités (ex. : taux de faux positifs)
- Surconfiance dans les visualisations (biais visuels)
- Ignorance des limites des modèles (garbage in, garbage out)

**Programmes de formation** : Coursera Data Literacy, Tableau Blueprint, programmes internes (SNCF Data Academy, Engie Data Campus)

#### Data Democratization — la démocratisation des données

**Objectif** : Rendre les données accessibles, compréhensibles et utilisables par tous les collaborateurs, pas seulement les data scientists ou les équipes IT.

**Leviers** :
- **Self-service BI** : outils permettant aux métiers de créer leurs propres rapports sans l'IT (Power BI, Tableau, Looker)
- **Data catalog** : inventaire des données disponibles avec descriptions métier
- **Data mesh** : architecture décentralisée où chaque domaine produit et gère ses propres données
- **Formation** : programmes de data literacy à l'échelle de l'organisation

**Risques** de la démocratisation non maîtrisée :
- Prolifération de rapports contradictoires ("chiffres différents selon qui les calcule")
- Violations de confidentialité si les accès ne sont pas correctement gérés
- "Analyse paralysis" : trop de données sans cadre de décision

#### Silos de données — le principal obstacle

**Définition** : Ensemble de données isolé dans un système ou une équipe, non accessible ou non partagé avec le reste de l'organisation.

**Causes** :
- Organisations structurées par fonctions (finance, RH, marketing, ops) avec leurs propres outils
- Systèmes applicatifs non intégrés (legacy, acquisitions)
- Culture de rétention de l'information (pouvoir informationnel)
- Absence d'architecture data transverse

**Conséquences** :
- Visions fragmentées du client (CRM ≠ ERP ≠ e-commerce)
- Impossibilité de croiser les données pour des analyses avancées
- Duplication des efforts de collecte et de transformation
- Méfiance entre équipes

**Solutions** : ETL/ELT centralisé, data warehouse unifié, data lake, data mesh (décentralisation avec standards communs)

#### Roadmap de montée en maturité data
```
Étape 1 : Audit de l'existant (cartographie des données, des outils, des usages)
Étape 2 : Définir une stratégie data avec sponsorship C-level (CDO)
Étape 3 : Construire les fondations (data platform, gouvernance, data catalog)
Étape 4 : Former les équipes (data literacy programs)
Étape 5 : Déployer le self-service (BI accessible aux métiers)
Étape 6 : Analytics avancé et IA
```

### Avantages / Inconvénients

| Avantages d'une haute maturité data | Obstacles à la progression |
|-------------------------------------|---------------------------|
| Décisions plus rapides et mieux fondées | Investissements initiaux élevés (plateforme, formation, gouvernance) |
| Avantage concurrentiel durable | Résistance culturelle des silos |
| Réduction des erreurs liées aux données | Nécessite un CDO et un sponsorship C-level |
| Meilleure conformité réglementaire | Temps long (3-5 ans pour atteindre la maturité avancée) |
| Capacité à déployer l'IA et le ML | Manque de talents data literacy à tous les niveaux |

### Acteurs et solutions du marché
- **Gartner** : Data & Analytics Maturity Model, référence pour les assessments
- **EDM Council** : DCAM, référence secteur financier
- **Qlik** : éditeur du "Data Literacy Index", programmes de formation associés
- **Dataiku** : plateforme visant à démocratiser l'accès à l'IA/ML pour les non-experts
- **Tableau Blueprint** : méthodologie et programme de formation à la data literacy
- **Coursera / DataCamp** : formations data literacy en ligne
- **SNCF Data Academy** : programme interne emblématique de data literacy à grande échelle

### Cas d'usage concrets
1. **SNCF** a lancé la "Data Academy" pour former 10 000 collaborateurs à la data literacy en 3 ans. L'objectif : que chaque manager puisse lire et questionner un tableau de bord Power BI sans intermédiaire IT. Résultat : réduction de 40 % des demandes de rapports ad hoc adressées à la DSI.
2. **ING Bank** est souvent citée comme exemple de maturité data niveau 5 : chaque décision de crédit, de tarification produit et de recommandation client est pilotée par des modèles ML en production, sans intervention humaine systématique.
3. **Michelin** a conduit un audit de maturité data (DCAM) révélant que 80 % de ses données industrielles étaient enfermées dans des silos usines. Un programme de 3 ans a permis de centraliser ces données sur une plateforme Azure unifiée, rendant possible l'analyse prédictive de la qualité de production.

### Chiffres et tendances
- Le marché de la data literacy formation atteindra **8,1 Md$** en 2026 (Allied Market Research)
- **67 % des décideurs** estiment que leurs collaborateurs ne sont pas suffisamment à l'aise avec les données pour les utiliser efficacement (Accenture)
- Les organisations data-driven ont **23 fois plus de chances** d'acquérir de nouveaux clients (McKinsey)
- La pandémie COVID a accéléré la prise de conscience : 78 % des CDO ont vu leur budget augmenter post-2020 (NewVantage Partners)

## Flashcards
#flashcards

Quels sont les 5 niveaux du modèle de maturité data Gartner ? :: Aware (reconnaissance de la valeur des données), Reactive (exploitation sur problème), Proactive (anticipation, KPIs réguliers), Managed (gouvernance formelle, qualité mesurée), Effective (IA/ML opérationnels, données au cœur de chaque décision).

Que signifie "data literacy" et pourquoi est-ce stratégique ? :: Capacité à lire, comprendre, questionner et communiquer avec des données. Stratégique car sans data literacy, les collaborateurs ne peuvent pas exploiter les investissements en data/BI, et les décisions restent basées sur l'intuition plutôt que les faits.

Qu'est-ce qu'un silo de données et quelles en sont les causes principales ? :: Ensemble de données isolé dans un système ou une équipe, non partagé avec le reste de l'organisation. Causes : organisations fonctionnelles avec leurs propres outils, systèmes non intégrés (legacy), culture de rétention de l'information, absence d'architecture data transverse.

Quelle est la différence entre être "data-informed" et "data-driven" ? :: Data-informed : les données sont consultées ponctuellement pour éclairer une décision, mais l'intuition reste prépondérante. Data-driven : les données sont systématiquement au cœur de chaque décision, avec des processus formels de collecte, analyse et reporting.

Comment la data democratization peut-elle devenir un risque ? :: En l'absence de gouvernance, elle produit des rapports contradictoires (chiffres différents selon la source), des violations de confidentialité (mauvais contrôle des accès) et une "analysis paralysis" (trop de données sans cadre de décision).

Qu'est-ce que le DCAM et dans quel secteur est-il principalement utilisé ? :: Data Management Capability Assessment Model, framework de l'EDM Council évaluant 8 capacités (stratégie, architecture, qualité, gouvernance...). Principalement utilisé dans le secteur financier et les industries régulées pour évaluer et améliorer la maturité data.

Quel est l'obstacle culturel principal à la montée en maturité data des organisations ? :: La résistance des silos organisationnels : les équipes et départements gardent "leurs" données comme source de pouvoir informationnel. Cela nécessite un changement culturel profond et un sponsorship au niveau C-suite (CDO, DG) pour être surmonté.

## Sources
- Gartner – "Data & Analytics Maturity Model" : https://www.gartner.com
- Forrester – "The Data-Driven Enterprise" : https://www.forrester.com
- Qlik – "Data Literacy Index" : https://www.qlik.com/data-literacy
- EDM Council – DCAM Framework : https://edmcouncil.org
- McKinsey – "The age of analytics" : https://www.mckinsey.com
- NewVantage Partners – "Big Data and AI Executive Survey 2023" : https://www.newvantage.com

## Notions liées
- [[Data Governance]]
- [[Business Intelligence (BI)]]
- [[Data Mesh et Data Fabric]]
- [[Types d'analytics]]
- [[Monétisation des données]]
