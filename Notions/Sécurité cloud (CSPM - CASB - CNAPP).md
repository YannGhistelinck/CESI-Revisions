---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Sécurité cloud (CSPM - CASB - CNAPP)

![[N — Sécurité cloud (CSPM - CASB - CNAPP).mp3]]
## En bref
> **Définition** : La sécurité cloud regroupe un ensemble d'outils et de pratiques visant à protéger les environnements cloud contre les mauvaises configurations, les accès non autorisés et les menaces. Les acronymes CSPM, CASB et CNAPP désignent des catégories d'outils complémentaires couvrant respectivement la posture de sécurité, l'accès aux applications cloud et la protection native des applications cloud.
> **Pourquoi c'est important** : Dans une DSI, la majorité des incidents cloud sont causés par des erreurs de configuration (misconfiguration) et non par des failles zero-day. Ces outils permettent d'automatiser la détection des dérives et de maintenir une posture de sécurité conforme en continu, notamment dans les architectures multi-cloud.
> **Chiffres clés** :
> - 99 % des défaillances de sécurité cloud seront imputables au client, pas au fournisseur, jusqu'en 2025 (Gartner)
> - 45 % des violations de données sont liées au cloud en 2023 (IBM Cost of a Data Breach Report 2023)
> - Le marché CNAPP devrait atteindre 23 Md$ en 2028 (MarketsandMarkets, 2023)

## Approfondir

### Fonctionnement

**CSPM (Cloud Security Posture Management)**
Le CSPM analyse en continu la configuration des ressources cloud (IAM, stockage, réseau, services managés) pour détecter les écarts par rapport aux benchmarks de sécurité (CIS Benchmarks, NIST, ISO 27001). Il génère des alertes et peut appliquer des remédiation automatiques. Il fonctionne via des APIs des fournisseurs cloud (AWS Config, Azure Policy, GCP Security Command Center).

**CASB (Cloud Access Security Broker)**
Le CASB s'intercale entre les utilisateurs et les services cloud pour contrôler, auditer et protéger les accès. Il opère en mode proxy (inline) ou via des APIs. Il assure quatre fonctions : visibilité sur le Shadow IT, conformité (DLP), protection contre les menaces, contrôle d'accès (UEBA).

**CNAPP (Cloud-Native Application Protection Platform)**
Le CNAPP est une plateforme unifiée qui regroupe CSPM + CWPP (Cloud Workload Protection Platform) + CIEM + scan des images conteneurs + DAST/SAST cloud. Il couvre le cycle de vie complet de l'application cloud-native, du code au runtime. Gartner a formalisé ce terme en 2021.

**CWPP (Cloud Workload Protection Platform)**
Protection des workloads à l'exécution : VMs, conteneurs, fonctions serverless. Détection des comportements anormaux, protection mémoire, contrôle des processus.

**CIEM (Cloud Infrastructure Entitlement Management)**
Gestion des droits et des permissions dans le cloud. Détecte les comptes surprivilégiés, les permissions inutilisées, les rôles transitifs dangereux. Applique le principe du moindre privilège.

**Landing Zone et Guardrails**
Une landing zone est une architecture cloud préconfigurée et sécurisée servant de socle pour déployer des workloads. Les guardrails sont des politiques préventives (Service Control Policies AWS, Azure Policy) et détectives (AWS Config Rules) appliquées à toute l'organisation cloud. Ils empêchent les dérives de configuration dès la création des ressources.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection continue et automatisée des misconfigurations | Génération possible de nombreux faux positifs (alert fatigue) |
| Couverture multi-cloud et multi-comptes | Coût élevé des solutions enterprise (Prisma Cloud, Wiz) |
| Réduction du délai de détection (MTTD) | Courbe d'apprentissage et complexité d'intégration |
| Conformité réglementaire automatisée (PCI-DSS, RGPD, ISO 27001) | Dépendance aux APIs des CSP, couverture parfois incomplète |
| CNAPP unifie les outils et réduit la complexité | Risque de fausse assurance si mal paramétré |

### Acteurs et solutions du marché

| Solution | Type | Éditeur |
|----------|------|---------|
| Prisma Cloud | CNAPP | Palo Alto Networks |
| Wiz | CNAPP / CSPM | Wiz Inc. (racheté par Google, 2024) |
| Microsoft Defender for Cloud | CNAPP | Microsoft |
| Lacework | CNAPP | Lacework |
| Orca Security | CNAPP / CSPM | Orca Security |
| Netskope | CASB / SSE | Netskope |
| McAfee MVISION Cloud | CASB | Skyhigh Security |
| AWS Security Hub | CSPM natif | AWS |
| Azure Security Center | CSPM natif | Microsoft |

### Cas d'usage concrets

1. **Détection de bucket S3 public** : Un CSPM détecte automatiquement qu'un bucket S3 a été ouvert en accès public lors d'un déploiement Terraform mal configuré. Une alerte est remontée et une remédiation automatique remet le bucket en privé, avant toute exfiltration de données.

2. **Contrôle du Shadow IT avec un CASB** : Une entreprise déploie un CASB en mode proxy pour identifier que 40 % des collaborateurs utilisent des services cloud non approuvés (Dropbox, WeTransfer) pour partager des fichiers sensibles. Le CASB bloque les transferts non conformes et redirige vers les solutions approuvées.

3. **CIEM et comptes sur-privilegiés** : Lors d'un audit CIEM, on découvre que 78 % des rôles IAM AWS n'ont pas utilisé leurs permissions depuis 90 jours. Le CIEM recommande une réduction des droits, réduisant drastiquement la surface d'attaque en cas de compromission de compte.

### Chiffres et tendances

- Gartner classe CNAPP comme une technologie "transformationnelle" dans son Hype Cycle for Cloud Security 2023
- 75 % des entreprises auront consolidé leurs outils de sécurité cloud vers une approche CNAPP d'ici 2026 (Gartner)
- Les misconfigurations cloud représentent la première cause d'incidents cloud (Verizon DBIR 2023)
- Acquisition de Wiz par Google pour 23 Md$ en 2024 : signal fort de la centralité de ce marché

## Flashcards
#flashcards/Cloud_et_Virtualisation/Sécurité_cloud_CSPM_CASB_CNAPP #flashcards/Management_et_stratégie/Sécurité_cloud_CSPM_CASB_CNAPP

Qu'est-ce que le CSPM ? :: Cloud Security Posture Management. Outil qui analyse en continu les configurations cloud pour détecter les écarts par rapport aux bonnes pratiques et benchmarks de sécurité (CIS, NIST).

Quelle est la différence entre CSPM et CWPP ? :: Le CSPM gère la posture de configuration des ressources cloud (infrastructure). Le CWPP protège les workloads à l'exécution (VMs, conteneurs, fonctions serverless) contre les menaces actives.

Qu'est-ce qu'un CASB et quels sont ses 4 piliers ? :: Cloud Access Security Broker. Intermédiaire entre utilisateurs et services cloud. Ses 4 piliers : Visibilité (Shadow IT), Conformité (DLP), Protection contre les menaces, Contrôle d'accès.

Qu'est-ce que le CNAPP ? :: Cloud-Native Application Protection Platform. Plateforme unifiée qui regroupe CSPM, CWPP, CIEM et scan des conteneurs pour couvrir la sécurité des applications cloud-native de bout en bout.

Qu'est-ce qu'une landing zone ? :: Architecture cloud préconfigurée et sécurisée servant de fondation pour déployer des workloads. Elle inclut les guardrails, la gestion des comptes, le réseau de base et les politiques de conformité.

Qu'est-ce que le CIEM ? :: Cloud Infrastructure Entitlement Management. Gère les droits et permissions dans le cloud, détecte les comptes sur-privilégiés et applique le principe du moindre privilège.

Quelle est la principale cause d'incidents cloud selon Gartner ? :: Les misconfigurations (mauvaises configurations), imputables au client dans 99 % des cas, pas au fournisseur cloud.

## Sources

- Gartner, "Innovation Insight for CNAPP", 2021
- Gartner, Hype Cycle for Cloud Security, 2023
- IBM, "Cost of a Data Breach Report", 2023
- Verizon, "Data Breach Investigations Report", 2023
- NIST SP 800-210 : General Access Control Guidance for Cloud Systems
- CIS Benchmarks : https://www.cisecurity.org/cis-benchmarks

## Notions liées
- [[Zero Trust]]
- [[Authentification et gestion des accès (IAM)]]
- [[Défense en profondeur]]
- [[SASE - SD-WAN]]
- [[Chiffrement et gestion des clés]]
- [[Infrastructure des datacenters]]
