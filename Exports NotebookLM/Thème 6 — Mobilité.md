# Mobilité — Guide de révision complet

## Introduction

La mobilité est devenue un enjeu stratégique majeur pour toute Direction des Systèmes d'Information depuis la généralisation du travail hybride, accélérée par la crise Covid-19 de 2020. Ce thème couvre la manière dont les organisations gèrent les terminaux de leurs collaborateurs, sécurisent les accès distants à leur système d'information, construisent un environnement de travail numérique cohérent, et exploitent les nouvelles technologies comme le low-code, la RPA ou l'edge computing pour gagner en agilité. Pour un manager IT ou un architecte logiciel, maîtriser la mobilité, c'est être capable de répondre à une question simple mais complexe : comment permettre à chaque collaborateur de travailler efficacement, depuis n'importe où et depuis n'importe quel terminal, en garantissant la sécurité des données de l'entreprise ?

---

## Notions clés à maîtriser

### Gestion de la mobilité — UEM (Unified Endpoint Management)

L'UEM, pour Unified Endpoint Management, est une approche unifiée de gestion de l'ensemble des terminaux d'une organisation depuis une console centrale. Il rassemble smartphones, tablettes, PC et objets connectés sous un seul outil de pilotage. Pour bien comprendre l'UEM, il faut retracer son évolution historique.

Tout a commencé avec le MDM, le Mobile Device Management, qui gérait les appareils mobiles au niveau matériel : enrôlement, verrouillage, effacement complet à distance. Ensuite est apparu le MAM, le Mobile Application Management, qui descendait à la couche des applications pour déployer et révoquer des apps professionnelles sans toucher aux données personnelles. Puis le MCM, le Mobile Content Management, a sécurisé l'accès aux documents d'entreprise. Ces trois briques ont fusionné dans l'EMM, l'Enterprise Mobility Management. L'UEM est l'étape suivante : il étend l'EMM à tous les types de terminaux, y compris les PC Windows, macOS et les objets IoT, dans une console unique.

Parmi les mécanismes clés à connaître, il faut retenir l'enrôlement OTA, pour Over-The-Air, qui permet de déployer des profils de configuration et des politiques de sécurité sur les terminaux à distance, sans contact physique, via des programmes comme Apple DEP, Android Enterprise ou Windows Autopilot. La containerisation mobile crée un espace chiffré et isolé sur le terminal, séparant complètement les données professionnelles des données personnelles. Le wipe sélectif est la capacité à supprimer uniquement le container professionnel d'un terminal, sans effacer les photos et données personnelles de l'utilisateur — indispensable dans un contexte BYOD. Le geofencing définit des zones géographiques virtuelles et déclenche automatiquement des actions lorsqu'un appareil entre ou sort d'une zone, comme activer le VPN ou bloquer la caméra en zone sensible.

En termes de chiffres, le marché mondial de l'UEM était estimé à 4,7 milliards de dollars en 2023, avec une croissance annuelle de 20 %. Soixante-douze pourcent des entreprises ont subi une violation de données liée à un terminal mobile entre 2020 et 2023, et un employé utilise en moyenne trois à quatre appareils pour travailler. Les leaders du marché sont Microsoft Intune, intégré à l'écosystème Microsoft 365 et Azure AD, VMware Workspace ONE de Broadcom, et Jamf, spécialiste Apple.

### Politiques de terminaux — BYOD, COPE et les autres modèles

Les politiques de terminaux définissent qui possède et qui contrôle les appareils utilisés par les collaborateurs. Plusieurs modèles coexistent, chacun avec un niveau de contrôle et de contraintes différent.

Le BYOD, pour Bring Your Own Device, est le modèle où l'employé utilise son propre terminal personnel à des fins professionnelles. L'entreprise peut installer un profil de gestion dans un container cloisonné, mais ne possède pas l'appareil. Quatre-vingt-deux pourcent des entreprises permettent à leurs employés d'accéder aux ressources professionnelles depuis leurs appareils personnels, mais 38 % d'entre elles ayant adopté le BYOD ont subi une violation de données liée à ces appareils.

Le COPE, pour Corporate-Owned, Personally Enabled, est le compromis le plus répandu dans les grandes entreprises françaises : l'entreprise achète et gère l'appareil, mais autorise l'employé à l'utiliser à titre personnel, réseaux sociaux et applications personnelles compris. La DSI maintient un contrôle total sur la couche professionnelle.

Le COBO, pour Corporate-Owned, Business Only, réserve l'appareil à un usage strictement professionnel, sans aucune application personnelle. Ce modèle est utilisé dans les secteurs très réglementés comme la défense, la banque d'investissement ou la santé, notamment pour se conformer aux exigences de traçabilité des communications. Le CYOD, pour Choose Your Own Device, laisse à l'employé le choix parmi un catalogue d'appareils homologués achetés par l'entreprise. Enfin, le COSU, pour Corporate-Owned, Single Use, désigne des appareils dédiés à un seul usage, verrouillés en mode kiosque, très utilisés dans le retail, la logistique et la santé.

Un élément juridique fondamental : la charte informatique doit être annexée au règlement intérieur pour avoir une valeur contraignante opposable aux salariés. La Cour de cassation a confirmé ce principe en 2010. En contexte BYOD, elle doit préciser la frontière entre sphère professionnelle et sphère personnelle, et l'employeur ne peut accéder aux données personnelles présentes sur l'appareil selon les recommandations de la CNIL.

### Digital Workplace (espace de travail numérique)

La Digital Workplace désigne l'ensemble des outils, plateformes et services numériques mis à disposition des collaborateurs pour travailler, collaborer et communiquer, quel que soit leur lieu ou leur terminal. Le marché mondial était estimé à 35 milliards de dollars en 2023, avec une croissance annuelle de 21 %. Quatre-vingt-cinq pourcent des employés se déclarent plus productifs avec les bons outils numériques.

La Digital Workplace s'articule autour de plusieurs couches. L'UCaaS, pour Unified Communications as a Service, unifie téléphonie, visioconférence, messagerie instantanée et collaboration en temps réel dans le cloud. Microsoft Teams avec ses 300 millions d'utilisateurs actifs mensuels en 2023 est l'exemple le plus emblématique. Le DaaS, pour Desktop as a Service, virtualise le poste de travail complet dans le cloud : l'environnement de travail entier, système d'exploitation, applications et données, est délivré en streaming sur n'importe quel terminal. Azure Virtual Desktop, Amazon WorkSpaces et Citrix DaaS sont les solutions de référence.

Les PWA, ou Progressive Web Apps, sont des applications web qui se comportent comme des applications natives : installation sur l'écran d'accueil, fonctionnement hors ligne et notifications push. Elles permettent de déployer des outils métier accessibles depuis n'importe quel navigateur sans passer par les stores Apple ou Google — un avantage majeur pour la mobilité. L'approche API-first consiste à concevoir toutes les fonctionnalités du SI sous forme d'API documentées avant de construire les interfaces, permettant l'intégration native entre outils comme Teams, le CRM et l'ERP.

Le DEX, pour Digital Employee Experience, est devenu un indicateur stratégique : il mesure la qualité de l'expérience numérique des collaborateurs via des métriques de performance des applications, de disponibilité des outils et de satisfaction. Des plateformes comme Nexthink, Aternity ou 1E mesurent et améliorent le DEX en temps réel. Cinquante-neuf pourcent des DSI considèrent l'amélioration du DEX comme une priorité stratégique pour 2024 et 2025.

Deux risques majeurs à mentionner : la dépendance à Internet, car une panne réseau paralyse tous les outils, et le shadow IT si les outils proposés ne correspondent pas aux besoins réels. Sur la souveraineté, les solutions Microsoft 365 et Google Workspace sont soumises au CLOUD Act américain, qui permet aux autorités américaines d'accéder aux données hébergées par des entreprises américaines, même en Europe. Des alternatives souveraines existent comme Citadel Team de Thales ou Oodrive.

### Télétravail et travail hybride

Le télétravail est défini par l'article L1222-9 du Code du travail comme toute forme de travail effectuée hors des locaux de l'employeur avec les technologies de l'information et de la communication, de manière volontaire. Quarante-sept pourcent des salariés français pratiquaient le télétravail de manière régulière en 2023, et 54 % des cadres refuseraient un poste sans possibilité de télétravail selon l'APEC. Les télétravailleurs déclarent un gain de productivité moyen de 22 % selon une étude de l'université Stanford.

Le cadre légal repose sur plusieurs textes. L'ordonnance Macron de 2017 a introduit la flexibilité du télétravail, et l'ANI, l'Accord National Interprofessionnel du 26 novembre 2020, est l'accord de référence négocié par les partenaires sociaux. Il encadre l'organisation du télétravail, le droit à la déconnexion, la lutte contre l'isolement et la prise en charge des frais professionnels. Le droit à la déconnexion, introduit par la loi El Khomri du 8 août 2016 à l'article L2242-17, oblige les entreprises de plus de 50 salariés à négocier les modalités permettant aux salariés de ne pas être sollicités hors du temps de travail.

Les formes d'organisation se déclinent en hybride structuré, avec des jours de présence et de télétravail définis à l'avance, hybride flexible où l'employé choisit librement ses jours, full remote sans ancrage géographique obligatoire, et nomadisme numérique depuis différents pays. Le flex office est l'organisation dans laquelle les collaborateurs n'ont plus de bureau attitré et réservent un espace à la demande, permettant aux entreprises de réduire leur surface de bureaux avec des ratios de 0,7 à 0,8 bureau par employé. Le flex office a réduit les surfaces de bureaux de 30 % en moyenne dans les grandes entreprises françaises.

Du point de vue de la DSI, le télétravail impose de sécuriser les accès distants, via VPN ou ZTNA, de fournir les outils adaptés, et de gérer les risques cybersécurité liés à l'utilisation de réseaux WiFi non sécurisés et d'appareils personnels.

### VPN et accès distant — vers le ZTNA

Un VPN, pour Virtual Private Network, est un tunnel chiffré établi entre un terminal distant et le réseau de l'entreprise, permettant à un utilisateur de se connecter aux ressources internes comme s'il était physiquement présent. Le tunnel utilise des protocoles de chiffrement comme IPSec, SSL/TLS, OpenVPN ou WireGuard. Le principe est simple : le client s'authentifie, le tunnel est établi, tout le trafic est chiffré et le client obtient une adresse IP sur le réseau interne.

Cependant, les VPN sont devenus un vecteur d'attaque majeur. Ils sont responsables de 40 % des vecteurs d'attaque initiaux dans les incidents de ransomware selon Mandiant en 2023. Des vulnérabilités critiques sur les concentrateurs VPN de Citrix, Ivanti et Fortinet ont été massivement exploitées entre 2020 et 2024. La raison est structurelle : un concentrateur VPN est exposé directement sur Internet, souvent difficile à patcher rapidement pour des raisons opérationnelles, et son exploitation donne un accès direct au réseau interne.

Le ZTNA, pour Zero Trust Network Access, est la réponse moderne à ces failles. Fondé sur le principe de ne jamais faire confiance et de toujours vérifier, le ZTNA accorde un accès granulaire à des applications spécifiques, et non au réseau entier, après vérification continue de l'identité de l'utilisateur, de la conformité du terminal et du contexte comme la géolocalisation, l'heure et le comportement. Les serveurs internes ne sont jamais exposés directement sur Internet. Les prestataires cloud comme Zscaler Private Access, Cloudflare Access et Palo Alto Prisma Access portent ces solutions. Soixante-douze pourcent des entreprises prévoient de déployer ou d'étendre le ZTNA d'ici 2025.

Le split tunneling mérite d'être mentionné : il permet de n'envoyer par le VPN que le trafic destiné aux ressources internes, le reste allant directement sur Internet. Avantage : meilleures performances et moins de charge sur le concentrateur. Risque : le trafic Internet de l'utilisateur échappe au filtrage de l'entreprise.

Le ZTNA est l'un des composants clés du SASE, le Secure Access Service Edge, une architecture réseau et sécurité cloud qui intègre SD-WAN, ZTNA, CASB et SWG dans une solution unifiée.

### Low-code et No-code

Le low-code est une approche de développement logiciel qui minimise la quantité de code manuel en utilisant des interfaces visuelles, du drag-and-drop et des composants préconstruits. Le no-code va plus loin : il permet à des utilisateurs sans compétence technique de créer des applications complètes sans écrire une seule ligne de code.

Ces approches répondent à une double pression : la pénurie de développeurs, estimée à 85 millions de professionnels manquants d'ici 2030, et l'accélération des besoins métier. Gartner estime que 70 % des applications créées par des entreprises seront développées avec des outils low-code ou no-code d'ici 2025. Le marché mondial devrait atteindre 187 milliards de dollars en 2030.

Le concept de citizen developer est fondamental : il désigne un employé non-développeur, un commercial, un responsable RH ou un opérationnel, qui crée des applications pour son équipe grâce aux outils low-code ou no-code, avec l'approbation et l'encadrement de la DSI.

La Power Platform de Microsoft est la suite de référence dans l'écosystème Microsoft 365 : Power Apps pour la création d'applications mobiles et web, Power Automate pour l'automatisation de workflows, Power BI pour la Business Intelligence et Power Pages pour les portails web. Elle compte plus de 33 millions d'utilisateurs actifs mensuels. Mendix, racheté par Siemens en 2018, est le leader pour les applications métier complexes dans l'industrie et la finance. OutSystems est positionné sur les applications critiques d'entreprise, et Bubble sur les startups qui veulent valider un MVP rapidement sans développeur.

Les risques pour la DSI sont réels : shadow IT si les applications sont créées sans validation IT, dette technique si elles ne sont pas maintenues, vendor lock-in fort, problèmes de sécurité si les données sensibles sont mal protégées, et absence de tests et de documentation.

### RPA — Robotic Process Automation (Automatisation robotisée des processus)

La RPA est une technologie qui permet de créer des robots logiciels capables de reproduire les actions qu'un humain effectuerait sur un ordinateur : clics, saisies, extractions de données, copier-coller entre applications, envoi d'e-mails. Les robots RPA opèrent sur la couche de présentation des applications existantes, sans modifier le code source.

Un robot RPA observe et enregistre les actions d'un humain, les rejoue de manière automatique, prend des décisions simples basées sur des règles prédéfinies et consigne ses actions dans des journaux d'audit. Il existe deux types principaux : l'attended bot, déclenché manuellement par un utilisateur qui reste dans la boucle, et l'unattended bot, déclenché automatiquement par un scheduler ou un événement, fonctionnant en arrière-plan sans intervention humaine.

L'avantage stratégique de la RPA pour les systèmes legacy est majeur : elle interagit avec l'interface graphique des applications sans nécessiter d'API ni d'accès aux bases de données, ce qui la rend déployable rapidement sur des ERP anciens ou des applications mainframe. Un robot RPA traite en moyenne 15 à 20 fois plus vite qu'un humain des tâches répétitives, avec un ROI généralement inférieur à 12 mois.

Le process mining, avec des outils comme Celonis, analyse les journaux d'événements du SI pour identifier les processus automatisables. Il est souvent la première étape avant un projet RPA. L'hyperautomation est le concept formalisé par Gartner qui combine RPA, IA avec reconnaissance optique de caractères et traitement du langage naturel, et BPM pour automatiser des processus de bout en bout incluant des tâches non structurées. Les leaders du marché sont UiPath, Automation Anywhere et Blue Prism, auxquels s'ajoute Microsoft Power Automate Desktop intégré à M365.

Les risques à surveiller : la fragilité face aux changements d'interface, car une mise à jour applicative peut casser un robot, la maintenance chronophage et le bot sprawl, la prolifération incontrôlée de robots difficiles à gouverner.

### Edge Computing (calcul en périphérie)

L'edge computing est un paradigme d'architecture dans lequel le traitement des données s'effectue au plus près de la source, capteurs, appareils IoT et terminaux mobiles, plutôt que d'envoyer toutes les données vers un datacenter central ou le cloud. Le marché mondial était estimé à 61 milliards de dollars en 2023, avec une croissance de 37 % par an.

La raison d'être de l'edge computing est la latence. Un datacenter centralisé introduit une latence de 50 à 150 millisecondes. Un edge régional descend à 5 à 20 millisecondes. Un edge on-premises tombe sous les 5 millisecondes. Pour les usages temps réel comme la chirurgie robotique ou les véhicules autonomes, les exigences sont inférieures à 1 milliseconde. Or un véhicule autonome génère entre 4 et 8 téraoctets de données par jour, un volume impossible à envoyer intégralement dans le cloud en temps réel. Gartner estime que 75 % des données d'entreprise seront créées et traitées à l'extérieur des datacenters traditionnels d'ici 2025.

L'architecture edge computing se représente en trois couches : les devices et capteurs IoT à la périphérie, la couche edge ou périphérie avec ses passerelles de traitement local, et le cloud central pour le stockage long terme et les analyses globales. Le fog computing, concept introduit par Cisco, désigne une variante qui utilise des nœuds de calcul intégrés à l'infrastructure réseau existante comme les routeurs et les switchs.

La 5G est un catalyseur majeur de l'edge computing grâce à sa latence ultra-faible et à l'architecture MEC, pour Multi-access Edge Computing, qui place des serveurs de calcul au niveau des antennes 5G. Les opérateurs télécom deviennent ainsi des fournisseurs de capacité edge. Les acteurs majeurs sont AWS avec Greengrass, Microsoft Azure avec Azure IoT Edge, NVIDIA avec ses puces Jetson pour l'edge AI, et les opérateurs télécom avec leurs offres MEC 5G.

Les défis pour la DSI : gestion distribuée complexe de milliers de nœuds edge à surveiller et mettre à jour, sécurité difficile sur des équipements dispersés et physiquement accessibles, hétérogénéité des équipements et coût d'infrastructure physique.

---

## Questions que le jury pourrait poser

- BYOD versus COPE : quel modèle choisir pour une PME et quels risques ?
- Comment sécuriser les accès distants dans un contexte de télétravail généralisé ?
- Quels impacts du télétravail sur l'architecture du SI ?
- MDM, EMM, UEM : quelle évolution et pourquoi ?
- Comment la Digital Workplace améliore-t-elle la productivité des collaborateurs ?
- VPN traditionnel versus ZTNA : pourquoi migrer ?
- Le low-code et le no-code sont-ils un risque ou une opportunité pour la DSI ?
- Comment l'Edge Computing répond-il aux enjeux de latence et de mobilité ?
- Droit à la déconnexion : quelles obligations pour l'entreprise ?

---

## Points de vigilance

Premier point de vigilance : confondre MDM, EMM et UEM. Le MDM gère les appareils mobiles, l'EMM étend à la gestion des applications et des contenus, et l'UEM unifie tous les types de terminaux dans une seule console. Ce sont des étapes successives d'une évolution, pas des synonymes.

Deuxième point de vigilance : sous-estimer les risques juridiques du BYOD. La DSI ne peut pas contrôler l'appareil personnel d'un collaborateur comme s'il s'agissait d'un appareil d'entreprise. La CNIL est explicite : l'employeur ne peut accéder aux données personnelles présentes sur l'appareil. La charte informatique doit être annexée au règlement intérieur, sinon elle n'a aucune valeur contraignante.

Troisième point de vigilance : présenter le VPN comme une solution de sécurité suffisante. Les concentrateurs VPN sont aujourd'hui l'un des vecteurs d'attaque les plus exploités par les ransomwares. La migration vers le ZTNA est une priorité de modernisation, avec l'objectif de ne jamais exposer le réseau interne directement.

Quatrième point de vigilance : ignorer la gouvernance du low-code et du no-code. Le risque n'est pas la technologie elle-même mais le shadow IT qu'elle génère quand elle n'est pas encadrée. La DSI doit définir une gouvernance claire : quels outils sont autorisés, qui peut créer des applications, avec quelles contraintes de sécurité et de documentation.

Cinquième point de vigilance : opposer edge computing et cloud computing. Ce sont des architectures complémentaires, pas concurrentes. Le bon réflexe est de savoir ce qui doit être traité en edge, les données critiques en temps réel et les données volumineuses sans pertinence globale, et ce qui doit remonter au cloud, les données historiques pour l'analyse, l'entraînement des modèles IA et le pilotage global.
