---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Architecture logicielle

![[N — Architecture logicielle.mp3]]
## En bref
> **Définition** : L'architecture logicielle désigne l'ensemble des décisions structurelles fondamentales qui définissent l'organisation d'un système : ses composants, leurs responsabilités, les relations entre eux et les principes guidant leur conception. C'est la discipline qui permet de gérer la complexité à l'échelle d'un système entier.
> **Pourquoi c'est important** : Pour une DSI, les décisions d'architecture sont les plus coûteuses à remettre en cause. Une mauvaise architecture crée une dette structurelle qui contraint l'évolution du système pendant des années. A contrario, une bonne architecture permet l'évolutivité, la testabilité et l'indépendance technologique.
> **Chiffres clés** :
> - Le coût de correction d'une décision d'architecture incorrecte est **1 000 fois plus élevé** en production qu'en phase de conception (NIST).
> - **70 % des projets de transformation** échouent à cause de défis architecturaux (McKinsey Digital, 2020).
> - La **Clean Architecture** de Robert C. Martin est citée dans plus de **60 % des projets** visant une architecture testable et maintenable (sondages communauté Java/DotNet).

## Approfondir

### Fonctionnement

#### Concepts fondamentaux : couplage et cohésion
- **Couplage** : mesure du degré de dépendance entre modules. Un **couplage faible** est souhaitable : les modules peuvent évoluer indépendamment.
  - Types : couplage de données (données passées en paramètre), de contrôle, commun (global), de contenu (accès aux internals d'un autre module — le pire).
- **Cohésion** : mesure du degré de responsabilité focalisée d'un module. Une **cohésion forte** est souhaitable : chaque module fait une seule chose et bien.
  - Règle d'or : **fort cohésion + faible couplage** = architecture maintenable.

#### Architecture en couches (Layered Architecture)
La plus répandue historiquement. Organisation typique en **4 couches** :
1. **Présentation** (UI/API) : interaction avec l'utilisateur ou le client.
2. **Application** (Use Cases) : orchestration de la logique métier.
3. **Domaine** : entités et règles métier pures.
4. **Infrastructure** : persistance, messagerie, services externes.

Problème classique : les dépendances "tombent" vers le bas, ce qui couple la logique métier à l'infrastructure.

#### Clean Architecture (Robert C. Martin, 2017)
La **Clean Architecture** résout le problème des dépendances de l'architecture en couches via la **règle de dépendance** :
> "Les dépendances de code source ne peuvent pointer que vers l'intérieur."

Organisation en cercles concentriques :
- **Centre** : Entités (règles métier de l'entreprise) — aucune dépendance externe.
- **Use Cases** : règles métier de l'application.
- **Interface Adapters** : controllers, presenters, gateways.
- **Frameworks & Drivers** : UI, DB, web, appareils — couche la plus externe.

Conséquence : la logique métier est **indépendante** du framework, de la base de données et de l'interface. Elle est **testable** isolément.

#### Architecture Hexagonale (Ports and Adapters, Alistair Cockburn, 2005)
Aussi appelée **Ports & Adapters**. L'application est au centre, entourée de **ports** (interfaces) et d'**adaptateurs** (implémentations concrètes) :
- **Ports** : interfaces définies par l'application (ex. : `UserRepository`, `EmailService`).
- **Adaptateurs primaires** (driving) : ce qui appelle l'application (HTTP controller, CLI, tests).
- **Adaptateurs secondaires** (driven) : ce que l'application appelle (PostgreSQL, SMTP, Kafka).

Similaire à la Clean Architecture mais avec une terminologie différente. Permet de **swapper** les implémentations sans modifier le domaine.

#### Domain-Driven Design — DDD (Eric Evans, 2003)
Le **DDD** est une approche de conception centrée sur le **modèle du domaine métier**. Concepts clés :
- **Ubiquitous Language** : langage partagé entre développeurs et experts métier, utilisé dans le code et les conversations.
- **Bounded Context** : limite explicite dans laquelle un modèle s'applique (ex. : "Commande" dans le contexte Vente ≠ "Commande" dans le contexte Logistique).
- **Entités** : objets avec une identité persistante (ex. : `Client` avec un `id`).
- **Value Objects** : objets définis par leurs attributs, sans identité (ex. : `Adresse`, `MonnaieEUR`).
- **Aggregates** : cluster d'entités formant une unité transactionnelle (ex. : `Commande` + `LignesDeCommande`).
- **Domain Events** : événements significatifs dans le domaine (ex. : `CommandePassée`, `PaiementReçu`).
- **Repositories** : abstraction de la persistance des aggregates.
- **Domain Services** : logique métier ne relevant d'aucune entité.

DDD **Tactique** (patterns ci-dessus) + DDD **Stratégique** (Context Map, Bounded Contexts, Anti-Corruption Layer).

#### Architecture Decision Records — ADR
Un **ADR** est un document court capturant une décision architecturale importante, son contexte et ses conséquences. Format type :
```markdown
# ADR-001 : Utilisation de PostgreSQL comme base de données principale

## Statut
Accepté

## Contexte
Le système nécessite des transactions ACID et des requêtes relationnelles complexes.

## Décision
Nous utilisons PostgreSQL.

## Conséquences
+ Support transactions ACID, JSON natif, extensions riches.
- Moins adapté aux workloads de type time-series ou graphe.
```
Les ADR sont versionnés avec le code (ex. : dans `/docs/adr/`). Ils constituent la **mémoire architecturale** du projet.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Clean Architecture : testabilité maximale, indépendance technologique | Courbe d'apprentissage élevée (DDD, Clean Arch) |
| DDD : alignement fort entre code et métier | Sur-engineering possible pour des systèmes simples |
| Hexagonale : facilité de swap des adaptateurs | Prolifération de couches et d'abstractions |
| ADR : traçabilité et mémoire des décisions | ADR nécessitent une discipline d'équipe pour être maintenus |
| Faible couplage : évolutivité et maintenabilité | Architecture hexagonale peut complexifier les projets simples |

### Acteurs et solutions du marché
- **Archi** : outil open source de modélisation d'architecture (notation ArchiMate).
- **C4 Model** (Simon Brown) : framework de documentation d'architecture en 4 niveaux (Context, Container, Component, Code) — très populaire.
- **Structurizr** : outil pour créer des diagrammes C4 as code.
- **PlantUML / Mermaid** : diagrammes d'architecture as code.
- **Backstage** (Spotify) : portail de gestion des composants et de la documentation architecturale.
- **Arc42** : template de documentation architecturale structurée.

### Cas d'usage concrets
1. **Migration vers la Clean Architecture** : une équipe Symfony migre progressivement son application vers la Clean Architecture. Le domaine métier est extrait dans un module `src/Domain` sans aucune dépendance Symfony. Les use cases sont testables sans base de données. La durée des builds de tests unitaires passe de 8 min à 45 secondes.
2. **DDD et Bounded Contexts** : une plateforme e-commerce Française identifie 6 Bounded Contexts (Catalogue, Commande, Livraison, Facturation, Client, Promotions) via des ateliers Event Storming. Chaque contexte est implémenté par une équipe autonome avec son propre modèle, évitant le "grand modèle de données unifié" impossible à maintenir.
3. **ADR en pratique** : une équipe DevOps adopte les ADR pour documenter ses choix Kubernetes vs ECS, PostgreSQL vs MongoDB, gRPC vs REST. 18 mois plus tard, lors de l'arrivée de nouveaux membres, les ADR permettent de comprendre en 2 heures les raisons de chaque choix technique.

### Chiffres et tendances
- Le **C4 Model** est adopté par plus de **500 000 équipes** selon Simon Brown (2023).
- **Event Storming** (Alberto Brandolini) est utilisé dans 40 % des projets DDD pour la découverte collaborative du domaine.
- Les formations DDD (DDD Europe, Domain-Driven Design Crew) connaissent une croissance de **25 % par an** depuis 2018.

## Flashcards
#flashcards/Développement/Architecture_logicielle
Quelle est la règle de dépendance fondamentale de la Clean Architecture ? :: Les dépendances de code source ne peuvent pointer que **vers l'intérieur** des cercles concentriques — jamais vers l'extérieur. Le domaine ne dépend de rien.

Quelle est la différence entre l'architecture hexagonale et la Clean Architecture ? :: Conceptuellement similaires (domaine au centre, indépendance technologique), mais terminologie différente : l'hexagonale parle de **ports** (interfaces) et **adaptateurs** (implémentations), la Clean Arch de couches concentriques.

Qu'est-ce qu'un Bounded Context en DDD ? :: Une **limite explicite** dans laquelle un modèle de domaine particulier s'applique et reste cohérent. Un même concept (ex. "Commande") peut avoir des significations différentes selon le contexte.

Qu'est-ce qu'un ADR et où les stocker ? :: Un **Architecture Decision Record** est un document court capturant une décision architecturale importante, son contexte et ses conséquences. Ils sont versionnés avec le code (ex. `/docs/adr/`).

Définissez couplage faible et cohésion forte et expliquez pourquoi ce sont des objectifs. :: **Couplage faible** : peu de dépendances entre modules → évolution indépendante. **Cohésion forte** : chaque module a une responsabilité unique et focalisée → lisibilité et testabilité. Ensemble : architecture maintenable et évolutive.

Quels sont les concepts tactiques fondamentaux du DDD ? :: Entités (identité persistante), Value Objects (définis par leurs attributs), Aggregates (unités transactionnelles), Domain Events, Repositories, Domain Services, Ubiquitous Language.

Qu'est-ce que le C4 Model et quels sont ses 4 niveaux ? :: Framework de documentation architecturale de Simon Brown : **C**ontext (système dans son environnement), **C**ontainer (applications/services), **C**omponent (composants internes), **C**ode (classes/modules).

## Sources
- Martin, R.C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
- Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.
- Cockburn, A. (2005). *Hexagonal Architecture*. alistair.cockburn.us.
- Brown, S. (2018). *Software Architecture for Developers*. Lean Publishing.
- Nygard, M. (2011). *Documenting Architecture Decisions*. thinkrelevance.com.

## Notions liées
- [[Microservices vs monolithe]]
- [[Clean Code et refactoring]]
- [[Dette technique]]
- [[TDD - BDD]]
- [[DDD]]
- [[Conteneurisation (Docker - Kubernetes)]]
