---
type: notion
thèmes:
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# SLA - SLO - SLI

![[N — SLA - SLO - SLI.mp3]]
## En bref

### Définition
- **SLI (Service Level Indicator)** : mesure technique brute d'un aspect de la performance d'un service (ex : taux de disponibilité réel).
- **SLO (Service Level Objective)** : objectif interne cible pour un SLI (ex : disponibilité ≥ 99,9 %).
- **SLA (Service Level Agreement)** : contrat formalisé entre un fournisseur et un client définissant les niveaux de service attendus, avec pénalités en cas de non-respect.
- **XLA (Experience Level Agreement)** : évolution du SLA centrée sur l'expérience perçue par l'utilisateur (NPS, satisfaction) plutôt que sur des métriques techniques.

### Pourquoi c'est important
Ces notions structurent la relation entre la DSI et ses clients (internes ou externes). Elles permettent de définir des engagements mesurables, de piloter la qualité de service, d'aligner les équipes SRE/Ops sur des objectifs concrets et de justifier les niveaux d'investissement en infrastructure.

### Chiffres clés
- Un SLA à **99,9 %** autorise **8h45 min** d'indisponibilité par an
- Un SLA à **99,99 %** (four nines) n'autorise que **52 min** d'indisponibilité par an
- Un SLA à **99,999 %** (five nines) n'autorise que **5 min 15 s** d'indisponibilité par an
- **80 % des organisations** mesurent leurs SLA uniquement en disponibilité, négligeant la performance et l'expérience (Gartner, 2023)
- Les violations de SLA coûtent en moyenne **3 à 5 % du contrat** en pénalités

---

## Approfondir

### Fonctionnement

#### La hiérarchie SLI → SLO → SLA

```
SLI (mesure réelle) → SLO (objectif interne) → SLA (engagement contractuel)
     99,97 %              ≥ 99,9 %                   ≥ 99,5 %
```

Le SLO est toujours plus strict que le SLA : il sert de filet de sécurité interne.

#### SLI — Service Level Indicator

Exemples de SLI selon le type de service :

| Type de service | SLI typiques |
|---|---|
| **API REST** | Taux de requêtes réussies (2xx/total), latence p99 |
| **Application web** | Disponibilité (uptime), temps de chargement |
| **Base de données** | Latence de lecture/écriture, taux d'erreur |
| **Pipeline de données** | Fraîcheur des données, taux de complétion |
| **Service e-mail** | Taux de délivrabilité, délai de distribution |

#### SLO — Service Level Objective

- Objectif interne, non contractuel
- Défini par les équipes SRE avec les Product Managers
- Associé à un **Error Budget** : budget d'erreur autorisé

**Error Budget :**
> Si SLO = 99,9 %, l'error budget mensuel = 0,1 % × 30 jours × 24h = **43,2 min/mois**

Quand l'error budget est épuisé :
- Gel des déploiements
- Priorité aux actions de fiabilité plutôt qu'aux nouvelles features

#### SLA — Service Level Agreement

Structure d'un SLA :

| Section | Contenu |
|---|---|
| **Périmètre** | Services couverts, exclusions |
| **Engagements** | Disponibilité, performance, support |
| **Mesure** | Méthode de calcul, outils, période |
| **Pénalités** | Crédit de service, compensation financière |
| **Escalade** | Procédure en cas de violation |
| **Révision** | Fréquence de revue contractuelle |

#### OLA — Operational Level Agreement

- Accord interne entre équipes IT (ex : entre l'équipe réseau et l'équipe applicative)
- Soutient le SLA externe, non visible du client final

#### XLA — Experience Level Agreement

- Évolution post-SLA centrée sur la **perception utilisateur**
- Mesurée via : NPS (Net Promoter Score), CSAT, CES (Customer Effort Score)
- Répond à la limite des SLA purement techniques : "Le système est disponible mais inutilisable"
- Adopté par les DSI orientées Digital Workplace et ITSM moderne

#### NPS — Net Promoter Score

- Mesure la probabilité de recommandation (0 à 10)
- **Promoteurs** : 9-10 | **Passifs** : 7-8 | **Détracteurs** : 0-6
- **NPS = % Promoteurs − % Détracteurs**
- NPS > 50 = excellent | NPS > 70 = world class

#### Tableau de disponibilité (Nines)

| SLA | Indisponibilité/an | Indisponibilité/mois |
|---|---|---|
| 99 % (two nines) | 3 j 15 h | 7 h 18 min |
| 99,9 % (three nines) | 8 h 45 min | 43,8 min |
| 99,95 % | 4 h 22 min | 21,9 min |
| 99,99 % (four nines) | 52 min 36 s | 4 min 23 s |
| 99,999 % (five nines) | 5 min 15 s | 26 s |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Clarification des responsabilités et attentes | SLA mal définis créent des litiges contractuels |
| Base objective pour les pénalités et crédits | Focalisation technique ignorant l'expérience réelle |
| Error budget = régulation dev vs ops (SRE) | Five nines souvent inutiles et très coûteux |
| XLA améliore l'alignement sur la valeur perçue | Mesure de l'expérience subjective difficile à automatiser |
| Pilotage de la qualité de service dans le temps | Risque de jeu sur les définitions pour éviter les pénalités |

### Acteurs

- **ITSM/ITIL** : ServiceNow, Jira Service Management, Freshservice
- **Monitoring SLI** : Datadog, Dynatrace, New Relic, Prometheus/Grafana
- **SRE** : Google (créateur du concept SRE et SLO/Error Budget)
- **XLA** : Nexthink, Lakeside Software, 1E (Digital Employee Experience)
- **Référentiel** : ITIL 4 (SLA, OLA), Google SRE Book (SLO, Error Budget)

### Cas d'usage

- **Cloud public** : AWS SLA à 99,99 % pour EC2, avec crédit de service en cas de violation
- **ESN** : SLA d'infogérance définissant MTTR < 4h pour les incidents P1
- **Application critique** : SLO interne à 99,95 % avec error budget géré par l'équipe SRE
- **Digital Workplace** : XLA mesurant le NPS des employés sur les outils IT (Teams, laptop, VPN)
- **API publique** : SLA de performance (p99 < 200 ms) et disponibilité (99,9 %)

### Chiffres complémentaires

- Google cible un **error budget à 0** pour ses services critiques (pas 100 % de SLO respecté)
- **99,99 %** est le seuil typique des services financiers critiques (banking, trading)
- La différence de coût entre **99,9 %** et **99,999 %** de disponibilité est souvent **10x** en infrastructure

---

## Flashcards
#flashcards/Optimisation_du_SI/SLA_SLO_SLI

Quelle est la hiérarchie SLI → SLO → SLA ? :: SLI = mesure technique réelle. SLO = objectif interne cible (plus strict que le SLA). SLA = engagement contractuel avec le client, avec pénalités.

Qu'est-ce qu'un error budget et comment est-il calculé ? :: C'est le budget d'indisponibilité autorisé défini par le SLO. Exemple : SLO 99,9 % → error budget = 0,1 % × 30 jours × 24h = 43,2 min/mois. Quand il est épuisé, les déploiements sont gelés.

Combien de temps d'indisponibilité autorise un SLA à 99,9 % par an ? :: 8 heures et 45 minutes par an (soit 43,8 min/mois).

Qu'est-ce qu'un XLA et en quoi diffère-t-il d'un SLA ? :: Un XLA (Experience Level Agreement) mesure l'expérience perçue par l'utilisateur (NPS, CSAT) plutôt que des métriques techniques. Un service peut respecter son SLA tout en offrant une mauvaise expérience utilisateur.

Quelle est la formule du NPS ? :: NPS = % de Promoteurs (notes 9-10) − % de Détracteurs (notes 0-6). Il varie de -100 à +100. Un NPS > 50 est excellent.

Quelle est la différence entre SLA et OLA ? :: Le SLA est un accord contractuel entre le fournisseur IT et le client final. L'OLA (Operational Level Agreement) est un accord interne entre équipes IT qui soutient le SLA.

Pourquoi viser 99,999 % (five nines) est-il souvent contre-productif ? :: Le coût en infrastructure et en processus est exponentiellement plus élevé, et la plupart des services n'ont pas besoin de ce niveau. La différence de coût entre 99,9 % et 99,999 % est souvent un facteur 10x.

---

## Sources

- Google — "Site Reliability Engineering" (SRE Book, 2016 — sre.google)
- ITIL 4 Foundation — AXELOS/PeopleCert
- Gartner — "SLA Best Practices" (2023)
- Nexthink — "XLA Guide: Measuring Employee Experience" (2022)
- AWS Service Level Agreements (aws.amazon.com/legal/service-level-agreements)

---

## Notions liées

[[MTTR - MTBF]] · [[SRE (Site Reliability Engineering)]] · [[Observabilité]] · [[KPI et pilotage de la performance]] · [[DORA Metrics]] · [[PCA - PRA]] · [[Métriques de sécurité]] · [[Système d'Information (SI)]] · [[ChatOps]]
