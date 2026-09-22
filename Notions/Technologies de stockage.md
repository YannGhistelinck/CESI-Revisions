---
type: notion
thèmes:
  - SI et environnement
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Technologies de stockage

![[N — Technologies de stockage.mp3]]
## En bref
> **Définition** : Les technologies de stockage désignent l'ensemble des solutions matérielles et logicielles permettant de conserver les données d'un SI. Dans une optique Green IT, le choix de la technologie, de l'architecture et des politiques de gestion des données a un impact direct sur la consommation énergétique et les émissions de GES.
> **Pourquoi c'est important** : Le stockage est le poste de consommation électrique qui croît le plus rapidement dans les datacenters. Avec l'explosion du volume de données (+25 % par an), la DSI doit arbitrer entre performance, coût et impact environnemental pour éviter l'accumulation de "dark data" inutile.
> **Chiffres clés** :
> - Le volume mondial de données devrait atteindre **120 zettaoctets en 2023** (IDC)
> - Le stockage représente **15 à 25 %** de la consommation électrique d'un datacenter
> - La déduplication peut réduire le volume de données stockées de **50 à 95 %** selon le type de données

## Approfondir

### Fonctionnement

#### Hiérarchie des supports : du plus rapide au plus green

| Support | Technologie | Performance | Consommation | Usage typique |
|---------|-------------|-------------|--------------|---------------|
| **SSD NVMe** | Flash NAND, interface PCIe | Très haute (< 0,1 ms) | Moyenne (3–10 W) | Hot data, bases de données, VMs |
| **SSD SATA/SAS** | Flash NAND | Haute (0,1–1 ms) | Faible (2–5 W) | Données chaudes à tièdes |
| **HDD** | Plateaux magnétiques | Moyenne (5–10 ms) | Moyenne (5–12 W) | Warm data, fichiers, NAS |
| **LTO (bande magnétique)** | Bande linéaire | Faible (accès séquentiel) | Quasi nulle en veille (< 0,5 W) | Cold data, archivage long terme |
| **Stockage objet (S3)** | HDD + logiciel | Moyenne | Variable | Data lakes, médias, sauvegardes |

#### Green Storage
Approche consistant à réduire l'empreinte énergétique du stockage par :
- **Tiering automatique** : déplacer automatiquement les données vers le support le moins énergivore adapté à la fréquence d'accès
- **Déduplication** : suppression des blocs de données identiques (ratio typique 2:1 à 20:1 selon le type de données)
- **Compression** : réduction de la taille des données avant stockage (ratio 1,5:1 à 3:1)
- **Thin provisioning** : allocation dynamique de l'espace réel, évite le gaspillage de capacité pré-allouée mais inutilisée

#### Tiering (stockage hiérarchique)
Le tiering classe les données en niveaux selon leur "chaleur" (fréquence d'accès) :
- **Tier 0** : SSD NVMe (données critiques temps réel)
- **Tier 1** : SSD SATA ou HDD hautes performances (données actives)
- **Tier 2** : HDD SATA standards (données tièdes)
- **Tier 3** : LTO ou stockage objet froid (archives, conformité)

Des solutions comme **IBM Spectrum Scale**, **NetApp FabricPool**, ou **AWS S3 Intelligent-Tiering** automatisent ces déplacements selon des politiques configurables.

#### Stockage Objet (Object Storage / S3)
Paradigme de stockage où les données sont stockées sous forme d'objets (données + métadonnées + identifiant unique), sans hiérarchie de répertoires. 

Avantages Green IT :
- Supporte de très grandes densités de stockage sur HDD bon marché
- Compatible avec l'erasure coding (moins redondant que la réplication 3x)
- Interface HTTP/S3 standardisée (Amazon S3, MinIO, Ceph)

#### Erasure Coding
Alternative à la réplication 3x (RAID ou triple copie cloud). L'erasure coding découpe les données en fragments et ajoute des fragments de parité, permettant de reconstituer les données si N fragments sont perdus.

- Réplication 3x : 200 % de surcoût de stockage
- Erasure coding 8+4 : environ 50 % de surcoût de stockage
- Économie significative en espace disque, donc en énergie

#### SDS – Software-Defined Storage
Le SDS dissocie le logiciel de gestion du stockage du matériel sous-jacent. Permet d'utiliser du matériel standard (commodity hardware) moins cher et plus dense. Exemples : **Ceph**, **GlusterFS**, **vSAN**.

#### WORM et Stockage Immuable
**WORM** (Write Once, Read Many) : données écrites une fois, ne pouvant pas être modifiées ou supprimées avant une date définie. Utilisé pour la conformité réglementaire (RGPD, archives légales).
**Stockage immuable** : extension du WORM dans le cloud (ex. AWS S3 Object Lock, Azure Immutable Blob Storage). Protection contre les ransomwares.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| LTO : consommation quasi nulle en veille, très faible coût/To | LTO : accès séquentiel lent, incompatible avec accès aléatoire |
| Déduplication/compression : réduction massive des volumes | Déduplication : CPU intensif, latence additionnelle |
| Erasure coding : économie de 30–50 % d'espace vs réplication | Erasure coding : overhead de calcul, reconstruction lente |
| Thin provisioning : évite le gaspillage de capacité | Thin provisioning : risque de surprovisioning si mal géré |
| SSD NVMe : très basse latence, moins de disques nécessaires | SSD NVMe : coût plus élevé/To que HDD |

### Acteurs et solutions du marché
- **NetApp** : ONTAP, FabricPool (tiering automatique vers S3)
- **Dell EMC** : PowerStore, Isilon (scale-out NAS)
- **IBM** : Spectrum Scale, TS4500 (robotique LTO)
- **Pure Storage** : arrays 100 % flash, déduplication inline
- **Ceph / MinIO / GlusterFS** : solutions SDS open source
- **AWS** : S3, S3 Glacier, S3 Intelligent-Tiering, EBS
- **Microsoft Azure** : Blob Storage (Hot/Cool/Archive), Azure NetApp Files
- **Spectralogic / Quantum** : solutions robotiques LTO

### Cas d'usage concrets
1. **SNCF** a déployé NetApp FabricPool pour migrer automatiquement les données froides de ses baies SAN vers du stockage objet S3, réduisant sa consommation de stockage primaire de 40 %.
2. **Facebook (Meta)** utilise massivement l'erasure coding dans ses data centers pour stocker les photos et vidéos froides, économisant des centaines de pétaoctets de stockage par rapport à une réplication 3x.
3. **Bibliothèque nationale de France (BnF)** archive ses contenus numérisés sur bandes LTO dans plusieurs sites géographiques (stratégie LOCKSS : Lots of Copies Keep Stuff Safe).

### Chiffres et tendances
- Coût du stockage LTO : environ **0,005 $/Go** vs 0,02 $/Go pour HDD et 0,08 $/Go pour SSD
- Un robot LTO en veille consomme < **1 kW**, contre 5–15 kW pour une baie SAN équivalente
- L'adoption du NVMe dans les datacenters croît de **+40 % par an** (IDC, 2023)
- **90 % des données** d'une entreprise ne sont jamais réutilisées après 90 jours (Gartner)
- Le dark data (données stockées mais inutilisées) représenterait **55 % du volume total** stocké en entreprise

## Flashcards
#flashcards/SI_et_environnement/Technologies_de_stockage #flashcards/Big_DATA/Technologies_de_stockage

Qu'est-ce que le tiering de stockage ? :: Organisation des données en niveaux (tiers) selon leur fréquence d'accès, des plus rapides/coûteux (SSD NVMe) aux plus lents/économiques (LTO, stockage objet froid), avec déplacement automatique.

Quelle est la différence entre déduplication et compression ? :: La déduplication supprime les blocs de données identiques (efficace sur VM, fichiers similaires). La compression réduit la taille de chaque bloc en encodant les redondances internes. Les deux sont complémentaires.

Pourquoi l'erasure coding est-il plus green que la réplication 3x ? :: Il réduit l'overhead de stockage de ~200 % (réplication 3x) à ~50 % (ex. 8+4), économisant ainsi de l'espace disque, de l'énergie et du matériel.

Qu'est-ce que le thin provisioning ? :: Allocation dynamique de l'espace de stockage : on alloue uniquement l'espace réellement utilisé plutôt que de réserver toute la capacité demandée, évitant le gaspillage.

Quels supports sont recommandés pour le cold data dans une optique Green IT ? :: Les bandes magnétiques LTO (consommation quasi nulle en veille) et le stockage objet sur HDD avec tiering automatique (ex. S3 Glacier).

Qu'est-ce que le WORM ? :: Write Once, Read Many : données écrites une seule fois et non modifiables/supprimables avant une date fixée. Utilisé pour la conformité réglementaire et la protection contre les ransomwares.

Qu'est-ce que le SDS (Software-Defined Storage) ? :: Découplage du logiciel de gestion du stockage et du matériel physique, permettant d'utiliser du matériel standard. Exemples : Ceph, GlusterFS, VMware vSAN.

## Sources
- IDC – "Data Age 2025" (volume mondial de données) : https://www.idc.com
- SNIA – Storage Networking Industry Association (standards et bonnes pratiques) : https://www.snia.org
- GreenIT.fr – Impact environnemental du stockage : https://www.greenit.fr
- Spectralogic – Guide LTO et archivage sur bande : https://spectralogic.com
- AWS – Documentation S3 Intelligent-Tiering : https://docs.aws.amazon.com

## Notions liées
- [[Data Lifecycle Management]]
- [[Indicateurs environnementaux du SI]]
- [[Infrastructure des datacenters]]
- [[Analyse du Cycle de Vie (ACV)]]
