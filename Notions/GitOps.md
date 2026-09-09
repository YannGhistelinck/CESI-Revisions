---
type: notion
thèmes:
  - Développement
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# GitOps

## En bref
> **Définition** : Le GitOps est un paradigme opérationnel formalisé par Alexis Richardson (Weaveworks) en 2017, qui utilise Git comme **source unique de vérité** pour l'infrastructure et les applications. Toute modification de l'infrastructure ou des déploiements passe par un commit dans Git. Un opérateur (ArgoCD, Flux) surveille en permanence le dépôt Git et **réconcilie** automatiquement l'état réel du cluster Kubernetes avec l'état déclaré dans Git.
> **Pourquoi c'est important** : Le GitOps résout les problèmes de dérive de configuration (drift) et de manque de traçabilité des déploiements. Il apporte au déploiement d'infrastructure les mêmes garanties que le développement logiciel : revue de code, historique, rollback en 1 commande (`git revert`), et audit complet. C'est le standard émergent pour les déploiements Kubernetes.
> **Chiffres clés** :
> - 65 % des organisations utilisant Kubernetes adoptent ou évaluent le GitOps (CNCF Survey, 2023).
> - ArgoCD est l'outil CI/CD le plus utilisé dans les environnements Kubernetes (CNCF Survey, 2024).
> - Le GitOps réduit le MTTR de 40 % grâce au rollback immédiat via `git revert` (Weaveworks, 2022).

## Approfondir

### Fonctionnement

**Les 4 principes du GitOps (OpenGitOps v1.0, CNCF)**
1. **Déclaratif** : l'état souhaité du système est exprimé déclarativement (YAML Kubernetes, Helm charts, Kustomize)
2. **Versionné et immuable** : l'état souhaité est stocké dans Git (historique complet, immuabilité des commits)
3. **Récupéré automatiquement** : les agents récupèrent (pull) l'état souhaité depuis Git automatiquement
4. **Réconcilié en continu** : des agents logiciels assurent en permanence que l'état réel correspond à l'état déclaré (reconciliation loop)

**Modèle Push vs Pull**
| Modèle | Fonctionnement | Exemple |
|--------|---------------|---------|
| Push (CI traditionnel) | Le pipeline CI pousse les changements vers le cluster | `kubectl apply` dans Jenkins |
| Pull (GitOps) | Un agent dans le cluster récupère les changements depuis Git | ArgoCD, Flux |

Le modèle Pull est plus sécurisé car le cluster n'expose pas d'API aux systèmes externes — c'est l'agent interne qui initie les connexions.

**Flux de travail GitOps typique**
```
Développeur → PR dans Git → Revue de code → Merge → 
ArgoCD/Flux détecte le changement → Compare état Git vs cluster → 
Applique les différences (reconciliation) → Sync status ✓
```

**Gestion du drift**
Le drift est la divergence entre l'état déclaré dans Git et l'état réel du cluster (modification manuelle "out-of-band"). ArgoCD détecte ce drift en temps réel et peut le corriger automatiquement (auto-sync) ou alerter les équipes.

**ArgoCD — fonctionnement**
- Interface web montrant l'état de synchronisation de chaque application
- Diff visuel entre l'état Git et l'état du cluster
- Rollback en 1 clic (ou `argocd app rollback`)
- Gestion multi-cluster et multi-tenant
- Support Helm, Kustomize, Jsonnet, YAML brut

**Flux — fonctionnement**
- Toolkit modulaire (Source Controller, Kustomize Controller, Helm Controller…)
- Multi-tenant natif, drift detection, alerts via Slack/Teams
- Progressive Delivery via Flagger (canary automatisé)

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Traçabilité totale (chaque déploiement = commit Git) | Complexité initiale de mise en place |
| Rollback immédiat et fiable (`git revert`) | Gestion des secrets délicate (ne pas stocker en clair dans Git) |
| Audit complet et conformité facilitée | Courbe d'apprentissage pour les équipes Ops |
| Dérive détectée et corrigée automatiquement | Modèle Pull moins adapté aux déploiements hors Kubernetes |
| Sécurité renforcée (modèle Pull, pas d'accès externe au cluster) | Synchronisation bi-directionnelle complexe (données stateful) |
| Revue de code appliquée à l'infrastructure | Nécessite une discipline de "tout dans Git" stricte |

### Acteurs et solutions du marché
| Outil | Éditeur | Caractéristiques |
|-------|---------|-----------------|
| ArgoCD | Intuit / CNCF | Le plus populaire, UI riche, multi-cluster, RBAC |
| Flux | Weaveworks / CNCF | Toolkit modulaire, Flagger pour progressive delivery |
| Fleet | Rancher (SUSE) | GitOps à très grande échelle (milliers de clusters) |
| Argo Rollouts | CNCF | Déploiements progressifs (canary, blue-green) pour K8s |
| Jenkins X | CloudBees | CI/CD GitOps-native pour Kubernetes |

**Gestion des secrets en GitOps**
Les secrets ne doivent jamais être committé en clair dans Git. Solutions :
- **Sealed Secrets** (Bitnami) : secrets chiffrés dans Git, déchiffrés dans le cluster
- **External Secrets Operator** : synchronise depuis HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
- **SOPS** (Mozilla) : chiffrement de fichiers YAML avec GPG/age/KMS

### Cas d'usage concrets
1. **Weaveworks** (fondateur du GitOps) : la société gère l'ensemble de son infrastructure Kubernetes via Flux. Chaque modification passe par une PR GitHub, reviewée par 2 ingénieurs, avant déploiement automatique en prod. Le temps de déploiement est passé de 2 heures à 15 minutes.
2. **Tokio Marine (assurance)** : migration de 200+ microservices vers un modèle GitOps avec ArgoCD. Résultat : zéro déploiement manuel, 100 % de traçabilité, conformité SOX automatisée via les PR Git.
3. **Adobe** : gestion de 1 000+ clusters Kubernetes dans 8 régions AWS via ArgoCD en mode multi-tenant. L'équipe platform engineering de 10 personnes gère l'ensemble des déploiements pour 200 équipes de développement.

### Chiffres et tendances
- ArgoCD a franchi le seuil de 10 millions de téléchargements en 2023 (CNCF).
- OpenGitOps v1.0 (standard CNCF) a été publié en 2021.
- 78 % des utilisateurs de GitOps rapportent une amélioration de la fiabilité des déploiements (CNCF Survey, 2023).
- Le GitOps s'étend hors de Kubernetes : des projets comme Crossplane permettent d'appliquer le modèle GitOps aux ressources cloud (AWS, Azure, GCP).

## Flashcards
#flashcards/Développement/GitOps #flashcards/Cloud_et_Virtualisation/GitOps
- Qui a inventé le terme GitOps et quand ? :: Alexis Richardson, CEO de Weaveworks, en 2017.
- Quels sont les 4 principes du GitOps selon l'OpenGitOps v1.0 ? :: Déclaratif, versionné et immuable (dans Git), récupéré automatiquement (pull), et réconcilié en continu.
- Quelle est la différence entre le modèle Push et le modèle Pull en GitOps ? :: En mode Push, le pipeline CI envoie les changements vers le cluster (ex. kubectl apply dans Jenkins). En mode Pull, un agent dans le cluster (ArgoCD, Flux) récupère les changements depuis Git — plus sécurisé car le cluster n'expose pas son API.
- Qu'est-ce que le "drift" en GitOps et comment est-il géré ? :: Le drift est la divergence entre l'état déclaré dans Git et l'état réel du cluster (causée par des modifications manuelles "out-of-band"). ArgoCD et Flux le détectent en temps réel et peuvent le corriger automatiquement (auto-sync).
- Pourquoi ne doit-on pas stocker les secrets en clair dans Git en GitOps ? :: Git est un dépôt potentiellement public ou accessible à de nombreuses personnes ; les secrets en clair seraient exposés. Solutions : Sealed Secrets (chiffrement dans Git), External Secrets Operator (stockage dans un vault externe), SOPS.
- Quelle est la différence entre ArgoCD et Flux ? :: ArgoCD offre une interface web riche, un diff visuel et une gestion centralisée multi-cluster. Flux est un toolkit modulaire plus flexible, avec Flagger pour le progressive delivery automatisé. Les deux sont des projets CNCF incubés.
- Quel est le bénéfice du GitOps pour l'audit de conformité ? :: Chaque déploiement étant traçable à un commit Git signé et approuvé via PR, l'historique complet est disponible — simplifiant les audits SOX, PCI-DSS, ISO 27001 qui exigent de prouver "qui a déployé quoi, quand, et pourquoi".

## Sources
- Alexis Richardson, "GitOps - Operations by Pull Request", Weaveworks, 2017 : https://www.weave.works/blog/gitops-operations-by-pull-request
- OpenGitOps v1.0 (CNCF) : https://opengitops.dev/
- CNCF Survey 2023 : https://www.cncf.io/reports/cncf-annual-survey-2023/
- ArgoCD documentation : https://argo-cd.readthedocs.io/
- Flux documentation : https://fluxcd.io/

## Notions liées
- [[DevOps]]
- [[CI - CD]]
- [[Infrastructure as Code (IaC)]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Stratégies de déploiement]]
- [[Cloud Native et 12-Factor App]]
