---
type: notion
thèmes:
  - Cybersécurité
  - Mobilité
statut: pas vu
dernière_révision: 
---

# EDR - XDR - NDR

## En bref
> **Définition** : L'EDR (Endpoint Detection and Response) est une solution de sécurité installée sur les terminaux (postes, serveurs) pour détecter, analyser et répondre aux menaces en temps réel, via une analyse comportementale et une collecte télémétriques continue. Le XDR (Extended DR) étend cette visibilité à l'ensemble des couches du SI (endpoint, réseau, cloud, email, identité). Le NDR (Network Detection and Response) se concentre sur la détection des menaces dans le trafic réseau.
> **Pourquoi c'est important** : Les antivirus traditionnels basés sur des signatures sont inefficaces contre les malwares polymorphes, les attaques fileless et les APT. L'EDR/XDR/NDR permettent une détection comportementale, une réponse rapide et une capacité de forensique avancée, essentielles pour les équipes SOC modernes.
> **Chiffres clés** :
> - Le marché mondial de l'EDR était de 3,4 Md$ en 2023 et devrait atteindre 13,8 Md$ en 2032 (Precedence Research).
> - Les outils EDR/XDR réduisent le temps de détection des menaces avancées de 78 % par rapport aux antivirus traditionnels (Forrester Research).
> - 70 % des violations commencent par un endpoint compromis (Ponemon Institute).

## Approfondir

### Fonctionnement

**EDR (Endpoint Detection and Response)** :
Un agent léger est installé sur chaque endpoint (Windows, Linux, macOS, serveurs). Il collecte en continu la télémétrie système : processus créés, connexions réseau, accès au registre, création de fichiers, exécution de scripts. Cette télémétrie est analysée localement et dans le cloud par des moteurs IA/ML pour détecter des comportements anormaux.

Capacités clés :
- **Détection comportementale** : détecte les attaques sans signature connue (zero-day, fileless malware).
- **Threat hunting** : permet à un analyste SOC de chercher proactivement des IOC ou des TTP dans la télémétrie historique.
- **Réponse** : isolation de l'endpoint, kill process, suppression de fichier, rollback, tout depuis la console centralisée.
- **Forensique** : timeline d'attaque complète, mémoire RAM, artefacts système.

**NDR (Network Detection and Response)** :
Analyse le trafic réseau en temps réel (métadonnées de flux NetFlow, ou paquets complets avec DPI) pour détecter des comportements anormaux : communications avec des C2 (Command & Control), exfiltration de données, mouvements latéraux, protocoles anormaux. Basé sur des algorithmes ML et de l'analyse comportementale (pas de signatures). Avantage : détecte les menaces sur les appareils sans agent (IoT, OT, équipements réseau).

**XDR (Extended Detection and Response)** :
Évolution naturelle de l'EDR. Le XDR corrèle la télémétrie de multiples sources (endpoint, réseau, email, cloud, identité, applications) dans une plateforme unifiée pour offrir une vision globale de l'attaque. Élimine les angles morts des outils silotés.

Deux modèles :
- **Native XDR** : plateforme d'un seul éditeur couvrant toutes les couches (CrowdStrike, SentinelOne, Microsoft Defender XDR). Plus simple à déployer, moins flexible.
- **Open XDR (Hybrid XDR)** : agrège des données de outils tiers via des intégrations. Plus flexible, plus complexe.

**MITRE ATT&CK** : base de connaissances mondiale des tactiques, techniques et procédures (TTP) des attaquants. Les EDR/XDR modernes mappent leurs détections sur le framework ATT&CK pour permettre une évaluation de la couverture défensive et une communication standardisée entre équipes.

**Comparaison EDR / NDR / XDR** :
| Critère | EDR | NDR | XDR |
|---------|-----|-----|-----|
| Source de données | Endpoints | Réseau | Multi-sources |
| Couverture des appareils sans agent | Non | Oui | Partiel |
| Complexité | Modérée | Modérée | Élevée |
| Vision de l'attaque | Partielle | Partielle | Globale |
| Réponse | Endpoint | Réseau | Coordonnée |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection comportementale (zero-day, fileless) | Agent à déployer sur chaque endpoint (EDR) |
| Réponse rapide depuis la console centralisée | Coût élevé des licences commerciales |
| Forensique et threat hunting avancés | Volume de télémétrie important à gérer |
| XDR : vision unifiée cross-couches | XDR natif = dépendance à un seul éditeur |
| NDR : couverture des appareils sans agent (IoT, OT) | NDR : nécessite accès au trafic réseau (TAP/SPAN) |
| Intégration MITRE ATT&CK pour évaluation de couverture | Courbe d'apprentissage pour le threat hunting |

### Acteurs et solutions du marché

**EDR / XDR leaders** :
- **CrowdStrike Falcon** : leader Gartner MQ EPP 2024, architecture cloud-native, excellent threat hunting (Falcon OverWatch).
- **SentinelOne** : IA autonome, réponse automatique, forte croissance. XDR avec Singularity.
- **Microsoft Defender for Endpoint / XDR** : intégré à l'écosystème Microsoft 365, rapport qualité/prix excellent pour les environnements Windows.
- **Palo Alto Cortex XDR** : intégration avec XSOAR (SOAR), vision réseau et endpoint.
- **ESET Protect** : acteur européen, bon rapport qualité/prix pour les PME.
- **Harfanglab** : EDR français, certifié ANSSI, référencé pour les OIV/OSE. Alternative souveraine.

**NDR leaders** :
- **Darktrace** : pionnier de l'IA pour le NDR, détection comportementale autonome.
- **Vectra AI** : NDR spécialisé sur la détection des attaques post-compromission.
- **ExtraHop (Reveal(x))** : NDR enterprise, analyse du trafic chiffré.
- **Stamus Networks** : NDR open source (Suricata-based), acteur français.
- **Zeek (open source)** : analyseur de trafic réseau, base de nombreuses solutions NDR.

### Cas d'usage concrets

1. **Détection d'une attaque fileless (EDR)** : un attaquant exécute un payload PowerShell directement en mémoire, sans écrire de fichier sur le disque (fileless). L'antivirus ne détecte rien. L'EDR analyse le comportement du processus PowerShell (injection de code, connexion réseau vers un C2) et isole automatiquement l'endpoint en 45 secondes.

2. **Détection d'exfiltration via NDR** : le NDR détecte un volume anormal de données sortantes vers une IP externe inconnue à 3h du matin, via un protocole DNS encapsulé (DNS tunneling). Alerte immédiate, blocage du flux, investigation forensique sur l'endpoint source.

3. **Corrélation XDR — attaque multi-vecteurs** : email de phishing reçu (détecté par Defender for Office 365) → lien cliqué, payload téléchargé (EDR) → connexion à un C2 (NDR) → tentative de mouvement latéral (identité AD). Le XDR corrèle ces 4 événements de 4 sources différentes en un seul incident cohérent, avec la timeline d'attaque complète et la réponse coordonnée.

### Chiffres et tendances
- CrowdStrike évalue le "breakout time" moyen d'un attaquant (entre accès initial et mouvement latéral) à 62 minutes en 2023 — l'EDR doit répondre avant.
- Gartner (2024) : le XDR est la technologie de sécurité avec le plus fort ROI parmi les plateformes de détection.
- Le NDR est le seul outil capable de détecter les menaces sur les appareils IoT et OT non patchables.
- HarfangLab (EDR français) est l'une des rares solutions qualifiées ANSSI, requis pour certains OIV.
- Microsoft Defender XDR couvre nativement 5 vecteurs : endpoint, email, identité, cloud apps, données — représentant 85 % des cas d'usage XDR pour les environnements Microsoft.

## Flashcards
#flashcards
Qu'est-ce qu'un EDR et en quoi diffère-t-il d'un antivirus ? :: L'EDR collecte une télémétrie comportementale continue sur les endpoints et détecte les menaces par analyse comportementale/IA, sans dépendre de signatures. L'antivirus traditionnel compare les fichiers à une base de signatures connues, inefficace contre les zero-days et les attaques fileless.

Qu'est-ce qu'une attaque fileless et pourquoi est-elle difficile à détecter ? :: Attaque s'exécutant directement en mémoire RAM sans écrire de fichier sur le disque. Invisible aux antivirus basés sur les fichiers. Seule une analyse comportementale des processus (EDR) permet de la détecter.

Qu'est-ce que le XDR et quelle est sa valeur ajoutée par rapport à l'EDR ? :: Extended Detection and Response : corrèle la télémétrie de multiples sources (endpoint, réseau, email, cloud, identité) dans une plateforme unifiée. Élimine les angles morts des outils silotés et offre une vision globale de l'attaque.

Quelle est la différence entre XDR natif et Open XDR ? :: XDR natif : toutes les couches couvertes par un seul éditeur (plus simple, moins flexible). Open XDR : agrège des données de outils tiers via des intégrations (plus flexible, plus complexe à déployer).

Pourquoi le NDR est-il complémentaire à l'EDR ? :: Le NDR détecte les menaces dans le trafic réseau et couvre les appareils sans agent (IoT, OT, équipements réseau) invisibles à l'EDR. Il détecte notamment les mouvements latéraux, l'exfiltration et les communications C2.

Qu'est-ce que le framework MITRE ATT&CK et quel est son lien avec EDR/XDR ? :: Base de connaissances des tactiques, techniques et procédures (TTP) des attaquants. Les EDR/XDR mappent leurs détections sur ce framework pour évaluer leur couverture défensive et standardiser la communication entre équipes.

Qu'est-ce que HarfangLab et pourquoi est-il stratégique en France ? :: EDR français certifié ANSSI, alternative souveraine aux acteurs américains (CrowdStrike, SentinelOne). Requis ou fortement recommandé pour les OIV et OSE soumis aux réglementations de souveraineté des données.

## Sources
- ANSSI — Qualification et certification de solutions de sécurité — www.ssi.gouv.fr
- MITRE ATT&CK Framework — attack.mitre.org
- Gartner — Magic Quadrant for Endpoint Protection Platforms 2024
- CrowdStrike — Global Threat Report 2024 — www.crowdstrike.com
- Forrester — The Total Economic Impact of CrowdStrike Falcon
- Darktrace — www.darktrace.com
- HarfangLab — www.harfanglab.io

## Notions liées
- [[SIEM]]
- [[SOAR]]
- [[Menaces cyber]]
- [[Zero Trust]]
- [[Cyber-résilience]]
- [[Défense en profondeur]]
