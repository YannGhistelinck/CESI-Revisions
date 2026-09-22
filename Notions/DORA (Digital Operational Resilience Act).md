---
type: notion
thèmes:
  - Cybersécurité
  - Cloud et Virtualisation
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# DORA (Digital Operational Resilience Act)

![[N — DORA (Digital Operational Resilience Act).mp3]]
## En bref

### Définition
DORA (Digital Operational Resilience Act) est un règlement européen (UE 2022/2554) entré en vigueur le 17 janvier 2025. Il impose aux entités du secteur financier (banques, assurances, prestataires de services d'investissement, fournisseurs de cryptoactifs…) et à leurs prestataires TIC critiques un cadre unifié de gestion du risque opérationnel numérique, de tests de résilience et de notification des incidents majeurs.

### Pourquoi c'est important
DORA crée pour la première fois une exigence réglementaire directe sur les prestataires TIC (cloud providers, ESN) qui servent le secteur financier. Pour un DSI ou RSSI d'une entité financière ou d'un fournisseur critique, DORA est une obligation légale non-négociable depuis janvier 2025.

### Chiffres clés
- DORA s'applique à plus de 22 000 entités financières en Europe
- Les prestataires TIC critiques désignés par les AES (Autorités Européennes de Surveillance) sont soumis à des audits directs
- Amendes potentielles : jusqu'à 2 % du chiffre d'affaires mondial annuel pour les entités financières ; jusqu'à 1 % pour les prestataires TIC pendant la période de non-conformité
- Date d'application : 17 janvier 2025 (2 ans après l'entrée en vigueur du règlement)

---

## Approfondir

### Fonctionnement

#### Périmètre d'application
**Entités financières concernées :**
- Établissements de crédit (banques)
- Entreprises d'investissement
- Établissements de paiement et de monnaie électronique
- Compagnies d'assurance et de réassurance
- Sociétés de gestion d'actifs
- Prestataires de services de cryptoactifs (CASP — MiCA)
- Contreparties centrales (CCP), dépositaires centraux

**Exclusions** : petites entités avec des régimes simplifiés (proportionnalité selon la taille et le profil de risque).

#### Les 5 piliers de DORA

**Pilier 1 — Gestion du risque TIC (ICT Risk Management)**
- Cadre de gouvernance : le conseil d'administration est directement responsable de la résilience numérique
- Stratégie de résilience numérique, politique de sécurité de l'information
- Gestion des actifs TIC, classification des risques
- Plan de continuité des activités (BCP) et plan de reprise après sinistre (DRP) TIC
- Revue annuelle du cadre de gestion des risques

**Pilier 2 — Gestion des incidents TIC (ICT Incident Management)**
- Définition et classification des incidents : critères réglementaires (durée, impact clients, perte de données…)
- Processus de notification obligatoire en 3 étapes :
  - **Notification initiale** : dans les 4h suivant la classification (entités financières majeures)
  - **Rapport intermédiaire** : dans les 72h
  - **Rapport final** : dans le mois suivant la clôture
- Autorités compétentes : BCE, ACPR (France), BaFin (Allemagne), etc.

**Pilier 3 — Tests de résilience opérationnelle numérique (DORA Testing)**
- Tests de base annuels pour toutes les entités (tests de vulnérabilité, scans réseau…)
- **TLPT (Threat-Led Penetration Testing)** : tests avancés basés sur la menace réelle (type TIBER-EU), obligatoires tous les 3 ans pour les entités significatives
- Les prestataires TIC critiques peuvent être inclus dans le périmètre des TLPT

**Pilier 4 — Risque lié aux tiers (ICT Third-Party Risk)**
- Registre complet de tous les prestataires TIC (contrats, SLA, niveaux de criticité)
- Exigences contractuelles minimales obligatoires avec les prestataires TIC (clauses DORA)
- Stratégie de sortie et plans de continuité en cas de défaillance d'un prestataire
- Concentration du risque : vigilance sur la dépendance à un prestataire dominant (ex. AWS, Azure, Google Cloud)
- Désignation de **Prestataires TIC Critiques (CTPP)** par les Autorités Européennes de Surveillance — soumis à un régime de surveillance directe

**Pilier 5 — Partage d'informations**
- Partage volontaire de renseignements sur les cybermenaces entre entités financières
- Encouragé mais non obligatoire
- Cadres de partage : ISAC financiers (FS-ISAC, CERT-FIN…)

#### Gouvernance DORA
- Le conseil d'administration doit suivre des formations en résilience numérique
- Désignation d'un responsable DORA en interne (souvent le RSSI ou le DSI)
- Reporting régulier au conseil sur la posture de résilience numérique

#### Articulation avec d'autres réglementations
| Réglementation | Lien avec DORA |
|----------------|----------------|
| NIS2 | Complémentaire : NIS2 = secteurs critiques, DORA = spécifique finance. Entités financières soumises aux deux. |
| RGPD | DORA impose la notification des incidents impactant les données personnelles, cohérent avec RGPD |
| ISO 27001 | DORA s'appuie sur les bonnes pratiques SMSI mais va plus loin (tests TLPT, tiers) |
| EBA Guidelines | DORA remplace/complète les guidelines EBA sur l'outsourcing et la sécurité TIC |
| MiCA | DORA s'applique aux CASP réglementés par MiCA |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Harmonisation réglementaire européenne | Charge de conformité massive (coût estimé 50-150 M€ pour une grande banque) |
| Résilience systémique du secteur financier | Délais très courts pour la notification d'incidents (4h) |
| Pression sur les prestataires cloud pour durcir leur sécurité | Risque de concentration sur quelques prestataires "conformes" |
| Clarification des responsabilités conseil d'administration | Complexité de la gestion des tiers (registre, clauses, exit plans) |
| Convergence avec NIS2, ISO 27001 | Manque de précision sur certains critères de classification d'incidents |

### Acteurs et solutions

| Acteur / Solution | Rôle |
|-------------------|------|
| EBA, EIOPA, ESMA (AES) | Autorités Européennes de Surveillance — émettent les RTS/ITS techniques |
| ACPR, BCE | Supervision des entités financières françaises et européennes |
| AWS, Azure, Google Cloud | Prestataires TIC potentiellement désignés comme critiques |
| Deloitte, PwC, KPMG, EY | Conseil et audit de conformité DORA |
| IBM, ServiceNow | Solutions ITSM/GRC pour la conformité DORA |
| FS-ISAC | Partage d'information sur les menaces (pilier 5) |

### Cas d'usage concrets

- **Banque française (Tier 1)** : programme DORA en 2 ans — cartographie de 300+ prestataires TIC, revue de 800 contrats, déploiement d'un processus de notification incidents en 4h, 3 TLPT planifiés
- **Assureur européen** : désignation d'un "DORA Officer" (RSSI élargi), formation du conseil d'administration, intégration des clauses DORA dans tous les nouveaux contrats cloud
- **FinTech (CASP MiCA)** : application du régime simplifié DORA avec tests de base annuels et notification des incidents significatifs à l'AMF
- **ESN prestataire TIC critique** : soumission au programme de surveillance directe des AES — audits, rapports trimestriels, obligation de corriger les vulnérabilités identifiées

### Chiffres et tendances

- 17 janvier 2025 : date d'applicabilité de DORA — toutes les entités devaient être conformes
- Les RTS (Regulatory Technical Standards) et ITS (Implementing Technical Standards) de DORA : 13 textes techniques publiés par les AES entre 2023 et 2024
- Concentration cloud : BCE identifie que 65 % de l'infrastructure cloud des banques européennes repose sur 3 prestataires (AWS, Azure, GCP)
- Tendance 2025 : les premiers audits TLPT commencent ; les premiers prestataires critiques sont désignés par les AES
- Budget moyen de mise en conformité DORA : 2-5 M€ pour une banque régionale, 50-150 M€ pour un groupe systémique

---

## Flashcards
#flashcards/Cybersécurité/DORA_Digital_Operational_Resilience_Act #flashcards/Cloud_et_Virtualisation/DORA_Digital_Operational_Resilience_Act #flashcards/Management_et_stratégie/DORA_Digital_Operational_Resilience_Act

Qu'est-ce que DORA et à qui s'applique-t-il ? :: Règlement UE 2022/2554 applicable depuis le 17 janvier 2025. S'applique aux entités financières (banques, assurances, prestataires d'investissement, CASP) et à leurs prestataires TIC critiques opérant en Europe.

Quels sont les 5 piliers de DORA ? :: 1. Gestion du risque TIC, 2. Gestion et notification des incidents TIC, 3. Tests de résilience (dont TLPT), 4. Gestion du risque lié aux tiers, 5. Partage d'informations sur les cybermenaces.

Quels sont les délais de notification d'incident imposés par DORA ? :: Notification initiale dans les 4h, rapport intermédiaire dans les 72h, rapport final dans le mois suivant la clôture — auprès de l'autorité compétente (ex. ACPR en France).

Qu'est-ce qu'un TLPT selon DORA ? :: Threat-Led Penetration Testing : test d'intrusion avancé basé sur la menace réelle (modèle TIBER-EU), obligatoire tous les 3 ans pour les entités financières significatives. Il peut inclure les prestataires TIC dans son périmètre.

Quelle est la différence entre DORA et NIS2 ? :: NIS2 couvre l'ensemble des secteurs critiques (santé, énergie, transport, numérique…). DORA est spécifique au secteur financier et va plus loin sur la gestion des tiers TIC et les tests de résilience. Les entités financières sont soumises aux deux.

Qu'est-ce qu'un prestataire TIC critique selon DORA ? :: Prestataire désigné par les Autorités Européennes de Surveillance (AES) en raison de leur importance systémique pour le secteur financier. Ils sont soumis à une surveillance directe des AES (audits, rapports, corrections obligatoires).

Quel est l'enjeu DORA lié à la concentration cloud ? :: Les AES surveillent le risque de concentration excessive chez un seul prestataire cloud (AWS, Azure, GCP). Les entités financières doivent avoir des stratégies de sortie et des plans de continuité en cas de défaillance de leur fournisseur cloud principal.

---

## Sources

- Règlement (UE) 2022/2554 du Parlement européen et du Conseil (DORA), 14 décembre 2022
- EBA, EIOPA, ESMA, *Regulatory Technical Standards DORA*, 2023-2024
- ACPR, *Guide de mise en conformité DORA*, 2024
- BCE, *Report on Supervisory Priorities for Digital Resilience*, 2024
- FS-ISAC, *DORA Implementation Guidance*, 2024

---

## Notions liées

- [[NIS2]]
- [[ISO 27001 - 27002]]
- [[Cyber-résilience]]
- [[PCA - PRA]]
- [[EBIOS RM et gestion des risques cyber]]
- [[Gouvernance IT]]
- [[Cloud souverain]]
- [[Certifications et normes cloud]]
