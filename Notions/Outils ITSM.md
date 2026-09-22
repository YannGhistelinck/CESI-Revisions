---
type: notion
thèmes:
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Outils ITSM

![[N — Outils ITSM.mp3]]
## En bref

### Définition
Les **outils ITSM (IT Service Management)** sont des plateformes logicielles qui automatisent, centralisent et optimisent la gestion des services informatiques selon les référentiels ITIL/ITSM. Ils couvrent les processus clés : gestion des incidents, des problèmes, des changements, des actifs, des configurations (CMDB) et du catalogue de services.

Les trois leaders du marché sont :
- **ServiceNow** : plateforme cloud de gestion des workflows d'entreprise, leader mondial ITSM
- **Jira Service Management (Atlassian)** : outil orienté développeurs/DevOps, intégration native avec Jira Software
- **Outils de ticketing secondaires** : Freshservice, ManageEngine, Zendesk, TOPdesk, BMC Helix, iTop (open source)

### Pourquoi c'est important
Un outil ITSM bien configuré réduit le Mean Time To Repair (MTTR), améliore la satisfaction utilisateur, garantit la traçabilité des changements et produit les KPI nécessaires au pilotage de la qualité de service. C'est le système nerveux opérationnel de la DSI.

### Chiffres clés
- ServiceNow pèse plus de 8 Md$ de revenus annuels (2023) et est utilisé par 85 % des Fortune 500
- Jira Service Management compte plus de 45 000 clients dans 190 pays
- Le marché mondial des outils ITSM est estimé à 12 Md$ en 2024 (CAGR ~15 %)
- Les organisations utilisant un ITSM mature réduisent leur MTTR de 40 % en moyenne

---

## Approfondir

### Fonctionnement

**Modules fonctionnels communs des outils ITSM :**

| Module | Description |
|--------|-------------|
| Gestion des incidents | Enregistrement, catégorisation, priorisation, escalade, résolution |
| Gestion des problèmes | RCA, erreurs connues (KEDB), prévention des récurrences |
| Gestion des changements | CAB (Change Advisory Board), approbations, calendrier des changements |
| Catalogue de services | Self-service portal, formulaires de demande standardisés |
| CMDB | Base de données de configuration, cartographie des actifs IT |
| Gestion des niveaux de service | SLA, OLA, UC — alertes et reporting |
| Gestion des actifs | Inventaire, cycle de vie, licences |

**ServiceNow :**
- Architecture cloud SaaS multi-tenant
- Modules : ITSM, ITOM (opérations), ITAM (actifs), HRSD, SecOps, CSM
- Now Platform : low-code/no-code pour créer des workflows personnalisés
- Intégrations natives : Azure, AWS, Slack, Microsoft Teams
- IA intégrée : Now Assist (IA générative), prédiction des incidents
- Certification : ServiceNow CSA, CIS, CAD

**Jira Service Management (JSM) :**
- Issu de Jira Software (Atlassian) — adapté aux équipes DevOps
- Gestion des incidents en mode "alerte" (intégration Opsgenie)
- Portail client self-service configurable
- Assets (CMDB légère intégrée depuis 2021)
- Intégrations : Confluence, Bitbucket, GitHub, PagerDuty
- Avantage clé : pont naturel entre IT Ops et développement

**Comparaison ServiceNow vs JSM :**

| Critère | ServiceNow | Jira Service Management |
|---------|------------|------------------------|
| Cible principale | Grandes entreprises | PME / équipes DevOps |
| Complexité | Élevée (forte capacité de personnalisation) | Modérée (plus accessible) |
| Prix | Premium (licences utilisateurs nommés) | Freemium jusqu'à 3 agents |
| CMDB | Native et complète | Assets (moins mature) |
| Intégration Dev | Possible mais non native | Native (écosystème Atlassian) |
| IA | Now Assist (générative) | Atlassian Intelligence |

**Métriques clés pilotées par un ITSM :**
- **MTTR** (Mean Time To Repair) : temps moyen de résolution
- **MTTD** (Mean Time To Detect) : temps moyen de détection
- **FCR** (First Call Resolution Rate) : taux de résolution au premier contact
- **SLA compliance** : respect des engagements de niveau de service
- **Ticket volume trends** : évolution du volume par catégorie

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Centralisation et traçabilité totale des tickets | Coût de licence élevé (ServiceNow notamment) |
| Automatisation des workflows répétitifs | Complexité d'implémentation et de paramétrage |
| Reporting et KPI en temps réel | Risque de sur-configuration (processus trop lourds) |
| Self-service réduisant la charge N1 | Adoption utilisateur parfois difficile |
| Conformité ITIL out-of-the-box | Dépendance éditeur (vendor lock-in) |

### Acteurs
- **ServiceNow** : leader mondial ITSM enterprise
- **Atlassian (Jira Service Management)** : leader DevOps-friendly
- **BMC (Helix ITSM)** : historique, très présent en grande entreprise
- **Freshworks (Freshservice)** : alternative mid-market
- **ManageEngine (ServiceDesk Plus)** : alternative économique
- **iTop** : solution open source française (Combodo)
- **TOPdesk** : acteur européen, fort en secteur public

### Cas d'usage
- **Centre de services** : traitement automatisé des tickets N1 via portail self-service et chatbot IA (ServiceNow Virtual Agent)
- **Gestion des changements** : workflow d'approbation CAB automatisé dans ServiceNow pour les changements en production
- **Supervision et incidents** : intégration JSM + Opsgenie pour alerter les astreintes et déclencher les runbooks automatiquement
- **CMDB** : cartographie des dépendances applicatives pour évaluer l'impact d'un incident avant escalade

### Chiffres complémentaires
- Les organisations avec un self-service portal actif réduisent les tickets N1 de 30 % (Freshservice, 2023)
- Le ROI moyen de ServiceNow est estimé à 487 % sur 3 ans (Forrester TEI, 2023)

---

## Flashcards
#flashcards/Optimisation_du_SI/Outils_ITSM

Que signifie ITSM et quels sont ses processus clés ? :: IT Service Management — gestion des incidents, problèmes, changements, actifs, configurations (CMDB) et niveaux de service (SLA).

Quelle est la différence principale entre ServiceNow et Jira Service Management ? :: ServiceNow cible les grandes entreprises avec une plateforme complète et complexe ; JSM est orienté DevOps et PME avec une intégration native à l'écosystème Atlassian.

Qu'est-ce qu'une CMDB ? :: Configuration Management Database — base de données centralisant les actifs IT (CI : Configuration Items) et leurs dépendances, indispensable pour l'impact analysis.

Quelles sont les 4 métriques clés pilotées par un ITSM ? :: MTTR (résolution), MTTD (détection), FCR (résolution au premier contact), SLA compliance.

Qu'est-ce que le CAB dans la gestion des changements ITSM ? :: Change Advisory Board — comité qui évalue et approuve les changements planifiés pour minimiser le risque en production.

Citez trois outils ITSM alternatifs à ServiceNow et JSM. :: Freshservice, ManageEngine ServiceDesk Plus, iTop (open source français), TOPdesk, BMC Helix.

Quel est le bénéfice principal du self-service portal dans un ITSM ? :: Réduire le volume de tickets N1 en permettant aux utilisateurs de résoudre eux-mêmes leurs demandes courantes, libérant le centre de services pour les incidents complexes.

---

## Sources
- ServiceNow Annual Report 2023 — servicenow.com
- Atlassian, Jira Service Management documentation — atlassian.com
- Forrester Total Economic Impact, ServiceNow, 2023
- Gartner Magic Quadrant for IT Service Management Tools, 2023
- AXELOS, ITIL 4 Foundation, 2019

---

## Notions liées
- [[Amélioration continue (PDCA - Lean - Kaizen)]]
- [[VeriSM]]
- [[Observabilité]]
- [[DORA Metrics]]
- [[Orchestration et automatisation]]
- [[PCA - PRA]]
- [[DevOps]]
