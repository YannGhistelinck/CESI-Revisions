---
type: notion
thèmes:
  - IA
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# AIOps

## En bref

### Définition
L'**AIOps** (Artificial Intelligence for IT Operations) désigne l'application de l'IA et du machine learning à la gestion et l'exploitation des systèmes d'information. L'objectif est d'automatiser la détection d'anomalies, la corrélation d'événements, le diagnostic et la remédiation des incidents. Cela se concrétise par des capacités de **self-healing infrastructure** (auto-réparation), de **digital twin infrastructure** (jumeau numérique du SI), de **zero-touch provisioning** et une progression vers des niveaux d'autonomie croissants (niveau 0 à 5).

### Pourquoi c'est important
Les SI modernes (cloud hybride, microservices, Kubernetes, edge) génèrent des volumes de logs, métriques et traces impossibles à traiter manuellement. L'AIOps permet de passer d'une gestion réactive (incident → ticket → résolution) à une gestion prédictive et autonome, réduisant le MTTR (Mean Time to Repair) et le nombre d'incidents en production.

### Chiffres clés
- Marché AIOps : **~21 Md$ en 2024**, CAGR 33 % jusqu'en 2030
- Réduction du MTTR avec AIOps : **50 à 75 %** (études Gartner/IDC)
- Volume de données IT généré : **2,5 exaoctets/jour** dans les grandes entreprises
- 40 % des entreprises Fortune 1000 utilisent une solution AIOps en production (2024)
- ROI moyen AIOps : **200-350 %** sur 3 ans (Forrester, 2023)

---

## Approfondir

### Fonctionnement

#### Les niveaux d'autonomie IA (0 à 5)

Analogie avec la conduite autonome appliquée aux opérations IT :

| Niveau | Nom | Description | Rôle humain |
|---|---|---|---|
| **0** | Manuel | Aucune automatisation, tout est fait manuellement | 100 % humain |
| **1** | Assisté | Outils de monitoring classiques, alertes | Détection aidée, action humaine |
| **2** | Partiellement automatisé | IA détecte et suggère des actions | Humain valide et exécute |
| **3** | Conditionnel automatisé | IA exécute des remédiations pré-approuvées | Humain supervise, intervient si hors scope |
| **4** | Hautement automatisé | IA gère la majorité des incidents en autonomie | Humain sur exceptions et stratégie |
| **5** | Totalement autonome | SI auto-géré en toutes circonstances | Humain définit les objectifs uniquement |

La plupart des entreprises avancées sont en **niveau 2-3** en 2024.

#### Capacités clés de l'AIOps

**1. Détection et corrélation d'anomalies**
- Analyse de millions de métriques/logs en temps réel (CPU, latence, erreurs HTTP…)
- Corrélation d'événements disparates pour identifier la cause racine (**root cause analysis**)
- Réduction du bruit d'alerte : -70 à -90 % d'alertes avec déduplication IA

**2. Self-Healing Infrastructure**
- Détection automatique d'une anomalie (ex : pod Kubernetes en CrashLoopBackOff)
- Analyse de la cause (OOM, config incorrecte, dépendance défaillante)
- Remédiation automatique : restart, scaling, rollback, isolation du composant
- Apprentissage des patterns pour prévention future

**3. Digital Twin Infrastructure**
- Réplique virtuelle du SI (topologie, dépendances, configurations)
- Simulation d'impacts avant tout changement (patch, migration, montée en charge)
- Détection de dérives de configuration (drift) par comparaison avec le jumeau
- Optimisation de capacité par simulation

**4. Zero-Touch Provisioning (ZTP)**
- Déploiement automatique d'équipements réseau/serveurs sans intervention manuelle
- Le device se configure automatiquement au boot (DHCP + TFTP + templates)
- Applications : déploiement de switchs, routeurs, serveurs en datacentre ou edge

**5. Prédiction et optimisation**
- Maintenance prédictive des infrastructures (disques, mémoire, réseau)
- Capacity planning prédictif
- Optimisation des coûts cloud (rightsizing, spot instances)

#### Architecture AIOps typique

```
Sources de données       Ingestion/Stockage       IA/ML              Action
─────────────────        ─────────────────        ──────             ──────
Logs (ELK, Splunk)  →
Métriques (Prometheus) → Data Lake / Stream   →  Détection       →  Alertes
Traces (Jaeger/OTEL) →  (Kafka, S3, TSDB)       Corrélation        Tickets
CMDB / Topologie    →                            Root Cause      →  Auto-remédiation
Events ITSM         →                            Prédiction      →  ZTP
```

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| MTTR réduit de 50-75 % | Investissement initial élevé (outils + données + formation) |
| Réduction du bruit d'alerte (-70-90 %) | Nécessite des données historiques de qualité |
| Disponibilité 24/7, détection en temps réel | Risque de "faux positifs" et remédiations incorrectes |
| Libère les équipes ops des tâches répétitives | Résistance culturelle des équipes IT (peur du remplacement) |
| Corrélation impossible manuellement à grande échelle | Explicabilité limitée des décisions IA |
| Optimisation des coûts cloud | Dépendance aux vendors (lock-in) |

### Acteurs
- **Plateformes AIOps** : ServiceNow (Now Platform + AI), Dynatrace (Davis AI), Datadog (Watchdog AI), IBM Watson AIOps, Moogsoft, BigPanda
- **Monitoring/Observabilité** : Grafana, Prometheus, Splunk, Elastic, New Relic
- **Cloud natif** : AWS DevOps Guru, Azure Monitor AI, Google Cloud Operations
- **Réseau** : Cisco ThousandEyes, Juniper Mist AI

### Cas d'usage
- **Incident management** : corrélation automatique d'alertes → 1 incident = 1 ticket (vs 50 alertes)
- **Kubernetes** : self-healing pods, auto-scaling prédictif
- **Réseau** : détection de dégradation avant l'impact utilisateur (Juniper Mist)
- **Cloud costs** : rightsizing automatique des VMs (économies 20-40 %)
- **Change management** : simulation d'impact de mise en production via digital twin

### Chiffres complémentaires
- Dynatrace Davis AI : traite **500 000 dépendances** en temps réel par minute
- IBM Watson AIOps : réduit de 85 % le temps de résolution des incidents
- Le ZTP réduit le temps de déploiement réseau de **jours à minutes**

---

## Flashcards
#flashcards/IA/AIOps #flashcards/Optimisation_du_SI/AIOps

Qu'est-ce que l'AIOps et quel problème résout-il ? :: L'AIOps applique l'IA/ML aux opérations IT pour automatiser la détection d'anomalies, la corrélation d'événements et la remédiation d'incidents. Il résout l'impossibilité de gérer manuellement les volumes de données (logs, métriques, traces) des SI modernes.

Décrivez les niveaux 0 à 5 d'autonomie IA dans les opérations IT. :: Niveau 0 = tout manuel ; Niveau 1 = alertes automatiques, action humaine ; Niveau 2 = IA suggère, humain exécute ; Niveau 3 = IA exécute les remédiations pré-approuvées ; Niveau 4 = IA autonome sur la majorité, humain sur exceptions ; Niveau 5 = SI totalement auto-géré.

Qu'est-ce que le self-healing infrastructure ? :: Capacité d'un SI à détecter automatiquement une défaillance, en identifier la cause, et la corriger sans intervention humaine (ex : restart automatique d'un pod Kubernetes, rollback de déploiement, scaling).

Qu'est-ce qu'un digital twin d'infrastructure ? :: Un jumeau numérique du SI : réplique virtuelle de la topologie, des dépendances et des configurations, permettant de simuler l'impact de changements avant leur application en production et de détecter les dérives de configuration.

Qu'est-ce que le Zero-Touch Provisioning ? :: Technique permettant à un équipement réseau ou serveur de se configurer automatiquement au démarrage (sans intervention humaine) en récupérant sa configuration depuis un serveur central via DHCP/TFTP/API.

Quel est l'impact mesurable de l'AIOps sur le MTTR ? :: L'AIOps réduit le MTTR (Mean Time to Repair) de 50 à 75 % grâce à la corrélation automatique des événements, l'identification rapide de la cause racine et les remédiations automatisées.

Citez 3 plateformes AIOps du marché. :: Dynatrace (Davis AI), ServiceNow (Now Platform AI), IBM Watson AIOps, Datadog (Watchdog), Moogsoft, BigPanda.

---

## Sources
- Gartner — Market Guide for AIOps Platforms, 2024
- Forrester — The Total Economic Impact of AIOps, 2023
- Dynatrace — State of Observability Report, 2024
- IBM — Watson AIOps documentation
- IDC — AIOps Market Forecast, 2024

---

## Notions liées
- [[Intelligence Artificielle — fondamentaux]]
- [[MLOps - DataOps]]
- [[IA générative et LLM]]
