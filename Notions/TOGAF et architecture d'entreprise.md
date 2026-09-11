---
type: notion
thèmes:
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# TOGAF et architecture d'entreprise

## En bref

### Définition
TOGAF (The Open Group Architecture Framework) est le référentiel mondial le plus utilisé pour l'architecture d'entreprise (Enterprise Architecture — EA). Il fournit une méthode (ADM — Architecture Development Method), un vocabulaire commun et un ensemble de bonnes pratiques pour aligner l'architecture du SI sur la stratégie de l'organisation.

### Pourquoi c'est important
Sans architecture d'entreprise, le SI croît de manière désorganisée (urbanisation non maîtrisée, dette technique, silos applicatifs). TOGAF permet au DSI de justifier les investissements SI, d'anticiper les transformations et de communiquer avec le COMEX sur la trajectoire du SI.

### Chiffres clés
- TOGAF est utilisé par 80 % des entreprises du Fortune 500 (The Open Group, 2023)
- Plus de 100 000 professionnels certifiés TOGAF dans le monde
- TOGAF Standard v10 publié en 2022 — version la plus récente

---

## Approfondir

### Fonctionnement

#### Architecture d'entreprise (EA)
L'EA est la discipline qui aligne la stratégie, les processus métiers, les données et les systèmes d'information. Elle se décompose en 4 domaines :
1. **Architecture métier (Business Architecture)** : processus, organigrammes, objectifs stratégiques
2. **Architecture des données (Data Architecture)** : modèles de données, flux, gouvernance des données
3. **Architecture applicative (Application Architecture)** : cartographie des applications, flux d'échange
4. **Architecture technologique (Technology Architecture)** : infrastructure, réseaux, plateformes

#### ADM — Architecture Development Method
Méthode itérative en phases de TOGAF :
- **Phase préliminaire** : adaptation du cadre et définition des principes d'architecture
- **Phase A — Vision de l'architecture** : définir la portée et les objectifs du projet d'architecture
- **Phase B — Architecture métier** : modéliser les processus et capacités cibles
- **Phase C — Architectures des SI** : applications et données
- **Phase D — Architecture technologique** : infrastructure cible
- **Phase E — Opportunités et solutions** : planification de la transition
- **Phase F — Planification de la migration** : roadmap détaillée
- **Phase G — Gouvernance de l'implémentation** : supervision des projets de réalisation
- **Phase H — Gestion du changement d'architecture** : pilotage de l'évolution
- **Gestion des exigences** : transversale à toutes les phases

#### Référentiel d'architecture (Architecture Repository)
Stockage des livrables : paysage de l'architecture, modèles de référence, standards, bonnes pratiques.

#### SDSI — Schéma Directeur du Système d'Information
- Document stratégique qui définit la trajectoire du SI sur 3 à 5 ans
- Contenu : état des lieux (AS-IS), vision cible (TO-BE), roadmap des projets, budget prévisionnel
- Validé par le COMEX et le COPIL SI
- TOGAF ADM est la méthode pour le construire

#### Urbanisation du SI
- Métaphore de l'urbanisme : organiser le SI comme une ville (quartiers, îlots, lots)
- Objectif : cohérence, interopérabilité, agilité et maîtrise de la complexité
- **Plan d'urbanisme SI** : cartographie des zones fonctionnelles et des flux
- Zones typiques : Zone de présentation (front-end), Zone de traitement (back-end), Zone de ressources (données, référentiels), Zone d'échange (APIs, ESB)
- Complémentaire à TOGAF : l'urbanisation est la pratique française d'EA

#### Autres référentiels EA
- **Zachman Framework** : matrice à double entrée (Quoi/Comment/Où/Qui/Quand/Pourquoi × Contextuel/Conceptuel/Logique/Physique/Détaillé)
- **ArchiMate** : langage de modélisation EA standardisé par The Open Group, souvent utilisé avec TOGAF

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Référentiel universel et reconnu | Complexité et lourdeur du cadre complet |
| Alignement SI/stratégie structuré | Mise en œuvre longue (18-36 mois) |
| Réduction de la dette technique | Compétences rares et coûteuses |
| Facilite les audits et la gouvernance | Risque de produire des livrables sans usage réel |
| Base pour le SDSI et la roadmap IT | Nécessite une forte adhésion du management |

### Acteurs et solutions

| Acteur / Solution | Rôle |
|-------------------|------|
| The Open Group | Propriétaire de TOGAF et ArchiMate |
| Sparx Systems (Enterprise Architect) | Outil de modélisation EA / ArchiMate |
| BiZZdesign (Hopex) | Plateforme EA enterprise |
| LeanIX | EA orientée cloud et SaaS |
| Mega International (Hopex) | EA + gouvernance des données |
| Orbus Software (iServer) | EA mid-market |

### Cas d'usage concrets

- **Groupe bancaire** : utilisation de TOGAF ADM pour construire le SDSI 2025-2030, cartographier 400 applications et établir une roadmap de décommissionnement du legacy (économie cible : 15 M€/an)
- **Administration publique** : plan d'urbanisme SI pour rationaliser les échanges inter-administrations et réduire les doublons applicatifs (-30 % d'applications en 3 ans)
- **Industriel** : architecture cible SAP S/4HANA avec TOGAF pour préparer la migration et gérer l'impact sur les 80 applications périphériques
- **Startup scale-up** : architecture applicative ArchiMate pour documenter la plateforme avant une levée de fonds et rassurer les investisseurs sur la scalabilité du SI

### Chiffres et tendances

- 60 % des grandes DSI ont un programme EA formalisé (Gartner, 2024)
- Tendance 2024-2025 : EA + cloud (cartographie multi-cloud, FinOps) et EA + IA (gouvernance des modèles)
- TOGAF v10 intègre pour la première fois des modules adaptables (TOGAF Series Guides) pour les petites organisations et l'EA agile
- ArchiMate 3.2 (2022) : nouveau standard de modélisation EA

---

## Flashcards
#flashcards/Management_et_stratégie/TOGAF_et_architecture_d_entreprise

Qu'est-ce que l'ADM de TOGAF ? :: Architecture Development Method : méthode itérative en 9 phases (A à H + gestion des exigences) pour développer et gérer l'architecture d'entreprise, de la vision jusqu'à la gouvernance de l'implémentation.

Quels sont les 4 domaines de l'architecture d'entreprise ? :: Architecture métier (Business), Architecture des données, Architecture applicative, Architecture technologique. TOGAF les couvre tous dans les phases B, C et D.

Qu'est-ce qu'un SDSI ? :: Schéma Directeur du Système d'Information : document stratégique définissant l'état des lieux (AS-IS), la vision cible (TO-BE) et la roadmap des projets IT sur 3 à 5 ans, validé par le COMEX.

Quelle est la différence entre TOGAF et l'urbanisation du SI ? :: TOGAF est un cadre global et international d'EA. L'urbanisation du SI est une pratique française qui organise le SI par zones/quartiers/îlots, complémentaire à TOGAF dans sa dimension applicative et d'échanges.

Quel est le rôle d'ArchiMate dans l'EA ? :: ArchiMate est le langage de modélisation standardisé de The Open Group pour représenter l'architecture d'entreprise. Il est souvent utilisé avec TOGAF pour produire des cartographies lisibles et cohérentes.

Quelle est la phase A de TOGAF ADM ? :: La "Vision de l'architecture" : définir la portée du projet d'architecture, identifier les parties prenantes, établir les objectifs et obtenir l'approbation pour lancer le cycle ADM.

---

## Sources

- The Open Group, *TOGAF Standard, 10th Edition*, 2022
- The Open Group, *ArchiMate 3.2 Specification*, 2022
- Gartner, *Enterprise Architecture Programs Report*, 2024
- Cigref, *Urbanisation des systèmes d'information*, 2020

---

## Notions liées

- [[Gouvernance IT]]
- [[ITIL 4]]
- [[Legacy et dette technique]]
- [[Microservices vs monolithe]]
- [[Data Governance]]
- [[RACI et outils de gouvernance projet]]
