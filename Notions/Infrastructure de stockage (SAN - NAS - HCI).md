---
type: notion
thèmes:
  - Big DATA
  - SI et environnement
statut: pas vu
dernière_révision: 
---

# Infrastructure de stockage (SAN - NAS - HCI)

## En bref
> **Définition** : Les infrastructures de stockage désignent l'ensemble des architectures matérielles et logicielles permettant de stocker, accéder et gérer les données en entreprise. Les trois modèles dominants sont le SAN (Storage Area Network), le NAS (Network Attached Storage) et l'HCI (Hyperconverged Infrastructure). Le stockage objet constitue un quatrième paradigme adapté au Big Data.
> **Pourquoi c'est important** : Le choix de l'infrastructure de stockage conditionne les performances, la scalabilité, le coût et la résilience du système d'information. Dans un contexte Big Data, où les volumes doublent tous les 2 ans (loi de Moore du stockage), cette décision est stratégique.
> **Chiffres clés** :
> - **120 zettaoctets** de données créées dans le monde en 2023 (IDC)
> - Le marché mondial du stockage d'entreprise pèse **60 Md$** en 2024 (IDC)
> - L'HCI représente désormais **30 % des dépenses** d'infrastructure de datacenter (Gartner)

## Approfondir

### Fonctionnement

#### SAN — Storage Area Network
Réseau dédié haute performance reliant les serveurs à un pool de stockage centralisé via des protocoles spécialisés.

**Protocoles** :
- **Fibre Channel (FC)** : réseau dédié optique, très faible latence, coûteux
- **iSCSI** : SAN sur réseau IP Ethernet standard, moins coûteux
- **NVMe-oF** : NVMe over Fabrics, ultra-basse latence pour stockage Flash

**Caractéristiques** :
- Les serveurs voient le stockage SAN comme un disque local (accès bloc)
- Performances maximales, idéal pour bases de données critiques (Oracle, SQL Server)
- Architecture complexe, coûteuse, administrée par des spécialistes storage

**Cas d'usage** : bases de données transactionnelles, virtualisation VMware, ERP critiques (SAP)

#### NAS — Network Attached Storage
Serveur de fichiers connecté au réseau local, accessible via des protocoles de partage de fichiers.

**Protocoles** :
- **SMB/CIFS** : partage Windows (réseau Microsoft)
- **NFS** : partage Unix/Linux
- **AFP** : Apple Filing Protocol (usage déclinant)

**Caractéristiques** :
- Accès fichier (et non bloc) : le système de fichiers est géré par le NAS
- Simple à administrer, peu coûteux, accessible à tous les utilisateurs du réseau
- Performances inférieures au SAN pour les charges transactionnelles intensives

**Acteurs** : NetApp, Dell EMC Isilon, Synology, QNAP, Pure Storage

**Cas d'usage** : partage de fichiers, home directories, archivage, médias, Big Data (HDFS sur NAS)

#### HCI — Hyperconverged Infrastructure
Architecture convergée intégrant calcul, stockage et réseau sur des nœuds x86 standard, gérés par une couche logicielle unifiée (Software-Defined Storage).

```
Nœud 1 : CPU + RAM + SSD/HDD + hyperviseur
Nœud 2 : CPU + RAM + SSD/HDD + hyperviseur   → Pool partagé via software
Nœud 3 : CPU + RAM + SSD/HDD + hyperviseur
```

**Fonctionnement** :
- Les données sont répliquées entre nœuds (facteur de réplication 2 ou 3)
- Scale-out horizontal : ajout d'un nœud pour augmenter simultanément compute et storage
- Gestion centralisée via une interface unique (vSphere, Nutanix Prism, etc.)

**Acteurs** : Nutanix, VMware vSAN, Dell VxRail, HPE SimpliVity, Scale Computing

**Avantages** : simplicité opérationnelle, scalabilité linéaire, TCO réduit
**Inconvénients** : moins performant qu'un SAN dédié pour les charges extrêmes, couplage compute/storage

#### Stockage objet (Object Storage)
Paradigme radicalement différent : les données sont stockées sous forme d'objets (donnée + métadonnées + identifiant unique UUID) dans un espace d'adressage plat (pas de hiérarchie de répertoires).

**Protocoles** : **S3** (Amazon Simple Storage Service, devenu standard de facto), Swift (OpenStack)

**Caractéristiques** :
- Scalabilité quasi illimitée (exaoctets)
- Idéal pour données non structurées (images, vidéos, logs, sauvegardes, data lake)
- Accès via API HTTP/REST, pas de montage de disque
- Pas adapté aux accès aléatoires à haute fréquence (latence plus élevée)

**Acteurs** : AWS S3, Azure Blob Storage, Google Cloud Storage, MinIO (open source), Ceph

**Cas d'usage Big Data** : Data lake, stockage des raw data avant traitement Spark/Hadoop, archives froides

### Comparatif des architectures

| Critère | SAN | NAS | HCI | Stockage objet |
|---------|-----|-----|-----|----------------|
| Type d'accès | Bloc | Fichier | Bloc/Fichier | Objet (API) |
| Performance | Très élevée | Moyenne | Élevée | Moyenne |
| Scalabilité | Verticale (limitée) | Verticale | Horizontale | Horizontale (illimitée) |
| Complexité | Très élevée | Faible | Faible-Moyenne | Faible |
| Coût | Très élevé | Faible-Moyen | Moyen | Faible |
| Cas Big Data | BDD critiques | Partage de fichiers | VMs, petits clusters | Data lake, archive |

### Avantages / Inconvénients

| Architecture | Avantages | Inconvénients |
|---|---|---|
| **SAN** | Performances maximales, faible latence | Coût très élevé, compétences spécialisées requises |
| **NAS** | Simplicité, coût réduit, multi-protocoles | Performances limitées, point de contention réseau |
| **HCI** | Scale-out simple, gestion unifiée, TCO réduit | Couplage compute/storage, moins adapté aux charges extrêmes |
| **Stockage objet** | Scalabilité infinie, coût très bas, API standard | Latence plus élevée, pas d'accès bloc/fichier natif |

### Acteurs et solutions du marché
- **NetApp** : leader SAN/NAS hybride, solution ONTAP (on-prem et cloud)
- **Dell EMC** : PowerStore (SAN), Isilon (NAS), VxRail (HCI)
- **HPE** : Nimble Storage (SAN), Primera, SimpliVity (HCI)
- **Nutanix** : leader HCI, plateforme Prism
- **Pure Storage** : SAN 100 % Flash (FlashArray), stockage objet (FlashBlade)
- **AWS / Azure / GCP** : stockage objet cloud (S3, Blob, GCS)
- **MinIO** : stockage objet open source compatible S3, déployable on-prem

### Cas d'usage concrets
1. **BNP Paribas** exploite un SAN Fibre Channel pour ses bases de données transactionnelles (trading, paiements), où la latence sub-milliseconde est critique. Son data lake Big Data repose sur du stockage objet MinIO on-premise.
2. **Airbus** utilise une architecture HCI Nutanix pour ses environnements de développement et de test, réduisant son parc de serveurs de 60 % tout en simplifiant l'administration.
3. **Netflix** stocke l'intégralité de sa bibliothèque vidéo (plusieurs exaoctets) sur AWS S3, avec un coût de stockage inférieur à 0,023 $/Go/mois pour les données froides (S3 Glacier).

### Chiffres et tendances
- Le stockage objet représente désormais **65 % des nouvelles capacités** déployées en datacenter (IDC, 2024)
- Le marché HCI croît à **+15 % par an** (Gartner)
- Le coût du SSD NVMe a chuté de **90 % en 5 ans**, rendant le SAN Flash accessible aux ETI
- Le **Software-Defined Storage** (SDS) — comme Ceph — permet de s'abstraire du matériel : tendance forte chez les GAFAM et opérateurs cloud

## Flashcards
#flashcards/Big_DATA/Infrastructure_de_stockage_SAN_NAS_HCI #flashcards/SI_et_environnement/Infrastructure_de_stockage_SAN_NAS_HCI

Quelle est la différence fondamentale entre SAN et NAS ? :: Le SAN offre un accès bloc (le serveur voit un disque local) via un réseau dédié haute performance. Le NAS offre un accès fichier (partage réseau) via les protocoles SMB/NFS sur le LAN. Le SAN est plus performant mais plus coûteux et complexe.

Qu'est-ce que l'HCI et quel est son principal avantage ? :: L'Hyperconverged Infrastructure intègre calcul, stockage et réseau sur des nœuds x86 standard gérés par du software. Son principal avantage est la scalabilité scale-out : on ajoute un nœud pour augmenter simultanément compute et storage, avec une gestion centralisée simplifiée.

Quel est le protocole standard du stockage objet et qui l'a popularisé ? :: Le protocole S3 (Simple Storage Service), créé par Amazon en 2006, est devenu le standard de facto. Il permet l'accès aux objets via API HTTP/REST. MinIO et Ceph implémentent ce même protocole on-premise.

Pourquoi le stockage objet est-il particulièrement adapté au Big Data ? :: Il offre une scalabilité quasi illimitée (exaoctets), un coût très bas, et une API standard (S3) compatible avec tous les outils Big Data (Spark, Hadoop, Flink). Il est idéal pour stocker les raw data d'un data lake avant traitement.

Qu'est-ce que le NVMe-oF et pourquoi est-ce important ? :: NVMe over Fabrics est une extension du protocole NVMe (conçu pour SSD) sur réseau (Ethernet RDMA, Fibre Channel). Il permet d'atteindre des latences inférieures à 100 microsecondes pour le SAN, contre plusieurs millisecondes avec iSCSI.

Quel est le principal inconvénient de l'HCI par rapport au SAN ? :: Le couplage entre compute et storage : on ne peut pas scaler l'un sans l'autre. Si on a besoin de plus de stockage sans besoin de compute supplémentaire (ou vice versa), l'HCI est moins efficient économiquement qu'une architecture SAN/NAS découplée.

Quelle technologie open source permet de déployer un stockage objet compatible S3 on-premise ? :: MinIO (distribué sous licence Apache 2.0) et Ceph (avec son composant RadosGW). Ces solutions permettent aux entreprises de construire un stockage objet privé sans dépendance aux hyperscalers cloud.

## Sources
- IDC – "Data Age 2025 / 2030" : https://www.idc.com
- Gartner – "Magic Quadrant for Primary Storage" : https://www.gartner.com
- NetApp – Documentation ONTAP : https://docs.netapp.com
- Nutanix – "The HCI Buyer's Guide" : https://www.nutanix.com
- MinIO – Documentation officielle : https://min.io/docs
- Pure Storage – "The Future of Storage" : https://www.purestorage.com

## Notions liées
- [[Technologies de stockage]]
- [[Data Lifecycle Management]]
- [[Infrastructure des datacenters]]
- [[Modèles de déploiement cloud]]
- [[Data Mesh et Data Fabric]]
