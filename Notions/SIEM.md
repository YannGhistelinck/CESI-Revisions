---
type: notion
thèmes:
  - Cybersécurité
  - IA
statut: pas vu
dernière_révision: 
---

# SIEM

## En bref
> **Définition** : Le SIEM (Security Information and Event Management) est une plateforme centralisant la collecte, l'agrégation, la normalisation et la corrélation des logs et événements de sécurité issus de l'ensemble du SI (réseaux, serveurs, applications, endpoints). Il permet la détection en temps réel des menaces, la génération d'alertes et la conservation des journaux à des fins d'investigation et de conformité.
> **Pourquoi c'est important** : Un SI complexe génère des millions d'événements par jour, impossibles à surveiller manuellement. Le SIEM est le cerveau du SOC (Security Operations Center) : il agrège la visibilité de toutes les couches du SI pour détecter des comportements malveillants que les outils silotés ne verraient pas. Il est souvent requis par les réglementations (NIS2, ISO 27001, DORA).
> **Chiffres clés** :
> - Le marché mondial du SIEM était évalué à 5,97 Md$ en 2023 et devrait atteindre 10,9 Md$ en 2030 (Fortune Business Insights).
> - Un SOC reçoit en moyenne 11 000 alertes de sécurité par jour, dont 45 % sont des faux positifs (Ponemon Institute 2022).
> - Le délai médian entre l'intrusion et la détection est de 21 jours (Mandiant M-Trends 2024) — le SIEM vise à le réduire à quelques heures.

## Approfondir

### Fonctionnement

**Architecture SIEM** :
1. **Collecte** : agents (forwarders) ou protocoles standards (Syslog, WinEvent, API) récupèrent les logs de toutes les sources.
2. **Normalisation** : conversion des logs dans un format commun (ECS pour Elastic, CIM pour Splunk).
3. **Corrélation** : règles de corrélation (ex. : 5 échecs d'authentification en 2 minutes sur un même compte) déclenchent des alertes.
4. **Stockage** : conservation à long terme des logs pour investigation forensique et conformité réglementaire (RGPD, NIS2 : 1 an recommandé).
5. **Alerting** : génération de tickets d'incident, intégration avec SOAR pour automatisation.
6. **Reporting** : tableaux de bord de conformité, rapports de sécurité.

**Corrélation d'événements** : coeur du SIEM. Une règle de corrélation croise des événements de sources différentes pour identifier un comportement malveillant. Exemple : un utilisateur se connecte depuis Paris à 9h et depuis Shanghai à 9h05 (impossible travel) — sans corrélation entre les logs VPN et les logs applicatifs, cela serait indétectable.

**UEBA (User and Entity Behavior Analytics)** : module IA/ML intégré aux SIEM modernes qui établit un profil comportemental de base pour chaque utilisateur et entité, puis détecte les anomalies statistiques (connexion à une heure inhabituelle, accès à des ressources jamais consultées, volume de téléchargement anormal).

**Détection d'anomalies** : deux approches complémentaires :
- Règles statiques (signatures) : rapides mais génèrent des faux positifs sur des comportements légitimes.
- Détection comportementale (UEBA/ML) : plus précis mais nécessite une phase d'apprentissage et une calibration.

**Next-Gen SIEM** : les SIEM modernes s'appuient sur des data lakes (stockage massif, pas de licence par volume), des pipelines de traitement en temps réel, et intègrent nativement des capacités de threat intelligence, UEBA et automatisation (vers le SOAR).

**Solutions majeures** :
- **Splunk** : leader historique, très puissant, coûteux (licence par volume de données). Langage de requête : SPL.
- **Elastic Security (SIEM)** : basé sur Elasticsearch, open source, flexible, adoption forte. Langage : KQL/EQL.
- **IBM QRadar** : robuste, très utilisé dans les grandes entreprises et OIV. Bonne corrélation native.
- **Wazuh** : SIEM open source gratuit, basé sur OSSEC. Excellente option pour les PME ou les environnements avec budget limité. Intègre HIDS, détection des vulnérabilités, FIM.
- **Microsoft Sentinel** : SIEM cloud-native (Azure), tarification à la donnée ingérée, intégration native avec l'écosystème Microsoft 365/Defender.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Visibilité centralisée sur tout le SI | Volume d'alertes élevé, risque de fatigue des analystes |
| Détection de menaces croisées (corrélation) | Coût élevé (Splunk, QRadar) ou effort d'intégration (Elastic) |
| Conservation des logs pour forensique et conformité | Nécessite une expertise technique importante pour les règles |
| Base du SOC et de la réponse aux incidents | Faux positifs nombreux si règles mal calibrées |
| Intégration avec SOAR pour automatisation | Temps de déploiement et de calibration long (6-12 mois) |
| Obligatoire dans de nombreux cadres réglementaires | Wazuh gratuit mais limité en performance à grande échelle |

### Acteurs et solutions du marché

| Solution | Type | Points forts | Usage typique |
|----------|------|--------------|---------------|
| Splunk Enterprise Security | Commercial | Puissance, écosystème apps | Grandes entreprises, SOC avancés |
| Elastic Security | Open source/Commercial | Flexibilité, coût, API | Startups, ESN, SOC modernes |
| IBM QRadar | Commercial | Corrélation, OIV | Industries régulées, grands groupes |
| Wazuh | Open source | Gratuit, HIDS intégré | PME, budgets limités, compliance |
| Microsoft Sentinel | Cloud SaaS | Intégration M365, scalabilité | Environnements Microsoft |
| Exabeam | Commercial | UEBA, Next-Gen | SOC centrés sur le comportement |

### Cas d'usage concrets

1. **Détection d'une fraude interne** : le SIEM d'une banque corrèle des connexions tardives, des accès inhabituels à des comptes clients et un export massif de fichiers CSV. L'alerte UEBA déclenche une investigation qui révèle un employé en cours d'exfiltration de données clients.

2. **Détection d'un mouvement latéral (APT)** : règle de corrélation entre les logs Active Directory (création d'un compte admin), les logs réseau (scan de ports internes) et les logs d'un serveur de sauvegarde (tentative d'accès à 3h du matin). Sans SIEM, ces 3 événements dans des outils différents seraient passés inaperçus.

3. **Conformité NIS2** : un opérateur de services essentiels utilise Splunk pour générer automatiquement les rapports de journalisation requis par l'ANSSI, prouver la traçabilité des accès privilégiés et respecter les délais de notification d'incident (24h pour NIS2).

### Chiffres et tendances
- Le SIEM cloud-native (Microsoft Sentinel, Google Chronicle) représente 35 % du marché en 2023 et progresse de 20 % par an (Gartner).
- L'UEBA réduit le temps de détection des insider threats de 70 % par rapport aux règles statiques seules (Gartner).
- 60 % des SOC utilisent déjà ou prévoient d'utiliser l'IA générative pour l'analyse des alertes SIEM d'ici 2025 (IDC).
- Wazuh compte plus de 20 millions de téléchargements et est déployé dans plus de 1 000 organisations dans le monde.

## Flashcards
#flashcards/Cybersécurité/SIEM #flashcards/IA/SIEM
Qu'est-ce qu'un SIEM ? :: Plateforme centralisant la collecte, la normalisation, la corrélation et l'analyse des logs et événements de sécurité du SI. Coeur du SOC, il détecte les menaces en temps réel et conserve les journaux pour forensique et conformité.

Qu'est-ce que la corrélation d'événements dans un SIEM ? :: Mécanisme croisant des événements de sources différentes pour détecter des comportements malveillants invisibles individuellement. Ex. : connexion Paris + connexion Shanghai dans la même minute = "impossible travel".

Quelle est la différence entre Splunk et Wazuh ? :: Splunk est une solution commerciale très puissante (licence par volume, coûteuse), leader sur les grands SOC. Wazuh est open source et gratuit, idéal pour les PME ou budgets limités, avec HIDS intégré.

Qu'est-ce que l'UEBA dans un SIEM ? :: User and Entity Behavior Analytics : module IA/ML établissant un profil comportemental de base pour chaque utilisateur, détectant les anomalies statistiques (connexion inhabituelle, accès anormal, exfiltration).

Quelles sont les 3 limites principales d'un SIEM ? :: 1. Volume d'alertes élevé et faux positifs nombreux. 2. Coût et complexité d'intégration. 3. Nécessite une expertise avancée pour la calibration des règles de corrélation.

Qu'est-ce qu'un Next-Gen SIEM ? :: SIEM moderne utilisant un data lake (pas de limite de volume), des pipelines temps réel, et intégrant nativement threat intelligence, UEBA et automatisation (SOAR). Ex. : Microsoft Sentinel, Google Chronicle, Exabeam.

Quel est le délai moyen de détection d'une intrusion et comment le SIEM y contribue-t-il ? :: 21 jours en médiane (Mandiant 2024). Le SIEM vise à réduire ce délai à quelques heures via la corrélation en temps réel et les règles de détection comportementale.

## Sources
- ANSSI — Recommandations pour la journalisation des systèmes d'information — www.ssi.gouv.fr
- Mandiant — M-Trends 2024 — www.mandiant.com
- Gartner — Magic Quadrant for SIEM 2023
- Ponemon Institute — State of Security Operations Report 2022
- Documentation officielle Splunk — docs.splunk.com
- Documentation officielle Elastic Security — www.elastic.co/security
- Documentation officielle Wazuh — documentation.wazuh.com
- IBM QRadar documentation — www.ibm.com/security/qradar

## Notions liées
- [[SOAR]]
- [[EDR - XDR - NDR]]
- [[Menaces cyber]]
- [[Défense en profondeur]]
- [[Cyber-résilience]]
- [[Zero Trust]]
