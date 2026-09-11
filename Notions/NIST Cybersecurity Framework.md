---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# NIST Cybersecurity Framework

## En bref
> **Définition** : Le NIST Cybersecurity Framework (NIST CSF) est un cadre de référence volontaire développé par le National Institute of Standards and Technology (NIST) américain, publié en 2014 et mis à jour en version 2.0 en février 2024. Il structure la gestion des risques cyber en 6 fonctions (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) et fournit un langage commun pour piloter la cybersécurité à tous les niveaux de l'organisation.
> **Pourquoi c'est important** : Adopté par des milliers d'organisations dans le monde, le NIST CSF est devenu un standard de facto pour évaluer et améliorer la maturité cyber. Il est utilisé par les RSSI et DSI pour structurer leur stratégie, prioriser les investissements et communiquer avec la direction. Il est complémentaire des normes ISO 27001 et sert de référence pour de nombreux cadres réglementaires.
> **Chiffres clés** :
> - Plus de 5 000 organisations dans 100 pays utilisent le NIST CSF (NIST, 2023)
> - 30 % des entreprises du Fortune 500 s'y réfèrent dans leurs rapports annuels
> - Le CSF 2.0 (2024) ajoute une 6e fonction GOVERN et intègre la sécurité de la chaîne d'approvisionnement

## Approfondir

### Fonctionnement

**Structure du NIST CSF 2.0 :**

Le framework est organisé en 3 composants :
- **Core** : les 6 fonctions, leurs catégories et sous-catégories
- **Profils** : état actuel ("profil actuel") et état cible ("profil cible") de l'organisation
- **Niveaux d'implémentation (Tiers)** : de 1 (Partiel) à 4 (Adaptatif), mesurant la maturité des pratiques

**Les 6 fonctions du Core (CSF 2.0) :**

**1. GOVERN (GV) — Nouveau dans CSF 2.0**
- Établir et maintenir la stratégie, les politiques, les rôles et responsabilités en matière de cybersécurité
- Intégration du risque cyber dans la gouvernance globale de l'organisation
- Gestion des risques liés à la chaîne d'approvisionnement
- Exemples : politique cybersécurité approuvée par la direction, rôles RSSI/DPO définis, budget cyber alloué

**2. IDENTIFY (ID)**
- Comprendre le contexte de l'organisation, les actifs critiques et les risques
- Inventaire des actifs matériels et logiciels, cartographie des dépendances
- Évaluation des risques (analyse de menaces, vulnérabilités, impacts)
- Exemples : CMDB à jour, analyse de risques annuelle, cartographie du SI

**3. PROTECT (PR)**
- Mettre en place les mesures de protection des actifs critiques
- Contrôle d'accès, sensibilisation/formation, sécurité des données, processus de protection, maintenance, technologies de protection
- Exemples : MFA, chiffrement, segmentation réseau, patch management, DLP, formation phishing

**4. DETECT (DE)**
- Identifier rapidement les événements de cybersécurité
- Surveillance continue, détection des anomalies, processus de détection
- Exemples : SIEM, SOC, IDS/IPS, monitoring des logs, threat hunting

**5. RESPOND (RS)**
- Gérer un incident de cybersécurité détecté
- Plan de réponse, communication, analyse, atténuation, amélioration
- Exemples : procédures de réponse aux incidents, cellule de crise, notification ANSSI/CNIL, forensics

**6. RECOVER (RC)**
- Restaurer les capacités et services après un incident
- Plan de récupération, communication, améliorations post-incident
- Exemples : PRA activé, restauration depuis sauvegardes, retour d'expérience (REX), communication aux parties prenantes

**Niveaux d'implémentation (Tiers) :**
| Niveau | Nom | Description |
|--------|-----|-------------|
| Tier 1 | Partiel | Pratiques ad hoc, réactives, peu formalisées |
| Tier 2 | Informé des risques | Pratiques partiellement formalisées, conscience des risques |
| Tier 3 | Répétable | Pratiques formalisées, politiques définies, révisées régulièrement |
| Tier 4 | Adaptatif | Amélioration continue, réponse agile aux menaces, pratiques intégrées |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Cadre flexible et adapté à toute taille d'organisation | Non certifiable (pas d'audit tiers officiel) |
| Langage commun entre métiers, IT et direction | Américain, moins intégré aux exigences réglementaires européennes |
| Gratuit et accessible (disponible sur nist.gov) | Nécessite une adaptation au contexte de l'organisation |
| Complémentaire avec ISO 27001 et NIS2 | Peut rester théorique sans pilotage rigoureux |
| CSF 2.0 intègre gouvernance et supply chain | Risque de confusion avec les autres cadres NIST (SP 800-53, SP 800-171) |
| Référence mondiale reconnue par les assureurs | Mise à jour 2.0 nécessite une révision des implémentations existantes |

### Acteurs et solutions du marché
- **NIST** : nist.gov/cyberframework — documentation officielle, ressources et outils
- **Outils d'auto-évaluation** : NIST CSF Tool (officiel), CISA Cyber Essentials, ServiceNow GRC
- **Cabinets de conseil** : tous les grands cabinets (Accenture, Deloitte, KPMG, Wavestone) proposent des missions d'évaluation et de mise en œuvre du NIST CSF
- **Intégration dans les produits de sécurité** : Microsoft Defender XDR, Palo Alto Cortex XSIAM, CrowdStrike Falcon mappent leurs fonctionnalités sur les fonctions NIST CSF
- **Correspondance normative** : CISA a publié des guides de correspondance NIST CSF ↔ ISO 27001 ↔ CIS Controls

### Cas d'usage concrets
1. **Évaluation de maturité cyber pour un COMEX** : Une DSI utilise le NIST CSF pour réaliser une évaluation de maturité (Tier actuel vs Tier cible) présentée au COMEX. Les résultats permettent de prioriser un plan d'investissement pluriannuel en cybersécurité avec un langage compréhensible par les non-techniciens.
2. **Réponse à un incident ransomware** : Lors d'une attaque, l'équipe de réponse s'appuie sur les fonctions DETECT → RESPOND → RECOVER du CSF pour orchestrer les actions : isolation des systèmes, notification des autorités, activation du PRA, communication de crise, puis REX post-incident.
3. **Audit de fournisseurs** : Un grand groupe exige de ses fournisseurs IT qu'ils s'auto-évaluent selon le NIST CSF et atteignent un niveau Tier 3 minimum. Cela structure les exigences de sécurité de la chaîne d'approvisionnement sans imposer une certification onéreuse.

### Chiffres et tendances
- Le CSF 2.0 (février 2024) est la première mise à jour majeure depuis 2018 : ajout de GOVERN, intégration du supply chain risk management, nouvelles ressources d'implémentation
- Adoption mondiale en forte hausse : utilisé bien au-delà des USA, notamment en Europe comme complément à l'ISO 27001
- La CISA (Cybersecurity and Infrastructure Security Agency) aux États-Unis s'appuie sur le NIST CSF pour ses recommandations sectorielles
- La correspondance NIST CSF ↔ NIS2 est documentée par l'ENISA, facilitant la double conformité

## Flashcards
#flashcards/Cybersécurité/NIST_Cybersecurity_Framework
Quelles sont les 6 fonctions du NIST CSF 2.0 ? :: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER. La fonction GOVERN est la nouveauté du CSF 2.0 (2024), elle pilote toutes les autres.

Quelle est la différence entre un profil actuel et un profil cible dans le NIST CSF ? :: Le profil actuel décrit l'état de maturité cyber actuel de l'organisation. Le profil cible définit l'état souhaité. L'écart entre les deux guide le plan d'action.

Quels sont les 4 niveaux d'implémentation (Tiers) du NIST CSF ? :: Tier 1 (Partiel, ad hoc), Tier 2 (Informé des risques, partiellement formalisé), Tier 3 (Répétable, formalisé et révisé), Tier 4 (Adaptatif, amélioration continue).

Quelle est la principale nouveauté du NIST CSF 2.0 ? :: L'ajout de la fonction GOVERN, qui place la gouvernance et la stratégie cyber au centre du cadre. Elle couvre la politique de sécurité, les rôles et responsabilités, la gestion des risques de la chaîne d'approvisionnement.

Le NIST CSF est-il certifiable ? :: Non, le NIST CSF est un cadre volontaire et non certifiable. Il n'existe pas d'audit tiers officiel comme pour l'ISO 27001. Son utilisation est une démarche d'auto-évaluation et d'amélioration.

Comment le NIST CSF se positionne-t-il par rapport à l'ISO 27001 ? :: Les deux sont complémentaires. Le NIST CSF est plus flexible et stratégique (adapté à la communication avec la direction). L'ISO 27001 est normative et certifiable (plus opérationnelle). De nombreuses organisations utilisent les deux simultanément.

À quoi sert la fonction IDENTIFY dans le NIST CSF ? :: À comprendre le contexte de l'organisation : inventaire des actifs (matériels, logiciels, données), cartographie des dépendances, analyse des risques. C'est le prérequis à toutes les autres fonctions.

## Sources
- NIST Cybersecurity Framework 2.0 (février 2024) — nist.gov/cyberframework
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems
- CISA — NIST CSF Implementation Guide
- ENISA — Mapping NIS2 to NIST CSF
- Gartner — Market Guide for Security Risk and Compliance Frameworks, 2023

## Notions liées
- [[ISO 27001 - 27002]]
- [[NIS2]]
- [[PCA - PRA]]
- [[Authentification et gestion des accès (IAM)]]
- [[Outils de sécurité réseau]]
- [[ANSSI et acteurs de la cybersécurité]]
