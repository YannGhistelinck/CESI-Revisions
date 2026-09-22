---
type: notion
thèmes:
  - IA
  - Mobilité
statut: pas vu
dernière_révision: 2026-09-08
---

# Edge AI

![[N — Edge AI.mp3]]
## En bref

### Définition
L'**Edge AI** (IA en périphérie) désigne l'exécution de modèles d'intelligence artificielle directement sur des dispositifs locaux (smartphones, capteurs IoT, caméras, véhicules, équipements industriels) plutôt que sur des serveurs cloud distants. L'inférence se fait "au plus près des données", sans ou avec peu de connectivité réseau.

### Pourquoi c'est important
L'Edge AI répond à des contraintes critiques : latence temps réel, confidentialité des données, disponibilité sans connexion, coût de bande passante et consommation énergétique. Avec l'essor de l'IoT (50+ Md de dispositifs connectés en 2025) et des usages industriels, l'IA embarquée devient un enjeu stratégique majeur.

### Chiffres clés
- Le marché de l'Edge AI devrait atteindre **107 Md$** d'ici 2030 (MarketsandMarkets, TCAM ~20 %).
- **55 %** des données mondiales seront traitées à la périphérie d'ici 2025 (IDC).
- Un modèle de détection d'objet peut fonctionner à **< 5 ms** de latence en local vs **50-200 ms** avec un aller-retour cloud.
- Apple Neural Engine (A17 Pro) : **35 TOPS** (tera-opérations par seconde) pour l'inférence IA sur mobile.

---

## Approfondir

### Fonctionnement

#### Architecture Edge AI

```
Dispositif Edge (capteur, smartphone, caméra)
       ↓  [Inférence locale — modèle léger]
  Edge Gateway / Fog Node
       ↓  [Agrégation, pré-filtrage]
    Cloud / Datacenter
       ↓  [Ré-entraînement, modèles lourds]
```

L'inférence (prédiction) s'effectue en local ; l'entraînement reste généralement dans le cloud, puis le modèle est déployé (pushed) sur le dispositif.

#### Techniques clés pour des modèles légers (TinyML / Efficient AI)

| Technique | Description | Gain |
|---|---|---|
| **Quantization** | Réduction de la précision des poids (float32 → int8) | Taille ÷ 4, vitesse ×2-4 |
| **Pruning (élagage)** | Suppression des connexions/neurones peu contributifs | Taille ÷ 2-10 |
| **Knowledge distillation** | Entraîner un petit modèle "élève" à imiter un grand modèle "professeur" | Modèle léger à précision proche |
| **Architecture dédiée** | MobileNet, EfficientNet, SqueezeNet, YOLO Nano | Conçus nativement pour l'edge |
| **NAS (Neural Architecture Search)** | Recherche automatique d'architecture optimale pour une contrainte matérielle | Optimisation sur mesure |

#### Hardware spécialisé
- **NPU (Neural Processing Unit)** : Apple Neural Engine, Qualcomm Hexagon.
- **GPU embarqué** : NVIDIA Jetson (nano, Orin).
- **FPGA** : Intel (Altera), Xilinx — reconfigurables pour l'inférence.
- **MCU avec IA** : STM32, Arduino Nano 33 BLE (TinyML).
- **TPU Edge** : Google Coral (USB, module PCIe).

### Avantages / Inconvénients

| Avantages | Inconvénients / Défis |
|---|---|
| Latence ultra-faible (temps réel) | Puissance de calcul et mémoire limitées |
| Fonctionne hors connexion | Modèles moins précis que les versions cloud |
| Confidentialité : données traitées en local | Mise à jour et gestion du parc de dispositifs complexe |
| Économie de bande passante | Hétérogénéité matérielle = fragmentation |
| Résilience (pas de dépendance au cloud) | Sécurité physique des dispositifs (tampering) |
| Moindre consommation réseau | Coût de développement des modèles optimisés |

### Acteurs
- **NVIDIA** : Jetson (plateforme edge IA industrielle et robotique).
- **Google** : TensorFlow Lite, Coral (TPU Edge).
- **Apple** : Neural Engine intégré aux puces A/M-series.
- **Qualcomm** : AI Engine dans les SoC Snapdragon (mobile, automobile).
- **ARM** : architectures Cortex-M avec support TinyML (Ethos NPU).
- **STMicroelectronics** : microcontrôleurs STM32 pour TinyML.
- **Edge Impulse** : plateforme de développement TinyML.

### Cas d'usage
- **Vision industrielle** : détection de défauts sur chaîne de production en temps réel (< 10 ms).
- **Véhicules autonomes** : perception (LiDAR, caméras) traitée localement par l'ECU/SoC du véhicule.
- **Santé / Wearables** : détection d'arythmie cardiaque sur Apple Watch, glucomètre intelligent.
- **Retail** : caméras de comptage et d'analyse comportementale en magasin sans envoi d'images au cloud.
- **Agriculture de précision** : drones analysant les cultures et ajustant les traitements en vol.
- **Smart Grid** : détection d'anomalies sur réseau électrique par capteurs distribués.
- **Défense** : drones de reconnaissance autonomes en zone de déni d'accès réseau.

### Chiffres complémentaires
- **TinyML** : le marché des microcontrôleurs capables d'exécuter du ML devrait dépasser **70 Md d'unités** en 2030 (ABI Research).
- Réduction de la latence : l'edge réduit le temps de réponse de **60 à 80 %** par rapport au cloud pour les applications temps réel.
- **80 %** de la consommation énergétique des réseaux mobiles pourrait être réduite par le traitement edge (ETSI).

---

## Flashcards
#flashcards/IA/Edge_AI #flashcards/Mobilité/Edge_AI

**Qu'est-ce que l'Edge AI ?** :: Exécution de modèles IA directement sur des dispositifs locaux (smartphones, capteurs, caméras) sans dépendance au cloud, pour des raisons de latence, confidentialité et disponibilité hors ligne.

**Quelle est la différence entre entraînement et inférence dans l'Edge AI ?** :: L'entraînement reste généralement dans le cloud (ressources importantes) ; l'inférence (prédiction) est déployée et exécutée localement sur le dispositif edge.

**Qu'est-ce que la quantization en IA embarquée ?** :: Technique réduisant la précision des poids du modèle (ex. : float32 → int8) pour diviser la taille par 4 et accélérer l'inférence, avec une perte minime de précision.

**Citez trois exemples de hardware spécialisé pour l'Edge AI.** :: NVIDIA Jetson (GPU embarqué), Google Coral (TPU Edge), Apple Neural Engine (NPU intégré aux puces A/M-series).

**Qu'est-ce que le TinyML ?** :: Branche de l'Edge AI consistant à faire tourner des modèles de machine learning sur des microcontrôleurs très contraints (quelques centaines de kB de mémoire, quelques mW de consommation).

**Pourquoi l'Edge AI est-il préféré au cloud pour les véhicules autonomes ?** :: La latence d'un aller-retour cloud (50-200 ms) est incompatible avec les décisions de sécurité temps réel (freinage, évitement) qui requièrent moins de 10 ms. Le traitement doit être local et fonctionner même sans réseau.

**Quels sont les deux principaux défis de l'Edge AI ?** :: La capacité de calcul et mémoire limitées des dispositifs (nécessitant des modèles compressés) et la gestion du cycle de vie des modèles sur un parc hétérogène de dispositifs distribués.

---

## Sources
- MarketsandMarkets, "Edge AI Market — Global Forecast to 2030", 2023
- IDC, "Data Age 2025 — The Digitization of the World", 2023
- Pete Warden & Daniel Situnayake, *TinyML*, O'Reilly, 2019
- NVIDIA, Jetson Platform Documentation — [developer.nvidia.com](https://developer.nvidia.com/embedded/jetson)
- Edge Impulse — [edgeimpulse.com](https://edgeimpulse.com)
- Google, TensorFlow Lite — [tensorflow.org/lite](https://www.tensorflow.org/lite)

---

## Notions liées
- [[Edge Computing]]
- [[Digital Twin]]
- [[Industrie 4.0 et XR]]
- [[IoT]] 
- [[Gestion de la mobilité (UEM)]]
- [[IA de confiance et IA responsable]]
- [[Écoconception logicielle]]
