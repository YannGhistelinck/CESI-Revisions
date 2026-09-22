---
type: notion
thèmes:
  - Développement
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Infrastructure as Code (IaC)

![[N — Infrastructure as Code (IaC).mp3]]
## En bref
> **Définition** : L'Infrastructure as Code (IaC) est la pratique consistant à gérer et provisionner l'infrastructure informatique (serveurs, réseaux, bases de données, stockage) via des fichiers de configuration déclaratifs ou des scripts versionnés dans Git, plutôt que via des interfaces manuelles ou des CLI. L'infrastructure devient du code : versionnable, testable, partageable et reproductible. Terraform (HashiCorp, 2014) en est l'outil de référence multi-cloud.
> **Pourquoi c'est important** : L'infrastructure manuelle est lente, peu reproductible et source d'erreurs humaines (snowflake servers). L'IaC permet de créer des environnements identiques en minutes, de détecter et corriger les dérives de configuration, et d'industrialiser la gestion du SI à grande échelle — condition sine qua non du DevOps et du cloud.
> **Chiffres clés** :
> - Terraform est utilisé par plus de 2 millions de développeurs dans le monde (HashiCorp, 2024).
> - Les équipes utilisant l'IaC réduisent le temps de provisionnement d'infrastructure de 80 % (Puppet State of DevOps, 2023).
> - Les incidents liés aux mauvaises configurations cloud représentent 80 % des violations de données cloud (Gartner, 2023).

## Approfondir

### Fonctionnement

**Approches déclarative vs impérative**
| Approche | Principe | Exemple |
|----------|----------|---------|
| Déclarative | On décrit l'état final souhaité ; l'outil détermine comment y arriver | Terraform, Pulumi, CloudFormation |
| Impérative | On décrit les étapes à exécuter séquentiellement | Ansible (mode ad-hoc), scripts Bash, Chef |

En pratique, les outils modernes combinent les deux (Ansible peut être déclaratif pour la gestion de configuration).

**L'idempotence**
Propriété fondamentale de l'IaC : exécuter le même code plusieurs fois produit toujours le même résultat (l'infrastructure converge vers l'état déclaré). Si la ressource existe déjà, elle n'est pas recréée ; si elle est conforme, elle n'est pas modifiée. Cela rend les déploiements sûrs et réexécutables.

**Terraform — fonctionnement**
Terraform utilise le langage HCL (HashiCorp Configuration Language) :
```
Terraform init → Terraform plan (diff état vs réel) → 
Terraform apply (provisionnement) → State file (terraform.tfstate)
```
- **Providers** : plugins pour chaque cloud/service (AWS, Azure, GCP, Kubernetes, Datadog…)
- **Modules** : blocs réutilisables d'infrastructure (module VPC, module EKS…)
- **State** : fichier d'état stockant la correspondance entre code et ressources réelles (à stocker en remote : S3, Azure Blob, Terraform Cloud)
- **Plan** : aperçu des changements avant application ("`+` créer, `-` supprimer, `~` modifier")

**Drift Detection**
Le drift est la divergence entre l'état déclaré dans le code et l'état réel de l'infrastructure (modification manuelle hors IaC). `terraform plan` détecte ce drift. Des outils comme Driftctl ou Terraform Cloud permettent une détection continue.

**Ansible — fonctionnement**
Ansible est agentless (SSH/WinRM) et utilise des **playbooks** YAML pour la gestion de configuration :
- **Inventaire** : liste des hôtes à configurer
- **Playbooks** : séquences de tâches (tasks) organisées en rôles
- **Modules** : unités de travail idempotentes (apt, yum, copy, service, k8s…)
- Usage : configuration d'OS, déploiement d'applications, orchestration de tâches

**Pulumi — spécificité**
Pulumi permet d'écrire l'IaC dans des langages de programmation généraux (Python, TypeScript, Go, C#) avec tests unitaires natifs et logique conditionnelle, là où Terraform utilise HCL (DSL).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Reproductibilité totale des environnements | Courbe d'apprentissage initiale (HCL, YAML, concepts Terraform) |
| Versionnement Git (historique, rollback, revue) | Gestion du state Terraform complexe (corruption, conflits) |
| Provisionnement rapide (minutes vs semaines) | Drift difficile à gérer si disciplines d'équipe insuffisantes |
| Réduction des erreurs humaines | Coût de migration des infras existantes vers l'IaC |
| Documentation vivante de l'infrastructure | Risque de mauvaises configurations à grande échelle (tout est automatisé) |
| Base du GitOps et du DevOps | Dépendance à un outil (HashiCorp a changé la licence Terraform en BSL en 2023) |

### Acteurs et solutions du marché
| Outil | Éditeur | Type | Spécificité |
|-------|---------|------|-------------|
| Terraform | HashiCorp (IBM) | Déclaratif, multi-cloud | Standard de facto ; licence BSL depuis 2023 |
| OpenTofu | Linux Foundation | Déclaratif, multi-cloud | Fork open source de Terraform (MPL-2.0) |
| Pulumi | Pulumi Corp | Déclaratif, multi-cloud | Langages généraux (Python, TS, Go) |
| AWS CloudFormation | Amazon | Déclaratif, AWS only | Natif AWS, JSON/YAML |
| AWS CDK | Amazon | Impératif/déclaratif | TypeScript/Python → CloudFormation |
| Azure Bicep | Microsoft | Déclaratif, Azure only | Remplace ARM templates |
| Ansible | Red Hat (IBM) | Impératif/déclaratif | Gestion de configuration, agentless |
| Crossplane | CNCF | Déclaratif | IaC via Kubernetes CRDs (GitOps-native) |

### Cas d'usage concrets
1. **Société Générale** : l'équipe Cloud CoE gère 1 500+ comptes AWS via Terraform. L'intégralité des landing zones, des VPC et des politiques IAM est versionnée dans GitLab, avec des pipelines CI/CD appliquant les changements via `terraform apply`. Résultat : provisionnement d'un nouveau compte AWS en 20 minutes (vs 6 semaines en manuel).
2. **Spotify** : utilise Terraform pour gérer ses 10 000+ ressources GCP. Les équipes créent leur propre infrastructure via des modules Terraform internes publiés dans un catalogue interne (infrastructure self-service).
3. **OVHcloud** : OVHcloud a open-sourcé son provider Terraform officiel, permettant à ses clients de provisionner VMs, DNS, stockage objet via IaC. L'ensemble de l'infrastructure interne OVHcloud est aussi gérée par IaC.

### Chiffres et tendances
- OpenTofu (fork open source de Terraform post-BSL) a franchi 1 million de téléchargements en 3 mois après sa création (2024).
- Crossplane (IaC Kubernetes-native) connaît une adoption de +200 % par an (CNCF, 2024).
- 67 % des entreprises cloud utilisent Terraform comme outil IaC principal (HashiCorp State of the Cloud, 2023).
- Le Policy as Code (OPA, Sentinel) s'impose comme complément de l'IaC pour la gouvernance (règles de conformité appliquées avant `terraform apply`).

## Flashcards
#flashcards/Développement/Infrastructure_as_Code_IaC #flashcards/Cloud_et_Virtualisation/Infrastructure_as_Code_IaC #flashcards/Optimisation_du_SI/Infrastructure_as_Code_IaC
- Qu'est-ce que l'idempotence en IaC ? :: La propriété garantissant qu'appliquer le même code IaC plusieurs fois produit toujours le même résultat — si la ressource est déjà conforme, elle n'est pas modifiée. Cela rend les déploiements sûrs et réexécutables.
- Quelle est la différence entre Terraform et Ansible ? :: Terraform est déclaratif et orienté provisionnement d'infrastructure cloud (création de VMs, réseaux, BDD). Ansible est agentless et orienté gestion de configuration (installation de paquets, déploiement d'apps sur des serveurs existants). Ils sont complémentaires.
- Qu'est-ce que le "drift" en IaC et comment le détecter ? :: La divergence entre l'état déclaré dans le code et l'état réel de l'infrastructure (modification manuelle hors IaC). `terraform plan` le détecte ponctuellement ; Driftctl ou Terraform Cloud permettent une détection continue.
- Pourquoi le state Terraform est-il critique et où le stocker ? :: Le state (terraform.tfstate) est le fichier qui mappe le code aux ressources réelles. Sa corruption ou sa perte empêche Terraform de gérer l'infrastructure. Il doit être stocké en remote (S3 + DynamoDB, Terraform Cloud) avec verrouillage pour éviter les conflits.
- Quelle est la différence entre Terraform et OpenTofu ? :: OpenTofu est un fork open source de Terraform créé par la Linux Foundation en 2023, après que HashiCorp a changé la licence de Terraform de MPL-2.0 vers BSL (Business Source License), rendant son usage commercial plus restrictif.
- Qu'est-ce que Pulumi apporte par rapport à Terraform ? :: Pulumi permet d'écrire l'IaC dans des langages de programmation généraux (Python, TypeScript, Go, C#) avec tests unitaires natifs, boucles et conditions — là où Terraform utilise HCL (Domain Specific Language) plus limité.
- Qu'est-ce que le "Policy as Code" en IaC ? :: La définition de règles de conformité et de sécurité sous forme de code (OPA/Rego, HashiCorp Sentinel) vérifiées automatiquement avant chaque `terraform apply`, empêchant le déploiement de configurations non conformes.

## Sources
- HashiCorp, *Terraform: Up & Running*, Yevgeniy Brikman, O'Reilly, 3e édition, 2022
- OpenTofu : https://opentofu.org/
- Puppet State of DevOps Report 2023 : https://www.puppet.com/resources/state-of-platform-engineering
- Gartner, "Cloud Security Is a Shared Responsibility", 2023
- CNCF, Crossplane project : https://www.crossplane.io/

## Notions liées
- [[DevOps]]
- [[GitOps]]
- [[CI - CD]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Cloud Native et 12-Factor App]]
- [[Sécurité cloud (CSPM - CASB - CNAPP)]]
- [[Migration cloud (les 7R)]]
