---
type: notion
thèmes:
  - SI et environnement
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Projets innovants de datacenters

## En bref
> **Définition** : Face aux contraintes énergétiques et environnementales, des projets innovants réinventent le concept de datacenter : placement sous-marin pour profiter du refroidissement naturel, valorisation de la chaleur fatale comme source de chauffage domestique ("chaudière numérique"), ou encore couplage entre minage de cryptomonnaies et besoins de chaleur.
> **Pourquoi c'est important** : Ces innovations illustrent des approches systémiques qui dépassent la simple optimisation interne : elles cherchent à intégrer le datacenter dans son écosystème (réseau de chaleur, bâtiment, milieu marin), transformant un déchet (chaleur) ou une contrainte (refroidissement) en ressource. La DSI doit connaître ces tendances pour les anticiper dans ses choix d'hébergement.
> **Chiffres clés** :
> - **8x moins de pannes** que les datacenters terrestres : résultat du Projet Natick de Microsoft
> - La chaudière numérique Qarnot génère **3 kWh de chaleur** pour 1 kWh d'électricité consommé, avec les calculs fournis en plus
> - Le green mining utilise des **énergies renouvelables excédentaires** (hydraulique, éolien) pour le minage, réduisant l'empreinte carbone de la preuve de travail

## Approfondir

### Fonctionnement

#### Projet Natick – Datacenter sous-marin (Microsoft)
Initiative de recherche de Microsoft consistant à déployer un module de datacenter hermétique au fond de la mer.

**Phase 1 (2015)** : test de faisabilité en Californie (12 serveurs, 105 jours)
**Phase 2 (2018–2020)** : déploiement réel à 35 m de profondeur au large des Orcades (Écosse, mer du Nord)
- **864 serveurs** dans un cylindre de 12 m de long, 3 m de diamètre
- Refroidi par l'eau de mer en circuit fermé
- Alimenté par des câbles depuis l'infrastructure d'énergie marine des Orcades (renouvelable)
- Atmosphère intérieure : **azote** (pour éviter l'oxydation et l'humidité)
- Connexion : câble sous-marin à haute capacité

**Résultats publiés en 2020** :
- Taux de panne des serveurs **8x inférieur** au datacenter terrestre de référence
- Hypothèse : atmosphère stable (azote, pas d'oxydation, pas de chocs thermiques liés aux interventions humaines)
- PUE excellent grâce au refroidissement naturel par l'eau de mer
- Le projet n'a pas été industrialisé (contraintes de maintenance, coûts d'installation)

**Intérêts Green IT** :
- Refroidissement gratuit et naturel
- Proximité des câbles sous-marins intercontinentaux (latence réduite pour les usages côtiers)
- Potentiel d'alimentation par énergie marine (houle, marée, éolien offshore)

#### Qarnot Computing – La chaudière numérique
Entreprise française (fondée en 2010) qui détourne le principe du datacenter centralisé : les processeurs de calcul sont distribués dans des radiateurs et des boilers installés chez des particuliers et dans des bureaux.

**Fonctionnement** :
1. Qarnot installe ses "chaudières numériques" (Q.rad) ou boilers numériques (Q.boiler) chez ses clients (promoteurs immobiliers, bailleurs sociaux)
2. Les Q.rad et Q.boiler contiennent des processeurs ou GPU qui effectuent des calculs pour des clients professionnels (ingénierie, finance, rendu 3D, calcul scientifique)
3. La chaleur produite par les calculs chauffe le logement ou l'eau chaude sanitaire
4. Le client chauffagiste ne paie pas l'électricité (prise en charge par Qarnot)
5. Le client calcul (ex. studio d'animation, banque) paie Qarnot pour ses calculs

**Bilan énergétique** :
- Rendement thermique : quasi 100 % (toute l'électricité devient chaleur)
- Comparé à une résistance électrique classique : même consommation, mais les calculs sont fournis en bonus
- Comparé à un datacenter classique : la chaleur fatale est valorisée localement, sans transport via réseau de chaleur

**Clients calcul** : Société Générale (calcul de risques), EDF, studios d'animation, chercheurs universitaires.

**Déploiement** : Des centaines de Q.rad installés dans des logements sociaux (Paris, Bordeaux, Lyon), des bureaux, des crèches.

#### Green Mining – Minage de cryptomonnaies et énergies renouvelables
Le minage de Bitcoin (Proof of Work) est extrêmement énergivore : le réseau Bitcoin consomme autant que certains pays. La tendance du "green mining" cherche à utiliser des énergies renouvelables excédentaires ou fatales.

**Cas d'usage green mining** :
- **Hydraulique excédentaire** : dans les régions où les barrages produisent plus d'électricité que le réseau n'en absorbe (Québec, Sichuan, Scandinavie), les mineurs absorbent l'excédent à coût quasi nul
- **Éolien/solaire intermittent** : les fermes de minage s'allument quand la production renouvelable dépasse la demande, évitant le curtailment (gaspillage d'énergie renouvelable)
- **Géothermie** : fermes de minage en Islande alimentées à 100 % par la géothermie locale
- **Récupération de chaleur** : certains mineurs revendent leur chaleur fatale à des serres ou des réseaux de chaleur

**Lien avec la chaudière numérique** :
Certaines startups (ex. Hestiia, MintGreen au Canada) commercialisent des radiateurs minant du Bitcoin, reprenant le concept Qarnot appliqué au minage.

**Controverses** :
- La consommation du réseau Bitcoin reste très élevée, même avec des énergies renouvelables
- Le green mining peut détourner des ressources renouvelables d'autres usages
- Ethereum a migré vers Proof of Stake (2022), réduisant sa consommation de **99,95 %**

### Avantages / Inconvénients

| Concept | Avantages | Inconvénients |
|---------|-----------|---------------|
| **Datacenter sous-marin** | Refroidissement gratuit, moins de pannes, énergie marine | Maintenance complexe/coûteuse, contraintes logistiques, impact marin à évaluer |
| **Chaudière numérique** | 100 % de la chaleur valorisée, chauffage gratuit, calcul distribué | Infrastructure distribuée difficile à sécuriser, débit limité, latence réseau |
| **Green mining** | Absorption des surplus renouvelables, revenu pour les producteurs | Légitimité débattue, consommation absolue élevée, volatilité du marché crypto |

### Acteurs et solutions du marché
- **Microsoft Research** : Projet Natick (R&D, non commercialisé)
- **Qarnot Computing** : chaudière numérique commercialisée en France
- **Hestiia** : radiateur Bitcoin grand public (fondée par d'anciens de Qarnot)
- **MintGreen** (Canada) : valorisation de chaleur de minage pour réseaux de chaleur
- **Genesis Mining** (Islande) : green mining géothermique
- **DMG Blockchain** (Canada) : minage hydraulique certifié renouvelable
- **Iceotope / Submer** : immersion cooling applicable aux deux marchés

### Cas d'usage concrets
1. **Microsoft Natick** : résultats scientifiques publiés, mais industrialisation non décidée. Démonstration de la viabilité technique et des gains de fiabilité d'un datacenter en atmosphère contrôlée.
2. **Qarnot × Nantes Métropole Habitat** : installation de Q.rad dans des logements sociaux nantais. Les locataires chauffent leur logement gratuitement, Qarnot vend les calculs à ses clients professionnels.
3. **Ville de Vancouver** : MintGreen fournit de la chaleur pour le chauffage de bâtiments municipaux à partir de ses fermes de minage de Bitcoin alimentées à 100 % par l'hydroélectricité de la Colombie-Britannique.

### Chiffres et tendances
- Le réseau Bitcoin consomme environ **150 TWh/an** (Cambridge Centre for Alternative Finance, 2023), soit plus que l'Argentine
- La migration d'Ethereum vers Proof of Stake (The Merge, sept. 2022) a réduit sa consommation de **99,95 %**
- La part du minage Bitcoin alimenté par des énergies renouvelables est estimée à **25–40 %** selon les études (Cambridge, 2022)
- Le marché des datacenters sous-marins est encore au stade R&D, aucun déploiement commercial opérationnel en 2024

## Flashcards
#flashcards/SI_et_environnement/Projets_innovants_de_datacenters #flashcards/Blockchain/Projets_innovants_de_datacenters

Quel était l'objectif principal du Projet Natick de Microsoft ? :: Explorer la faisabilité de datacenters sous-marins pour bénéficier du refroidissement naturel par l'eau de mer, réduire les pannes (atmosphère contrôlée à l'azote) et se rapprocher des câbles sous-marins.

Quel résultat surprenant a été observé dans le Projet Natick ? :: Un taux de panne 8x inférieur à celui des datacenters terrestres, probablement dû à l'atmosphère d'azote (pas d'oxydation, pas d'humidité, pas de chocs thermiques liés aux interventions humaines).

Comment fonctionne la chaudière numérique de Qarnot ? :: Des Q.rad (radiateurs contenant des CPU/GPU) effectuent des calculs pour des clients professionnels. La chaleur produite chauffe le logement. Le client hébergeur ne paie pas l'électricité ; Qarnot se rémunère via les clients calcul.

Quelle est la différence entre le Proof of Work (Bitcoin) et le Proof of Stake (Ethereum post-Merge) en termes d'énergie ? :: Le Proof of Work (minage) consomme une énergie considérable (~150 TWh/an pour Bitcoin). Le Proof of Stake d'Ethereum (depuis sept. 2022) a réduit sa consommation de 99,95 %, ne nécessitant plus de puissance de calcul compétitive.

Qu'est-ce que le "curtailment" et quel lien avec le green mining ? :: Le curtailment est le gaspillage d'électricité renouvelable produite en excès (barrages, éolien) quand le réseau ne peut pas l'absorber. Les fermes de minage peuvent jouer le rôle de consommateur flexible pour absorber ces surplus.

Pourquoi la chaudière numérique Qarnot est-elle plus efficace qu'un datacenter traditionnel du point de vue thermodynamique ? :: Toute l'électricité consommée par les processeurs est convertie en chaleur, valorisée localement dans le bâtiment. Un datacenter classique refroidit cette chaleur vers l'extérieur (perte sèche). Rendement global quasi nul de perte.

## Sources
- Microsoft Research – Projet Natick : https://natick.research.microsoft.com
- Qarnot Computing – Site officiel : https://www.qarnot.com
- Cambridge Centre for Alternative Finance – Bitcoin Electricity Consumption Index : https://ccaf.io/cbnsi/cbeci
- The Shift Project – Impact environnemental du Bitcoin : https://theshiftproject.org
- Ethereum Foundation – The Merge (Proof of Stake) : https://ethereum.org/en/upgrades/merge
- MintGreen – Heat recovery from Bitcoin mining : https://mintgreen.co

## Notions liées
- [[Refroidissement des datacenters]]
- [[Infrastructure des datacenters]]
- [[Indicateurs environnementaux du SI]]
- [[Analyse du Cycle de Vie (ACV)]]
