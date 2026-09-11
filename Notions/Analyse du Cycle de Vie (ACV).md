---
type: notion
thèmes:
  - SI et environnement
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Analyse du Cycle de Vie (ACV)

## En bref
> **Définition** : L'Analyse du Cycle de Vie (ACV) est une méthode normalisée (ISO 14040/14044) qui évalue l'ensemble des impacts environnementaux d'un produit ou service depuis l'extraction des matières premières jusqu'à sa fin de vie ("du berceau à la tombe"). Appliquée au numérique, elle permet de quantifier l'empreinte réelle d'un équipement ou d'un service cloud.
> **Pourquoi c'est important** : La DSI ne peut pas piloter ce qu'elle ne mesure pas. L'ACV révèle que la fabrication des équipements (phase souvent ignorée) domine le bilan environnemental du numérique, ce qui remet en cause les stratégies de renouvellement rapide du parc matériel.
> **Chiffres clés** :
> - La fabrication représente **78 % de l'empreinte carbone** d'un smartphone (ADEME, 2022)
> - **72 % de l'empreinte carbone** d'un ordinateur portable provient de sa fabrication
> - Le cloud computing représente environ **3,9 % des émissions mondiales de GES** en 2020 (The Shift Project)

## Approfondir

### Fonctionnement

#### Les 4 phases d'une ACV
1. **Définition des objectifs et du périmètre** : Que mesure-t-on ? Quelle unité fonctionnelle ? (ex. : "héberger 1 To de données pendant 1 an")
2. **Inventaire du cycle de vie (ICV)** : Collecte de toutes les données d'entrées et sorties (matériaux, énergie, émissions) sur l'ensemble du cycle
3. **Évaluation des impacts** : Traduction des données en indicateurs (réchauffement climatique, épuisement des ressources, consommation d'eau…)
4. **Interprétation** : Identification des points chauds et recommandations

#### Les 4 phases du cycle de vie d'un équipement numérique
| Phase | Description | Part typique de l'impact |
|-------|-------------|--------------------------|
| **Fabrication** | Extraction minière, transformation, assemblage | 50 – 80 % selon l'équipement |
| **Transport** | Logistique mondiale | 2 – 5 % |
| **Usage** | Consommation électrique pendant la durée de vie | 15 – 45 % |
| **Fin de vie** | Recyclage, DEEE, mise en décharge | 1 – 5 % |

#### TCO Environnemental
Le Total Cost of Ownership environnemental étend le TCO financier classique aux coûts externes :
- Coût carbone de la fabrication (amortissement sur la durée d'usage)
- Coût carbone de l'électricité consommée (dépend du mix énergétique)
- Coût de la fin de vie (filières de recyclage DEEE)

L'allongement de la durée de vie d'un équipement est le levier le plus efficace : amortir le coût carbone de fabrication sur 5 ans au lieu de 3 ans réduit l'empreinte de 40 %.

#### Empreinte carbone numérique
Démarche opérationnelle dérivée de l'ACV, popularisée par GreenIT.fr, qui permet à une organisation d'évaluer rapidement l'impact de son parc SI :
- Inventaire des équipements (utilisateurs, serveurs, réseau, salles blanches)
- Application de facteurs d'émission (base de données Ecoinvent, Base Empreinte ADEME)
- Résultat en tonnes de CO₂ équivalent, ventilé par phase et par équipement

#### Cloud Carbon Footprint
Outil open source (initié par ThoughtWorks) permettant de mesurer les émissions de CO₂ des services cloud AWS, GCP et Azure. Il calcule :
- La consommation électrique estimée des ressources utilisées (instances, stockage, réseau)
- L'intensité carbone du mix électrique de la région hébergeant les ressources
- Un score en kgCO₂e par ressource et par période

Limites : les hyperscalers ne publient pas toutes les données nécessaires, l'outil repose donc sur des estimations.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Vision complète, évite les transferts de pollution | Coûteuse et longue à réaliser rigoureusement |
| Normalisée ISO 14040/14044, reconnue internationalement | Données fournisseurs souvent indisponibles ou opaques |
| Identifie les vrais points chauds (souvent la fabrication) | Résultats sensibles aux hypothèses de périmètre |
| Base solide pour l'écoconception | Expertise spécialisée requise |
| Cloud Carbon Footprint permet une estimation rapide | Le cloud cache la complexité réelle de l'infrastructure |

### Acteurs et solutions du marché
- **ADEME** : Base Empreinte (facteurs d'émission), méthodologie Bilan Carbone
- **GreenIT.fr** : Numériques Responsables, outil d'évaluation de l'empreinte numérique
- **Cloud Carbon Footprint** (open source) : https://www.cloudcarbonfootprint.org
- **Ecoinvent** : Base de données ACV de référence mondiale
- **Boavizta** : Consortium français développant des outils open source d'empreinte numérique (PowerAPI, BoaviztAPI)
- **Resilio** (ex-GreenSI) : Conseil et outillage en numérique responsable
- AWS, GCP, Azure : Tous proposent désormais des tableaux de bord carbone natifs (AWS Customer Carbon Footprint Tool, Google Cloud Carbon Footprint, Microsoft Emissions Impact Dashboard)

### Cas d'usage concrets
1. **Renault** a réalisé une ACV de ses postes de travail et a décidé d'allonger la durée de vie de ses PC de 4 à 5 ans, économisant plusieurs milliers de tonnes de CO₂ par an.
2. **L'État français** via la DINUM impose depuis 2023 aux administrations une déclaration des équipements dans le cadre du référentiel général d'écoconception (RGESN).
3. **Capgemini** utilise Cloud Carbon Footprint pour calculer et compenser l'empreinte de ses projets cloud client, avec un dashboard intégré dans ses offres de conseil.

### Chiffres et tendances
- Durée de vie moyenne d'un smartphone en France : **2,3 ans** (ADEME), l'allonger à 4 ans divise l'empreinte par presque 2
- 1 To de données stockées dans un datacenter cloud = environ **0,16 kgCO₂e/mois** (estimation moyenne, très variable selon le mix électrique)
- **34 millions** de tonnes de déchets électroniques produits en Europe chaque année (Eurostat)
- Le marché des services cloud devrait atteindre **1 000 Md$ en 2027** (Gartner), amplifiant l'enjeu carbone

## Flashcards
#flashcards

Quelles sont les 4 phases d'une ACV ? :: 1. Définition des objectifs/périmètre. 2. Inventaire du cycle de vie (ICV). 3. Évaluation des impacts. 4. Interprétation. Normalisée ISO 14040/14044.

Quelle phase du cycle de vie d'un équipement numérique est la plus impactante ? :: La fabrication, qui représente 50 à 80 % de l'impact selon l'équipement (ex. 78 % pour un smartphone, 72 % pour un laptop).

Qu'est-ce que le TCO environnemental ? :: Extension du TCO financier intégrant le coût carbone de la fabrication, de l'électricité consommée et de la fin de vie (DEEE).

Quel est le principal levier pour réduire l'empreinte numérique d'un parc ? :: Allonger la durée de vie des équipements, pour amortir l'impact carbone de fabrication sur plus d'années.

Qu'est-ce que Cloud Carbon Footprint ? :: Outil open source (ThoughtWorks) qui estime les émissions CO₂ des ressources cloud AWS, GCP et Azure en combinant consommation électrique estimée et intensité carbone de la région.

Quelle est la limite principale de Cloud Carbon Footprint ? :: Les hyperscalers ne publient pas toutes les données nécessaires, les calculs reposent donc sur des estimations et des modèles approximatifs.

Quelle norme internationale encadre l'ACV ? :: ISO 14040 (principes et cadre) et ISO 14044 (exigences et lignes directrices).

## Sources
- ADEME – Base Empreinte et méthodologie Bilan Carbone : https://www.ademe.fr
- Cloud Carbon Footprint (open source) : https://www.cloudcarbonfootprint.org
- Boavizta – outils open source d'empreinte numérique : https://boavizta.org
- GreenIT.fr – Empreinte numérique des organisations : https://www.greenit.fr
- The Shift Project – "Lean ICT : pour une sobriété numérique" : https://theshiftproject.org
- Norme ISO 14040:2006 et ISO 14044:2006

## Notions liées
- [[Indicateurs environnementaux du SI]]
- [[Infrastructure des datacenters]]
- [[Data Lifecycle Management]]
- [[VDI et client léger]]
