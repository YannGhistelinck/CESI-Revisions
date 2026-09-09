---
type: notion
thèmes:
  - Cybersécurité
  - IA
statut: pas vu
dernière_révision: 
---

# SOC

## En bref
> **Définition** : Un Security Operations Center (SOC) est une équipe centralisée — appuyée par des outils technologiques — dont la mission est de surveiller en continu le SI d'une organisation, détecter les incidents de sécurité, y répondre et améliorer la posture de sécurité. Il constitue le centre névralgique opérationnel de la cybersécurité d'une organisation.
> **Pourquoi c'est important** : Face à la sophistication croissante des attaques et aux exigences réglementaires (NIS2, DORA, LPM), disposer d'une capacité de détection et de réponse 24/7 est devenu incontournable pour les DSI. Le SOC est la réponse organisationnelle et technique à cet impératif.
> **Chiffres clés** :
> - 74 % des grandes entreprises françaises disposent d'un SOC ou d'un service MDR en 2024 (CESIN Baromètre 2024).
> - Le temps moyen de détection d'un incident sans SOC dédié est de 197 jours, contre 16 jours avec un SOC mature (IBM Cost of a Data Breach 2023 / Mandiant 2024).
> - Le marché mondial des SOC as a Service croît de 22 % par an et atteindra 11 milliards de dollars en 2027 (MarketsandMarkets).

## Approfondir

### Fonctionnement

**Les modèles de SOC**

- **SOC interne (In-house)** : équipe appartenant à l'organisation, opérée 24/7, totalement dédiée au SI de l'entreprise. Offre le meilleur niveau de personnalisation et de contexte métier, mais coûteux (masse salariale, outils, infrastructure).
- **SOC externalisé (MSSP — Managed Security Service Provider)** : le prestataire fournit la surveillance, les outils et les analystes. Modèle mutualisé, adapté aux organisations ne pouvant pas financer un SOC interne.
- **SOC hybride** : l'organisation conserve une équipe interne (L2/L3, expertise métier) et délègue la surveillance 24/7 au MSSP. Compromis courant.
- **MDR (Managed Detection and Response)** : évolution du MSSP, avec une capacité de réponse active (containment d'endpoints, isolation réseau) et du Threat Hunting intégré. Distinction clé : le MDR agit, le MSSP classique alerte.
- **SOC virtuel** : pas de locaux physiques dédiés, les analystes travaillent à distance, souvent associé à des outils cloud-native.

**Les niveaux d'analystes**

- **L1 (Tier 1 — Triage)** : surveille les alertes du SIEM, qualifie les faux positifs, escalade les incidents confirmés. Volume élevé, temps de traitement court (quelques minutes par alerte).
- **L2 (Tier 2 — Investigation)** : investigation approfondie des incidents escaladés par L1, corrélation de logs, analyse forensique de premier niveau, confinement.
- **L3 (Tier 3 — Expert/Threat Hunter)** : gestion des incidents complexes, Threat Hunting proactif, rétro-ingénierie de malwares, amélioration des règles de détection.
- **SOC Manager / CISO** : pilotage stratégique, reportings, relations avec la direction et les régulateurs.

**Les outils clés du SOC**

- **SIEM** (Security Information and Event Management) : agrégation et corrélation de logs (Splunk, Microsoft Sentinel, IBM QRadar, Elastic SIEM). Cœur de la détection.
- **SOAR** (Security Orchestration, Automation and Response) : automatisation des réponses et orchestration des playbooks (Palo Alto XSOAR, Splunk SOAR, Microsoft Sentinel Logic Apps). Réduit le temps de réponse et la fatigue d'alerte.
- **EDR/XDR** : visibilité et réponse sur les endpoints, puis l'ensemble du SI (CrowdStrike Falcon, SentinelOne, Microsoft Defender XDR).
- **Threat Intelligence Platform** : enrichissement des alertes avec du contexte (MISP, Recorded Future, ThreatConnect).
- **Ticketing** : gestion des incidents (ServiceNow, Jira, TheHive).

**CSIRT / CERT**

Le CSIRT (Computer Security Incident Response Team) ou CERT est une équipe spécialisée dans la réponse aux incidents, complémentaire ou intégrée au SOC. Le SOC détecte et surveille en continu ; le CSIRT/CERT intervient lors d'incidents avérés avec un mandat plus large (coordination, communication de crise, publication d'alertes). En France, l'ANSSI coordonne le réseau des CERT nationaux. Les entreprises du CAC40 disposent généralement d'un CERT privé.

**Le processus SOC (cycle de vie d'un incident)**

1. **Collecte des logs** : endpoints, réseau, applications, cloud, AD...
2. **Détection** : règles SIEM, alertes EDR, détection comportementale (UEBA).
3. **Triage (L1)** : qualification, faux positif ou vrai positif ?
4. **Investigation (L2)** : analyse de la cause racine, étendue de la compromission.
5. **Confinement** : isolation du poste/compte compromis, blocage IP.
6. **Eradication** : suppression du malware, correction de la vulnérabilité.
7. **Restauration** : remise en production sécurisée.
8. **Post-mortem** : retour d'expérience, amélioration des règles.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Surveillance continue 24/7 du SI | Coût élevé d'un SOC interne mature (1-5 M€/an) |
| Réduction du temps de détection et de réponse | Pénurie d'analystes qualifiés sur le marché |
| Conformité réglementaire (NIS2, LPM, DORA) | Fatigue d'alerte des analystes (burn-out, turnover élevé) |
| Centralisation de la visibilité sur l'ensemble du SI | Risque de dépendance vis-à-vis d'un MSSP |
| Amélioration continue via les retours d'expérience | Le SOC externalisé a moins de contexte métier |
| Le MDR offre une réponse active (vs simple alerting) | Complexité d'intégration des sources de logs hétérogènes |

### Acteurs et solutions du marché

**SIEM**
- **Microsoft Sentinel** : leader croissance, natif cloud Azure, connecteurs étendus.
- **Splunk Enterprise Security** : référence on-premise et hybride, très répandu.
- **IBM QRadar** : historiquement présent dans les grandes entreprises.
- **Elastic SIEM** : open source, très personnalisable.

**SOAR**
- **Palo Alto XSOAR** : leader du marché SOAR autonome.
- **Splunk SOAR** (ex-Phantom).
- **Microsoft Sentinel** : intègre une couche SOAR via Logic Apps/Playbooks.

**MDR / MSSP**
- **CrowdStrike Falcon Complete** : MDR avec réponse active.
- **SentinelOne Vigilance** : MDR s'appuyant sur l'IA.
- **Sophos MDR**, **Arctic Wolf**, **Atos/Eviden**, **Thales** : acteurs européens.
- **Orange Cyberdefense** : leader français des MSSP.

### Cas d'usage concrets

**1. SOC hybride dans un groupe industriel (secteur énergie)**
Un groupe énergétique français dispose d'une équipe interne de 5 personnes (L2/L3, CERT) et externalise la surveillance 24/7 à Orange Cyberdefense (MSSP). Microsoft Sentinel est le SIEM central. En cas d'alerte critique, le MSSP confinement l'endpoint via l'EDR et notifie le CERT interne dans les 15 minutes. Ce modèle respecte les obligations LPM/NIS2 pour les OIV.

**2. Création d'un SOC interne dans une banque (NIS2/DORA)**
Suite à l'entrée en vigueur de DORA, une banque régionale monte un SOC interne de 8 analystes. Elle adopte Microsoft Sentinel, intègre ses 1 200 sources de logs (Active Directory, Azure, PAN-OS, Oracle), et automatise 60 % du triage L1 via des playbooks SOAR. Le MTTD passe de 72h à 4h en 6 mois.

**3. MDR pour une PME industrielle (secteur manufacturing)**
Une PME de 500 salariés, victime d'un ransomware en 2022, souscrit à un service MDR (SentinelOne Vigilance). Le MDR détecte en 3 minutes une tentative de Kerberoasting, isole le poste concerné automatiquement, et alerte l'IT. La PME bénéficie d'une capacité SOC 24/7 pour ~3 000 €/mois, sans recruter d'analyste dédié.

### Chiffres et tendances
- La fatigue d'alerte est citée comme problème n°1 par 65 % des analystes SOC (Enterprise Strategy Group, 2023). Un analyste L1 traite en moyenne 4 500 alertes par semaine.
- L'automatisation SOAR réduit le temps de réponse moyen de 52 % (IBM Security, 2023).
- Le taux de turnover dans les équipes SOC atteint 30-40 % par an, alimentant la pénurie.
- NIS2 (transposée en France en 2024) impose des capacités de détection/réponse à ~15 000 entités supplémentaires.
- L'IA générative commence à être intégrée dans les SIEM (Microsoft Copilot for Security, CrowdStrike Charlotte AI) pour aider les analystes L1 dans leur triage.

## Flashcards
#flashcards/Cybersécurité/SOC #flashcards/IA/SOC

Quelle est la différence entre un MSSP et un MDR ? :: Le MSSP (Managed Security Service Provider) surveille et alerte. Le MDR (Managed Detection and Response) va plus loin : il répond activement (isolation d'endpoint, confinement réseau) et inclut du Threat Hunting. Le MDR est une évolution du MSSP vers plus d'autonomie et de proactivité.

Quels sont les 3 niveaux d'analystes SOC et leurs rôles ? :: L1 = triage des alertes, qualification faux positifs / vrais positifs. L2 = investigation approfondie, corrélation, confinement. L3 = incidents complexes, Threat Hunting, rétro-ingénierie, amélioration des règles de détection.

Quelle est la différence entre un SOC et un CSIRT/CERT ? :: Le SOC surveille en continu et gère les alertes au quotidien. Le CSIRT/CERT intervient sur les incidents majeurs avec un rôle élargi : coordination, communication de crise, publication d'alertes. Un CERT peut aussi avoir un rôle national (CERT-FR de l'ANSSI).

Qu'est-ce que la fatigue d'alerte et comment y remédier ? :: La fatigue d'alerte est l'épuisement des analystes face au volume trop élevé d'alertes (majoritairement faux positifs). Remèdes : SOAR (automatisation du triage), ML pour la priorisation, amélioration des règles de détection, métriques de qualité des alertes.

Qu'est-ce qu'un SOAR et en quoi diffère-t-il d'un SIEM ? :: Le SIEM collecte et corrèle les logs pour détecter. Le SOAR orchestre et automatise la réponse (playbooks). Exemples : alerte SIEM → playbook SOAR qui isole automatiquement l'IP, crée un ticket, notifie l'analyste. Les deux sont complémentaires.

Quelles obligations réglementaires justifient un SOC en France ? :: NIS2 (directive européenne, imposant des capacités de détection/réponse pour ~15 000 entités), DORA (secteur financier, exigences de résilience opérationnelle), LPM (Loi de Programmation Militaire pour les OIV/OES). L'ANSSI peut imposer des audits et qualifications.

Quel est l'impact d'un SOC sur le coût d'un incident ? :: Selon IBM (2023), les organisations avec un SOC mature réduisent le coût moyen d'une violation de données de 1,49 M$ (de 4,45 M$ à 2,96 M$). Le temps de confinement est divisé par 5 en moyenne.

## Sources
- IBM Cost of a Data Breach Report 2023
- CESIN Baromètre de la cybersécurité 2024
- Mandiant M-Trends 2024
- ANSSI — Guide d'hygiène informatique et recommandations SOC
- Enterprise Strategy Group — SOC Analyst Experience Survey 2023
- Gartner Magic Quadrant for Security Information and Event Management 2023
- MarketsandMarkets — SOC as a Service Market Report 2023

## Notions liées
- [[Threat Intelligence et Threat Hunting]]
- [[Forensics]]
- [[IA en cybersécurité]]
- [[Métriques de sécurité]]
- [[Red Team - Blue Team - Purple Team]]
- [[EBIOS RM et gestion des risques cyber]]
