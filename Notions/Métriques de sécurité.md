---
type: notion
thèmes:
  - Cybersécurité
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Métriques de sécurité

## En bref
> **Définition** : Les métriques de sécurité sont des indicateurs quantifiables permettant de mesurer l'efficacité des contrôles de sécurité, la performance du SOC et la progression de la maturité cyber d'une organisation. Elles permettent de piloter objectivement la cybersécurité et de justifier les investissements auprès de la direction.
> **Pourquoi c'est important** : Sans métriques, la cybersécurité reste perçue comme un centre de coûts opaque. Les métriques permettent au RSSI de démontrer la valeur des investissements, d'identifier les dégradations de performance, de respecter les SLA contractuels (MSSP/MDR) et de dialoguer avec le COMEX sur des bases factuelles.
> **Chiffres clés** :
> - Les organisations avec des métriques de sécurité matures réduisent le coût d'un incident de 30 % en moyenne (IBM, 2023).
> - Seuls 42 % des RSSI disposent de métriques permettant de mesurer le ROI de leurs investissements sécurité (Gartner, 2023).
> - Un MTTD < 24h et un MTTR < 4h sont considérés comme des indicateurs de maturité SOC élevée (SANS Institute).

## Approfondir

### Fonctionnement

**Les métriques de détection et réponse**

**MTTD — Mean Time To Detect**
Temps moyen entre le début d'un incident (ou compromission) et sa détection par l'équipe de sécurité. C'est l'indicateur le plus critique : plus le MTTD est élevé, plus l'attaquant a eu le temps de s'installer, de se latéraliser et d'exfiltrer des données.
- Référence secteur : 16 jours (Mandiant 2024) — objectif d'un SOC mature : < 24h pour les incidents critiques.
- Calcul : Somme des durées (détection - début incident) / Nombre d'incidents.
- Dépend de : qualité des logs, couverture des sources (EDR, réseau, identités), règles de détection, UEBA.

**MTTR — Mean Time To Respond / Recover**
Temps moyen entre la détection d'un incident et sa résolution complète (confinement, éradication, restauration). Il englobe deux sous-métriques :
- **MTTC (Mean Time To Contain)** : temps pour isoler la menace et empêcher sa propagation.
- **MTTF (Mean Time To Fix)** : temps pour éliminer la menace et remettre les systèmes en état normal.
- Référence : MTTR moyen de 280 jours (identification + containment) selon IBM 2023 — objectif mature : < 4h pour un incident critique, < 24h pour un incident majeur.

**SLA SOC**
Les contrats avec les MSSP/MDR définissent des SLA (Service Level Agreements) précis :
- **SLA de notification** : délai maximum entre la détection d'un incident critique et la notification du client (typiquement 15 à 30 minutes).
- **SLA de prise en charge** : délai entre la création du ticket et l'affectation à un analyste (ex : P1 < 15 min, P2 < 1h, P3 < 4h).
- **SLA de résolution** : délai de résolution selon la priorité de l'incident.
- **Disponibilité** : taux de disponibilité des services de surveillance (99,9 % en général).
- Les SLA sont mesurés mensuellement et font l'objet de pénalités contractuelles en cas de non-respect.

**Les métriques de sensibilisation et de risque humain**

**CTR — Click-Through Rate (taux de clics sur phishing simulé)**
Pourcentage d'employés ayant cliqué sur un lien malveillant lors d'une campagne de phishing simulé. Indicateur direct du niveau de résistance humaine au phishing.
- Référence : taux moyen initial de 30-40 % avant formation, objectif < 5 % après programme de sensibilisation mature (KnowBe4, 2023).
- Segmentation clé : par département, par niveau hiérarchique (les cadres dirigeants sont souvent plus vulnérables car moins formés).

**Report Rate (taux de signalement)**
Pourcentage d'employés ayant signalé un mail suspect au SOC ou à la DSI. Indicateur complémentaire et plus positif que le CTR : mesure la culture de sécurité active.
- Objectif : > 30 % de signalement des mails suspectés comme phishing.
- Un report rate élevé transforme les employés en capteurs humains du SOC.

**Phishing Resilience Score**
Combinaison du CTR et du report rate pour évaluer la résilience globale de l'organisation face au phishing.
Formula : PRS = Report Rate / (CTR + Report Rate)

**Les métriques de couverture et de maturité**

- **Couverture MITRE ATT&CK** : % de techniques MITRE ATT&CK couvertes par des règles de détection actives. Indicateur de la profondeur de la détection.
- **Taux de faux positifs (False Positive Rate)** : % des alertes SIEM qui sont de faux positifs. Un taux > 95 % signale une qualité de règles insuffisante et une fatigue d'alerte.
- **MTTP (Mean Time To Patch)** : temps moyen entre la publication d'un patch critique et son déploiement. CISA recommande < 15 jours pour les vulnérabilités critiques.
- **Asset coverage** : % du SI couvert par un EDR actif (objectif : > 95 %).
- **Nombre d'incidents par mois** : en hausse ou en baisse ? À corréler avec l'évolution du périmètre et des méthodes d'attaque.
- **Coût par incident** : coût moyen de traitement d'un incident (heures analyste, outils, remédiation).

**Dashboard et reporting RSSI**

Les métriques sont présentées à différentes audiences :
- **COMEX** : métriques haut niveau (coût d'un incident, évolution du risque résiduel, conformité réglementaire).
- **DSI** : métriques opérationnelles (MTTD, MTTR, SLA, couverture EDR).
- **SOC Manager** : métriques granulaires (taux de faux positifs, MTTC par type d'incident, charge des analystes).

Les frameworks de reporting : **NIST CSF (Identify, Protect, Detect, Respond, Recover)**, **ISO 27004** (métriques SMSI), **CIS Controls v8** (métriques associées à chaque contrôle).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Pilotage objectif de la performance SOC | Risque de Goodhart's Law (optimiser la métrique et non l'objectif) |
| Justification des investissements sécurité auprès du COMEX | Certaines métriques difficiles à mesurer (ex : incidents évités) |
| Identification rapide des dégradations de performance | Trop de métriques = paralysie analytique |
| SLA contractuels mesurables et opposables aux MSSP | Les métriques peuvent être manipulées (sous-déclarer les incidents) |
| Aide à la priorisation des actions et investissements | Benchmark difficile : chaque organisation est différente |
| Conformité réglementaire (NIS2 exige des reportings) | Le coût de collecte et d'analyse des métriques peut être significatif |

### Acteurs et solutions du marché

**Plateformes de métriques SOC**
- **Microsoft Sentinel** : tableaux de bord natifs MTTD/MTTR, taux de faux positifs.
- **Splunk** : dashboards personnalisables, Splunk SIEM Essentials for Security.
- **ServiceNow Security Operations** : métriques SLA et gestion des incidents.
- **TheHive** : gestion d'incidents open source avec métriques.
- **Elastic SIEM** : dashboards open source personnalisables.

**Plateformes de phishing simulé**
- **KnowBe4** : leader du marché, campagnes phishing simulées + formation, dashboard CTR/Report Rate.
- **Proofpoint Security Awareness Training**.
- **Cofense PhishMe**.
- **Gophish** : solution open source.

**Frameworks de métriques**
- **NIST CSF** : Framework de cybersécurité avec métriques associées à chaque fonction.
- **ISO 27004** : norme de mesure et d'évaluation des SMSI.
- **CIS Controls v8** : 18 contrôles avec métriques d'implémentation.
- **SANS Security Awareness Maturity Model** : évaluation de la maturité du programme de sensibilisation.

### Cas d'usage concrets

**1. Tableau de bord SOC dans un groupe industriel**
La DSI d'un groupe industriel met en place un dashboard mensuel présenté au COMEX : MTTD (cible : < 4h, réel : 8h), MTTR (cible : < 24h, réel : 36h), taux de faux positifs (87 %), couverture EDR (82 %). Ce dashboard révèle que 40 % des faux positifs proviennent d'une seule règle SIEM mal calibrée. Son ajustement réduit de 30 % la charge de travail L1 en 2 semaines.

**2. Suivi du CTR phishing dans un groupe bancaire**
Après un incident de phishing, une banque régionale lance un programme de phishing simulé mensuel. Le CTR initial est de 34 %. Après 6 mois de micro-formations ciblées post-clic, il descend à 7 %. Le report rate passe de 5 % à 28 %. Ces métriques sont présentées au régulateur (ACPR) comme preuve de la maturité du programme de sensibilisation.

**3. SLA MSSP et gestion contractuelle**
Un groupe retail externalise sa surveillance SOC à un MSSP avec des SLA : P1 notifié en < 15 min, MTTC < 2h. Lors d'un incident ransomware en 2023, le MSSP met 47 minutes à notifier (vs SLA 15 min) et 5h pour le containment (vs SLA 2h). Grâce au suivi précis des métriques, la DSI active les pénalités contractuelles et engage une renégociation du contrat avec des engagements renforcés.

### Chiffres et tendances
- MTTD moyen tous secteurs : 197 jours sans SOC dédié / 16 jours avec SOC mature (IBM/Mandiant 2023-2024).
- MTTR moyen global : 73 jours pour identifier et contenir une violation (IBM Cost of Data Breach 2023).
- Taux de clic moyen sur phishing simulé (sans formation) : 32,4 % (KnowBe4 Annual Phishing Report 2023).
- Après 12 mois de formation : le CTR tombe à 5 % en moyenne.
- Chaque jour supplémentaire de MTTD coûte en moyenne 5 000 $ en dommages supplémentaires pour une organisation de taille intermédiaire.
- NIS2 impose des reportings aux autorités nationales dans les 24h (alerte initiale), 72h (notification) et 1 mois (rapport final) — métriques réglementaires obligatoires.

## Flashcards
#flashcards/Cybersécurité/Métriques_de_sécurité #flashcards/Optimisation_du_SI/Métriques_de_sécurité

Qu'est-ce que le MTTD et pourquoi est-il l'indicateur le plus critique ? :: Mean Time To Detect : temps moyen entre le début d'une compromission et sa détection. C'est l'indicateur le plus critique car il mesure directement la fenêtre d'opportunité de l'attaquant. Chaque jour supplémentaire augmente l'étendue de la compromission. Objectif d'un SOC mature : < 24h pour les incidents critiques.

Quelle est la différence entre MTTR, MTTC et MTTF ? :: MTTR (Mean Time To Respond/Recover) est le temps total de résolution d'un incident. Il se décompose en MTTC (Mean Time To Contain : temps d'isolation de la menace) + MTTF (Mean Time To Fix : temps d'éradication et restauration). Le MTTC est prioritaire pour limiter la propagation.

Qu'est-ce que le CTR (Click-Through Rate) en sécurité et quel est l'objectif ? :: Pourcentage d'employés cliquant sur un lien lors d'une campagne de phishing simulé. Indicateur de la résistance humaine au phishing. Taux moyen initial : ~32 %. Objectif après programme de sensibilisation mature : < 5 % (KnowBe4, 2023).

Qu'est-ce que le Report Rate et pourquoi est-il plus positif que le CTR ? :: Taux de signalement de mails suspects au SOC. Mesure la culture de sécurité active (vs le CTR qui mesure les erreurs). Un report rate élevé transforme les employés en capteurs humains. Objectif : > 30 %. Complémentaire au CTR dans le Phishing Resilience Score.

Quels sont les SLA typiques d'un contrat MSSP ? :: Notification d'un incident P1 < 15-30 min, prise en charge < 15 min pour P1, résolution < 2-4h pour P1 selon criticité. Disponibilité du service : 99,9 %. Les SLA font l'objet de pénalités contractuelles et sont mesurés mensuellement.

Qu'est-ce que la Goodhart's Law appliquée aux métriques de sécurité ? :: "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure." Ex : si le SOC est évalué uniquement sur le nombre d'alertes traitées, les analystes peuvent clôturer rapidement les alertes sans investigation approfondie. Il faut toujours mesurer plusieurs métriques complémentaires.

Quels frameworks structurent les métriques de sécurité ? :: NIST CSF (métriques par fonction : Identify, Protect, Detect, Respond, Recover), ISO 27004 (métriques SMSI), CIS Controls v8 (métriques par contrôle). NIS2 impose des délais réglementaires : 24h alerte initiale, 72h notification, 1 mois rapport final.

## Sources
- IBM Cost of a Data Breach Report 2023
- Mandiant M-Trends 2024
- KnowBe4 — Annual Phishing by Industry Benchmarking Report 2023
- Gartner — Metrics That Matter for CISO Reporting 2023
- SANS Institute — Security Awareness Maturity Model
- NIST Cybersecurity Framework (CSF) 2.0 — https://www.nist.gov/cyberframework
- ISO/IEC 27004:2016 — Information security management: Monitoring, measurement, analysis and evaluation
- CIS Controls v8 — https://www.cisecurity.org

## Notions liées
- [[SOC]]
- [[Sensibilisation et facteur humain]]
- [[IA en cybersécurité]]
- [[EBIOS RM et gestion des risques cyber]]
- [[Threat Intelligence et Threat Hunting]]
- [[Red Team - Blue Team - Purple Team]]
