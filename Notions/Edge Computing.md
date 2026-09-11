---
type: notion
thèmes:
  - Mobilité
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Edge Computing

## En bref
> **Définition** : L'edge computing (calcul en périphérie) est un paradigme d'architecture dans lequel le traitement des données s'effectue au plus près de la source (capteurs, appareils IoT, terminaux mobiles), plutôt que d'envoyer toutes les données vers un datacenter central ou le cloud. L'objectif est de réduire la latence, économiser la bande passante et permettre un traitement en temps réel là où la connectivité peut être limitée ou intermittente.
> **Pourquoi c'est important** : Avec l'explosion de l'IoT (des milliards d'objets connectés) et des usages temps réel (véhicules autonomes, chirurgie à distance, contrôle industriel), l'envoi de toutes les données vers le cloud centralisé est devenu impossible : la bande passante serait saturée et la latence inacceptable. L'edge computing est une réponse architecturale à ces contraintes, complémentaire du cloud.
> **Chiffres clés** :
> - Le marché mondial de l'edge computing était estimé à **61 milliards USD en 2023**, en croissance de 37 % par an (Grand View Research, 2024)
> - **75 % des données d'entreprise** seront créées et traitées à l'extérieur des datacenters traditionnels d'ici 2025 (Gartner)
> - Un véhicule autonome génère entre **4 et 8 To de données par jour** — impossible à envoyer intégralement dans le cloud en temps réel

## Approfondir

### Fonctionnement

**Architecture en couches de l'edge computing**

L'architecture edge computing se représente en trois couches :

```
[Devices / Capteurs / IoT]  ←  Cloud lointain (latence élevée, bande passante)
        ↓
[Edge Layer / Périphérie]   ←  Traitement local, faible latence
        ↓
[Cloud Central]              ←  Stockage long terme, analytics globaux
```

**Composants de l'edge :**
- **Edge device** : le terminal lui-même (smartphone, caméra, capteur industriel) avec capacité de calcul embarquée (ex : GPU embarqué dans une caméra IA)
- **Edge gateway / Edge node** : serveur ou boîtier physique déployé sur site (dans une usine, un magasin, une antenne 5G) qui agrège et prétraite les données avant de les envoyer au cloud
- **Far edge** : infrastructure de calcul dans les locaux du client (on-premises)
- **Near edge** : infrastructure dans des points de présence régionaux (PoP) ou datacenters d'opérateurs télécom

**Fog Computing**
Concept introduit par Cisco, parfois utilisé comme synonyme d'edge computing mais plus précis : le fog computing désigne une couche intermédiaire entre les devices IoT et le cloud, constituée de nœuds de calcul distribués sur le réseau (routeurs, switchs, gateways avec capacité de calcul). Le fog computing est une forme d'edge computing qui s'appuie sur l'infrastructure réseau existante.

**Latence — le critère clé**
La latence est le délai entre l'émission d'une donnée et la réception de la réponse :
- Cloud centralisé (datacenter distant) : 50 à 150 ms
- Edge régional (PoP opérateur) : 5 à 20 ms
- Far edge (on-premises) : < 5 ms
- Exigences temps réel (chirurgie robotique, véhicule autonome) : < 1 ms

**5G et edge computing**
La 5G est un catalyseur majeur de l'edge computing grâce à sa latence ultra-faible (< 1 ms dans les configurations avancées) et à l'architecture MEC (Multi-access Edge Computing) qui place des serveurs de calcul au niveau des antennes 5G. Les opérateurs télécom deviennent ainsi des fournisseurs de capacité edge.

**Edge computing vs Cloud computing**

| Critère | Cloud Computing | Edge Computing |
|---------|----------------|----------------|
| Localisation du traitement | Datacenter centralisé | Au plus proche de la source |
| Latence | 50-150 ms | < 5 ms |
| Bande passante | Consomme beaucoup | Économise la bande passante |
| Disponibilité offline | Non | Oui (traitement local) |
| Scalabilité | Infinie (cloud élastique) | Limitée par les ressources locales |
| Gestion et maintenance | Centralisée | Distribuée et complexe |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Latence ultra-faible pour les traitements temps réel | Gestion distribuée complexe (milliers de nœuds edge) |
| Réduction de la bande passante consommée (filtrage local) | Coût d'infrastructure physique edge plus élevé |
| Fonctionnement hors ligne (déconnecté du cloud) | Sécurité plus difficile à assurer sur des nœuds dispersés |
| Traitement de données sensibles en local (conformité RGPD) | Mises à jour et maintenance sur des équipements distants |
| Scalabilité par multiplication des nœuds | Hétérogénéité des équipements (standardisation difficile) |
| Traitement des volumes massifs de données IoT | Durée de vie limitée des équipements en environnement industriel |

### Acteurs et solutions du marché

| Acteur | Solution | Positionnement |
|--------|----------|----------------|
| AWS | AWS Greengrass, AWS Outposts | Edge IoT et cloud hybride |
| Microsoft Azure | Azure IoT Edge, Azure Stack Edge | Edge industriel et hybride |
| Google | Google Distributed Cloud Edge | Edge opérateur et entreprise |
| Cisco | Cisco Edge Intelligence | Fog computing et réseau edge |
| HPE | HPE Edgeline, GreenLake | Infrastructure edge industrielle |
| Dell | Dell EMC Streaming Data Platform | Edge data management |
| NVIDIA | Jetson (edge AI) | Edge AI avec GPU embarqués |
| Opérateurs télécom | MEC 5G (Orange, SFR, Bouygues) | Edge au niveau des antennes 5G |

### Cas d'usage concrets

**1. Contrôle qualité en temps réel dans une usine (Industrie 4.0)**
Un constructeur automobile déploie des caméras IA équipées de puces NVIDIA Jetson sur sa ligne d'assemblage. Les images sont analysées localement (edge) en moins de 10 ms : les pièces défectueuses sont détectées et écartées sans attendre le cloud. Seules les anomalies statistiques et les données de pilotage sont remontées au cloud pour l'analyse globale. La bande passante consommée est réduite de 90 %.

**2. Véhicule autonome**
Les véhicules autonomes Level 4 embarquent plusieurs dizaines de capteurs (LIDAR, radar, caméras) générant 4 à 8 To/jour. Le traitement de la perception (détection des obstacles, décision de freinage) doit s'effectuer en moins de 50 ms — impossible via le cloud. Tout le traitement critique est réalisé en local (edge embarqué). Le cloud reçoit uniquement les données anonymisées d'apprentissage pour améliorer les modèles IA.

**3. Réseau de distribution d'énergie intelligente**
Un opérateur d'énergie déploie des edge gateways sur 5 000 transformateurs électriques. Chaque gateway analyse les données de consommation localement, détecte les anomalies (surcharges, pannes) et déclenche des actions correctives en temps réel. Seules les données agrégées sont transmises au cloud pour le pilotage global du réseau. La résilience est assurée même en cas de coupure réseau.

### Chiffres et tendances

- **IDC** prédit 55,7 milliards d'appareils IoT connectés d'ici 2025, générant 79,4 zettaoctets de données
- **75 % des données d'entreprise** seront créées et traitées hors des datacenters centraux d'ici 2025 (Gartner)
- Le marché du MEC (Multi-access Edge Computing) avec la 5G est estimé à **15 milliards USD en 2030** (GSMA Intelligence)
- **AWS Greengrass** est déployé sur plus de 100 millions d'appareils IoT (Amazon, 2023)
- Tendance : **edge AI** — déploiement de modèles de machine learning directement sur les nœuds edge (TensorFlow Lite, ONNX Runtime, NVIDIA Triton) pour des décisions autonomes sans connexion cloud
- Convergence **edge + 5G + IA** : les opérateurs télécom ouvrent leurs infrastructures MEC à des services edge managés pour les entreprises

## Flashcards
#flashcards

Qu'est-ce que l'edge computing et pourquoi s'oppose-t-il au cloud centralisé ? :: L'edge computing consiste à traiter les données au plus proche de leur source (capteurs, terminaux), plutôt que de les envoyer vers un datacenter distant. Il s'oppose au cloud centralisé car il réduit la latence (< 5 ms vs 50-150 ms), économise la bande passante et permet un fonctionnement hors ligne — indispensable pour les usages temps réel.

Quelle est la différence entre edge computing et fog computing ? :: Le fog computing est un type d'edge computing qui utilise des nœuds de calcul intégrés à l'infrastructure réseau existante (routeurs, switchs, gateways) pour créer une couche intermédiaire entre les devices IoT et le cloud. L'edge computing est le terme générique, le fog en est une déclinaison réseau.

Pourquoi la 5G est-elle un catalyseur de l'edge computing ? :: La 5G apporte une latence ultra-faible (< 1 ms dans les configurations avancées) et une architecture MEC (Multi-access Edge Computing) qui place des serveurs de calcul au niveau des antennes. Cela permet un traitement edge ultra-proche des terminaux mobiles, ouvrant la voie aux applications temps réel (chirurgie robotique, réalité augmentée industrielle).

Donnez deux exemples concrets d'usage de l'edge computing. :: 1) Contrôle qualité par vision IA dans une usine : les caméras edge analysent les pièces en moins de 10 ms, détectent les défauts sans connexion cloud. 2) Véhicule autonome : le traitement de la perception (obstacles, freinage) est intégralement local car les 4 à 8 To/jour générés ne peuvent être envoyés au cloud en temps réel.

Quels sont les principaux défis de l'edge computing pour une DSI ? :: Gestion distribuée complexe (milliers de nœuds edge à surveiller et mettre à jour), sécurité difficile sur des équipements dispersés et physiquement accessibles, hétérogénéité des équipements, coût d'infrastructure physique et maintenance sur site.

Quelle est la règle générale pour décider ce qui est traité en edge vs dans le cloud ? :: Les données critiques en temps réel (décisions en < 10 ms), les données volumineuses non pertinentes pour le cloud et les données sensibles à la conformité locale (RGPD) sont traitées en edge. Les données historiques pour l'analyse, l'entraînement des modèles IA et le pilotage global sont remontées au cloud.

## Sources

- Gartner, "Edge Computing: Key Trends and Predictions", 2023
- Grand View Research, "Edge Computing Market Size", 2024
- IDC, "IoT and Edge Computing Forecast", 2024
- AWS Documentation, "AWS Greengrass", aws.amazon.com
- Microsoft Azure Documentation, "Azure IoT Edge", learn.microsoft.com
- GSMA Intelligence, "The 5G Era: Age of Boundless Connectivity", 2023
- NVIDIA, "Edge AI and Embedded Computing", nvidia.com

## Notions liées
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Infrastructure des datacenters]]
- [[Industrie 4.0 et XR]]
- [[Digital Twin]]
- [[Cloud Native et 12-Factor App]]
- [[Modèles de déploiement cloud]]
- [[RPA (Robotic Process Automation)]]
- [[5G et réseaux mobiles]]
