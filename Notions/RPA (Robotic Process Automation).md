---
type: notion
thèmes:
  - Mobilité
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# RPA (Robotic Process Automation)

## En bref
> **Définition** : La RPA (Robotic Process Automation) est une technologie qui permet de créer des robots logiciels capables de reproduire les actions qu'un humain effectuerait sur un ordinateur : clics, saisies, extraction de données, copier-coller entre applications, envoi d'e-mails. Les robots RPA opèrent sur la couche de présentation des applications existantes, sans modifier le code source, ce qui les rend très rapides à déployer sur des systèmes legacy.
> **Pourquoi c'est important** : Dans une DSI ou une direction métier, la RPA permet d'automatiser des tâches répétitives et à faible valeur ajoutée (saisie de données, rapprochements, transferts de fichiers) sans refonte du SI. Elle libère les collaborateurs pour des tâches à plus forte valeur, réduit les erreurs et accélère les traitements. Elle est un levier d'optimisation du SI sans nécessiter d'intégration lourde.
> **Chiffres clés** :
> - Le marché mondial de la RPA était de **4,4 milliards USD en 2023**, en croissance de 22 % par an (Gartner, 2023)
> - Un robot RPA traite en moyenne **15 à 20x plus vite** qu'un humain des tâches répétitives (Deloitte, 2022)
> - **85 % des entreprises** ayant déployé la RPA rapportent une réduction des erreurs de traitement (Deloitte, Global RPA Survey, 2022)

## Approfondir

### Fonctionnement

**Comment fonctionne un robot RPA ?**

Un robot RPA est un programme logiciel qui :
1. **Observe et enregistre** les actions d'un humain sur son écran (capture de clics, de frappes clavier) — phase de développement
2. **Rejoue** ces actions de manière automatique et déterministe sur les applications cibles
3. **Prend des décisions simples** basées sur des règles prédéfinies (if/then/else)
4. **Consigne ses actions** dans des journaux d'audit pour la traçabilité

Types de robots :
- **Attended bot** : robot assisté, déclenché manuellement par un utilisateur. Il travaille aux côtés de l'humain, qui reste dans la boucle. Usage : traitement de demandes clients en temps réel.
- **Unattended bot** : robot autonome, déclenché automatiquement par un scheduler ou un événement. Il s'exécute en arrière-plan, sans intervention humaine. Usage : traitements nocturnes, rapprochements bancaires.
- **Hybrid bot** : combine les deux modes selon les étapes du processus.

**RPA vs intégration classique (ETL/API)**
La RPA ne nécessite pas d'API ni d'accès à la base de données : elle interagit avec l'interface graphique, comme le ferait un utilisateur. C'est son principal avantage pour les systèmes legacy (ERP anciens, applications mainframe) qui n'exposent pas d'API.

**Process Mining**
Technique d'analyse des processus métier basée sur les journaux d'événements (logs) des systèmes d'information. Elle permet d'identifier les processus automatisables, les goulots d'étranglement et les déviations par rapport au processus théorique. Outils : Celonis, UiPath Process Mining, SAP Signavio. Le process mining est souvent la première étape avant un projet RPA.

**Hyperautomation**
Concept formalisé par Gartner : combinaison de RPA + IA (OCR, NLP, machine learning) + BPM + process mining pour automatiser des processus de bout en bout, y compris des tâches non structurées. L'hyperautomation va au-delà de la simple RPA en intégrant la compréhension du langage naturel, la reconnaissance d'images et la prise de décision intelligente.

Exemple d'hyperautomation : un robot qui extrait le contenu d'une facture reçue par e-mail (OCR + NLP), le rapproche avec la commande dans l'ERP (RPA), valide ou escalade selon des règles métier (BPM), et enregistre le paiement (RPA) — sans intervention humaine si tout est conforme.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Déploiement rapide sans modification du SI existant | Fragile face aux changements d'interface (mise à jour applicative) |
| ROI rapide (généralement < 12 mois) | Maintenance des robots chronophage |
| Réduction des erreurs de saisie | Ne résout pas les problèmes de processus sous-jacents |
| Disponibilité 24h/24, 7j/7 | Risque de "ROI theater" : automatiser des processus à faible impact |
| Traçabilité et auditabilité des actions | Résistance au changement des collaborateurs (peur du remplacement) |
| Applicable aux systèmes legacy sans API | Limité aux tâches basées sur des règles (pas de cas ambigus) |

### Acteurs et solutions du marché

| Éditeur | Solution | Positionnement |
|---------|----------|----------------|
| UiPath | UiPath Platform | Leader mondial, fort sur l'IA et l'hyperautomation |
| Automation Anywhere | Automation 360 | Leader, fort sur le cloud-native et les grandes entreprises |
| Blue Prism | Blue Prism (SS&C) | Pionnier de la RPA, fort sur les secteurs réglementés |
| Microsoft | Power Automate Desktop | Intégré M365, accessible aux non-développeurs |
| SAP | SAP Build Process Automation | Intégré à l'écosystème SAP |
| Celonis | Celonis EMS | Leader du process mining, intègre la RPA |
| Nintex | Nintex RPA | PME, processus documentaires |

### Cas d'usage concrets

**1. Rapprochement bancaire automatisé (Finance)**
Une direction financière traitait manuellement 2 000 lignes d'écritures comptables par jour entre son ERP SAP et sa banque. Un robot RPA Automation Anywhere se connecte au portail bancaire, extrait les relevés, les ouvre dans SAP et effectue le rapprochement. Le temps de traitement passe de 4 heures/jour à 15 minutes, le taux d'erreur de 2 % à quasi 0 %. ROI atteint en 4 mois.

**2. Traitement des sinistres assurance (Hyperautomation)**
Un assureur reçoit 500 déclarations de sinistres automobiles par jour par e-mail. Un robot UiPath extrait le PDF de la déclaration, un module OCR lit les champs, un module NLP interprète la description du sinistre, un score de risque est calculé. Si le sinistre est standard, la RPA ouvre le dossier dans le système de gestion et déclenche le remboursement. Les sinistres complexes sont escaladés à un expert. Résultat : 70 % des sinistres traités sans intervention humaine.

**3. Onboarding RH (Attended + Unattended)**
Lors de l'embauche d'un nouveau collaborateur, un attended bot guide le gestionnaire RH dans la saisie des informations, puis un unattended bot crée automatiquement le compte Active Directory, l'adresse e-mail, les accès aux applications métier et envoie le kit d'accueil par e-mail. Le délai d'onboarding IT passe de 3 jours à 2 heures.

### Chiffres et tendances

- **Deloitte Global RPA Survey** (2022) : 53 % des entreprises ont commencé leur parcours RPA, 72 % prévoient de l'étendre
- **UiPath** compte plus de 10 000 clients dans 70 pays (2024)
- Coût moyen d'un robot RPA : entre **5 000 € et 15 000 €/an** de licence (selon l'éditeur et le type)
- Tendance majeure : **RPA + IA générative** — les robots interagissent avec des LLM pour traiter des données non structurées (emails, contrats, formulaires libres)
- **Process mining** : adoption en forte croissance (Celonis valorisé 13 Md$ en 2021) ; devient un prérequis avant tout projet RPA ou ERP
- Risque : le "bot sprawl" — prolifération incontrôlée de robots, difficiles à maintenir et à gouverner

## Flashcards
#flashcards/Mobilité/RPA_Robotic_Process_Automation #flashcards/Optimisation_du_SI/RPA_Robotic_Process_Automation

Quelle est la différence entre un attended bot et un unattended bot ? :: Un attended bot est déclenché manuellement par un utilisateur et travaille en collaboration avec lui (traitement de demandes en temps réel). Un unattended bot fonctionne de manière autonome, déclenché par un scheduler ou un événement, sans intervention humaine (traitements nocturnes).

Pourquoi la RPA est-elle adaptée aux systèmes legacy ? :: Parce qu'elle interagit avec l'interface graphique des applications (comme le ferait un utilisateur humain), sans nécessiter d'API, d'accès aux bases de données ou de modification du code source. Elle est donc déployable rapidement sur des ERP anciens ou des applications mainframe.

Qu'est-ce que l'hyperautomation ? :: L'hyperautomation combine la RPA avec l'IA (OCR, NLP, machine learning) et le BPM pour automatiser des processus de bout en bout, y compris des tâches non structurées. Elle va au-delà de la simple RPA en permettant la compréhension du langage naturel et la prise de décision intelligente.

Qu'est-ce que le process mining et quel est son lien avec la RPA ? :: Le process mining analyse les journaux d'événements (logs) du SI pour cartographier les processus réels, identifier les tâches répétitives automatisables et les goulots d'étranglement. Il est généralement la première étape d'un projet RPA pour cibler les bons processus à automatiser.

Quelles sont les principales limites de la RPA ? :: La RPA est fragile face aux changements d'interface (une mise à jour applicative peut casser un robot). Elle ne convient qu'aux tâches basées sur des règles strictes. Elle peut générer de la maintenance coûteuse et, si mal gouvernée, du "bot sprawl" (prolifération incontrôlée de robots).

Citez trois éditeurs RPA majeurs et leurs caractéristiques. :: UiPath : leader mondial, fort sur IA et hyperautomation. Automation Anywhere : leader cloud-native. Blue Prism : pionnier, fort sur les secteurs réglementés (finance, santé). Microsoft Power Automate Desktop est l'option accessible intégrée à M365.

## Sources

- Gartner, "Magic Quadrant for Robotic Process Automation", 2023
- Deloitte, "Global RPA Survey", 2022
- UiPath, Annual Report 2024
- Forrester, "The RPA Market Will Reach $22B By 2025"
- Celonis, "Process Mining and Automation Report", 2023
- KPMG, "Intelligent Automation Survey", 2022

## Notions liées
- [[Low-code - No-code]]
- [[Digital Workplace]]
- [[Business Intelligence (BI)]]
- [[DevOps]]
- [[Architecture logicielle]]
- [[Infrastructure as Code (IaC)]]
- [[ETL - ELT et pipelines de données]]
