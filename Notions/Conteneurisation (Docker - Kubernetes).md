---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Développement
statut: pas vu
dernière_révision: 
---

# Conteneurisation (Docker - Kubernetes)

## En bref
> **Définition** : La conteneurisation est une technique de virtualisation légère qui isole une application et ses dépendances dans un conteneur portable et autonome. Docker est le moteur de conteneurs le plus répandu ; Kubernetes (K8s) est l'orchestrateur open source de référence qui automatise le déploiement, la mise à l'échelle et la gestion des conteneurs en production.
> **Pourquoi c'est important** : Pour une DSI, les conteneurs permettent de livrer des applications de façon cohérente entre les environnements (dev, test, prod), de réduire la dette liée aux dépendances, et d'accélérer les cycles de déploiement CI/CD. Kubernetes est devenu le standard de facto pour l'orchestration à grande échelle.
> **Chiffres clés** :
> - 87 % des organisations utilisent des conteneurs en production (CNCF Survey 2023).
> - Le marché mondial des conteneurs devrait atteindre 9,6 Md$ en 2028 (MarketsandMarkets, 2023).
> - Kubernetes est utilisé par plus de 5,6 millions de développeurs dans le monde (CNCF, 2023).

## Approfondir

### Fonctionnement

**Docker**
Docker repose sur les primitives Linux (cgroups, namespaces) pour isoler les processus. Le cycle de vie Docker est :
1. **Dockerfile** : fichier déclaratif décrivant l'image (OS de base, dépendances, code, point d'entrée).
2. **Image Docker** : artefact immuable et versionné construit à partir du Dockerfile (`docker build`).
3. **Container Registry** : dépôt d'images (Docker Hub, GitHub Container Registry, AWS ECR, Harbor en auto-hébergé). Les images sont taguées et poussées (`docker push`) puis tirées (`docker pull`).
4. **Container** : instance en cours d'exécution d'une image (`docker run`). Les conteneurs partagent le noyau de l'hôte, contrairement aux VMs.

**Kubernetes**
Kubernetes orchestre des conteneurs sur un cluster de nœuds :
- **Control Plane** : API Server, Scheduler, Controller Manager, etcd (stockage de l'état du cluster).
- **Worker Nodes** : exécutent les workloads via le kubelet et le container runtime (containerd, CRI-O).
- **Pod** : unité atomique de déploiement, regroupe un ou plusieurs conteneurs partageant réseau et stockage.
- **Deployment / StatefulSet / DaemonSet** : contrôleurs décrivant l'état désiré.
- **Service** : abstraction réseau stable exposant un ensemble de pods (ClusterIP, NodePort, LoadBalancer).
- **Ingress / Gateway API** : gestion du trafic HTTP/S entrant.
- **ConfigMap / Secret** : injection de configuration et données sensibles.
- **Helm** : gestionnaire de paquets Kubernetes. Un *chart* Helm est un template paramétrable permettant de déployer une application complexe en une commande (`helm install`).
- **CNCF (Cloud Native Computing Foundation)** : fondation Linux qui héberge Kubernetes, Prometheus, Envoy, Argo CD et 150+ projets cloud native. Elle certifie les distributions Kubernetes conformes (CKA, CKAD, CKS).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Portabilité totale entre environnements | Courbe d'apprentissage élevée (surtout K8s) |
| Démarrage rapide (secondes vs minutes pour les VMs) | Surface d'attaque accrue si mauvaise configuration (privilèges, images non signées) |
| Densité élevée : plusieurs conteneurs par hôte | Gestion des données persistantes complexe (volumes, StatefulSets) |
| Mise à l'échelle automatique (HPA, VPA, KEDA) | Réseau et DNS K8s peuvent être complexes à déboguer |
| Isolation des dépendances (pas de "ça marche chez moi") | Surcoût opérationnel : monitoring, logging, sécurité supplémentaires |
| Intégration native CI/CD (GitOps, Argo CD, Flux) | Coûts potentiels élevés si le cluster est mal dimensionné |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Docker Inc. | Docker Desktop, Docker Hub, Docker Scout (analyse vulnérabilités) |
| Google | GKE (Google Kubernetes Engine), co-créateur de K8s |
| AWS | EKS (Elastic Kubernetes Service), ECS, Fargate (serverless containers) |
| Microsoft Azure | AKS (Azure Kubernetes Service) |
| Red Hat | OpenShift (K8s entreprise avec sécurité renforcée) |
| Rancher (SUSE) | Rancher, RKE2, K3s (K8s léger pour edge) |
| HashiCorp | Nomad (orchestrateur alternatif plus simple) |
| Harbor | Registry open source avec scan de vulnérabilités |

### Cas d'usage concrets
1. **Migration d'une application monolithique vers des microservices (BNP Paribas)** : la banque a déployé Kubernetes sur OpenShift pour décomposer ses applications critiques, réduisant les temps de déploiement de plusieurs heures à quelques minutes.
2. **Spotify** : utilise Kubernetes pour orchestrer des milliers de microservices gérant la recommandation musicale, la diffusion audio et les pipelines de données en temps réel.
3. **Airbus** : utilise des conteneurs pour les pipelines de traitement d'images satellites et les outils de simulation, avec déploiement multi-cloud sécurisé via Helm.

### Chiffres et tendances
- 44 % des organisations exécutent K8s sur plusieurs clouds (CNCF, 2023).
- La sécurité des conteneurs est la préoccupation n°1 : 37 % des incidents cloud impliquent des images vulnérables (Sysdig TDR, 2024).
- L'adoption de l'architecture GitOps (Argo CD, Flux) a doublé entre 2021 et 2023.
- Le nombre de pods gérés par cluster a augmenté de 50 % en deux ans, signe d'une montée en maturité.

## Flashcards
#flashcards/Cloud_et_Virtualisation/Conteneurisation_Docker_Kubernetes #flashcards/Développement/Conteneurisation_Docker_Kubernetes
- Qu'est-ce qu'un conteneur Docker ? :: Instance en cours d'exécution d'une image Docker, isolée via les namespaces et cgroups Linux, partageant le noyau de l'hôte.
- Quelle est la différence entre une image et un conteneur ? :: L'image est un artefact immuable (modèle) ; le conteneur est une instance vivante de cette image.
- Qu'est-ce qu'un Pod Kubernetes ? :: L'unité atomique de déploiement K8s, regroupant un ou plusieurs conteneurs qui partagent le même réseau et le même stockage local.
- À quoi sert Helm ? :: Helm est le gestionnaire de paquets Kubernetes ; il permet de packager, versionner et déployer des applications complexes via des charts paramétrables.
- Qu'est-ce que la CNCF ? :: La Cloud Native Computing Foundation (Linux Foundation) : gouverne Kubernetes et 150+ projets open source cloud native, et certifie les ingénieurs K8s (CKA, CKAD, CKS).
- Quelle est la différence entre un Deployment et un StatefulSet ? :: Un Deployment gère des pods sans état (stateless) ; un StatefulSet gère des pods avec état persistant (bases de données, etc.) en garantissant un ordre de démarrage et une identité stable.
- Qu'est-ce qu'un Container Registry ? :: Un dépôt centralisé pour stocker, versionner et distribuer des images Docker (ex : Docker Hub, AWS ECR, Harbor).

## Sources
- CNCF Annual Survey 2023 : https://www.cncf.io/reports/cncf-annual-survey-2023/
- Docker Documentation : https://docs.docker.com/
- Kubernetes Documentation : https://kubernetes.io/docs/
- Sysdig Global Cloud Threat Report 2024 : https://sysdig.com/threat-detection-and-response/
- MarketsandMarkets, Container Market Report, 2023

## Notions liées
- [[Cloud Native et 12-Factor App]]
- [[Service Mesh]]
- [[FinOps]]
- [[Zero Trust]]
- [[Infrastructure des datacenters]]
