---
type: notion
thèmes:
  - Cybersécurité
  - IA
statut: pas vu
dernière_révision: 
---

# Threat Intelligence et Threat Hunting

![[N — Threat Intelligence et Threat Hunting.mp3]]
## En bref
> **Définition** : La Cyber Threat Intelligence (CTI) est le processus de collecte, d'analyse et de partage d'informations sur les menaces cyber afin d'anticiper et de contrer les attaques. Le Threat Hunting est une démarche proactive consistant à rechercher activement des compromissions au sein d'un SI, sans attendre qu'une alerte soit levée.
> **Pourquoi c'est important** : Dans un contexte où les attaquants opèrent en moyenne plusieurs mois avant d'être détectés, la CTI et le Threat Hunting permettent aux DSI de passer d'une posture réactive à une posture proactive, réduisant significativement le temps de détection et limitant l'impact des incidents.
> **Chiffres clés** :
> - Temps moyen de détection d'une intrusion (dwell time) : 16 jours en 2023, contre 24 jours en 2022 (Mandiant M-Trends 2024).
> - 60 % des organisations ayant une équipe de Threat Hunting déclarent détecter des menaces que les outils automatisés avaient manquées (SANS Institute, 2023).
> - Le marché mondial de la CTI est estimé à 18,1 milliards de dollars en 2028, avec un CAGR de 19,5 % (MarketsandMarkets, 2023).

## Approfondir

### Fonctionnement

**Cyber Threat Intelligence (CTI)**

La CTI s'organise autour de quatre niveaux de renseignement :
- **Stratégique** : informations à destination des décideurs (tendances géopolitiques, motivations des groupes d'attaquants).
- **Opérationnel** : informations sur les campagnes d'attaques en cours (TTP utilisées, cibles visées).
- **Tactique** : indicateurs de compromission (IoC) concrets : adresses IP malveillantes, hashes de fichiers, domaines C2, URLs.
- **Technique** : détails fins sur les exploits, les variantes de malwares, les signatures.

Le cycle de production de la CTI suit cinq étapes : **Collecte → Traitement → Analyse → Diffusion → Feedback**. Les sources sont variées : OSINT (forums, dark web, réseaux sociaux), ISAC (Information Sharing and Analysis Centers), partenaires, honeypots, logs internes.

**Indicateurs de Compromission (IoC)**

Les IoC sont des artefacts observables trahissant une compromission : adresses IP, URLs, hashes MD5/SHA-256, noms de domaines, clés de registre Windows, mutex. Ils sont partagés via des formats standardisés : **STIX** (Structured Threat Information Expression) et **TAXII** (Trusted Automated Exchange of Intelligence Information).

**TTP et MITRE ATT&CK**

Les TTP (Tactics, Techniques and Procedures) décrivent le comportement des attaquants avec un niveau d'abstraction plus élevé que les IoC, et sont beaucoup plus durables (un attaquant change d'IP facilement, mais pas de TTP). Le framework **MITRE ATT&CK** recense plus de 400 techniques réparties en 14 tactiques (Reconnaissance, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command & Control, Exfiltration, Impact). Il est utilisé pour mapper les attaques détectées, identifier les angles morts de détection et prioriser les investissements défensifs.

**Threat Hunting**

Le Threat Hunting est un processus itératif :
1. **Hypothèse** : formulée à partir d'IoC, de TTP, ou d'intuition de l'analyste.
2. **Investigation** : requêtes sur les logs, EDR, SIEM, forensics mémoire.
3. **Découverte** : identification de comportements anormaux.
4. **Réponse** : remediation et enrichissement des règles de détection.

Les hunts peuvent être déclenchés par une alerte CTI (un nouveau groupe APT cible le secteur), ou être opportunistes (revue périodique des anomalies). Les outils principaux : **SIEM** (Splunk, Microsoft Sentinel), **EDR** (CrowdStrike Falcon, SentinelOne), **threat hunting platforms** (Recorded Future, ThreatConnect).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection de menaces avancées non couvertes par les outils automatisés | Nécessite des analystes très qualifiés (pénurie de compétences) |
| Réduction du dwell time et donc de l'impact des attaques | Coût élevé (licences, ressources humaines) |
| Enrichissement continu des règles SIEM/EDR | Risque de faux positifs générant des investigations inutiles |
| Meilleure compréhension du profil de risque de l'organisation | Difficile à justifier sans métriques claires (ROI non immédiat) |
| Partage d'intelligence inter-organisations via ISAC | La CTI externe peut être de qualité variable ou obsolète |
| Posture proactive vs réactive | Le Threat Hunting artisanal n'est pas scalable sans automatisation |

### Acteurs et solutions du marché

**Plateformes CTI**
- **Recorded Future** : leader du marché, CTI temps réel enrichie par IA.
- **Mandiant Threat Intelligence** (Google) : référence sur les APT, analyses approfondies.
- **MISP** (Malware Information Sharing Platform) : solution open source très répandue pour le partage de CTI.
- **OpenCTI** : plateforme open source française (Filigran), structuration et visualisation de la CTI.
- **ThreatConnect** : intégration CTI + orchestration SOAR.
- **Anomali** : corrélation CTI avec les logs internes.

**Threat Hunting**
- **CrowdStrike Falcon Overwatch** : service de Threat Hunting managé.
- **Microsoft Defender XDR / Sentinel** : hunting via KQL (Kusto Query Language).
- **Elastic SIEM** : hunting open source avec capacités ML.
- **Velociraptor** : outil open source de forensics et hunting sur endpoint.

**Communautés et partage**
- **FIRST** (Forum of Incident Response and Security Teams) : réseau international de CERT/CSIRT.
- **FS-ISAC**, **H-ISAC** : partage sectoriel (finance, santé).
- **ANSSI** : publications TLP (Traffic Light Protocol) sur les menaces françaises.

### Cas d'usage concrets

**1. Détection d'une campagne APT via CTI (secteur énergie)**
En 2021, lors de la campagne APT41 ciblant les opérateurs d'infrastructures critiques, plusieurs ISAC du secteur énergie ont diffusé des IoC (hashes de malwares, IPs de C2) via MISP. Les équipes SOC abonnées ont pu créer des règles de détection et bloquer les tentatives d'intrusion en moins de 24h après la publication du bulletin.

**2. Threat Hunting post-incident SolarWinds**
Après la découverte du backdoor SUNBURST fin 2020, les équipes de hunting ont recherché dans les logs de connexions SAML les indicateurs comportementaux décrits par Microsoft et FireEye (rotation de tokens, connexions depuis des IPs d'hébergeurs inhabituels). Des organisations non directement compromises ont ainsi découvert des mouvements latéraux préalables.

**3. Hunting proactif sur Kerberoasting**
Une équipe de Threat Hunting formule l'hypothèse qu'un attaquant tente du Kerberoasting (technique MITRE ATT&CK T1558.003). Elle requête l'Active Directory pour identifier les comptes de service avec SPN, croise avec les logs d'événements Kerberos (ID 4769) pour détecter des demandes de tickets TGS en masse depuis un seul compte. Découverte d'un compte compromis en mouvement latéral.

### Chiffres et tendances
- Le nombre de nouveaux groupes APT trackés par Mandiant est passé de 900 à plus de 1 100 entre 2022 et 2023.
- 74 % des incidents impliquent un élément humain (phishing, abus de credentials) — IoC comportementaux > IoC techniques (Verizon DBIR 2024).
- MITRE ATT&CK est utilisé par plus de 90 % des équipes SOC avancées comme référentiel de détection.
- L'automatisation de la CTI via IA (LLM pour analyse de rapports, clustering de malwares) réduit de 40 % le temps d'analyse manuelle selon Gartner (2023).
- Le Threat Hunting managé (MDR incluant hunting) connaît une croissance de 25 % par an.

## Flashcards
#flashcards/Cybersécurité/Threat_Intelligence_et_Threat_Hunting #flashcards/IA/Threat_Intelligence_et_Threat_Hunting

Qu'est-ce qu'un IoC (Indicator of Compromise) ? :: Un artefact observable indiquant qu'un système a été compromis : hash de fichier, adresse IP malveillante, nom de domaine, clé de registre. Les IoC sont de courte durée de vie car les attaquants les changent facilement.

Quelle est la différence entre IoC et TTP ? :: Les IoC sont des indicateurs techniques précis (IP, hash) qui peuvent être changés rapidement par l'attaquant. Les TTP décrivent le comportement de l'attaquant (comment il opère) et sont beaucoup plus durables et pertinents pour la détection à long terme.

Qu'est-ce que le framework MITRE ATT&CK ? :: Une base de connaissance collaborative recensant les tactiques, techniques et procédures (TTP) des attaquants réels, organisées en 14 tactiques et plus de 400 techniques. Utilisée pour la détection, la chasse aux menaces et l'évaluation des contrôles de sécurité.

Quelles sont les 4 niveaux de CTI ? :: Stratégique (décideurs, tendances), Opérationnel (campagnes en cours), Tactique (IoC concrets), Technique (détails exploits/malwares).

Qu'est-ce que le dwell time ? :: Le temps moyen entre la compromission initiale d'un système et sa détection. En 2023, il est de 16 jours selon Mandiant. Le Threat Hunting vise à le réduire.

Quel est le format standard d'échange de CTI ? :: STIX (format de données) et TAXII (protocole de transport) sont les standards ouverts. MISP est la plateforme open source la plus utilisée pour partager ces données entre organisations.

Quelle est la différence entre Threat Intelligence et Threat Hunting ? :: La CTI est la collecte et l'analyse de renseignements sur les menaces (externe/interne). Le Threat Hunting est la recherche active de compromissions dans le SI, souvent alimentée par la CTI. La CTI informe, le Threat Hunting agit.

## Sources
- Mandiant M-Trends Report 2024
- MITRE ATT&CK Framework — https://attack.mitre.org
- SANS Institute — Threat Hunting Survey 2023
- OpenCTI (Filigran) — https://www.opencti.io
- MISP Project — https://www.misp-project.org
- Verizon Data Breach Investigations Report (DBIR) 2024
- ANSSI — Rapports de menaces et bulletins TLP

## Notions liées
- [[SOC]]
- [[Forensics]]
- [[IA en cybersécurité]]
- [[Red Team - Blue Team - Purple Team]]
- [[EBIOS RM et gestion des risques cyber]]
- [[Métriques de sécurité]]
