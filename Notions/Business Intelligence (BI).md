---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Business Intelligence (BI)

![[N — Business Intelligence (BI).mp3]]
## En bref
> **Définition** : La Business Intelligence (BI) désigne l'ensemble des technologies, processus et méthodes permettant de collecter, transformer et visualiser les données d'une organisation pour faciliter la prise de décision. Elle englobe la conception de tableaux de bord (dashboards), les rapports automatisés, l'analyse exploratoire et, plus récemment, le self-service BI et l'augmented analytics (BI enrichie par l'IA).
> **Pourquoi c'est important** : La BI transforme les données brutes en informations actionnables. Elle est le principal point de contact entre les équipes data et les métiers. Un dashboard bien conçu peut remplacer des heures de travail manuel et accélérer drastiquement les cycles de décision.
> **Chiffres clés** :
> - Le marché mondial de la BI pèse **29 Md$** en 2024 et croît de **+9 % par an** (Gartner)
> - **Power BI** compte plus de **250 000 organisations** clientes dans 220 pays (Microsoft, 2024)
> - Les entreprises investissant dans la BI ont un ROI moyen de **13,01$** pour chaque dollar investi (Nucleus Research)

## Approfondir

### Fonctionnement

#### Architecture BI classique

```
Sources de données → ETL/ELT → Data Warehouse → Couche sémantique → Outil BI → Utilisateur final
(ERP, CRM, Web...)  (transformation)  (stockage OLAP)  (modèle de données)  (dashboard, rapport)
```

**OLAP vs OLTP** :
- **OLTP** (Online Transaction Processing) : bases optimisées pour les transactions unitaires rapides (INSERT, UPDATE). Ex. : base de commandes e-commerce.
- **OLAP** (Online Analytical Processing) : bases optimisées pour les requêtes analytiques agrégées (SUM, COUNT, GROUP BY). Ex. : datawarehouse pour les rapports de vente.

**Modélisation dimensionnelle** (Ralph Kimball) :
- **Table de faits** : métriques mesurables (chiffre d'affaires, quantité vendue)
- **Tables de dimensions** : contexte des faits (client, produit, date, géographie)
- Schéma en étoile ou en flocon (star/snowflake schema)

#### Self-Service BI
Paradigme permettant aux utilisateurs métier de créer leurs propres analyses et visualisations sans dépendre de l'équipe IT ou data.

**Conditions requises** :
- Données préparées et publiées dans une couche sémantique (modèle de données accessible)
- Outil BI avec interface drag-and-drop
- Gouvernance des données (sinon prolifération de rapports contradictoires)
- Formation à la data literacy des utilisateurs

**Risques** : shadow IT analytique, "chiffres différents selon qui les calcule", accès à des données sensibles non contrôlés.

#### DataViz — Visualisation des données
Représentation graphique des données pour faciliter leur compréhension et révéler des patterns invisibles dans les tableaux.

**Principes fondamentaux** (Edward Tufte, Alberto Cairo) :
- **Data-ink ratio** : maximiser l'information, éliminer le bruit visuel
- **Chartjunk** : éléments graphiques sans valeur informationnelle (à éviter)
- Choisir le bon type de graphique selon le message :
  - Comparaison : bar chart, column chart
  - Évolution temporelle : line chart
  - Proportion/composition : pie chart (usage limité), treemap, stacked bar
  - Distribution : histogram, box plot
  - Corrélation : scatter plot
  - Géographique : choroplèthe, heat map

#### Augmented Analytics
Intégration de l'IA et du ML dans les outils BI pour automatiser l'analyse et générer des insights proactifs.

**Fonctionnalités** :
- **Natural Language Query (NLQ)** : poser des questions en langage naturel ("Quel est le CA du mois dernier en Île-de-France ?")
- **Auto-insights** : détection automatique d'anomalies, de tendances, de corrélations
- **Explain the data** : explication automatique des variations (ex. : "Le CA a baissé de 12 % car les ventes de la catégorie X ont chuté")
- **Smart narratives** : génération automatique de textes résumant les données

Exemple : **Power BI Q&A**, **Tableau Ask Data**, **Looker Explore**, **Dataiku** (ML intégré)

#### Les principaux outils BI

| Outil | Éditeur | Positionnement |
|-------|---------|----------------|
| **Power BI** | Microsoft | Leader marché, intégration Microsoft 365, excellent rapport qualité/prix |
| **Tableau** | Salesforce | Référence DataViz, très puissant analytiquement, coûteux |
| **Looker** | Google | BI cloud-native, modélisation LookML, intégré BigQuery |
| **Qlik Sense** | Qlik | Moteur associatif unique (vs SQL), fort en analyse exploratoire |
| **Metabase** | Metabase Inc. | Open source, simple, idéal pour les startups et équipes techniques |
| **Dataiku** | Dataiku | Au-delà de la BI : plateforme Data Science + BI + MLOps |
| **Superset** | Apache | Open source, très populaire dans les data stacks modernes |
| **MicroStrategy** | MicroStrategy | Entreprise, gouvernance forte, finance et retail |

**Quadrant Gartner 2024 (Analytics and BI)** : Microsoft (Power BI), Salesforce (Tableau) et Google (Looker) dominent le "Magic Quadrant Leader" quadrant.

#### Couche sémantique (Semantic Layer)
Abstraction entre les données brutes et les utilisateurs finaux, traduisant les concepts techniques en termes métier.
- "ca_ht" → "Chiffre d'affaires HT"
- Métriques précalculées (taux de marge, panier moyen)
- Règles de filtrage et de sécurité des données (row-level security)

Outils : **dbt** (transformation + sémantique), **AtScale**, **Cube.dev**

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Décisions accélérées et mieux fondées | Données mal préparées → rapports erronés ("garbage in, garbage out") |
| Autonomie des métiers (self-service) | Gouvernance complexe : prolifération de rapports contradictoires |
| Réduction des silos par la visualisation partagée | Coût des licences élevé (Tableau, MicroStrategy) |
| Identification rapide des anomalies et tendances | Adoption difficile sans data literacy des utilisateurs |
| ROI mesurable (Nucleus Research : 13$/1$) | Risque de "dashboard fatigue" si trop de métriques non hiérarchisées |

### Acteurs et solutions du marché
- **Microsoft Power BI** : leader en volume, prix agressif (10€/utilisateur/mois), intégration Teams/Office
- **Tableau** (Salesforce) : référence en DataViz, Tableau Public (gratuit), Tableau Server/Cloud
- **Looker** (Google) : modélisation LookML, fort sur les données BigQuery
- **Qlik** : moteur associatif, fort en discovery analytics
- **Metabase** : open source, déployable on-prem, très accessible aux équipes techniques
- **Dataiku** : plateforme end-to-end Data Science + BI, très présent dans les grandes entreprises françaises

### Cas d'usage concrets
1. **Décathlon** utilise Power BI pour piloter ses 1 700 magasins dans 60 pays. Les directeurs de magasin accèdent à leurs KPIs (CA, stock, marge) en temps réel sur tablette. Le self-service BI a réduit de 70 % les demandes de rapports ad hoc à la DSI centrale.
2. **Airbus** exploite Tableau pour la surveillance de la qualité de production. Des dashboards temps réel agrègent les données de capteurs de 50 chaînes d'assemblage. Les anomalies sont détectées automatiquement (augmented analytics) et alertent les ingénieurs qualité.
3. **Leboncoin** utilise Metabase comme outil BI interne, donnant accès aux données de performance à l'ensemble des équipes produit. L'outil open source leur évite les coûts de licence tout en permettant une analyse SQL pour les utilisateurs avancés.

### Chiffres et tendances
- **Power BI** est l'outil le plus utilisé en France en entreprise avec **62 % de part de marché** sur les outils BI (BARC, 2023)
- L'augmented analytics (IA dans la BI) est la fonctionnalité la plus demandée par **68 % des acheteurs BI** (Gartner, 2024)
- Le **self-service BI** est désormais adopté par **71 % des grandes entreprises** (Forrester)
- **Apache Superset** est devenu le standard de facto des data stacks modernes (dbt + Airflow + Superset)

## Flashcards
#flashcards/Big_DATA/Business_Intelligence_BI

Quelle est la différence entre OLTP et OLAP ? :: OLTP (Online Transaction Processing) est optimisé pour les transactions unitaires rapides (INSERT, UPDATE) — ex. base de commandes. OLAP (Online Analytical Processing) est optimisé pour les requêtes analytiques agrégées (SUM, GROUP BY) — ex. datawarehouse pour les rapports de vente.

Qu'est-ce que le self-service BI et quels sont ses risques ? :: Paradigme permettant aux métiers de créer leurs propres analyses sans l'IT. Risques : prolifération de rapports contradictoires ("chiffres différents selon qui les calcule"), accès non contrôlé à des données sensibles, et shadow IT analytique en l'absence de gouvernance.

Quelles sont les 3 fonctionnalités principales de l'augmented analytics ? :: 1) Natural Language Query (questions en langage naturel), 2) Auto-insights (détection automatique d'anomalies/tendances), 3) Explain the data (explication automatique des variations). Ces fonctionnalités utilisent l'IA/ML pour rendre la BI accessible aux non-experts.

Qu'est-ce que la modélisation dimensionnelle et qui l'a formalisée ? :: Méthode de modélisation des datawarehouses formalisée par Ralph Kimball. Elle organise les données en tables de faits (métriques mesurables : CA, quantités) et tables de dimensions (contexte : client, produit, date). Résulte en un schéma en étoile (star schema) ou en flocon (snowflake schema).

Quel est le positionnement différenciant de Qlik par rapport à Power BI et Tableau ? :: Qlik repose sur un moteur associatif (vs relationnel/SQL). Il permet d'explorer librement les associations entre n'importe quelles données sans prédéfinir les jointures. Fort en analyse exploratoire et discovery analytics, là où Power BI/Tableau suivent un modèle de données prédéfini.

Qu'est-ce que la couche sémantique (semantic layer) en BI ? :: Abstraction entre les données brutes et les utilisateurs, traduisant les concepts techniques en termes métier (ex. "ca_ht" → "Chiffre d'affaires HT") et précalculant les métriques (taux de marge, panier moyen). Permet à différents outils BI d'utiliser les mêmes définitions cohérentes.

Qu'est-ce que le "data-ink ratio" de Tufte et pourquoi est-ce important en DataViz ? :: Principe selon lequel la proportion de "l'encre" consacrée à représenter des données réelles doit être maximisée, et les éléments graphiques sans valeur informative (chartjunk) éliminés. Un ratio élevé = visualisation efficace. Fondement de la bonne pratique en design de dashboards.

## Sources
- Gartner – "Magic Quadrant for Analytics and Business Intelligence Platforms 2024" : https://www.gartner.com
- Nucleus Research – "The ROI of Business Intelligence" : https://nucleusresearch.com
- Edward Tufte – "The Visual Display of Quantitative Information" (livre)
- Microsoft – Power BI Blog : https://powerbi.microsoft.com/blog
- BARC – "BI Survey 2023" : https://bi-survey.com
- Dataiku – Documentation officielle : https://doc.dataiku.com

## Notions liées
- [[Types d'analytics]]
- [[Data Governance]]
- [[Data Maturity et Data Literacy]]
- [[Data Mesh et Data Fabric]]
- [[IA en cybersécurité]]
