---
type: notion
thèmes:
  - Mobilité
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# VPN et accès distant

![[N — VPN et accès distant.mp3]]
## En bref
> **Définition** : Un VPN (Virtual Private Network) est un tunnel chiffré établi entre un terminal distant et le réseau de l'entreprise, permettant à un utilisateur de se connecter aux ressources internes comme s'il était physiquement présent sur le réseau local. Le ZTNA (Zero Trust Network Access) est l'évolution moderne du VPN : plutôt que d'ouvrir un accès au réseau entier, il octroie un accès granulaire à des applications spécifiques après vérification continue de l'identité et du contexte.
> **Pourquoi c'est important** : Avec la généralisation du télétravail et de la mobilité, l'accès sécurisé au SI depuis l'extérieur est devenu un enjeu critique pour toute DSI. Un VPN mal configuré ou un accès distant non protégé représente l'un des vecteurs d'attaque les plus exploités par les cybercriminels (ransomwares, APT). Le passage au ZTNA est une priorité de modernisation des architectures de sécurité.
> **Chiffres clés** :
> - **Les VPN sont responsables de 40 % des vecteurs d'attaque initiaux** dans les incidents de ransomware (Mandiant, 2023)
> - **72 % des entreprises** prévoient de déployer ou d'étendre le ZTNA d'ici 2025 (Gartner, 2023)
> - Le marché du ZTNA devrait atteindre **38 milliards USD en 2029** (MarketsandMarkets, 2024)

## Approfondir

### Fonctionnement

**VPN — Virtual Private Network**

Le VPN crée un tunnel chiffré (protocoles IPSec, SSL/TLS, OpenVPN, WireGuard) entre le client et un concentrateur VPN hébergé dans l'entreprise ou le cloud.

Mécanisme :
1. Le client s'authentifie auprès du concentrateur VPN (identifiant/mot de passe + MFA)
2. Le tunnel est établi et tout le trafic du client est encapsulé et chiffré
3. Le client obtient une adresse IP sur le réseau interne de l'entreprise
4. Il peut accéder à toutes les ressources réseau (serveurs, partages, applications)

Types de VPN :
- **VPN site-à-site** : connecte deux réseaux d'entreprise (entre deux sites physiques ou avec un cloud privé)
- **VPN client-à-site** (remote access VPN) : connecte un utilisateur distant au réseau de l'entreprise, c'est le cas d'usage du télétravail
- **VPN SSL/TLS** : passe par le port HTTPS (443), peu bloqué par les pare-feux d'hôtels/réseaux publics

**Split Tunneling**
Par défaut, un VPN route tout le trafic de l'utilisateur par le tunnel (full tunnel). Le split tunneling permet de définir quelles destinations passent par le VPN (ressources internes) et lesquelles vont directement sur Internet (YouTube, Netflix). 

Avantages : réduit la charge sur le concentrateur VPN, améliore la performance pour les utilisateurs.
Risques : le trafic internet de l'utilisateur échappe au filtrage de l'entreprise, potentiel de fuite de données ou infection via un site malveillant.

**ZTNA — Zero Trust Network Access**
Approche fondée sur le principe "ne jamais faire confiance, toujours vérifier". Contrairement au VPN qui accorde un accès au réseau entier, le ZTNA accorde un accès granulaire à des applications spécifiques, après vérification continue de :
- L'identité de l'utilisateur (MFA, SSO)
- La conformité du terminal (OS à jour, antivirus actif, chiffrement)
- Le contexte (géolocalisation, heure, comportement)

Architecture ZTNA :
- **ZTNA as a Service** : le broker d'accès est hébergé dans le cloud (Cloudflare Access, Zscaler Private Access, Palo Alto Prisma Access)
- L'utilisateur ne se connecte jamais directement au réseau interne : il accède à une application via le broker
- Les serveurs internes ne sont jamais exposés directement sur Internet (micro-segmentation)

**Positionnement SASE**
Le ZTNA est l'un des composants du SASE (Secure Access Service Edge) qui intègre SD-WAN, ZTNA, CASB et SWG dans une architecture cloud unifiée. Voir [[SASE - SD-WAN]].

### Avantages / Inconvénients

| Avantages VPN | Inconvénients VPN |
|---------------|-------------------|
| Technologie mature et universelle | Accès trop large au réseau (principe de moindre privilège non respecté) |
| Chiffrement robuste du tunnel | Concentrateur VPN = point de défaillance unique |
| Compatible avec toutes les applications | Dégradation des performances (latence du tunnel) |
| Gratuit avec OpenVPN/WireGuard | Vecteur d'attaque majeur si non patché |

| Avantages ZTNA | Inconvénients ZTNA |
|----------------|-------------------|
| Accès granulaire par application | Migration complexe depuis une architecture VPN existante |
| Vérification continue du contexte | Coût plus élevé que le VPN traditionnel |
| Surface d'attaque réduite | Nécessite une identité forte (IdP, MFA) bien déployée |
| Meilleure expérience utilisateur (pas de latence VPN) | Dépendance au cloud broker (disponibilité) |

### Acteurs et solutions du marché

| Solution | Type | Éditeur |
|----------|------|---------|
| Cisco AnyConnect / Secure Client | VPN + ZTNA | Cisco |
| Pulse Secure / Ivanti | VPN | Ivanti |
| GlobalProtect | VPN + ZTNA | Palo Alto Networks |
| Zscaler Private Access (ZPA) | ZTNA SaaS | Zscaler |
| Cloudflare Access | ZTNA SaaS | Cloudflare |
| Prisma Access | SASE/ZTNA | Palo Alto Networks |
| Netskope Private Access | ZTNA SaaS | Netskope |
| OpenVPN | VPN open source | OpenVPN Inc. |
| WireGuard | VPN open source | Jason Donenfeld |

### Cas d'usage concrets

**1. Migration VPN vers ZTNA dans une banque**
Une banque de 10 000 employés exploitait deux concentrateurs VPN Cisco pour les accès distants. Suite à une exploitation de vulnérabilité CVE sur le concentrateur (incident Pulse Secure 2021), la DSI décide de migrer vers Zscaler Private Access. Les 200 applications internes sont publiées une à une via le broker ZPA. Les utilisateurs accèdent à leurs applications depuis un navigateur ou un agent léger, sans accès réseau global. La surface d'attaque est réduite de 80 %.

**2. Split tunneling pour une ESN**
Une ESN de 3 000 consultants utilise Palo Alto GlobalProtect en mode split tunneling. Les flux vers les serveurs de l'ESN passent par le VPN (chiffré, filtré), les flux vers Internet vont directement par la connexion locale. Les consultants bénéficient de meilleures performances pour les visioconférences Teams, sans surcharger les concentrateurs VPN.

**3. Accès ZTNA pour des sous-traitants**
Une entreprise industrielle donne accès à ses sous-traitants à des applications de GPAO spécifiques via Cloudflare Access. Sans VPN, sans compte Active Directory interne : les sous-traitants s'authentifient via leur propre IdP (Google, Microsoft) et accèdent uniquement à l'application autorisée. L'accès est limité à des plages horaires et des IP sources définies.

### Chiffres et tendances

- **Vulnérabilités critiques** sur les concentrateurs VPN majeures entre 2020 et 2024 : Citrix CVE-2023-4966 ("CitrixBleed"), Ivanti CVE-2024-21887, Fortinet CVE-2022-40684 — chaque fois exploitées massivement avant le patch
- **Gartner prédit** que d'ici 2025, au moins 70 % des nouveaux déploiements d'accès distant utiliseront le ZTNA plutôt que le VPN (2022)
- Le **WireGuard** s'impose comme le protocole VPN de nouvelle génération : 3x plus rapide qu'OpenVPN, code source 4x plus petit (moins de surface d'attaque)
- Tendance : intégration du **ZTNA dans les solutions UEM** (Intune + Entra ID Conditional Access) pour conditionner l'accès aux ressources à la conformité du terminal

## Flashcards
#flashcards/Mobilité/VPN_et_accès_distant #flashcards/Cybersécurité/VPN_et_accès_distant

Quelle est la différence fondamentale entre VPN et ZTNA ? :: Le VPN accorde un accès au réseau entier de l'entreprise après authentification (confiance implicite une fois connecté). Le ZTNA accorde un accès granulaire à des applications spécifiques après vérification continue de l'identité, du terminal et du contexte — sans jamais exposer le réseau interne.

Qu'est-ce que le split tunneling et quels sont ses risques ? :: Le split tunneling permet de n'envoyer par le VPN que le trafic destiné aux ressources internes, le reste allant directement sur Internet. Avantage : meilleures performances, moins de charge sur le concentrateur. Risque : le trafic Internet de l'utilisateur échappe au filtrage de l'entreprise.

Pourquoi les concentrateurs VPN sont-ils devenus un vecteur d'attaque majeur ? :: Ils sont exposés directement sur Internet, souvent non patchés rapidement en raison de contraintes opérationnelles, et leur exploitation donne directement accès au réseau interne. Des CVE critiques sur Pulse Secure, Citrix et Fortinet ont été massivement exploitées entre 2020 et 2024.

Qu'est-ce que le principe de "never trust, always verify" dans le ZTNA ? :: C'est le fondement du Zero Trust : aucun utilisateur, terminal ou réseau n'est considéré comme fiable par défaut, même s'il est déjà connecté. L'accès est accordé après vérification continue de l'identité, de la conformité du terminal et du contexte (lieu, heure, comportement).

Quels protocoles VPN sont les plus utilisés en entreprise ? :: IPSec pour les VPN site-à-site (très répandu entre datacenters). SSL/TLS pour les VPN remote access (port 443, peu bloqué). WireGuard, nouvelle génération, plus rapide et plus sûr qu'OpenVPN, en forte adoption.

Qu'est-ce que le SASE et quel lien avec le ZTNA ? :: Le SASE (Secure Access Service Edge) est une architecture réseau et sécurité cloud qui intègre SD-WAN, ZTNA, CASB (Cloud Access Security Broker) et SWG (Secure Web Gateway) dans une solution unifiée. Le ZTNA est l'un des composants clés du SASE, remplaçant le VPN traditionnel.

## Sources

- Gartner, "Market Guide for Zero Trust Network Access", 2022-2023
- Mandiant, "M-Trends Report", 2023
- ANSSI, "Recommandations sur le nomadisme numérique", 2020 (anssi.gouv.fr)
- MarketsandMarkets, "Zero Trust Security Market", 2024
- NIST SP 800-207, "Zero Trust Architecture", 2020
- Cloudflare, "What is ZTNA?", cloudflare.com

## Notions liées
- [[Zero Trust]]
- [[SASE - SD-WAN]]
- [[Gestion de la mobilité (UEM)]]
- [[Télétravail et travail hybride]]
- [[Digital Workplace]]
- [[Défense en profondeur]]
- [[Authentification et gestion des accès (IAM)]]
