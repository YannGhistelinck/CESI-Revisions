---
type: notion
thèmes:
  - SI et environnement
  - Management et stratégie
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Indicateurs environnementaux du SI

## En bref
> **Définition** : Les indicateurs environnementaux du SI sont des métriques standardisées qui permettent de mesurer et de piloter l'impact écologique d'une infrastructure informatique, notamment des datacenters. Ils couvrent la consommation d'énergie, d'eau, et les émissions de gaz à effet de serre.
> **Pourquoi c'est important** : Pour une DSI, ces indicateurs sont indispensables pour identifier les gisements d'optimisation, répondre aux obligations réglementaires (loi REEN, Décret Tertiaire) et construire une démarche Green IT crédible et mesurable.
> **Chiffres clés** :
> - Le numérique représente environ **4 % des émissions mondiales de GES** (The Shift Project, 2023)
> - Un datacenter avec un PUE de 2,0 gaspille autant d'énergie qu'il en consomme utilement ; l'objectif est un PUE < 1,5
> - Les hyperscalers (Google, Microsoft, AWS) affichent des PUE moyens entre **1,1 et 1,2**

## Approfondir

### Fonctionnement

#### PUE – Power Usage Effectiveness
Le PUE est le ratio entre l'énergie totale consommée par un datacenter et l'énergie effectivement consommée par les équipements IT.

**PUE = Énergie totale du datacenter / Énergie consommée par les équipements IT**

- PUE = 1,0 : perfection théorique (toute l'énergie va aux équipements IT)
- PUE = 2,0 : 50 % de l'énergie est perdue en refroidissement, alimentation, etc.
- Norme de référence : **ISO/IEC 30134-2**

#### CUE – Carbon Usage Effectiveness
Le CUE mesure les émissions de CO₂ liées au fonctionnement du datacenter, rapportées à la puissance IT.

**CUE = Émissions CO₂ totales (kgCO₂) / Énergie consommée par les équipements IT (kWh)**

Un CUE de 0 signifie une alimentation 100 % renouvelable.

#### WUE – Water Usage Effectiveness
Le WUE mesure la quantité d'eau utilisée pour le refroidissement, rapportée à l'énergie IT.

**WUE = Consommation d'eau annuelle (litres) / Énergie consommée par les équipements IT (kWh)**

Particulièrement critique dans les zones de stress hydrique.

#### ERE – Energy Reuse Effectiveness
L'ERE mesure la part de chaleur fatale récupérée et réutilisée (chauffage urbain, serres, etc.).

**ERE = (Énergie totale − Énergie réutilisée) / Énergie équipements IT**

Un ERE < 1 indique une récupération de chaleur effective. Norme : **ISO/IEC 30134-3**.

#### Bilan GES et GHG Protocol
Le GHG Protocol (Greenhouse Gas Protocol) est le standard mondial de comptabilisation des émissions de GES. Il distingue trois périmètres :

| Scope | Définition | Exemples numériques |
|-------|------------|---------------------|
| **Scope 1** | Émissions directes (combustion sur site) | Groupes électrogènes fioul, chauffage gaz du datacenter |
| **Scope 2** | Émissions indirectes liées à l'énergie achetée | Électricité du réseau (dépend du mix énergétique national) |
| **Scope 3** | Toutes les autres émissions indirectes | Fabrication des serveurs, transport, déchets, télétravail des employés |

Le Scope 3 représente souvent **70 à 80 %** du bilan carbone numérique d'une organisation. Il est le plus difficile à mesurer mais le plus important.

#### Bilan carbone numérique
Méthodologie développée par l'ADEME et GreenIT.fr pour évaluer l'empreinte carbone d'un parc informatique en intégrant :
- La fabrication des équipements (phase dominante)
- L'utilisation (consommation électrique)
- La fin de vie (recyclage, DEEE)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Mesure objective et comparable dans le temps | PUE ne reflète pas l'efficacité réelle des applications |
| Outils de pilotage pour réduire les coûts | Scope 3 très difficile à mesurer précisément |
| Base pour le reporting ESG et la conformité | Risque de greenwashing si indicateurs mal définis |
| Facilitent la négociation avec les fournisseurs cloud | Nécessitent des outils de métrologie coûteux |
| Reconnus internationalement (ISO/IEC) | Les méthodes varient entre acteurs, comparaison difficile |

### Acteurs et solutions du marché
- **ADEME** : Référentiel Bilan Carbone, guide numérique responsable
- **GreenIT.fr** : Outils d'évaluation de l'empreinte numérique des organisations
- **The Green Grid** : Consortium qui a défini le PUE, le WUE, le CUE
- **ISO/IEC 30134** : Série de normes pour les métriques datacenter
- **Carbon Disclosure Project (CDP)** : Reporting carbone pour les entreprises
- **GHG Protocol** : Standard de comptabilisation des GES (World Resources Institute + WBCSD)
- Outils SaaS : **Salesforce Net Zero Cloud**, **Microsoft Sustainability Manager**, **Sweep**

### Cas d'usage concrets
1. **OVHcloud** publie annuellement son bilan carbone selon le GHG Protocol (Scopes 1, 2 et 3) et affiche ses PUE par datacenter sur son site public.
2. **La Poste** a utilisé la méthodologie Bilan Carbone de l'ADEME pour identifier que le poste "équipements informatiques des agents" était son premier poste d'émission numérique, déclenchant un plan de renouvellement allongé.
3. **Google** compense son Scope 2 à 100 % via des PPA (Power Purchase Agreements) d'énergie renouvelable depuis 2017 et vise l'absence de carbone 24/7 d'ici 2030.

### Chiffres et tendances
- PUE mondial moyen (Uptime Institute, 2023) : **1,58**
- PUE des hyperscalers : **1,10 – 1,20**
- Le numérique pèse **2,5 % des émissions GES françaises** (ARCEP/ADEME, 2023)
- La fabrication représente **78 %** de l'empreinte carbone d'un smartphone
- Croissance annuelle du trafic de données : **+25 % par an** (Cisco)
- La loi REEN (2021) impose aux datacenters > 500 kW de publier leur PUE et WUE

## Flashcards
#flashcards

Qu'est-ce que le PUE et comment se calcule-t-il ? :: PUE = Énergie totale datacenter / Énergie équipements IT. Un PUE de 1,0 est idéal, 2,0 signifie 50 % de pertes. Norme ISO/IEC 30134-2.

Quels sont les 3 Scopes du GHG Protocol ? :: Scope 1 = émissions directes (combustion sur site). Scope 2 = énergie achetée (électricité). Scope 3 = toutes les autres émissions indirectes (fabrication, transport, fin de vie).

Quel Scope représente la plus grande part du bilan carbone numérique ? :: Le Scope 3, qui représente souvent 70 à 80 % du total, notamment via la fabrication des équipements.

Que mesure le WUE ? :: Water Usage Effectiveness : litres d'eau consommés pour le refroidissement par kWh d'énergie IT. Critique dans les zones de stress hydrique.

Que mesure le CUE ? :: Carbon Usage Effectiveness : kg de CO₂ émis par kWh consommé par les équipements IT. Un CUE de 0 indique une alimentation 100 % renouvelable.

Quelle est la différence entre ERE et PUE ? :: Le PUE mesure l'efficacité énergétique globale. L'ERE (Energy Reuse Effectiveness) prend en compte la chaleur fatale récupérée et réutilisée : un ERE < 1 signifie qu'on réutilise de la chaleur.

Quelle loi française impose la publication du PUE aux grands datacenters ? :: La loi REEN (Réduire l'Empreinte Environnementale du Numérique), adoptée en 2021, impose aux datacenters > 500 kW de publier PUE, WUE et taux d'énergie renouvelable.

## Sources
- ADEME – Guide "Numérique et environnement" : https://www.ademe.fr
- The Green Grid – Définition des métriques PUE/WUE/CUE : https://www.thegreengrid.org
- GHG Protocol : https://ghgprotocol.org
- The Shift Project – Rapport "Lean ICT" 2023 : https://theshiftproject.org
- ARCEP/ADEME – Rapport "Empreinte environnementale du numérique en France" 2023 : https://www.arcep.fr
- Uptime Institute – Global Data Center Survey 2023 : https://uptimeinstitute.com
- Loi REEN (n°2021-1485) : https://www.legifrance.gouv.fr

## Notions liées
- [[Analyse du Cycle de Vie (ACV)]]
- [[Refroidissement des datacenters]]
- [[Infrastructure des datacenters]]
- [[Technologies de stockage]]
