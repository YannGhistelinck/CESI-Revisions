---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Modèles de service cloud

![[N — Modèles de service cloud.mp3]]
## En bref
> **Définition** : Les modèles de service cloud définissent le niveau d'abstraction et de responsabilité entre le fournisseur et le client : IaaS (Infrastructure as a Service), PaaS (Platform as a Service), SaaS (Software as a Service), et les modèles émergents comme FaaS et le serverless.
> **Pourquoi c'est important** : Le choix du modèle conditionne directement la répartition des coûts, la vitesse de déploiement et le niveau de contrôle conservé par la DSI. Un mauvais choix génère soit une sur-ingénierie soit une perte de maîtrise.
> **Chiffres clés** :
> - Le marché SaaS mondial représentait 197 milliards de dollars en 2023 (Gartner, 2024)
> - Le serverless affiche une croissance annuelle de ~25% et représente un marché de 36 milliards de dollars projeté en 2028 (MarketsandMarkets, 2023)
> - 85% des organisations utiliseront une stratégie cloud-first d'ici 2025 (Gartner)

## Approfondir

### Fonctionnement

**IaaS (Infrastructure as a Service)**
Le fournisseur met à disposition des ressources informatiques virtualisées : serveurs, stockage, réseau. Le client gère l'OS, le middleware, les runtimes et les applications. Exemples : AWS EC2, Azure Virtual Machines, Google Compute Engine.

**PaaS (Platform as a Service)**
Le fournisseur gère l'infrastructure et le runtime. Le client se concentre sur le code et les données. Adapté au développement applicatif sans gestion de serveur. Exemples : AWS Elastic Beanstalk, Azure App Service, Google App Engine, Heroku.

**SaaS (Software as a Service)**
L'application est entièrement gérée par le fournisseur, accessible via un navigateur. Le client ne contrôle que les données et la configuration. Exemples : Microsoft 365, Salesforce, Google Workspace, ServiceNow.

**FaaS (Function as a Service)**
Exécution de fonctions à la demande, facturées à l'invocation. Pas de gestion de serveur ni de conteneur par le client. Exemples : AWS Lambda, Azure Functions, Google Cloud Functions.

**Serverless**
Paradigme plus large que le FaaS : englobe toute architecture où la gestion des serveurs est entièrement abstraite (FaaS + BaaS — Backend as a Service). Le code s'exécute uniquement quand il est déclenché. Avantage majeur : facturation à la milliseconde d'exécution, pas de ressource idle.

**Modèle de responsabilité partagée**
Chaque modèle déplace la frontière de responsabilité. En IaaS, le client est responsable de l'OS et au-dessus. En PaaS, le fournisseur prend en charge l'OS et le runtime. En SaaS, le fournisseur gère tout sauf les données et accès utilisateurs. Ce modèle est critique pour la sécurité : une incompréhension génère des angles morts de sécurité.

| Couche | On-Premise | IaaS | PaaS | SaaS |
|--------|-----------|------|------|------|
| Application | Client | Client | Client | Fournisseur |
| Runtime | Client | Client | Fournisseur | Fournisseur |
| OS | Client | Client | Fournisseur | Fournisseur |
| Virtualisation | Client | Fournisseur | Fournisseur | Fournisseur |
| Matériel | Client | Fournisseur | Fournisseur | Fournisseur |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction du time-to-market (PaaS, SaaS) | Perte de contrôle progressive (IaaS → SaaS) |
| Pas d'investissement matériel initial | Dépendance au fournisseur (vendor lock-in) |
| Scalabilité native, élasticité | Latence réseau pour les workloads critiques |
| Mutualisation des coûts d'infrastructure | Complexité de la sécurité partagée |
| Serverless : facturation à l'usage réel | Cold start sur FaaS (latence au premier appel) |
| Mises à jour gérées (SaaS) | Personnalisation limitée en SaaS |

### Acteurs et solutions du marché

- **IaaS** : AWS (EC2, S3, VPC), Microsoft Azure (VMs, Blob Storage), Google Cloud (GCE, GCS), OVHcloud (cloud privé souverain), Outscale (filiale Dassault, SecNumCloud)
- **PaaS** : Heroku (Salesforce), AWS Elastic Beanstalk, Azure App Service, Cloud Foundry (open source), Red Hat OpenShift
- **SaaS** : Microsoft 365, Google Workspace, Salesforce, SAP S/4HANA Cloud, ServiceNow, Workday
- **FaaS / Serverless** : AWS Lambda (leader du marché), Azure Functions, Google Cloud Functions, Cloudflare Workers, Vercel (edge functions)

### Cas d'usage concrets

1. **Migration SaaS d'un ERP** : une PME remplace son ERP on-premise par SAP S/4HANA Cloud. La DSI supprime la gestion de 3 serveurs, les mises à jour sont automatiques. Économie estimée : 40% sur les coûts d'exploitation (source : cas clients SAP).

2. **Backend serverless pour une app mobile** : une startup utilise AWS Lambda + API Gateway pour gérer les pics de charge lors d'un lancement. Facturation à la requête, aucun serveur idle en dehors des pics.

3. **PaaS pour accélérer le développement** : une équipe DevOps déploie une application Node.js sur Azure App Service. Le pipeline CI/CD est intégré, l'OS et le runtime sont gérés par Azure. Le temps de déploiement passe de 2 semaines à 2 jours.

### Chiffres et tendances

- IaaS : 150 milliards de dollars de marché en 2023, dominé par AWS (31%), Azure (25%), Google Cloud (11%) (Synergy Research, 2024)
- 70% des workloads d'entreprise seront hébergés dans le cloud d'ici 2025 (IDC)
- Serverless : adoption en hausse dans les architectures microservices, portée par Kubernetes et les service mesh
- FaaS limite à 15 minutes d'exécution sur AWS Lambda, contrainte architecturale à intégrer dès la conception

## Flashcards
#flashcards/Cloud_et_Virtualisation/Modèles_de_service_cloud #flashcards/Optimisation_du_SI/Modèles_de_service_cloud

Qu'est-ce que le modèle de responsabilité partagée ? :: Principe selon lequel la sécurité est une responsabilité divisée entre le fournisseur (infrastructure, hyperviseur) et le client (données, accès, configuration). La frontière varie selon le modèle (IaaS/PaaS/SaaS).

Quelle est la différence entre FaaS et serverless ? :: Le FaaS (Function as a Service) est l'exécution de fonctions à la demande. Le serverless est un paradigme plus large qui inclut le FaaS et le BaaS (Backend as a Service), où toute gestion de serveur est abstraite.

Quelles couches restent sous responsabilité du client en IaaS ? :: Le système d'exploitation, le middleware, le runtime, les applications et les données.

Quel est le principal risque du modèle SaaS pour une DSI ? :: La perte de contrôle sur les données et la dépendance au fournisseur (vendor lock-in), avec une personnalisation limitée.

Qu'est-ce qu'un "cold start" en FaaS ? :: Latence additionnelle lors de la première invocation d'une fonction, le temps que l'environnement d'exécution soit initialisé. Problématique pour les applications temps réel.

Citez 3 exemples de SaaS utilisés en entreprise. :: Microsoft 365, Salesforce (CRM), ServiceNow (ITSM) / Google Workspace, SAP S/4HANA Cloud, Workday (RH).

Pourquoi le PaaS accélère-t-il le développement ? :: Parce que le fournisseur gère l'OS, le runtime et l'infrastructure, l'équipe se concentre uniquement sur le code métier. Réduction du time-to-market.

## Sources

- Gartner, "Cloud End-User Spending Forecast", 2024
- MarketsandMarkets, "Serverless Architecture Market", 2023
- Synergy Research Group, "Cloud Infrastructure Market", Q4 2023
- NIST SP 800-145, "The NIST Definition of Cloud Computing"
- AWS, Azure, Google Cloud — documentations officielles sur le shared responsibility model

## Notions liées

- [[Modèles de déploiement cloud]]
- [[Économie du cloud]]
- [[Vendor lock-in et réversibilité]]
- [[Cloud souverain]]
- [[FinOps]]
- [[Infrastructure des datacenters]]
