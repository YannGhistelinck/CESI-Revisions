---
type: notion
thèmes:
  - Développement
  - IA
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Digital Twin

## En bref
> **Définition** : Un jumeau numérique (digital twin) est une réplique virtuelle dynamique d'un objet physique, d'un processus, d'un système ou d'une organisation, alimentée en temps réel par des données issues de capteurs IoT, de systèmes d'information ou de simulations. Il permet de surveiller, simuler, analyser et optimiser son homologue physique sans intervention sur le réel.
> **Pourquoi c'est important** : Pour une DSI, le digital twin représente la convergence entre le monde opérationnel (OT) et le monde informatique (IT). Il permet d'anticiper les pannes, d'optimiser les processus, de tester des scénarios "what-if" sans risque, et de former des opérateurs sur des répliques fidèles de systèmes critiques.
> **Chiffres clés** :
> - Le marché mondial des digital twins est estimé à 73,5 Md$ en 2027, avec une croissance de 35 % par an (MarketsandMarkets, 2022).
> - 36 % des entreprises industrielles utilisent des jumeaux numériques en 2023 (Gartner).
> - Les entreprises utilisant des digital twins réduisent leurs coûts de maintenance de 25 % et leurs temps d'arrêt de 35 % (Siemens, 2023).

## Approfondir

### Fonctionnement

**Architecture d'un jumeau numérique**
Un digital twin repose sur trois composants fondamentaux :
1. **L'entité physique** : l'objet réel (machine, bâtiment, réseau, processus, humain).
2. **Le jumeau numérique** : le modèle virtuel maintenu à jour (modèle 3D, équations physiques, état courant).
3. **Le lien de données** : flux bidirectionnel entre le physique et le virtuel (capteurs IoT → jumeau, et commandes jumeau → actionneurs physiques).

**Types de jumeaux numériques**
- **Digital Twin du produit** : réplique d'un produit tout au long de son cycle de vie (conception, fabrication, utilisation, recyclage). Ex : jumeau d'un moteur d'avion Rolls-Royce.
- **Digital Twin du processus** : réplique d'un processus de production ou logistique pour optimisation en temps réel. Ex : jumeau d'une chaîne de montage automobile.
- **Digital Twin du système** : réplique d'un système complexe composé de multiples équipements. Ex : jumeau d'un réseau électrique ou d'une ville (Singapore Digital Twin).
- **Digital Twin d'infrastructure IT** : réplique de l'infrastructure informatique (réseau, datacenter, cloud) pour la gestion des capacités et la simulation de pannes.

**BIM (Building Information Modeling)**
Le BIM est la norme de modélisation numérique du bâtiment et de l'infrastructure (norme ISO 19650). Un modèle BIM enrichi de données IoT et de flux temps réel constitue un digital twin du bâtiment. Utilisé pour la gestion de l'énergie, la maintenance prédictive, la sécurité incendie. Niveaux de maturité BIM : LOD 100 à LOD 500.

**Digital Twin d'infrastructure IT**
Réplique virtuelle de l'infrastructure réseau et cloud permettant de simuler l'impact d'une modification avant déploiement, de détecter des goulots d'étranglement, de tester la résilience. Exemples : NVIDIA Omniverse pour les datacenters, Forward Networks pour les réseaux.

**Rôle de l'IA dans les jumeaux numériques**
- **Maintenance prédictive** : des modèles ML analysent les données capteurs du jumeau pour prédire les pannes avant qu'elles surviennent.
- **Optimisation** : des algorithmes d'optimisation (reinforcement learning) testent des stratégies opérationnelles sur le jumeau avant de les appliquer au réel.
- **Simulation de scénarios** : des modèles physiques (éléments finis, CFD) simulés sur GPU permettent des tests "what-if" (ex : impact d'un séisme sur un pont).
- **Génération automatique de jumeaux** : des modèles de computer vision et de LiDAR permettent de générer automatiquement un jumeau numérique à partir de scans 3D.

**NVIDIA Omniverse et le Metaverse industriel**
NVIDIA Omniverse est une plateforme de simulation et de collaboration 3D basée sur Universal Scene Description (USD) de Pixar. Elle est la fondation technologique du "Metaverse industriel" (concept BMW, Siemens, Ericsson) : un espace virtuel partagé où des jumeaux numériques d'usines entières sont simulés en temps réel sur GPU.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction des coûts de maintenance (prédictif vs curatif) | Complexité et coût de création du modèle initial |
| Test de scénarios sans risque sur le réel | Synchronisation temps réel exigeante en bande passante et calcul |
| Optimisation continue des processus par l'IA | Qualité du jumeau dépend de la qualité des données capteurs (GIGO) |
| Formation sur réplique fidèle de systèmes critiques | Cybersécurité : le jumeau est une cible d'attaque (accès au réel via le virtuel) |
| Traçabilité complète du cycle de vie produit | Interopérabilité difficile entre les plateformes (pas de standard universel) |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Siemens | Xcelerator (platform digital twin), Teamcenter, NX, jumeaux de production |
| NVIDIA | Omniverse — simulation 3D collaborative, jumeaux numériques d'usines |
| PTC | ThingWorx (IoT + digital twin), Vuforia (RA sur jumeau) |
| Dassault Systèmes | 3DEXPERIENCE platform, SIMULIA (simulation physique), CATIA |
| Microsoft | Azure Digital Twins (service managé), Azure IoT Hub |
| GE | Predix (jumeaux numériques industriels, maintenance prédictive turbines) |
| Forward Networks | Digital twin du réseau informatique pour analyse et simulation |
| Bentley Systems | iTwin (digital twin d'infrastructure civile, BIM connecté) |

### Cas d'usage concrets
1. **Rolls-Royce** : chaque moteur d'avion vendu possède un jumeau numérique alimenté par 100+ capteurs. Des algorithmes de ML prédisent les besoins de maintenance moteur par moteur, réduisant les immobilisations non planifiées de 30 %.
2. **Singapore National Digital Twin** : Singapour a créé un jumeau numérique de l'intégralité de la ville (bâtiments, réseaux, trafic, eau), utilisé pour la planification urbaine, la gestion des crises et l'optimisation énergétique.
3. **BMW Group** : utilise NVIDIA Omniverse pour simuler ses usines de production (ex : usine de Munich) avant tout changement physique, testant virtuellement des milliers de scénarios d'optimisation et formant les équipes sur le jumeau.

### Chiffres et tendances
- 70 % des entreprises industrielles prévoient d'investir dans les digital twins d'ici 2025 (IDC, 2023).
- La maintenance prédictive via digital twin réduit les coûts de maintenance de 10 à 25 % et les pannes de 70 % (McKinsey, 2022).
- NVIDIA estime que chaque euro investi dans l'Omniverse pour la simulation industrielle rapporte 10 euros en réduction de coûts de mise en service.
- Le BIM est désormais obligatoire pour les projets publics > 1 M€ en France (Loi ELAN, 2018 — décrets d'application progressifs).

## Flashcards
#flashcards
- Qu'est-ce qu'un jumeau numérique (digital twin) ? :: Une réplique virtuelle dynamique d'un objet ou système physique, alimentée en temps réel par des données capteurs, permettant de surveiller, simuler et optimiser son homologue réel.
- Quels sont les trois composants fondamentaux d'un digital twin ? :: L'entité physique, le jumeau numérique (modèle virtuel), et le lien de données bidirectionnel (capteurs IoT → jumeau, commandes → actionneurs).
- Qu'est-ce que le BIM ? :: Building Information Modeling — norme ISO 19650 de modélisation numérique du bâtiment ; un modèle BIM enrichi de données temps réel constitue un digital twin du bâtiment.
- Quel est le rôle de l'IA dans un digital twin ? :: Maintenance prédictive (ML sur données capteurs), optimisation (reinforcement learning), simulation "what-if", et génération automatique de jumeaux (computer vision, LiDAR).
- Qu'est-ce que NVIDIA Omniverse ? :: Une plateforme de simulation et collaboration 3D basée sur USD (Universal Scene Description), fondation du Metaverse industriel pour simuler des usines entières en temps réel.
- Quel est le principal risque cybersécurité lié aux digital twins ? :: Le jumeau peut être une cible d'attaque donnant accès aux commandes du système réel via l'interface numérique-physique.
- Qu'est-ce que la maintenance prédictive ? :: L'utilisation de modèles ML analysant les données capteurs d'un équipement (via son jumeau numérique) pour anticiper les pannes avant qu'elles surviennent, évitant les arrêts non planifiés.

## Sources
- MarketsandMarkets Digital Twin Market Report 2022 : https://www.marketsandmarkets.com/Market-Reports/digital-twin-market-225269522.html
- Siemens Digital Twin : https://www.siemens.com/global/en/products/automation/topic-areas/digital-twin.html
- NVIDIA Omniverse : https://www.nvidia.com/en-us/omniverse/
- Microsoft Azure Digital Twins : https://azure.microsoft.com/en-us/products/digital-twins/
- Bentley iTwin : https://www.bentley.com/software/itwin-platform/
- ISO 19650 (BIM) : https://www.iso.org/standard/68078.html

## Notions liées
- [[Réalité étendue (XR)]]
- [[Industrie 4.0 et XR]]
- [[Big Data — fondamentaux]]
- [[Infrastructure des datacenters]]
- [[Écoconception logicielle]]
- [[IA en cybersécurité]]
