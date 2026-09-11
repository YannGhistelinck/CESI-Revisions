---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Forensics

## En bref
> **Définition** : L'investigation numérique (forensics ou digital forensics) est l'ensemble des techniques et processus permettant de collecter, préserver, analyser et présenter des preuves numériques de manière légalement recevable, dans le cadre d'un incident de sécurité, d'une enquête interne ou d'une procédure judiciaire. Elle vise à reconstituer ce qui s'est passé, comment, et par qui.
> **Pourquoi c'est important** : Face à un incident (ransomware, fuite de données, fraude interne), la DSI doit être capable de comprendre la cause racine, l'étendue de la compromission et de constituer des preuves pouvant être utilisées en justice ou auprès des régulateurs. Sans forensics rigoureuse, les preuves numériques peuvent être invalidées et la remédiation incomplète.
> **Chiffres clés** :
> - 70 % des affaires cyber portées devant les tribunaux en France sont rejetées ou affaiblies faute de preuves numériques correctement collectées (Rapport IGJ, 2022).
> - Le coût moyen d'une investigation post-ransomware est de 1,4 M$ pour une organisation de taille intermédiaire (Sophos State of Ransomware 2023).
> - 80 % des forensics post-incident révèlent que l'attaquant était présent depuis plus de 30 jours avant la détection (Mandiant M-Trends 2024).

## Approfondir

### Fonctionnement

**Les principes fondamentaux**

- **Préservation de l'intégrité** : toute copie de données doit être effectuée sur un support write-blocker pour éviter toute altération. L'intégrité est vérifiée par hachage (MD5, SHA-256) avant et après la copie.
- **Chaîne de custody (chain of custody)** : traçabilité documentée de chaque pièce à conviction numérique (qui l'a collectée, quand, comment, où elle a été stockée). Indispensable pour la recevabilité judiciaire.
- **Ordre de volatilité** : les preuves sont collectées du plus volatil au moins volatil (mémoire RAM → processus → connexions réseau → logs systèmes → disque dur).
- **Non-altération du système source** : principe "do no harm" — l'analyste ne modifie pas le système compromis.

**Les phases d'une investigation forensique**

1. **Identification** : définir le périmètre, les systèmes à investiguer, les objectifs (criminelle, disciplinaire, technique).
2. **Collecte (Acquisition)** : image forensique du disque (bit-à-bit), dump mémoire RAM, extraction des logs, capture réseau.
3. **Préservation** : stockage sécurisé des images forensiques, calcul de hashes, chain of custody.
4. **Analyse** : extraction d'artéfacts, timeline, recherche d'IoC, rétro-ingénierie de malwares.
5. **Documentation** : rapport d'investigation détaillé, chronologie des faits.
6. **Présentation** : restitution aux parties prenantes (COMEX, direction juridique, autorités).

**Les types de forensics**

- **Disk Forensics** : analyse des systèmes de fichiers (NTFS, ext4), récupération de fichiers supprimés, analyse des métadonnées, MFT (Master File Table), LNK files, Prefetch, Shellbags.
- **Memory Forensics** : analyse du dump RAM pour extraire processus en cours, connexions réseau, mots de passe en clair, malwares fileless. Outil de référence : **Volatility**.
- **Network Forensics** : analyse des captures réseau (PCAP) pour reconstituer les communications de l'attaquant, détecter l'exfiltration. Outil : **Wireshark**, **Zeek**, **NetworkMiner**.
- **Log Analysis** : corrélation des journaux système (Windows Event Logs, Syslog), Active Directory (événements 4624, 4625, 4768, 4769), applications.
- **Mobile Forensics** : extraction et analyse des données de smartphones (Cellebrite UFED, Oxygen Forensic).
- **Cloud Forensics** : investigation dans les environnements cloud (AWS CloudTrail, Azure Activity Logs, GCP Audit Logs) — spécificité : données hors de l'infrastructure cliente.
- **Malware Analysis** (statique/dynamique) : reverse engineering des malwares découverts. Outils : **Ghidra**, **IDA Pro**, **Any.run** (sandbox), **VirusTotal**.

**Artefacts Windows clés**

Les systèmes Windows laissent de nombreuses traces exploitables :
- **Registre Windows** : historique des programmes exécutés (UserAssist, MRU), périphériques connectés (USBSTOR), services installés.
- **Prefetch** : liste des exécutables lancés avec leur timestamp et nombre d'exécutions.
- **Event Logs** : Security (authentifications, créations de comptes), System, Application, PowerShell.
- **$MFT** : Master File Table NTFS, timeline de création/modification/accès de chaque fichier.
- **Browser artifacts** : historique, téléchargements, cache, favoris.
- **LNK files et Jump Lists** : fichiers récemment ouverts depuis des chemins révélateurs.

**Forensics et droit français**

En France, la collecte de preuves numériques dans le cadre d'une procédure pénale est encadrée par le Code de procédure pénale. Les entreprises peuvent mener des investigations internes mais doivent respecter le RGPD (traitement des données personnelles des employés) et le droit du travail. Le dépôt de plainte auprès du Parquet ou de la Gendarmerie (C3N — Centre de lutte contre les criminalités Numériques) peut ensuite déclencher une investigation officielle.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Reconstitution précise de l'incident (cause racine, étendue) | Très chronophage et nécessite des experts spécialisés |
| Preuves légalement recevables pour action judiciaire ou réglementaire | Données volatiles perdues si le système est redémarré avant l'acquisition |
| Identification d'autres systèmes compromis lors de l'investigation | Tensions avec le droit du travail et la vie privée des employés |
| Amélioration des règles de détection après l'analyse | Coût élevé (prestataires forensics : 1 500 à 3 000 €/jour) |
| Indispensable pour les notifications RGPD (72h CNIL) | Environnements cloud compliquent la collecte (dépendance au CSP) |
| Aide à la remédiation complète (évite les rechutes) | Risque de contamination des preuves si protocoles non respectés |

### Acteurs et solutions du marché

**Outils open source**
- **Autopsy / Sleuth Kit** : plateforme d'analyse forensique complète, interface graphique.
- **Volatility** : référence mondiale pour l'analyse mémoire.
- **Velociraptor** : collecte d'artefacts à distance sur des flottes d'endpoints.
- **Wireshark** : analyse de captures réseau.
- **Ghidra** (NSA) : rétro-ingénierie de malwares.
- **KAPE** (Kroll Artifact Parser and Extractor) : collecte rapide d'artefacts Windows.

**Outils commerciaux**
- **EnCase** (OpenText) : standard judiciaire, très utilisé par les forces de l'ordre.
- **FTK** (AccessData/Exterro) : alternative à EnCase, très répandue.
- **Cellebrite UFED** : extraction de données mobiles (référence mondiale).
- **CrowdStrike Falcon Forensics**, **SentinelOne Singularity** : forensics intégrée aux EDR.
- **X-Ways Forensics** : outil expert très performant.

**Prestataires**
- **Wavestone**, **Intrinsec**, **Sekoia**, **ITrust** : acteurs français de référence en réponse à incident et forensics.
- **Mandiant** (Google), **Kroll**, **CrowdStrike Services** : acteurs internationaux.
- **ANSSI** : intervient sur les incidents d'OIV/OES et publie des rapports post-incident.

### Cas d'usage concrets

**1. Investigation post-ransomware LockBit (secteur hospitalier)**
Un CHU est victime d'un ransomware LockBit 3.0. L'équipe forensics (prestataire + DSI) procède au dump mémoire des serveurs encore actifs, image les disques durs des machines non chiffrées, et extrait les logs Active Directory des 30 derniers jours. L'analyse révèle un accès initial via un compte VPN compromis 45 jours avant le chiffrement, un mouvement latéral via Pass-the-Hash, et l'exfiltration de 200 Go de données de patients via un C2 hébergé en Europe de l'Est. Ces preuves permettent de notifier la CNIL dans les 72h et d'identifier les lacunes de détection (absence de MFA sur le VPN).

**2. Investigation de fraude interne (secteur bancaire)**
Un contrôleur de gestion est soupçonné d'avoir exfiltré des données clients vers un concurrent. L'investigation forensique (respectant le cadre RGPD et le droit du travail, avec l'accord du CE) analyse les logs DLP, les métadonnées de fichiers Office (historique de modification), les artefacts USB (USBSTOR dans le registre), et l'historique de messagerie. Les preuves recueillies avec chain of custody sont transmises au service juridique pour procédure disciplinaire et dépôt de plainte.

**3. Cloud Forensics après compromission d'un compte Azure (secteur SaaS)**
Un accès administrateur Azure est compromis suite à un credential stuffing. L'investigation se base sur les Azure Activity Logs et Microsoft Defender for Cloud pour reconstituer les actions de l'attaquant : création d'une VM de minage, exfiltration de secrets depuis Azure Key Vault, désactivation des alertes Security Center. L'investigation est réalisée sans accès physique aux serveurs Microsoft, uniquement via les APIs et logs natifs.

### Chiffres et tendances
- Les attaques fileless (sans fichier sur disque) représentent 40 % des incidents en 2023, rendant la forensics disque insuffisante sans analyse mémoire (CrowdStrike Global Threat Report 2024).
- Le cloud forensics est la discipline la plus en croissance : 65 % des incidents en 2023 impliquent un environnement cloud ou hybride (Mandiant).
- La durée moyenne d'une investigation forensique complète post-ransomware est de 3 à 6 semaines pour une organisation de taille intermédiaire.
- La pénurie de forensiciens qualifiés en France est estimée à 2 000 postes non pourvus (ANSSI, 2023).
- Les EDR modernes (CrowdStrike, SentinelOne) intègrent des capacités de forensics "live" réduisant le temps de collecte de plusieurs jours à quelques heures.

## Flashcards
#flashcards

Qu'est-ce que la chaîne de custody (chain of custody) en forensics ? :: La traçabilité documentée de chaque pièce à conviction numérique : qui l'a collectée, quand, comment elle a été préservée et stockée. Sans chain of custody rigoureuse, les preuves peuvent être irrecevables en justice.

Qu'est-ce que l'ordre de volatilité et pourquoi est-il important ? :: Les preuves numériques doivent être collectées du plus volatil au moins volatil : RAM → processus actifs → connexions réseau → logs → disque dur. Sans respecter cet ordre, les données les plus précieuses (mémoire, connexions C2 actives) sont perdues après un redémarrage.

Quel est l'outil de référence pour l'analyse de mémoire RAM en forensics ? :: Volatility (open source) est le standard mondial. Il permet d'extraire les processus en cours, les connexions réseau, les clés de chiffrement en mémoire, et de détecter les malwares fileless qui ne laissent pas de traces sur le disque.

Quels sont les principaux artefacts Windows exploitables en forensics ? :: Registre Windows (UserAssist, USBSTOR, MRU), Prefetch (exécutables lancés), Event Logs (4624 logon, 4768 Kerberos), $MFT (timeline NTFS), LNK files (fichiers récemment ouverts), Browser artifacts (historique, téléchargements).

Quelle est la contrainte légale principale pour les investigations internes en France ? :: Le respect du RGPD (traitement des données personnelles des employés) et du droit du travail. Une investigation interne doit être proportionnée, justifiée, et idéalement validée par le CSE. Les preuves doivent être collectées dans le respect de ces cadres pour être utilisables.

Qu'est-ce que le cloud forensics et en quoi est-il différent du forensics traditionnel ? :: Investigation dans les environnements cloud (AWS CloudTrail, Azure Logs, GCP Audit Logs). Différence clé : pas d'accès physique aux serveurs, dépendance aux logs fournis par le CSP, risque que des données aient été supprimées ou non disponibles. Nécessite des compétences cloud spécifiques.

Qu'est-ce qu'un malware fileless et pourquoi complique-t-il le forensics ? :: Un malware fileless s'exécute entièrement en mémoire (via PowerShell, WMI, LOLBins) sans écrire de fichier sur le disque. Il ne laisse pas de traces sur le disque dur, nécessitant une analyse mémoire (dump RAM + Volatility) pour être détecté, au lieu du forensics disque classique.

## Sources
- ANSSI — Guide de réponse à incident (https://www.ssi.gouv.fr)
- Mandiant M-Trends 2024
- SANS Institute — FOR508 : Advanced Incident Response, Threat Hunting, and Digital Forensics
- Volatility Foundation — https://www.volatilityfoundation.org
- Sophos — State of Ransomware 2023
- Kroll — Global Fraud and Risk Report 2023
- CrowdStrike — Global Threat Report 2024
- CNIL — Lignes directrices sur les investigations internes et le RGPD

## Notions liées
- [[SOC]]
- [[Threat Intelligence et Threat Hunting]]
- [[Red Team - Blue Team - Purple Team]]
- [[IA en cybersécurité]]
- [[EBIOS RM et gestion des risques cyber]]
