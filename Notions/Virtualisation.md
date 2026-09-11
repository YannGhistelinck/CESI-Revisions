---
type: notion
thèmes:
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Virtualisation

## En bref
> **Définition** : La virtualisation est la technologie qui permet de créer des représentations logicielles de ressources physiques (serveurs, stockage, réseau). Une machine virtuelle (VM) est un environnement informatique isolé qui émule un ordinateur complet, partageant les ressources physiques d'un hôte via un hyperviseur. C'est la brique fondamentale du cloud computing moderne.
> **Pourquoi c'est important** : La virtualisation a transformé l'exploitation des datacenters en permettant la consolidation des serveurs (taux d'utilisation de 5-15 % à 60-80 %), la flexibilité d'allocation des ressources, la haute disponibilité (vMotion, live migration) et la résilience. Elle est le socle technique sur lequel reposent l'IaaS, les clouds privés et les environnements hybrides gérés par toute DSI.
> **Chiffres clés** :
> - La virtualisation a permis de réduire de 30 à 40 % les coûts des datacenters d'entreprise depuis 2005 (IDC)
> - VMware est présent dans 80 % des datacenters d'entreprise dans le monde (2022, avant rachat par Broadcom)
> - Le marché des hyperviseurs et plateformes de virtualisation dépasse 12 Md$ en 2023 (MarketsandMarkets)

## Approfondir

### Fonctionnement

**Machine Virtuelle (VM)**
Une VM est un environnement informatique complet et isolé, incluant un CPU virtuel (vCPU), de la RAM virtuelle, des disques virtuels (VMDK, VHD, qcow2) et des interfaces réseau virtuelles. Chaque VM exécute son propre système d'exploitation (OS guest) de manière totalement isolée des autres VMs partageant le même hôte physique. Cette isolation est garantie par l'hyperviseur.

**Hyperviseur de type 1 (Bare-Metal)**
S'exécute directement sur le matériel physique, sans OS hôte intermédiaire. Haute performance car aucune couche OS n'est intercalée. Utilisé dans les datacenters d'entreprise et les clouds publics.
- Exemples : VMware ESXi, Microsoft Hyper-V (Server), Citrix Hypervisor (ex-XenServer), KVM (Kernel-based Virtual Machine, intégré au noyau Linux)

**Hyperviseur de type 2 (Hosted)**
S'exécute comme une application au-dessus d'un OS hôte (Windows, macOS, Linux). Moins performant (double couche d'abstraction) mais plus simple à installer. Utilisé principalement pour les postes de travail et le développement.
- Exemples : VMware Workstation, Oracle VirtualBox, Parallels Desktop (macOS)

**VMware — Références et contexte**
VMware (fondé en 1998, racheté par Broadcom en 2023 pour 61 Md$) est l'acteur historique dominant de la virtualisation d'entreprise. Sa suite vSphere (ESXi + vCenter) est le standard de fait. Fonctionnalités clés de vSphere : vMotion (migration à chaud des VMs sans interruption), DRS (Distributed Resource Scheduler), HA (High Availability), vSAN (stockage virtualisé). Le rachat par Broadcom et les changements de licences (fin des licences perpétuelles, passage au modèle bundle obligatoire) ont provoqué un exode vers des alternatives open-source.

**Proxmox VE**
Plateforme de virtualisation open-source basée sur KVM (pour les VMs) et LXC (pour les conteneurs Linux). Hyperviseur de type 1 (bare-metal). Interface web intégrée, support du clustering, haute disponibilité, stockage distribué (Ceph intégré), live migration. Gratuit (licence AGPL v3), avec support commercial disponible. Fortement adopté par les PME, les établissements d'enseignement et les entreprises en migration post-VMware.

**Nutanix AHV (Acropolis Hypervisor)**
Hyperviseur intégré à la plateforme hyper-convergée Nutanix. Basé sur KVM, il est fourni sans surcoût avec les licences Nutanix. L'infrastructure hyper-convergée (HCI) Nutanix fusionne compute, stockage et réseau dans des nœuds standardisés (appliances). Gestion unifiée via Prism Central. Nutanix est positionné sur le marché enterprise et sert d'alternative à VMware vSphere + vSAN.

**OpenStack**
Plateforme open-source de cloud privé permettant de gérer des pools de ressources compute (Nova), stockage (Cinder, Swift) et réseau (Neutron) via des APIs compatibles AWS. Utilisé par les opérateurs télécoms, les grandes entreprises et les entités publiques souhaitant maîtriser leur cloud sans dépendance à un CSP. Support multi-hyperviseurs (KVM, Xen, VMware). Complexité d'exploitation élevée.

**Virtualisation vs Conteneurisation**
La VM virtualise le matériel complet (OS inclus). Le conteneur (Docker, Kubernetes) virtualise uniquement l'espace utilisateur et partage le noyau de l'OS hôte. Les conteneurs sont plus légers, démarrent en secondes, mais offrent un niveau d'isolation moindre. Les deux technologies sont complémentaires.

**NUMA, vCPU, Overcommit**
- NUMA (Non-Uniform Memory Access) : architecture multi-processeur où chaque processeur a un accès plus rapide à sa propre mémoire. Les hyperviseurs doivent en tenir compte pour les VMs haute performance.
- vCPU : processeur virtuel alloué à une VM. Peut être sur-alloué (overcommit) : plusieurs vCPUs partagent un cœur physique. Efficace si les VMs ne sont pas toutes chargées simultanément.
- Memory overcommit : allocation de RAM virtuelle supérieure à la RAM physique, compensée par des mécanismes de ballooning et de swap.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Consolidation serveurs (réduction du nombre de machines physiques) | Overhead de l'hyperviseur (5-15 % de performance en moins vs. bare metal) |
| Isolation et cloisonnement entre VMs | Complexité de gestion à grande échelle (licences VMware coûteuses) |
| Snapshot et restauration rapide des VMs | "VM sprawl" : prolifération non maîtrisée de VMs inutilisées |
| Live migration (vMotion) : zéro downtime pour les opérations de maintenance | Risque de "noisy neighbor" : une VM consommatrice impacte les autres |
| Haute disponibilité et reprise automatique (HA) | Dépendance au stockage partagé (SAN) dans les architectures classiques |
| Base du cloud computing et des environnements hybrides | Coût élevé des licences VMware post-rachat Broadcom |

### Acteurs et solutions du marché

| Solution | Type | Éditeur | Positionnement |
|----------|------|---------|----------------|
| VMware vSphere (ESXi + vCenter) | Hyperviseur type 1 | Broadcom (ex-VMware) | Enterprise, datacenter |
| Proxmox VE | Hyperviseur type 1 open-source | Proxmox Server Solutions | PME, alternative VMware |
| Nutanix AHV | Hyperviseur type 1 (HCI) | Nutanix | Enterprise, hyper-convergé |
| Microsoft Hyper-V | Hyperviseur type 1 | Microsoft | Environnement Microsoft |
| KVM / QEMU | Hyperviseur type 1 (Linux) | Communauté open-source | Cloud providers, OpenStack |
| OpenStack | Cloud privé (multi-hyperviseurs) | OpenStack Foundation | Opérateurs, grandes entreprises |
| Oracle VM VirtualBox | Hyperviseur type 2 | Oracle | Dev, test, formations |
| VMware Workstation / Fusion | Hyperviseur type 2 | Broadcom | Dev, postes de travail |

### Cas d'usage concrets

1. **Consolidation serveurs dans une DSI** : Une DSI de 300 serveurs physiques à un taux d'utilisation moyen de 10 % migre vers VMware vSphere. Elle consolide ses 300 serveurs en 30 hôtes ESXi physiques (ratio 10:1), passant de 10 % à 70 % d'utilisation des ressources physiques. La facture électrique annuelle du datacenter diminue de 60 %, et le renouvellement matériel coûte 10 fois moins cher.

2. **Migration post-VMware vers Proxmox** : Suite au rachat de VMware par Broadcom et à l'augmentation des licences (facteur 3 à 5 selon les configurations), une collectivité territoriale migre ses 150 VMs de ESXi vers Proxmox VE. La migration utilise l'outil `qm importovf` pour convertir les VMDKs en qcow2. Proxmox Cluster avec Ceph remplace vSAN. L'économie annuelle en licences est de 150 000 €.

3. **Cloud privé OpenStack pour un opérateur télécom** : Un opérateur télécom européen déploie OpenStack sur 200 nœuds physiques pour héberger les fonctions de son réseau (VNF : Virtual Network Functions). Nova gère les VMs KVM, Neutron gère le réseau SDN, Cinder gère les volumes persistants. L'API OpenStack compatible AWS permet de réutiliser des outils Terraform existants. Ce cloud privé héberge 4 000 VMs de production.

### Chiffres et tendances

- VMware rachetée par Broadcom en novembre 2023 pour 61 Md$ : plus grande acquisition du secteur tech à ce jour
- Proxmox VE : croissance de 400 % des nouvelles installations entre 2022 et 2024 (source : communauté Proxmox Forum)
- KVM équipe la quasi-totalité des clouds publics majeurs (AWS utilise Nitro, basé sur KVM ; GCP utilise KVM)
- Le marché de l'hyper-convergence (Nutanix, VMware vSAN, Dell VxRail) représente 14 Md$ en 2023
- Nutanix revendique 25 000 clients enterprise dans 185 pays (Nutanix, 2023)

## Flashcards
#flashcards/Cloud_et_Virtualisation/Virtualisation

Quelle est la différence entre un hyperviseur de type 1 et de type 2 ? :: Type 1 (bare-metal) : s'exécute directement sur le matériel physique, sans OS hôte (ex : VMware ESXi, KVM, Hyper-V). Type 2 (hosted) : s'exécute comme une application au-dessus d'un OS hôte (ex : VirtualBox, VMware Workstation). Type 1 est plus performant, type 2 plus simple à installer.

Qu'est-ce que vMotion chez VMware ? :: Fonctionnalité VMware permettant la migration à chaud d'une VM d'un hôte ESXi vers un autre, sans interruption de service (zéro downtime). Utilise un réseau dédié pour copier la mémoire de la VM pendant qu'elle continue de fonctionner.

Qu'est-ce que Proxmox VE et pourquoi est-il en forte croissance ? :: Proxmox VE est un hyperviseur open-source de type 1 basé sur KVM et LXC, avec une interface web intégrée et support du clustering/HA. Il est en forte croissance car il constitue une alternative gratuite à VMware vSphere, dont les licences ont fortement augmenté après le rachat par Broadcom en 2023.

Qu'est-ce que Nutanix AHV et le modèle HCI ? :: Nutanix AHV est l'hyperviseur basé sur KVM fourni avec la plateforme Nutanix. Le modèle HCI (Hyper-Converged Infrastructure) fusionne compute, stockage et réseau dans des nœuds standardisés, simplifiant l'architecture en éliminant les SAN dédiés.

Quelle est la différence fondamentale entre une VM et un conteneur ? :: Une VM virtualise le matériel complet avec son propre OS (noyau inclus). Un conteneur (Docker) virtualise uniquement l'espace utilisateur et partage le noyau de l'OS hôte. Les conteneurs sont plus légers et plus rapides à démarrer, mais offrent un isolement moindre.

Qu'est-ce qu'OpenStack ? :: Plateforme open-source de cloud privé permettant de gérer des pools de ressources compute (Nova), stockage (Cinder, Swift) et réseau (Neutron) via des APIs. Utilisé par les opérateurs et grandes entreprises souhaitant un cloud privé sans dépendance à un CSP.

Qu'est-ce que l'overcommit de ressources dans la virtualisation ? :: Technique consistant à allouer aux VMs plus de ressources (vCPU, RAM) que la capacité physique réelle de l'hôte. Fonctionne car les VMs ne consomment pas toutes leurs ressources simultanément. Permet d'augmenter la densité de VMs par hôte, au risque de dégradation des performances en cas de pic simultané.

## Sources

- VMware, "Introduction to VMware vSphere", Documentation officielle
- Proxmox Server Solutions, "Proxmox VE Administration Guide"
- Nutanix, "AHV Administration Guide"
- OpenStack Foundation, "OpenStack Documentation" : docs.openstack.org
- IDC, "Worldwide Virtualization Infrastructure Market", 2022-2023
- MarketsandMarkets, "Server Virtualization Market", 2023
- Broadcom, "VMware by Broadcom", communiqué de rachat, novembre 2023

## Notions liées
- [[Migration cloud (les 7R)]]
- [[Infrastructure des datacenters]]
- [[VDI et client léger]]
- [[Technologies de stockage]]
- [[Sécurité cloud (CSPM - CASB - CNAPP)]]
- [[Legacy et dette technique]]
