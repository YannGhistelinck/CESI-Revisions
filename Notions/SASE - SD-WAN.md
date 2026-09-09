---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Mobilité
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# SASE - SD-WAN

## En bref
> **Définition** : Le SASE (Secure Access Service Edge, prononcé "sassy") est un cadre architectural défini par Gartner en 2019 qui converge les fonctions réseau (SD-WAN) et les fonctions de sécurité cloud (SSE : SWG, CASB, ZTNA, FWaaS) dans un service cloud unifié et distribué. L'objectif est de connecter et sécuriser tous les utilisateurs, appareils et applications depuis n'importe quel endroit, sans backhauling vers un datacenter central.
> **Pourquoi c'est important** : Avec la généralisation du télétravail et le déplacement des applications vers le cloud (SaaS, IaaS), l'architecture réseau traditionnelle en "château-fort" (VPN vers datacenter central) est devenue un goulot d'étranglement. La DSI doit repenser l'architecture réseau pour connecter directement les utilisateurs au cloud tout en maintenant un niveau de sécurité homogène.
> **Chiffres clés** :
> - Le marché SASE devrait atteindre 25 Md$ en 2027 (Gartner, 2023)
> - 60 % des entreprises auront des stratégies et calendriers de déploiement SASE explicites d'ici 2025 (Gartner, 2022)
> - La latence moyenne réduite de 30-50 % grâce au SD-WAN par rapport aux architectures MPLS traditionnelles (IDC, 2022)

## Approfondir

### Fonctionnement

**SD-WAN (Software-Defined Wide Area Network)**
Le SD-WAN virtualise et abstrait la couche réseau WAN. Il permet d'utiliser plusieurs types de liaisons (MPLS, fibre Internet, 4G/5G) et d'appliquer des politiques de routage intelligentes selon l'application, la qualité de lien et la priorité. Fonctions clés : routage applicatif (traffic steering), QoS dynamique, failover automatique, chiffrement des tunnels (IPSec/SD-WAN overlay). Les boîtiers SD-WAN sont déployés en site (CPE : Customer Premises Equipment) et gérés centralement par un orchestrateur.

**SSE (Security Service Edge)**
Sous-ensemble du SASE centré sur la sécurité. Le SSE regroupe :
- **SWG (Secure Web Gateway)** : filtrage web, inspection SSL, protection contre les malwares
- **CASB** : contrôle des accès aux applications SaaS
- **ZTNA (Zero Trust Network Access)** : remplacement du VPN, accès applicatif sur base de l'identité et du contexte
- **FWaaS (Firewall as a Service)** : pare-feu cloud avec inspection L7

**Architecture SASE complète**
SASE = SD-WAN + SSE. Le trafic des utilisateurs (mobiles, sites) est acheminé vers le Point of Presence (PoP) SASE le plus proche, où toutes les fonctions de sécurité sont appliquées avant d'accéder à Internet ou aux applications cloud. Cela évite le backhauling (faire passer le trafic par un datacenter central avant d'aller sur Internet).

**Cloud Broker**
Intermédiaire qui facilite l'utilisation de services cloud entre un client et les fournisseurs. Dans le contexte SASE, le CASB joue souvent le rôle de cloud broker : il négocie l'accès, applique les politiques de sécurité, gère la conformité et peut faire de la médiation entre fournisseurs.

**Déploiement : Single-vendor vs. Dual-vendor SASE**
- Single-vendor : un seul éditeur fournit SD-WAN + SSE (ex : Cisco, Palo Alto Prisma SASE). Simplicité, mais dépendance fournisseur.
- Dual-vendor : SD-WAN d'un éditeur (ex : Fortinet) + SSE d'un autre (ex : Zscaler). Plus de flexibilité, intégration plus complexe.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Accès sécurisé universel (télétravail, mobilité, multi-site) | Complexité de migration depuis une architecture MPLS/VPN existante |
| Réduction des coûts MPLS (remplacement par Internet + SD-WAN) | Dépendance à la qualité d'Internet pour les liaisons SD-WAN |
| Sécurité homogène quel que soit l'emplacement de l'utilisateur | Risque de vendor lock-in (surtout en single-vendor) |
| Gestion centralisée et visibilité unifiée (tableau de bord unique) | Latence potentielle si les PoPs SASE ne sont pas proches des utilisateurs |
| Scalabilité cloud (pas de dimensionnement matériel à prévoir) | Coût de la transformation organisationnelle (skills réseau + sécurité à réunir) |
| Remplacement du VPN par ZTNA (plus granulaire et plus sûr) | Maturité variable des offres single-vendor |

### Acteurs et solutions du marché

| Solution | Positionnement | Éditeur |
|----------|----------------|---------|
| Zscaler Zero Trust Exchange | SSE leader (Magic Quadrant) | Zscaler |
| Palo Alto Prisma SASE | SASE single-vendor | Palo Alto Networks |
| Cisco Umbrella + SD-WAN | SASE (dual composant) | Cisco |
| Fortinet Secure SD-WAN | SD-WAN + SASE | Fortinet |
| Netskope | SSE / CASB fort | Netskope |
| VMware SD-WAN (VeloCloud) | SD-WAN | Broadcom (ex-VMware) |
| Cloudflare One | SASE / SSE | Cloudflare |
| Microsoft Entra Internet Access | SSE natif Azure | Microsoft |

### Cas d'usage concrets

1. **Télétravail massif post-COVID** : Une entreprise de 5 000 collaborateurs remplace son VPN SSL saturé par une solution ZTNA (Zscaler Private Access). Les utilisateurs accèdent directement aux applications SaaS via le PoP Zscaler le plus proche, sans passer par le datacenter. La latence moyenne chute de 120 ms à 25 ms pour l'accès à Office 365.

2. **Remplacement MPLS dans une enseigne retail** : Une chaîne de distribution remplace ses liaisons MPLS à 500 €/mois par site par des liaisons Internet 4G/fibre avec SD-WAN Fortinet. Les politiques de QoS priorisent les applications métier (caisses, ERP). L'économie annuelle est de 2 M€ pour 400 sites, avec une disponibilité améliorée par le dual-link automatique.

3. **SASE pour une banque multi-pays** : Une banque régionale déploie un SASE Palo Alto Prisma pour ses 80 agences en Afrique de l'Ouest. Le filtrage web, le CASB et le ZTNA sont appliqués uniformément depuis le PoP SASE le plus proche, en conformité avec les réglementations locales. La DSI gère l'ensemble depuis un tableau de bord unique.

### Chiffres et tendances

- Gartner a introduit le terme SASE en août 2019 dans le rapport "The Future of Network Security Is in the Cloud"
- Gartner Magic Quadrant for Single-Vendor SASE : Zscaler et Palo Alto Networks en position de leaders en 2023
- 70 % des nouveaux déploiements SD-WAN incluent des fonctions de sécurité intégrées en 2023 (IDC)
- Le marché SSE seul devrait atteindre 11 Md$ en 2026 (Gartner)
- L'adoption du ZTNA comme remplacement du VPN progresse : 31 % des entreprises ont déployé ZTNA en 2023 vs 10 % en 2021

## Flashcards
#flashcards/Cloud_et_Virtualisation/SASE_SD_WAN #flashcards/Mobilité/SASE_SD_WAN #flashcards/Management_et_stratégie/SASE_SD_WAN

Qu'est-ce que le SASE et par qui a-t-il été défini ? :: Secure Access Service Edge. Cadre architectural défini par Gartner en 2019 qui converge SD-WAN (réseau) et SSE (sécurité cloud : SWG, CASB, ZTNA, FWaaS) dans un service cloud unifié et distribué.

Quelle est la différence entre SASE et SSE ? :: Le SASE est le cadre complet = SD-WAN + SSE. Le SSE (Security Service Edge) est la composante sécurité uniquement du SASE (SWG + CASB + ZTNA + FWaaS), sans la partie réseau SD-WAN.

Qu'est-ce que le SD-WAN et quel problème résout-il ? :: Software-Defined WAN. Il virtualise le réseau étendu pour utiliser plusieurs types de liaisons (MPLS, Internet, 4G) avec des politiques de routage applicatif intelligentes. Il résout le coût élevé et la rigidité des liaisons MPLS.

Qu'est-ce que le backhauling et pourquoi SASE l'élimine-t-il ? :: Le backhauling consiste à faire transiter le trafic Internet des utilisateurs via un datacenter central avant de le laisser sortir. SASE l'élimine en traitant le trafic au PoP SASE le plus proche de l'utilisateur, réduisant la latence.

Qu'est-ce que le ZTNA et en quoi remplace-t-il le VPN ? :: Zero Trust Network Access. Donne accès uniquement aux applications spécifiques autorisées, sur la base de l'identité et du contexte (device, lieu, heure), sans exposer tout le réseau comme un VPN. Plus granulaire et plus sûr.

Quelle est la différence entre un déploiement SASE single-vendor et dual-vendor ? :: Single-vendor : un seul éditeur fournit SD-WAN + SSE (simplicité, mais vendor lock-in). Dual-vendor : SD-WAN d'un éditeur et SSE d'un autre (flexibilité accrue, mais intégration plus complexe).

Quels sont les 4 composants du SSE ? :: SWG (Secure Web Gateway), CASB (Cloud Access Security Broker), ZTNA (Zero Trust Network Access), FWaaS (Firewall as a Service).

## Sources

- Gartner, "The Future of Network Security Is in the Cloud", 2019
- Gartner, Magic Quadrant for Single-Vendor SASE, 2023
- Gartner, Market Guide for Security Service Edge, 2023
- IDC, "SD-WAN Infrastructure Market", 2022-2023
- ANSSI, "Recommandations de sécurité pour les architectures basées sur le cloud", 2021

## Notions liées
- [[Zero Trust]]
- [[Sécurité cloud (CSPM - CASB - CNAPP)]]
- [[Authentification et gestion des accès (IAM)]]
- [[Virtualisation]]
- [[Infrastructure des datacenters]]
- [[VDI et client léger]]
