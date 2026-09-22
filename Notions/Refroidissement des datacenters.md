---
type: notion
thèmes:
  - SI et environnement
statut: pas vu
dernière_révision: 
---

# Refroidissement des datacenters

![[N — Refroidissement des datacenters.mp3]]
## En bref
> **Définition** : Le refroidissement des datacenters désigne l'ensemble des techniques permettant d'évacuer la chaleur produite par les équipements informatiques. C'est le principal poste de dépense énergétique après l'IT lui-même, représentant typiquement 30 à 40 % de la consommation totale d'un datacenter classique.
> **Pourquoi c'est important** : Le choix du système de refroidissement est le premier levier d'amélioration du PUE. Un mauvais refroidissement peut augmenter de 100 % la facture énergétique d'un datacenter. La DSI doit comprendre ces enjeux pour qualifier les offres d'hébergement et piloter ses propres salles serveurs.
> **Chiffres clés** :
> - Le refroidissement représente **30 à 40 %** de la consommation d'un datacenter traditionnel (PUE ~ 2,0)
> - Le free cooling peut réduire la consommation de refroidissement de **50 à 90 %** selon le climat
> - Les datacenters consomment environ **1 à 2 % de l'électricité mondiale** (AIE, 2022)

## Approfondir

### Fonctionnement

#### Hot aisle / Cold aisle (gestion des allées chaudes/froides)
Organisation physique des baies serveurs alternant allées froides (soufflage d'air froid) et allées chaudes (extraction d'air chaud) :
- Les serveurs aspirent l'air froid en façade (allée froide) et rejettent l'air chaud en arrière (allée chaude)
- Des panneaux de confinement isolent les deux flux, évitant la remixion (qui forcerait le refroidissement à travailler deux fois)
- Gain typique : **15 à 30 %** de réduction de la consommation de refroidissement vs une salle non organisée
- Extension : confinement total des allées (cages d'allée chaude ou froide) pour gains supplémentaires

#### Free Cooling (refroidissement par l'air extérieur)
Principe : utiliser directement l'air extérieur froid pour refroidir les équipements, sans (ou avec peu de) recours à la climatisation mécanique (groupe froid).

- **Free cooling direct** : l'air extérieur filtré entre directement dans la salle
- **Free cooling indirect** : l'air extérieur refroidit l'eau d'un circuit fermé via un échangeur, sans contact direct avec l'air de la salle
- Opérationnel quand la température extérieure est < **18–22 °C** (selon les équipements)
- En France : exploitable **70 à 80 %** de l'année selon la région
- En Scandinavie ou Islande : exploitable **95 %+** de l'année → PUE proches de 1,1

#### Refroidissement adiabatique
Technique utilisant l'évaporation d'eau pour refroidir l'air avant de l'envoyer dans le datacenter. Consomme peu d'électricité mais consomme de l'eau.
- Efficace par temps chaud et sec
- Permet d'étendre la plage d'utilisation du free cooling
- À surveiller : impact sur le WUE (Water Usage Effectiveness)

#### Watercooling (refroidissement liquide sur les baies)
Circulation d'eau froide dans des échangeurs thermiques proches ou dans les baies serveurs :
- **Refroidissement en bout de rangée (row cooling)** : unités de climatisation placées entre les rangées de baies, eau glacée en circuit fermé
- **Refroidissement en arrière de baie (rear-door heat exchanger)** : porte arrière de baie avec serpentin eau froide, capture la chaleur avant qu'elle ne se diffuse dans la salle
- Permet de traiter des densités > **20 kW/baie** (impossibles en air)

#### Liquid Cooling direct (Direct Liquid Cooling / DLC)
Circulation de liquide caloporteur directement au contact des composants (processeurs, GPU) :
- **Cold plates** : plaques métalliques traversées par de l'eau, posées sur les CPU/GPU
- Très efficace pour les serveurs HPC et IA (densités > 50 kW/rack)
- Adopté par les supercalculateurs (NVIDIA DGX, Intel Gaudi)

#### Immersion Cooling (refroidissement par immersion)
Les serveurs sont plongés entièrement dans un liquide diélectrique non conducteur :
- **Immersion à un seul bain (single-phase)** : le liquide reste liquide, refroidi par un échangeur externe. Ex. : huile minérale ou liquide 3M Novec
- **Immersion à changement de phase (two-phase)** : le liquide s'évapore au contact des composants chauds, se condense en partie haute et retombe (cycle naturel). Ex. : 3M Novec 7100
- PUE potentiel : **1,02 à 1,05**
- Élimine les ventilateurs des serveurs, réduisant bruit et consommation
- Adopté par des opérateurs de Bitcoin mining et certains HPC (Iceotope, LiquidStack)

#### Récupération de chaleur fatale
La chaleur produite par les serveurs est une énergie qui peut être valorisée plutôt que gaspillée :
- **Chauffage de bâtiments** : la chaleur à 45–60 °C peut alimenter un réseau de chaleur urbain
- **Serres agricoles** : chauffage de serres maraîchères (projet Intradata/Agrilys)
- **Piscines municipales** : chauffage de l'eau (projet de datacenter à Paris)
- Condition : la chaleur doit être à une température suffisante (> 35–40 °C)
- Freins : complexité administrative, distance avec les utilisateurs de chaleur

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Free cooling : très faible consommation électrique | Free cooling direct : filtration air, risque de pollution (poussière, humidité) |
| Immersion cooling : PUE quasi idéal, très haute densité | Immersion cooling : coût élevé, maintenance complexe, liquide spécifique |
| Récupération chaleur fatale : valorisation énergétique | Récupération chaleur : investissement infrastructure, dépendance d'un tiers |
| Hot/cold aisle : ROI rapide, facile à mettre en œuvre | Confinement des allées : travaux, réorganisation physique |
| DLC : traite les très hautes densités (IA, HPC) | DLC : remplacement du matériel existant souvent nécessaire |

### Acteurs et solutions du marché
- **Schneider Electric** : solutions de confinement d'allées, InRow cooling, refroidissement liquide
- **Vertiv** : systèmes de refroidissement précis, liebert Deluxe System
- **Rittal** : armoires avec cooling intégré, liquid cooling packages
- **Iceotope / LiquidStack** : immersion cooling (single et two-phase)
- **3M** : liquides Novec pour immersion two-phase
- **EkkoSense** : logiciel d'optimisation thermique par IA
- **Aligned Energy** : opérateur datacenter spécialisé en refroidissement à haute efficacité

### Cas d'usage concrets
1. **Microsoft Project Natick** : datacenter sous-marin testé au large des côtes d'Écosse (2018–2020), refroidi par l'eau de mer. Résultats : taux de panne 8x inférieur aux datacenters terrestres, PUE excellent.
2. **OVHcloud Roubaix** : utilise le watercooling (refroidissement par eau en circuit fermé) sur l'ensemble de ses serveurs depuis ses origines, atteignant des PUE entre 1,09 et 1,4 selon les sites.
3. **Stockolm Data Parks** (Suède) : plusieurs datacenters récupèrent leur chaleur fatale pour alimenter le réseau de chaleur urbain de Stockholm, chauffant des milliers de logements.

### Chiffres et tendances
- Le free cooling est opérationnel en France **environ 6 000 heures/an** (68 % du temps)
- L'immersion cooling peut réduire la consommation de refroidissement de **95 %** vs climatisation traditionnelle
- La densité moyenne des baies progresse : de **5–7 kW** en 2015 à **15–20 kW** en 2023, rendant le refroidissement liquide incontournable pour l'IA
- Le marché du liquid cooling datacenter croît de **+25 % par an** (Allied Market Research, 2023)

## Flashcards
#flashcards/SI_et_environnement/Refroidissement_des_datacenters

Qu'est-ce que le free cooling et dans quelles conditions fonctionne-t-il ? :: Utilisation de l'air extérieur froid (< 18–22 °C) pour refroidir les équipements, sans ou avec peu de groupe froid. Opérationnel 70–80 % de l'année en France, 95 %+ en Scandinavie.

Quelle est la différence entre hot aisle et cold aisle ? :: Organisation alternée des baies : l'allée froide est soufflée d'air froid (face avant des serveurs), l'allée chaude évacue l'air chaud (face arrière). Le confinement empêche le remixion des deux flux.

Qu'est-ce que l'immersion cooling two-phase ? :: Les serveurs sont immergés dans un liquide diélectrique qui s'évapore au contact des composants chauds, se condense en partie haute et retombe naturellement, sans pompe. PUE possible : 1,02–1,05.

Pourquoi la récupération de chaleur fatale est-elle un enjeu Green IT important ? :: Elle valorise la chaleur inévitablement produite par les serveurs (40–60 °C) pour alimenter des réseaux de chaleur, des serres ou des bâtiments, transformant un déchet thermique en ressource.

Quel système de refroidissement est le plus adapté aux serveurs IA/HPC à très haute densité ? :: Le Direct Liquid Cooling (DLC) avec cold plates sur CPU/GPU, ou l'immersion cooling, capables de traiter > 50 kW/rack, impossible en refroidissement par air.

Qu'est-ce que le refroidissement adiabatique ? :: Technique utilisant l'évaporation d'eau pour pré-refroidir l'air. Peu énergivore électriquement mais consomme de l'eau (impact WUE). Étend la plage d'utilisation du free cooling.

Quel indicateur mesure l'efficacité du refroidissement d'un datacenter ? :: Le PUE (Power Usage Effectiveness) = Énergie totale / Énergie IT. Le refroidissement vise à le réduire au maximum (idéal : 1,0 ; classique : 1,5 à 2,0).

## Sources
- Uptime Institute – "Global Data Center Survey 2023" : https://uptimeinstitute.com
- AIE (Agence Internationale de l'Énergie) – "Data Centres and Data Transmission Networks" : https://www.iea.org
- Schneider Electric – White papers sur l'efficacité des datacenters : https://www.se.com/ww/en/work/campaign/life-is-on/white-papers.jsp
- The Green Grid – PUE et métriques datacenter : https://www.thegreengrid.org
- Microsoft Research – Projet Natick : https://natick.research.microsoft.com
- OVHcloud – Rapport environnemental annuel : https://corporate.ovhcloud.com

## Notions liées
- [[Indicateurs environnementaux du SI]]
- [[Infrastructure des datacenters]]
- [[Projets innovants de datacenters]]
- [[Analyse du Cycle de Vie (ACV)]]
