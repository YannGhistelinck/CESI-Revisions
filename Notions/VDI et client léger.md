---
type: notion
thèmes:
  - SI et environnement
  - Mobilité
statut: pas vu
dernière_révision: 
---

# VDI et client léger

![[N — VDI et client léger.mp3]]
## En bref
> **Définition** : La VDI (Virtual Desktop Infrastructure) est une architecture qui héberge les postes de travail des utilisateurs sous forme de machines virtuelles sur des serveurs centralisés. L'utilisateur accède à son bureau via un client léger (thin client), un appareil bas de gamme qui n'exécute aucun calcul local. Le DaaS (Desktop as a Service) est la version cloud de la VDI.
> **Pourquoi c'est important** : La VDI et les clients légers permettent de réduire drastiquement la consommation électrique du parc postes de travail (80 à 90 % de réduction par rapport à un PC classique) et d'allonger la durée de vie des équipements utilisateurs. C'est un levier majeur de Green IT pour les DSI avec des flottes importantes.
> **Chiffres clés** :
> - Un client léger consomme **5 à 15 W** vs **65 à 150 W** pour un PC de bureau classique
> - Durée de vie d'un client léger : **7 à 10 ans** vs 3 à 5 ans pour un PC
> - La VDI peut réduire la consommation électrique du parc utilisateur de **70 à 90 %** (Citrix, VMware)

## Approfondir

### Fonctionnement

#### Architecture VDI
La VDI déplace le calcul du poste utilisateur vers un datacenter centralisé :

```
[Utilisateur] → [Client léger / navigateur] → [Réseau] → [Broker VDI] → [VM bureau sur serveur]
```

**Composants principaux** :
- **Hyperviseur** : héberge les VM de bureau (VMware ESXi, Citrix Hypervisor, Hyper-V)
- **Broker de connexion** : route l'utilisateur vers sa VM (VMware Horizon, Citrix Virtual Apps & Desktops, Microsoft RDS)
- **Protocole d'affichage** : transmet l'écran compressé au client (PCoIP, HDX/ICA, RDP, BLAST Extreme)
- **Stockage des profils** : solution de persistance (FSLogix, Citrix Profile Management)
- **Client** : thin client, PC recyclé, tablet, smartphone

**Types de déploiements VDI** :
| Type | Description | Usage |
|------|-------------|-------|
| **VDI persistante** | Chaque utilisateur a sa propre VM dédiée | Métiers avec outils lourds ou personnalisations |
| **VDI non persistante** | Pool de VM partagées, remises à zéro à chaque session | Postes standardisés (centres d'appels, caisses) |
| **Published Apps (RDSH)** | Applications partagées sur des serveurs multi-sessions | Applications bureautiques standard, Office |

#### Client léger (Thin Client)
Appareil informatique minimaliste conçu uniquement pour se connecter à un bureau virtuel distant :
- **Matériel** : ARM ou x86 basse consommation, 2–8 Go RAM, stockage flash 4–16 Go (pas de pièces mobiles)
- **OS** : OS léger dédié (ThinOS, HP ThinPro, Igel OS) ou Linux allégé
- **Consommation** : 5 à 15 W (vs 65–150 W pour un PC de bureau)
- **Avantages sécurité** : pas de données locales, pas de stockage, mise à jour centralisée
- **Durée de vie** : 7 à 10 ans (pas de vieillissement logiciel local)

**Zero client** : version encore plus minimaliste, sans OS local, se connectant directement via PCoIP ou Teradici.

#### DaaS – Desktop as a Service
La VDI hébergée dans le cloud public, gérée par un fournisseur tiers :
- **Amazon WorkSpaces** : DaaS AWS, facturation à l'heure ou au mois
- **Microsoft Azure Virtual Desktop (AVD)** : intégré à Microsoft 365, optimisé pour Office et Teams
- **Citrix DaaS** : anciennement Citrix Cloud, multi-cloud
- **VMware Horizon Cloud** : sur Azure, AWS ou GCP

Avantages vs VDI on-premise :
- Pas de capex infrastructure
- Élasticité (scale up/down)
- Maintenance de l'hyperviseur prise en charge

Impact Green IT du DaaS : dépend du mix énergétique du cloud provider (cf. indicateurs CUE) mais mutualisation des ressources globalement plus efficiente.

#### Certifications Energy Star (équipements)
Programme américain de l'EPA (Environmental Protection Agency) certifiant l'efficacité énergétique des équipements électroniques :
- Appliqué aux PC, serveurs, moniteurs, imprimantes, équipements réseau
- Pour les clients légers : consommation en veille < **2 W** et en fonctionnement conforme aux seuils Energy Star
- Évolution : Energy Star 9.0 pour les ordinateurs (2022) impose des seuils de consommation plus stricts
- Référence dans les appels d'offres publics et marchés IT

#### TCO Certified
Programme de certification suédois (Swedish Confederation of Professional Employees) évaluant les produits IT selon des critères sociaux et environnementaux tout au long du cycle de vie :
- **Critères environnementaux** : efficacité énergétique, substances dangereuses, recyclabilité
- **Critères sociaux** : conditions de travail dans les usines de fabrication
- **Critères ergonomiques** : confort d'utilisation, émissions sonores
- Certifie PC, serveurs, moniteurs, smartphones, casques audio
- Reconnue dans les achats publics européens (critère CCTP)

Différence avec Energy Star :
- Energy Star = uniquement la consommation électrique en usage
- TCO Certified = approche cycle de vie complet (fabrication, usage, fin de vie, social)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Réduction de 70–90 % de la consommation du parc utilisateur | Dépendance réseau : si le réseau tombe, tout s'arrête |
| Durée de vie clients légers 2–3x supérieure aux PC | Investissement initial élevé (infrastructure serveur VDI) |
| Sécurité renforcée (pas de données locales) | Latence perceptible pour les usages graphiques intensifs |
| Gestion centralisée (mises à jour, déploiements) | Pas adapté aux usages hors ligne ou nomades déconnectés |
| Réduction des coûts de support sur site | Nécessite une infrastructure réseau robuste et redondante |
| Compatibilité avec le recyclage de vieux PC en clients légers | Peut nécessiter la migration de certains logiciels incompatibles |

### Acteurs et solutions du marché
- **Citrix** : Virtual Apps & Desktops, DaaS (leader historique du marché)
- **VMware (Broadcom)** : Horizon (VDI on-premise et DaaS), Blast Extreme protocol
- **Microsoft** : Azure Virtual Desktop (AVD), Windows 365
- **HP / HPE** : thin clients HP t-series, ThinPro OS
- **IGEL** : OS léger universel pour thin clients (transforme tout PC en thin client)
- **10ZiG** : thin clients et zero clients spécialisés
- **Amazon** : WorkSpaces, AppStream 2.0
- **Wyse (Dell)** : gamme de thin clients Dell Wyse

### Cas d'usage concrets
1. **Caisse d'Épargne Île-de-France** a déployé 15 000 postes VDI Citrix sur des clients légers HP, réduisant sa consommation électrique de bureau de 85 % et le nombre d'interventions sur site de 70 %.
2. **CHU de Lille** utilise des clients légers IGEL dans ses services hospitaliers pour accéder aux applications métier (DPI, PACS radiologie). Avantage : pas de données patients locales, conformité RGPD native, postes très faciles à désinfecter.
3. **Airbus** a transformé des PC en fin de vie en thin clients via IGEL OS, prolongeant leur durée de vie de 3 ans supplémentaires tout en les intégrant dans l'infrastructure Citrix existante, économisant le coût et l'empreinte de 5 000 nouveaux équipements.

### Chiffres et tendances
- Le marché mondial de la VDI devrait atteindre **29 Md$ en 2027** (Grand View Research)
- Un déploiement VDI de 1 000 postes peut économiser **200 000 kWh/an** soit ~20 tonnes de CO₂e (réseau électrique français)
- **65 % des entreprises** du Fortune 500 utilisent Citrix ou VMware Horizon (Citrix, 2022)
- IGEL OS transforme n'importe quel PC x86 en thin client en moins de 30 minutes, avec une gestion centralisée
- Le marché DaaS croît de **+23 % par an** depuis 2020 (IDC)

## Flashcards
#flashcards/SI_et_environnement/VDI_et_client_léger #flashcards/Mobilité/VDI_et_client_léger

Qu'est-ce que la VDI et comment fonctionne-t-elle ? :: Virtual Desktop Infrastructure : les postes de travail sont des VM hébergées dans un datacenter centralisé. L'utilisateur y accède via un client léger et un protocole d'affichage (PCoIP, HDX, RDP). Aucun calcul n'est effectué localement.

Quelle est la consommation électrique comparée d'un client léger vs un PC de bureau ? :: Un thin client consomme 5–15 W, un PC de bureau classique 65–150 W. Réduction de 70 à 90 % selon les équipements.

Quelle est la différence entre VDI persistante et non persistante ? :: Persistante : chaque utilisateur a sa VM dédiée qu'il retrouve à chaque connexion (personnalisations conservées). Non persistante : les VM sont partagées, remises à zéro à chaque session (idéal pour postes standardisés).

Qu'est-ce que le DaaS ? :: Desktop as a Service : VDI hébergée dans le cloud public (Amazon WorkSpaces, Azure Virtual Desktop, Citrix DaaS). Pas de capex infrastructure, élasticité, maintenance externalisée.

Qu'est-ce que la certification TCO Certified et en quoi diffère-t-elle d'Energy Star ? :: TCO Certified (suédoise) évalue le cycle de vie complet : fabrication (substances dangereuses), usage (énergie), fin de vie (recyclabilité) et conditions sociales. Energy Star ne certifie que la consommation électrique en usage.

Pourquoi les clients légers ont-ils une durée de vie plus longue que les PC ? :: Pas de pièces mobiles (pas de HDD), pas d'OS complexe qui se dégrade, pas de mise à jour lourde locale, matériel simple peu sollicité. 7 à 10 ans vs 3 à 5 ans pour un PC classique.

Quel protocole d'affichage est associé à VMware Horizon ? :: VMware Blast Extreme (et PCoIP via Teradici, racheté par HP). Citrix utilise HDX/ICA. Microsoft RDS utilise RDP.

## Sources
- VMware – "End-User Computing Sustainability" : https://www.vmware.com
- Citrix – "The Sustainable Workplace" : https://www.citrix.com
- IGEL – OS léger pour thin clients : https://www.igel.com
- Energy Star – Programme EPA : https://www.energystar.gov
- TCO Certified – Critères et base de produits : https://tcocertified.com
- ADEME – Guide "Numérique responsable" (équipements utilisateurs) : https://www.ademe.fr
- Microsoft – Azure Virtual Desktop documentation : https://docs.microsoft.com/fr-fr/azure/virtual-desktop

## Notions liées
- [[Infrastructure des datacenters]]
- [[Analyse du Cycle de Vie (ACV)]]
- [[Indicateurs environnementaux du SI]]
- [[Technologies de stockage]]
