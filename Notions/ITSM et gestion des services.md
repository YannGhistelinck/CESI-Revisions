---
type: notion
thèmes:
  - Optimisation du SI
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# ITSM et gestion des services

## En bref

### Définition
L'IT Service Management (ITSM) désigne l'ensemble des activités, politiques et processus permettant de concevoir, délivrer, gérer et améliorer les services informatiques fournis aux utilisateurs et aux métiers. Il couvre la gestion des incidents, des problèmes, des changements, des actifs et de la relation client IT.

### Pourquoi c'est important
L'ITSM est le moteur opérationnel de la DSI. Il garantit la continuité de service, la satisfaction utilisateur et la maîtrise des risques. En 2024, la transformation ITSM (adoption de XLA, automatisation via AI Ops) est au cœur de la modernisation des DSI.

### Chiffres clés
- 72 % des DSI considèrent l'ITSM comme critique pour la continuité opérationnelle (HDI, 2023)
- Le MTTR moyen en entreprise est de 4h ; les meilleures pratiques ITIL le ramènent sous 1h
- ISO/IEC 20000 : plus de 8 000 organisations certifiées dans le monde

---

## Approfondir

### Fonctionnement

#### SLA / OLA / UC — La chaîne des engagements de service
- **SLA (Service Level Agreement)** : contrat entre la DSI et le client/métier. Définit les niveaux de service (disponibilité, MTTR, délai de résolution). Ex. : disponibilité applicative 99,5 %.
- **OLA (Operational Level Agreement)** : accord interne entre équipes IT. Ex. : l'équipe réseau s'engage à intervenir en 30 min sur un incident critique.
- **UC (Underpinning Contract)** : contrat avec un fournisseur externe. Ex. : contrat de maintenance matérielle avec un délai d'intervention de 4h.

#### Gestion des incidents
- Objectif : rétablir le service le plus rapidement possible
- Classification : P1 (critique) → P4 (faible)
- Processus : détection → enregistrement → catégorisation → priorisation → investigation → résolution → clôture
- KPIs : MTTR, taux de résolution au premier contact (FCR), taux de réouverture

#### Gestion des problèmes
- Objectif : identifier et éliminer les causes racines des incidents récurrents
- Deux modes : réactif (post-incident) et proactif (analyse tendancielle)
- Livrés : Known Error Database (KEDB), workarounds, RFC (Request for Change)
- Méthode : analyse des causes racines (RCA) — 5 Pourquoi, diagramme d'Ishikawa

#### Gestion des changements
- Objectif : minimiser les risques liés aux modifications du SI
- Types de changements :
  - **Standard** : pré-approuvé, à faible risque (ex. ajout d'un utilisateur)
  - **Normal** : soumis au CAB pour évaluation
  - **Urgent** : approuvé par le ECAB (Emergency CAB)
- **CAB (Change Advisory Board)** : comité d'approbation des changements, composé de représentants techniques et métiers

#### CMDB et CI
- **CMDB (Configuration Management Database)** : référentiel central de tous les éléments de configuration du SI
- **CI (Configuration Item)** : tout élément géré dans la CMDB (serveur, application, service, contrat…)
- Relation avec les incidents/problèmes/changements : chaque ticket est lié à un ou plusieurs CI
- Outils : ServiceNow, iTop, Lansweeper

#### Service Desk
- Point de contact unique (SPOC) entre les utilisateurs et la DSI
- Niveaux de support : N1 (premier niveau, résolution ou escalade), N2 (spécialistes techniques), N3 (experts / éditeurs)
- KPIs : satisfaction utilisateur (CSAT), taux de résolution N1, temps de prise en charge

#### Catalogue de services
- Liste structurée de tous les services IT disponibles pour les utilisateurs
- Deux parties : catalogue de services métier (vue utilisateur) et catalogue technique (vue DSI)
- Outil clé pour la communication DSI/métiers et la gestion des SLA

#### XLA — Experience Level Agreement
- Évolution des SLA : mesurer l'expérience réelle des utilisateurs plutôt que de simples métriques techniques
- Indicateurs : NPS (Net Promoter Score), CSAT, DEX (Digital Employee Experience)
- Tendance 2023-2025 : complémentaire aux SLA, intégré dans les outils ITSM modernes

#### ISO/IEC 20000
- Norme internationale pour la gestion des services IT
- Couvre les exigences d'un SMS (Service Management System)
- Compatible avec ITIL 4, COBIT, ISO 27001
- Certification pour les fournisseurs de services IT (infogérance, ESN)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Standardisation et traçabilité des opérations | Risque de sur-processualisation |
| Réduction du MTTR et des incidents récurrents | Coût d'implémentation d'un outil ITSM |
| Amélioration de la satisfaction utilisateur | Adoption difficile par les équipes techniques |
| Conformité réglementaire (ISO 20000, SOC2) | CMDB difficile à maintenir à jour |
| Base solide pour l'automatisation | Résistance au changement culturel |

### Acteurs et solutions

| Acteur / Solution | Rôle |
|-------------------|------|
| ServiceNow | Leader ITSM enterprise, CMDB, AI Ops |
| Jira Service Management (Atlassian) | ITSM orienté développeurs et équipes Agile |
| BMC Helix ITSM | ITSM enterprise, gestion des actifs |
| Freshservice | ITSM cloud, mid-market |
| iTop | ITSM open source |
| Axelos / PeopleCert | Formation et certification ITIL |
| BSI, AFNOR | Certification ISO/IEC 20000 |

### Cas d'usage concrets

- **DSI grande distribution** : mise en place d'un service desk N1/N2/N3 avec SLA contractualisé (P1 < 30 min, P2 < 2h) et CMDB couvrant 15 000 CI — réduction de 30 % des incidents majeurs en 6 mois
- **Secteur santé** : gestion des changements avec CAB hebdomadaire et gel des changements pendant les périodes critiques (pic d'activité aux urgences)
- **ESN en infogérance** : certification ISO/IEC 20000 pour rassurer les clients sur la qualité de service et remporter des appels d'offres publics
- **Fintech** : adoption des XLA pour mesurer le DEX des traders et prioriser les investissements IT sur les points de friction les plus impactants

### Chiffres et tendances

- AI Ops : 40 % des grandes DSI utilisent l'IA pour la corrélation d'incidents en 2025 (Gartner)
- Automatisation ITSM : les bots de service desk résolvent jusqu'à 30 % des tickets N1 sans intervention humaine
- Tendance "shift-left" : remonter la résolution au niveau N1 pour réduire les coûts
- DEX (Digital Employee Experience) : nouvel indicateur phare des DSI en 2024-2025

---

## Flashcards
#flashcards/Optimisation_du_SI/ITSM_et_gestion_des_services #flashcards/Management_et_stratégie/ITSM_et_gestion_des_services

Quelle est la différence entre SLA, OLA et UC ? :: SLA : engagement DSI → client/métier. OLA : accord interne entre équipes IT. UC : contrat avec un fournisseur externe. Ensemble, ils forment la chaîne des engagements de service.

Quelle est la différence entre gestion des incidents et gestion des problèmes ? :: La gestion des incidents vise à rétablir le service rapidement (symptôme). La gestion des problèmes cherche à éliminer la cause racine pour éviter la récurrence.

Qu'est-ce qu'une CMDB et à quoi sert-elle ? :: Configuration Management Database : référentiel de tous les éléments de configuration (CI) du SI. Elle lie les actifs IT aux incidents, problèmes et changements pour améliorer la traçabilité et l'impact analysis.

Quel est le rôle du CAB ? :: Change Advisory Board : comité qui évalue et approuve les changements normaux pour minimiser les risques de perturbation du SI.

Qu'est-ce qu'un XLA et en quoi diffère-t-il d'un SLA ? :: Un XLA (Experience Level Agreement) mesure l'expérience réelle de l'utilisateur (NPS, CSAT, DEX) là où le SLA mesure des métriques techniques. Le XLA place l'humain au centre de la performance IT.

Que couvre la norme ISO/IEC 20000 ? :: Les exigences pour établir, implémenter, maintenir et améliorer un Système de Management des Services (SMS) IT. C'est la norme de référence pour la certification des fournisseurs ITSM.

Quels sont les 3 types de changements ITIL ? :: Standard (pré-approuvé, faible risque), Normal (soumis au CAB), Urgent (approuvé par le Emergency CAB en cas de crise).

---

## Sources

- Axelos, *ITIL Foundation: ITIL 4 Edition*, TSO, 2019
- ISO/IEC 20000-1:2018, *Service Management System Requirements*
- HDI, *Technical Support and Help Desk Practices & Salary Report*, 2023
- Gartner, *Magic Quadrant for ITSM Tools*, 2024

---

## Notions liées

- [[ITIL 4]]
- [[Gouvernance IT]]
- [[PCA - PRA]]
- [[Observabilité]]
- [[SRE (Site Reliability Engineering)]]
- [[DevOps]]
