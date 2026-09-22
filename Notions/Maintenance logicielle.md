---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Maintenance logicielle

![[N — Maintenance logicielle.mp3]]
## En bref
> **Définition** : La maintenance logicielle désigne l'ensemble des activités réalisées après la livraison d'un logiciel pour corriger des défauts, améliorer les performances, adapter l'environnement ou ajouter de nouvelles fonctionnalités. Elle est normalisée par l'ISO 14764 et représente la phase la plus longue du cycle de vie logiciel.
> **Pourquoi c'est important** : Dans une DSI, la maintenance représente la majorité du budget informatique. Mal gérée, elle conduit à l'accumulation de dette technique et à l'obsolescence des systèmes. La comprendre permet d'optimiser les ressources, de justifier les investissements de modernisation et de maintenir la qualité opérationnelle.
> **Chiffres clés** :
> - La maintenance représente en moyenne **60 à 80 % du coût total** d'un logiciel sur son cycle de vie (Pigoski, 1996 ; IEEE).
> - Selon Lehman, un logiciel doit évoluer continuellement sous peine de devenir progressivement **moins utile** — c'est la 1ère loi de Lehman.
> - Le coût annuel de la maintenance des systèmes **legacy** aux États-Unis est estimé à **337 Md$** (GAO, 2019, pour le seul gouvernement fédéral).

## Approfondir

### Fonctionnement

#### Les 4 types de maintenance (ISO 14764)
La norme **ISO/IEC 14764:2006** (basée sur les travaux d'Lientz & Swanson, 1978) définit 4 types :

| Type | Description | Part du budget |
|------|-------------|----------------|
| **Corrective** | Correction de défauts et bugs détectés en production | ~20 % |
| **Adaptative** | Adaptation à un nouvel environnement (OS, SGBD, cloud, loi) | ~25 % |
| **Perfective** | Amélioration des performances ou ajout de fonctionnalités demandées | ~50 % |
| **Préventive** | Refactoring, mise à jour des dépendances, réduction de la dette technique | ~5 % |

La maintenance perfective est la plus consommatrice de ressources ; la préventive est souvent négligée alors qu'elle évite des coûts futurs bien plus élevés.

#### Les lois de Lehman (1974–1996)
Manny Lehman a formulé 8 lois empiriques sur l'évolution des systèmes logiciels "E-type" (systèmes en interaction avec le monde réel) :

1. **Changement continu** : un logiciel doit continuellement s'adapter ou devenir progressivement moins utile.
2. **Complexité croissante** : sans effort explicite pour la contrôler, la complexité d'un système augmente au fil des évolutions.
3. **Auto-régulation** : les attributs du processus d'évolution sont stables et statistiquement mesurables.
4. **Conservation de la stabilité organisationnelle** : le taux d'activité moyen reste constant sur la durée de vie du projet.
5. **Conservation de la familiarité** : la quantité de changements par release reste approximativement constante.
6. **Croissance continue** : les fonctionnalités doivent augmenter continuellement pour maintenir la satisfaction utilisateur.
7. **Qualité déclinante** : sans maintenance active, la qualité perçue d'un logiciel diminue.
8. **Système de rétroaction** : les processus d'évolution sont des systèmes multi-boucles de rétroaction.

#### Processus de maintenance (ISO 14764)
ISO 14764 définit le processus de maintenance en phases :
1. **Analyse de l'impact** : évaluation de l'effort et des risques de la modification.
2. **Implémentation** : développement de la modification.
3. **Revue et test** : validation de la correction ou de l'amélioration.
4. **Livraison** : déploiement en production.
5. **Clôture** : documentation et archivage.

#### Relation avec ITIL (gestion des changements)
En entreprise, la maintenance logicielle s'articule avec les processus ITIL v4 :
- **Incident Management** → déclenche la maintenance corrective.
- **Change Management** → encadre les maintenances adaptatives et perfectives.
- **Problem Management** → identifie les causes racines et oriente la maintenance préventive.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Prolonge la durée de vie d'investissements logiciels existants | Coût élevé et croissant avec le temps (effet de la 2e loi de Lehman) |
| La maintenance préventive réduit la dette technique | La maintenance corrective perturbe les plannings de développement |
| Améliore la satisfaction utilisateur (perfective) | Les systèmes legacy deviennent difficiles à maintenir (manque de documentation, technologies obsolètes) |
| Cadre normatif ISO 14764 pour les contrats TMA | Risque de "maintenance infinie" sans décision de remplacement |
| Permet d'adapter les systèmes aux nouvelles réglementations | Perte de compétences sur les technologies anciennes (COBOL, mainframe) |

### Acteurs et solutions du marché
- **TMA (Tierce Maintenance Applicative)** : Atos, Sopra Steria, CGI, Capgemini — prestations de maintenance externalisée avec SLA contractuels.
- **Outils de gestion des incidents/changements** : ServiceNow, Jira Service Management, BMC Remedy.
- **Outils d'analyse d'impact** : CAST Imaging (cartographie applicative), SonarQube (dette technique).
- **Plateformes de monitoring** : Datadog, Dynatrace, New Relic — détection proactive des anomalies déclenchant la maintenance corrective.
- **GitHub Dependabot / Snyk** : automatisation de la maintenance adaptative sur les dépendances (CVE, versions obsolètes).

### Cas d'usage concrets
1. **Maintenance adaptative — RGPD** : en 2018, des milliers d'applications doivent intégrer les exigences RGPD (gestion du consentement, droit à l'oubli). Cette maintenance adaptative a représenté des millions d'euros pour les grandes DSI françaises, illustrant l'impact des contraintes réglementaires sur les budgets de maintenance.
2. **Maintenance corrective en production** : une banque subit un incident P1 sur son système de paiement. L'équipe de TMA applique le processus ISO 14764 : analyse d'impact (30 min), correctif en environnement isolé (2h), tests de régression automatisés (1h), déploiement en production et monitoring renforcé pendant 24h.
3. **Maintenance préventive planifiée** : une DSI consacre 20 % de sa capacité d'une équipe à la maintenance préventive : mise à jour trimestrielle des dépendances, refactoring des modules identifiés par SonarQube comme à dette élevée, migration de Java 8 vers Java 21. Résultat : réduction de 40 % des incidents de production en 2 ans.

### Chiffres et tendances
- La **dette technique** mondiale est estimée à **1 500 Md$** (CAST Software, 2022), illustrant l'ampleur du retard de maintenance préventive accumulé.
- Les applications de plus de **15 ans** représentent 40 % des systèmes d'information des grandes entreprises françaises (Syntec Numérique).
- Les contrats de **TMA** représentent environ **30 % du marché des services informatiques** en France (Syntec Numérique, 2023).

## Flashcards
#flashcards/Développement/Maintenance_logicielle
Quels sont les 4 types de maintenance définis par ISO 14764 ? :: **Corrective** (bugs), **Adaptative** (nouvel environnement/réglementation), **Perfective** (amélioration/nouvelles fonctionnalités), **Préventive** (refactoring, réduction de dette technique).

Quelle est la 1ère loi de Lehman sur l'évolution logicielle ? :: **Loi du changement continu** : un logiciel E-type doit continuellement s'adapter à son environnement, sans quoi il devient progressivement moins satisfaisant et moins utile.

Quelle est la 2e loi de Lehman et ses implications pour la maintenance ? :: **Loi de la complexité croissante** : sans effort actif pour la maîtriser, la complexité d'un logiciel augmente à chaque évolution — ce qui justifie la maintenance préventive (refactoring).

Quelle proportion du coût total d'un logiciel la maintenance représente-t-elle sur son cycle de vie ? :: Entre **60 et 80 %** du coût total du logiciel, selon les études IEEE et Pigoski (1996).

Quelle norme internationale encadre la maintenance logicielle ? :: **ISO/IEC 14764:2006** — Software Engineering : Software Life Cycle Processes — Maintenance.

Qu'est-ce que la TMA et quels acteurs la proposent en France ? :: La **Tierce Maintenance Applicative** est l'externalisation de la maintenance à un prestataire tiers, avec SLA contractuels. Acteurs : Atos, Sopra Steria, CGI, Capgemini.

Quel type de maintenance est le plus souvent négligé malgré son impact préventif sur les coûts ? :: La maintenance **préventive** (refactoring, mise à jour des dépendances, réduction de dette technique), qui ne représente que ~5 % des budgets mais évite des coûts bien plus élevés à terme.

## Sources
- ISO/IEC 14764:2006 — Software Engineering: Software Life Cycle Processes — Maintenance.
- Lientz, B.P. & Swanson, E.B. (1980). *Software Maintenance Management*. Addison-Wesley.
- Lehman, M.M. & Ramil, J.F. (2001). *Rules and Tools for Software Evolution Planning and Management*. Annals of Software Engineering.
- Pigoski, T.M. (1996). *Practical Software Maintenance*. IEEE Computer Society Press.
- GAO (2019). *Federal Agencies Need to Address Aging Legacy Systems*. GAO-19-471.
- CAST Software (2022). *CAST Highlight State of Software Intelligence Report*.

## Notions liées
- [[Dette technique]]
- [[Clean Code et refactoring]]
- [[Qualité logicielle — normes et modèles]]
- [[CMMI]]
- [[Architecture logicielle]]
