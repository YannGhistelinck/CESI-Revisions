---
type: notion
thèmes:
  - Cybersécurité
  - IA
statut: pas vu
dernière_révision: 
---

# Acteurs cybersécurité (éditeurs)

## En bref

### Définition
Le marché de la cybersécurité est structuré autour d'éditeurs spécialisés couvrant différents domaines : détection et réponse aux incidents (EDR/XDR), threat intelligence, sécurisation des emails, sensibilisation des utilisateurs et services managés (MSSP). On distingue les acteurs américains dominants, les acteurs français souverains et les intégrateurs/MSSP.

**Acteurs couverts :** Darktrace, CrowdStrike, SentinelOne, Sekoia.io, HarfangLab, KnowBe4, Cofense, Mailinblack, Orange Cyberdefense, Thales.

### Pourquoi c'est important
La connaissance des éditeurs et de leur positionnement est essentielle pour un RSSI ou DSI afin de choisir les solutions adaptées au contexte (souveraineté, budget, maturité), de comprendre les rapports de force du marché et de répondre aux enjeux de conformité (NIS2, RGPD).

### Chiffres clés
- Le marché mondial de la cybersécurité dépasse 190 Md$ en 2023 (Gartner)
- CrowdStrike pèse plus de 3 Md$ de revenus annuels (2023)
- La France compte 4 licornes cyber : Sekoia.io, HarfangLab, Tehtris, Anozr Way
- 95 % des violations de données impliquent une erreur humaine (Verizon DBIR 2023) — d'où l'importance de KnowBe4/Cofense

---

## Approfondir

### Fonctionnement

#### Détection et réponse aux menaces avancées (EDR/XDR/NDR)

**Darktrace (Royaume-Uni, fondée 2013)**
- Spécialité : IA comportementale (Cyber AI) pour la détection d'anomalies en temps réel
- Produits : Enterprise Immune System (NDR), DETECT/RESPOND, Email Security, OT Security
- Approche : modélisation du comportement "normal" de chaque entité (utilisateur, appareil, réseau) — détection par déviation
- Clients : 9 000+ organisations dans 110 pays
- Points forts : détection de menaces inconnues (zero-day, insider threats)
- Points faibles : taux de faux positifs, coût élevé, boîte noire algorithmique

**CrowdStrike (USA, fondée 2011)**
- Spécialité : EDR/XDR cloud-native — Falcon Platform
- Produits : Falcon Prevent (antivirus NG), Falcon Insight (EDR), Falcon X (Threat Intelligence), Falcon OverWatch (MDR)
- Architecture : agent léger + analyse cloud (Threat Graph) — corrélation de milliards d'événements
- Falcon Complete : MDR managé 24/7
- Points forts : performance, Threat Intelligence de référence mondiale, MITRE ATT&CK leader
- Points faibles : incident juillet 2024 (mise à jour défectueuse → 8,5 millions de BSOD Windows)

**SentinelOne (USA, fondée 2013)**
- Spécialité : EDR/XDR autonome avec IA — Singularity Platform
- Produits : Singularity Endpoint, Singularity Cloud (CNAPP), Singularity Data Lake (SIEM)
- Différenciateur : réponse autonome (sans intervention humaine) — Storyline™ pour la corrélation d'attaques
- Acquisition de Attivo Networks (Identity Security) en 2022
- Points forts : automatisation de la réponse, couverture cloud/endpoint/identité
- Points faibles : maturité SOAR moins développée que CrowdStrike

#### Acteurs souverains français

**Sekoia.io (France, fondée 2018)**
- Spécialité : CTI (Cyber Threat Intelligence) + SIEM/SOAR — plateforme SOC cloud-native
- Produit phare : Sekoia.io XDR/SOC Platform
- Labellisée SecNumCloud (ANSSI) — souveraineté française garantie
- Intègre 700+ feeds de Threat Intelligence et des playbooks automatisés
- Clients : SOC internes de grandes entreprises françaises, OIV, administrations
- Points forts : souveraineté, CTI de qualité, conformité réglementaire

**HarfangLab (France, fondée 2018)**
- Spécialité : EDR souverain — solution open source partielle
- Produit phare : Hurukai (EDR)
- Certifié CSPN par l'ANSSI (Certification de Sécurité de Premier Niveau)
- Retenu dans le cadre du plan cyber gouvernemental
- Points forts : souveraineté, transparence du code, audit possible, déploiement on-premise
- Points faibles : écosystème intégrations plus limité que CrowdStrike/SentinelOne

#### Sensibilisation et sécurité email

**KnowBe4 (USA, fondée 2010)**
- Spécialité : Security Awareness Training (SAT) + simulations de phishing
- Plus grande plateforme mondiale de formation à la cybersécurité : 65 000+ clients
- Produits : plateforme de phishing simulé, formations gamifiées, PhishER (analyse des emails signalés)
- Acquisition par Vista Equity Partners (2023, 4,6 Md$)
- Points forts : vaste bibliothèque de contenus, reporting détaillé, intégration Microsoft 365/Google Workspace

**Cofense (USA, fondée 2008)**
- Spécialité : protection contre le phishing — simulation + réponse aux incidents email
- Produits : Cofense PhishMe (simulation), Cofense Triage (analyse), Cofense Intelligence (CTI email)
- Réseau de reporters humains : 35 millions d'utilisateurs entraînés
- Points forts : Threat Intelligence email basée sur comportements réels, intégration SIEM/SOAR

**Mailinblack (France, fondée 2003)**
- Spécialité : protection des messageries professionnelles + sensibilisation
- Produits : Mailinblack Protect (filtrage email IA), Mailinblack Cyber Coach (sensibilisation)
- Solution souveraine française, hébergée en France
- Clients : 15 000+ organisations, fort dans les PME et secteur public français
- Points forts : souveraineté, simplicité de déploiement, prix compétitif vs alternatives US

#### Intégrateurs / MSSP français

**Orange Cyberdefense**
- Filiale cybersécurité d'Orange, leader MSSP européen
- Services : SOC managé 24/7, threat intelligence (CERT-OCD), tests d'intrusion, réponse à incident, formation
- Présence : 18 pays, 3 000+ experts cyber
- Centre opérationnel : CyberSOC, EclecticIQ (CTI), Managed Detection & Response
- Points forts : couverture mondiale, souveraineté française, portefeuille de services complet

**Thales (France)**
- Division Cyber : Thales Group — Cybersecurity Products & Services
- Produits : HSM (Hardware Security Modules), Ciphertrust (chiffrement), SOC managé, identité numérique
- Contexte : acteur de défense nationale — contrats OIV, OTAN, secteur aérospatial et défense
- Certifications : évaluations CSPN, agréments IGC (Infrastructure de Gestion des Clés)
- Points forts : ancrage national/défense, maîtrise hardware-to-software, souveraineté maximale

### Avantages / Inconvénients

| Acteur | Points forts | Points faibles |
|--------|-------------|----------------|
| Darktrace | IA comportementale, menaces inconnues | Boîte noire, faux positifs |
| CrowdStrike | Threat Intel leader, cloud-native | Incident 2024, coût élevé |
| SentinelOne | Réponse autonome, couverture cloud | SOAR moins mature |
| Sekoia.io | Souveraineté, CTI, SecNumCloud | Notoriété internationale limitée |
| HarfangLab | Souveraineté, CSPN, transparence | Écosystème intégrations restreint |
| KnowBe4 | Phishing simulation, 65k clients | Américain, pas souverain |
| Cofense | CTI email, réseau reporters | Spécialisé email uniquement |
| Mailinblack | Souverain, PME, prix | Périmètre limité à l'email |
| Orange Cyberdefense | MSSP complet, présence EU | Moins outillé vs pure players |
| Thales | Défense, HSM, souveraineté max | Moins accessible PME |

### Cas d'usage
- **OIV / OSE** : HarfangLab EDR + Sekoia.io SIEM/SOC + Thales HSM → stack souveraine conforme NIS2
- **Grand groupe international** : CrowdStrike Falcon + SentinelOne Cloud + KnowBe4 → protection endpoints + sensibilisation
- **PME** : Mailinblack Protect + formation KnowBe4 → premier niveau de protection email accessible
- **SOC interne** : Sekoia.io plateforme + Orange Cyberdefense MDR → hybride interne/externalisé

---

## Flashcards
#flashcards

Quelle est la spécialité de Darktrace et comment fonctionne son IA ? :: IA comportementale (Cyber AI) qui modélise le comportement "normal" de chaque entité réseau et détecte toute déviation — permet de détecter des menaces inconnues (zero-day).

Quelle est la différence entre CrowdStrike et SentinelOne ? :: CrowdStrike s'appuie sur une Threat Intelligence cloud massive (Threat Graph) ; SentinelOne se différencie par sa réponse autonome sans intervention humaine (Storyline™).

Quels sont les deux EDR souverains français certifiés ANSSI ? :: HarfangLab (CSPN) et Sekoia.io (SecNumCloud) — tous deux labellisés par l'ANSSI.

Quelle est la différence entre KnowBe4 et Cofense ? :: KnowBe4 est la plus grande plateforme de security awareness training ; Cofense se spécialise dans la réponse aux incidents de phishing email avec un réseau de 35 millions de reporters.

Quel est le positionnement de Mailinblack sur le marché ? :: Solution française souveraine de protection des messageries (filtrage IA) et de sensibilisation, ciblant les PME et le secteur public avec un prix compétitif.

Qu'est-ce qu'un MSSP et citez deux exemples français. :: Managed Security Service Provider — prestataire gérant la sécurité pour le compte de ses clients ; exemples : Orange Cyberdefense, Thales.

Pourquoi l'incident CrowdStrike de juillet 2024 est-il emblématique ? :: Une mise à jour défectueuse de l'agent Falcon a provoqué 8,5 millions de BSOD Windows simultanément, illustrant les risques de concentration et de mise à jour automatique des solutions de sécurité.

---

## Sources
- Gartner Magic Quadrant for Endpoint Protection Platforms, 2023
- Verizon Data Breach Investigations Report (DBIR), 2023
- ANSSI — annuaire des produits certifiés — ssi.gouv.fr
- CrowdStrike Annual Report 2023
- SentinelOne S-1, 2021
- Sekoia.io — sekoia.io
- HarfangLab — harfanglab.io
- Orange Cyberdefense Annual Report 2023

---

## Notions liées
- [[EDR - XDR - NDR]]
- [[SIEM]]
- [[SOAR]]
- [[SOC]]
- [[Threat Intelligence et Threat Hunting]]
- [[IA en cybersécurité]]
- [[Sensibilisation et facteur humain]]
- [[NIS2]]
- [[Ingénierie sociale]]
