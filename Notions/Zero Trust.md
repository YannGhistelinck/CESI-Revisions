---
type: notion
thèmes:
  - Cybersécurité
  - Cloud et Virtualisation
  - Mobilité
statut: pas vu
dernière_révision: 
---

# Zero Trust

![[N — Zero Trust.mp3]]
## En bref
> **Définition** : Zero Trust est une architecture de sécurité fondée sur le principe "ne jamais faire confiance, toujours vérifier" (Never Trust, Always Verify). Elle refuse la notion de périmètre réseau de confiance et exige une authentification et une autorisation continues pour chaque utilisateur, appareil et flux réseau, qu'ils soient internes ou externes.
> **Pourquoi c'est important** : Avec la généralisation du cloud, du télétravail et des appareils mobiles, le périmètre réseau traditionnel a disparu. Une DSI ne peut plus présupposer qu'un utilisateur connecté au VPN est digne de confiance. Zero Trust réduit drastiquement la surface d'attaque et limite les dégâts en cas de compromission.
> **Chiffres clés** :
> - Le marché Zero Trust était estimé à 31,6 Md$ en 2023 et devrait atteindre 133,7 Md$ en 2032 (Fortune Business Insights).
> - 72 % des organisations mondiales déclarent être en cours d'adoption de Zero Trust en 2023 (Okta State of Zero Trust Security 2023).
> - Les entreprises ayant adopté Zero Trust ont un coût moyen de violation de données inférieur de 1,76 M$ à celles qui ne l'ont pas fait (IBM Cost of a Data Breach 2023).

## Approfondir

### Fonctionnement

**Principes fondateurs (NIST SP 800-207)** :
1. Toutes les ressources sont considérées comme non fiables par défaut, qu'elles soient sur le réseau interne ou externe.
2. L'accès est accordé au cas par cas, selon le contexte (identité, appareil, localisation, comportement).
3. L'accès est limité au strict minimum nécessaire (least privilege).
4. Tout le trafic est inspecté et journalisé.
5. L'authentification et l'autorisation sont dynamiques et continuellement réévaluées.

**Least Privilege (moindre privilège)** : chaque utilisateur, service ou application ne dispose que des droits strictement nécessaires à sa fonction. Couplé à une revue périodique des droits (recertification). Limite l'impact d'une compromission.

**Micro-segmentation** : division du réseau en zones de sécurité granulaires (jusqu'au niveau de la charge de travail individuelle). Chaque flux est contrôlé par des politiques. Empêche le mouvement latéral de l'attaquant. Différent du VLAN traditionnel (plus granulaire, dynamique).

**ZTNA (Zero Trust Network Access)** : remplace le VPN traditionnel. L'accès aux applications est accordé application par application, après vérification de l'identité et du contexte de l'appareil. L'utilisateur n'accède jamais au réseau entier. Solutions : Zscaler Private Access, Cloudflare Access, Palo Alto Prisma Access.

**Identity-centric security** : l'identité devient le nouveau périmètre. IAM (Identity and Access Management), MFA obligatoire, SSO, PAM (Privileged Access Management), et détection des anomalies comportementales (UEBA).

**Continuous Verification** : les sessions ne sont pas considérées comme permanentes. Le contexte (score de risque de l'appareil, géolocalisation, comportement) est réévalué en continu pour adapter dynamiquement les droits d'accès (Conditional Access).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction drastique de la surface d'attaque | Complexité de mise en oeuvre et de migration |
| Limitation du mouvement latéral | Projet long terme (2-5 ans pour une adoption complète) |
| Adapté au cloud et au télétravail | Nécessite une maturité IAM solide en prérequis |
| Visibilité totale sur les flux et accès | Peut dégrader l'expérience utilisateur si mal calibré |
| Conformité facilitée (logs exhaustifs) | Coût initial élevé (licences, intégration) |
| Réduction du coût des violations de données | Résistances culturelles (fin du "on est en interne, c'est sûr") |

### Acteurs et solutions du marché

**Plateformes Zero Trust complètes (ZTNA + CASB + SWG = SSE/SASE)** :
- Zscaler (leader Gartner Magic Quadrant SSE 2024)
- Palo Alto Networks Prisma Access
- Cloudflare One
- Netskope

**IAM / MFA / PAM** :
- Microsoft Entra ID (Azure AD) + Conditional Access
- Okta, Ping Identity
- CyberArk (PAM), BeyondTrust

**Micro-segmentation** :
- Illumio, Guardicore (Akamai)
- VMware NSX

**Référentiel** : NIST SP 800-207, CISA Zero Trust Maturity Model, Microsoft Zero Trust Deployment Guide.

### Cas d'usage concrets

1. **Google BeyondCorp (2014)** : pionnier du Zero Trust. Google a supprimé son VPN interne et migré vers un modèle où chaque accès est vérifié en fonction de l'identité et de l'état de l'appareil, indépendamment de la localisation réseau. Publié en open source sous BeyondCorp Enterprise.

2. **Télétravail massif (COVID-19, 2020)** : la pandémie a mis en évidence les limites du VPN traditionnel (engorgement, accès réseau trop large). Les entreprises ont accéléré l'adoption du ZTNA pour sécuriser l'accès à distance de manière granulaire.

3. **Administration française** : la DINUM et l'ANSSI recommandent l'architecture Zero Trust dans le cadre de la politique de sécurité des systèmes d'information de l'État (PSSIE). Plusieurs ministères sont en cours de déploiement.

### Chiffres et tendances
- CISA (USA) impose l'adoption du Zero Trust à toutes les agences fédérales d'ici 2024 (Executive Order 14028, 2021).
- Le ZTNA est la technologie de sécurité à la croissance la plus rapide : +70 % de nouveaux déploiements entre 2022 et 2024 (Gartner).
- 85 % des organisations qui ont adopté Zero Trust rapportent une amélioration de leur posture de sécurité (Okta 2023).
- D'ici 2025, 60 % des entreprises remplaceront leur VPN par du ZTNA (Gartner).

## Flashcards
#flashcards/Cybersécurité/Zero_Trust #flashcards/Cloud_et_Virtualisation/Zero_Trust #flashcards/Mobilité/Zero_Trust
Quel est le principe fondamental du Zero Trust ? :: "Never Trust, Always Verify" — ne jamais présupposer la confiance, qu'un utilisateur soit interne ou externe au réseau. Chaque accès est vérifié en fonction de l'identité, de l'appareil et du contexte.

Qu'est-ce que le ZTNA et en quoi remplace-t-il le VPN ? :: Zero Trust Network Access : accorde l'accès application par application après vérification de l'identité et du contexte. Contrairement au VPN, l'utilisateur n'accède pas à tout le réseau, réduisant la surface d'attaque.

Qu'est-ce que la micro-segmentation ? :: Division du réseau en zones de sécurité très granulaires (jusqu'à la charge de travail individuelle), avec contrôle de chaque flux par politique. Empêche le mouvement latéral en cas de compromission.

Qu'est-ce que le principe de moindre privilège (least privilege) ? :: Chaque utilisateur, service ou application ne dispose que des droits strictement nécessaires à sa mission. Limite l'impact d'une compromission de compte.

Quel est le référentiel de référence pour Zero Trust ? :: NIST SP 800-207 (définition de l'architecture Zero Trust) et le CISA Zero Trust Maturity Model (guide d'implémentation par niveaux de maturité).

Quel a été le projet pionnier de Zero Trust en entreprise ? :: Google BeyondCorp (2014) : suppression du VPN interne, accès conditionné à l'identité et à l'état de l'appareil, indépendamment de la localisation réseau.

Pourquoi Zero Trust est-il particulièrement adapté au contexte cloud et mobilité ? :: Parce que le périmètre réseau traditionnel a disparu (cloud, SaaS, télétravail). Zero Trust sécurise les accès sans dépendre de la localisation physique ou réseau de l'utilisateur.

## Sources
- NIST SP 800-207 — Zero Trust Architecture — csrc.nist.gov
- CISA Zero Trust Maturity Model v2 — www.cisa.gov
- Okta — State of Zero Trust Security Report 2023 — www.okta.com
- IBM — Cost of a Data Breach Report 2023
- Gartner — Magic Quadrant for Security Service Edge (SSE) 2024
- ANSSI — Recommandations de sécurité pour les architectures Zero Trust — www.ssi.gouv.fr
- Google BeyondCorp — research.google/pubs/beyondcorp/

## Notions liées
- [[Menaces cyber]]
- [[Défense en profondeur]]
- [[SIEM]]
- [[EDR - XDR - NDR]]
- [[Cyber-résilience]]
