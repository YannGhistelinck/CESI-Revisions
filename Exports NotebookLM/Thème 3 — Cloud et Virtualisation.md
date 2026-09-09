# Cloud et Virtualisation — Guide de révision complet

## Introduction

Le thème "Cloud et Virtualisation" est au cœur de la transformation des systèmes d'information modernes. En moins de vingt ans, le cloud computing est passé d'une curiosité technique à une infrastructure mondiale incontournable. En 2024, le marché mondial du cloud dépasse six cent quatre-vingts milliards de dollars, et plus de quatre-vingt-sept pour cent des entreprises ont adopté une stratégie multi-cloud. Pour un directeur des systèmes d'information ou un architecte, maîtriser ce thème est désormais une compétence fondamentale.

Ce thème couvre un spectre très large : les modèles de service et de déploiement cloud, les questions de souveraineté et de droit applicable aux données, les enjeux de sécurité spécifiques aux environnements cloud, les stratégies de migration, les technologies de virtualisation et de conteneurisation, les architectures cloud native, et enfin le cadre réglementaire européen qui redessine les règles du marché. Chaque dimension est à la fois technique et stratégique : un mauvais choix architectural se traduit par des surcoûts, des risques de sécurité ou une dépendance fournisseur difficile à défaire.

Ce document synthétise l'ensemble des notions clés de ce thème pour vous préparer à en parler avec précision, avec des chiffres et avec la hauteur de vue attendue dans un grand oral.

---

## Notions clés à maîtriser

### Modèles de service cloud : Infrastructure, Plateforme et Logiciel en tant que service

Les modèles de service cloud définissent le niveau d'abstraction et la répartition des responsabilités entre le fournisseur et le client. On en distingue trois grandes catégories historiques, auxquelles s'ajoutent des modèles plus récents.

L'Infrastructure en tant que service, ou Infrastructure as a Service, est le modèle le plus bas niveau. Le fournisseur met à disposition des ressources informatiques virtualisées : serveurs, stockage, réseau. Le client gère lui-même le système d'exploitation, le middleware, les runtimes et les applications. Des exemples emblématiques sont Amazon Web Services EC2, Azure Virtual Machines et Google Compute Engine. Ce modèle offre un contrôle maximum mais impose une charge opérationnelle importante.

La Plateforme en tant que service, ou Platform as a Service, va plus loin dans l'abstraction. Le fournisseur gère l'infrastructure et le runtime. Le client se concentre uniquement sur son code et ses données. C'est le modèle de prédilection pour les équipes de développement qui veulent aller vite sans se préoccuper des serveurs. Heroku, Azure App Service ou AWS Elastic Beanstalk en sont des exemples. Les études montrent qu'un déploiement peut passer de deux semaines à deux jours grâce à ce modèle.

Le Logiciel en tant que service, ou Software as a Service, représente le niveau d'abstraction maximal. L'application est entièrement gérée par le fournisseur, accessible depuis un navigateur. Le client ne contrôle que ses données et la configuration. Microsoft 365, Salesforce, ServiceNow ou Google Workspace sont des exemples devenus standards dans les organisations. Le marché SaaS mondial représentait cent quatre-vingt-dix-sept milliards de dollars en 2023 selon Gartner.

Deux modèles émergents méritent une attention particulière. Le Function as a Service, ou FaaS, permet l'exécution de fonctions à la demande, facturées à l'invocation. AWS Lambda est le leader du marché. Le paradigme serverless est plus large encore : il englobe le FaaS et le Backend as a Service, où toute gestion de serveur est entièrement abstraite. La facturation se fait à la milliseconde d'exécution, sans ressource inactive. Le marché serverless affiche une croissance annuelle d'environ vingt-cinq pour cent.

Un concept transversal à tous ces modèles est le modèle de responsabilité partagée. La sécurité n'est pas uniquement du ressort du fournisseur. En Infrastructure as a Service, le client reste responsable du système d'exploitation et de tout ce qui est au-dessus. En Plateforme en tant que service, le fournisseur prend en charge le runtime. En Logiciel en tant que service, le fournisseur gère tout sauf les données et les accès utilisateurs. Incomprendre cette répartition est la première source d'angles morts de sécurité dans les organisations. Gartner estime que jusqu'en 2025, quatre-vingt-dix-neuf pour cent des défaillances de sécurité cloud seront imputables au client, pas au fournisseur.

---

### Modèles de déploiement cloud : public, privé, hybride et multi-cloud

Les modèles de déploiement désignent la façon dont l'infrastructure cloud est hébergée et partagée. Chaque modèle répond à des besoins différents en termes de sécurité, de souveraineté, de coûts et de flexibilité.

Le cloud public est une infrastructure mutualisée gérée par un fournisseur tiers comme Amazon Web Services, Microsoft Azure ou Google Cloud Platform. Les ressources sont partagées entre plusieurs clients grâce à une isolation logique. C'est le modèle le plus économique à court terme, avec une facturation à l'usage. Sa limite principale est le moindre contrôle sur la sécurité et la localisation des données.

Le cloud privé est une infrastructure dédiée à une seule organisation, hébergée sur ses propres locaux ou chez un hébergeur tiers. Il donne un contrôle total sur la configuration, la sécurité et la localisation des données. Des technologies comme VMware vSphere, OpenStack ou Nutanix permettent de le mettre en œuvre. Son investissement initial est élevé, mais il est incontournable pour les secteurs réglementés comme la banque ou la santé.

Le cloud hybride combine cloud public et cloud privé, interconnectés via un réseau privé virtuel ou une liaison dédiée. Il permet de conserver les workloads sensibles sur une infrastructure maîtrisée tout en exploitant le cloud public pour les besoins variables. Le cloud bursting en est l'illustration parfaite : une organisation déborde automatiquement sur le cloud public lors de pics de charge. Des solutions comme Azure Arc, AWS Outposts ou Google Anthos facilitent cette orchestration.

La stratégie multi-cloud consiste à utiliser plusieurs fournisseurs cloud publics simultanément. Les motivations sont multiples : éviter la dépendance à un seul fournisseur, optimiser les coûts, choisir le meilleur service de chaque acteur selon les besoins. En 2024, quatre-vingt-sept pour cent des entreprises ont adopté une stratégie multi-cloud selon Flexera. Sa complexité opérationnelle est son principal inconvénient.

Une notion importante est l'élasticité, qui se distingue de la simple scalabilité. La scalabilité est la capacité à monter en charge. L'élasticité inclut aussi la capacité à réduire les ressources automatiquement quand la charge baisse, sans intervention manuelle. C'est cette propriété qui rend le cloud fondamentalement différent d'une infrastructure traditionnelle : on ne paie que ce que l'on consomme réellement.

---

### Cloud souverain : enjeux de souveraineté et de confiance

Le cloud souverain désigne une offre cloud garantissant que les données sont hébergées et traitées sur le territoire national, par des entités soumises exclusivement au droit français ou européen, sans possibilité de transfert vers des juridictions étrangères.

La distinction entre cloud souverain et cloud de confiance est essentielle. Le cloud de confiance est un label intermédiaire : l'infrastructure peut être opérée par un acteur non-européen, mais avec des protections contractuelles et techniques pour isoler les données. Il ne garantit pas l'immunité totale aux lois extraterritoriales. Le cloud souverain va plus loin : l'opérateur doit être une entité de droit français ou européen, sans capital ni dépendance technologique étrangère significative.

En France, le référentiel le plus exigeant est SecNumCloud, délivré par l'Agence Nationale de la Sécurité des Systèmes d'Information, l'ANSSI. Il impose l'hébergement exclusif sur le territoire de l'Union européenne, un opérateur de droit français sans subordination à une loi étrangère, un cloisonnement technique rigoureux et des audits réguliers. En 2024, seules quelques offres disposent de cette qualification : OVHcloud et 3DS Outscale, filiale de Dassault Systèmes. Ce référentiel est obligatoire pour les Opérateurs d'Importance Vitale et les données de santé.

Deux initiatives méritent attention. S3NS est un partenariat entre Thales et Google Cloud visant la qualification SecNumCloud tout en s'appuyant sur les technologies Google. Bleu est un projet similaire impliquant Capgemini, Orange et Microsoft Azure. Ces modèles font débat : certains experts, dont des membres de l'ANSSI, estiment qu'une dépendance technologique à un acteur américain ne protège pas réellement contre le CLOUD Act américain.

Gaia-X est une initiative lancée en 2019 par la France et l'Allemagne pour créer un écosystème de données européen interopérable. Ce n'est pas un fournisseur cloud mais un cadre de gouvernance et de labellisation. Ses résultats sont jugés mitigés : l'adoption est lente, et la participation d'acteurs américains au sein même de l'initiative soulève des questions sur son indépendance réelle.

La doctrine "Cloud au centre" de la Direction Interministérielle du Numérique, publiée en 2021, impose que les nouvelles applications de l'État soient hébergées sur le cloud, avec priorité aux offres SecNumCloud pour les données sensibles. Elle concerne plus de huit cents applications de l'État français.

---

### Économie du cloud : modèles tarifaires et gestion des coûts

L'économie du cloud repose sur une transformation fondamentale : les dépenses informatiques passent du Capital Expenditure, les investissements en immobilisations, vers l'Operating Expenditure, les charges opérationnelles courantes. Cette conversion change la comptabilité, la fiscalité et la planification budgétaire des organisations.

Le modèle pay-as-you-go, ou paiement à l'usage, est la facturation par défaut des clouds publics : à la seconde ou à la minute selon la consommation réelle. Il est idéal pour les workloads imprévisibles ou variables, mais son tarif unitaire est le plus élevé.

Pour optimiser les coûts, les fournisseurs proposent des engagements à long terme. Les Reserved Instances, ou instances réservées, sont des engagements de un à trois ans sur un type d'instance spécifique, en échange d'une réduction de trente à soixante-dix pour cent par rapport au tarif à l'usage. Les Savings Plans sont des engagements sur un montant de dépense horaire minimum, plus flexibles car non liés à un type d'instance précis. Ces deux mécanismes sont adaptés aux workloads stables et prévisibles, comme les serveurs de production ou les bases de données.

Les Spot Instances, ou instances préemptibles, représentent les capacités non utilisées vendues avec une décote de soixante-dix à quatre-vingt-dix pour cent. Elles peuvent être interrompues avec un préavis très court. Elles conviennent aux traitements tolérants aux interruptions : apprentissage automatique, rendu graphique, traitements par lots.

Les frais de sortie, ou egress fees, sont souvent oubliés dans les budgets initiaux. Ils correspondent à la facturation du trafic de données sortant du cloud vers internet ou vers d'autres régions. Ces frais représentent en moyenne cinq à quinze pour cent de la facture cloud totale d'une entreprise. Ils créent une asymétrie qui rend la sortie coûteuse et favorise la dépendance fournisseur.

Sans gouvernance FinOps, les entreprises constatent fréquemment une dérive de trente à quarante pour cent par rapport aux prévisions. Flexera 2024 indique que trente-deux pour cent du budget cloud est gaspillé en ressources inutilisées ou surdimensionnées. Le cloud ne réduit pas mécaniquement les coûts : il faut une discipline de pilotage financier continue. Le FinOps, Financial Operations, est la pratique qui réunit ingénierie, finance et métier pour optimiser les dépenses cloud en temps réel.

---

### Vendor lock-in et réversibilité : gérer la dépendance fournisseur

Le vendor lock-in, ou dépendance fournisseur, désigne la situation dans laquelle une organisation ne peut pas changer de prestataire cloud sans coûts excessifs ou complexité technique majeure. Cinquante-neuf pour cent des entreprises l'identifient comme leur principale préoccupation cloud selon Flexera 2024.

Il existe cinq mécanismes principaux de dépendance. Le premier est le lock-in technique : l'utilisation de services propriétaires sans équivalent standard impose une réécriture applicative lors d'une migration. Le deuxième est le lock-in des données : les frais de sortie rendent financièrement dissuasive l'extraction de volumes massifs de données. Le troisième est le lock-in contractuel : les engagements pluriannuels avec réductions conditionnelles à la continuité. Le quatrième est le lock-in des compétences : les équipes formées sur les outils propriétaires d'un fournisseur sont difficiles à reconvertir. Le cinquième est le lock-in des intégrations : les APIs propriétaires et les connecteurs natifs créent une dépendance par l'écosystème.

Pour réduire la dépendance, plusieurs standards et outils sont disponibles. Kubernetes, standard open source de la Cloud Native Computing Foundation, fonctionne de manière identique sur tous les clouds et permet la portabilité des applications conteneurisées. Terraform, outil d'Infrastructure as Code, permet de décrire l'infrastructure dans un langage commun indépendant du fournisseur. Les bases de données open source comme PostgreSQL ou MySQL offrent une portabilité que les services managés propriétaires ne garantissent pas. MinIO et Ceph implémentent l'API de stockage S3 d'Amazon Web Services, devenue un standard de facto du stockage objet.

L'exit plan est un document stratégique recommandé par l'ANSSI et l'ENISA. Il définit, pour chaque service cloud critique, les conditions, coûts, délais et alternatives pour une migration vers un autre fournisseur. Un exit plan documenté constitue aussi un levier de négociation puissant : la preuve qu'une migration est techniquement faisable en quelques mois permet d'obtenir des remises supplémentaires significatives.

Sur le plan réglementaire, le Data Act européen, entré en vigueur en janvier 2024 et applicable depuis septembre 2025, impose la réversibilité technique et commerciale. Il prévoit la suppression progressive des frais de migration d'ici 2027 et l'interopérabilité entre services cloud.

---

### CLOUD Act et transferts de données : la juridiction américaine au cœur de l'enjeu européen

Le CLOUD Act, Clarifying Lawful Overseas Use of Data Act, est une loi fédérale américaine de 2018 qui permet aux autorités américaines de contraindre des entreprises de droit américain à fournir des données stockées à l'étranger. Toute organisation utilisant Amazon Web Services, Microsoft Azure ou Google Cloud utilise des services d'entreprises soumises au CLOUD Act. Leurs données peuvent donc théoriquement être accessibles par les autorités américaines, indépendamment de leur localisation physique sur des serveurs en Europe.

La FISA Section 702, Foreign Intelligence Surveillance Act, est complémentaire. Elle permet à la National Security Agency et au Federal Bureau of Investigation de surveiller les communications de ressortissants étrangers localisés hors des États-Unis, sans mandat individuel, en contraignant les fournisseurs de services américains. Elle a été renouvelée en 2024 pour deux ans.

L'arrêt Schrems II, rendu par la Cour de Justice de l'Union européenne en juillet 2020, a invalidé le Privacy Shield, le cadre de transfert de données entre l'Union européenne et les États-Unis. La cour a estimé que la surveillance américaine ne respecte pas les standards européens de protection des données. Cet arrêt a contraint des milliers d'entreprises à revoir leur base juridique pour les transferts transatlantiques.

Le Data Privacy Framework, adopté en juillet 2023, est le successeur du Privacy Shield. Il repose sur un décret exécutif américain créant un mécanisme de recours pour les ressortissants européens. Son principal risque est une possible invalidation par la Cour de Justice de l'Union européenne, ce que certains qualifient déjà de "Schrems III".

Un point de tension particulier est le gag order : l'ordonnance de non-divulgation qui peut accompagner une demande d'accès aux données, interdisant à l'opérateur d'informer le client ou la personne concernée. Cette pratique est incompatible avec l'obligation d'information du Règlement Général sur la Protection des Données, créant un conflit de juridictions non résolu à ce jour.

La distinction entre data residency et souveraineté des données est importante. La data residency désigne la localisation physique des données dans une région géographique. La souveraineté désigne la juridiction juridique applicable. Un opérateur américain peut héberger des données en France tout en restant soumis au CLOUD Act : la localisation physique ne suffit pas à garantir la souveraineté juridique.

---

### Sécurité cloud : gestion de la posture, accès et protection native des applications

La sécurité cloud regroupe des outils et pratiques spécialisés pour protéger les environnements cloud contre les mauvaises configurations, les accès non autorisés et les menaces. La grande majorité des incidents cloud sont causés par des erreurs de configuration, pas par des failles zero-day inconnues.

Le Cloud Security Posture Management, ou CSPM, analyse en continu la configuration des ressources cloud : gestion des identités et des accès, stockage, réseau, services managés. Il compare les configurations aux référentiels de sécurité comme les CIS Benchmarks ou les normes NIST et ISO 27001. Il génère des alertes et peut appliquer des remédiations automatiques. AWS Security Hub, Azure Security Center et des solutions tierces comme Wiz ou Prisma Cloud remplissent cette fonction.

Le Cloud Access Security Broker, ou CASB, s'intercale entre les utilisateurs et les services cloud pour contrôler, auditer et protéger les accès. Il opère en mode proxy ou via des APIs et remplit quatre fonctions : la visibilité sur le Shadow IT, la conformité via la prévention des pertes de données, la protection contre les menaces et le contrôle d'accès.

Le Cloud-Native Application Protection Platform, ou CNAPP, est une plateforme unifiée définie par Gartner en 2021. Elle regroupe le CSPM, le Cloud Workload Protection Platform ou CWPP pour la protection à l'exécution, et le Cloud Infrastructure Entitlement Management ou CIEM pour la gestion des droits. Elle couvre le cycle de vie complet de l'application cloud native, du code au runtime en production.

Le CIEM mérite une attention particulière. Il détecte les comptes surprivilégiés, les permissions inutilisées, les rôles transitifs dangereux. Des audits CIEM révèlent souvent que soixante-dix à quatre-vingts pour cent des rôles configurés n'ont pas été utilisés depuis des mois, créant une surface d'attaque considérable en cas de compromission de compte.

Une landing zone est une architecture cloud préconfigurée et sécurisée servant de socle pour déployer des workloads. Les guardrails sont des politiques préventives et détectives appliquées à toute l'organisation cloud qui empêchent les dérives de configuration dès la création des ressources.

---

### Chiffrement et gestion des clés : protéger les données dans le cloud

Le chiffrement est le processus de transformation de données lisibles en données illisibles sans clé de déchiffrement. Dans le cloud, on distingue trois états de protection.

Le chiffrement at rest protège les données stockées sur disque. L'algorithme standard est AES-256, considéré sûr par le National Institute of Standards and Technology jusqu'en 2030 et au-delà. Chaque fournisseur cloud propose des mécanismes natifs : AWS S3 Server-Side Encryption, Azure Storage Service Encryption, Google Cloud Customer-Managed Encryption Keys.

Le chiffrement in transit protège les données pendant leur transmission sur le réseau. Les protocoles standards sont TLS 1.2 et TLS 1.3, ce dernier étant recommandé par l'ANSSI depuis 2020. TLS 1.0 et 1.1 sont officiellement dépréciés depuis 2021.

Le chiffrement in use, ou Confidential Computing, est une technologie émergente permettant de chiffrer les données même pendant leur traitement en mémoire, via des environnements d'exécution de confiance comme Intel SGX ou AMD SEV.

La gestion des clés détermine le niveau de contrôle réel sur les données. Le Bring Your Own Key, ou BYOK, permet au client de générer ses propres clés de chiffrement et de les importer dans le service de gestion de clés du fournisseur cloud. Le client possède la clé, mais le fournisseur cloud pourrait y accéder techniquement. Le Hold Your Own Key, ou HYOK, va plus loin : le client conserve ses clés sur une infrastructure entièrement sous son contrôle, typiquement un module de sécurité matérielle on-premise. Le fournisseur cloud ne peut jamais accéder aux clés. C'est le niveau de contrôle maximal, utilisé par les banques pour les données les plus sensibles.

Les Hardware Security Modules, ou HSM, sont des modules matériels certifiés FIPS 140-2 ou 140-3 dédiés à la génération, au stockage et à la protection des clés cryptographiques dans un environnement physiquement isolé.

Une menace émergente mérite d'être connue : le "Harvest Now, Decrypt Later". Des acteurs malveillants collectent aujourd'hui des données chiffrées avec des algorithmes classiques, en anticipant que les ordinateurs quantiques leur permettront de les déchiffrer dans le futur. Cela justifie la migration progressive vers la cryptographie post-quantique, dont le National Institute of Standards and Technology a publié les premiers standards en 2022 et 2024.

---

### SASE et SD-WAN : connecter et sécuriser les utilisateurs dans un monde cloud

Le SASE, Secure Access Service Edge, prononcé "sassy", est un cadre architectural défini par Gartner en 2019. Il converge les fonctions réseau représentées par le Software-Defined Wide Area Network et les fonctions de sécurité cloud dans un service cloud unifié et distribué. Son objectif est de connecter et sécuriser tous les utilisateurs, appareils et applications depuis n'importe quel endroit, sans faire passer le trafic par un datacenter central.

Le Software-Defined Wide Area Network, ou SD-WAN, virtualise et abstrait la couche réseau étendue. Il permet d'utiliser plusieurs types de liaisons : liaisons MPLS traditionnelles, fibre internet, connexions 4G ou 5G. Il applique des politiques de routage intelligentes selon l'application et la qualité du lien, avec un basculement automatique en cas de panne.

La Security Service Edge, ou SSE, est la composante sécurité du SASE. Elle regroupe quatre éléments. La Secure Web Gateway filtre le web et inspecte le trafic chiffré. Le Cloud Access Security Broker contrôle les accès aux applications SaaS. Le Zero Trust Network Access, ou ZTNA, remplace le réseau privé virtuel traditionnel en donnant accès uniquement aux applications spécifiques autorisées, sur la base de l'identité et du contexte. Le Firewall as a Service est un pare-feu cloud avec inspection applicative.

Le SASE élimine le backhauling : la pratique consistant à faire transiter le trafic internet des utilisateurs via un datacenter central avant de le laisser sortir. Avec le SASE, le trafic est traité au point de présence le plus proche de l'utilisateur, réduisant la latence de trente à cinquante pour cent.

La généralisation du télétravail a rendu cette architecture incontournable. Les réseau privés virtuels traditionnels, dimensionnés pour une minorité d'utilisateurs distants, se sont retrouvés saturés lors de la crise du COVID-19. Le ZTNA offre une alternative plus granulaire et plus sûre : l'utilisateur accède à une application spécifique, pas à l'ensemble du réseau.

---

### Migration cloud — Les 7R : choisir la bonne stratégie pour chaque application

Les 7R sont un cadre de stratégies de migration cloud permettant à une direction des systèmes d'information de décider comment traiter chaque application lors d'un passage vers le cloud. Ce framework, popularisé par Amazon Web Services et Gartner, structure la phase d'évaluation de préparation au cloud.

Le premier R est le Rehost, également appelé Lift and Shift. Il s'agit de migrer l'application sans la modifier dans une machine virtuelle cloud. C'est la stratégie la plus rapide, sans optimisation, idéale pour sortir rapidement d'un datacenter en fin de contrat.

Le deuxième R est le Replatform, ou Lift Tinker and Shift. On migre avec des optimisations mineures sans refonte du code : par exemple, passer d'une base de données on-premise à un service managé de bases de données en cloud.

Le troisième R est le Repurchase, ou Drop and Shop. On remplace l'application par une solution logicielle en tant que service équivalente, par exemple remplacer un outil de gestion de la relation client développé en interne par Salesforce.

Le quatrième R est le Refactor ou Re-architect. Il s'agit de revoir en profondeur l'architecture pour exploiter les services cloud natifs : microservices, serverless, conteneurs. C'est la stratégie qui offre le plus de bénéfices mais aussi la plus complexe.

Le cinquième R est le Retire : désactiver l'application. Elle n'apporte plus de valeur métier ou est couverte par une autre solution. En moyenne, trente pour cent des applications identifiées lors d'un assessment sont candidates à cette stratégie.

Le sixième R est le Retain, ou Revisit : conserver l'application on-premise pour l'instant car les dépendances ne sont pas résolues ou le coût de migration dépasse le bénéfice.

Le septième R est le Relocate, ou Hypervisor Lift and Shift : migrer l'infrastructure virtualisée vers le cloud sans modifier le système d'exploitation ni les machines virtuelles, par exemple via VMware Cloud sur Amazon Web Services.

Le Cloud Readiness Assessment est l'évaluation préalable indispensable. Il produit une matrice de priorisation par application selon la complexité technique et la valeur métier. Le Wave Planning organise ensuite la migration en vagues successives, des applications les plus simples aux plus complexes, pour limiter les risques et apprendre au fil du temps.

Le Strangler Fig Pattern, proposé par Martin Fowler, est une technique de modernisation progressive d'une application legacy. On développe de nouvelles fonctionnalités cloud natives autour du système existant et on redirige progressivement le trafic vers le nouveau système jusqu'à ce que l'ancien soit entièrement remplacé. Cette approche évite la réécriture big-bang, dont le risque d'échec est très élevé.

---

### Legacy et dette technique : comprendre le poids du passé pour mieux le gérer

Un système legacy est une application ancienne, difficile à maintenir et à faire évoluer, mais qui reste en production car elle assure des fonctions métier critiques. La dette technique, concept introduit par Ward Cunningham en 1992, désigne l'accumulation de compromis de conception qui ralentissent les évolutions futures et augmentent le coût de maintenance.

La métaphore de la dette financière est éclairante : un code mal conçu livré rapidement, c'est emprunter de l'argent. On avance vite à court terme, mais on rembourse avec des intérêts sous forme de ralentissement des développements futurs. La dette technique mondiale est estimée à mille cinq cent vingt milliards de dollars selon le CAST Research Labs en 2022.

Pour une direction des systèmes d'information, les chiffres sont préoccupants : entre soixante et quatre-vingts pour cent du budget informatique des grandes entreprises est consacré à la maintenance des systèmes existants, laissant peu de ressources pour l'innovation.

Il existe cinq grandes approches de modernisation. La maintenance pure consiste à corriger les bugs et mettre à jour les dépendances de sécurité sans évolution fonctionnelle. Le refactoring, popularisé par Martin Fowler dans son ouvrage de référence de 1999, améliore la structure interne du code sans changer son comportement externe. La réarchitecture repense l'architecture globale, par exemple en passant d'un monolithe à une architecture en microservices. Le remplacement abandonne le système pour une solution packagée ou une réécriture complète. L'encapsulation ou wrapping consiste à entourer le système legacy d'une API REST pour le consommer comme un service moderne, sans toucher au code.

SonarQube est l'outil de référence pour mesurer la dette technique. Il note le code de A à E selon le rating SQALE et estime le temps de remboursement en jours-hommes. Le COBOL fait encore tourner quatre-vingt-dix-cinq pour cent des transactions de distributeurs automatiques de billets dans le monde.

La Boy Scout Rule est une pratique culturelle efficace : à chaque modification du code, laisser le module dans un meilleur état qu'avant, comme un scout qui laisse son camping plus propre qu'il ne l'a trouvé. Cela permet de gérer la dette de manière continue, sans projet dédié.

---

### Virtualisation : la brique fondamentale du cloud

La virtualisation est la technologie qui permet de créer des représentations logicielles de ressources physiques. Une machine virtuelle est un environnement informatique isolé qui émule un ordinateur complet, partageant les ressources physiques d'un hôte via un hyperviseur. C'est la brique fondamentale sur laquelle repose tout le cloud computing.

La virtualisation a transformé l'exploitation des datacenters. Elle a permis de faire passer le taux d'utilisation des serveurs de cinq à quinze pour cent vers soixante à quatre-vingts pour cent, réduisant de trente à quarante pour cent les coûts des datacenters d'entreprise depuis 2005.

Les hyperviseurs se distinguent en deux types. L'hyperviseur de type 1, dit bare-metal, s'exécute directement sur le matériel physique sans système d'exploitation hôte intermédiaire. Il offre de hautes performances. C'est le modèle utilisé dans les datacenters d'entreprise et les clouds publics. VMware ESXi, Microsoft Hyper-V, Citrix Hypervisor et KVM en sont des exemples. L'hyperviseur de type 2, dit hosted, s'exécute comme une application au-dessus d'un système d'exploitation hôte. Il est moins performant mais plus simple à installer, utilisé pour les postes de travail et le développement. Oracle VirtualBox et VMware Workstation en sont des exemples.

VMware, fondé en 1998 et racheté par Broadcom en novembre 2023 pour soixante et un milliards de dollars, était présent dans quatre-vingts pour cent des datacenters d'entreprise avant ce rachat. Les changements de licences qui ont suivi, avec la fin des licences perpétuelles et le passage à un modèle bundle obligatoire, ont provoqué un mouvement important vers des alternatives open source.

Proxmox VE est la principale alternative open source. Basé sur KVM pour les machines virtuelles et LXC pour les conteneurs Linux, il offre une interface web intégrée, le support du clustering, la haute disponibilité et un stockage distribué via Ceph. Il est gratuit sous licence libre et a connu une croissance de quatre cents pour cent des nouvelles installations entre 2022 et 2024.

Nutanix propose une infrastructure hyper-convergée qui fusionne le calcul, le stockage et le réseau dans des nœuds standardisés. Son hyperviseur AHV est basé sur KVM et fourni sans surcoût.

KVM équipe la quasi-totalité des clouds publics majeurs : Amazon Web Services utilise Nitro, basé sur KVM, et Google Cloud Platform utilise également KVM.

---

### Conteneurisation avec Docker et Kubernetes : la portabilité applicative

La conteneurisation est une technique de virtualisation légère qui isole une application et ses dépendances dans un conteneur portable et autonome. Contrairement à une machine virtuelle, un conteneur ne virtualise pas le matériel complet mais uniquement l'espace utilisateur, en partageant le noyau de l'hôte. Les conteneurs démarrent en secondes là où les machines virtuelles prennent des minutes. En 2023, quatre-vingt-sept pour cent des organisations utilisent des conteneurs en production.

Docker est le moteur de conteneurs le plus répandu. Son cycle de vie est simple. Le Dockerfile est un fichier déclaratif décrivant l'image. L'image Docker est un artefact immuable et versionné. Le Container Registry est le dépôt d'images, comme Docker Hub ou Amazon Elastic Container Registry. Le conteneur est l'instance en cours d'exécution d'une image.

Kubernetes, souvent abrégé K8s, est l'orchestrateur open source de référence. Il automatise le déploiement, la mise à l'échelle et la gestion des conteneurs en production. Son architecture se divise en deux parties. Le Control Plane centralise l'intelligence du cluster avec l'API Server, le Scheduler, le Controller Manager et etcd pour le stockage de l'état. Les Worker Nodes exécutent les workloads via le kubelet.

Quelques concepts Kubernetes méritent d'être maîtrisés. Le Pod est l'unité atomique de déploiement, regroupant un ou plusieurs conteneurs partageant réseau et stockage. Un Deployment décrit l'état désiré pour les applications sans état. Un StatefulSet gère les applications avec état persistant comme les bases de données, en garantissant un ordre de démarrage et une identité stable. Helm est le gestionnaire de paquets Kubernetes, permettant de déployer des applications complexes via des charts paramétrables.

La Cloud Native Computing Foundation, ou CNCF, héberge Kubernetes et plus de cent cinquante projets cloud natifs open source. Elle délivre des certifications reconnues pour les ingénieurs Kubernetes.

La sécurité des conteneurs est la préoccupation numéro un : trente-sept pour cent des incidents cloud impliquent des images vulnérables selon le rapport Sysdig 2024.

---

### Service Mesh : sécuriser et observer la communication entre microservices

Un service mesh est une couche d'infrastructure dédiée à la gestion de la communication entre microservices. Il injecte un proxy sidecar à côté de chaque service pour gérer de façon transparente le chiffrement mutuel TLS, le routage, la résilience et l'observabilité.

Sans service mesh, la logique de communication sécurisée est codée dans chaque application, créant de la duplication et des risques. Le service mesh externalise cette complexité au niveau de l'infrastructure.

Un service mesh se compose de deux plans. Le Data Plane, ou plan de données, est l'ensemble des proxies légers déployés automatiquement à côté de chaque instance de service. Le proxy le plus utilisé est Envoy, développé initialement par Lyft. Tout le trafic réseau passe par ce sidecar de façon transparente pour l'application. Le Control Plane, ou plan de contrôle, centralise la configuration et distribue les politiques aux proxies.

Les fonctionnalités clés d'un service mesh sont nombreuses. Le mTLS, Mutual Transport Layer Security, assure le chiffrement et l'authentification mutuelle automatiques entre tous les services sans modifier le code applicatif. Le routage avancé permet les déploiements progressifs : canary releases, tests A/B, traffic shifting. La résilience est gérée via les retries automatiques, les timeouts et les circuit breakers qui coupent temporairement les appels vers un service défaillant pour éviter les pannes en cascade. L'observabilité est générée automatiquement : métriques de latence, taux d'erreur, traces distribuées.

Istio est le service mesh le plus utilisé, représentant soixante-et-onze pour cent des adoptions. Il est développé par Google, IBM et Lyft. Il est devenu un projet CNCF Graduated en 2023. Linkerd est une alternative plus légère et plus simple à opérer, avec des proxies écrits en Rust.

---

### Cloud Native et 12-Factor App : exploiter pleinement le cloud

Le terme cloud native désigne une approche de conception et d'exploitation d'applications qui exploite pleinement les capacités du cloud : élasticité, automatisation, résilience. Elle s'appuie sur des microservices, des conteneurs, l'orchestration et des pratiques DevOps avec intégration et déploiement continus.

La Cloud Native Computing Foundation définit le cloud native autour de quatre piliers : les conteneurs, l'orchestration via Kubernetes, les microservices et les pratiques DevOps avec des pipelines d'intégration et de déploiement continus.

Les propriétés clés d'une application cloud native sont l'auto-healing, c'est-à-dire le redémarrage automatique des conteneurs défaillants par l'orchestrateur, l'auto-scaling ou ajustement automatique du nombre d'instances en fonction de la charge, l'immutabilité, signifiant que les conteneurs et infrastructures ne sont jamais modifiés en place mais recréés depuis des artefacts versionnés, et l'observabilité avec les trois piliers que sont les logs, les métriques et les traces.

La méthodologie 12-Factor App, formalisée par Heroku en 2012, définit douze principes pour concevoir des applications cloud natives portables, scalables et maintenables. Quelques facteurs clés méritent une attention particulière. Le facteur Config indique que toute configuration doit être injectée via des variables d'environnement, jamais codée dans le code source. Le facteur Stateless Processes impose que les processus soient sans état, l'état étant externalisé dans des services comme une base de données ou un cache, ce qui permet le scaling horizontal. Le facteur Disposability exige un démarrage rapide et un arrêt gracieux pour permettre l'élasticité. Le facteur Dev Prod Parity préconise des environnements de développement et de production aussi similaires que possible pour réduire les bugs en production.

Une application migée sans refonte par un simple Lift and Shift ne bénéficie pas de ces propriétés. Elle s'exécute dans le cloud mais n'en exploite ni l'élasticité, ni la résilience, ni l'auto-scaling. C'est souvent plus coûteux qu'on-premise. Les entreprises cloud natives déploient du code deux cent huit fois plus fréquemment que les entreprises traditionnelles selon le rapport DORA 2023.

---

### Certifications et normes cloud : les garanties formelles de sécurité

Les certifications cloud sont des référentiels qui permettent aux fournisseurs de démontrer leur niveau de sécurité, de conformité et de protection des données. Pour une direction des systèmes d'information, le choix d'un fournisseur cloud certifié est souvent un prérequis légal.

ISO 27017 est une extension de l'ISO 27001 spécifique au cloud. Elle définit des contrôles de sécurité supplémentaires pour les fournisseurs et clients cloud, couvrant la séparation des environnements virtuels, la journalisation et la suppression sécurisée des données. ISO 27018 est le premier standard international dédié à la protection des données à caractère personnel dans le cloud public. Il interdit notamment d'utiliser les données clients à des fins commerciales et impose la notification des violations.

Le programme CSA STAR, développé par la Cloud Security Alliance, propose trois niveaux de certification. Le niveau 1 est une auto-évaluation via un questionnaire public. Le niveau 2 est un audit indépendant basé sur l'ISO 27001 augmenté de la Cloud Controls Matrix, un référentiel de cent quatre-vingt-dix-sept contrôles sur dix-sept domaines.

SOC 2 Type II est un rapport d'audit américain évaluant les contrôles internes d'un fournisseur sur cinq critères : sécurité, disponibilité, intégrité des traitements, confidentialité et vie privée. La différence entre Type I et Type II est fondamentale : le Type II couvre une période de six à douze mois, démontrant la permanence des contrôles dans le temps.

La certification HDS, Hébergement de Données de Santé, est obligatoire en France pour tout hébergeur traitant des données de santé à caractère personnel. Elle est délivrée par des organismes accrédités sur la base de l'ISO 27001 augmentée d'un référentiel spécifique.

SecNumCloud est le visa de sécurité de l'ANSSI, le plus exigeant pour les données sensibles de l'État. En 2024, seuls OVHcloud et 3DS Outscale disposent d'offres qualifiées.

L'EUCS, European Union Cybersecurity Certification Scheme for Cloud Services, est en cours de finalisation par l'ENISA. Son niveau High serait équivalent à SecNumCloud et constituerait un cadre européen harmonisé.

---

### Data Act et Data Governance Act : le nouveau droit européen de la donnée

Le Data Act est un règlement européen, numéro UE 2023/2854, entré en vigueur le 11 janvier 2024 et applicable depuis le 12 septembre 2025. Il régit le partage, l'accès et l'utilisation des données générées par les produits connectés et les services associés. Il s'inscrit dans un arsenal réglementaire plus large comprenant le Règlement Général sur la Protection des Données de 2018, le Data Governance Act applicable depuis septembre 2023 et l'AI Act.

Pour les fournisseurs cloud, le Data Act impose des obligations importantes. Ils doivent garantir la réversibilité technique et commerciale effective. Les frais de migration doivent être progressivement supprimés jusqu'à leur disparition totale en 2027. L'interopérabilité entre services cloud est requise. Ces dispositions visent directement à réduire le vendor lock-in et à faciliter la concurrence sur le marché européen du cloud.

Pour les produits connectés, le Data Act établit un droit d'accès des utilisateurs aux données générées par les objets qu'ils utilisent. Une voiture connectée génère des données de conduite, de consommation, de diagnostics. Avant le Data Act, ces données appartiennent de facto au constructeur. Après le Data Act, le conducteur peut demander à les partager avec son assureur ou un garagiste indépendant.

Le partage Business-to-Government, ou B2G, permet aux autorités publiques d'accéder en cas de nécessité, comme une crise ou une catastrophe naturelle, aux données pertinentes détenues par des entreprises privées dans l'intérêt général.

Le Data Governance Act, antérieur et complémentaire, encadre les mécanismes de partage volontaire de données. Il crée un statut réglementé pour les intermédiaires de données, des entités qui facilitent le partage entre acteurs sans pouvoir utiliser elles-mêmes les données. Il introduit aussi le concept d'altruisme des données : un cadre légal pour que des personnes ou organisations partagent volontairement leurs données pour l'intérêt général, par exemple la recherche médicale.

La Commission européenne estime que le Data Act libérera deux cent soixante-dix milliards d'euros de valeur économique d'ici 2028 en permettant une meilleure exploitation des données industrielles, dont quatre-vingts pour cent ne sont jamais utilisées aujourd'hui.

---

### Acteurs cloud : hyperscalers américains et alternatives européennes souveraines

Le marché du cloud computing est très concentré. Amazon Web Services, Microsoft Azure et Google Cloud Platform représentent ensemble soixante-sept pour cent du marché mondial en 2024 selon Synergy Research Group.

Amazon Web Services, pionnier du cloud public lancé en 2006, détient environ trente et un pour cent du marché. Il propose plus de deux cents services et couvre trente-deux régions avec cent deux zones de disponibilité dans le monde. Sa profondeur d'offre reste inégalée.

Microsoft Azure, deuxième acteur mondial avec environ vingt-cinq pour cent du marché, bénéficie d'une intégration profonde avec l'écosystème Microsoft, notamment Microsoft 365 et Active Directory. C'est l'acteur de référence pour les organisations très intégrées dans l'univers Microsoft.

Google Cloud Platform, troisième acteur avec environ onze pour cent du marché, est particulièrement fort sur les données, l'apprentissage automatique et les technologies open source. Kubernetes, TensorFlow et Istio sont nés chez Google.

Ces trois acteurs sont tous soumis au CLOUD Act américain, ce qui limite leur attractivité pour les données souveraines européennes.

Du côté européen, OVHcloud est le premier opérateur cloud européen, fondé en 1999 à Roubaix. Il dispose de quarante-trois datacenters dans douze pays et n'est pas soumis au CLOUD Act. Il détient la qualification SecNumCloud pour certaines offres et la certification HDS. Scaleway, filiale du groupe Iliad qui possède également Free, est particulièrement orientée vers les développeurs et les startups, avec un positionnement API-first et un engagement environnemental fort. 3DS Outscale, filiale de Dassault Systèmes, est spécialisée dans le secteur public et les Opérateurs d'Importance Vitale, avec la double qualification SecNumCloud et HDS.

Du côté de la sécurité, Wiz est une startup américaine fondée en 2020, valorisée à douze milliards de dollars en 2024, qui a révolutionné la sécurité cloud avec son approche sans agent et son graphe de sécurité corrélant configurations, vulnérabilités et expositions réseau. Elle est utilisée par quarante pour cent des entreprises du Fortune 100. Google a annoncé son acquisition pour vingt-trois milliards de dollars en 2024. Palo Alto Prisma Cloud est la solution historique de référence pour les grandes entreprises et le secteur bancaire.

---

## Questions du jury — Réponses structurées

**Quelle différence entre Infrastructure en tant que service, Plateforme en tant que service et Logiciel en tant que service ? Dans quel cas choisir l'un ou l'autre ?**

En Infrastructure en tant que service, vous gérez tout au-dessus du matériel virtualisé : le système d'exploitation, le middleware, le runtime et l'application. C'est le modèle à choisir quand vous avez besoin d'un contrôle précis sur l'environnement ou que vous migrez des systèmes existants sans les modifier. En Plateforme en tant que service, le fournisseur gère l'infrastructure et le runtime. Votre équipe se concentre uniquement sur le code. C'est le modèle pour accélérer le développement d'applications sans vouloir gérer des serveurs. En Logiciel en tant que service, l'application est entièrement gérée par le fournisseur. Vous ne contrôlez que vos données et la configuration. C'est le modèle pour les fonctions standards : messagerie, CRM, gestion des ressources humaines, où vous ne voulez pas différencier par la technologie.

**Qu'est-ce que le modèle de responsabilité partagée et quelles en sont les implications ?**

Le modèle de responsabilité partagée définit la frontière entre ce que le fournisseur cloud sécurise et ce que le client doit sécuriser lui-même. Le fournisseur est toujours responsable de la sécurité de l'infrastructure physique, de l'hyperviseur et des services natifs. Le client est toujours responsable de ses données et de la gestion des identités et des accès. Pour tout ce qui se trouve entre les deux, la responsabilité varie selon le modèle : en Infrastructure en tant que service, le client gère le système d'exploitation et au-dessus ; en Logiciel en tant que service, le fournisseur gère tout sauf les données et les configurations utilisateurs. La principale implication pour une direction des systèmes d'information est qu'une incompréhension de cette frontière génère des angles morts de sécurité. C'est la cause de quatre-vingt-dix-neuf pour cent des incidents cloud selon Gartner.

**Cloud souverain : pourquoi est-ce un enjeu pour les entreprises françaises ?**

Le CLOUD Act américain de 2018 permet aux autorités américaines de contraindre toute entreprise de droit américain à fournir des données, même stockées en France. Amazon Web Services, Microsoft Azure et Google Cloud sont tous des entreprises américaines soumises à cette loi. Pour une administration publique, un hôpital, un Opérateur d'Importance Vitale, utiliser ces services expose potentiellement des données sensibles à une demande des autorités américaines, y compris avec une ordonnance de non-divulgation interdisant d'en informer le client. Le cloud souverain, via la qualification SecNumCloud de l'ANSSI, garantit que l'opérateur est de droit français, qu'il n'existe pas de dépendance à une loi étrangère et que les données restent sous juridiction française ou européenne.

**Comment évaluer le coût réel du cloud par rapport à une infrastructure on-premise ?**

L'évaluation doit s'appuyer sur le Coût Total de Possession, ou TCO, sur trois à cinq ans. Pour le cloud, il faut comptabiliser : la facturation à l'usage ou les Reserved Instances, les frais de sortie de données souvent oubliés, les coûts de bande passante, les licences des outils de gestion cloud, et la formation des équipes. Pour l'infrastructure on-premise, il faut inclure le matériel, les licences logicielles, l'énergie, le refroidissement, la main d'œuvre d'exploitation, et le coût de remplacement à cinq ans. Sans oublier que le cloud transforme le capital en charges opérationnelles, avec des implications comptables et fiscales. En pratique, le cloud est souvent avantageux pour les workloads variables, mais pour les workloads stables et prévisibles à fort volume, on-premise peut être moins coûteux sur cinq ans. C'est ce que Dropbox a démontré en 2016 en rapatriant ses données, économisant soixante-quinze millions de dollars en deux ans.

**Quels sont les risques du vendor lock-in et comment les atténuer ?**

Les risques sont multiples : perte de pouvoir de négociation en cas de hausse tarifaire, coût de migration très élevé allant de quinze à trente-cinq pour cent du budget annuel informatique concerné selon Gartner, dépendance aux décisions stratégiques du fournisseur, et risque de continuité si le fournisseur change de modèle comme Broadcom avec VMware. Pour atténuer ces risques : utiliser des standards ouverts et des outils portables comme Kubernetes et Terraform, préférer des bases de données open source aux services managés propriétaires, éviter les services sans équivalent chez un concurrent, documenter un exit plan pour chaque service critique, et anticiper les exigences du Data Act sur la portabilité.

**Quels sont les 7R de la migration cloud et comment choisir la bonne stratégie ?**

Les 7R sont Rehost, Replatform, Repurchase, Refactor ou Re-architect, Retire, Retain et Relocate. Le choix repose sur une analyse coût-bénéfice pour chaque application : sa valeur métier, sa complexité technique, sa dette technique et ses contraintes réglementaires. Le Rehost convient aux applications qu'on doit migrer rapidement sans temps pour les modifier. Le Replatform s'applique quand on peut bénéficier de services managés sans réécriture. Le Repurchase est pertinent pour les fonctions standards sans différenciation. Le Refactor est réservé aux applications à forte valeur qui nécessitent d'exploiter pleinement le cloud. On commence toujours par un Cloud Readiness Assessment pour catégoriser toutes les applications avant de planifier les vagues de migration.

**Conteneurisation par rapport à virtualisation : quand privilégier l'une ou l'autre ?**

La virtualisation crée des machines virtuelles complètes avec leur propre système d'exploitation. Elle offre une isolation forte et une compatibilité avec tout type d'application, mais elle est plus lourde : démarrage en minutes, empreinte mémoire importante. La conteneurisation partage le noyau de l'hôte et isole uniquement l'espace utilisateur. Elle est plus légère : démarrage en secondes, densité plus élevée par hôte. Les conteneurs sont idéaux pour les applications cloud natives et les microservices dans des environnements DevOps. Les machines virtuelles restent nécessaires pour les workloads qui requièrent une isolation complète, un système d'exploitation spécifique ou une compatibilité avec des applications legacy. En pratique, les deux coexistent : les conteneurs tournent souvent à l'intérieur de machines virtuelles.

**Qu'est-ce que le Cloud Native et pourquoi migrer ne suffit pas ?**

Le Cloud Native est une façon de concevoir des applications pour exploiter pleinement les capacités du cloud : auto-scaling, auto-healing, déploiement continu, observabilité. Migrer une application sans la modifier, le simple Lift and Shift, la déplace dans le cloud mais sans lui apporter ces propriétés. Elle conserve ses limitations : elle ne se redimensionne pas automatiquement, elle n'est pas résiliente face aux pannes de nœuds, et elle coûte souvent plus cher qu'on-premise car elle n'exploite pas les ressources de façon dynamique. La méthodologie 12-Factor App définit les douze principes à respecter pour rendre une application réellement cloud native. Les entreprises qui respectent ces principes déploient deux cent huit fois plus fréquemment selon le rapport DORA 2023.

**Comment justifier un projet de migration cloud auprès du Comité de Direction ?**

Un dossier de migration cloud convaincant pour un Comité de Direction doit articuler quatre dimensions. La dimension financière : TCO comparé sur cinq ans, transformation du capital en charges opérationnelles, réduction des coûts de maintenance et de renouvellement matériel. La dimension stratégique : réduction du time-to-market, capacité à scaler rapidement pour saisir des opportunités, accès aux dernières innovations sans investissement en recherche et développement. La dimension de risque : résilience améliorée, continuité d'activité, sécurité gérée par des équipes spécialisées. La dimension de conformité : respect du RGPD, certification HDS si nécessaire, posture réglementaire renforcée. Il faut aussi être honnête sur les risques : coûts cachés comme les frais de sortie, risque de lock-in fournisseur, courbe d'apprentissage des équipes, et nécessité d'une gouvernance FinOps pour éviter les dérives.

---

## Points de vigilance pour le grand oral

Le premier point de vigilance est la confusion entre data residency et souveraineté des données. Héberger ses données dans un datacenter situé en France ne suffit pas si le fournisseur est une entreprise américaine soumise au CLOUD Act. La souveraineté est une question de juridiction, pas de géographie.

Le deuxième point est la tentation du Lift and Shift sans optimisation. Migrer à l'identique dans le cloud peut coûter plus cher qu'on-premise si les instances ne sont pas redimensionnées. Le cloud n'est pas synonyme de réduction de coûts automatique ; il faut une discipline de gouvernance financière continue.

Le troisième point est le modèle de responsabilité partagée. Rappellez systématiquement que la sécurité dans le cloud est une co-responsabilité. Le fournisseur sécurise son infrastructure, mais le client reste responsable de ses configurations, de ses données et de ses identités et accès. Ne pas le comprendre est la première source d'incidents cloud.

Le quatrième point concerne les chiffres. Ne confondez pas les parts de marché : Amazon Web Services est à trente et un pour cent, Azure à vingt-cinq pour cent, Google Cloud à onze pour cent. Et en France, seuls OVHcloud et 3DS Outscale disposent d'offres qualifiées SecNumCloud en 2024.

Le cinquième point est la nuance sur SecNumCloud. S3NS et Bleu ne sont pas encore qualifiés SecNumCloud en 2024. Ils sont en cours de qualification. Le débat sur leur vraie souveraineté reste ouvert car ils s'appuient technologiquement sur Google Cloud et Microsoft Azure respectivement.

Le sixième point est la distinction entre le Data Act et le RGPD. Le RGPD protège les données personnelles. Le Data Act porte sur les données des produits connectés et la portabilité cloud. Ce sont deux règlements différents avec des objectifs distincts, même si tous deux contribuent à la souveraineté numérique européenne.

Le septième point concerne la dette technique. Elle n'est pas uniquement un problème technique : c'est un problème stratégique. Soixante à quatre-vingts pour cent du budget informatique en maintenance laisse peu de marge pour l'innovation. La gérer est une décision managériale autant que technique.
