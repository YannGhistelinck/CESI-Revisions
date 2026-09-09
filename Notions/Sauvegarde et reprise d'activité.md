---
type: notion
thèmes:
  - Big DATA
  - Cybersécurité
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Sauvegarde et reprise d'activité

## En bref
> **Définition** : La sauvegarde (backup) est la copie périodique des données pour permettre leur restauration en cas de perte ou de corruption. La reprise d'activité (Disaster Recovery) est l'ensemble des processus et technologies permettant de rétablir les systèmes informatiques après un sinistre (cyberattaque, panne matérielle, catastrophe naturelle, erreur humaine). Ces deux disciplines s'inscrivent dans le cadre plus large du PCA/PRA (Plan de Continuité / Plan de Reprise d'Activité).
> **Pourquoi c'est important** : Les ransomwares ciblent en priorité les sauvegardes pour rendre toute restauration impossible. Pour une DSI, une stratégie de sauvegarde robuste est la dernière ligne de défense contre la perte irrémédiable de données. Sans elle, une cyberattaque peut être fatale pour l'entreprise.
> **Chiffres clés** :
> - **93 % des entreprises** sans PRA robuste font faillite dans l'année suivant un sinistre majeur (études FEMA / Gartner).
> - Le coût moyen d'une heure d'indisponibilité applicative est estimé à **300 000 dollars** pour les grandes entreprises (Gartner, 2023).
> - **76 % des organisations** ayant subi une attaque ransomware avaient des sauvegardes — mais seulement **42 %** ont pu récupérer toutes leurs données (Sophos, 2024).

## Approfondir

### Fonctionnement

#### Types de sauvegardes

**Sauvegarde complète (Full Backup)**
- Copie intégrale de toutes les données sélectionnées.
- Avantages : restauration simple et rapide (une seule source).
- Inconvénients : longue durée d'exécution, espace de stockage important.
- Fréquence typique : hebdomadaire ou mensuelle.

**Sauvegarde incrémentale (Incremental Backup)**
- Sauvegarde uniquement les données modifiées depuis la **dernière sauvegarde** (complète ou incrémentale).
- Avantages : rapide, économe en espace.
- Inconvénients : restauration lente et complexe (nécessite la sauvegarde complète + toutes les incrémentales successives).
- Chaîne de restauration : Full (Dimanche) + Incrémentale Lundi + ... + Incrémentale Samedi.

**Sauvegarde différentielle (Differential Backup)**
- Sauvegarde uniquement les données modifiées depuis la **dernière sauvegarde complète**.
- Compromis : restauration plus simple qu'incrémentale (Full + 1 différentielle), taille intermédiaire.
- Croît en taille au fil du temps jusqu'à la prochaine sauvegarde complète.

**Comparatif :**

| Type | Données sauvegardées | Espace | Vitesse backup | Vitesse restauration |
|------|---------------------|--------|----------------|---------------------|
| Complète | Tout | +++ | Lente | Rapide |
| Incrémentale | Depuis dernière sauvegarde | + | Rapide | Lente |
| Différentielle | Depuis dernière complète | ++ | Moyenne | Moyenne |

**Sauvegarde synthétique complète** : reconstitution d'une sauvegarde complète à partir d'une complète + incrémentales, sans re-lire les données sources. Optimise les performances.

**Sauvegarde continue (CDP — Continuous Data Protection)** : réplication en temps réel de chaque écriture. RPO quasi nul. Utilisé pour les bases de données critiques.

#### La règle 3-2-1 et ses évolutions

**Règle 3-2-1 (règle de base, Peter Krogh, 2009) :**
- **3** copies des données (1 originale + 2 sauvegardes).
- **2** supports de stockage différents (ex. : disque local + NAS).
- **1** copie hors site (offsite), géographiquement séparée.

**Règle 3-2-1-1-0 (standard moderne recommandé par le NIST et Veeam) :**
- **3** copies des données.
- **2** supports de stockage différents (types de media distincts).
- **1** copie hors site.
- **1** copie hors ligne (offline) ou air-gapped (déconnectée du réseau) — résiste aux ransomwares.
- **0** erreur vérifiée : les restaurations doivent être testées et validées régulièrement.

**Règle 4-3-2 (pour les environnements très critiques) :**
- 4 copies, 3 sites géographiques distincts, 2 copies hors site.

**Air-gapped backup** : copie physiquement ou logiquement isolée du réseau. Inaccessible depuis Internet ou le SI principal. Peut être une bande magnétique déconnectée, un stockage objet avec accès bloqué, ou un cloud avec accès par token temporaire.

#### Immutable Backup (sauvegarde immuable)

Concept fondamental contre les ransomwares : une sauvegarde immuable ne peut pas être modifiée, chiffrée ou supprimée pendant une période définie (WORM — Write Once Read Many).

**Implémentations :**
- **Object Lock S3 (AWS)** : verrou d'objet en mode Compliance (impossible à supprimer, même par l'administrateur AWS) ou Governance.
- **Azure Blob Storage Immutable** : politiques de rétention immuables.
- **Veeam Immutable Backup** : sauvegardes durcies sur Linux avec attribut immuable (chattr +i).
- **Bandes magnétiques LTO** : physiquement immuables une fois écrites (WORM tapes).
- **NetBackup Resiliency Platform, Cohesity DataProtect** : immutabilité native.

**Principe :** même si un attaquant compromet les accès administrateur, les données immuables restent intactes pendant la période de rétention.

#### Métriques fondamentales : RPO et RTO

Ces deux métriques définissent les objectifs du Plan de Reprise d'Activité :

| Métrique | Définition | Question | Exemple |
|----------|------------|----------|---------|
| **RPO** (Recovery Point Objective) | Perte de données maximale acceptable (en temps) | "Jusqu'à quand puis-je perdre des données ?" | RPO = 4h : je peux perdre 4h de transactions |
| **RTO** (Recovery Time Objective) | Durée maximale acceptable d'indisponibilité | "En combien de temps dois-je redémarrer ?" | RTO = 2h : le système doit être opérationnel en 2h |

- **RPO et RTO proches de zéro** : solutions coûteuses (réplication synchrone, active-active).
- **RPO et RTO élevés** : solutions moins coûteuses (backup sur bande, site froid).

**Niveaux de DR :**
- **Site chaud (Hot Site)** : infrastructure miroir active en permanence. Basculement en minutes. Coût très élevé.
- **Site tiède (Warm Site)** : infrastructure préconfigurée mais dormante. Basculement en heures.
- **Site froid (Cold Site)** : locaux et alimentation disponibles, matériel à installer. Basculement en jours.

#### BaaS — Backup as a Service

Service cloud de sauvegarde managé. Le fournisseur gère l'infrastructure, la déduplication, le chiffrement, la rétention et les tests de restauration.

**Avantages :**
- Pas d'infrastructure de sauvegarde à maintenir.
- Scalabilité automatique.
- Chiffrement en transit et au repos inclus.
- Copie hors site native (cloud).

**Solutions principales :**
- **Veeam Cloud Connect** : sauvegarde vers le cloud depuis des environnements on-premise ou cloud.
- **Azure Backup** : service intégré pour VMs Azure, bases SQL, SAP HANA, fichiers.
- **AWS Backup** : centralisation des sauvegardes de tous les services AWS.
- **Commvault Metallic** : SaaS de sauvegarde multi-cloud.
- **Acronis Cyber Protect Cloud** : sauvegarde + cybersécurité intégrées.

#### DRaaS — Disaster Recovery as a Service

Service cloud de reprise après sinistre managé. L'infrastructure de reprise est hébergée dans le cloud du fournisseur.

**Fonctionnement :**
- Réplication continue des VMs et des données vers le cloud fournisseur.
- En cas de sinistre : activation ("failover") des machines virtuelles dans le cloud en quelques minutes.
- Tests de DR réguliers sans impacter la production.

**Avantages vs DR traditionnel :**
- Suppression du coût du site de reprise physique (CAPEX → OPEX).
- RTO réduit de jours à minutes.
- Tests non intrusifs.

**Solutions :**
- **Zerto** (Hewlett Packard Enterprise) : réplication continue, RTO < 5 minutes.
- **VMware Cloud Disaster Recovery** : DR dans VMware Cloud on AWS.
- **Azure Site Recovery (ASR)** : réplication et basculement vers Azure.
- **AWS Elastic Disaster Recovery (DRS)** : réplication vers AWS, facturation uniquement à l'activation.
- **Nutanix DRaaS**, **Veeam Disaster Recovery Orchestrator**.

#### Gouvernance et conformité des sauvegardes

**RGPD et sauvegardes :**
- Les données personnelles dans les sauvegardes sont soumises aux mêmes droits (droit à l'effacement, portabilité).
- Nécessite une politique de rétention définie et documentée.
- Chiffrement obligatoire des sauvegardes contenant des données personnelles.

**Normes et standards :**
- **ISO 22301** : système de management de la continuité d'activité (SMCA).
- **NIST SP 800-34** : guide de planification de la continuité informatique.
- **RGS (Référentiel Général de Sécurité)** : exigences ANSSI pour les systèmes d'État.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Protection contre ransomwares, sinistres, erreurs humaines | Coût de stockage et d'infrastructure (surtout hot/warm site) |
| Conformité réglementaire (RGPD, secteur bancaire, santé) | Complexité de la gestion des politiques de rétention |
| BaaS/DRaaS : réduction du CAPEX, externalisation | Risque de dépendance au fournisseur cloud (lock-in) |
| Immuabilité : résistance aux attaques ransomwares ciblant les backups | Les sauvegardes non testées donnent une fausse sécurité |
| Scalabilité du cloud pour absorber les volumes Big Data | RPO/RTO faibles = coûts exponentiels |
| Tests de DR non intrusifs avec DRaaS | Temps de restauration parfois sous-estimé en production |

### Acteurs et solutions du marché

- **Logiciels de sauvegarde** : Veeam Backup & Replication, Commvault, Veritas NetBackup, Cohesity DataProtect, Rubrik.
- **BaaS** : Azure Backup, AWS Backup, Acronis Cyber Protect Cloud, Veeam Cloud Connect.
- **DRaaS** : Zerto, Azure Site Recovery, AWS Elastic Disaster Recovery, VMware Cloud DR.
- **Stockage immuable** : AWS S3 Object Lock, Azure Immutable Blob, NetApp SnapLock.
- **Bandes magnétiques** : LTO-9 (18 To natif, 45 To compressé), StorageTek (Oracle).

### Cas d'usage concrets

1. **Attaque ransomware — Hôpital de Corbeil-Essonnes (2022)** : L'hôpital a subi une attaque du groupe Lockbit qui a chiffré l'ensemble du SI, y compris les sauvegardes accessibles depuis le réseau. La reconstruction a pris plusieurs mois, coûtant plusieurs millions d'euros. Leçon : l'absence de copie air-gapped et immuable a rendu la restauration quasi impossible.

2. **Règle 3-2-1-1-0 — Groupe industriel** : Un groupe manufacturier applique : sauvegarde complète hebdomadaire sur NAS local + réplication quotidienne vers Azure Backup + copie mensuelle sur bandes LTO hors site (air-gap). Chaque trimestre, un test de restauration à blanc valide la chaîne complète. Après un ransomware en 2023, la restauration depuis la bande a permis de rétablir 98 % des données en 6 heures.

3. **DRaaS — Banque régionale avec Zerto** : Une banque régionale utilise Zerto pour répliquer en continu ses VMs critiques (core banking, messagerie) vers Azure. Lors d'un incendie dans le datacenter principal, le basculement vers Azure a été réalisé en 4 minutes, avec une perte de données inférieure à 15 secondes (RPO effectif).

### Chiffres et tendances

- Le marché mondial du backup & recovery devrait atteindre **23 milliards de dollars d'ici 2028** (Fortune Business Insights, 2023).
- **60 % des sauvegardes** présentent des défauts qui les rendent partiellement ou totalement inutilisables lors de la restauration (Veeam Data Protection Report, 2024).
- La bande magnétique LTO reste le support le moins coûteux pour les archivages long terme : **6 fois moins cher** que le disque dur pour les données froides.
- Tendance : **cyber recovery vault** — coffre-fort numérique isolé du réseau, spécifiquement conçu pour résister aux ransomwares sophistiqués (Dell CyberRecovery, IBM Cyber Vault).
- L'immuabilité des sauvegardes devient une exigence explicite dans **NIS2** et les réglementations DORA (secteur financier).

## Flashcards
#flashcards/Big_DATA/Sauvegarde_et_reprise_d_activité #flashcards/Cybersécurité/Sauvegarde_et_reprise_d_activité #flashcards/Management_et_stratégie/Sauvegarde_et_reprise_d_activité

Quelle est la différence entre sauvegarde incrémentale et différentielle ? :: Incrémentale : sauvegarde les données modifiées depuis la DERNIÈRE sauvegarde (complète ou incrémentale) — rapide, mais restauration complexe (chaîne complète). Différentielle : sauvegarde les données modifiées depuis la DERNIÈRE COMPLÈTE — taille croissante, mais restauration simplifiée (complète + 1 différentielle).

Qu'est-ce que la règle 3-2-1-1-0 ? :: 3 copies des données, sur 2 supports différents, dont 1 hors site, 1 hors ligne (air-gapped/immuable), et 0 erreur vérifiée par des tests réguliers de restauration.

Qu'est-ce qu'une sauvegarde immuable (immutable backup) ? :: Sauvegarde qui ne peut être ni modifiée, ni chiffrée, ni supprimée pendant une période définie (WORM). Protège contre les ransomwares qui ciblent les backups. Exemples : AWS S3 Object Lock, Azure Immutable Blob.

Quelle est la différence entre RPO et RTO ? :: RPO (Recovery Point Objective) : perte de données maximale acceptable en temps ("jusqu'à quand perdre des données"). RTO (Recovery Time Objective) : durée maximale d'indisponibilité acceptable ("en combien de temps reprendre").

Qu'est-ce que le BaaS ? :: Backup as a Service : sauvegarde hébergée dans le cloud par un fournisseur managé. Supprime l'infrastructure de sauvegarde, offre scalabilité et copie hors site native. Ex. : Azure Backup, AWS Backup, Veeam Cloud Connect.

Qu'est-ce que le DRaaS et en quoi diffère-t-il du BaaS ? :: DRaaS (Disaster Recovery as a Service) : reprise d'activité complète dans le cloud en cas de sinistre, avec basculement des VMs en quelques minutes. Le BaaS se limite à la sauvegarde/restauration des données ; le DRaaS couvre la reprise applicative complète.

Pourquoi la règle 3-2-1 ne suffit plus face aux ransomwares modernes ? :: Les ransomwares ciblent désormais les sauvegardes accessibles depuis le réseau. Sans copie air-gapped (hors ligne) et immuable, toutes les copies peuvent être chiffrées. La règle 3-2-1-1-0 ajoute ces protections essentielles.

## Sources

- Veeam, *Data Protection Trends Report 2024*.
- Sophos, *State of Ransomware 2024*.
- Gartner, *Magic Quadrant for Enterprise Backup & Recovery*, 2023.
- ANSSI, *Recommandations sur la sauvegarde des systèmes d'information*, 2020.
- NIST SP 800-34, *Contingency Planning Guide for Federal Information Systems*, 2020.
- Fortune Business Insights, *Backup & Recovery Market Report*, 2023.
- ISO 22301:2019, *Business Continuity Management Systems*.

## Notions liées

- [[PCA - PRA]]
- [[Cyber-résilience]]
- [[Big Data — fondamentaux]]
- [[Data Lifecycle Management]]
- [[Plateformes cloud Big Data]]
- [[Chiffrement et gestion des clés]]
- [[NIS2]]
- [[Technologies de stockage]]
