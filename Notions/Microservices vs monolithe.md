---
type: notion
thèmes:
  - Développement
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Microservices vs monolithe

## En bref
> **Définition** : Un **monolithe** est une application dans laquelle tous les composants fonctionnels sont déployés comme une seule unité. Une architecture **microservices** décompose l'application en services indépendants, chacun responsable d'une capacité métier, déployables et scalables indépendamment. L'**event-driven architecture** (EDA) est un style complémentaire dans lequel les services communiquent via des événements asynchrones.
> **Pourquoi c'est important** : Le choix entre monolithe et microservices est l'une des décisions architecturales les plus structurantes pour une DSI. Il impacte le modèle organisationnel (loi de Conway), les coûts d'infrastructure, la complexité opérationnelle et la capacité à scaler.
> **Chiffres clés** :
> - **86 % des organisations** utilisant les microservices rapportent une amélioration de leur fréquence de déploiement (CNCF Survey, 2022).
> - Netflix déploie plus de **1 000 fois par jour** grâce à ses microservices.
> - Le coût opérationnel des microservices est **en moyenne 3 à 5 fois plus élevé** qu'un monolithe équivalent pour de petites équipes (ThoughtWorks).

## Approfondir

### Fonctionnement

#### Architecture monolithique
Dans un monolithe, toutes les fonctionnalités (UI, logique métier, accès données) sont dans une seule base de code, compilées et déployées ensemble.

**Variantes** :
- **Monolithe modulaire** : code organisé en modules distincts mais déployé comme une seule unité. Meilleure maintenabilité sans la complexité opérationnelle des microservices. Recommandé par Martin Fowler comme première étape.
- **Monolithe distribué** (anti-pattern) : services qui semblent séparés mais sont fortement couplés — le pire des deux mondes.

**Avantages du monolithe** : simplicité de développement local, debuggage facilité, latence interne faible (appels en mémoire), transactions ACID simples, coût opérationnel faible.

**Inconvénients** : scaling global de l'application entière (pas de scaling sélectif), déploiements coordonnés pour tous les composants, risque de couplage croissant avec le temps.

#### Architecture microservices
Chaque service est **autonome** : sa propre base de code, son propre déploiement, sa propre base de données (pattern **Database per Service**).

**Principes fondamentaux** :
- **Single Responsibility** : chaque service = une capacité métier.
- **Loose Coupling** : communication via API (REST, gRPC) ou événements — pas de base de données partagée.
- **High Cohesion** : tout ce qui doit évoluer ensemble est dans le même service.
- **Décentralisation** : chaque service choisit sa technologie (polyglottisme).

**Communication** :
- **Synchrone** : HTTP/REST, gRPC (protobuf) — pour les requêtes nécessitant une réponse immédiate.
- **Asynchrone** : messaging (Kafka, RabbitMQ, AWS SQS) — pour les opérations non bloquantes et le découplage temporel.

**Patterns clés** :
- **API Gateway** : point d'entrée unique, routage, authentification, rate limiting (Kong, AWS API Gateway, NGINX).
- **Service Discovery** : les services se trouvent dynamiquement (Consul, Kubernetes DNS, Eureka).
- **Circuit Breaker** : interrompt les appels vers un service défaillant pour éviter les cascades (Resilience4j, Hystrix).
- **Saga Pattern** : gestion des transactions distribuées via une séquence d'événements compensatoires (alternative aux transactions ACID distribuées impossibles).
- **CQRS** (Command Query Responsibility Segregation) : séparation des opérations de lecture et d'écriture, souvent associé à l'event sourcing.

#### Event-Driven Architecture (EDA)
Les services communiquent en **publiant et consommant des événements** via un broker de messages :
- **Producteurs** → publient des événements (ex. : `OrderPlaced`, `PaymentProcessed`).
- **Consommateurs** → s'abonnent aux événements pertinents.
- **Broker** : Kafka (stream processing, persistance), RabbitMQ (AMQP, routing complexe), AWS SNS/SQS.

**Event Sourcing** : l'état de l'application est dérivé d'une séquence d'événements immuables — plutôt que de stocker l'état courant, on stocke l'historique des changements.

**Avantages de l'EDA** : découplage temporel et spatial, auditabilité (log d'événements), scalabilité horizontale. **Inconvénients** : debugging complexe, consistance éventuelle (eventual consistency), nécessite une infrastructure de messaging.

#### Patterns de migration : du monolithe aux microservices
1. **Strangler Fig Pattern** (Martin Fowler) : remplacement progressif des fonctionnalités du monolithe par des microservices. Un proxy (Strangler Façade) route les requêtes vers l'ancien ou le nouveau système. Pas de migration big bang.
2. **Anti-Corruption Layer** (DDD) : couche de traduction entre le monolithe et les nouveaux microservices pour éviter que le modèle de domaine du monolithe ne contamine les nouveaux services.
3. **Decompose by Subdomain** : utiliser les Bounded Contexts DDD pour identifier les frontières naturelles des futurs microservices.
4. **Extract Service** : extraire un composant du monolithe en service indépendant, en commençant par les composants les plus stables et les moins couplés.

#### Loi de Conway
> "Les organisations qui conçoivent des systèmes produisent des systèmes qui copient les structures de communication de ces organisations." (Melvin Conway, 1968)

Les microservices impliquent une **organisation en équipes autonomes** (feature teams, squads) — chaque équipe possède un ou plusieurs services de bout en bout. C'est la **Conway's Law inversée** utilisée par Amazon ("pizza team" : une équipe = une taille de pizza).

### Avantages / Inconvénients
| Microservices — Avantages | Microservices — Inconvénients |
|-----------|---------------|
| Scaling indépendant de chaque service | Complexité opérationnelle (observabilité, réseau, sécurité) |
| Déploiement indépendant → fréquence élevée | Transactions distribuées difficiles (pas d'ACID simple) |
| Polyglottisme technologique | Latence réseau entre services |
| Résilience : une défaillance isolée n'impacte pas tout | Coût infra plus élevé (nombreux conteneurs, sidecars) |
| Alignement org/architecture (Conway's Law) | Debugging et tracing distribués complexes |

| Monolithe — Avantages | Monolithe — Inconvénients |
|-----------|---------------|
| Simplicité de développement et de debugging | Scaling global uniquement |
| Transactions ACID simples | Déploiements coordonnés (risque) |
| Faible latence (appels en mémoire) | Couplage croissant avec le temps |
| Coût opérationnel faible | Onboarding difficile sur un gros monolithe |

### Acteurs et solutions du marché
- **Orchestrateurs** : Kubernetes (CNCF) — standard de facto pour déployer et orchestrer les microservices.
- **Service Mesh** : Istio, Linkerd — gestion du trafic, sécurité mTLS, observabilité entre services.
- **API Gateway** : Kong, AWS API Gateway, NGINX, Apigee (Google).
- **Message Broker** : Apache Kafka (stream processing), RabbitMQ, AWS SQS/SNS, Azure Service Bus.
- **Frameworks microservices** : Spring Boot + Spring Cloud (Java), NestJS (Node.js), Dapr (framework agnostique de Microsoft).
- **Observabilité** : Jaeger/Zipkin (distributed tracing), Prometheus + Grafana (métriques), ELK Stack (logs).

### Cas d'usage concrets
1. **Netflix** : pionnier des microservices, Netflix a migré de son monolithe DVD vers une architecture de plus de **700 microservices** entre 2008 et 2012. Ils ont créé de nombreux patterns (Circuit Breaker avec Hystrix, Chaos Monkey pour la résilience). Résultat : 99,99 % de disponibilité pour 238 millions d'abonnés.
2. **Amazon** : Amazon a décomposé son monolithe e-commerce en services autonomes en 2002 (Jeff Bezos "API Mandate"). Chaque service est possédé par une "pizza team". Cette architecture permet de déployer plus de **150 000 fois par jour** (Amazon, 2023).
3. **Strangler Fig en France** : une grande banque française migre son core banking monolithique vers des microservices via le pattern Strangler Fig. Elle commence par extraire le service de notifications, puis les virements SEPA, puis les prêts. La migration dure 5 ans mais sans interruption de service.

### Chiffres et tendances
- **60 % des nouvelles applications** en entreprise sont conçues avec une approche microservices ou cloud-native (CNCF Survey, 2023).
- Le **monolithe modulaire** connaît un retour en grâce (DHH/Basecamp, Stack Overflow) pour les équipes < 50 développeurs.
- **Shopify** (1,7 M de marchands, Ruby on Rails) a choisi de rester sur un monolithe modulaire et de le modulariser plutôt que de migrer vers des microservices.

## Flashcards
#flashcards/Développement/Microservices_vs_monolithe #flashcards/Cloud_et_Virtualisation/Microservices_vs_monolithe
Quelle est la différence fondamentale entre microservices et monolithe en termes de déploiement ? :: Dans un **monolithe**, toute l'application est déployée comme une seule unité. Dans les **microservices**, chaque service est déployé indépendamment, avec son propre cycle de vie.

Qu'est-ce que le pattern Strangler Fig et à quoi sert-il ? :: Pattern de migration progressive de Martin Fowler : un **proxy** (Strangler Façade) redirige progressivement le trafic du monolithe vers de nouveaux microservices, évitant une migration big bang risquée.

Qu'est-ce que la loi de Conway et quelle est son implication pour les microservices ? :: "Les systèmes reflètent les structures de communication de leurs organisations." (Conway, 1968). Implication : les microservices nécessitent des **équipes autonomes** (squads) possédant chacune leurs services de bout en bout.

Qu'est-ce que le pattern Database per Service et pourquoi est-il fondamental en microservices ? :: Chaque microservice possède sa **propre base de données**, inaccessible directement par les autres services. Garantit l'**indépendance** et le **faible couplage** — sans partage de base de données.

Qu'est-ce que le Saga Pattern et pourquoi est-il nécessaire en microservices ? :: Mécanisme de gestion des **transactions distribuées** via une séquence d'événements et de compensations — puisqu'on ne peut pas avoir de transactions ACID simples entre services indépendants.

Citez 3 avantages du monolithe sur les microservices pour une petite équipe. :: Simplicité de développement et de debugging, **transactions ACID** simples, faible latence (appels en mémoire), coût opérationnel réduit.

Qu'est-ce que l'Event Sourcing et quel avantage apporte-t-il ? :: L'état de l'application est dérivé d'une **séquence d'événements immuables** plutôt que de stocker l'état courant. Avantages : auditabilité complète, capacité de rejouer l'historique, découplage.

## Sources
- Newman, S. (2021). *Building Microservices* (2e éd.). O'Reilly.
- Fowler, M. & Lewis, J. (2014). *Microservices*. martinfowler.com.
- Richardson, C. (2018). *Microservices Patterns*. Manning.
- CNCF (2023). *Annual Survey on Microservices Adoption*.
- Conway, M.E. (1968). *How Do Committees Invent?* Datamation.
- Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.

## Notions liées
- [[Architecture logicielle]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Service Mesh]]
- [[Cloud Native et 12-Factor App]]
- [[Dette technique]]
- [[TDD - BDD]]
