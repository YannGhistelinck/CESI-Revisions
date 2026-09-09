---
type: notion
thèmes:
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# RACI et outils de gouvernance projet

## En bref

### Définition
Le RACI est un outil de gouvernance qui clarifie les rôles et responsabilités de chaque acteur dans un projet ou un processus. Couplé aux outils de gouvernance projet (business case, COPIL, charte de projet, registre des risques), il structure la prise de décision et la responsabilisation pour garantir la réussite des projets IT.

### Pourquoi c'est important
L'absence de clarté sur les responsabilités est l'une des premières causes d'échec projet. Dans un contexte multi-équipes et multi-fournisseurs (typique des DSI modernes), le RACI est indispensable pour éviter les angles morts, les doublons et les conflits de décision. C'est un outil quotidien du chef de projet et du DSI.

### Chiffres clés
- 39 % des projets IT échouent par manque de clarté sur les rôles (PMI, Pulse of the Profession, 2023)
- 70 % des projets dépassent leur budget ou leurs délais (Gartner)
- Le business case réduit de 25 % le risque d'abandon prématuré d'un projet (PMI)

---

## Approfondir

### Fonctionnement

#### La matrice RACI
Chaque tâche ou décision est attribuée à 4 types de rôles :

| Lettre | Rôle | Signification |
|--------|------|---------------|
| **R** | Responsible | Réalise le travail. Peut être plusieurs personnes. |
| **A** | Accountable | Responsable final (signataire, décideur). Un seul par tâche. |
| **C** | Consulted | Consulté avant la décision ou l'action. Communication bilatérale. |
| **I** | Informed | Informé après la décision. Communication unilatérale. |

**Règles d'or du RACI :**
- Toujours un seul **A** par ligne (sinon personne n'est vraiment responsable)
- Éviter les colonnes trop chargées en **R** (surcharge) ou trop vides (goulets)
- Distinguer clairement **C** (avis nécessaire) de **I** (pour information seulement)
- Variantes : RASCI (S = Support), DACI (Driver, Approver, Contributors, Informed), RACI-VS

#### Construction d'un RACI
1. Lister toutes les tâches/livrables/décisions du projet
2. Identifier tous les acteurs (personnes, équipes, fournisseurs)
3. Pour chaque tâche × acteur, attribuer R, A, C ou I
4. Valider avec toutes les parties prenantes
5. Faire vivre la matrice (révisions à chaque phase projet)

#### Business Case
Document de justification d'un projet, soumis au COPIL pour décision de lancement :
- **Problématique** : contexte et enjeux
- **Objectifs** : SMART, alignés sur la stratégie
- **Options analysées** : scénarios comparés (make/buy/do nothing)
- **Bénéfices attendus** : qualitatifs et quantitatifs (ROI, TCO, NPV)
- **Coûts** : CAPEX, OPEX, ressources humaines
- **Risques** : matrice risques/impacts
- **Recommandation** : option préconisée avec plan de mise en œuvre
- **Critères de succès** et KPIs de suivi

#### COPIL — Comité de Pilotage
Instance de gouvernance d'un projet ou programme :
- **Fréquence** : mensuelle (projet normal), bimensuelle (projet critique)
- **Composition** : sponsor (A), DSI ou délégué, chef de projet, représentants métiers clés, parfois fournisseurs
- **Ordre du jour type** : avancement vs plan, indicateurs qualité/délai/budget, risques/actions, décisions requises
- **Livrables** : compte-rendu, tableau de bord projet, décisions tracées (log de décisions)

#### Gouvernance de projet — Autres outils

| Outil | Description |
|-------|-------------|
| Charte de projet | Document fondateur : objectifs, périmètre, équipe, budget, délais |
| Plan de management de projet | Détail des 10 domaines de connaissance PMI |
| Registre des risques | Liste, probabilité, impact, plan de réponse |
| Registre des parties prenantes | Identification, pouvoir/intérêt, stratégie d'engagement |
| Tableau de bord projet | RAG (Red/Amber/Green) sur délais, budget, qualité, risques |
| Plan de communication | Qui reçoit quoi, quand, par quel canal |
| Matrice d'escalade | Seuils de déclenchement et chaîne d'escalade |

#### PMI vs PRINCE2 — Comparaison des approches de gouvernance

| Dimension | PMI (PMBOK) | PRINCE2 |
|-----------|-------------|---------|
| Origine | USA, universel | UK, secteur public |
| Structure | 10 domaines de connaissance | 7 principes, 7 thèmes, 7 processus |
| Gouvernance | Chef de projet central | Project Board (sponsor, senior user, senior supplier) |
| Flexibilité | Forte (adaptatif) | Prescriptif mais adaptable |
| Certification | PMP | PRINCE2 Practitioner |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Clarté des responsabilités | Peut devenir trop lourd si trop détaillé |
| Réduction des conflits de rôle | Nécessite un effort d'animation pour être maintenu |
| Facilite l'onboarding de nouveaux membres | Pas adapté aux organisations très agiles |
| Traçabilité des décisions (COPIL) | Risque de "réunionite" si gouvernance mal calibrée |
| Business case : objectivise les décisions | Business case peut être biaisé par les commanditaires |

### Acteurs et solutions

| Acteur / Solution | Rôle |
|-------------------|------|
| PMI | PMBOK, certification PMP, standard de référence mondial |
| Axelos / PeopleCert | PRINCE2, MSP (Managing Successful Programmes) |
| Microsoft Project | Planification et suivi de projet |
| Jira, Asana, Monday.com | Gestion de projet collaborative et agile |
| Confluence | Documentation projet (charte, RACI, COPIL CR) |
| Power BI | Tableaux de bord projet et portfolio |

### Cas d'usage concrets

- **DSI grande entreprise** : RACI défini pour la migration ERP (SAP S/4HANA) impliquant 6 équipes internes et 3 prestataires — réduction de 40 % des conflits de responsabilité vs projet précédent
- **Projet transversal SI/RH** : business case chiffrant un ROI de 3 ans pour convaincre le COMEX de financer un SIRH (€800K investis, €1,2M économisés sur 3 ans)
- **Programme de transformation digitale** : COPIL mensuel avec tableau de bord RAG pour 12 projets simultanés, escalade automatique si budget dépassé de plus de 10 %
- **ESN en infogérance** : RACI contractualisé dans le SLA pour clarifier les responsabilités entre le client et le prestataire sur chaque type d'incident

### Chiffres et tendances

- 55 % des chefs de projet estiment que des rôles mal définis sont la principale cause d'échec projet (PMI, 2023)
- Tendance 2024-2025 : gouvernance projet Agile (hybride RACI + rôles Scrum), Product Owner comme A sur les user stories
- OKR (Objectives and Key Results) : nouveau cadre de définition des objectifs qui complète le business case
- Adoption croissante des outils no-code (Monday.com, Notion) pour les tableaux de bord projet en remplacement de MS Project

---

## Flashcards
#flashcards/Management_et_stratégie/RACI_et_outils_de_gouvernance_projet

Que signifie RACI ? :: Responsible (réalise), Accountable (responsable final — un seul par tâche), Consulted (consulté avant), Informed (informé après). Outil de clarification des rôles dans un projet ou processus.

Quelle est la règle d'or du RACI sur le rôle A ? :: Il ne peut y avoir qu'un seul Accountable par tâche ou décision. S'il y en a plusieurs, personne n'est vraiment responsable — c'est la principale cause de blocage.

Quels sont les éléments obligatoires d'un business case ? :: Problématique, objectifs SMART, options analysées, bénéfices attendus (ROI/TCO), coûts (CAPEX/OPEX), risques, recommandation et critères de succès.

Quel est l'ordre du jour type d'un COPIL ? :: Avancement vs plan, indicateurs QCD (Qualité-Coût-Délai), risques et actions en cours, décisions requises, points d'escalade. Clôture par compte-rendu et log de décisions.

Quelle est la différence entre C et I dans le RACI ? :: C (Consulted) : l'acteur est consulté avant la décision, communication bilatérale. I (Informed) : l'acteur est informé après la décision, communication unilatérale. Confondre les deux surcharge les processus.

Quelle est la différence principale entre PMI (PMBOK) et PRINCE2 ? :: PMI est orienté chef de projet central avec 10 domaines de connaissance, flexible et universel. PRINCE2 est orienté Project Board (gouvernance collective) avec 7 principes/thèmes/processus, plus prescriptif et utilisé surtout au UK.

---

## Sources

- PMI, *A Guide to the Project Management Body of Knowledge (PMBOK), 7th Edition*, 2021
- Axelos, *PRINCE2 Practitioner Manual*, 2017
- PMI, *Pulse of the Profession 2023*
- Gartner, *IT Project and Portfolio Management Report*, 2024

---

## Notions liées

- [[Gouvernance IT]]
- [[ITIL 4]]
- [[SAFe et agilité à l'échelle]]
- [[TOGAF et architecture d'entreprise]]
- [[CMMI]]
