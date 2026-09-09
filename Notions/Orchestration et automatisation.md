---
type: notion
thèmes:
  - Optimisation du SI
  - Développement
statut: pas vu
dernière_révision: 
---

# Orchestration et automatisation

## En bref

### Définition
L'**orchestration** désigne la coordination automatisée de systèmes, services et processus hétérogènes pour exécuter des workflows complexes. Elle va au-delà de la simple automatisation d'une tâche isolée.

L'**automatisation** est l'exécution autonome d'une tâche sans intervention humaine (script, bot, outil RPA).

L'**hyperautomation** (Gartner) est une approche combinant RPA, IA, ML, Process Mining, BPMS et low-code pour automatiser le maximum de processus métier et IT de bout en bout.

**Outils clés :**
- **Kubernetes** : orchestrateur de conteneurs — déploiement, scaling, auto-healing des pods
- **Apache Airflow** : orchestrateur de workflows de données (DAG — Directed Acyclic Graph)
- **Terraform / Ansible** : orchestration d'infrastructure (IaC)
- **GitHub Actions / GitLab CI** : orchestration de pipelines CI/CD
- **RPA** (UiPath, Automation Anywhere, Blue Prism) : automatisation des tâches répétitives sur interfaces

### Pourquoi c'est important
Les SI modernes sont composés de centaines de microservices, pipelines de données et processus métier. Sans orchestration, la complexité opérationnelle devient ingérable. L'orchestration et l'automatisation réduisent les erreurs humaines, accélèrent les livraisons et libèrent les équipes pour des tâches à valeur ajoutée.

### Chiffres clés
- Kubernetes est utilisé par 96 % des organisations cloud-native (CNCF Survey 2023)
- L'hyperautomation représente un marché de 26 Md$ en 2025 (Gartner)
- Les organisations automatisant leurs pipelines CI/CD déploient 208 fois plus fréquemment (DORA Report 2023)
- L'automatisation RPA génère un ROI moyen de 250 % sur 3 ans (Forrester)

---

## Approfondir

### Fonctionnement

**Kubernetes — architecture et orchestration de conteneurs :**
- **Control Plane** : API Server, etcd (état du cluster), Scheduler, Controller Manager
- **Worker Nodes** : Kubelet, kube-proxy, conteneurs (Pods)
- Fonctionnalités : rolling updates, auto-scaling (HPA/VPA), self-healing, load balancing, service discovery
- Distributions : GKE (Google), AKS (Azure), EKS (AWS), OpenShift (Red Hat), k3s (edge)
- Service Mesh (Istio, Linkerd) : couche de gestion du trafic inter-services

**Apache Airflow — orchestration de workflows de données :**
- Modélisation des workflows en DAG (graphe orienté acyclique) en Python
- Composants : Scheduler, Webserver, Worker, Metadata DB
- Opérateurs : BashOperator, PythonOperator, DockerOperator, KubernetesPodOperator
- Cas d'usage : pipelines ETL/ELT, ML pipelines, data quality checks
- Alternatives : Prefect, Dagster, Luigi, Azure Data Factory

**Niveaux d'automatisation :**
1. **Automatisation de tâches** : scripts bash/Python, cron jobs
2. **Automatisation de processus (RPA)** : bots sur interfaces graphiques (UiPath, Blue Prism)
3. **Orchestration de services** : Kubernetes, Airflow, pipelines CI/CD
4. **Hyperautomation** : combinaison IA + RPA + Process Mining + low-code — vision bout en bout

**Hyperautomation — composants :**
- **Process Mining** (Celonis, UiPath Process Mining) : découverte automatique des processus réels
- **RPA** : automatisation des tâches répétitives
- **IA/ML** : traitement du langage, vision, décision
- **BPMS** (Business Process Management Suite) : modélisation et gouvernance des processus
- **Low-code** : accélération du développement des automatisations

**Orchestration CI/CD :**
- GitHub Actions : workflows YAML déclenchés par événements (push, PR, schedule)
- GitLab CI/CD : pipelines intégrés au repo
- Jenkins : serveur CI/CD historique, très extensible
- ArgoCD : GitOps — synchronisation Kubernetes depuis Git

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Réduction drastique des erreurs manuelles | Complexité d'implémentation initiale |
| Scalabilité automatique des workloads | Courbe d'apprentissage élevée (Kubernetes notamment) |
| Accélération des cycles de livraison | Risque de "sur-automatisation" mal maîtrisée |
| Libération des équipes pour des tâches à VA | Dépendance aux outils et écosystèmes |
| Disponibilité accrue (auto-healing) | Coût de maintenance des pipelines d'automatisation |
| Réduction des coûts opérationnels à terme | Sécurité des accès aux orchestrateurs à maîtriser |

### Acteurs
- **CNCF** (Cloud Native Computing Foundation) : gouverne Kubernetes, Argo, etc.
- **Google** : créateur de Kubernetes (Borg en interne), GKE
- **Apache Software Foundation** : Airflow, Kafka, Spark
- **UiPath / Automation Anywhere / Blue Prism** : leaders RPA
- **HashiCorp (Terraform)** : orchestration IaC
- **Celonis** : leader du Process Mining
- **Microsoft (Power Automate)** : automatisation low-code enterprise

### Cas d'usage
- **DevOps/DevSecOps** : pipeline CI/CD entièrement orchestré (test, scan sécurité, build, déploiement Kubernetes) via GitHub Actions + ArgoCD
- **Data Engineering** : Airflow orchestre les pipelines ETL nocturnes de l'entrepôt de données (extraction API → transformation Spark → chargement BigQuery)
- **Opérations IT** : auto-scaling Kubernetes lors des pics de charge e-commerce (Black Friday)
- **Hyperautomation RH** : onboarding automatisé (création compte AD, attribution licences, équipement) via RPA + workflow ITSM

### Chiffres complémentaires
- 70 % des entreprises déclarent avoir au moins un projet hyperautomation en cours (Gartner 2023)
- Kubernetes réduit le coût d'exploitation des applications cloud-native de 30 à 50 % vs VMs traditionnelles
- UiPath compte plus de 10 000 clients entreprises dans 80+ pays

---

## Flashcards
#flashcards/Optimisation_du_SI/Orchestration_et_automatisation #flashcards/Développement/Orchestration_et_automatisation

Quelle est la différence entre automatisation et orchestration ? :: L'automatisation exécute une tâche isolée sans intervention humaine ; l'orchestration coordonne plusieurs systèmes et tâches automatisées pour exécuter des workflows complexes de bout en bout.

Qu'est-ce que Kubernetes et quel problème résout-il ? :: Orchestrateur de conteneurs open source qui automatise le déploiement, le scaling et la gestion des applications conteneurisées, résolvant la complexité opérationnelle des microservices.

Qu'est-ce qu'un DAG dans Apache Airflow ? :: Un Directed Acyclic Graph — représentation du workflow de données où chaque nœud est une tâche et les arêtes définissent les dépendances d'exécution.

Qu'est-ce que l'hyperautomation selon Gartner ? :: Une approche combinant RPA, IA, ML, Process Mining et low-code pour automatiser le maximum de processus de bout en bout — au-delà de l'automatisation tâche par tâche.

Citez 3 outils d'orchestration CI/CD. :: GitHub Actions, GitLab CI/CD, Jenkins, ArgoCD (GitOps).

Qu'est-ce que le Process Mining et à quoi sert-il dans l'hyperautomation ? :: Technique qui analyse les logs des systèmes pour découvrir automatiquement les processus réels, identifier les inefficacités et prioriser les candidats à l'automatisation.

Quels sont les 3 leaders RPA du marché ? :: UiPath, Automation Anywhere, Blue Prism.

---

## Sources
- CNCF Annual Survey 2023 — cncf.io
- Apache Airflow Documentation — airflow.apache.org
- Gartner, *Hyperautomation Forecast*, 2023
- DORA State of DevOps Report, 2023
- Forrester, *The Total Economic Impact of UiPath*, 2023
- Kubernetes Documentation — kubernetes.io

---

## Notions liées
- [[Conteneurisation (Docker - Kubernetes)]]
- [[CI - CD]]
- [[GitOps]]
- [[Infrastructure as Code (IaC)]]
- [[RPA (Robotic Process Automation)]]
- [[Outils ITSM]]
- [[DevOps]]
- [[Platform Engineering]]
