---
type: notion
thèmes:
  - Développement
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Platform Engineering

## En bref
> **Définition** : Le Platform Engineering est la discipline consistant à concevoir et opérer une plateforme interne (Internal Developer Platform — IDP) qui met à disposition des développeurs un ensemble de capacités en libre-service (infrastructure, CI/CD, observabilité, sécurité) via une interface unifiée (Internal Developer Portal). L'objectif est de réduire la charge cognitive des développeurs et d'accélérer la livraison de valeur.
> **Pourquoi c'est important** : Face à la complexité croissante des architectures cloud-native (Kubernetes, microservices, GitOps), les développeurs passent une part croissante de leur temps à gérer l'infrastructure plutôt qu'à coder. Le Platform Engineering industrialise les bonnes pratiques et les met à disposition via une API ou un portail, transformant l'infrastructure en produit interne.
> **Chiffres clés** :
> - 80 % des grandes organisations auront des équipes de Platform Engineering dédiées d'ici 2026 (Gartner, 2023).
> - Les équipes utilisant un IDP réduisent leur cognitive load de 40 % et leur time-to-deploy de 60 % (CNCF Platform Engineering whitepaper, 2023).
> - Le marché des Internal Developer Portals dépasse 1 Md$ en 2024 (Forrester).

## Approfondir

### Fonctionnement

**Internal Developer Platform (IDP) vs Internal Developer Portal**
- **IDP (plateforme)** : ensemble des capacités techniques (cloud, CI/CD, secrets management, bases de données, monitoring) exposées via des APIs et une couche d'abstraction. Le développeur provisionne ses ressources sans connaître la complexité sous-jacente.
- **Internal Developer Portal (portail)** : interface utilisateur (souvent Backstage) qui agrège en un seul endroit le catalogue de services, la documentation, les templates de projet, les métriques de santé des services et les workflows de self-service.

**Composants typiques d'une IDP**
1. **Service Catalog** : inventaire de tous les services, APIs et bibliothèques de l'organisation avec leurs propriétaires, leur statut et leur documentation.
2. **Golden Paths (chemins dorés)** : templates pré-approuvés et sécurisés pour créer un nouveau service (scaffold automatique : repo Git, pipeline CI/CD, namespace Kubernetes, monitoring, alerting).
3. **Self-service infrastructure** : provisionnement de bases de données, buckets, files de messages via des formulaires ou une CLI, sans ticket à l'équipe infrastructure.
4. **Scorecard de maturité** : tableau de bord évaluant chaque service sur des critères de qualité (couverture de tests, présence d'un runbook, conformité sécurité, DORA Metrics).
5. **Gestion des secrets** : intégration avec Vault (HashiCorp) ou les gestionnaires de secrets cloud pour injecter les secrets sans les exposer dans le code.

**Backstage (Spotify)**
Outil open source créé par Spotify en 2020, devenu un projet CNCF Incubating en 2022. Il est la base de facto des Internal Developer Portals. Il s'étend via des plugins (Kubernetes, ArgoCD, PagerDuty, Lighthouse, TechDocs).

**Lien avec le concept de "Platform as a Product"**
L'équipe Platform Engineering adopte une approche produit : elle a ses propres utilisateurs (les développeurs), recueille du feedback, priorise des fonctionnalités et mesure son NPS (Net Promoter Score) interne. Cela implique des Product Managers dédiés à la plateforme.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction de la charge cognitive des développeurs | Investissement initial élevé (équipe dédiée, tooling) |
| Standardisation et sécurisation des pratiques | Risque de créer un "goulot d'étranglement" si la plateforme est trop rigide |
| Accélération du time-to-market | Résistance des équipes à abandonner leur autonomie totale |
| Gouvernance et conformité intégrées dès la création | Nécessite une culture "platform as a product" et du product management |
| Amélioration de la Developer Experience (DX) | La complexité de la plateforme peut reproduire celle qu'on cherchait à masquer |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Spotify / CNCF | Backstage — Internal Developer Portal open source, standard de facto |
| HashiCorp | Terraform, Vault, Waypoint — briques d'infrastructure as code et secrets |
| Humanitec | Orchestrateur de plateforme (Platform Orchestrator), référence IDP SaaS |
| Cortex | Developer portal concurrent de Backstage, centré scorecard et métriques |
| Port | Internal Developer Portal no-code/low-code, cataloque et self-service |
| OpsLevel | Catalogue de services et scorecard de maturité pour les microservices |
| Crossplane | Outil CNCF pour provisionner l'infrastructure cloud via Kubernetes Custom Resources |

### Cas d'usage concrets
1. **Spotify** : a créé Backstage en interne pour gérer 2 000+ microservices développés par 2 000 ingénieurs. Après l'open sourcing en 2020, plus de 900 entreprises ont adopté Backstage (dont Netflix, Airbnb, Zalando).
2. **Zalando** : a construit une IDP complète (ZAPFL) permettant à ses 2 500 développeurs de déployer en production en quelques minutes via des golden paths Kubernetes, réduisant les demandes au système ops de 70 %.
3. **BNP Paribas** : déploie un Internal Developer Portal basé sur Backstage pour centraliser le catalogue de 300+ APIs internes, automatiser les onboardings équipes et standardiser les pipelines CI/CD au niveau groupe.

### Chiffres et tendances
- Backstage est utilisé par plus de 900 organisations, avec 100+ plugins CNCF officiels (2024).
- 71 % des équipes Platform Engineering mesurent leur succès via le NPS développeur interne (CNCF, 2023).
- Gartner cite le Platform Engineering comme l'une des 10 tendances technologiques stratégiques de 2024.
- Le "cognitive load" est identifié comme le principal obstacle à la productivité des développeurs (State of DevOps 2023).

## Flashcards
#flashcards
- Qu'est-ce que le Platform Engineering ? :: La discipline consistant à concevoir et opérer une plateforme interne (IDP) qui met à disposition des développeurs des capacités en libre-service pour réduire leur charge cognitive et accélérer la livraison.
- Quelle est la différence entre une IDP et un Internal Developer Portal ? :: L'IDP est l'ensemble des capacités techniques (infrastructure, CI/CD, secrets) ; le portail est l'interface UI (souvent Backstage) qui les expose aux développeurs.
- Qu'est-ce qu'un "Golden Path" ? :: Un template pré-approuvé et sécurisé pour créer un nouveau service (repo Git, pipeline CI/CD, namespace K8s, monitoring) en respectant les standards de l'organisation.
- Qui a créé Backstage et quel est son statut actuel ? :: Créé par Spotify en 2020, Backstage est devenu un projet CNCF Incubating en 2022 et est le standard de facto des Internal Developer Portals.
- Qu'est-ce que le concept "Platform as a Product" ? :: Traiter la plateforme interne comme un produit à part entière, avec des utilisateurs (développeurs), du feedback, des priorités et un NPS interne.
- Quel outil CNCF permet de provisionner l'infrastructure cloud via des Custom Resources Kubernetes ? :: Crossplane.
- Pourquoi le Platform Engineering est-il lié à la Developer Experience (DX) ? :: Il vise à réduire la friction et la charge cognitive des développeurs en leur fournissant des outils, des templates et des workflows standardisés accessibles en self-service.

## Sources
- CNCF Platform Engineering Whitepaper 2023 : https://tag-app-delivery.cncf.io/whitepapers/platforms/
- Backstage.io (Spotify / CNCF) : https://backstage.io/
- Gartner Top 10 Strategic Technology Trends 2024 : https://www.gartner.com/en/information-technology/insights/top-technology-trends
- Humanitec State of Internal Developer Portals 2023 : https://humanitec.com/blog/state-of-internal-developer-portals-2023
- Team Topologies (Matthew Skelton & Manuel Pais) — Éditions IT Revolution, 2019

## Notions liées
- [[DORA Metrics]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Cloud Native et 12-Factor App]]
- [[Service Mesh]]
- [[Legacy et dette technique]]
