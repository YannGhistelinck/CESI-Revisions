---
type: notion
thèmes:
  - Développement
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# CMMI

## En bref
> **Définition** : Le CMMI (Capability Maturity Model Integration) est un référentiel d'amélioration des processus organisationnels développé par le SEI (Software Engineering Institute, Carnegie Mellon). Il décrit un ensemble de bonnes pratiques permettant à une organisation de mesurer et d'améliorer la maturité de ses processus de développement, de services ou d'acquisition.
> **Pourquoi c'est important** : Pour une DSI ou une ESN, le niveau CMMI est un signal de confiance sur la maîtrise des processus : il conditionne l'accès à certains marchés publics (défense, aéronautique), réduit les risques projet et améliore la prévisibilité des coûts et des délais.
> **Chiffres clés** :
> - Plus de **10 000 organisations** dans le monde ont réalisé une évaluation CMMI (ISACA / CMMI Institute, 2023).
> - Les organisations de niveau CMMI 3+ constatent en moyenne **34 % de réduction des défauts** et **19 % de gains de productivité** (SEI, études longitudinales).
> - Le CMMI couvre **3 domaines** : CMMI-DEV (développement), CMMI-SVC (services), CMMI-ACQ (acquisition).

## Approfondir

### Fonctionnement

#### Histoire et versions
- **CMM** (1991, Watts Humphrey / SEI) : modèle initial centré sur le développement logiciel.
- **CMMI v1.1** (2002) : intégration des modèles SW-CMM, SE-CMM et IPD-CMM.
- **CMMI v1.3** (2010) : version largement déployée, introduit CMMI-DEV, CMMI-SVC, CMMI-ACQ.
- **CMMI v2.0** (2018) : refonte par le CMMI Institute (spin-off du SEI), approche plus pratique, meilleure intégration avec l'agilité.

#### Les 5 niveaux de maturité (représentation par étapes)
| Niveau | Nom | Description |
|--------|-----|-------------|
| 1 | Initial | Processus imprévisibles, réactifs, succès dépendant des individus |
| 2 | Managed (Géré) | Processus planifiés et contrôlés au niveau projet |
| 3 | Defined (Défini) | Processus standardisés à l'échelle de l'organisation |
| 4 | Quantitatively Managed | Processus mesurés et contrôlés statistiquement |
| 5 | Optimizing | Amélioration continue basée sur les données |

#### Représentation continue vs par étapes
- **Par étapes** : évaluation globale de l'organisation sur les 5 niveaux.
- **Continue** : évaluation individuelle de chaque domaine de processus (Process Area) selon 6 niveaux de capacité (0 à 5), permettant une amélioration ciblée.

#### Domaines de processus (Process Areas) — exemples CMMI-DEV v1.3
- **Niveau 2** : Requirements Management (REQM), Project Planning (PP), Project Monitoring and Control (PMC), Supplier Agreement Management (SAM), Measurement and Analysis (MA), Process and Product Quality Assurance (PPQA), Configuration Management (CM).
- **Niveau 3** : Requirements Development (RD), Technical Solution (TS), Product Integration (PI), Verification (VER), Validation (VAL), Risk Management (RSKM), Decision Analysis and Resolution (DAR), Organizational Process Definition (OPD), Organizational Training (OT)...
- **Niveau 4** : Organizational Process Performance (OPP), Quantitative Project Management (QPM).
- **Niveau 5** : Causal Analysis and Resolution (CAR), Organizational Performance Management (OPM).

#### Processus d'évaluation — SCAMPI
L'évaluation officielle CMMI suit la méthode **SCAMPI** (Standard CMMI Appraisal Method for Process Improvement) en 3 classes :
- **SCAMPI A** : évaluation officielle, résultat certifiable, conduite par un Lead Appraiser accrédité.
- **SCAMPI B** : évaluation intermédiaire, non certifiable.
- **SCAMPI C** : auto-évaluation rapide.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Référentiel reconnu internationalement, facteur de confiance clients | Démarche longue et coûteuse (plusieurs mois à années, dizaines à centaines de k€) |
| Améliore la prévisibilité des projets et réduit les défauts | Risque de bureaucratisation et de "compliance theater" |
| Facilite l'accès aux marchés publics et défense | Peu adapté nativement aux méthodes agiles (amélioré en v2.0) |
| Structure l'amélioration continue de manière progressive | Nécessite un sponsor fort et un changement culturel profond |
| Applicable à tous les types d'organisations (DEV, SVC, ACQ) | La certification est portée par l'organisation, non par les individus |

### Acteurs et solutions du marché
- **CMMI Institute** (filiale d'ISACA depuis 2016) : propriétaire du référentiel, accrédite les Lead Appraisers.
- **ESN certifiées CMMI niveau 3+** : Infosys, Capgemini, Cognizant, TCS, Sopra Steria (pour certaines entités).
- **Consultants / cabinets spécialisés** : accompagnement à la mise en oeuvre et à la préparation des SCAMPI.
- **Outils de support** : Jira (traçabilité), Confluence (documentation des processus), outils de métriques (SonarQube, dashboards PMO).

### Cas d'usage concrets
1. **Secteur défense/aéronautique** : Thales et Airbus imposent à leurs sous-traitants logiciels un niveau CMMI 3 minimum comme condition contractuelle, assurant une maîtrise des processus de développement et de vérification.
2. **ESN en croissance** : une ESN de taille moyenne vise le niveau CMMI 2 pour formaliser ses pratiques de gestion de projet et réduire la dépendance aux personnes clés, avant de viser le niveau 3 pour standardiser à l'échelle de l'organisation.
3. **Transformation agile** : une DSI combine CMMI v2.0 et SAFe (Scaled Agile Framework) pour structurer ses pratiques de planification, mesure et amélioration tout en maintenant la flexibilité agile.

### Chiffres et tendances
- CMMI v2.0 intègre explicitement les **pratiques agiles** (sprints, backlogs) comme preuves acceptables pour certains domaines de processus.
- L'Inde concentre la majorité des certifications CMMI niveau 5 (environ **60 % des organisations certifiées CMMI 5** sont indiennes).
- En France, le CMMI est surtout présent dans les secteurs **défense, spatial et systèmes critiques** (CNES, DGA, Thales).

## Flashcards
#flashcards
Que signifie CMMI et qui l'a développé ? :: **Capability Maturity Model Integration**, développé par le **SEI** (Software Engineering Institute, Carnegie Mellon University). La version 2.0 est gérée par le **CMMI Institute** (ISACA).

Quels sont les 5 niveaux de maturité CMMI et leurs noms ? :: 1-Initial, 2-Managed (Géré), 3-Defined (Défini), 4-Quantitatively Managed, 5-Optimizing.

Quelle est la différence entre représentation par étapes et représentation continue dans CMMI ? :: Par **étapes** : niveau global de maturité de l'organisation (1 à 5). En **continue** : niveau de capacité de chaque domaine de processus individuellement (0 à 5).

Qu'est-ce que SCAMPI et quelles sont ses 3 classes ? :: **SCAMPI** est la méthode officielle d'évaluation CMMI. Classe **A** = évaluation officielle certifiable ; classe **B** = évaluation intermédiaire ; classe **C** = auto-évaluation rapide.

À partir de quel niveau CMMI les processus sont-ils standardisés à l'échelle de toute l'organisation (et non seulement par projet) ? :: **Niveau 3 — Defined** : les processus sont définis, documentés et standardisés pour l'ensemble de l'organisation.

Quelle amélioration majeure apporte CMMI v2.0 (2018) par rapport à v1.3 ? :: Une meilleure intégration avec les **méthodes agiles** (Scrum, Kanban) et une approche plus pratique et orientée résultats business.

Quels sont les 3 domaines couverts par CMMI v1.3 ? :: **CMMI-DEV** (développement), **CMMI-SVC** (services), **CMMI-ACQ** (acquisition/gestion des fournisseurs).

## Sources
- SEI / Carnegie Mellon. *CMMI for Development, Version 1.3*. CMU/SEI-2010-TR-033.
- CMMI Institute. *CMMI V2.0 Model Overview*. 2018.
- ISACA / CMMI Institute. *State of CMMI Report*. 2023.
- Humphrey, W.S. (1989). *Managing the Software Process*. Addison-Wesley.
- Gibson, D.L., Goldenson, D.R., Kost, K. (2006). *Performance Results of CMMI-Based Process Improvement*. SEI Technical Report.

## Notions liées
- [[Qualité logicielle — normes et modèles]]
- [[Analyse de code (SAST - DAST)]]
- [[Dette technique]]
- [[Clean Code et refactoring]]
- [[Maintenance logicielle]]
