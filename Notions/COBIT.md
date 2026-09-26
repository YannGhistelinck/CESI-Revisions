---
type: notion
thèmes:
  - Management et stratégie
  - Optimisation du SI
statut: pas vu
dernière_révision: 
catégorie: framework
---

# COBIT

![[N — COBIT.mp3]]
## En bref
> **Définition** : COBIT (Control Objectives for Information and Related Technologies) est un cadre de gouvernance et de management des systèmes d'information édité par l'ISACA. Dans sa version actuelle (COBIT 2019), il fournit un modèle complet pour aligner l'IT sur les objectifs métier, gérer les risques et créer de la valeur. COBIT définit 40 objectifs de gouvernance et de management regroupés en 5 domaines, avec un système de niveaux de capacité (0 à 5) pour évaluer la maturité de chaque processus.
> **Pourquoi c'est important** : Sans cadre de gouvernance IT structuré, les investissements technologiques risquent d'être déconnectés de la stratégie d'entreprise, les risques mal maîtrisés et la conformité réglementaire difficile à démontrer. COBIT est le référentiel le plus reconnu internationalement pour la gouvernance IT et sert de socle aux audits SI (notamment pour les commissaires aux comptes et les auditeurs internes).
> **Chiffres clés** :
> - COBIT est utilisé dans plus de 180 pays et traduit en 40 langues (ISACA, 2024).
> - 72 % des entreprises du Fortune 500 utilisent COBIT comme cadre de gouvernance IT (ISACA).
> - Le marché mondial de la gouvernance IT atteindra 18,4 Md$ en 2028 (MarketsandMarkets).

## Approfondir

### Fonctionnement

**Les 5 domaines COBIT 2019**

| Domaine | Code | Description | Nb d'objectifs |
|---------|------|-------------|----------------|
| **Évaluer, Diriger, Surveiller** | EDM | Gouvernance : le conseil d'administration fixe la direction | 5 |
| **Aligner, Planifier, Organiser** | APO | Stratégie IT, architecture, innovation, risques, RH | 14 |
| **Construire, Acquérir, Implémenter** | BAI | Programmes, projets, changements, actifs IT | 11 |
| **Livrer, Servir, Supporter** | DSS | Opérations, incidents, problèmes, continuité, sécurité | 6 |
| **Surveiller, Évaluer, Apprécier** | MEA | Conformité, audit interne, assurance qualité | 4 |

**Distinction gouvernance / management**
COBIT sépare clairement :
- **Gouvernance** (EDM) : responsabilité du conseil d'administration — évaluer, diriger, surveiller. Fixe les objectifs, arbitre les priorités, contrôle la conformité.
- **Management** (APO, BAI, DSS, MEA) : responsabilité de la DSI — planifier, construire, livrer, surveiller. Exécute la stratégie définie par la gouvernance.

**Cascade d'objectifs (Goals Cascade)**
Mécanisme central de COBIT pour aligner IT et métier :
1. **Besoins des parties prenantes** → 2. **Objectifs d'entreprise** (13 objectifs génériques) → 3. **Objectifs d'alignement** (13 objectifs IT) → 4. **Objectifs de gouvernance/management** (40 processus)

Chaque lien est pondéré (primaire/secondaire), permettant de prioriser les processus à améliorer en fonction des enjeux stratégiques de l'entreprise.

**Modèle de maturité (niveaux de capacité)**

| Niveau | Nom | Description |
|--------|-----|-------------|
| 0 | Processus incomplet | Pas de processus ou échec à atteindre les objectifs |
| 1 | Processus réalisé | Le processus atteint ses objectifs mais de façon non formalisée |
| 2 | Processus géré | Planifié, suivi, ajusté |
| 3 | Processus établi | Basé sur un processus défini et standardisé |
| 4 | Processus prévisible | Opère dans des limites définies, mesuré quantitativement |
| 5 | Processus optimisé | Amélioration continue, innovation |

**Design Factors (COBIT 2019)**
COBIT 2019 introduit 11 "design factors" pour adapter le cadre au contexte de l'entreprise : stratégie d'entreprise, taille, profil de risque, modèle de sourcing IT, méthode d'implémentation, paysage des menaces, exigences de conformité, etc. Cela évite l'approche "one size fits all" des versions précédentes.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Cadre complet couvrant gouvernance ET management | Complexité de mise en œuvre (40 processus) |
| Alignement IT-métier structuré (Goals Cascade) | Perçu comme bureaucratique dans les PME |
| Compatible avec ITIL, ISO 27001, TOGAF, CMMI | Nécessite des compétences spécialisées |
| Modèle de maturité objectif et mesurable | Coût de certification et de formation |
| Reconnu internationalement pour l'audit IT | Adaptation au contexte agile encore limitée |
| Design Factors pour personnaliser l'approche | Documentation volumineuse |

### COBIT vs ITIL vs TOGAF

| Critère | COBIT | ITIL | TOGAF |
|---------|-------|------|-------|
| Focus | Gouvernance IT globale | Gestion des services IT | Architecture d'entreprise |
| Éditeur | ISACA | Axelos / PeopleCert | The Open Group |
| Scope | Stratégie → opérations | Opérations et services | Architecture et transformation |
| Public cible | DSI, auditeurs, RSSI | Équipes IT opérationnelles | Architectes d'entreprise |
| Complémentarité | Chapeau de gouvernance | S'intègre sous COBIT (DSS) | S'intègre sous COBIT (APO) |

**COBIT est souvent utilisé comme cadre fédérateur**, avec ITIL pour les processus opérationnels et TOGAF pour l'architecture.

### Cas d'usage concrets

1. **Audit SI d'une PME industrielle** : une entreprise de 500 salariés utilise COBIT pour structurer son audit SI annuel. La cascade d'objectifs identifie les 12 processus prioritaires (sur 40). L'évaluation de maturité révèle que la gestion des incidents (DSS02) est au niveau 1 → plan d'action pour atteindre le niveau 3 en 18 mois.

2. **Conformité RGPD via COBIT** : COBIT 2019 mappe ses processus sur les exigences RGPD. Les processus APO01 (cadre de gestion IT), APO12 (gestion des risques), DSS05 (sécurité) et MEA03 (conformité) sont utilisés comme base pour démontrer la conformité aux autorités de contrôle.

3. **Intégration COBIT + ITIL dans un groupe bancaire** : COBIT fournit le cadre de gouvernance (reporting au comité d'audit, gestion des risques IT), tandis qu'ITIL structure les processus opérationnels (gestion des incidents, changements, niveaux de service). Les deux référentiels sont mappés pour éviter les doublons.

### Chiffres et tendances
- ISACA compte plus de 170 000 membres dans 188 pays (2024).
- La certification COBIT Foundation est la plus demandée pour les profils gouvernance IT, avec +35 % de croissance annuelle.
- COBIT 2019 est aligné sur 17 standards internationaux (ISO 27001, ISO 38500, ITIL, TOGAF, CMMI, PMBOK, etc.).
- 65 % des grandes entreprises européennes utilisent COBIT dans le cadre de leur mise en conformité DORA (Deloitte, 2024).

## Flashcards
#flashcards/Management_et_stratégie/COBIT #flashcards/Optimisation_du_SI/COBIT

Qu'est-ce que COBIT et quel est son éditeur ? :: COBIT (Control Objectives for Information and Related Technologies) est un cadre de gouvernance et de management IT édité par l'ISACA. Il définit 40 objectifs répartis en 5 domaines pour aligner l'IT sur les objectifs métier.

Quels sont les 5 domaines de COBIT 2019 ? :: EDM (Évaluer, Diriger, Surveiller — gouvernance), APO (Aligner, Planifier, Organiser), BAI (Construire, Acquérir, Implémenter), DSS (Livrer, Servir, Supporter), MEA (Surveiller, Évaluer, Apprécier).

Quelle est la différence entre gouvernance et management dans COBIT ? :: La gouvernance (EDM) est la responsabilité du conseil d'administration : fixer la direction, arbitrer, contrôler. Le management (APO, BAI, DSS, MEA) est la responsabilité de la DSI : planifier, construire, livrer, surveiller.

Qu'est-ce que la cascade d'objectifs (Goals Cascade) dans COBIT ? :: Mécanisme d'alignement : besoins des parties prenantes → objectifs d'entreprise → objectifs d'alignement IT → objectifs de gouvernance/management. Permet de prioriser les processus à améliorer en fonction de la stratégie.

Comment COBIT, ITIL et TOGAF se complètent-ils ? :: COBIT sert de cadre fédérateur de gouvernance IT globale. ITIL s'intègre sous le domaine DSS pour la gestion des services. TOGAF s'intègre sous le domaine APO pour l'architecture d'entreprise.

Qu'est-ce qu'un "Design Factor" dans COBIT 2019 ? :: Un des 11 paramètres contextuels (stratégie, taille, profil de risque, sourcing, menaces, conformité…) permettant d'adapter COBIT au contexte spécifique de l'entreprise, évitant l'approche "one size fits all".

## Sources
- ISACA — *COBIT 2019 Framework: Governance and Management Objectives*, 2018
- ISACA — *COBIT 2019 Design Guide*, 2018
- De Haes, S., Van Grembergen, W. — *Enterprise Governance of IT*, Springer, 2015
- Deloitte — *IT Governance Trends Survey*, 2024

## Notions liées
- [[ITIL 4]]
- [[TOGAF et architecture d'entreprise]]
- [[Gouvernance IT]]
- [[Audit SI]]
- [[ISO 27001 - 27002]]
- [[CMMI]]
- [[DORA (Digital Operational Resilience Act)]]
- [[KPI et pilotage de la performance]]
