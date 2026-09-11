---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Red Team - Blue Team - Purple Team

## En bref
> **Définition** : La Red Team simule des attaquants réels pour tester les défenses d'une organisation en conditions réalistes. La Blue Team est l'équipe défensive qui surveille, détecte et répond aux attaques. La Purple Team est un mode collaboratif où Red et Blue travaillent ensemble pour améliorer simultanément les capacités offensives et défensives, maximisant les apprentissages.
> **Pourquoi c'est important** : Un test de sécurité purement théorique ou limité à des scans de vulnérabilités ne valide pas la capacité réelle à détecter et répondre à une attaque sophistiquée. Les exercices Red/Blue/Purple permettent aux DSI de valider leurs investissements sécurité en conditions proches du réel et d'identifier leurs angles morts.
> **Chiffres clés** :
> - 56 % des organisations n'ont découvert des lacunes critiques dans leurs défenses qu'à l'occasion d'un exercice Red Team (Cymulate, 2023).
> - Le marché mondial du pentest et des services Red Team croît de 13,7 % par an et atteindra 4,5 milliards de dollars en 2027 (Grand View Research).
> - En moyenne, une Red Team professionnelle accède aux systèmes critiques dans 75 % des engagements (Rapid7 Pentesting Report, 2023).

## Approfondir

### Fonctionnement

**Red Team**

La Red Team est une équipe d'attaquants éthiques dont la mission est de simuler une menace avancée persistante (APT) ou un attaquant ciblé, en cherchant à atteindre un objectif défini (accéder à la base de données clients, exfiltrer des données sensibles, compromettre le contrôleur de domaine) sans que la Blue Team soit prévenue. Cela se distingue du pentest classique :

- **Pentest (test de pénétration)** : périmètre défini, objectif de trouver des vulnérabilités techniques, durée courte (1-2 semaines), rapport de vulnérabilités. Souvent White Box (avec documentation fournie) ou Grey Box.
- **Red Team engagement** : objectif métier (flag), périmètre ouvert, durée longue (4-12 semaines), techniques avancées (ingénierie sociale, phishing ciblé, exploitation de la chaîne d'approvisionnement), tests de la détection réelle.

Les phases d'un engagement Red Team suivent les étapes MITRE ATT&CK :
1. Reconnaissance (OSINT, cartographie de la surface d'attaque)
2. Initial Access (phishing, exploitation de services exposés)
3. Persistance et mouvement latéral
4. Accès aux objectifs (exfiltration, chiffrement)
5. Rapport et debriefing

**Blue Team**

La Blue Team englobe toutes les fonctions défensives : SOC, équipes réseau, administration système, réponse à incident. Elle ne sait pas qu'une Red Team est active (sauf dans certains scénarios). Son niveau de maturité est évalué sur sa capacité à détecter, contenir et éradiquer l'attaque simulée.

**Purple Team**

En mode Purple Team, Red et Blue collaborent en temps réel ou en sessions structurées :
- La Red Team exécute une technique (ex : Pass-the-Hash sur un contrôleur de domaine).
- La Blue Team vérifie si elle a généré une alerte dans le SIEM.
- Ensemble, ils analysent pourquoi la détection a fonctionné ou échoué et améliorent les règles immédiatement.

Ce mode est plus didactique et permet un transfert de compétences rapide. Il est moins réaliste (la Blue Team est prévenue) mais plus efficace pour l'amélioration continue.

**Tabletop Exercise (TTX)**

Exercice de simulation sur table (sans actions techniques réelles) : les participants discutent de la réponse à un scénario d'incident (ransomware, fuite de données) pour tester les procédures, les chaînes de décision, la communication de crise. Plus accessible, adapté aux COMEX et aux directions métier.

**Cyber Range**

Environnement d'entraînement virtuel reproduisant une infrastructure IT réaliste (réseaux, serveurs, endpoints) dans lequel des équipes s'entraînent à détecter et répondre à des attaques simulées. Utilisé pour la formation des analystes SOC, les compétitions CTF (Capture The Flag) et les exercices inter-organisations (ex : exercices ENISA, ANSSI).

**TIBER-EU / DORA TLPT**

TIBER-EU (Threat Intelligence-Based Ethical Red Teaming) est un cadre européen pour les Red Team engagements dans le secteur financier, basé sur de la CTI réelle. DORA impose des TLPT (Threat-Led Penetration Testing) similaires pour les entités financières systémiques, supervisés par les régulateurs (BCE, ACPR).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Validation réaliste des capacités de détection et réponse | Coût élevé d'un engagement Red Team professionnel (50k-500k€) |
| Identification des angles morts non couverts par les outils | Risque d'impacts sur la production si mal cadré |
| Test de bout en bout (technique, processus, humain) | Nécessite une Blue Team mature pour en tirer des bénéfices |
| Amélioration de la maturité des équipes SOC | Le pentest seul ne teste pas la détection (seulement les vulnérabilités) |
| Purple Team : amélioration continue à moindre coût | Le mode Purple Team est moins réaliste qu'un vrai Red Team |
| Conformité réglementaire (DORA TLPT, TIBER-EU) | Résultats difficiles à comparer d'un exercice à l'autre sans métriques |

### Acteurs et solutions du marché

**Prestataires Red Team**
- **ANSSI** : qualification PASSI (Prestataires d'Audit de Sécurité des Systèmes d'Information) — référence française pour sélectionner un prestataire fiable.
- **Synacktiv** : leader français des tests offensifs (racheté par Assystem).
- **HarfangLab**, **Sekoia**, **Wavestone** : acteurs français reconnus.
- **Rapid7**, **Bishop Fox**, **NetSPI** : acteurs internationaux.

**Outils Red Team**
- **Cobalt Strike** : framework de simulation d'attaque le plus utilisé (aussi par les vrais attaquants).
- **Metasploit** : framework open source de référence pour l'exploitation.
- **BloodHound** : analyse des chemins d'attaque dans Active Directory.
- **Sliver**, **Havoc** : alternatives open source à Cobalt Strike.
- **Burp Suite** : test d'applications web.

**Outils Blue Team / Validation**
- **MITRE ATT&CK Evaluations** : évaluation des EDR face à des TTP réelles.
- **Atomic Red Team** : tests unitaires de détection (open source, Red Canary).
- **Caldera** (MITRE) : automatisation des émulations d'adversaires.
- **Cymulate**, **Picus Security** : plateformes de BAS (Breach and Attack Simulation) pour tester en continu les défenses.

### Cas d'usage concrets

**1. Red Team engagement dans un groupe bancaire (TIBER-EU)**
Une grande banque européenne mandate une équipe Red Team qualifiée pour réaliser un engagement TIBER-EU sur 12 semaines. Basée sur de la CTI réelle (groupe APT ciblant le secteur financier), la Red Team compromet un accès VPN via phishing ciblé, pivote vers le réseau SWIFT et exfiltre des données de test. La Blue Team n'a détecté que 40 % des étapes. Le rapport conduit à refondre la segmentation réseau et les règles EDR.

**2. Purple Team dans une DSI industrielle**
Une équipe de 3 Red Teamers et 4 analystes SOC passent 3 jours à exécuter 50 techniques MITRE ATT&CK sur un environnement de test. Pour chaque technique, ils vérifient si Splunk a généré une alerte. Résultat : 35 % des techniques non détectées. En fin d'exercice, 12 nouvelles règles de détection sont déployées. Coût : 3 jours de prestation vs 50k€ pour un Red Team engagement complet.

**3. Cyber Range pour la formation des analystes (ANSSI / ENISA)**
L'ANSSI organise l'exercice Defnet chaque année, un exercice cyber range inter-universitaire. Des équipes de 5 étudiants défendent une infrastructure simulée face à des attaquants réels pendant 48h. Format utilisé aussi en entreprise pour accélérer la montée en compétence des analystes SOC L1/L2.

### Chiffres et tendances
- 75 % des engagements Red Team professionnels atteignent leur objectif (compromission des systèmes critiques), démontrant que les défenses réelles sont insuffisantes (Rapid7, 2023).
- Le phishing reste le vecteur d'accès initial n°1 utilisé par les Red Teams (68 % des engagements — Verizon DBIR 2024).
- Le marché du BAS (Breach and Attack Simulation) croît de 37 % par an : alternative automatisée aux Red Teams ponctuels pour tester en continu.
- DORA (2025) impose des TLPT tous les 3 ans aux entités financières systémiques en Europe.
- L'IA générative commence à être utilisée par les Red Teams pour automatiser la génération de phishing ciblé et l'analyse de code.

## Flashcards
#flashcards

Quelle est la différence entre un pentest et un engagement Red Team ? :: Le pentest est cadré (périmètre défini, durée courte, rapport de vulnérabilités techniques). Le Red Team simule un attaquant APT sur un objectif métier (flag), sans périmètre limité, sur une durée longue, en testant aussi la détection réelle par la Blue Team.

Qu'est-ce que la Purple Team et quel est son intérêt ? :: Mode collaboratif où Red et Blue travaillent ensemble : la Red Team exécute des techniques, la Blue vérifie la détection immédiatement. Plus didactique et moins coûteux qu'un Red Team complet, permet d'améliorer rapidement les règles de détection et de former les analystes.

Qu'est-ce que TIBER-EU / DORA TLPT ? :: TIBER-EU est un cadre européen de Red Teaming basé sur la CTI réelle pour le secteur financier. DORA impose des TLPT (Threat-Led Penetration Testing) tous les 3 ans aux entités financières systémiques, supervisés par les régulateurs bancaires.

Qu'est-ce qu'un tabletop exercise (TTX) ? :: Exercice de simulation sur table sans actions techniques réelles. Les participants discutent de leur réponse à un scénario d'incident (ransomware, fuite de données). Adapté aux COMEX, DSI, équipes juridiques pour tester les procédures et la communication de crise.

Qu'est-ce qu'un Cyber Range ? :: Environnement d'entraînement virtuel reproduisant une infrastructure IT réaliste, utilisé pour former les équipes SOC, organiser des CTF ou des exercices inter-organisations. Exemples : exercices ANSSI (Defnet), ENISA Cyber Europe.

Qu'est-ce que BloodHound et pourquoi est-il utilisé en Red Team ? :: BloodHound est un outil d'analyse des chemins d'attaque dans Active Directory. Il permet à la Red Team (et aux défenseurs en mode Blue Team) de visualiser les chemins de compromission possibles vers le Domain Admin, via les relations de groupes, délégations Kerberos et ACL.

Qu'est-ce que le BAS (Breach and Attack Simulation) ? :: Plateformes (Cymulate, Picus) permettant de simuler automatiquement et en continu des techniques d'attaque (MITRE ATT&CK) sur l'infrastructure réelle pour valider que les contrôles de sécurité (EDR, SIEM, firewall) détectent bien. Alternative continue aux Red Teams ponctuels.

## Sources
- MITRE ATT&CK — https://attack.mitre.org
- ANSSI — Référentiel PASSI et recommandations Red Team
- Rapid7 — Under the Hoodie Pentesting Report 2023
- Verizon DBIR 2024
- TIBER-EU Framework (BCE) — https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu
- Grand View Research — Penetration Testing Market 2023
- Cymulate — State of Cybersecurity Effectiveness 2023
- Red Canary — Atomic Red Team (https://github.com/redcanaryco/atomic-red-team)

## Notions liées
- [[SOC]]
- [[Threat Intelligence et Threat Hunting]]
- [[Forensics]]
- [[Métriques de sécurité]]
- [[EBIOS RM et gestion des risques cyber]]
