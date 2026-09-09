# Thème 10 — Optimisation du Système d'Information — Guide de révision complet

## Introduction

L'optimisation du Système d'Information, ou SI, est l'un des enjeux stratégiques majeurs pour toute organisation moderne. Un Système d'Information est l'ensemble organisé de ressources humaines, matérielles, logicielles, de procédures et de données permettant de collecter, stocker, traiter et distribuer l'information nécessaire au fonctionnement d'une organisation. Il est, en quelque sorte, le système nerveux de l'entreprise : il conditionne la prise de décision, la performance opérationnelle, la relation client et la compétitivité.

Ce thème couvre un spectre très large de notions, allant du pilotage de la performance par les indicateurs clés, à la gestion des services IT par les référentiels comme ITIL et VeriSM, en passant par l'amélioration continue avec le cycle PDCA et le Lean, l'automatisation et l'orchestration des processus, la veille stratégique, la gestion de projet, et la protection des données. Ces sujets sont profondément liés : optimiser un SI ne signifie pas seulement l'améliorer techniquement, mais aligner en permanence la technologie sur la valeur métier, tout en maîtrisant les risques et les coûts.

À l'heure où soixante-dix pour cent des projets de transformation SI échouent à atteindre leurs objectifs initiaux selon McKinsey, et où le coût moyen d'une heure d'indisponibilité SI est estimé à cinq mille six cents dollars par minute pour les grandes entreprises selon Gartner, la maîtrise de ces notions est à la fois une exigence professionnelle et un levier de différenciation stratégique.

---

## Notions clés

### Le Système d'Information : architecture et enjeux

Un Système d'Information s'articule autour de quatre fonctions fondamentales. La collecte correspond à l'acquisition des données via des capteurs, des formulaires, des interfaces de programmation applicative ou des progiciels de gestion intégrés. Le stockage recouvre les bases de données relationnelles, les bases NoSQL, les lacs de données et les archives. Le traitement englobe les calculs, les workflows et les règles métier. Enfin, la diffusion permet de restituer l'information via des tableaux de bord, des rapports, des API et des portails.

On distingue trois niveaux dans un Système d'Information, selon le modèle du chercheur Robert Anthony. Le niveau opérationnel traite les transactions quotidiennes, comme les progiciels de gestion intégrés ou les outils de gestion de la relation client. Le niveau tactique permet le pilotage et le reporting via la Business Intelligence. Le niveau stratégique sert l'aide à la décision grâce aux systèmes d'aide à la décision et aux tableaux de bord exécutifs.

En matière d'architecture, on oppose classiquement les architectures monolithiques, centralisées et peu évolutives, aux architectures orientées services, dites SOA pour Service-Oriented Architecture, et aux architectures microservices, où chaque service est autonome et déployable indépendamment. Une architecture orientée événements, dite event-driven, permet quant à elle une communication asynchrone entre composants.

Un indicateur essentiel pour piloter un Système d'Information est le ratio entre le budget consacré au maintien en condition opérationnelle, appelé le run, et celui consacré à l'innovation, appelé le build. En moyenne, soixante-dix pour cent des budgets IT sont absorbés par le run, ce qui laisse peu de place à la transformation. Rééquilibrer ce ratio est souvent le premier objectif d'une démarche d'optimisation.

### Les indicateurs clés de performance et le pilotage de la performance

Un indicateur clé de performance, ou KPI pour Key Performance Indicator en anglais, est un indicateur quantifiable permettant d'évaluer l'atteinte d'un objectif stratégique ou opérationnel. Il ne faut pas confondre un KPI avec un indicateur clé de risque, ou KRI pour Key Risk Indicator, qui mesure quant à lui l'exposition à un risque.

Le pilotage de la performance s'appuie sur plusieurs cadres complémentaires. Le Balanced Scorecard, conçu par Kaplan et Norton en 1992, équilibre quatre axes : l'axe financier, qui répond à la question de la perception par les actionnaires ; l'axe client, qui mesure la satisfaction et la fidélité ; l'axe des processus internes, qui évalue l'excellence opérationnelle ; et l'axe de l'apprentissage et de la croissance, qui mesure la capacité d'innovation.

Les Objectifs et Résultats Clés, ou OKR pour Objectives and Key Results, ont été popularisés par Intel puis adoptés par Google dès 1999. Un objectif est ambitieux, qualitatif et inspirant. Il est associé à trois à cinq résultats clés, qui sont des mesures vérifiables et quantifiables. Le score cible d'un OKR est de zéro virgule six à zéro virgule sept : un score parfait de un virgule zéro signifie que l'objectif n'était pas assez ambitieux.

La loi de Goodhart est un piège majeur du pilotage par indicateurs. Elle stipule que lorsqu'une mesure devient une cible, elle cesse d'être une bonne mesure. En pratique, cela conduit au gaming des métriques : un développeur va augmenter son nombre de commits inutilement pour améliorer son KPI, ou un centre d'appels va raccrocher prématurément pour réduire son indicateur de durée d'appel. Le remède consiste à diversifier les indicateurs et à mesurer les résultats réels, les outcomes, plutôt que les activités, les outputs. Il est également recommandé de ne pas dépasser cinq à sept KPI par niveau de management, pour éviter la paralysie décisionnelle par excès d'information.

On distingue aussi les indicateurs avancés, ou leading indicators, qui prédisent une performance future comme le nombre de tests automatisés écrits, des indicateurs retardés, ou lagging indicators, qui constatent une performance passée comme le chiffre d'affaires du trimestre.

### Les métriques de pilotage de projet

Les métriques de pilotage projet permettent de mesurer et d'optimiser la performance des équipes de développement logiciel. Les métriques de flux sont fondamentales. La vélocité mesure le nombre de points d'histoire, ou story points, livrés par sprint en méthode Agile. Le Lead Time est le temps écoulé entre la création d'une demande et sa livraison en production, depuis l'entrée dans le backlog jusqu'au déploiement. Le Cycle Time est le temps entre le début du travail actif et la livraison, c'est-à-dire le Lead Time moins le temps d'attente en backlog. Le Throughput mesure le nombre d'éléments livrés par unité de temps.

La loi de Little, issue du Lean, énonce que le Lead Time est égal au Work in Progress divisé par le Throughput. Son implication concrète est que limiter le travail en cours est le levier le plus puissant pour réduire le Lead Time, sans augmenter la capacité de l'équipe.

La méthode de la Valeur Acquise, ou Earned Value Management en anglais, est un cadre de contrôle de projet combinant périmètre, coût et délais. L'indice de performance des coûts, le CPI pour Cost Performance Index, est le ratio entre la valeur acquise et le coût réel. Un CPI inférieur à un signale un dépassement budgétaire. L'indice de performance des délais, le SPI pour Schedule Performance Index, est le ratio entre la valeur acquise et la valeur planifiée. Un SPI inférieur à un signale un retard.

Les quatre métriques DORA, issues du rapport annuel de l'organisation DevOps Research and Assessment, sont les références pour mesurer la performance DevOps : la fréquence de déploiement, le Lead Time for Changes, le taux d'échec des changements ou Change Failure Rate, et le temps moyen de récupération après incident, le MTTR. Les équipes élites déploient plusieurs fois par jour avec un Lead Time inférieur à une heure.

### Les frameworks de gestion de projet

Face à la complexité des Systèmes d'Information, des frameworks structurés de gestion de projet ont émergé pour standardiser les pratiques et réduire les risques. Soixante-dix pour cent des projets IT échouent ou dépassent le budget et les délais initiaux selon le Chaos Report du Standish Group.

Le PMBOK, pour Project Management Body of Knowledge, est édité par le PMI, le Project Management Institute. Sa version 6 définissait dix domaines de connaissance et quarante-neuf processus répartis en cinq groupes : démarrage, planification, exécution, surveillance et contrôle, clôture. La version 7, publiée en 2021, marque un changement majeur en passant à douze principes de management plus flexibles, mieux alignés avec les approches agiles.

PRINCE2, acronyme de Projects IN Controlled Environments, est édité par PeopleCert. Il repose sur sept principes, dont la justification business continue, le management par exception et le focus sur les produits livrables. Le principe du management par exception est sa spécificité : les décisions sont déléguées avec des seuils de tolérance, et on ne remonte à l'échelon supérieur qu'en cas de dépassement de ces tolérances.

SAFe, pour Scaled Agile Framework, permet d'appliquer l'Agile à grande échelle dans les organisations. Il s'organise en quatre niveaux : l'équipe, le programme, la grande solution et le portefeuille. L'élément central est l'Agile Release Train, ou ART, une équipe d'équipes de cinquante à cent vingt-cinq personnes qui planifient et livrent ensemble selon une cadence commune de dix semaines, appelée Program Increment. Le PI Planning est l'événement de deux jours où toutes les équipes d'un ART planifient ensemble le prochain Program Increment.

La norme ISO 21500, révisée en 2021 sous le numéro ISO 21502, est un référentiel générique international, compatible avec PMBOK, sans certification propre.

### SLA, SLO, SLI : la hiérarchie des engagements de service

Ces trois notions structurent la relation entre la Direction des Systèmes d'Information et ses clients internes ou externes. Le SLI, Service Level Indicator en anglais, est la mesure technique brute d'un aspect de la performance d'un service, par exemple le taux de disponibilité réel mesuré à quatre-vingt-dix-neuf virgule quatre-vingt-dix-sept pour cent. Le SLO, Service Level Objective, est l'objectif interne cible pour un SLI, par exemple une disponibilité supérieure ou égale à quatre-vingt-dix-neuf virgule neuf pour cent. Le SLO est toujours plus strict que le SLA, pour servir de filet de sécurité interne. Le SLA, Service Level Agreement, est le contrat formalisé avec le client, avec pénalités en cas de non-respect.

La notion d'error budget, ou budget d'erreur, est au cœur de la pratique SRE, Site Reliability Engineering. Si le SLO est de quatre-vingt-dix-neuf virgule neuf pour cent, l'error budget mensuel est de zéro virgule un pour cent multiplié par trente jours et vingt-quatre heures, soit quarante-trois virgule deux minutes par mois. Quand ce budget est épuisé, les déploiements sont gelés et la priorité passe à la fiabilité plutôt qu'aux nouvelles fonctionnalités.

Les chiffres des niveaux de service sont importants à connaître. Un SLA à quatre-vingt-dix-neuf virgule neuf pour cent, appelé three nines, autorise huit heures quarante-cinq minutes d'indisponibilité par an. Un SLA à quatre-vingt-dix-neuf virgule quatre-vingt-dix-neuf pour cent, appelé four nines, n'en autorise que cinquante-deux minutes. Un SLA à quatre-vingt-dix-neuf virgule quatre-vingt-dix-neuf-neuf pour cent, appelé five nines, n'autorise que cinq minutes quinze secondes par an, et son coût en infrastructure est souvent dix fois supérieur au three nines.

L'OLA, Operational Level Agreement, est un accord interne entre équipes IT qui soutient le SLA externe. Le XLA, Experience Level Agreement, est une évolution centrée sur l'expérience perçue par l'utilisateur, mesurée via le Net Promoter Score, le CSAT ou le Customer Effort Score, plutôt que sur des métriques purement techniques.

### MTTR et MTBF : piloter la disponibilité et la résilience

Le MTBF, Mean Time Between Failures, ou temps moyen entre deux pannes successives, mesure la fiabilité d'un système. Il se calcule en divisant le temps total de fonctionnement par le nombre de pannes. Le MTTR, Mean Time To Recover, mesure la résilience et la réactivité.

La formule de disponibilité est la suivante : la disponibilité est égale au MTBF divisé par la somme du MTBF et du MTTR, le tout multiplié par cent. Concrètement, avec un MTBF de mille heures et un MTTR d'une heure, on obtient une disponibilité de quatre-vingt-dix-neuf virgule neuf pour cent. Avec le même MTBF et un MTTR de dix heures, la disponibilité tombe à quatre-vingt-dix-neuf virgule zéro un pour cent. Cette formule démontre que réduire le MTTR a un impact plus rapide sur la disponibilité qu'augmenter le MTBF, car le MTTR est directement sous contrôle des équipes par l'automatisation et les runbooks.

La famille MTTR comprend quatre métriques distinctes. Le MTTA, Mean Time To Acknowledge, mesure le temps entre l'alerte et la prise en charge. Le MTTD, Mean Time To Detect, mesure le temps entre l'apparition du problème et sa détection. Le MTTR mesure le temps entre la détection et le retour à la normale. Le MTTF, Mean Time To Failure, s'applique aux systèmes non réparables.

En cybersécurité, le MTTD moyen mondial pour détecter une violation de données est de cent quatre-vingt-dix-sept jours selon le rapport IBM Cost of a Data Breach de 2023, et il faut en moyenne soixante-dix jours supplémentaires pour la remédiation. Ces chiffres justifient les investissements dans les outils de détection comme les SIEM, les EDR et les SOAR.

Le Chaos Engineering, popularisé par Netflix avec son outil Chaos Monkey, consiste à injecter délibérément des pannes en production pour tester la résilience réelle, pratiquer les runbooks et identifier les points de défaillance uniques, appelés Single Point of Failure ou SPOF.

### Veille stratégique et technologique

La veille stratégique est un processus continu et organisé de collecte, d'analyse et de diffusion d'informations sur l'environnement d'une organisation pour éclairer les décisions stratégiques. Quatre-vingt-dix pour cent de l'information stratégique est disponible en source ouverte, et les entreprises pratiquant la veille structurée prennent des décisions trois fois plus vite que leurs concurrents selon Forrester.

Le cycle de la veille comporte cinq étapes : la planification, qui définit les besoins et les axes de veille ; la collecte à partir de sources primaires et secondaires ; le traitement par filtrage, analyse et qualification ; la diffusion via newsletters, tableaux de bord ou alertes ; et enfin la décision, qui génère une rétroaction vers la planification.

On distingue quatre types de veille. La veille technologique surveille les innovations, les brevets et les nouvelles solutions via IEEE, arXiv et les dépôts de brevets. La veille concurrentielle analyse les stratégies des concurrents via les rapports annuels et LinkedIn. La veille réglementaire suit les lois et directives comme le Règlement Général sur la Protection des Données, NIS2 ou l'AI Act, via le Journal Officiel, l'ANSSI et EUR-Lex. La veille sociétale et de marché observe les tendances consommateurs et l'opinion publique.

L'intelligence économique est plus large que la veille : elle repose sur trois piliers, la collecte d'information via la veille, la protection du patrimoine informationnel, et l'influence stratégique sur l'environnement. En France, elle est coordonnée par le SISSE, Service de l'information stratégique et de la sécurité économiques, créé en 2016.

Le Hype Cycle de Gartner est un outil phare de la veille technologique. Il identifie cinq phases dans l'adoption d'une technologie : le déclencheur d'innovation, le pic des espoirs exagérés, le creux de la désillusion, la pente de l'illumination et le plateau de la productivité.

### Signal faible et OSINT

Le signal faible est un concept formalisé par Igor Ansoff en 1975. Il désigne une information précoce, ambiguë et fragmentaire annonçant un changement stratégique potentiel, noyée dans le bruit informationnel. Un signal faible se caractérise par son ambiguïté, pouvant avoir plusieurs interprétations, sa précocité, sa fragmentation et son faible volume.

Des exemples de signaux faibles en informatique incluent les recrutements massifs d'un concurrent sur un profil d'intelligence artificielle, signalant un pivot stratégique imminent ; des dépôts de brevets inhabituels d'un grand acteur technologique dans un nouveau domaine ; ou des discussions sur des forums spécialisés autour d'une vulnérabilité non encore référencée comme CVE.

L'OSINT, Open Source INTelligence, est la collecte et l'analyse de renseignements à partir de sources ouvertes et légalement accessibles, comme le web, les réseaux sociaux, les bases de données publiques ou les documents officiels. Il est distinct du HUMINT, renseignement humain, du SIGINT, renseignement sur les signaux, et du CYBINT, renseignement cyber. Soixante-cinq pour cent des cyberattaques sont précédées de signaux OSINT détectables.

Parmi les outils OSINT, Shodan est un moteur de recherche d'appareils connectés à internet indexant plus d'un virgule cinq milliard d'appareils et services exposés. Maltego cartographie les relations entre entités. Le Google Dorking utilise des opérateurs de recherche avancés pour trouver des informations sensibles indexées involontairement.

L'infobésité, terme popularisé par Alvin Toffler en 1970, désigne la surcharge informationnelle rendant la prise de décision difficile. La curation de contenu répond à ce problème en sélectionnant, organisant et contextualisant l'information pertinente.

### VUCA et benchmark

L'acronyme VUCA, issu du vocabulaire militaire américain des années quatre-vingt-dix, décrit un environnement caractérisé par quatre dimensions : la Volatilité, désignant des changements rapides et imprévisibles ; l'Incertitude, traduite par un manque d'information fiable ; la Complexité, liée à la multiplicité des acteurs et des interdépendances, notamment dans les Systèmes d'Information hybrides multicloud ; et l'Ambiguïté, résultant de signaux contradictoires sans précédent historique.

Face à VUCA, Bob Johansen a proposé le contre-modèle VUCA Prime, où chaque dimension reçoit une réponse managériale : la Vision face à la Volatilité, la Compréhension face à l'Incertitude, la Clarté face à la Complexité, et l'Agilité face à l'Ambiguïté.

Le benchmark, ou étalonnage concurrentiel, est une démarche structurée consistant à se comparer à des référentiels internes ou externes pour identifier des axes d'amélioration. En France, la norme AFNOR XP X50-053 de 1999 encadre cette démarche en six étapes : l'initialisation, la collecte interne, l'identification des partenaires de benchmark, la collecte externe, l'analyse des écarts appelée gap analysis, et enfin le plan d'action et le suivi.

Le benchmark est stratégique pour un Directeur des Systèmes d'Information car il objective la performance du SI, légitime les investissements et identifie les meilleures pratiques transposables. Ses limites résident dans le risque de copier une pratique sans l'adapter au contexte organisationnel propre.

### Amélioration continue : PDCA, Lean, Kaizen

L'amélioration continue est une philosophie de gestion visant à optimiser de façon itérative et permanente les processus, produits et services. Elle repose sur plusieurs cadres complémentaires.

Le cycle PDCA, ou cycle de Deming, du nom de William Edwards Deming qui en a popularisé l'usage, comprend quatre étapes. Plan consiste à identifier le problème, analyser les causes racines et définir le plan d'action. Do consiste à mettre en œuvre le plan à petite échelle. Check consiste à mesurer les résultats par rapport aux objectifs. Act consiste à standardiser si le résultat est satisfaisant, ou à ajuster et relancer un nouveau cycle dans le cas contraire.

Le Lean IT est l'application des principes du Toyota Production System au Système d'Information. Son objectif est d'éliminer les gaspillages, appelés muda en japonais, et de maximiser la valeur livrée. On identifie sept types de gaspillages transposés au Lean IT : la surproduction de fonctionnalités non utilisées, les temps d'attente dans les files de tickets, les transports inutiles de données redondantes, le sur-traitement par des processus bureaucratiques excessifs, les stocks de backlog non priorisé, les mouvements inutiles liés aux interfaces non ergonomiques, et les défauts sous forme de bugs et d'incidents.

Le Kaizen est la philosophie japonaise du changement en mieux, fondée sur de petites améliorations continues impliquant tous les acteurs. En pratique informatique, il se manifeste par des Kaizen blitz, des chantiers courts de deux à cinq jours sur un processus précis.

La Root Cause Analysis, ou analyse des causes racines, vise à éviter la récurrence des incidents. Ses deux méthodes principales sont les cinq Pourquoi, qui remontent la chaîne causale en posant la question pourquoi cinq fois, et le diagramme d'Ishikawa, qui cartographie les causes par catégories. La culture du post-mortem blameless, sans désignation de coupable, est essentielle pour créer un environnement psychologiquement sûr propice à l'apprentissage.

### Value Stream Mapping

La Value Stream Mapping, ou cartographie de la chaîne de valeur, est un outil visuel issu du Toyota Production System permettant de représenter toutes les étapes d'un flux, à valeur ajoutée et sans valeur ajoutée, pour délivrer un produit ou service. En moyenne, seulement vingt à trente pour cent du temps d'un processus informatique est à valeur ajoutée.

La réalisation d'une cartographie suit six étapes : sélectionner le flux à cartographier ; cartographier l'état actuel en documentant chaque étape, les temps de cycle et les temps d'attente ; calculer les indicateurs clés comme le Lead Time, le Process Time et le ratio valeur ajoutée sur non-valeur ajoutée ; identifier les gaspillages et les goulots d'étranglement ; concevoir l'état futur optimal ; et enfin mettre en œuvre un plan d'action.

Le Lean Six Sigma combine les principes Lean d'élimination des gaspillages avec le Six Sigma de réduction de la variabilité. Il s'appuie sur la démarche DMAIC : Define pour définir le problème, Measure pour collecter les données, Analyze pour identifier les causes racines, Improve pour implémenter les solutions, et Control pour pérenniser les gains.

Appliquée au DevOps, la cartographie de la chaîne de valeur permet de visualiser le flux depuis le commit du développeur jusqu'au déploiement en production, en identifiant les délais d'attente, les approbations manuelles et les goulots d'étranglement. Les équipes DevOps ayant réalisé cette démarche réduisent leur Lead Time de déploiement de soixante pour cent en médiane selon le rapport DORA.

### VeriSM : un méta-cadre de gestion des services

VeriSM, acronyme de Value-driven, Evolving, Responsive, Integrated Service Management, est un modèle de gestion des services IT publié en 2017 par l'IFDC, la Fondation internationale des compétences numériques. Il propose une approche intégrée, adaptative et orientée valeur permettant aux organisations de combiner librement différents référentiels, ITIL, Agile, DevOps, Lean ou COBIT, plutôt qu'en appliquer un seul de façon rigide.

Les quatre composants du modèle VeriSM sont la Gouvernance, qui définit les règles, politiques et responsabilités ; les Principes de gestion des services, qui constituent le cadre de valeurs commun ; le Management Mesh, ou maillage de management, qui est le cœur du modèle et combine dynamiquement l'environnement, les ressources, les pratiques de management et les technologies émergentes ; et la Culture organisationnelle, fondée sur la collaboration et la confiance.

Le cycle de livraison de service VeriSM comprend quatre étapes en boucle continue : Define pour définir les exigences du service en lien avec la stratégie ; Produce pour concevoir et développer le service ; Provide pour déployer et opérer le service ; et Respond pour mesurer, apprendre et améliorer.

VeriSM répond à un besoin réel : soixante-dix pour cent des Directeurs des Systèmes d'Information déclarent utiliser plus de trois référentiels différents simultanément selon Gartner. VeriSM évite le piège du tout ITIL ou du tout Agile en favorisant une gouvernance orientée résultats.

### Les outils ITSM : IT Service Management

Les outils d'IT Service Management sont des plateformes logicielles qui automatisent, centralisent et optimisent la gestion des services informatiques. Ils couvrent les processus clés définis par ITIL : gestion des incidents, des problèmes, des changements, des actifs, des configurations via une base de données de configuration appelée CMDB, et du catalogue de services.

ServiceNow est le leader mondial du marché ITSM avec plus de huit milliards de dollars de revenus annuels en 2023 et une adoption par quatre-vingt-cinq pour cent des entreprises du Fortune 500. C'est une plateforme cloud en mode SaaS multi-tenant qui couvre l'ITSM, l'ITOM pour les opérations IT, l'ITAM pour les actifs, les ressources humaines, la sécurité et la gestion de la relation client. Sa plateforme Now intègre des capacités low-code et no-code pour créer des workflows personnalisés, ainsi qu'une intelligence artificielle générative appelée Now Assist.

Jira Service Management d'Atlassian est orienté vers les équipes DevOps et les petites et moyennes entreprises. Il offre une intégration native avec l'écosystème Atlassian, notamment Jira Software, Confluence et Bitbucket, ainsi qu'une gestion des alertes via Opsgenie. Son avantage clé est le pont naturel entre les opérations IT et le développement.

La CMDB, Configuration Management Database, est une base de données centralisant les actifs IT appelés Configuration Items ou CI, et leurs dépendances. Elle est indispensable pour l'analyse d'impact avant un changement ou lors d'un incident.

Le Change Advisory Board, ou CAB, est le comité qui évalue et approuve les changements planifiés pour minimiser le risque en production. C'est un processus central de la gestion des changements ITSM.

Les métriques clés pilotées par un outil ITSM sont le MTTR pour la résolution, le MTTD pour la détection, le taux de résolution au premier contact appelé FCR pour First Call Resolution Rate, et la conformité aux engagements de niveau de service.

### Orchestration et automatisation

L'orchestration désigne la coordination automatisée de systèmes, services et processus hétérogènes pour exécuter des workflows complexes. Elle va au-delà de la simple automatisation d'une tâche isolée. L'automatisation est l'exécution autonome d'une tâche sans intervention humaine. L'hyperautomation, concept de Gartner, est une approche combinant la RPA, le Robotic Process Automation, l'intelligence artificielle, le Machine Learning, le Process Mining, les suites de gestion des processus métier et le low-code pour automatiser le maximum de processus de bout en bout.

Kubernetes est l'orchestrateur de conteneurs de référence, utilisé par quatre-vingt-seize pour cent des organisations cloud-native selon l'enquête annuelle de la Cloud Native Computing Foundation. Il automatise le déploiement, le scaling, la mise à jour par roulement et l'auto-guérison des applications conteneurisées. Ses fonctionnalités clés sont le rolling update, l'autoscaling horizontal et vertical, le self-healing et la découverte de services.

Apache Airflow est l'orchestrateur de workflows de données de référence. Il modélise les pipelines de données sous forme de graphes orientés acycliques, appelés DAG pour Directed Acyclic Graph, définis en Python. Il est utilisé pour les pipelines ETL, les pipelines de Machine Learning et les vérifications de qualité des données.

La RPA, Robotic Process Automation, automatise les tâches répétitives sur des interfaces graphiques sans modifier les applications existantes. Les trois leaders du marché sont UiPath, Automation Anywhere et Blue Prism. La RPA génère un retour sur investissement moyen de deux cent cinquante pour cent sur trois ans selon Forrester.

Les organisations automatisant leurs pipelines d'intégration et de déploiement continu déploient deux cent huit fois plus fréquemment selon le rapport DORA de 2023.

### ISO 9001 et qualité

La norme ISO 9001, dans sa version 2015, est la norme internationale de référence pour les systèmes de management de la qualité. Elle est la plus certifiée au monde, avec plus d'un million de certifications dans cent soixante-dix pays. Elle définit sept principes : l'orientation client, le leadership, l'implication du personnel, l'approche processus, l'amélioration continue, la prise de décision fondée sur des preuves, et le management des relations avec les parties intéressées.

Sa structure, appelée HLS pour High Level Structure, est commune à toutes les normes ISO de management, ce qui facilite les intégrations multi-normes comme avec ISO 27001 pour la sécurité de l'information ou ISO 14001 pour l'environnement. Le cycle PDCA se reflète directement dans sa structure : les chapitres quatre à sept correspondent au Plan, le chapitre huit au Do, le chapitre neuf au Check et le chapitre dix au Act.

La certification suit un cycle de trois ans avec des audits de surveillance annuels, réalisés par des organismes accrédités comme Bureau Veritas, l'AFNOR Certification ou SGS. La réduction moyenne des coûts de non-qualité après certification est de vingt à trente pour cent. Philip Crosby estimait que le coût de la non-qualité représentait en moyenne cinq à huit pour cent du chiffre d'affaires d'une entreprise.

Pour une Direction des Systèmes d'Information, ISO 9001 structure les processus de gestion des projets, des incidents et des changements. Les indicateurs qualité typiques sont le taux de disponibilité, le MTTR, la satisfaction utilisateur via le Net Promoter Score, et le taux de déploiements sans incident.

### Les acteurs de la cybersécurité : éditeurs et solutions

La protection du Système d'Information passe par la maîtrise du paysage des éditeurs de cybersécurité. Le marché mondial dépasse cent quatre-vingt-dix milliards de dollars en 2023.

Darktrace, fondée au Royaume-Uni en 2013, se spécialise dans l'intelligence artificielle comportementale qui modélise le comportement normal de chaque entité du réseau et détecte toute déviation. Son approche permet de détecter des menaces inconnues, appelées zero-day, ou des menaces internes.

CrowdStrike, fondée aux États-Unis en 2011, propose la plateforme Falcon, un EDR et XDR cloud-native. Son avantage réside dans sa Threat Intelligence de référence mondiale et ses performances en évaluation MITRE ATT&CK. L'incident de juillet 2024, où une mise à jour défectueuse a provoqué huit millions cinq cent mille pannes de systèmes Windows simultanément, illustre les risques de concentration et de mise à jour automatique des solutions de sécurité.

SentinelOne se distingue par sa réponse autonome sans intervention humaine, grâce à sa technologie Storyline qui corrèle automatiquement les événements d'une attaque.

Du côté des acteurs souverains français, Sekoia.io, fondée en 2018, propose une plateforme SOC cloud-native certifiée SecNumCloud par l'ANSSI, intégrant une Cyber Threat Intelligence riche et des playbooks automatisés. HarfangLab propose un EDR souverain certifié CSPN par l'ANSSI, déployable en local, avec une transparence partielle du code.

Pour la sensibilisation des utilisateurs, KnowBe4 est la plus grande plateforme mondiale de formation à la cybersécurité avec soixante-cinq mille clients, proposant des simulations de phishing et des formations gamifiées. Cofense se spécialise dans la réponse aux incidents de phishing avec un réseau de trente-cinq millions d'utilisateurs formés. Mailinblack est la solution française souveraine de protection des messageries, ciblant les petites et moyennes entreprises et le secteur public.

Orange Cyberdefense est le leader MSSP, Managed Security Service Provider, européen, avec dix-huit pays de présence et trois mille experts cyber. Thales intervient notamment pour les acteurs de défense et les Opérateurs d'Importance Vitale, les OIV.

### Sauvegarde et protection des données

La sauvegarde est la dernière ligne de défense contre les ransomwares : quatre-vingt-treize pour cent des attaques ransomware ciblent les sauvegardes pour empêcher la restauration selon le rapport Veeam Ransomware Trends de 2023.

Deux concepts sont fondamentaux. Le RPO, Recovery Point Objective, désigne la perte de données maximale acceptable, exprimée en temps, par exemple une heure signifie qu'on peut restaurer jusqu'à une heure avant l'incident. Le RTO, Recovery Time Objective, désigne le délai maximal acceptable pour restaurer le service après un incident.

La règle 3-2-1-1-0 est la bonne pratique de référence : trois copies des données, sur deux supports différents, avec une copie hors site, une copie offline ou immuable avec air gap, et zéro erreur lors des tests de restauration.

L'immuabilité des sauvegardes est le mécanisme clé contre les ransomwares : des backups immuables, conformes aux technologies WORM pour Write Once Read Many, Object Lock sur Amazon S3 ou Hardened Repository, ne peuvent être ni modifiés ni supprimés pendant une période définie, même par un attaquant ayant compromis les accès administrateur.

La protection continue des données, ou CDP pour Continuous Data Protection, capture chaque écriture en temps réel et permet un RPO quasi nul de l'ordre de quelques secondes.

Veeam est le leader mondial de la sauvegarde, protégeant plus de quatre cent cinquante mille clients. Ses fonctionnalités clés sont l'Instant VM Recovery, le SureBackup pour les tests automatiques de restauration et le Hardened Linux Repository pour l'immuabilité. Rubrik se différencie par son approche Zero Trust Data Security, avec des sauvegardes architecturalement immuables by design, et le Threat Hunting qui scanne les backups à la recherche d'indicateurs de compromission.

---

## Questions du jury

Les questions suivantes représentent les angles d'attaque les plus fréquents pour ce thème au Grand Oral.

Comment optimiser un Système d'Information sans passer par le cloud ? L'optimisation peut emprunter de nombreuses voies sans migration cloud : l'automatisation des processus via la RPA et les pipelines CI/CD, l'application de l'amélioration continue PDCA et Lean pour éliminer les gaspillages, la mise en place d'un outil ITSM pour structurer la gestion des incidents et des changements, l'adoption d'une démarche qualité ISO 9001, et le pilotage rigoureux par les KPI et les SLA.

ITIL 4 et COBIT, comment choisir son référentiel de gouvernance IT ? ITIL 4 est centré sur la gestion des services IT et les pratiques opérationnelles. COBIT est centré sur la gouvernance IT au niveau du Conseil d'administration et des dirigeants, alignant IT et stratégie d'entreprise. Les deux sont complémentaires : COBIT pose le cadre de gouvernance, ITIL détaille l'exécution opérationnelle.

Quels KPI sont les plus pertinents pour piloter un projet IT ? Les KPI les plus pertinents combinent des indicateurs de flux comme le Lead Time et le Cycle Time, des indicateurs de qualité comme le Change Failure Rate et le MTTR, des indicateurs financiers comme le CPI en méthode de la Valeur Acquise, et des indicateurs de satisfaction comme le Net Promoter Score. Il faut viser cinq à sept KPI maximum par niveau de management pour rester actionnable.

Comment mettre en place une veille technologique efficace dans une Direction des Systèmes d'Information ? Une veille efficace repose sur le cycle en cinq étapes : planifier les axes prioritaires, collecter via des outils d'agrégation comme Feedly Pro ou Digimind, traiter en filtrant les signaux pertinents, diffuser vers les bonnes parties prenantes, et déclencher des décisions actionnables. La qualification des sources et la lutte contre l'infobésité par la curation sont essentielles.

Qu'est-ce que l'amélioration continue appliquée au SI ? C'est l'application systématique du cycle PDCA à chaque incident, chaque sprint et chaque processus. Concrètement : des rétrospectives agiles après chaque sprint, des post-mortems blameless après chaque incident majeur, des chantiers Kaizen sur les processus à faible valeur ajoutée, et des indicateurs DORA pour mesurer la progression DevOps.

Quelle est la différence entre SLA, SLO et SLI et comment les utiliser ? Le SLI est la mesure technique brute. Le SLO est l'objectif interne plus strict que le SLA, qui crée un filet de sécurité et définit l'error budget. Le SLA est le contrat avec le client. La hiérarchie SLI vers SLO vers SLA permet de détecter une dégradation bien avant de violer un engagement contractuel.

Comment l'automatisation optimise-t-elle le Système d'Information ? L'automatisation agit sur plusieurs leviers : réduction des erreurs humaines, accélération des cycles de déploiement, libération des équipes pour les tâches à valeur ajoutée, et disponibilité accrue par l'auto-healing Kubernetes. La RPA automatise les processus répétitifs, les pipelines CI/CD accélèrent le delivery, et l'hyperautomation vise l'automatisation de bout en bout avec l'IA.

VUCA : comment piloter un SI dans un environnement incertain ? En appliquant le VUCA Prime de Bob Johansen : la Vision pour contrer la Volatilité, la Compréhension pour contrer l'Incertitude, la Clarté pour contrer la Complexité et l'Agilité pour contrer l'Ambiguïté. Concrètement, cela se traduit par une gouvernance agile, un benchmark régulier des pratiques sectorielles, et une veille stratégique pour anticiper les ruptures.

Comment mesurer le MTTR et le MTBF et améliorer la disponibilité du SI ? Le MTBF se calcule en divisant le temps de fonctionnement total par le nombre de pannes. Le MTTR se mesure depuis la détection jusqu'au retour à la normale. Pour améliorer la disponibilité, on peut augmenter le MTBF par l'architecture redondante, et surtout réduire le MTTR par l'automatisation des runbooks, le ChatOps et le Chaos Engineering pour s'entraîner régulièrement.

---

## Points de vigilance

Plusieurs pièges conceptuels méritent une attention particulière à l'oral.

La confusion entre SLA, SLO et SLI est très fréquente. Retenir la hiérarchie dans l'ordre SLI vers SLO vers SLA, et le fait que le SLO est toujours plus exigeant que le SLA.

La loi de Goodhart doit être systématiquement mentionnée dès qu'on parle de KPI. Sans cette nuance, le propos paraît naïf.

Ne pas confondre Lead Time et Cycle Time. Le Lead Time part de la création du ticket, le Cycle Time part du début du travail actif.

Le MTTR est souvent présenté comme une métrique unique, alors qu'il s'agit d'une famille comprenant le MTTD, le MTTA et le MTTR au sens strict.

VeriSM est souvent inconnu des jurés eux-mêmes : l'expliquer clairement comme un méta-cadre qui intègre ITIL, Agile et DevOps sans les remplacer est un bon point de distinction.

Sur la sauvegarde, l'immuabilité et la règle 3-2-1-1-0 sont les éléments différenciants par rapport à une réponse basique qui ne mentionnerait que le backup simple.

Concernant les acteurs cybersécurité, la distinction entre solutions souveraines françaises, HarfangLab et Sekoia.io certifiés ANSSI, et solutions américaines dominantes, CrowdStrike et SentinelOne, est particulièrement pertinente dans le contexte réglementaire NIS2.

Sur l'automatisation, il est important de distinguer les niveaux : l'automatisation d'une tâche isolée par un script, la RPA qui agit sur des interfaces graphiques, l'orchestration qui coordonne des systèmes hétérogènes comme Kubernetes ou Airflow, et l'hyperautomation qui vise la transformation de bout en bout.

Enfin, l'ISO 9001 n'est pas une norme spécifiquement informatique : elle s'applique à toute organisation, et c'est sa complémentarité avec ISO 20000 pour l'ITSM et ISO 27001 pour la sécurité qui crée un système de management intégré cohérent pour une Direction des Systèmes d'Information.

---

*Document généré pour révision audio NotebookLM — Thème 10 : Optimisation du Système d'Information — 18 notions consolidées.*
