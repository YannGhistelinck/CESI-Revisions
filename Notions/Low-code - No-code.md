---
type: notion
thèmes:
  - Mobilité
  - Développement
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Low-code / No-code

![[N — Low-code - No-code.mp3]]
## En bref
> **Définition** : Le low-code est une approche de développement logiciel qui minimise la quantité de code manuel en utilisant des interfaces visuelles, du drag-and-drop et des composants préconstruits. Le no-code va plus loin : il permet à des utilisateurs sans compétence technique de créer des applications complètes sans écrire une seule ligne de code. Ces deux approches accélèrent la création d'applications et démocratisent le développement au sein des organisations.
> **Pourquoi c'est important** : Face à la pénurie de développeurs et à l'accélération des besoins métier, le low-code/no-code permet aux DSI de réduire les backlogs applicatifs et d'impliquer les métiers dans la création de leurs propres outils (concept de "citizen developer"). Cependant, cela crée de nouveaux défis de gouvernance, de sécurité et de dette technique si mal encadré.
> **Chiffres clés** :
> - Le marché mondial du low-code/no-code devrait atteindre **187 milliards USD en 2030** (Gartner, 2023)
> - **70 % des applications** créées par des entreprises seront développées avec des outils low-code ou no-code d'ici 2025 (Gartner)
> - La pénurie mondiale de développeurs est estimée à **85 millions de professionnels** d'ici 2030 (Korn Ferry, 2021)

## Approfondir

### Fonctionnement

**Low-code**
Plateforme de développement qui accélère la création d'applications via des éditeurs visuels (drag-and-drop), des modèles préconstruits et des connecteurs prêts à l'emploi. Des développeurs professionnels restent impliqués pour la logique complexe et les intégrations critiques.
- Public cible : développeurs pro qui veulent aller plus vite, développeurs "fusion" (entre IT et métier)
- Exemples d'usage : applications web et mobiles, automatisation de processus, portails RH, applications métier

**No-code**
Plateforme permettant à des utilisateurs métier (non-développeurs) de créer des applications, des workflows et des bases de données via des interfaces purement visuelles.
- Public cible : citizen developers (commerciaux, RH, opérations, marketing)
- Exemples d'usage : tableaux de bord, formulaires intelligents, automatisations simples, mini-CRM

**Citizen Developer**
Employé non-développeur qui crée des applications pour son propre usage ou pour son équipe, avec l'approbation de la DSI, grâce aux outils low-code/no-code. Concept formalisé par Gartner. La DSI doit encadrer cette pratique via une gouvernance (Shadow IT low-code).

**Power Platform (Microsoft)**
Suite low-code/no-code intégrée à Microsoft 365 :
- **Power Apps** : création d'applications mobiles et web
- **Power Automate** : automatisation de workflows (équivalent no-code de la RPA légère)
- **Power BI** : Business Intelligence et tableaux de bord
- **Power Pages** : création de portails web
- **Dataverse** : base de données relationnelle low-code sous-jacente

Avantage majeur : intégration native avec Microsoft 365, Azure AD, Dynamics 365 et 900+ connecteurs.

**Mendix**
Plateforme low-code d'entreprise (rachetée par Siemens en 2018). Fort sur les applications métier complexes, la collaboration dev/métier et le déploiement cloud. Utilisé dans l'industrie, la finance et le secteur public. Dispose d'un marketplace d'applications préconstruites.

**Autres plateformes majeures :**
- **OutSystems** : low-code pour applications d'entreprise critiques, fort sur la performance et la sécurité
- **Appian** : fort sur BPM (Business Process Management) et low-code
- **Bubble** : no-code web, très utilisé par les startups pour les MVPs
- **Airtable** : no-code orienté base de données collaborative
- **Make (ex-Integromat)** : no-code pour l'automatisation et l'intégration entre apps (concurrent de Zapier)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Délai de mise sur le marché réduit (x5 à x10 vs dev traditionnel) | Risque de dette technique si mal gouverné |
| Réduction des coûts de développement | Limitations techniques pour les cas d'usage complexes |
| Démocratisation : les métiers participent à la création | Shadow IT si non encadré par la DSI |
| Absorption des backlogs applicatifs | Vendor lock-in fort (migration difficile si changement d'outil) |
| Maintenance facilitée par les outils visuels | Performances moindres que le développement sur mesure |
| Idéal pour les MVPs et le prototypage rapide | Enjeux de sécurité si les citizen developers manquent de formation |

### Acteurs et solutions du marché

| Plateforme | Type | Éditeur | Positionnement |
|-----------|------|---------|----------------|
| Power Apps / Power Automate | Low-code/No-code | Microsoft | Leader PME-ETI, intégré M365 |
| Mendix | Low-code | Siemens | Industrie, applications complexes |
| OutSystems | Low-code | OutSystems | Applications critiques d'entreprise |
| Appian | Low-code | Appian | BPM + low-code |
| Bubble | No-code | Bubble | Startups, MVPs web |
| Airtable | No-code | Airtable | Bases de données collaboratives |
| Zapier / Make | No-code | Zapier / Celonis | Automatisation d'intégrations |
| Salesforce Lightning | Low-code | Salesforce | CRM et apps commerciales |

### Cas d'usage concrets

**1. Digitalisation RH avec Power Apps**
Le service RH d'un groupe industriel de 5 000 personnes crée une application Power Apps de gestion des demandes de formation en 3 semaines (vs 6 mois estimés pour un développement classique). L'application se connecte directement à SharePoint (stockage des dossiers), Power Automate (circuit de validation) et Teams (notifications). Le budget : 0 € de développement externe (inclus dans la licence M365 E3).

**2. Startup avec MVP no-code**
Une startup de la FoodTech crée son MVP (marketplace de producteurs locaux) en 8 semaines sur Bubble, sans développeur. Le MVP est testé auprès de 500 utilisateurs, valide le product-market fit, et lève 500 000 € avant de reconstruire la plateforme en technologie sur mesure (React/Node.js) pour passer à l'échelle.

**3. Automatisation de rapport avec Mendix dans une usine**
Un constructeur aéronautique utilise Mendix pour créer une application de reporting qualité connectée aux PLCs (automates industriels) et à l'ERP SAP. Les opérateurs saisissent les non-conformités sur tablette ; les données alimentent automatiquement des rapports Power BI. Le projet est livré en 4 mois vs 18 mois estimés en développement Java classique.

### Chiffres et tendances

- **Gartner** estime que les plateformes low-code généreront 65 % du développement applicatif en 2024
- **Power Platform** compte plus de **33 millions d'utilisateurs actifs** mensuels (Microsoft, 2024)
- **Mendix** annonce des accélérations de développement de **5 à 10x** par rapport au développement traditionnel
- Tendance : **IA générative + low-code** — les plateformes intègrent des copilots IA (Power Apps Copilot, Mendix AI) qui génèrent des applications à partir de descriptions en langage naturel
- Risque émergent : les applications low-code créées par les citizen developers sont souvent **non testées, non documentées et sans stratégie de continuité** — enjeu de gouvernance pour les DSI

## Flashcards
#flashcards/Mobilité/Low_code_No_code #flashcards/Développement/Low_code_No_code #flashcards/Big_DATA/Low_code_No_code

Quelle est la différence entre low-code et no-code ? :: Le low-code permet d'accélérer le développement avec des interfaces visuelles mais nécessite encore des développeurs pour la logique complexe. Le no-code permet à des non-développeurs (citizen developers) de créer des applications complètes sans écrire de code.

Qu'est-ce qu'un citizen developer ? :: Un employé non-développeur (commercial, RH, opérationnel) qui crée des applications pour son équipe grâce aux outils low-code/no-code, avec l'approbation et l'encadrement de la DSI. Concept formalisé par Gartner.

Quels sont les 4 composants de la Power Platform Microsoft ? :: Power Apps (création d'applications), Power Automate (automatisation de workflows), Power BI (Business Intelligence et tableaux de bord), Power Pages (création de portails web). Tous s'appuient sur Dataverse comme base de données sous-jacente.

Quels sont les principaux risques du low-code/no-code pour une DSI ? :: Shadow IT (applications créées sans validation IT), dette technique (applications non maintenues), vendor lock-in (migration difficile), problèmes de sécurité (données sensibles mal protégées), et absence de tests et de documentation.

Pourquoi Mendix est-il positionné comme un outil low-code "enterprise" ? :: Mendix est conçu pour des applications métier complexes avec des exigences de performance, de sécurité et d'intégration. Il permet une collaboration structurée entre développeurs et métiers, gère le cycle de vie complet et supporte des déploiements cloud, on-premises et hybrides. Il est utilisé dans des secteurs réglementés comme la finance et l'industrie.

Dans quel contexte le no-code est-il particulièrement utile pour les startups ? :: Pour créer des MVPs (Minimum Viable Products) rapidement et à faible coût, sans développeurs. Des outils comme Bubble permettent de valider un concept en quelques semaines, tester le product-market fit, et lever des fonds avant d'investir dans un développement sur mesure.

## Sources

- Gartner, "Magic Quadrant for Enterprise Low-Code Application Platforms", 2023
- Gartner, "Low-Code Development Technologies Evaluation Guide", 2023
- Microsoft Power Platform Blog, 2024
- Mendix, "State of Low-Code Report", 2023
- Korn Ferry, "Future of Work", 2021
- Forrester, "The Forrester Wave: Low-Code Platforms For Business Developers", 2023

## Notions liées
- [[RPA (Robotic Process Automation)]]
- [[Digital Workplace]]
- [[DevOps]]
- [[CI - CD]]
- [[Architecture logicielle]]
- [[Business Intelligence (BI)]]
- [[Dette technique]]
