---
type: notion
thèmes:
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Système d'Information (SI)

## En bref

### Définition
Un Système d'Information (SI) est l'ensemble organisé de ressources (humaines, matérielles, logicielles, procédures et données) permettant de collecter, stocker, traiter et distribuer l'information nécessaire au fonctionnement d'une organisation.

### Pourquoi c'est important
Le SI est le système nerveux de l'entreprise : il conditionne la prise de décision, la performance opérationnelle, la relation client et la compétitivité. Son optimisation est un levier stratégique directement lié à la valeur métier.

### Chiffres clés
- Le marché mondial des services SI dépasse **1 200 Md$ en 2024** (Gartner)
- Les entreprises consacrent en moyenne **4 à 6 % de leur CA** aux dépenses IT
- **70 % des projets de transformation SI** échouent à atteindre leurs objectifs initiaux (McKinsey)
- Le coût moyen d'une heure d'indisponibilité SI est estimé à **5 600 $/min** pour les grandes entreprises (Gartner)

---

## Approfondir

### Fonctionnement

Un SI s'articule autour de quatre fonctions fondamentales :

1. **Collecte** — acquisition des données (capteurs, formulaires, APIs, ERP)
2. **Stockage** — bases de données relationnelles, NoSQL, data lakes, archives
3. **Traitement** — calculs, workflows, règles métier, algorithmes
4. **Diffusion** — dashboards, rapports, APIs, notifications, portails

#### Composantes du SI

| Composante | Description | Exemples |
|---|---|---|
| **Matérielle** | Serveurs, postes, réseaux, stockage | Dell, Cisco, NetApp |
| **Logicielle** | Applications métier, OS, middleware | SAP, Salesforce, Oracle |
| **Données** | Référentiels, bases, entrepôts | SGBD, Data Warehouse |
| **Procédures** | Règles, processus, gouvernance | ITIL, COBIT |
| **Humaine** | Utilisateurs, DSI, administrateurs | Équipes IT & métier |

#### Niveaux du SI (modèle de Anthony)

- **Niveau opérationnel** — Traitement des transactions quotidiennes (ERP, CRM)
- **Niveau tactique** — Pilotage et reporting (BI, tableaux de bord)
- **Niveau stratégique** — Aide à la décision (EIS, DSS)

#### Architectures SI

- **Monolithique** — Application centralisée, simple mais peu évolutive
- **SOA (Service-Oriented Architecture)** — Services réutilisables exposés via des contrats
- **Microservices** — Services autonomes, déployables indépendamment
- **Event-driven** — Communication asynchrone par événements

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Centralisation et cohérence de l'information | Coût de mise en oeuvre et de maintenance élevé |
| Automatisation des processus répétitifs | Risque de dépendance technologique (vendor lock-in) |
| Aide à la décision en temps réel | Complexité croissante avec la dette technique |
| Traçabilité et auditabilité | Surface d'attaque cyber étendue |
| Collaboration inter-services facilitée | Résistance au changement des utilisateurs |

### Acteurs

- **Éditeurs ERP** : SAP, Oracle, Microsoft Dynamics, Sage
- **Intégrateurs SI** : Capgemini, Accenture, Sopra Steria, Atos
- **Cabinets conseil** : McKinsey, Gartner, Forrester
- **Référentiels** : COBIT (gouvernance), ITIL (services IT), TOGAF (architecture d'entreprise)
- **Normalisateurs** : ISO (ISO/IEC 38500 pour la gouvernance IT)

### Cas d'usage

- **Transformation digitale** : migration d'un SI legacy vers une architecture cloud-native
- **Fusion-acquisition** : cartographie et rationalisation des SI de deux entités
- **Conformité RGPD** : cartographie des données personnelles dans le SI
- **Réduction des coûts** : audit du shadow IT, consolidation des licences logicielles

### Chiffres complémentaires

- **70 %** des budgets IT sont consacrés au maintien en condition opérationnelle (run), contre 30 % pour l'innovation (build)
- **85 %** des entreprises du Fortune 500 utilisent SAP comme ERP central
- Durée de vie moyenne d'un SI legacy : **20 à 30 ans**

---

## Flashcards
#flashcards/Optimisation_du_SI/Système_d_Information_SI

Qu'est-ce qu'un Système d'Information ? :: Ensemble organisé de ressources (humaines, matérielles, logicielles, données, procédures) permettant de collecter, stocker, traiter et distribuer l'information au sein d'une organisation.

Quelles sont les 4 fonctions fondamentales d'un SI ? :: Collecte, Stockage, Traitement, Diffusion.

Quels sont les 3 niveaux du SI selon le modèle d'Anthony ? :: Niveau opérationnel (transactions), niveau tactique (pilotage), niveau stratégique (aide à la décision).

Quelle est la différence entre architecture SOA et microservices ? :: SOA expose des services via des contrats partagés (ESB central) ; les microservices sont des unités autonomes déployables indépendamment, sans point de contrôle central.

Qu'est-ce que le shadow IT ? :: L'ensemble des applications et outils informatiques utilisés par les employés sans validation ni contrôle de la DSI, créant des risques de sécurité et de gouvernance.

Qu'est-ce que TOGAF ? :: The Open Group Architecture Framework — référentiel de conception d'architecture d'entreprise permettant de structurer et aligner le SI avec la stratégie business.

Pourquoi le ratio run/build est-il un indicateur clé pour la DSI ? :: Il mesure la part du budget IT consacrée à la maintenance (run) vs à l'innovation (build). Un ratio trop élevé côté run indique un SI obsolète freinant la transformation.

---

## Sources

- Gartner — IT Spending Forecast 2024
- McKinsey — "Unlocking success in digital transformations" (2018)
- ISO/IEC 38500:2015 — Gouvernance IT
- COBIT 2019 — ISACA
- TOGAF Standard — The Open Group

---

## Notions liées

[[Gouvernance IT]] · [[Legacy et dette technique]] · [[Architecture logicielle]] · [[DevOps]] · [[KPI et pilotage de la performance]] · [[Métriques de pilotage projet]] · [[Frameworks de gestion de projet]] · [[SLA - SLO - SLI]] · [[Observabilité]]
