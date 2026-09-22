---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Cybersécurité
  - Big DATA
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Sauvegarde et solutions de protection des données

![[N — Sauvegarde et solutions de protection des données.mp3]]
## En bref

### Définition
La **sauvegarde** (backup) est la copie de données à un instant T pour permettre leur restauration en cas de perte, corruption ou attaque. La **protection continue des données (CDP — Continuous Data Protection)** capture chaque modification en temps réel, réduisant le RPO (Recovery Point Objective) à quelques secondes.

Les leaders du marché sont :
- **Veeam** : leader mondial de la sauvegarde pour environnements virtuels, cloud et physiques
- **Rubrik** : plateforme de gestion des données multi-cloud orientée sécurité et ransomware recovery
- **Commvault, Zerto, Cohesity, Acronis** : alternatives significatives

### Pourquoi c'est important
Les ransomwares ciblent prioritairement les sauvegardes pour empêcher la restauration. Une stratégie de sauvegarde robuste (règle 3-2-1-1-0, immuabilité, air gap) est la dernière ligne de défense. Sans backup opérationnel, le PRA (Plan de Reprise d'Activité) est inopérant.

### Chiffres clés
- 93 % des attaques ransomware ciblent les sauvegardes (Veeam Ransomware Trends Report 2023)
- Coût moyen d'une attaque ransomware avec paiement : 1,85 M$ (Sophos State of Ransomware 2023)
- Veeam protège plus de 450 000 clients dans 180+ pays
- Rubrik est valorisé 6 Md$ (IPO NYSE, 2024)
- Le marché mondial du backup & recovery dépasse 15 Md$ en 2024 (CAGR ~10 %)

---

## Approfondir

### Fonctionnement

**Concepts fondamentaux :**

| Concept | Définition |
|---------|------------|
| RPO (Recovery Point Objective) | Perte de données maximale acceptable (ex. 1h = restauration possible jusqu'à 1h avant l'incident) |
| RTO (Recovery Time Objective) | Délai maximal acceptable pour restaurer le service |
| CDP (Continuous Data Protection) | Capture de chaque écriture en temps réel — RPO quasi nul |
| Immuabilité | Backups non modifiables et non supprimables pendant une période définie |
| Air gap | Isolation physique ou logique des sauvegardes (déconnexion du réseau principal) |
| Déduplication | Élimination des données redondantes pour réduire l'espace de stockage |
| Réplication | Copie synchrone ou asynchrone des données vers un site distant |

**Règle 3-2-1-1-0 (évolution de la règle 3-2-1) :**
- **3** copies des données
- **2** supports différents (ex. disque + bande)
- **1** copie hors site (cloud ou site distant)
- **1** copie offline/immuable (air gap, object lock S3)
- **0** erreur lors des tests de restauration

**Types de sauvegarde :**
- **Complète (Full)** : copie intégrale de toutes les données — lente mais restauration simple
- **Incrémentale** : seules les modifications depuis la dernière sauvegarde — rapide, restauration complexe (chaîne)
- **Différentielle** : modifications depuis la dernière sauvegarde complète — compromis
- **Synthétique** : full synthétique créé à partir d'incrémentiels sans relire les données sources

**Veeam Backup & Replication :**
- Leader Gartner Magic Quadrant depuis 8 ans consécutifs
- Protection : VMware vSphere, Hyper-V, Nutanix AHV, AWS, Azure, GCP, workloads physiques
- Fonctionnalités clés : Instant VM Recovery, SureBackup (test automatique de restauration), Veeam ONE (monitoring), Hardened Linux Repository (immuabilité)
- Veeam Data Platform : version 2023 — unified platform couvrant backup, monitoring, recovery orchestration
- Intégration ransomware : détection d'anomalies inline, WORM storage, immutable backups

**Rubrik Security Cloud :**
- Approche "Zero Trust Data Security" — données immutables by design
- Architecture : cluster Rubrik (appliance ou cloud) + SLA Policy Engine
- Fonctionnalités : Polaris (SaaS management), Sensitive Data Discovery (DLP intégré), Threat Hunting (scan des backups pour IOC), Ransomware Recovery
- Rubrik Cloud Vault : air gap cloud (AWS, Azure, GCP)
- Différenciateur : les backups Rubrik sont architecturalement non modifiables — même l'administrateur ne peut pas les supprimer pendant le retention lock

**Autres acteurs clés :**

| Éditeur | Positionnement |
|---------|---------------|
| Commvault | Entreprise historique, couverture large, forte gouvernance des données |
| Zerto | Spécialiste CDP et disaster recovery — RPO en secondes |
| Cohesity | Plateforme de gestion des données secondaires + backup + analytics |
| Acronis | Mid-market / MSP, backup + EDR intégré (Cyber Protect) |
| Arcserve | Mid-market, forte présence PME |
| Bacula Enterprise | Open source d'entreprise |

**Protection des données Big Data :**
- Sauvegarde de clusters Hadoop/Spark : snapshots HDFS, réplication cross-cluster
- Protection des bases de données : Oracle RMAN, pg_dump (PostgreSQL), MySQL Enterprise Backup
- Sauvegarde objet S3 : cross-region replication, Object Lock (WORM), versioning
- Data Lifecycle Management : politique de rétention automatisée, archivage Glacier

**Sécurisation des sauvegardes contre les ransomwares :**
1. Isolation des sauvegardes (compte dédié, RBAC strict)
2. Immuabilité (Object Lock S3, WORM, Hardened Repository)
3. Air gap (copies offline ou cloud vault déconnecté)
4. Chiffrement des sauvegardes (AES-256 + gestion des clés externe)
5. Tests de restauration réguliers et automatisés
6. Détection d'anomalies sur les données de backup (Rubrik Threat Hunting, Veeam)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Dernière ligne de défense contre ransomware | Coût storage et licences significatif |
| Conformité réglementaire (RGPD, NIS2) | Complexité de gestion multi-environnements |
| RTO/RPO maîtrisés = PRA opérationnel | Tests de restauration souvent négligés |
| Immuabilité = protection contre la compromission admin | Fenêtres de sauvegarde impactant les performances |
| CDP = perte de données quasi nulle | Bande passante de réplication vers le cloud |
| Détection d'anomalies intégrée (Rubrik) | Dépendance éditeur pour les nouvelles plateformes |

### Acteurs
- **Veeam** : leader mondial, racheté par Insight Partners (2019, 5 Md$)
- **Rubrik** : challenger, IPO NYSE 2024, orienté data security
- **Commvault** : historique enterprise, coté NASDAQ
- **Zerto** : spécialiste CDP, acquis par HPE (2021, 374 M$)
- **Cohesity** : data management + backup, fusion avec Veritas (2024)
- **Acronis** : mid-market / MSP
- **Dell Technologies (PowerProtect)** : backup hardware + software intégré
- **IBM Spectrum Protect** : enterprise legacy

### Cas d'usage
- **Attaque ransomware** : restauration depuis backup immuable Rubrik avec Threat Hunting pour valider l'absence d'IOC — RTO < 4h
- **PRA multi-site** : Veeam réplication asynchrone entre site principal et DR + test SureBackup mensuel automatisé
- **Big Data** : Commvault protection des clusters Spark + archivage automatique dans S3 Glacier selon la politique de rétention
- **Cloud hybride** : Rubrik Cloud Vault pour air gap des sauvegardes critiques dans un cloud vault isolé

---

## Flashcards
#flashcards/Cloud_et_Virtualisation/Sauvegarde_et_solutions_de_protection_des_données #flashcards/Cybersécurité/Sauvegarde_et_solutions_de_protection_des_données #flashcards/Big_DATA/Sauvegarde_et_solutions_de_protection_des_données #flashcards/Optimisation_du_SI/Sauvegarde_et_solutions_de_protection_des_données

Qu'est-ce que la règle 3-2-1-1-0 en matière de sauvegarde ? :: 3 copies, 2 supports différents, 1 copie hors site, 1 copie offline/immuable (air gap), 0 erreur lors des tests de restauration.

Quelle est la différence entre RPO et RTO ? :: RPO (Recovery Point Objective) = perte de données maximale acceptable (exprimée en temps) ; RTO (Recovery Time Objective) = délai maximal pour restaurer le service après un incident.

Qu'est-ce que la protection continue des données (CDP) ? :: Continuous Data Protection — capture de chaque écriture en temps réel, permettant un RPO quasi nul (secondes) et une restauration à n'importe quel point dans le temps.

Qu'est-ce que l'immuabilité des sauvegardes et pourquoi est-elle critique ? :: Les backups immuables (WORM, Object Lock, Hardened Repository) ne peuvent être ni modifiés ni supprimés pendant une période définie — ils résistent à un attaquant ayant compromis les accès admin.

Quelle est la différence principale entre Veeam et Rubrik ? :: Veeam est le leader universel du backup multi-plateforme ; Rubrik se différencie par une architecture "Zero Trust Data Security" avec immuabilité by design et Threat Hunting intégré dans les backups.

Pourquoi 93 % des ransomwares ciblent-ils les sauvegardes ? :: Parce qu'en compromettant ou chiffrant les backups, l'attaquant s'assure que la victime ne peut pas restaurer ses données sans payer la rançon.

Quelles sont les 4 types de sauvegarde classiques ? :: Complète (full), incrémentale (depuis le dernier backup), différentielle (depuis le dernier full), synthétique (full reconstruit depuis les incrémentiels).

---

## Sources
- Veeam Ransomware Trends Report, 2023 — veeam.com
- Rubrik Zero Labs, *The State of Data Security*, 2023
- Sophos, *State of Ransomware*, 2023
- Gartner Magic Quadrant for Enterprise Backup and Recovery Software Solutions, 2023
- ANSSI, *Guide de bonnes pratiques de sauvegarde*, ssi.gouv.fr

---

## Notions liées
- [[PCA - PRA]]
- [[Sauvegarde et reprise d'activité]]
- [[Cyber-résilience]]
- [[Chiffrement et gestion des clés]]
- [[Infrastructure de stockage (SAN - NAS - HCI)]]
- [[Technologies de stockage]]
- [[Data Lifecycle Management]]
- [[Menaces cyber]]
