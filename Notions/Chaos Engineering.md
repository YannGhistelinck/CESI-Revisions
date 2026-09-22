---
type: notion
thèmes:
  - Développement
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Chaos Engineering

![[N — Chaos Engineering.mp3]]
## En bref
> **Définition** : Le Chaos Engineering est la pratique consistant à introduire délibérément des défaillances contrôlées dans un système distribué en production (ou en environnement de pré-production) afin de vérifier sa résilience, d'identifier ses points de fragilité et de renforcer la confiance dans sa capacité à supporter des conditions adverses réelles.
> **Pourquoi c'est important** : Pour une DSI gérant des architectures microservices ou cloud-native, il est impossible de prévoir tous les modes de défaillance par les seuls tests classiques. Le Chaos Engineering permet de découvrir les failles avant qu'elles ne deviennent des incidents en production, réduisant ainsi le MTTR et améliorant la disponibilité réelle.
> **Chiffres clés** :
> - Netflix a réduit ses incidents de production significatifs de 25 % après l'adoption systématique du Chaos Engineering (2012).
> - 43 % des organisations pratiquant le Chaos Engineering déclarent avoir détecté des failles critiques avant un incident réel (Gremlin State of Chaos Engineering 2023).
> - Le marché du Chaos Engineering est estimé à 1,1 Md$ en 2024, croissance prévue de 20 % par an jusqu'en 2030.

## Approfondir

### Fonctionnement

**Principes fondateurs (Chaos Engineering Principles — principlesofchaos.org)**
1. Formuler une hypothèse sur le comportement en régime stable (*steady state*).
2. Varier les événements du monde réel (latence réseau, crash de pod, saturation CPU, défaillance d'une zone de disponibilité).
3. Exécuter l'expérience en production (ou dans un environnement miroir fidèle).
4. Réfuter l'hypothèse pour révéler les faiblesses.

**Chaos Monkey**
Outil créé par Netflix en 2011, initialement conçu pour tuer aléatoirement des instances EC2 en production. Fait partie de la suite **Simian Army** (Latency Monkey, Chaos Gorilla, etc.). Le principe : si des instances peuvent mourir à tout moment, les équipes sont forcées de concevoir des systèmes résilients.

**Types d'expériences de chaos**
- **Infrastructure** : arrêt de VM/conteneurs, saturation disque, panne réseau, blackhole DNS.
- **Application** : injection de latence, retour d'erreurs HTTP 5xx, consommation excessive de mémoire.
- **Plateforme** : indisponibilité d'une zone AWS/Azure/GCP (AZ), perte d'un nœud Kubernetes.
- **Humain / processus** : simulation de perte de documentation critique, rotation d'astreinte.

**Game Days**
Sessions planifiées où une équipe exécute des scénarios de chaos face à un groupe de réponse à incident. Permettent de tester simultanément les systèmes et les processus humains (runbooks, communication de crise, escalades).

**Relation avec le SRE (Site Reliability Engineering)**
Le Chaos Engineering est l'un des piliers du SRE (Google). Il s'articule avec les SLO (Service Level Objectives) : une expérience de chaos valide que le système respecte ses SLO même en conditions dégradées.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Découverte proactive des failles avant les incidents réels | Risque d'impact réel en production si mal encadré |
| Renforce la culture de la résilience dans les équipes | Nécessite une maturité observabilité/monitoring préalable |
| Valide les SLO et les runbooks de réponse à incident | Résistance culturelle forte (peur de "casser" la prod) |
| Améliore la confiance des équipes dans l'architecture | Peut révéler des dettes techniques difficiles à corriger |
| Complémentaire aux tests classiques | Coût organisationnel élevé (game days, formation) |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Netflix | Chaos Monkey (open source), SimianArmy, FIT (Failure Injection Testing) |
| Gremlin | Plateforme SaaS de Chaos Engineering enterprise, bibliothèque d'attaques prédéfinies |
| Chaos Mesh | Outil open source CNCF pour le chaos sur Kubernetes (injection de pannes granulaire) |
| Litmus Chaos | Plateforme open source (CNCF Sandbox), hub de scénarios chaos Kubernetes |
| AWS Fault Injection Simulator (FIS) | Service AWS managé pour les expériences de chaos sur l'écosystème AWS |
| Azure Chaos Studio | Service Azure pour les expériences de résilience sur ressources Azure |
| Steadybit | Plateforme Chaos Engineering orientée developer experience |

### Cas d'usage concrets
1. **Netflix** : utilise le Chaos Engineering en continu sur ses 700+ microservices. Chaos Monkey tourne en production tous les jours ouvrés, garantissant que la plateforme supporte la défaillance de n'importe quelle instance sans interruption de service.
2. **Amazon** : pratique des "GameDays" réguliers simulant la perte d'une région AWS entière, validant ainsi les mécanismes de bascule géographique de ses propres services (dont AWS S3, DynamoDB).
3. **Alibaba** : utilise ChaosBlade (leur outil interne open sourcé) pour valider la résilience de ses systèmes e-commerce lors des pics de Singles' Day (11/11), gérant des millions de transactions par seconde.

### Chiffres et tendances
- 78 % des organisations pratiquant le Chaos Engineering déclarent une amélioration mesurable de leur disponibilité (Gremlin, 2023).
- Le Chaos Engineering est recommandé par le NIST SP 800-160 Vol. 2 dans le cadre de la cyber-résilience des systèmes critiques.
- L'adoption en entreprise a progressé de 35 % entre 2021 et 2023 (marché Chaos Engineering).
- Les environnements Kubernetes sont la cible principale des expériences de chaos (67 % des cas selon Chaos Mesh Survey 2023).

## Flashcards
#flashcards/Développement/Chaos_Engineering #flashcards/Optimisation_du_SI/Chaos_Engineering
- Qu'est-ce que le Chaos Engineering ? :: La pratique d'introduire délibérément des défaillances dans un système pour valider sa résilience et identifier ses faiblesses avant qu'elles ne causent des incidents.
- Qu'est-ce que Chaos Monkey ? :: Outil créé par Netflix en 2011 qui tue aléatoirement des instances en production pour forcer la conception de systèmes résilients.
- Qu'est-ce qu'un "steady state" en Chaos Engineering ? :: Le comportement normal et mesurable d'un système (ex : taux d'erreur < 1 %, latence p99 < 200 ms) servant de référence pour évaluer l'impact d'une expérience de chaos.
- Qu'est-ce qu'un Game Day ? :: Une session planifiée où une équipe exécute des scénarios de chaos pour tester simultanément les systèmes et les processus humains (runbooks, communication de crise).
- Quelle est la relation entre Chaos Engineering et SRE ? :: Le Chaos Engineering est un pilier du SRE (Site Reliability Engineering) ; il valide que le système respecte ses SLO même dans des conditions dégradées.
- Quel outil AWS permet de pratiquer le Chaos Engineering ? :: AWS Fault Injection Simulator (FIS), service managé pour créer des expériences de résilience sur l'écosystème AWS.
- Quelle est la principale condition préalable au Chaos Engineering en production ? :: Une observabilité mature (monitoring, alerting, tracing) permettant de détecter immédiatement les impacts et de stopper l'expérience si nécessaire.

## Sources
- Principles of Chaos Engineering : https://principlesofchaos.org/
- Gremlin State of Chaos Engineering 2023 : https://www.gremlin.com/state-of-chaos-engineering/
- Netflix Tech Blog — Chaos Monkey : https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116
- CNCF Chaos Mesh : https://chaos-mesh.org/
- AWS Fault Injection Simulator : https://aws.amazon.com/fis/
- NIST SP 800-160 Vol. 2 (Cyber Resiliency Engineering) : https://csrc.nist.gov/publications/detail/sp/800-160/vol-2/final

## Notions liées
- [[DORA Metrics]]
- [[Cyber-résilience]]
- [[PCA - PRA]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Service Mesh]]
- [[Tests logiciels]]
