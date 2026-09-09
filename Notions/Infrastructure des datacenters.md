---
type: notion
thèmes:
  - SI et environnement
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Infrastructure des datacenters

## En bref
> **Définition** : L'infrastructure d'un datacenter comprend l'ensemble des équipements physiques et logiciels assurant l'alimentation électrique, la connectivité, la supervision et la gestion des ressources de calcul. La DSI pilote ces infrastructures avec des outils DCIM et cherche à maximiser le taux d'utilisation via la virtualisation, tout en sécurisant l'alimentation avec des UPS et PDU intelligents.
> **Pourquoi c'est important** : L'optimisation de l'infrastructure datacenter est le levier le plus direct pour réduire la consommation électrique d'un SI. La consolidation des serveurs physiques et la virtualisation permettent de réduire de 80 % le nombre de serveurs nécessaires, donc leur consommation.
> **Chiffres clés** :
> - Le taux d'utilisation moyen d'un serveur physique sans virtualisation : **5 à 15 %** (IDC)
> - La virtualisation peut réduire le nombre de serveurs physiques d'un rapport **5:1 à 20:1**
> - Les UPS inefficaces peuvent représenter **5 à 15 %** de pertes électriques supplémentaires

## Approfondir

### Fonctionnement

#### Consolidation de datacenters
La consolidation consiste à réduire le nombre de datacenters et/ou de serveurs physiques en regroupant les charges de travail. Elle est souvent couplée à une migration vers le cloud.

Étapes typiques :
1. **Inventaire et cartographie** des assets (CMDB)
2. **Analyse de l'utilisation réelle** (monitoring CPU, RAM, stockage)
3. **Identification des serveurs sous-utilisés** (< 20 % CPU moyen)
4. **Plan de consolidation** : virtualisation, migration cloud, décommissionnement
5. **Exécution et validation** des performances post-consolidation

Bénéfices Green IT :
- Réduction du nombre de serveurs → moins de consommation
- Réduction de l'espace nécessaire → moins de refroidissement
- Possibilité de fermer des salles entières

#### DCIM – Data Center Infrastructure Management
Logiciel de supervision centralisée de l'infrastructure physique du datacenter :
- **Surveillance en temps réel** : puissance consommée par baie, température par zone, état des onduleurs
- **Modélisation 3D** : localisation précise de chaque équipement, gestion des câbles
- **Planification de capacité** : prévision de la saturation électrique et thermique
- **Calcul automatique du PUE** : en temps réel
- **Alertes et seuils** : notification avant qu'une baie ne dépasse sa capacité électrique ou thermique

Principaux éditeurs : **Schneider Electric EcoStruxure IT**, **Vertiv Trellis**, **nlyte** (IBM), **Sunbird DCIM**, **Siemens Data Center Operations**.

#### UPS – Onduleurs (Uninterruptible Power Supply)
Les UPS protègent les équipements contre les coupures et fluctuations électriques. Ils représentent une source de pertes importantes si mal dimensionnés :
- Un UPS fonctionnant à **25 % de sa capacité** a un rendement de ~85 %
- Un UPS fonctionnant à **80 % de sa capacité** a un rendement de ~95–97 %
- Technologie recommandée : **double conversion Online** avec mode ECO pour les charges stables
- Les UPS modernes (ex. Schneider Galaxy VS) atteignent un rendement de **99 %** en mode ECO

Stratégie Green : dimensionner les UPS au plus proche de la charge réelle, utiliser des batteries Lithium-Ion (plus légères, plus longue durée de vie que le plomb).

#### PDU Intelligent – Power Distribution Unit
Les PDU (multiprises rack) distribuent l'électricité aux équipements. Un PDU intelligent ajoute :
- **Mesure de consommation** par prise (watt-heure en temps réel)
- **Contrôle à distance** des prises (reboot d'un serveur à distance)
- **Alertes** sur dépassement de seuil par prise ou par circuit
- **Remontée des données** vers le DCIM

Permet une granularité fine de la mesure, indispensable pour calculer un PUE précis et identifier les équipements énergivores.

#### Norme 80 PLUS Titanium
Programme de certification de l'efficacité des alimentations électriques des serveurs (PSU) :

| Niveau | Rendement à 20 % | Rendement à 50 % | Rendement à 100 % |
|--------|-----------------|-----------------|-------------------|
| 80 PLUS Bronze | 82 % | 85 % | 82 % |
| 80 PLUS Gold | 87 % | 90 % | 87 % |
| 80 PLUS Platinum | 90 % | 92 % | 89 % |
| **80 PLUS Titanium** | **90 %** | **96 %** | **94 %** |

Exiger des PSU 80 PLUS Titanium dans les appels d'offres matériel est une bonne pratique Green IT immédiate.

#### Virtualisation des serveurs
La virtualisation crée des machines virtuelles (VM) sur un hyperviseur qui partage les ressources d'un serveur physique entre plusieurs charges de travail :
- **VMware vSphere / ESXi** : hyperviseur de référence entreprise
- **Microsoft Hyper-V** : intégré à Windows Server
- **KVM / Proxmox** : open source
- **Xen** : utilisé par AWS en base

Impact énergétique : un serveur physique consomme presque autant à 10 % qu'à 80 % de charge (la consommation est peu proportionnelle à l'utilisation). La consolidation de 10 VM sur 1 hôte plutôt que 10 serveurs physiques peut diviser la consommation par 5 à 10.

Technologies complémentaires :
- **vMotion / Live Migration** : déplacement de VM en cours d'exécution entre hôtes, sans interruption, pour optimiser la charge
- **DRS (Distributed Resource Scheduler)** : équilibrage automatique de charge entre hôtes d'un cluster
- **Power Management** : extinction automatique des hôtes inutilisés en période creuse

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Virtualisation : réduction massive du nombre de serveurs physiques | Virtualisation : hyperviseur = point unique de défaillance si mal architecturé |
| DCIM : visibilité complète, base de décision pour l'optimisation | DCIM : coût de déploiement élevé, nécessite une base de données assets à jour |
| PDU intelligent : mesure granulaire, contrôle à distance | PDU intelligent : surcoût vs PDU standard, gestion des accès |
| 80 PLUS Titanium : rendement > 94 % à mi-charge | Alimentations Titanium : prix d'achat plus élevé |
| Consolidation : fermeture de salles, réduction de l'empreinte foncière | Consolidation : risque de SPOF, projet complexe avec beaucoup de parties prenantes |

### Acteurs et solutions du marché
- **VMware (Broadcom)** : vSphere, vSAN, vRealize
- **Microsoft** : Hyper-V, Azure Arc (gestion hybride)
- **Schneider Electric** : EcoStruxure IT (DCIM), Galaxy UPS, PDU intelligents
- **Vertiv** : UPS Liebert, Trellis DCIM
- **Sunbird Software** : DCIM mid-market
- **Nutanix** : HCI (Hyper-Converged Infrastructure), simplifie la consolidation
- **HPE, Dell, Lenovo** : serveurs avec gestion d'énergie intégrée (iLO, iDRAC, XCC)

### Cas d'usage concrets
1. **La DSI de l'État français** (DINUM) a piloté la consolidation des datacenters ministériels via le programme SWITCH, réduisant de 900 à moins de 100 salles informatiques, avec une économie estimée à plusieurs dizaines de millions d'euros par an.
2. **Air France** a virtualisé 95 % de son parc serveur sur VMware vSphere, passant de 4 000 serveurs physiques à 400, réduisant sa consommation de 60 % et libérant 1 500 m² de salle serveur.
3. **Renault** déploie des PDU intelligents Schneider Electric dans ses datacenters européens, permettant un suivi par prise et une réduction de 12 % de la consommation identifiée comme inutile (serveurs zombies non éteints).

### Chiffres et tendances
- Le marché mondial du DCIM devrait atteindre **5,1 Md$ en 2028** (MarketsandMarkets)
- Un serveur "zombie" (allumé mais sans charge utile) représente **200 à 500 W** gaspillés en permanence ; 20–30 % des serveurs en entreprise seraient dans cet état (Anthesis Group)
- Le taux de virtualisation moyen dans les entreprises françaises dépasse **80 %** (IDC France, 2022)
- La migration vers le cloud public peut réduire l'empreinte carbone IT de **65 à 84 %** vs datacenter on-premise (étude Accenture/WSP pour Microsoft, 2020)

## Flashcards
#flashcards

Qu'est-ce qu'un DCIM et à quoi sert-il ? :: Data Center Infrastructure Management : logiciel de supervision centralisée du datacenter (consommation par baie, température, état des UPS, PUE temps réel, planification de capacité).

Pourquoi un UPS doit-il fonctionner proche de sa charge nominale ? :: Un UPS à 25 % de charge a un rendement de ~85 % (15 % de pertes). À 80 % de charge, il atteint 95–97 %. Le surdimensionnement génère donc des pertes importantes.

Que signifie la certification 80 PLUS Titanium ? :: L'alimentation d'un serveur (PSU) atteint au moins 96 % de rendement à 50 % de charge, 94 % à 100 % de charge. C'est le niveau le plus élevé de la certification.

Comment la virtualisation réduit-elle la consommation énergétique ? :: En consolidant plusieurs charges de travail sur un seul serveur physique, elle augmente le taux d'utilisation réel (de 5–15 % à 70–80 %) et permet d'éteindre des serveurs physiques. Rapport 5:1 à 20:1.

Qu'est-ce qu'un serveur zombie et quel est son impact ? :: Serveur physique allumé et alimenté mais sans charge utile. Consomme 200–500 W inutilement. Représenterait 20–30 % du parc dans certaines organisations.

Qu'est-ce que le vMotion (VMware) / Live Migration (Hyper-V) ? :: Déplacement d'une VM en cours d'exécution d'un hôte physique à un autre, sans interruption de service. Permet d'optimiser la charge des hôtes et d'éteindre les hôtes sous-utilisés.

Qu'est-ce qu'un PDU intelligent ? :: Power Distribution Unit avec mesure de consommation par prise, contrôle à distance et remontée de métriques vers le DCIM. Permet d'identifier les équipements énergivores à la granularité de la prise électrique.

## Sources
- Schneider Electric – White papers DCIM et efficacité datacenter : https://www.se.com
- VMware – "VMware Sustainability Report" : https://www.vmware.com/company/sustainability.html
- IDC – "Server Virtualization and Consolidation" : https://www.idc.com
- DINUM – Programme SWITCH de consolidation des datacenters de l'État : https://www.numerique.gouv.fr
- Uptime Institute – "Global Data Center Survey" : https://uptimeinstitute.com
- 80 PLUS – Programme de certification : https://www.plugloadsolutions.com

## Notions liées
- [[Refroidissement des datacenters]]
- [[Indicateurs environnementaux du SI]]
- [[Projets innovants de datacenters]]
- [[VDI et client léger]]
- [[Analyse du Cycle de Vie (ACV)]]
