---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# SOAR

## En bref
> **Définition** : Le SOAR (Security Orchestration, Automation and Response) est une plateforme permettant d'orchestrer les outils de sécurité, d'automatiser les tâches répétitives de réponse aux incidents et de standardiser les procédures via des playbooks. Il complète le SIEM en transformant les alertes en actions concrètes, avec ou sans intervention humaine.
> **Pourquoi c'est important** : Face au volume d'alertes croissant (11 000/jour en moyenne dans un SOC) et à la pénurie de talents en cybersécurité, l'automatisation n'est plus une option. Le SOAR permet aux analystes SOC de se concentrer sur les tâches à haute valeur ajoutée en confiant les tâches répétitives à des playbooks automatisés. Il réduit le MTTR (Mean Time To Respond).
> **Chiffres clés** :
> - Le SOAR réduit le MTTR (temps moyen de réponse aux incidents) de 80 % en moyenne (IBM Security).
> - Les organisations utilisant un SOAR économisent 1,76 M$ par violation de données en moyenne par rapport à celles qui n'en ont pas (IBM Cost of a Data Breach 2023).
> - Le marché du SOAR devrait atteindre 2,9 Md$ en 2028 (MarketsandMarkets).

## Approfondir

### Fonctionnement

**Orchestration** : le SOAR intègre et coordonne des dizaines d'outils de sécurité hétérogènes via des connecteurs et des API (firewall, EDR, SIEM, threat intelligence, IAM, ticketing). Il crée un "tissu connectif" entre les outils qui seraient sinon silotés.

**Automatisation** : exécution automatique d'actions de réponse déclenchées par des alertes ou des événements :
- Blocage d'une IP sur le firewall
- Mise en quarantaine d'un endpoint compromis (via EDR)
- Désactivation d'un compte utilisateur (via AD/IAM)
- Enrichissement d'une alerte (renseignement sur une IP via VirusTotal, MISP)
- Création d'un ticket incident dans l'ITSM (ServiceNow, Jira)
- Notification de l'équipe de sécurité

**Playbooks** : flux de travail automatisés (workflows) définissant la séquence d'actions à exécuter en réponse à un type d'incident donné. Exemple de playbook "phishing" :
1. Extraction des IOC de l'email (IP, URL, hash de pièce jointe)
2. Vérification sur VirusTotal et MISP
3. Si malveillant : blocage de l'URL sur le proxy, de l'IP sur le firewall
4. Recherche des autres utilisateurs ayant reçu le même email
5. Notification aux utilisateurs concernés
6. Création du ticket incident
7. Rapport au RSSI

**Triptyque SIEM + SOAR + Threat Intelligence** : le SIEM détecte et alerte → le SOAR enrichit et automatise la réponse → les flux de threat intelligence (MISP, STIX/TAXII) alimentent les deux en contexte sur les menaces connues.

**MTTR / MTTD** :
- MTTD (Mean Time To Detect) : durée moyenne entre l'intrusion et la détection. Réduit par le SIEM.
- MTTR (Mean Time To Respond) : durée moyenne entre la détection et la résolution. Réduit par le SOAR.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction drastique du MTTR | Investissement initial en temps pour développer les playbooks |
| Libère les analystes des tâches répétitives | Risque d'automatisation d'une mauvaise réponse (faux positif) |
| Standardisation et cohérence des réponses | Nécessite une intégration soignée avec les outils existants |
| Scalabilité : traite des milliers d'alertes simultanément | Dépendance aux APIs des partenaires (évolutions, ruptures) |
| Traçabilité complète des actions de réponse | Courbe d'apprentissage importante pour les playbooks complexes |
| Économies significatives par incident | Peut créer une fausse confiance si les playbooks ne sont pas maintenus |

### Acteurs et solutions du marché

**Solutions commerciales** :
- **Palo Alto XSOAR (Cortex XSOAR)** : leader du marché, anciennement Demisto. Bibliothèque de 900+ intégrations, marketplace de playbooks.
- **Splunk SOAR (anciennement Phantom)** : intégration native avec Splunk SIEM, fort écosystème.
- **ServiceNow SecOps** : orienté ITSM + sécurité, adapté aux organisations déjà sur ServiceNow.
- **Microsoft Sentinel** : intègre des capacités SOAR natives (Logic Apps/Playbooks Azure).

**Solutions open source** :
- **The Hive Project** : plateforme open source de gestion des incidents de sécurité, souvent couplée avec Cortex (automatisation) et MISP (threat intelligence). Très utilisée en Europe.
- **Shuffle** : SOAR open source, simple, basé sur des workflows visuels.

**Threat Intelligence** :
- **MISP (Malware Information Sharing Platform)** : plateforme open source de partage d'IOC.
- **VirusTotal** : analyse de fichiers/URLs/IPs, API intégrée dans la plupart des SOAR.
- **OpenCTI** : plateforme de threat intelligence open source française (ANSSI).

### Cas d'usage concrets

1. **Réponse automatisée à un phishing** : le SIEM détecte un email suspect → le SOAR extrait les IOC, les vérifie sur VirusTotal → si malveillant : bloque l'URL sur le proxy et l'IP sur le firewall, liste les 47 autres destinataires, leur envoie une alerte → ticket créé dans ServiceNow → l'analyste n'intervient que pour valider et clore l'incident. MTTR : 8 minutes au lieu de 2 heures.

2. **Containment d'un endpoint compromis** : EDR détecte un comportement ransomware → SOAR déclenche automatiquement la mise en quarantaine réseau de l'endpoint via l'API EDR, désactive le compte AD associé, isole les partages réseau accessibles, notifie l'astreinte → l'analyste a accès à un rapport complet à son arrivée.

3. **Enrichissement de la threat intelligence** : chaque alerte SIEM est automatiquement enrichie par le SOAR (réputation de l'IP, appartenance à un botnet connu, géolocalisation, secteur ciblé) avant d'être présentée à l'analyste. La décision de qualification prend 30 secondes au lieu de 15 minutes.

### Chiffres et tendances
- Gartner : d'ici 2025, les SOC qui n'utilisent pas d'automatisation traiteront 30 % d'alertes de moins faute de capacité humaine.
- IBM (2023) : les organisations utilisant IA et automatisation dans la sécurité détectent et contiennent une violation 108 jours plus vite.
- Le nombre moyen de playbooks actifs dans un SOC mature est de 25 à 50 (Palo Alto Networks).
- Pénurie mondiale de talents cyber : 4 millions de postes non pourvus en 2023 (ISC2 Cybersecurity Workforce Study) — le SOAR est une réponse partielle à cette contrainte.

## Flashcards
#flashcards/Cybersécurité/SOAR
Qu'est-ce qu'un SOAR ? :: Security Orchestration, Automation and Response : plateforme orchestrant les outils de sécurité, automatisant les tâches répétitives de réponse aux incidents et standardisant les procédures via des playbooks.

Quelle est la différence entre SIEM et SOAR ? :: Le SIEM détecte et alerte (visibilité, corrélation). Le SOAR agit et automatise (réponse, orchestration). Ils sont complémentaires : le SIEM alimente le SOAR en alertes.

Qu'est-ce qu'un playbook SOAR ? :: Workflow automatisé définissant la séquence d'actions à exécuter en réponse à un type d'incident (phishing, ransomware, brute force). Peut inclure des actions automatiques et des points de décision humains.

Qu'est-ce que le MTTR et comment le SOAR le réduit-il ? :: Mean Time To Respond : durée entre la détection et la résolution d'un incident. Le SOAR le réduit en automatisant les actions de containment et d'enrichissement, éliminant les délais humains sur les tâches répétitives.

Citer 3 actions typiques automatisées par un SOAR. :: 1. Blocage d'une IP malveillante sur le firewall. 2. Mise en quarantaine d'un endpoint via EDR. 3. Désactivation d'un compte compromis dans l'Active Directory.

Qu'est-ce que The Hive et dans quel contexte est-il utilisé ? :: The Hive est une plateforme open source de gestion des incidents de sécurité, très utilisée en Europe (notamment en France). Souvent couplée avec Cortex (automatisation) et MISP (threat intelligence).

Pourquoi le SOAR est-il stratégique face à la pénurie de talents cyber ? :: Avec 4 millions de postes non pourvus dans le monde, le SOAR permet aux équipes réduites de traiter un volume d'alertes disproportionné en automatisant les tâches de niveau 1 et 2, réservant les analystes aux incidents complexes.

## Sources
- IBM — Cost of a Data Breach Report 2023
- Gartner — Market Guide for SOAR 2023
- Palo Alto Networks — Cortex XSOAR documentation — cortex.pan.dev
- The Hive Project — thehive-project.org
- ANSSI — OpenCTI — www.filigran.io/fr/opencti
- ISC2 Cybersecurity Workforce Study 2023 — www.isc2.org
- MarketsandMarkets — SOAR Market Report 2023

## Notions liées
- [[SIEM]]
- [[EDR - XDR - NDR]]
- [[Menaces cyber]]
- [[Cyber-résilience]]
- [[Défense en profondeur]]
- [[Zero Trust]]
