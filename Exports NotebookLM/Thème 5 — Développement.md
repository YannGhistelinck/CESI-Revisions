# Thème 5 — Développement
## Export consolidé pour NotebookLM — Grand Oral CESI MAALSI

---

## Introduction

Le thème Développement couvre l'ensemble des pratiques, méthodes et technologies qui permettent de concevoir, livrer et maintenir des logiciels de qualité à grande échelle. C'est le domaine de compétence central du profil MAALSI et le socle technique de la transformation numérique des organisations.

Ce thème s'articule autour de six grandes familles de notions. La première concerne la qualité logicielle au sens large : les normes internationales qui la définissent, les modèles de maturité qui la structurent, et les pratiques de code qui la produisent au quotidien. La deuxième aborde l'architecture logicielle, depuis les décisions structurantes (monolithe ou microservices) jusqu'aux patterns de conception avancés comme le Domain-Driven Design. La troisième famille regroupe les pratiques DevOps dans leur sens le plus large : intégration continue et déploiement continu, sécurité intégrée au pipeline, gestion de l'infrastructure par le code, et observabilité des systèmes en production. La quatrième concerne la fiabilité opérationnelle, avec le Site Reliability Engineering, les métriques DORA, le Chaos Engineering et le Platform Engineering. La cinquième aborde les tests logiciels et leur automatisation par l'intelligence artificielle. La sixième et dernière famille couvre les technologies émergentes que sont la réalité étendue, le jumeau numérique et leur application dans le contexte de l'Industrie 4.0.

Ces notions ne sont pas indépendantes : un code de qualité (Clean Code, SOLID) est la condition du TDD (Test-Driven Development) ; le TDD est la condition d'un pipeline d'intégration continue fiable ; un pipeline fiable est la condition du déploiement fréquent ; et le déploiement fréquent, mesuré par les métriques DORA, est la condition de la performance DevOps. Comprendre ces enchaînements, et savoir les articuler devant un jury, est l'objectif de ce document.

---

## Notions clés

### 1. Qualité logicielle — normes et modèles

La qualité logicielle désigne l'ensemble des propriétés d'un logiciel lui permettant de satisfaire des besoins exprimés ou implicites. Elle est évaluée selon des modèles normalisés qui structurent les critères de qualité en caractéristiques mesurables.

L'histoire de la normalisation de la qualité logicielle commence avec le modèle de McCall en 1977, qui organise les critères selon trois axes : l'opération du produit (correction, fiabilité, efficacité, intégrité, facilité d'utilisation), la révision du produit (maintenabilité, flexibilité, testabilité), et la transition du produit (portabilité, réutilisabilité, interopérabilité). En 1978, Boehm étend ce modèle en introduisant explicitement les compromis entre caractéristiques, par exemple entre efficacité et portabilité. En 1987, Grady chez Hewlett-Packard formalise l'acronyme FURPS Plus, qui signifie Fonctionnalité, Utilisabilité, Fiabilité, Performance, Maintenabilité, et qui est encore aujourd'hui utilisé pour rédiger les exigences non fonctionnelles dans les appels d'offres.

La norme de référence actuelle est l'ISO 25010, publiée en 2011 dans le cadre de la famille SQuaRE, qui signifie Systems and software Quality Requirements and Evaluation, et révisée en 2023. Elle définit huit caractéristiques de qualité principales : l'adéquation fonctionnelle, l'efficacité de performance, la compatibilité, la facilité d'utilisation, la fiabilité, la sécurité, la maintenabilité et la portabilité. La révision de 2023 y ajoute la sûreté fonctionnelle, en réponse aux enjeux des systèmes embarqués et de l'intelligence artificielle. Cette norme distingue la qualité interne (propriétés du code source, mesurées par des outils d'analyse statique), la qualité externe (comportement observable à l'exécution), et la qualité en utilisation (satisfaction de l'utilisateur dans son contexte réel).

Pour une Direction des Systèmes d'Information, ces normes servent de langage commun dans les appels d'offres, de grille d'évaluation pour les prestataires, et de base de référence pour les outils de Quality Gate en pipeline de déploiement. L'outil le plus répandu pour automatiser ces mesures est SonarQube, qui calcule une note de maintenabilité, fiabilité et sécurité alignée sur l'ISO 25010. Un chiffre important à retenir : les défauts non détectés en phase de conception coûtent en moyenne cent fois plus cher à corriger en production, selon l'étude du NIST de 2002.

### 2. CMMI — Capability Maturity Model Integration

Le CMMI, qui signifie Capability Maturity Model Integration, est un référentiel d'amélioration des processus organisationnels développé par le SEI, le Software Engineering Institute de Carnegie Mellon. Il décrit un ensemble de bonnes pratiques permettant à une organisation de mesurer et d'améliorer la maturité de ses processus de développement, de services ou d'acquisition.

Le CMMI définit cinq niveaux de maturité. Le niveau 1, appelé Initial, caractérise des processus imprévisibles, réactifs, où le succès dépend des individus. Le niveau 2, Géré, correspond à des processus planifiés et contrôlés au niveau de chaque projet. Le niveau 3, Défini, est le plus important en pratique : les processus sont standardisés à l'échelle de toute l'organisation, documentés et formalisés. Le niveau 4, Quantitativement géré, introduit le contrôle statistique des processus. Le niveau 5, Optimisant, correspond à l'amélioration continue pilotée par les données.

L'évaluation officielle suit la méthode SCAMPI, Standard CMMI Appraisal Method for Process Improvement, en trois classes : la classe A, qui est la seule certifiable, conduite par un Lead Appraiser accrédité ; la classe B, intermédiaire et non certifiable ; et la classe C, qui est une auto-évaluation rapide.

En France, le CMMI est principalement présent dans les secteurs défense, spatial et systèmes critiques : Thales, Airbus et le CNES imposent à leurs sous-traitants un niveau CMMI 3 minimum. Les organisations de niveau CMMI 3 et au-delà constatent en moyenne une réduction de 34 % des défauts et 19 % de gains de productivité. La version 2.0 du CMMI, publiée en 2018 par le CMMI Institute devenu filiale d'ISACA, intègre explicitement les pratiques agiles comme preuves acceptables pour certains domaines de processus.

### 3. Analyse de code — SAST et DAST

L'analyse de code regroupe les techniques permettant de détecter automatiquement des défauts, des vulnérabilités et des violations de bonnes pratiques dans un logiciel. Le SAST, Static Application Security Testing ou test de sécurité applicative statique, analyse le code source sans l'exécuter. Le DAST, Dynamic Application Security Testing ou test de sécurité applicative dynamique, analyse l'application en cours d'exécution en simulant des attaques externes.

Le SAST fonctionne par analyse syntaxique du code source, construction d'un arbre syntaxique abstrait (AST), analyse des flux de données pour suivre les entrées utilisateurs jusqu'aux sorties sensibles, et application de règles prédéfinies issues des listes de vulnérabilités communes (CWE et OWASP Top 10). Son avantage principal est l'analyse exhaustive du code, sa limite principale est un taux élevé de faux positifs, entre vingt et cinquante pour cent selon les outils.

Le DAST teste l'application comme le ferait un attaquant extérieur, en envoyant des requêtes malformées (injections SQL, XSS, CSRF) et en analysant les réponses. Il détecte les vulnérabilités réelles dans l'environnement d'exécution avec peu de faux positifs, mais ne couvre pas le code non exposé aux entrées externes.

Deux autres catégories complètent ces deux approches. L'IAST, Interactive Application Security Testing, instrumente l'application pendant les tests fonctionnels pour combiner les avantages du SAST et du DAST. Le SCA, Software Composition Analysis, analyse les dépendances open source et détecte les vulnérabilités connues (CVE) qui leur sont associées.

Le principe fondamental du DevSecOps est le "shift-left" en matière de sécurité : intégrer les contrôles de sécurité le plus tôt possible dans le cycle de développement, dès l'IDE pour le SAST et dans les environnements de staging pour le DAST, plutôt qu'uniquement avant la mise en production. La réglementation européenne accélère cette adoption : la directive NIS2 de 2023 et le Cyber Resilience Act de 2024 imposent la sécurité by design pour tous les produits numériques vendus dans l'Union européenne.

### 4. Maintenance logicielle

La maintenance logicielle désigne l'ensemble des activités réalisées après la livraison d'un logiciel pour corriger des défauts, améliorer les performances, adapter l'environnement ou ajouter de nouvelles fonctionnalités. Elle est normalisée par la norme ISO/IEC 14764 et représente la phase la plus longue et la plus coûteuse du cycle de vie logiciel : entre 60 et 80 % du coût total d'un logiciel sur sa durée de vie.

La norme ISO 14764 définit quatre types de maintenance. La maintenance corrective, qui représente environ 20 % des budgets, corrige les défauts et bugs détectés en production. La maintenance adaptative, environ 25 %, adapte le logiciel à un nouvel environnement : nouveau système d'exploitation, nouvelle réglementation (comme le RGPD en 2018), nouveau système de gestion de base de données. La maintenance perfective, la plus consommatrice avec environ 50 % des budgets, améliore les performances ou ajoute des fonctionnalités demandées par les utilisateurs. La maintenance préventive, souvent négligée avec seulement 5 % des budgets, consiste à refactoriser le code, mettre à jour les dépendances et réduire la dette technique pour éviter des coûts bien plus élevés à terme.

Le chercheur Manny Lehman a formulé huit lois empiriques sur l'évolution des systèmes logiciels. Les deux premières sont les plus importantes pour une Direction des Systèmes d'Information. La première loi stipule qu'un logiciel doit continuellement s'adapter à son environnement ou devenir progressivement moins utile. La deuxième loi affirme que sans effort explicite pour la maîtriser, la complexité d'un système augmente à chaque évolution, justifiant ainsi la maintenance préventive.

En France, la Tierce Maintenance Applicative représente environ 30 % du marché des services informatiques. Elle consiste à externaliser la maintenance à un prestataire (Atos, Sopra Steria, CGI, Capgemini) avec des engagements contractuels de niveau de service.

### 5. Clean Code et refactoring

Le Clean Code désigne un ensemble de principes et pratiques permettant d'écrire un code lisible, maintenable et évolutif. Le refactoring consiste à restructurer le code existant sans modifier son comportement observable, afin d'améliorer sa qualité interne. Robert C. Martin, surnommé "Uncle Bob", a formalisé ces principes dans son livre Clean Code publié en 2008, ouvrage qui s'est vendu à plus de 500 000 exemplaires.

Les principes fondamentaux du Clean Code concernent le nommage : les noms doivent être révélateurs d'intention, par exemple "calculateMonthlyInterest()" plutôt que "calc()". Chaque fonction doit faire une seule chose, idéalement entre cinq et dix lignes, avec au maximum trois paramètres. Les commentaires sont considérés comme un signe d'échec à écrire du code suffisamment clair, à l'exception de la documentation des API publiques.

Les principes SOLID, formulés par Robert C. Martin, constituent le socle de la conception orientée objet de qualité. Le S désigne le Single Responsibility Principle : une classe ne doit avoir qu'une seule raison de changer. Le O désigne le principe Ouvert/Fermé : ouvert à l'extension, fermé à la modification. Le L désigne le principe de substitution de Liskov : les sous-classes doivent être substituables à leurs classes parentes. Le I désigne le principe de ségrégation des interfaces : préférer plusieurs interfaces spécifiques à une interface générale. Le D désigne le principe d'inversion de dépendances : dépendre des abstractions, pas des implémentations.

Trois autres principes issus de l'Extreme Programming complètent cet arsenal. YAGNI, You Aren't Gonna Need It, signifie qu'il ne faut pas développer ce qui n'est pas encore nécessaire. DRY, Don't Repeat Yourself, signifie que toute connaissance doit avoir une représentation unique et non ambiguë dans le système. KISS, Keep It Simple Stupid, recommande de toujours préférer la solution la plus simple.

Martin Fowler a catalogué les "code smells", ou mauvaises odeurs du code : le code dupliqué, les méthodes trop longues, les classes trop grandes, les longues listes de paramètres, et l'envie de fonctionnalité (Feature Envy), qui se produit quand une méthode utilise plus les données d'une autre classe que les siennes. La complexité cyclomatique, métrique formalisée par McCabe en 1976, mesure le nombre de chemins d'exécution indépendants dans le code. Un refactoring devient conseillé au-delà d'une complexité cyclomatique de 20, et urgent au-delà de 50.

### 6. Dette technique

La dette technique désigne l'ensemble des compromis techniques délibérés ou accidentels accumulés dans un système logiciel, qui nécessiteront un travail futur supplémentaire pour être corrigés. La métaphore a été introduite par Ward Cunningham, co-auteur du Manifeste Agile, lors d'une conférence en 1992. Comme une dette financière, elle a un principal (le travail technique à faire) et des intérêts (le surcoût quotidien qu'elle impose sur chaque développement).

Martin Fowler distingue quatre quadrants selon deux axes : la dette délibérée versus accidentelle (avait-on choisi ce compromis ?), et imprudente versus prudente (savait-on ce qu'on faisait ?). La seule forme acceptable est la dette délibérée et prudente, celle où l'on décide consciemment de livrer rapidement pour rembourser ensuite, à condition de le faire effectivement.

La dette technique mondiale est estimée à 1 500 milliards de dollars (CAST Software, 2022). Les développeurs y consacrent en moyenne 33 % de leur temps (Stripe Developer Survey, 2018). SonarQube mesure la dette technique via le modèle SQALE en jours-homme de remboursement, et calcule un Technical Debt Ratio. Un ratio supérieur à 20 % indique un code non maintenable.

Le concept de bus factor, ou facteur bus, est une notion connexe importante : il mesure le nombre minimum de personnes dont la perte mettrait le projet en péril. Un bus factor de un signifie qu'une seule personne connaît un composant critique. Les remèdes sont le pair programming, les revues de code et la rotation des responsabilités.

La stratégie de gestion la plus répandue en mode agile est la règle des 20 % : allouer à chaque sprint 20 % de la vélocité à des tickets de remboursement de dette technique. Communiquer la dette technique à la direction avec des chiffres (par exemple "3 500 jours-homme de dette, soit 7 millions d'euros d'effort de remboursement") est bien plus efficace que d'utiliser un vocabulaire purement technique.

### 7. Architecture logicielle

L'architecture logicielle désigne l'ensemble des décisions structurelles fondamentales qui définissent l'organisation d'un système : ses composants, leurs responsabilités, les relations entre eux et les principes guidant leur conception. Le coût de correction d'une décision d'architecture incorrecte est mille fois plus élevé en production qu'en phase de conception.

Le principe fondamental de l'architecture est la recherche d'un faible couplage et d'une forte cohésion. Le couplage mesure le degré de dépendance entre modules : un faible couplage permet leur évolution indépendante. La cohésion mesure le degré de responsabilité focalisée d'un module : une forte cohésion signifie que chaque module fait une seule chose et bien.

La Clean Architecture, formalisée par Robert C. Martin en 2017, résout le problème des dépendances via la règle de dépendance : les dépendances de code source ne peuvent pointer que vers l'intérieur des cercles concentriques. Au centre se trouvent les entités métier pures, sans aucune dépendance externe. A l'extérieur se trouvent les frameworks, les bases de données et les interfaces. La conséquence directe est que la logique métier est testable isolément, sans base de données, sans serveur web.

L'architecture hexagonale, aussi appelée Ports and Adapters, formalisée par Alistair Cockburn en 2005, est conceptuellement similaire à la Clean Architecture mais utilise une terminologie différente : les ports sont les interfaces définies par l'application, les adaptateurs primaires sont ceux qui appellent l'application (contrôleurs HTTP, tests), et les adaptateurs secondaires sont ceux que l'application appelle (PostgreSQL, Kafka, SMTP).

Le Domain-Driven Design, ou DDD, formalisé par Eric Evans en 2003, est une approche de conception centrée sur le modèle du domaine métier. Ses concepts clés incluent le langage ubiquitaire (langage partagé entre développeurs et experts métier), les Bounded Contexts (limites explicites dans lesquelles un modèle s'applique), les entités (objets avec identité persistante), les objets valeurs (définis par leurs attributs), les agrégats (unités transactionnelles), et les événements de domaine.

Les Architecture Decision Records, ou ADR, sont de courts documents capturant une décision architecturale importante, son contexte et ses conséquences. Versionnés avec le code dans un répertoire tel que "/docs/adr/", ils constituent la mémoire architecturale du projet. Le modèle C4 de Simon Brown, adopté par plus de 500 000 équipes, structure la documentation d'architecture en quatre niveaux : Contexte, Conteneur, Composant et Code.

### 8. Microservices versus monolithe

Un monolithe est une application dans laquelle tous les composants fonctionnels sont déployés comme une seule unité. Une architecture microservices décompose l'application en services indépendants, chacun responsable d'une capacité métier, déployables et scalables indépendamment.

Le monolithe présente des avantages concrets pour les petites équipes : simplicité de développement local, débogage facilité, transactions ACID simples, faible latence grâce aux appels en mémoire, et coût opérationnel réduit. Le monolithe modulaire, recommandé par Martin Fowler comme première étape, organise le code en modules distincts mais le déploie comme une seule unité. Des entreprises comme Shopify et Stack Overflow ont choisi de rester sur ce modèle plutôt que de migrer vers des microservices.

Les microservices présentent des avantages différents : scaling indépendant de chaque service, déploiement indépendant permettant une haute fréquence de livraison, polyglottisme technologique, et résilience (une défaillance isolée n'impacte pas tout le système). Netflix déploie plus de 1 000 fois par jour grâce à ses 700 microservices. Mais le coût opérationnel est en moyenne 3 à 5 fois plus élevé qu'un monolithe équivalent pour de petites équipes.

Les patterns fondamentaux des microservices incluent le Database per Service (chaque service possède sa propre base de données, inaccessible directement par les autres), l'API Gateway (point d'entrée unique qui gère le routage, l'authentification et le rate limiting), le Circuit Breaker (qui interrompt les appels vers un service défaillant pour éviter les pannes en cascade), et le Saga Pattern (qui gère les transactions distribuées via une séquence d'événements compensatoires, puisque les transactions ACID classiques sont impossibles entre services indépendants).

La loi de Conway, formulée par Melvin Conway en 1968, est incontournable : "Les organisations qui conçoivent des systèmes produisent des systèmes qui copient leurs structures de communication." En pratique, une migration vers les microservices implique nécessairement une réorganisation en équipes autonomes (squads), chaque équipe possédant un ou plusieurs services de bout en bout.

Le Strangler Fig Pattern de Martin Fowler est le pattern de migration recommandé : un proxy redirige progressivement le trafic du monolithe vers de nouveaux microservices, évitant une migration "big bang" risquée.

### 9. TDD et BDD — développement guidé par les tests et par le comportement

Le TDD, Test-Driven Development ou développement guidé par les tests, est une pratique dans laquelle on écrit un test automatisé avant le code de production. Le cycle Red-Green-Refactor, formalisé par Kent Beck en 2003, se déroule en trois phases très courtes. La phase Rouge consiste à écrire un test qui échoue car le code n'existe pas encore. La phase Verte consiste à écrire le minimum de code de production pour faire passer le test. La phase Refactor consiste à améliorer la qualité du code sans modifier son comportement, les tests garantissant la non-régression.

Le BDD, Behavior-Driven Development ou développement guidé par le comportement, formalisé par Dan North en 2006, étend le TDD en exprimant les comportements attendus dans un langage naturel partagé avec les parties prenantes non techniques. Il utilise le format Gherkin avec les mots-clés Given (contexte initial), When (action déclenchante), et Then (résultat attendu). Ces scénarios sont lisibles par les product owners, les analystes métier et les juristes, et exécutables par les frameworks comme Cucumber.

Les études de terrain de Microsoft et IBM (2008) ont démontré que le TDD réduit les bugs en production de 40 à 80 %, avec un surcoût de développement initial de 15 à 35 % qui est largement compensé par une réduction du coût de maintenance de 40 à 90 % à long terme.

La pyramide des tests de Mike Cohn recommande une répartition en trois niveaux : beaucoup de tests unitaires en base (rapides, isolés, nombreux), moins de tests d'intégration au milieu, et peu de tests end-to-end au sommet (lents, fragiles, coûteux). En microservices, les tests de contrat (Consumer-Driven Contract avec l'outil Pact) vérifient que deux services communiquent conformément à un contrat défini.

Le pair programming, pratique d'Extreme Programming où deux développeurs travaillent ensemble sur le même ordinateur, est complémentaire du TDD. Le Driver écrit le code tactiquement, le Navigator observe et réfléchit stratégiquement. Les études montrent une réduction des bugs de 15 % avec un ROI généralement positif sur les tâches complexes.

### 10. DevOps

Le DevOps est un mouvement culturel et organisationnel né en 2008 et formalisé par Patrick Debois lors de la première DevOpsDays à Gand en 2009. Il vise à abattre le cloisonnement entre les équipes de développement (Dev) et d'exploitation (Ops) pour livrer des logiciels plus rapidement, de façon plus fiable et plus sûre.

Gene Kim a théorisé les trois voies du DevOps. La première voie, le Flow, consiste à accélérer le flux de valeur de la gauche (développement) vers la droite (production) via l'automatisation et les petits lots. La deuxième voie, le Feedback, consiste à créer des boucles de retour d'information rapides de la production vers le développement via le monitoring et les alertes. La troisième voie, l'Apprentissage, correspond à une culture d'amélioration continue et d'expérimentation via les post-mortems sans accusation et le Chaos Engineering.

Le modèle CALMS est le framework d'évaluation de la maturité DevOps : Culture (collaboration et responsabilité partagée), Automation (automatiser tout ce qui est répétable), Lean (réduire les gaspillages), Measurement (mesurer pour décider) et Sharing (partager outils et pratiques).

Les résultats obtenus par les organisations les plus matures sont spectaculaires : d'après le rapport DORA de 2023, les équipes Elite DevOps déploient 973 fois plus fréquemment et restaurent le service 6 570 fois plus vite que les organisations à faible performance. Le risque du "DevOps washing" est réel : adopter les outils (Jenkins, GitLab) sans transformation culturelle, en maintenant les silos Dev et Ops.

### 11. Intégration continue et déploiement continu

La CI/CD, Continuous Integration (Intégration Continue) et Continuous Delivery ou Deployment (Livraison ou Déploiement Continu), est un ensemble de pratiques d'automatisation du cycle de livraison logicielle. L'Intégration Continue consiste à intégrer le code de tous les développeurs dans le tronc principal plusieurs fois par jour ; à chaque push, un pipeline automatique déclenche la compilation, les tests unitaires, l'analyse statique, les tests d'intégration et la construction de l'artefact.

Il existe une distinction importante entre la Livraison Continue et le Déploiement Continu. La Livraison Continue maintient l'artefact toujours prêt à déployer mais requiert une validation humaine avant la mise en production ; c'est le modèle adopté dans les secteurs réglementés comme la banque et l'aéronautique. Le Déploiement Continu pousse automatiquement en production à chaque commit validé par les tests ; c'est le modèle de Netflix, Facebook et Etsy.

Le problème que résout l'Intégration Continue est ce qu'on appelle "l'integration hell" : lorsque les développeurs intègrent rarement leur code, les fusions deviennent extrêmement difficiles et génèrent de nombreux conflits. Le Trunk-Based Development, où tous les développeurs travaillent sur le tronc principal ou via des branches éphémères de moins de 24 heures, est la pratique recommandée pour éviter ce problème.

Les feature flags, ou bascules de fonctionnalités, permettent d'activer ou désactiver une fonctionnalité en production sans déploiement. Ils sont utilisés pour les tests A/B, les déploiements progressifs et les rollbacks instantanés sans redéploiement. Les outils spécialisés incluent LaunchDarkly, Unleash et Flagsmith.

### 12. DevSecOps

Le DevSecOps est l'extension du DevOps intégrant la sécurité comme responsabilité partagée et continue tout au long du cycle de développement logiciel. Le principe central est le "shift-left security" : déplacer les contrôles de sécurité le plus tôt possible dans le pipeline, dès le code voire la conception, plutôt que de les appliquer uniquement à la fin. La sécurité devient du code, "Security as Code" : automatisée, versionnée, testable.

Le pipeline DevSecOps type enchaîne plusieurs types d'analyses : le SAST et la détection de secrets à la soumission du code, le SCA (analyse des dépendances open source) lors de la construction, le scan des images de conteneurs, le scan de l'Infrastructure as Code, le DAST en environnement de staging, et la vérification de conformité avant le déploiement en production.

La modélisation des menaces (threat modeling) dès la phase de conception, l'Open Policy Agent (OPA) pour définir les politiques de sécurité sous forme de code, et le Software Bill of Materials (SBOM), inventaire exhaustif des composants d'une application, sont des concepts qui gagnent en importance. Le SBOM est rendu obligatoire pour les logiciels vendus au gouvernement américain depuis 2021 et tend à se généraliser en Europe.

Le principal défi organisationnel du DevSecOps est la résistance culturelle : la sécurité est perçue comme un frein par les développeurs, et les faux positifs générés par les outils d'analyse peuvent être nombreux. La clé est le modèle "you build it, you secure it" : les développeurs sont responsables de la sécurité de leurs services, accompagnés par une équipe de sécurité en rôle de conseil et de plateforme, et non de gendarme en bout de chaîne.

### 13. GitOps

Le GitOps est un paradigme opérationnel formalisé par Alexis Richardson de Weaveworks en 2017, qui utilise Git comme source unique de vérité pour l'infrastructure et les applications. Toute modification de l'infrastructure ou des déploiements passe par un commit dans Git. Un opérateur comme ArgoCD ou Flux surveille en permanence le dépôt Git et réconcilie automatiquement l'état réel du cluster Kubernetes avec l'état déclaré dans Git.

Les quatre principes du GitOps selon OpenGitOps version 1.0 (standard de la Cloud Native Computing Foundation, ou CNCF) sont les suivants. Premièrement, l'état souhaité du système est exprimé de façon déclarative. Deuxièmement, cet état est versionné et immuable dans Git. Troisièmement, les agents récupèrent (pull) automatiquement l'état souhaité depuis Git. Quatrièmement, des agents assurent en permanence que l'état réel correspond à l'état déclaré.

La différence entre le modèle Push et le modèle Pull est importante. Dans le modèle Push traditionnel, le pipeline CI envoie les changements vers le cluster. Dans le modèle Pull du GitOps, un agent interne au cluster récupère les changements depuis Git, ce qui est plus sécurisé car le cluster n'expose pas son API aux systèmes externes.

Le concept de "drift", ou dérive de configuration, désigne la divergence entre l'état déclaré dans Git et l'état réel du cluster, causée par des modifications manuelles en dehors du processus GitOps. ArgoCD détecte ce drift en temps réel et peut le corriger automatiquement. La gestion des secrets en GitOps est un défi : ils ne doivent jamais être stockés en clair dans Git, d'où l'utilisation de solutions comme Sealed Secrets, External Secrets Operator ou SOPS.

### 14. Infrastructure as Code

L'Infrastructure as Code, ou IaC, est la pratique consistant à gérer et provisionner l'infrastructure informatique via des fichiers de configuration déclaratifs ou des scripts versionnés dans Git, plutôt que via des interfaces manuelles. L'infrastructure devient du code : versionnable, testable, partageable et reproductible. Terraform de HashiCorp, lancé en 2014, en est l'outil de référence multi-cloud, utilisé par plus de 2 millions de développeurs dans le monde.

L'idempotence est la propriété fondamentale de l'IaC : exécuter le même code plusieurs fois produit toujours le même résultat. Si la ressource est déjà conforme à ce qui est déclaré, elle n'est pas modifiée. Cela rend les déploiements sûrs et réexécutables.

Terraform utilise le langage HCL (HashiCorp Configuration Language) et fonctionne en trois étapes : "terraform plan" affiche les changements prévus, "terraform apply" les applique, et un fichier d'état (terraform.tfstate) trace la correspondance entre le code et les ressources réelles. Ce fichier d'état doit impérativement être stocké en remote (sur S3 par exemple) avec verrouillage pour éviter les conflits entre membres d'équipe.

Ansible, de Red Hat, est complémentaire de Terraform : là où Terraform est orienté provisionnement d'infrastructure (créer des machines virtuelles, des réseaux, des bases de données), Ansible est orienté gestion de configuration (installer des paquets, déployer des applications sur des serveurs existants). En 2023, HashiCorp a changé la licence de Terraform d'une licence open source vers la Business Source License, conduisant à la création d'OpenTofu par la Linux Foundation comme fork libre.

Le Policy as Code s'impose comme complément de l'IaC : des règles de conformité et de sécurité définies sous forme de code (via Open Policy Agent ou HashiCorp Sentinel) sont vérifiées automatiquement avant chaque "terraform apply", empêchant le déploiement de configurations non conformes.

### 15. Observabilité

L'observabilité est la capacité à comprendre l'état interne d'un système à partir de ses sorties externes. Elle repose sur trois piliers : les logs (enregistrements textuels des événements horodatés), les métriques (données numériques agrégées dans le temps, appelées time series), et les traces distribuées (suivi du chemin d'une requête à travers les services d'un système distribué).

La distinction entre monitoring et observabilité est fondamentale. Le monitoring surveille des métriques prédéfinies (seuils statiques, alertes) : on sait ce qu'on cherche. L'observabilité permet d'explorer et de questionner le comportement d'un système pour découvrir des problèmes inconnus : on peut poser des questions non anticipées. Dans une architecture microservices, un incident peut impliquer des dizaines de services, et le monitoring traditionnel ne suffit plus pour diagnostiquer "pourquoi le service X est lent".

OpenTelemetry, né en 2019 de la fusion des projets OpenCensus et OpenTracing sous l'égide de la CNCF, est devenu le standard universel pour instrumenter les applications. Il fournit des SDK pour tous les langages principaux, un collecteur qui reçoit les données et les exporte vers n'importe quel backend, et le protocole OTLP. Son avantage central est la neutralité vis-à-vis des fournisseurs : on change de backend d'observabilité sans modifier le code applicatif.

L'architecture d'observabilité la plus répandue en open source combine Prometheus pour les métriques (avec son langage de requête PromQL), Grafana Loki pour les logs, et Jaeger ou Grafana Tempo pour les traces, le tout visualisé dans Grafana. Le tracing distribué fonctionne via un identifiant de trace unique (trace ID) qui relie des unités de travail appelées "spans" à travers tous les services traversés par une requête.

### 16. Stratégies de déploiement

Les stratégies de déploiement sont des patterns permettant de livrer de nouvelles versions d'une application en production tout en minimisant les risques d'interruption de service et d'impact utilisateur. Quarante-cinq pour cent des incidents de production sont causés par des déploiements.

Le déploiement "Big Bang" ou Recreate arrête complètement l'ancienne version avant de déployer la nouvelle. Il génère une indisponibilité et est réservé aux environnements non critiques.

Le Rolling Update remplace les instances une à une sans interruption de service, mais implique une coexistence temporaire des deux versions. Les APIs et les schémas de base de données doivent être rétrocompatibles pendant cette transition.

Le Blue-Green Deployment maintient deux environnements identiques en parallèle : le Blue (actif) et le Green (nouveau). Le trafic est basculé instantanément via un load balancer une fois la nouvelle version validée. Le Blue reste disponible pour un rollback immédiat, mais le coût de double infrastructure est la principale limite.

Le Canary Release déploie progressivement sur un faible pourcentage d'utilisateurs (5 à 10 %), augmenté progressivement si les métriques sont bonnes. Inspiré des canaris utilisés dans les mines de charbon comme alerte précoce, ce pattern réduit le "blast radius" (rayon d'impact) en cas de problème.

Le Progressive Delivery, concept formalisé par Jez Humble, combine déploiement progressif (canary), feature flags et observabilité pour contrôler finement le rollout des fonctionnalités, en maintenant une haute fréquence de livraison tout en réduisant le risque.

### 17. SRE — Site Reliability Engineering

Le Site Reliability Engineering, ou ingénierie de la fiabilité des sites, est une discipline née chez Google en 2003, formalisée par Ben Treynor Sloss et documentée dans le livre SRE d'O'Reilly (2016). Le SRE applique les principes du génie logiciel aux problèmes opérationnels, en traitant l'exploitation de systèmes à grande échelle comme un problème d'ingénierie.

La hiérarchie des indicateurs de fiabilité est fondamentale. Le SLI, Service Level Indicator ou indicateur de niveau de service, est la métrique mesurée, par exemple le taux de requêtes HTTP réussies. Le SLO, Service Level Objective ou objectif de niveau de service, est l'objectif interne défini pour ce SLI sur une période, par exemple 99,9 % de requêtes réussies sur 30 jours glissants. Le SLA, Service Level Agreement ou accord de niveau de service, est l'engagement contractuel avec pénalités financières envers le client. Un SLO est toujours plus strict que le SLA correspondant pour laisser une marge de sécurité.

L'error budget, ou budget d'erreur, est le concept central du SRE. C'est le complément du SLO : si le SLO est de 99,9 %, l'error budget est de 0,1 %, soit 43,2 minutes par mois. Ce mécanisme est puissant car il rend la décision de déployer ou non objective et dépolitisée : si l'error budget est intact, les équipes de développement peuvent déployer librement ; si l'error budget est épuisé, tous se concentrent sur la fiabilité jusqu'au prochain cycle.

Le "toil" est le travail opérationnel manuel, répétitif, sans valeur ajoutée à long terme et qui scale linéairement avec la taille du service (relancer manuellement un pod, répondre manuellement à des alertes). Les SRE doivent maintenir leur toil sous 50 % de leur temps et l'éliminer via l'automatisation.

Le blameless post-mortem, ou bilan post-incident sans accusation, est la pratique qui consiste à analyser un incident sans rechercher de responsabilité individuelle, mais en se concentrant sur les causes systémiques. Une culture de la "faute individuelle" pousse les équipes à cacher les incidents et à éviter les risques ; le blameless post-mortem génère au contraire des améliorations durables.

### 18. Métriques DORA

Les métriques DORA (DevOps Research and Assessment) sont quatre indicateurs clés issus d'un programme de recherche mené par Google depuis 2014, permettant de mesurer la performance des équipes de livraison logicielle. Elles distinguent les équipes Elite, High, Medium et Low en termes de performance DevOps.

La première métrique est la Deployment Frequency (fréquence de déploiement). Une équipe Elite déploie plusieurs fois par jour, une équipe Low moins d'une fois par mois. La deuxième métrique est le Lead Time for Changes (délai de mise en production) : temps entre le premier commit et la mise en production. Elite : moins d'une heure. Low : plus de six mois. La troisième métrique est le Change Failure Rate (taux d'échec des changements), qui mesure le pourcentage de déploiements entraînant un incident nécessitant un rollback ou un hotfix. Elite : 0 à 15 %. Low : 46 à 60 %. La quatrième métrique est le Mean Time to Restore, ou MTTR (temps moyen de rétablissement après incident). Elite : moins d'une heure. Low : entre une semaine et un mois.

En 2023, DORA a introduit une cinquième métrique, la Reliability, mesurée par le respect des SLO. Les équipes Elite ont 2,5 fois plus de probabilité de surpasser leurs objectifs commerciaux. La loi de Goodhart est un risque connu : "Quand une mesure devient un objectif, elle cesse d'être une bonne mesure." Il faut surveiller ces métriques sans qu'elles deviennent des fins en elles-mêmes.

### 19. Chaos Engineering

Le Chaos Engineering est la pratique consistant à introduire délibérément des défaillances contrôlées dans un système distribué, afin de vérifier sa résilience, d'identifier ses points de fragilité et de renforcer la confiance dans sa capacité à supporter des conditions adverses réelles. Netflix a popularisé cette approche avec Chaos Monkey en 2011, outil qui tue aléatoirement des instances en production pour forcer la conception de systèmes résilients.

La méthode scientifique du Chaos Engineering repose sur quatre étapes. Premièrement, formuler une hypothèse sur le comportement en régime stable (steady state). Deuxièmement, varier les événements du monde réel (latence réseau, crash de pod, saturation CPU). Troisièmement, exécuter l'expérience en production ou dans un environnement miroir fidèle. Quatrièmement, réfuter l'hypothèse pour révéler les faiblesses.

Les Game Days sont des sessions planifiées où une équipe exécute des scénarios de chaos face à un groupe de réponse à incident. Ils permettent de tester simultanément les systèmes et les processus humains : runbooks, communication de crise, escalades.

La condition préalable indispensable au Chaos Engineering en production est une observabilité mature : monitoring, alerting et tracing doivent permettre de détecter immédiatement les impacts et d'arrêter l'expérience si nécessaire. 43 % des organisations pratiquant le Chaos Engineering déclarent avoir détecté des failles critiques avant un incident réel.

### 20. Platform Engineering

Le Platform Engineering est la discipline consistant à concevoir et opérer une plateforme interne, appelée Internal Developer Platform ou IDP, qui met à disposition des développeurs un ensemble de capacités en libre-service (infrastructure, CI/CD, observabilité, sécurité) via une interface unifiée. L'objectif est de réduire la charge cognitive des développeurs et d'accélérer la livraison de valeur.

La distinction entre IDP et Internal Developer Portal est importante. La plateforme (IDP) est l'ensemble des capacités techniques exposées via des APIs. Le portail est l'interface utilisateur, souvent basée sur Backstage (créé par Spotify en 2020, devenu projet CNCF en 2022), qui les expose aux développeurs en un seul endroit.

Les composants typiques d'une plateforme incluent les Golden Paths (templates pré-approuvés pour créer un nouveau service avec son repo Git, son pipeline CI/CD, son namespace Kubernetes, son monitoring et son alerting en un seul clic), le self-service infrastructure (provisionner une base de données sans ticket à l'équipe infrastructure), et les scorecards de maturité (tableaux de bord évaluant chaque service sur des critères de qualité, de sécurité et de conformité).

Le concept de "Platform as a Product" est fondamental : l'équipe Platform Engineering traite sa plateforme comme un produit avec des utilisateurs (les développeurs), du feedback, des priorités et un Net Promoter Score interne. Selon Gartner, 80 % des grandes organisations auront des équipes de Platform Engineering dédiées d'ici 2026.

### 21. Tests logiciels

Les tests logiciels désignent l'ensemble des activités visant à évaluer la qualité d'un système en vérifiant qu'il se comporte conformément aux exigences. Un bug en production coûte en moyenne 30 fois plus cher à corriger qu'en phase de développement, et les bugs logiciels coûtent environ 2 400 milliards de dollars par an à l'économie mondiale.

La pyramide des tests de Mike Cohn guide la répartition : beaucoup de tests unitaires en base (rapides, isolés, nombreux), moins de tests d'intégration au milieu, peu de tests end-to-end au sommet (lents, fragiles, coûteux). Les tests unitaires ciblent une unité isolée de code avec des dépendances mockées. Les tests d'intégration vérifient les interactions entre composants. Les tests end-to-end simulent le parcours complet d'un utilisateur.

Deux types de tests avancés méritent une attention particulière. Le mutation testing injecte des mutations délibérées dans le code source (par exemple remplacer "supérieur à" par "supérieur ou égal à") et vérifie que les tests existants les détectent. C'est une mesure de la qualité réelle des tests, car une couverture de code à 100 % peut très bien passer à côté de bugs si les assertions ne sont pas pertinentes. Le fuzzing génère des entrées aléatoires ou semi-aléatoires pour découvrir des comportements inattendus et des vulnérabilités ; il est utilisé par Google (OSS-Fuzz) pour tester plus de 650 projets open source critiques en continu.

Les normes de référence sont l'ISTQB (International Software Testing Qualifications Board), certification internationale avec 1,2 million de certifiés dans le monde, et l'ISO/IEC 29119 sur les processus, la documentation et les techniques de test.

### 22. IA et automatisation des tests

L'IA appliquée aux tests logiciels regroupe les techniques permettant d'automatiser, améliorer et accélérer les activités de test. La maintenance des tests automatisés est le principal frein à leur adoption : 70 % des équipes QA citent ce défi comme prioritaire.

L'auto-healing (auto-guérison) des tests résout le problème des tests end-to-end qui se cassent à chaque modification d'interface car les sélecteurs CSS ou XPath ne correspondent plus à l'élément cible. L'outil apprend plusieurs façons d'identifier un élément et met à jour automatiquement le test lorsqu'un sélecteur échoue. Les outils leaders sont Testim, Mabl et Healenium (open source pour Selenium). Ces outils réduisent le temps de maintenance des tests de 40 à 60 %.

La Predictive Test Selection (sélection prédictive des tests) utilise des modèles d'apprentissage automatique qui analysent l'historique d'exécution pour prédire les tests les plus susceptibles d'échouer pour un changement de code donné. Seuls ces tests sont exécutés en CI/CD, réduisant la durée des pipelines de 40 à 80 %. Meta utilise cette approche en interne avec 80 % de réduction du nombre de tests exécutés par commit.

Les LLM (Large Language Models, ou grands modèles de langage) permettent de générer des cas de test depuis des user stories en langage naturel, de suggérer des cas limites (edge cases) oubliés, et d'expliquer les échecs de tests en langage compréhensible. Diffblue Cover génère automatiquement des tests unitaires Java. GitHub Copilot suggère des tests unitaires directement dans l'IDE. Le risque principal de l'auto-healing est de masquer des régressions réelles en adaptant le test à un comportement modifié qui aurait dû être signalé comme un bug.

### 23. Réalité étendue (XR)

La réalité étendue, Extended Reality en anglais, est un terme générique désignant l'ensemble des technologies qui altèrent ou enrichissent la perception de la réalité. Elle englobe la réalité augmentée (RA), la réalité virtuelle (RV) et la réalité mixte (RM), positionnées sur le continuum de Milgram entre le monde réel pur et l'environnement virtuel total.

En réalité augmentée, des éléments numériques 2D ou 3D sont superposés sur le monde réel via une caméra, le monde réel restant prépondérant (Pokémon GO, IKEA Place, Google Maps navigation). En réalité mixte, les objets numériques interagissent avec le monde réel en temps réel : un objet 3D peut se cacher derrière une table réelle grâce à l'occlusion, comme sur le HoloLens 2 de Microsoft. En réalité virtuelle, l'immersion est totale dans un environnement 100 % numérique via un casque opaque (Meta Quest 3, PlayStation VR2, Apple Vision Pro).

Le SLAM (Simultaneous Localization and Mapping) est l'algorithme fondamental du XR : le dispositif cartographie son environnement en temps réel tout en se localisant dedans, sans GPS. Le Spatial Computing, popularisé par Apple avec le Vision Pro en 2024, désigne le paradigme dans lequel l'interface utilisateur s'étend dans l'espace tridimensionnel en combinant vision, audio spatial, et suivi des mains et des yeux.

Le marché mondial du XR atteindra 1 700 milliards de dollars en 2030. 75 % des entreprises du Fortune 500 utilisent déjà une forme de XR pour la formation ou la maintenance. Unity est le moteur de développement XR dominant, utilisé dans 70 % des expériences XR développées.

### 24. Jumeau numérique (Digital Twin)

Un jumeau numérique est une réplique virtuelle dynamique d'un objet physique, d'un processus, d'un système ou d'une organisation, alimentée en temps réel par des données issues de capteurs IoT, de systèmes d'information ou de simulations. Il repose sur trois composants : l'entité physique, le jumeau numérique (le modèle virtuel) et le lien de données bidirectionnel entre les deux.

Quatre types de jumeaux numériques sont distingués. Le jumeau du produit réplique un produit tout au long de son cycle de vie, comme les moteurs d'avion de Rolls-Royce équipés chacun de 100 capteurs. Le jumeau du processus réplique un processus de production pour l'optimiser en temps réel. Le jumeau du système réplique un système complexe, comme le Singapore National Digital Twin qui couvre l'intégralité de la ville de Singapour pour la planification urbaine et la gestion des crises. Le jumeau d'infrastructure IT réplique l'infrastructure informatique (réseau, datacenter, cloud) pour simuler des pannes avant de les provoquer réellement.

Le BIM (Building Information Modeling), normalisé par l'ISO 19650, est la norme de modélisation numérique du bâtiment. Un modèle BIM enrichi de données IoT en temps réel constitue un jumeau numérique du bâtiment. En France, le BIM est obligatoire pour les projets publics de plus d'un million d'euros.

NVIDIA Omniverse est la plateforme de simulation 3D collaborative basée sur Universal Scene Description (USD) de Pixar, fondation du Metaverse industriel : BMW simule ses usines de production en entier sur cette plateforme avant tout changement physique. La maintenance prédictive via jumeau numérique réduit les coûts de maintenance de 10 à 25 % et les pannes de 70 %.

### 25. Industrie 4.0 et XR

L'Industrie 4.0 désigne la quatrième révolution industrielle, caractérisée par la convergence des technologies numériques (IoT, IA, big data, robotique, cloud, XR) avec les systèmes de production physiques. Le terme a été forgé par le gouvernement allemand en 2011. Elle succède à l'Industrie 1.0 (vapeur), l'Industrie 2.0 (électricité et production de masse) et l'Industrie 3.0 (automatisation et informatique).

La réalité étendue joue trois rôles distincts dans l'Industrie 4.0. La formation immersive en réalité virtuelle permet de former les opérateurs sur des scénarios inaccessibles en conditions réelles : intervention sur équipements haute tension, procédures d'urgence, montage de machines complexes. La rétention est 75 % supérieure aux formations classiques (PwC, 2022). La maintenance augmentée en réalité augmentée équipe les techniciens de lunettes AR (HoloLens 2, RealWear Navigator) qui voient des instructions étape par étape superposées sur l'équipement réel, des vues explosées des composants, et des alertes en temps réel depuis les capteurs IoT. La conception et simulation en XR permet aux ingénieurs de visualiser un équipement en taille réelle dans l'espace physique avant sa fabrication.

Boeing a réduit ses temps de câblage des ailes d'avion de 25 % et ses erreurs de 50 % grâce aux instructions holographiques superposées sur les harnais réels avec HoloLens. Renault déploie des formations VR sur Meta Quest pour former les mécaniciens à l'entretien de ses véhicules électriques dans ses centres mondiaux, en remplacement des véhicules démonstrateurs physiques coûteux. SNCF utilise la VR pour les formations de maintenance des voies ferrées et les procédures d'urgence en tunnel, avec traçabilité des compétences dans le LMS corporate.

---

## Questions jury

Les six sujets du jury pour ce thème appellent des réponses structurées.

Le sujet 28 demande si la norme ISO/CEI 9126 est nécessaire et suffisante pour garantir la qualité logicielle. La réponse doit rappeler que l'ISO 9126 a été remplacée en 2011 par l'ISO 25010 (famille SQuaRE), plus complète avec 8 caractéristiques dont la sécurité et la compatibilité, révisée en 2023 pour intégrer la sûreté fonctionnelle. Mais aucune norme n'est suffisante à elle seule : elle doit être complétée par des pratiques (TDD, Clean Code, revues de code) et des outils (SonarQube, SAST/DAST). ISO 25010 offre un référentiel contractualisable mais le risque de conformité de façade est réel.

Le sujet 29 porte sur la valeur ajoutée et le retour sur investissement de l'intégration continue. Les éléments quantifiés sont forts : les équipes pratiquant la CI/CD déploient 208 fois plus fréquemment (DORA), les équipes Elite ont un lead time inférieur à une heure contre plus de six mois pour les équipes Low. Le ROI est direct (bugs détectés en CI coûtent 6 fois moins qu'en test, 100 fois moins qu'en production) et indirect (réduction du burn-out, meilleure attractivité des talents, 5 fois moins de burn-out selon DORA 2023).

Le sujet 30 concerne l'apprentissage automatique et l'automatisation des tests. Les axes clés sont l'auto-healing (réduction de 40 à 60 % du temps de maintenance), la Predictive Test Selection (réduction de 40 à 80 % de la durée des pipelines), les tests visuels par IA (réduction de 90 % des faux positifs), et la génération de tests par LLM. Le risque principal à mentionner est que l'auto-healing peut masquer des régressions réelles.

Le sujet 31 porte sur la stratégie de maintenabilité logicielle et les coûts associés. La structure de réponse doit s'appuyer sur les 4 types de maintenance ISO 14764 (corrective 20 %, adaptative 25 %, perfective 50 %, préventive 5 %), les lois de Lehman (changement continu, complexité croissante), la notion de dette technique quantifiée en jours-homme par SonarQube, et les stratégies concrètes (règle des 20 %, TMA externalisée). Le chiffre clé : 60 à 80 % du coût total d'un logiciel est consacré à sa maintenance.

Le sujet 32 demande comment le DevOps peut améliorer la qualité du SI et la productivité. La réponse s'articule autour des 3 voies (Flow, Feedback, Learning), du modèle CALMS, et des métriques DORA. Les bénéfices concrets incluent la réduction du lead time, la réduction du Change Failure Rate grâce aux tests automatisés, et la réduction du MTTR grâce à l'observabilité. L'exemple d'ING Bank (passage de 1 déploiement par an à plusieurs par semaine, réduction des incidents de 50 %) illustre bien la transformation.

Le sujet 33 porte sur les enjeux et le positionnement de la RA/RV pour l'entreprise 4.0. La réponse doit couvrir les trois usages (formation immersive, maintenance augmentée, conception collaborative), les indicateurs de performance (Boeing : -25 % temps câblage, -50 % erreurs), les dispositifs (HoloLens 2 vs Meta Quest 3 vs Apple Vision Pro) et les enjeux d'adoption (coût de création de contenu, ergonomie, cybersécurité OT). Le lien avec le Digital Twin est un enrichissement : le XR est l'interface d'interaction avec le jumeau numérique.

Au-delà des sujets officiels, les questions types du jury touchent également aux thèmes suivants : ISO 9126 versus ISO 25010 et pourquoi la norme a évolué ; comment mesurer et gérer la dette technique dans un projet ; comment justifier le ROI de l'intégration continue auprès du CODIR ; TDD versus BDD, quelles pratiques pour garantir la qualité ; microservices versus monolithe, comment choisir la bonne architecture ; qu'est-ce que le DevSecOps et pourquoi intégrer la sécurité dès le développement ; les 4 métriques DORA et comment les utiliser ; comment le Platform Engineering améliore l'expérience développeur.

---

## Points de vigilance

Plusieurs confusions courantes sont à éviter absolument lors du grand oral.

Concernant la qualité logicielle, ne pas confondre ISO 9126 (norme remplacée, 6 caractéristiques) et ISO 25010 (norme actuelle, 8 caractéristiques, famille SQuaRE). Savoir que la révision 2023 d'ISO 25010 ajoute la Sûreté (Safety). Ne pas réduire la qualité à la seule correction fonctionnelle : la maintenabilité, la sécurité et la performance sont des caractéristiques de qualité à part entière.

Concernant la dette technique, ne pas la présenter comme uniquement négative : la dette délibérée et prudente est un levier tactique légitime si elle est remboursée rapidement. Savoir la quantifier : SonarQube l'exprime en jours-homme via le modèle SQALE, un Technical Debt Ratio supérieur à 20 % signifie un code non maintenable.

Concernant le DevOps, ne pas le réduire à des outils (Jenkins, GitLab). C'est avant tout une transformation culturelle. Le "DevOps washing" est le risque d'adopter les outils sans transformer l'organisation. Savoir distinguer DevOps (mouvement culturel) et SRE (implémentation concrète du DevOps par Google, avec des mécanismes précis comme les SLO et l'error budget).

Concernant la CI/CD, savoir distinguer Continuous Delivery (artefact prêt, validation humaine avant prod) et Continuous Deployment (automatique jusqu'en prod). Le premier convient aux secteurs réglementés, le second au SaaS. Ne pas confondre non plus les feature flags (mécanisme applicatif) et les stratégies de déploiement (mécanisme infrastructure).

Concernant les microservices, ne pas présenter le monolithe comme systématiquement obsolète : le monolithe modulaire est recommandé par Martin Fowler pour les équipes de moins de 50 développeurs. Le monolithe distribué est un anti-pattern (services qui semblent séparés mais sont fortement couplés). Connaître la loi de Conway est indispensable : l'architecture reflète l'organisation.

Concernant le SRE, savoir que le SLO est toujours plus strict que le SLA (marge de sécurité). Un SLO de 99,99 % correspond à seulement 4,32 minutes d'indisponibilité par mois. Ne pas confondre le MTTR (temps de rétablissement, métrique DORA) avec le MTBF (Mean Time Between Failures, temps moyen entre pannes, autre indicateur de fiabilité).

Concernant le XR, ne pas confondre réalité augmentée (éléments numériques superposés, monde réel prépondérant) et réalité mixte (objets numériques qui interagissent avec le monde réel, occlusion). Apple Vision Pro n'est pas un casque VR mais un casque de "spatial computing". Le HoloLens 2 est de la réalité mixte, pas de la réalité virtuelle.

Concernant les chiffres clés à retenir impérativement : les défauts non détectés en conception coûtent 100 fois plus cher en production (NIST) ; la maintenance représente 60 à 80 % du coût total d'un logiciel ; la dette technique mondiale est estimée à 1 500 milliards de dollars ; les équipes Elite DORA déploient 973 fois plus fréquemment ; le TDD réduit les bugs de 40 à 80 % ; Boeing a réduit son temps de câblage de 25 % grâce à la RA ; la formation en VR améliore la rétention de 75 % par rapport aux méthodes classiques.

Enfin, un point transversal à souligner : ces notions ne sont pas indépendantes. Un jury appréciera de voir les enchaînements : le Clean Code rend le TDD possible, le TDD rend la CI fiable, la CI rend le déploiement fréquent sûr, la fréquence de déploiement est mesurée par les métriques DORA, et les métriques DORA pilotent l'amélioration continue de l'organisation. Le Platform Engineering est la réponse organisationnelle à la complexité croissante de ces chaînes.
