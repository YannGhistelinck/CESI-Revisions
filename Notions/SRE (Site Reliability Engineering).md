---
type: notion
thèmes:
  - Développement
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# SRE (Site Reliability Engineering)

## En bref
> **Définition** : Le Site Reliability Engineering (SRE) est une discipline née chez Google en 2003, formalisée par Ben Treynor Sloss (VP Engineering Google) et documentée dans le livre *Site Reliability Engineering* (O'Reilly, 2016). Le SRE applique les principes du génie logiciel aux problèmes opérationnels, en traitant l'exploitation de systèmes à grande échelle comme un problème d'ingénierie. Les concepts clés sont : **SLI/SLO/SLA**, **error budget**, **toil** et **blameless post-mortem**.
> **Pourquoi c'est important** : Le SRE résout la tension fondamentale entre fiabilité (vouloir par les Ops) et vélocité (voulée par les Dev) via un mécanisme objectif : l'**error budget**. Si le système est trop fiable, on peut prendre plus de risques (déployer davantage). S'il dépasse son quota d'erreurs, on arrête les déploiements et on se concentre sur la fiabilité. Le SRE est la mise en pratique du DevOps dans des environnements à très grande échelle.
> **Chiffres clés** :
> - Google gère des millions de requêtes par seconde avec des SRE teams gérant moins de 5 % de "toil" (travail manuel répétitif).
> - Les organisations SRE matures restaurent les services 2 600 fois plus vite que les organisations traditionnelles (DORA, 2023).
> - Le marché des outils SRE / AIOps atteindra 13 Md$ en 2028 (Grand View Research).

## Approfondir

### Fonctionnement

**SLI, SLO, SLA — la hiérarchie des indicateurs de fiabilité**

| Concept | Définition | Exemple |
|---------|-----------|---------|
| **SLI** (Service Level Indicator) | Métrique quantitative mesurant un aspect du service | Taux de requêtes HTTP réussies (status < 500) |
| **SLO** (Service Level Objective) | Objectif cible pour un SLI sur une période | 99,9 % de requêtes réussies sur 30 jours glissants |
| **SLA** (Service Level Agreement) | Engagement contractuel avec pénalités financières | 99,9 % de disponibilité, sinon remise de 10 % |

Les SLO sont définis en interne (objectif d'équipe) ; les SLA sont contractuels (client/fournisseur). Un SLO est toujours plus strict que le SLA correspondant (marge de sécurité).

**Types de SLI courants**
- **Disponibilité** : % de requêtes réussies (ex. : 99,9 %)
- **Latence** : % de requêtes servies sous un seuil (ex. : 95 % < 200 ms)
- **Throughput** : volume traité (ex. : > 1 000 requêtes/s)
- **Correctness** : % de réponses correctes (ex. : 99,99 % pour un service de paiement)
- **Fraîcheur** : âge des données (ex. : données < 1 minute)

**Error Budget**
Concept central du SRE : le budget d'erreur est le complément du SLO.
```
SLO = 99,9 % → Error Budget = 0,1 % = 43,2 minutes/mois
SLO = 99,99 % → Error Budget = 0,01 % = 4,32 minutes/mois
```
Si l'error budget est consommé → on arrête les déploiements, on se concentre sur la fiabilité.
Si l'error budget est intact → on peut déployer plus agressivement.
Ce mécanisme rend la décision de déployer ou non **objective et dépolitisée**.

**Toil — définition et élimination**
Le "toil" est le travail opérationnel manuel, répétitif, sans valeur ajoutée à long terme et scalant linéairement avec la taille du service (ex. : relancer un pod manuellement, répondre à des alertes à la main, provisionner des serveurs un à un). Les SRE doivent maintenir leur toil sous 50 % de leur temps de travail et l'éliminer via l'automatisation.

**Blameless Post-Mortem**
Analyse d'un incident sans recherche de responsabilité individuelle ("who did it"), focalisée sur les causes systémiques ("why did the system fail"). Format standard :
1. **Timeline** : chronologie précise des événements
2. **Impact** : durée, utilisateurs affectés, SLO consommé
3. **Root Cause Analysis** : causes profondes (5 Whys, diagramme d'Ishikawa)
4. **Action items** : corrections techniques et systémiques, avec propriétaire et deadline
5. **Lessons learned** : ce qui a bien fonctionné, ce qui doit changer

**Chaos Engineering**
Pratique consistant à injecter des défaillances contrôlées en production pour tester la résilience du système. Popularisée par Netflix (Chaos Monkey, Simian Army). Permet de valider les SLO en conditions réelles et de découvrir les faiblesses avant qu'un incident réel ne les révèle.

**On-call et escalade**
Les SRE assurent des astreintes (on-call) avec des runbooks documentés pour chaque type d'alerte. Principe : une alerte qui ne peut pas être traitée par un runbook est soit du toil (à automatiser), soit une alerte mal définie (à supprimer ou reformuler).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Cadre objectif pour arbitrer fiabilité vs vélocité | Mise en place complexe (définir de bons SLI/SLO nécessite de la maturité) |
| Réduction du toil et de la charge opérationnelle | Culturellement difficile (abandon de la culture du "zéro incident") |
| Incidents mieux gérés et appris (post-mortem) | Profils SRE rares et coûteux (hybride Dev+Ops+Infra) |
| Fiabilité mesurable et améliorable | Risque d'over-engineering si appliqué à des petits systèmes |
| Alignement business (SLA contractuels fondés sur des SLO réalistes) | Tension possible avec les équipes Dev si l'error budget est mal géré |
| Culture d'apprentissage (blameless → innovation) | Besoin d'une observabilité robuste en prérequis |

### Acteurs et solutions du marché
| Catégorie | Solutions |
|-----------|-----------|
| Gestion des alertes / on-call | PagerDuty, Opsgenie (Atlassian), VictorOps |
| Observabilité (prérequis SRE) | Prometheus + Grafana, Datadog, Dynatrace, New Relic |
| Gestion des SLO | Sloth (open source), Nobl9, Datadog SLO, Grafana SLO |
| Chaos Engineering | Chaos Monkey (Netflix), LitmusChaos (CNCF), Gremlin |
| Incident Management | FireHydrant, Blameless, Incident.io, PagerDuty |
| Runbooks automatisés | Rundeck, Cortex, Backstage (Spotify) |

### Cas d'usage concrets
1. **Google** : inventeur du SRE, Google publie en open source ses pratiques via les livres SRE (2016, 2018). Chaque service Google a des SLO publics (ex. : Gmail 99,9 %). Les équipes SRE gèrent des milliards de requêtes avec des budgets d'erreur formalisés et des post-mortems partagés en interne.
2. **Spotify** : après avoir adopté le SRE, Spotify a réduit son MTTR de 4 heures à 12 minutes grâce à des runbooks automatisés et un framework de SLO centralisé (Backstage). Les équipes produit disposent de dashboards d'error budget en temps réel.
3. **Criteo** : la plateforme publicitaire française (1 000 Md de requêtes/jour) a adopté les pratiques SRE pour gérer ses SLA contractuels avec les annonceurs. L'error budget est le mécanisme de décision pour valider ou bloquer les déploiements des équipes data.

### Chiffres et tendances
- Le livre *Site Reliability Engineering* (Google, O'Reilly) est le 3e livre technique le plus lu par les ingénieurs infrastructure en 2024.
- 54 % des équipes DevOps matures ont adopté des pratiques SRE formelles (DORA, 2023).
- AIOps (IA appliquée à l'opérations) émerge comme extension du SRE : détection d'anomalies et remédiation automatique (Moogsoft, Dynatrace Davis AI).
- Platform Engineering (2024) est souvent vu comme l'évolution du SRE : créer une "Internal Developer Platform" pour que les équipes dev soient autonomes sans toil opérationnel.

## Flashcards
#flashcards
- Quelle est la différence entre SLI, SLO et SLA ? :: SLI = métrique mesurée (ex. taux de succès HTTP). SLO = objectif interne pour ce SLI (ex. 99,9 % sur 30 jours). SLA = engagement contractuel avec pénalités financières envers le client, toujours moins strict que le SLO interne.
- Qu'est-ce qu'un error budget et comment est-il calculé ? :: Le complément du SLO : si SLO = 99,9 %, l'error budget = 0,1 % = 43,2 minutes/mois. Il représente la quantité de downtime/erreurs "autorisée". Quand il est épuisé, les déploiements sont gelés jusqu'au prochain cycle.
- Qu'est-ce que le "toil" selon Google SRE et quel est l'objectif ? :: Le travail opérationnel manuel, répétitif, sans valeur ajoutée à long terme et scalant avec la taille du service. L'objectif SRE est de maintenir le toil sous 50 % du temps de travail et de l'éliminer via l'automatisation.
- Pourquoi les blameless post-mortems sont-ils fondamentaux dans la culture SRE ? :: Parce qu'une culture de la "faute individuelle" pousse les équipes à cacher les incidents et à éviter les risques. Le blameless post-mortem cherche les causes systémiques, favorise le partage d'information et génère des améliorations durables.
- Comment l'error budget arbitre-t-il la tension Dev/Ops ? :: Si l'error budget est intact, les Dev peuvent déployer librement (le système peut absorber le risque). Si l'error budget est épuisé, les déploiements sont gelés et tout le monde se concentre sur la fiabilité — décision objective, non politique.
- Qu'est-ce que le chaos engineering et qui l'a popularisé ? :: La pratique d'injecter des défaillances contrôlées en production (pannes de réseau, kills de pods, latences artificielles) pour tester et améliorer la résilience. Popularisé par Netflix avec Chaos Monkey (2011).
- Quelle est la différence entre SRE et DevOps ? :: DevOps est un mouvement culturel et un ensemble de pratiques. SRE est une implémentation concrète du DevOps développée par Google, avec des mécanismes précis (SLO, error budget, toil, post-mortem). Google dit souvent que "SRE is what you get when you treat operations as a software problem".

## Sources
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering*, Google / O'Reilly, 2016 : https://sre.google/sre-book/table-of-contents/
- Google, *The Site Reliability Workbook*, O'Reilly, 2018 : https://sre.google/workbook/table-of-contents/
- DORA State of DevOps Report 2023 : https://dora.dev/
- Sloth SLO tool : https://sloth.dev/

## Notions liées
- [[DevOps]]
- [[Observabilité]]
- [[PCA - PRA]]
- [[CI - CD]]
- [[Stratégies de déploiement]]
- [[Cyber-résilience]]
