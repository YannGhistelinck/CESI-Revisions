---
type: notion
thèmes:
  - Optimisation du SI
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# MTTR - MTBF

## En bref

### Définition
- **MTBF (Mean Time Between Failures)** : temps moyen entre deux pannes successives — mesure la **fiabilité** d'un système.
- **MTTR (Mean Time To Recover/Repair/Resolve/Respond)** : famille de métriques mesurant le temps nécessaire à la restauration d'un service après une panne — mesure la **résilience** et la **réactivité**.
- Ces indicateurs sont au coeur du pilotage de la **disponibilité** (Availability) et de la **résilience** du SI.

### Pourquoi c'est important
La disponibilité des services IT est directement liée à la performance business. MTBF et MTTR sont les deux leviers fondamentaux : augmenter le MTBF (moins de pannes) et réduire le MTTR (récupération plus rapide) sont les objectifs complémentaires des équipes SRE, Ops et cybersécurité.

### Chiffres clés
- Le coût moyen d'une panne IT est de **5 600 $/min** pour une grande entreprise (Gartner)
- Les équipes "Elite" DORA ont un **MTTR < 1 heure** pour les incidents de production
- Un MTTR moyen dans l'industrie est de **4 à 8 heures** pour les incidents P1
- Réduire le MTTR de **50 %** grâce à l'automatisation est un objectif atteignable selon PagerDuty
- La disponibilité **99,9 %** implique un MTBF >> MTTR (le service fonctionne la grande majorité du temps)

---

## Approfondir

### Fonctionnement

#### La famille MTTR

MTTR est un terme générique couvrant 4 métriques distinctes :

| Acronyme | Nom complet | Ce que ça mesure |
|---|---|---|
| **MTTA** | Mean Time To Acknowledge | Temps entre l'alerte et la prise en charge par un ingénieur |
| **MTTD** | Mean Time To Detect | Temps entre l'apparition du problème et sa détection |
| **MTTR** | Mean Time To Recover | Temps entre la détection et le retour à l'état normal |
| **MTTF** | Mean Time To Failure | Temps moyen de fonctionnement avant la première panne (systèmes non réparables) |

#### MTBF — Mean Time Between Failures

**Formule :**
> MTBF = Temps total de fonctionnement / Nombre de pannes

**Exemple :**
- Système opérationnel 8 760h/an avec 4 pannes → MTBF = 2 190h (≈ 91 jours)

**Fiabilité vs temps :**
- Courbe en baignoire (Bathtub Curve) : pannes précoces → période stable → vieillissement

#### Disponibilité (Availability)

**Formule :**
> Availability = MTBF / (MTBF + MTTR) × 100

**Exemple :**
- MTBF = 1 000h, MTTR = 1h → Availability = 1 000/1 001 = **99,9 %**
- MTBF = 1 000h, MTTR = 10h → Availability = 1 000/1 010 = **99,01 %**

Implication : **réduire le MTTR a un impact plus rapide sur la disponibilité** que d'augmenter le MTBF dans les systèmes complexes.

#### Cycle de vie d'un incident

```
Panne survient
     ↓
Détection (→ MTTD)
     ↓
Alerte reçue → Acknowledge (→ MTTA)
     ↓
Diagnostic & résolution
     ↓
Retour à la normale (→ MTTR)
     ↓
Post-mortem (→ améliore MTBF et MTTR futurs)
```

#### Résilience vs Fiabilité vs Disponibilité

| Concept | Définition | Métrique |
|---|---|---|
| **Fiabilité** | Capacité à fonctionner sans panne | MTBF, MTTF |
| **Résilience** | Capacité à se remettre d'une panne | MTTR |
| **Disponibilité** | Proportion du temps opérationnel | Availability % |
| **Maintenabilité** | Facilité à réparer/restaurer | MTTR |

#### MTTR en cybersécurité

En sécurité, le MTTR prend une dimension spécifique :
- **MTTD (Mean Time To Detect)** : temps avant de détecter une intrusion
  - Moyenne mondiale : **197 jours** (IBM Cost of Data Breach Report 2023)
- **MTTR cyber** : temps pour contenir et éradiquer une menace
  - Moyenne mondiale : **70 jours** supplémentaires pour la remédiation
- Ces métriques justifient l'investissement dans les **SIEM, EDR, SOAR**

#### Chaos Engineering et MTTR

Le Chaos Engineering (Netflix, Google) consiste à injecter délibérément des pannes pour :
1. Tester la résilience réelle (vs théorique)
2. Réduire le MTTR en pratiquant les runbooks
3. Identifier les points de défaillance uniques (SPOF)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Objectivation de la fiabilité et résilience | MTBF/MTTR sont des moyennes : masquent les cas extrêmes |
| Base de calcul de la disponibilité SLA | Ne distinguent pas la sévérité des incidents |
| Pilotage des équipes SRE et Ops | Difficiles à comparer entre organisations (périmètres différents) |
| Justification des investissements en automatisation | MTTD cyber élevé (197j) difficile à réduire rapidement |
| Alimentation des post-mortems | Risque de Goodhart : optimiser le MTTR en déclarant les incidents résolus trop tôt |

### Acteurs

- **SRE/Monitoring** : Google, PagerDuty, Datadog, Dynatrace, New Relic, Prometheus
- **ITSM** : ServiceNow, Jira Service Management (suivi des incidents)
- **Cybersécurité** : IBM X-Force, CrowdStrike, Splunk (SIEM/SOAR pour MTTD/MTTR cyber)
- **Chaos Engineering** : Netflix (Chaos Monkey), Gremlin, AWS Fault Injection Simulator
- **Référentiels** : ITIL 4, Google SRE Book, DORA Report

### Cas d'usage

- **SRE** : tableau de bord MTTR par sévérité d'incident, objectif MTTR P1 < 30 min
- **Infrastructure cloud** : MTBF des instances EC2, automatisation du failover
- **Cybersécurité** : MTTD et MTTR comme KRI pour justifier l'investissement SIEM/SOAR
- **PCA/PRA** : RTO (Recovery Time Objective) = MTTR cible contractuel
- **Post-mortem** : analyse des causes racines pour améliorer MTBF (réduire les pannes)

### Chiffres complémentaires

- **RTO (Recovery Time Objective)** = MTTR cible, défini dans le PCA/PRA
- **RPO (Recovery Point Objective)** = perte de données maximale acceptable (distinct du MTTR)
- Les équipes "Elite" DORA : MTTR < **1 heure**, MTBF implicitement > 1 semaine entre incidents
- Réduction du MTTD de **197 jours** à < 30 jours = objectif phare des SOC modernes

---

## Flashcards
#flashcards/Optimisation_du_SI/MTTR_MTBF #flashcards/Cybersécurité/MTTR_MTBF

Quelle est la formule de la disponibilité (Availability) à partir de MTBF et MTTR ? :: Availability = MTBF / (MTBF + MTTR). Exemple : MTBF=1000h, MTTR=1h → 99,9 % de disponibilité.

Quelle est la différence entre MTBF et MTTF ? :: MTBF s'applique aux systèmes réparables (temps entre deux pannes successives). MTTF s'applique aux systèmes non réparables (temps moyen avant la première défaillance définitive).

Quelles sont les 4 déclinaisons de MTTR ? :: MTTA (acknowledge), MTTD (detect), MTTR (recover/restore), et parfois MTTF (first response).

Quel est le MTTD moyen mondial pour détecter une violation de données ? :: 197 jours selon le IBM Cost of Data Breach Report 2023 — ce délai justifie l'investissement dans les SIEM et EDR.

Pourquoi réduire le MTTR a-t-il un impact plus immédiat sur la disponibilité qu'augmenter le MTBF ? :: Parce que MTTR est directement sous contrôle des équipes (runbooks, automatisation, on-call). Augmenter le MTBF nécessite des changements architecturaux profonds et plus lents.

Quelle est la relation entre MTTR et RTO (PCA/PRA) ? :: Le RTO (Recovery Time Objective) est le MTTR cible défini dans le Plan de Continuité d'Activité. Il représente la durée maximale d'indisponibilité acceptable après un incident.

Qu'est-ce que le Chaos Engineering et pourquoi réduit-il le MTTR ? :: Pratique consistant à injecter délibérément des pannes en production pour tester la résilience réelle. Réduit le MTTR car les équipes pratiquent les runbooks et identifient les SPOF avant les incidents réels.

---

## Sources

- Google — "Site Reliability Engineering" (SRE Book, sre.google)
- IBM Security — "Cost of a Data Breach Report 2023"
- DORA — "Accelerate State of DevOps Report 2023"
- PagerDuty — "State of Incident Management 2022"
- ITIL 4 Foundation — Service Management Framework

---

## Notions liées

[[SLA - SLO - SLI]] · [[SRE (Site Reliability Engineering)]] · [[PCA - PRA]] · [[Observabilité]] · [[DORA Metrics]] · [[Chaos Engineering]] · [[SIEM]] · [[SOAR]] · [[Cyber-résilience]] · [[ChatOps]] · [[Système d'Information (SI)]]
