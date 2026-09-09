---
type: notion
thèmes:
  - SI et environnement
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Sobriété numérique

## En bref
> **Définition** : La sobriété numérique consiste à réduire volontairement l'empreinte environnementale du numérique en limitant les usages superflus et en optimisant les ressources matérielles et logicielles. Elle se distingue de l'efficacité énergétique en questionnant l'utilité même des usages, pas seulement leur performance.
> **Pourquoi c'est important** : Le numérique représente 2,5 % des émissions de GES en France (ADEME/Arcep 2023) avec une trajectoire de croissance forte. Les DSI sont en première ligne pour réduire l'empreinte de leurs infrastructures et accompagner les métiers vers des pratiques plus responsables.
> **Chiffres clés** :
> - Le numérique émet autant de GES que l'aviation civile mondiale (environ 4 % des émissions mondiales selon le Shift Project, 2021)
> - 79 % de l'empreinte carbone du numérique français est due aux terminaux (fabrication incluse) — ADEME/Arcep 2023
> - Sans action, l'empreinte du numérique pourrait tripler d'ici 2050 en France (ADEME/Arcep 2023)

## Approfondir

### Fonctionnement

**Green IT 1.0 — Réduire l'impact du numérique sur l'environnement**
Optimisation des équipements et datacenters : PUE, refroidissement, efficacité des serveurs. L'approche est technique et porte sur l'infrastructure existante.

**Green IT 2.0 / Numérique Responsable (NR)**
Extension à l'ensemble du cycle de vie des équipements et des usages : allongement de la durée de vie des terminaux, écoconception des services, achats responsables, sensibilisation des utilisateurs.

**IT for Green**
Utilisation du numérique comme levier de décarbonation des autres secteurs : smart grids, agriculture de précision, optimisation logistique, jumeaux numériques pour la rénovation énergétique. Attention : l'effet net reste débattu.

**Effet rebond et paradoxe de Jevons**
L'amélioration de l'efficacité d'une technologie entraîne une augmentation de son utilisation, annulant partiellement ou totalement le gain environnemental. Exemple : des smartphones plus efficaces énergétiquement mais achetés en plus grand nombre et changés plus souvent.

**GreenOps**
Pratique issue du croisement DevOps / FinOps / Green IT : mesurer et réduire l'empreinte carbone des workloads cloud en temps réel. Inclut le choix de régions cloud à mix énergétique favorable, la planification des traitements batch sur des plages à énergie renouvelable (carbon-aware computing).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction des coûts énergétiques et d'infrastructure | Résistance culturelle au changement d'usages |
| Allongement de la durée de vie des équipements = moins d'extraction minière | Difficile à mesurer précisément (absence de standard unique) |
| Image et attractivité de l'entreprise (RSE) | Risque de greenwashing si non structuré |
| Conformité réglementaire anticipée (CSRD, REEN) | L'effet rebond peut annuler les gains |
| Réduction de la dépendance aux ressources rares | Nécessite une gouvernance transversale (DSI + métiers + achats) |

### Acteurs et solutions du marché
- **The Shift Project** : think tank de référence, rapports Lean ICT et Pour une sobriété numérique
- **ADEME / Arcep** : publications annuelles sur l'empreinte du numérique en France
- **INR (Institut du Numérique Responsable)** : label NR, référentiels, formation
- **Boavizta** : communauté open source, outils de mesure (Cloud-scanner, Boagent)
- **Outils GreenOps** : Cloud Carbon Footprint (open source), Climatiq API, outils natifs AWS/Azure/GCP (Customer Carbon Footprint Tool)

### Cas d'usage concrets
1. **SNCF** : démarche NR structurée avec un référent NR par direction, bilan numérique annuel, politique d'allongement des terminaux à 5 ans.
2. **Sopra Steria** : engagement net zéro, mesure de l'empreinte Scope 3, intégration de critères NR dans les appels d'offres.
3. **Carbon-aware computing (Microsoft)** : planification des tâches Azure en fonction de l'intensité carbone du réseau électrique (API Carbon Aware SDK, open source).

### Chiffres et tendances
- Fabrication des équipements = 78 % de l'empreinte carbone du numérique français (ADEME/Arcep 2023)
- La consommation électrique des datacenters mondiaux stagne (~200-250 TWh/an) grâce aux gains d'efficacité, mais les usages (IA, streaming) explosent — effet rebond massif
- L'IA générative multiplie par 10 à 100 la consommation énergétique par requête vs une recherche Google classique (estimation IEA 2024)
- Seules 14 % des entreprises françaises mesurent l'empreinte de leur SI (Cigref/Wavestone 2023)

## Flashcards
#flashcards/SI_et_environnement/Sobriété_numérique #flashcards/Management_et_stratégie/Sobriété_numérique

Quelle est la différence entre Green IT 1.0 et Green IT 2.0 ? :: Green IT 1.0 = optimiser l'infrastructure numérique (datacenter, serveurs, PUE). Green IT 2.0 / NR = étendre à tout le cycle de vie (terminaux, usages, achats, écoconception logicielle).

Qu'est-ce que l'effet rebond (paradoxe de Jevons) dans le numérique ? :: Un gain d'efficacité technologique entraîne une augmentation des usages qui compense ou dépasse le gain initial. Ex : smartphones plus efficaces mais achetés en masse et renouvelés plus fréquemment.

Quel est le principal poste d'empreinte carbone du numérique français ? :: La fabrication des terminaux utilisateurs (smartphones, ordinateurs, écrans), qui représente ~79 % de l'empreinte carbone totale (ADEME/Arcep 2023).

Qu'est-ce que le GreenOps ? :: Pratique consistant à mesurer et réduire l'empreinte carbone des workloads cloud en temps réel, en combinant approches DevOps, FinOps et Green IT (choix de régions, planification carbon-aware).

Qu'est-ce que l'"IT for Green" ? :: Utilisation du numérique comme levier de décarbonation des autres secteurs (smart grids, agriculture de précision, optimisation logistique). À distinguer du Green IT qui vise à réduire l'impact du numérique lui-même.

Quelle est l'empreinte GES du numérique mondial ? :: Environ 4 % des émissions mondiales de GES (Shift Project, 2021), comparable à l'aviation civile mondiale.

## Sources
- ADEME / Arcep — "Évaluation de l'empreinte environnementale du numérique en France" (2023) : https://www.arcep.fr/uploads/tx_gspublication/etude-numerique-environnement-ademe-arcep-volet03_janv2023.pdf
- The Shift Project — "Lean ICT : Pour une sobriété numérique" (2018) : https://theshiftproject.org/article/pour-une-sobriete-numerique-rapport-shift/
- The Shift Project — "Impact environnemental du numérique : tendances à 5 ans et gouvernance de la 5G" (2021)
- IEA — "Electricity 2024" (données sur consommation IA et datacenters)
- Boavizta (outils open source de mesure) : https://boavizta.org
- Cloud Carbon Footprint (outil open source GreenOps) : https://www.cloudcarbonfootprint.org

## Notions liées
- [[Fiche 10 : Écoconception logicielle]]
- [[Fiche 11 : Économie circulaire du numérique]]
- [[Fiche 12 : Outils de mesure d'impact environnemental]]
- [[Fiche 13 : Cadre réglementaire environnemental du SI]]
- [[Fiche 15 : FinOps]]
- [[Fiche 16 : Acteurs du numérique responsable]]
