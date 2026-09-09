# SI et environnement — Guide de révision complet

## Introduction

Le thème "Systèmes d'Information et environnement" est aujourd'hui au cœur des préoccupations des directions informatiques. Le numérique représente environ quatre pour cent des émissions mondiales de gaz à effet de serre, autant que l'aviation civile mondiale, et cette part est en croissance rapide. Pour un manager ou un architecte logiciel, maîtriser ces enjeux est devenu incontournable : les réglementations se multiplient (loi REEN, directive CSRD, décret tertiaire), les directions générales attendent des démarches structurées et mesurables, et la réputation des organisations en dépend. Ce thème couvre à la fois les indicateurs techniques de performance environnementale, les bonnes pratiques d'infrastructure et de développement, le cadre réglementaire applicable, et les acteurs de référence de l'écosystème du numérique responsable en France.

---

## Notions clés à maîtriser

### Indicateurs environnementaux du Système d'Information

Les indicateurs environnementaux du Système d'Information sont des métriques standardisées qui permettent de mesurer et de piloter l'impact écologique d'une infrastructure informatique. Ils constituent la base de toute démarche Green IT sérieuse : on ne peut réduire que ce que l'on mesure.

Le premier et le plus connu est le PUE, le Power Usage Effectiveness. Il se calcule en divisant l'énergie totale consommée par un datacenter par l'énergie effectivement utilisée par les équipements informatiques. Un PUE de un virgule zéro est la perfection théorique : toute l'énergie va aux serveurs. Un PUE de deux virgule zéro signifie que la moitié de l'énergie est perdue en refroidissement et alimentation électrique. Les hyperscalers comme Google, Microsoft ou Amazon Web Services affichent des PUE entre un virgule un et un virgule deux, grâce à des investissements massifs en efficacité. Le PUE moyen mondial était encore de un virgule cinquante-huit en 2023 selon l'Uptime Institute. La loi REEN impose aux datacenters de plus de cinq cents kilowatts de publier leur PUE.

Le CUE, Carbon Usage Effectiveness, mesure les émissions de CO2 liées au fonctionnement du datacenter rapportées à la puissance informatique. Un CUE de zéro indique une alimentation cent pour cent renouvelable.

Le WUE, Water Usage Effectiveness, mesure la consommation d'eau pour le refroidissement. Il est particulièrement critique dans les zones de stress hydrique où l'eau est une ressource rare.

L'ERE, Energy Reuse Effectiveness, mesure la part de chaleur fatale récupérée et réutilisée, par exemple pour le chauffage urbain. Un ERE inférieur à un signifie qu'on valorise effectivement la chaleur produite par les serveurs.

Ces quatre indicateurs sont définis par la série de normes ISO/IEC 30134. Ils permettent de comparer des datacenters entre eux et de suivre les progrès dans le temps.

Pour le bilan carbone du Système d'Information, la référence internationale est le GHG Protocol, le Greenhouse Gas Protocol. Il distingue trois périmètres. Le Scope un correspond aux émissions directes sur site, comme les groupes électrogènes au fioul. Le Scope deux couvre les émissions indirectes liées à l'électricité achetée, qui dépendent du mix énergétique national. Le Scope trois regroupe toutes les autres émissions indirectes : fabrication des serveurs, transport, déplacements, fin de vie des équipements. Ce Scope trois représente souvent soixante-dix à quatre-vingt pour cent du bilan carbone numérique d'une organisation. C'est le plus difficile à mesurer, mais aussi le plus important pour identifier les vrais leviers de réduction.

---

### Analyse du Cycle de Vie — ACV

L'Analyse du Cycle de Vie, ou ACV, est une méthode normalisée par les normes ISO 14040 et ISO 14044 qui évalue l'ensemble des impacts environnementaux d'un produit ou service depuis l'extraction des matières premières jusqu'à sa fin de vie. Appliquée au numérique, elle révèle une réalité souvent ignorée : la fabrication des équipements domine le bilan environnemental.

La fabrication d'un smartphone représente soixante-dix-huit pour cent de son empreinte carbone totale sur l'ensemble de sa vie. Pour un ordinateur portable, ce chiffre monte à soixante-douze pour cent. Les phases de transport, d'utilisation et de fin de vie pèsent beaucoup moins.

Cette réalité change profondément les priorités managériales. Renouveler son parc informatique tous les trois ans pour bénéficier de matériel plus efficace énergétiquement est souvent contre-productif. Amortir l'impact carbone de la fabrication sur cinq ans au lieu de trois ans réduit l'empreinte de quarante pour cent.

L'ACV comprend quatre phases. D'abord, la définition des objectifs et du périmètre. Ensuite, l'inventaire du cycle de vie, qui consiste à collecter toutes les données d'entrées et de sorties. Puis l'évaluation des impacts, traduits en indicateurs comme le réchauffement climatique ou l'épuisement des ressources. Enfin, l'interprétation, qui identifie les points chauds et formule des recommandations.

Pour les services cloud, l'outil open source Cloud Carbon Footprint, initié par ThoughtWorks, permet d'estimer les émissions de CO2 des ressources utilisées sur AWS, Google Cloud Platform et Azure. Il croise la consommation électrique estimée avec l'intensité carbone du mix électrique de la région hébergeant les ressources. Ses résultats restent des estimations car les hyperscalers ne publient pas toutes les données nécessaires.

---

### Technologies de stockage

Le stockage est le poste de consommation électrique qui croît le plus rapidement dans les datacenters. Le volume mondial de données devrait atteindre cent vingt zettaoctets, et le stockage représente quinze à vingt-cinq pour cent de la consommation électrique d'un datacenter.

Il existe une hiérarchie des supports selon leur performance et leur consommation. Les SSD NVMe (Solid State Drive avec interface PCIe) offrent des performances très élevées pour les données critiques, avec une consommation de trois à dix watts. Les disques durs HDD (Hard Disk Drive) à plateaux magnétiques sont adaptés aux données tièdes, avec cinq à douze watts. Les bandes magnétiques LTO (Linear Tape Open) représentent la solution la plus sobre pour l'archivage : leur consommation est quasi nulle en veille, inférieure à un demi-watt.

L'approche Green Storage consiste à réduire l'empreinte énergétique du stockage par plusieurs techniques. Le tiering automatique déplace les données vers le support le moins énergivore adapté à leur fréquence d'accès. La déduplication supprime les blocs de données identiques et peut réduire le volume de cinquante à quatre-vingt-quinze pour cent selon le type de données. La compression réduit la taille des données. Le thin provisioning alloue dynamiquement l'espace réel, évitant le gaspillage de capacité pré-allouée.

Le stockage objet, dont Amazon S3 est le standard de référence, stocke les données sous forme d'objets avec des métadonnées, sans hiérarchie de répertoires. Il est compatible avec des densités de stockage élevées sur disques durs économiques.

L'erasure coding est une alternative à la réplication triple, qui impose deux cents pour cent de surcoût de stockage. L'erasure coding réduit cet overhead à environ cinquante pour cent, économisant ainsi de l'espace disque et de l'énergie de manière significative. Ce procédé est massivement utilisé par Meta pour stocker ses photos et vidéos archivées.

Un chiffre clé à retenir : quatre-vingt-dix pour cent des données d'une entreprise ne sont jamais réutilisées après quatre-vingt-dix jours de création. Le dark data, ces données stockées mais inutilisées, représenterait cinquante-cinq pour cent du volume total stocké en entreprise.

---

### Data Lifecycle Management

Le Data Lifecycle Management, ou gestion du cycle de vie des données, désigne l'ensemble des politiques, processus et technologies permettant de gérer les données de leur création jusqu'à leur destruction définitive. C'est le levier le plus opérationnel pour réduire l'empreinte du stockage.

Sans politique de gestion du cycle de vie des données, les entreprises accumulent du dark data. Ces données collectées et stockées ne sont jamais consultées, mais elles consomment de l'énergie sur des supports actifs et représentent un risque légal au regard du Règlement Général sur la Protection des Données. Supprimer un téraoctet de dark data peut éviter l'émission d'environ une virgule cinq tonne de CO2 équivalent sur trois ans.

La classification par température est le premier outil du Data Lifecycle Management. Le hot data désigne les données actives, accédées quotidiennement, hébergées sur SSD. Le warm data couvre les données récentes peu consultées, sur disques durs. Le cold data regroupe les données rarement accédées, archivées sur bandes LTO ou stockage objet froid. Le frozen data correspond aux archives à conservation légale, sur LTO robotique ou S3 Glacier Deep Archive.

Il faut distinguer la sauvegarde de l'archivage. La sauvegarde protège des données actives contre les sinistres et permet une restauration rapide. L'archivage déplace des données inactives vers un stockage moins coûteux et moins énergivore pour conservation long terme. Ce sont deux processus différents avec des objectifs et des supports distincts.

Les obligations légales de rétention sont précises. Les documents comptables doivent être conservés dix ans en France. Les contrats commerciaux et les données de paie, cinq ans. Les données personnelles, selon le Règlement Général sur la Protection des Données, uniquement le temps nécessaire à la finalité pour laquelle elles ont été collectées.

---

### Refroidissement des datacenters

Le refroidissement représente trente à quarante pour cent de la consommation d'un datacenter traditionnel, ce qui en fait le principal levier d'amélioration du PUE après l'efficacité des équipements informatiques eux-mêmes.

La première technique, la plus simple et la plus accessible, est l'organisation hot aisle et cold aisle, les allées chaudes et froides. Les baies serveurs sont disposées en alternance : les serveurs aspirent l'air froid en façade depuis l'allée froide et rejettent l'air chaud en arrière vers l'allée chaude. Des panneaux de confinement isolent les deux flux. Ce simple principe peut réduire la consommation de refroidissement de quinze à trente pour cent.

Le free cooling, ou refroidissement par l'air extérieur, consiste à utiliser directement l'air froid naturel pour refroidir les équipements, sans groupe froid mécanique. Il est opérationnel quand la température extérieure est inférieure à dix-huit à vingt-deux degrés Celsius. En France, ce seuil est atteint environ soixante-dix à quatre-vingts pour cent de l'année. En Scandinavie ou en Islande, c'est plus de quatre-vingt-quinze pour cent de l'année, ce qui explique pourquoi de nombreux hyperscalers y installent leurs datacenters, atteignant des PUE proches de un virgule un.

Le refroidissement liquide, ou liquid cooling, est devenu incontournable avec l'essor de l'intelligence artificielle. La densité moyenne des baies est passée de cinq à sept kilowatts en 2015 à quinze à vingt kilowatts en 2023, et les serveurs IA peuvent dépasser cinquante kilowatts par baie, ce que le refroidissement par air ne peut plus traiter. Le Direct Liquid Cooling utilise des plaques métalliques traversées par de l'eau posées directement sur les processeurs et cartes graphiques.

L'immersion cooling représente l'avenir du refroidissement haute densité. Les serveurs sont plongés entièrement dans un liquide diélectrique non conducteur. La version two-phase, où le liquide s'évapore au contact des composants chauds et se condense naturellement en partie haute, peut atteindre un PUE de un virgule zéro deux à un virgule zéro cinq, très proche de la perfection.

La récupération de chaleur fatale transforme ce déchet thermique en ressource. La chaleur produite par les serveurs, entre quarante et soixante degrés Celsius, peut alimenter des réseaux de chaleur urbains. À Stockholm, plusieurs datacenters chauffent des milliers de logements grâce à cette valorisation. En France, Qarnot Computing a inventé la chaudière numérique : des radiateurs contenant des processeurs effectuent des calculs pour des clients professionnels, et la chaleur produite chauffe gratuitement le logement.

---

### Infrastructure des datacenters

L'infrastructure d'un datacenter regroupe l'ensemble des équipements physiques assurant l'alimentation électrique, la connectivité et la supervision des ressources de calcul. L'optimisation de cette infrastructure est le levier le plus direct pour réduire la consommation électrique du Système d'Information.

La virtualisation des serveurs est le premier levier historique. Sans virtualisation, le taux d'utilisation moyen d'un serveur physique est de cinq à quinze pour cent : la machine consomme presque autant à vide qu'en charge. En hébergeant plusieurs machines virtuelles sur un seul serveur physique, on peut atteindre un taux d'utilisation de soixante-dix à quatre-vingts pour cent. Le rapport de consolidation va de cinq pour un à vingt pour un selon les charges de travail. VMware vSphere, Microsoft Hyper-V et KVM sont les hyperviseurs de référence. Des fonctionnalités comme le vMotion chez VMware permettent de déplacer une machine virtuelle en cours d'exécution d'un serveur physique à un autre sans interruption, pour optimiser la charge et éteindre les serveurs sous-utilisés.

Un problème spécifique mérite attention : les serveurs zombies. Ce sont des serveurs physiques allumés et alimentés mais sans charge utile réelle. Ils consomment deux cents à cinq cents watts inutilement et représenteraient vingt à trente pour cent du parc dans certaines organisations.

Le DCIM, Data Center Infrastructure Management, est le logiciel de supervision centralisée du datacenter. Il surveille en temps réel la puissance consommée par baie, la température par zone, l'état des onduleurs, et calcule automatiquement le PUE. Des alertes sont générées avant qu'une baie ne dépasse sa capacité électrique ou thermique. C'est l'outil indispensable pour piloter et prouver les progrès d'une démarche Green IT.

Les onduleurs, ou UPS (Uninterruptible Power Supply), sont une source de pertes souvent négligée. Un onduleur fonctionnant à vingt-cinq pour cent de sa capacité a un rendement de seulement quatre-vingt-cinq pour cent. À quatre-vingt pour cent de sa capacité, il atteint quatre-vingt-quinze à quatre-vingt-dix-sept pour cent. Le surdimensionnement des onduleurs génère donc des pertes importantes et inutiles. La certification 80 PLUS Titanium pour les alimentations de serveurs garantit un rendement d'au moins quatre-vingt-seize pour cent à mi-charge.

---

### Projets innovants de datacenters

Face aux contraintes énergétiques et environnementales, des projets innovants réinventent le concept même de datacenter.

Le Projet Natick de Microsoft a consisté à déployer un module de datacenter hermétique au fond de la mer. La Phase 2, déployée en 2018 au large des Orcades en Écosse, a placé huit cent soixante-quatre serveurs dans un cylindre de douze mètres de long à trente-cinq mètres de profondeur. Le refroidissement était assuré par l'eau de mer. L'atmosphère intérieure était composée d'azote pour éviter l'oxydation. Les résultats publiés en 2020 ont été surprenants : un taux de panne huit fois inférieur à celui des datacenters terrestres, probablement grâce à l'atmosphère stable sans humidité ni chocs thermiques liés aux interventions humaines. Le projet n'a pas été industrialisé, mais il a démontré la faisabilité du concept.

Qarnot Computing a développé une approche radicalement différente avec la chaudière numérique. L'idée est de distribuer le calcul là où la chaleur est utile, dans les logements et bureaux. Des radiateurs contenant des processeurs, appelés Q.rad, effectuent des calculs pour des clients professionnels comme Société Générale pour le calcul de risques financiers ou des studios d'animation pour le rendu tridimensionnel. La chaleur produite chauffe le logement gratuitement. L'hébergeur ne paie pas l'électricité. Le rendement thermique est quasi cent pour cent : toute l'énergie électrique est convertie en chaleur valorisée localement.

Le green mining explore l'utilisation des surplus d'énergies renouvelables pour le minage de cryptomonnaies. Dans les régions où les barrages hydrauliques produisent plus d'électricité que le réseau n'en absorbe, les fermes de minage absorbent cet excédent à coût quasi nul. Cette approche évite le curtailment, c'est-à-dire le gaspillage d'énergie renouvelable produite en excès. Il faut cependant noter qu'Ethereum a migré vers une méthode de validation appelée Proof of Stake en septembre 2022, réduisant sa consommation de quatre-vingt-dix-neuf virgule quatre-vingt-quinze pour cent par rapport au minage traditionnel.

---

### VDI et client léger

La VDI, Virtual Desktop Infrastructure, est une architecture qui héberge les postes de travail des utilisateurs sous forme de machines virtuelles sur des serveurs centralisés. L'utilisateur accède à son bureau via un client léger, un terminal bas de gamme qui n'exécute aucun calcul local.

L'impact énergétique est considérable. Un client léger consomme entre cinq et quinze watts, contre soixante-cinq à cent cinquante watts pour un PC de bureau classique. La réduction de la consommation du parc utilisateur peut atteindre soixante-dix à quatre-vingt-dix pour cent. La durée de vie d'un client léger est de sept à dix ans, contre trois à cinq ans pour un PC, car il ne comporte pas de pièces mobiles et ne souffre pas de l'obsolescence logicielle locale.

L'architecture VDI repose sur un hyperviseur qui héberge les machines virtuelles de bureau, un broker de connexion qui route l'utilisateur vers sa session, et un protocole d'affichage qui transmet l'écran compressé au client. VMware utilise le protocole Blast Extreme, Citrix utilise HDX, Microsoft Remote Desktop Services utilise RDP.

Il existe deux types principaux de VDI. La VDI persistante donne à chaque utilisateur sa propre machine virtuelle dédiée, avec ses personnalisations conservées. La VDI non persistante utilise un pool de machines virtuelles partagées, remises à zéro à chaque session, idéale pour les postes standardisés comme les centres d'appels.

Le DaaS, Desktop as a Service, est la version cloud de la VDI, proposée par Amazon WorkSpaces, Microsoft Azure Virtual Desktop ou Citrix DaaS. Elle supprime l'investissement initial en infrastructure et offre de l'élasticité.

Pour les achats, deux certifications sont à connaître. Energy Star, programme américain de l'EPA (Environmental Protection Agency), certifie uniquement la consommation électrique en usage. TCO Certified, certification suédoise, adopte une approche cycle de vie complet couvrant la fabrication, l'usage, la fin de vie et les conditions sociales de production.

---

### Sobriété numérique

La sobriété numérique consiste à réduire volontairement l'empreinte environnementale du numérique en limitant les usages superflus et en optimisant les ressources. Elle se distingue de l'efficacité énergétique en questionnant l'utilité même des usages, pas seulement leur performance.

La distinction entre Green IT 1.0 et Green IT 2.0 est fondamentale. Le Green IT 1.0 correspond à l'optimisation de l'infrastructure numérique : réduire le PUE des datacenters, améliorer l'efficacité des serveurs. C'est une approche purement technique portant sur l'infrastructure existante. Le Green IT 2.0, aussi appelé Numérique Responsable, étend la démarche à l'ensemble du cycle de vie : allongement de la durée de vie des terminaux, écoconception des services numériques, achats responsables, sensibilisation des utilisateurs.

Une notion critique est l'effet rebond, aussi connu sous le nom de paradoxe de Jevons. L'amélioration de l'efficacité d'une technologie entraîne une augmentation de son utilisation, annulant partiellement ou totalement le gain environnemental. Des smartphones plus efficaces énergétiquement se vendent en plus grand nombre et se renouvellent plus fréquemment. La consommation électrique des datacenters mondiaux stagne grâce aux gains d'efficacité, mais les usages explosent avec l'intelligence artificielle, le streaming et le big data. L'intelligence artificielle générative multiplie par dix à cent la consommation énergétique par requête par rapport à une recherche Google classique.

L'IT for Green est une approche complémentaire : utiliser le numérique comme levier de décarbonation des autres secteurs, via les smart grids, l'agriculture de précision, l'optimisation logistique. L'effet net reste cependant débattu car le numérique consomme également des ressources pour fonctionner.

Le GreenOps est la pratique issue du croisement DevOps et FinOps avec les enjeux environnementaux. Il consiste à mesurer et réduire l'empreinte carbone des charges de travail cloud en temps réel, en choisissant des régions cloud à mix énergétique favorable et en planifiant les traitements par lot sur des plages à énergie renouvelable, une approche qu'on appelle le carbon-aware computing.

Un chiffre choc : seulement quatorze pour cent des entreprises françaises mesurent l'empreinte de leur Système d'Information (Cigref/Wavestone 2023).

---

### Écoconception logicielle

L'écoconception logicielle consiste à intégrer les critères environnementaux dès la conception d'un service numérique pour minimiser son empreinte tout au long de son cycle de vie. Elle agit sur la consommation de ressources matérielles — processeur, mémoire vive, réseau, stockage — et prolonge la compatibilité avec des équipements anciens.

Un logiciel lourd accélère l'obsolescence des terminaux, qui représentent le principal poste d'impact du numérique. Maintenir la compatibilité avec des équipements de cinq à sept ans évite de forcer le renouvellement matériel.

Les principes fondamentaux de l'écoconception logicielle s'appliquent à chaque couche du service. Côté réseau, il faut réduire le poids des pages, optimiser les requêtes et limiter les appels superflus. Les images représentent en moyenne cinquante à soixante pour cent du poids des pages web. Côté serveur, il faut optimiser les algorithmes et éviter le sur-provisionnement. Côté client, il faut limiter le JavaScript exécuté dans le navigateur. Côté fonctionnel, il faut supprimer les fonctionnalités inutiles et éviter les vidéos en lecture automatique.

Le RGESN, Référentiel Général d'Écoconception de Services Numériques, est le référentiel officiel publié par la Direction Interministérielle du Numérique et le Ministère de la Transition Écologique. Sa version 2024 comporte soixante-dix-neuf critères répartis en neuf thématiques. Il est obligatoire pour les services numériques publics et de plus en plus utilisé dans le secteur privé.

Le GR491, Guide de Référence de Conception Responsable de Services Numériques, publié par l'Institut du Numérique Responsable, liste quatre cent quatre-vingt-onze bonnes pratiques organisées par cycle de vie et par rôle. Il est plus exhaustif que le RGESN et sert de base aux audits approfondis.

L'EcoIndex est l'outil de mesure de référence pour les sites web. Il score une page de A (meilleur) à G en fonction du poids de la page, du nombre de requêtes HTTP et de la complexité du DOM, le nombre d'éléments HTML de la page. Un site web moyen émet environ zéro virgule cinq gramme de CO2 par page vue, contre plus de cinq grammes pour les sites les moins bien optimisés.

---

### Économie circulaire du numérique

L'économie circulaire appliquée au numérique vise à maintenir les équipements et matériaux à leur niveau de valeur le plus élevé le plus longtemps possible, en opposition au modèle linéaire fabriquer, utiliser, jeter.

La hiérarchie des actions, par ordre de priorité environnementale décroissante, est la suivante : refuser ce qui n'est pas utile, réduire le parc, réutiliser en interne, reconditionner pour un second cycle de vie, et enfin recycler via des filières agréées.

Le reconditionnement consiste à remettre à neuf un équipement d'occasion. Un ordinateur portable reconditionné émet quatre-vingts à quatre-vingt-dix pour cent de moins de CO2 à la fabrication qu'un neuf, car la fabrication représente la majorité de l'impact carbone sur le cycle de vie. Le marché du reconditionné croît de dix à quinze pour cent par an.

La loi AGEC, Anti-Gaspillage pour une Économie Circulaire de 2020, est la loi structurante en France. Elle impose l'affichage de l'indice de réparabilité sur les équipements électroniques, note de zéro à dix la facilité à réparer un produit. Elle interdit la destruction des invendus électroniques. Elle impose aux acheteurs publics d'acheter au moins vingt pour cent de matériels reconditionnés sur certaines catégories. Elle renforce également la filière des DEEE, les Déchets d'Équipements Électriques et Électroniques.

En France, les éco-organismes agréés pour la collecte et le traitement des DEEE professionnels sont Ecologic, Ecosystem, E-Déchets et Recyclia. Seuls quarante pour cent des DEEE ménagers sont collectés dans les filières agréées aujourd'hui, ce qui montre l'ampleur des progrès à faire.

---

### Outils de mesure d'impact environnemental

On ne peut optimiser que ce que l'on mesure. Les outils de mesure d'impact environnemental constituent le prérequis indispensable à toute démarche d'écoconception ou de sobriété numérique.

Pour les sites et applications web, l'EcoIndex est l'outil open source de référence, gratuit, développé par le Collectif Numérique Responsable. GreenIT-Analysis est son extension navigateur, qui analyse une page en temps réel lors de la navigation. Greenspector est une solution commerciale qui mesure la consommation réelle sur des terminaux mobiles physiques, particulièrement adaptée aux applications mobiles.

Pour les infrastructures serveur, Scaphandre est un agent open source (développé par Hubblo) qui mesure la consommation électrique par processus sur des serveurs Linux et exporte les données vers Prometheus et Grafana. Kepler, un projet de la Cloud Native Computing Foundation, fait de même pour les charges de travail Kubernetes.

Pour les environnements cloud, tous les grands hyperscalers proposent des outils natifs : AWS Customer Carbon Footprint Tool, Azure Emissions Insights, Google Cloud Carbon Footprint. L'outil open source Cloud Carbon Footprint permet une analyse multi-cloud. Boavizta et son Cloud-scanner mesurent l'empreinte en intégrant à la fois la fabrication et l'usage des équipements.

Le DCIM, Data Center Infrastructure Management, reste la référence pour le pilotage des datacenters physiques avec le calcul du PUE en temps réel. Les éditeurs de référence sont Schneider Electric EcoStruxure IT, Vertiv Trellis et Sunbird DCIM.

---

### Cadre réglementaire environnemental du Système d'Information

Le paysage réglementaire se densifie rapidement et les DSI ne peuvent plus traiter la question environnementale comme un sujet facultatif.

La loi REEN, pour Réduction de l'Empreinte Environnementale du Numérique, adoptée en novembre 2021, est la première loi française entièrement dédiée à l'impact numérique. Elle impose aux communes de plus de cinquante mille habitants d'adopter une stratégie numérique responsable avant 2025. Elle oblige les datacenters de plus de cinq cents kilowatts à obtenir un label de performance environnementale. Elle a créé l'Observatoire des impacts environnementaux du numérique auprès de l'ARCEP.

La directive CSRD, Corporate Sustainability Reporting Directive, adoptée par l'Union Européenne en 2022, est l'obligation de reporting extra-financier la plus ambitieuse de l'histoire. Elle s'applique progressivement entre 2024 et 2026 à plus de cinquante mille entreprises européennes, contre onze mille pour la précédente directive. Les entreprises doivent publier selon les normes ESRS leur impact environnemental, social et de gouvernance. L'empreinte du Système d'Information est couverte par l'ESRS E1 pour le changement climatique, l'ESRS E3 pour l'eau et l'ESRS E5 pour l'économie circulaire. Un audit par un commissaire aux comptes est obligatoire.

Le décret tertiaire de 2019 impose aux bâtiments tertiaires de plus de mille mètres carrés une réduction de la consommation énergétique de quarante pour cent en 2030, cinquante pour cent en 2040 et soixante pour cent en 2050 par rapport à une année de référence. Les salles serveurs situées dans des bâtiments tertiaires sont directement concernées. Les données doivent être déclarées sur la plateforme OPERAT gérée par l'ADEME.

La directive EED, Energy Efficiency Directive, dans sa révision de 2023, impose aux datacenters de plus de cinq cents kilowatts de déclarer leurs consommations, leur PUE, leur WUE et leur mix énergétique sur un registre européen, rendant obligatoire un reporting auparavant volontaire.

---

### Normes ISO environnementales

Les normes ISO fournissent des cadres structurés et certifiables pour gérer, mesurer et améliorer les impacts environnementaux.

L'ISO 14001 est la norme internationale de référence pour les systèmes de management environnemental. Elle impose à l'organisation d'identifier ses impacts environnementaux significatifs, dont le numérique, de définir des objectifs et des programmes d'amélioration, et de faire auditer son système par un organisme accrédité. Elle ne fixe pas de niveau de performance absolu mais exige une amélioration continue selon le cycle PDCA : Planifier, Déployer, Vérifier, Agir. Plus de trois cent mille entreprises sont certifiées dans le monde.

L'ISO 50001 est dédiée à la gestion de la performance énergétique. Elle est particulièrement pertinente pour les datacenters et les grandes infrastructures informatiques. Les entreprises certifiées réduisent leur consommation énergétique de dix à trente pour cent sur trois à cinq ans.

L'ISO 14064 fournit la méthodologie pour quantifier et déclarer les émissions de gaz à effet de serre d'une organisation selon les Scopes un, deux et trois. Elle est la base des bilans carbone fiables et vérifiables, et sert de référence pour les reportings CSRD.

Le Label Numérique Responsable, créé par l'Institut du Numérique Responsable, est le référentiel sectoriel français. Il évalue la maturité d'une organisation sur cinq axes : stratégie et gouvernance, sensibilisation et formation, réduction de l'empreinte des équipements, réduction de l'empreinte des services numériques, et prise en compte des impacts sociaux. Il implique une auto-évaluation puis un audit de vérification, et est valable trois ans.

---

### FinOps

Le FinOps, Financial Operations, est une pratique de gouvernance financière du cloud qui vise à optimiser les dépenses cloud en responsabilisant les équipes techniques sur les coûts. Il repose sur un cycle en trois phases impliquant les équipes Finance, Technique et Métiers.

La phase Informer consiste à obtenir une visibilité complète sur les dépenses cloud via l'étiquetage des ressources, l'attribution par équipe ou projet et des tableaux de bord en temps réel. La phase Optimiser identifie et élimine les gaspillages. La phase Opérer institutionnalise les pratiques en définissant des processus, des rituels et des indicateurs.

Le rightsizing, ou redimensionnement, consiste à ajuster la taille des instances cloud à leur utilisation réelle. Une instance cloud surdimensionnée consomme inutilement des ressources et génère des coûts et une empreinte carbone superflus. Analyser les métriques d'utilisation sur plusieurs semaines et descendre en gamme si le taux d'utilisation est faible peut réduire les coûts de vingt à quarante pour cent.

La notion de zombie applicatif est critique : ce sont des applications ou ressources cloud toujours actives et facturées mais non utilisées. Serveurs oubliés après un projet, environnements de test non éteints, bases de données orphelines. Ils représentent cinq à quinze pour cent des ressources cloud dans les grandes organisations.

La différence entre showback et chargeback est importante. Le showback rend visible la consommation de chaque équipe sans refacturation formelle, pour sensibiliser. Le chargeback va plus loin en refacturant effectivement les coûts aux équipes consommatrices, créant une incitation économique directe à optimiser.

La convergence avec le GreenOps est naturelle : supprimer les ressources inutilisées réduit à la fois les coûts et la consommation d'énergie. Le GreenOps ajoute le choix de régions cloud à faible intensité carbone et la planification des traitements par lot selon les plages d'énergie renouvelable disponible. Le gaspillage cloud moyen estimé par la FinOps Foundation est de trente à trente-cinq pour cent des dépenses totales.

---

### Acteurs du numérique responsable

L'écosystème du numérique responsable en France est riche et structuré. Savoir qui fait quoi permet à un responsable informatique de trouver rapidement les données de référence, les référentiels à appliquer et les formations disponibles.

The Shift Project est le think tank de référence sur la décarbonation, fondé en 2010 par Jean-Marc Jancovici. Son rapport "Lean ICT : Pour une sobriété numérique" de 2018 a été le premier document majeur à quantifier l'empreinte carbone du numérique. Il fédère plus de cent entreprises membres et travaille à partir de données chiffrées et de modèles macro-économiques indépendants.

L'Institut du Numérique Responsable, l'INR, est l'association créée en 2018 qui produit le GR491, anime le label Numérique Responsable et dispense des formations certifiantes. Il est le référent opérationnel pour les organisations qui veulent structurer leur démarche.

L'ADEME, Agence de la transition écologique, co-publie avec l'ARCEP l'étude de référence annuelle sur l'empreinte environnementale du numérique en France. Elle gère la plateforme OPERAT pour le décret tertiaire, publie des guides pratiques et finance des projets de recherche comme Boavizta.

L'ARCEP, Autorité de Régulation des Communications Électroniques et des Postes, est le régulateur français des télécommunications. Elle anime l'Observatoire des impacts environnementaux du numérique créé par la loi REEN et collecte les données auprès des opérateurs et des fournisseurs de services.

Le Cigref regroupe les directeurs informatiques des plus grandes entreprises françaises, dont plus de quatre-vingt-dix pour cent des sociétés du CAC 40. Il publie des études sur la maturité numérique responsable et des benchmarks sur les pratiques cloud.

Boavizta est une communauté open source de praticiens qui développe des outils de mesure d'empreinte numérique comme Cloud-scanner et Datavizta, la base de données open source des impacts environnementaux des équipements.

---

## Questions que le jury pourrait poser

Le jury peut vous demander quel est le PUE de votre datacenter et comment l'améliorer. Il peut aussi vous interroger sur la méthode pour mesurer l'empreinte carbone d'un Système d'Information. Il vous demandera peut-être quelles sont les obligations réglementaires d'une Direction des Systèmes d'Information en matière d'impact environnemental, notamment au regard de la loi REEN, de la directive CSRD et du décret tertiaire.

La distinction entre Green IT et IT for Green est une question classique. Vous devrez expliquer que le Green IT vise à réduire l'impact du numérique lui-même, tandis que l'IT for Green utilise le numérique comme levier pour décarboner d'autres secteurs.

Comment convaincre un comité de direction d'investir dans la sobriété numérique, et quel retour sur investissement mettre en avant ? Cette question teste votre capacité à argumenter en termes business. Le FinOps montre que trente à trente-cinq pour cent des dépenses cloud sont gaspillées, le rightsizing peut réduire les factures de vingt à quarante pour cent, et la conformité réglementaire (CSRD, REEN) est désormais obligatoire.

L'effet rebond est un sujet récurrent : vous devrez expliquer le paradoxe de Jevons et ses manifestations dans le numérique, notamment avec l'explosion des usages d'intelligence artificielle générative qui consomme dix à cent fois plus d'énergie par requête qu'une recherche classique.

Sur l'écoconception dans un cycle de développement logiciel, vous devrez citer le RGESN, l'EcoIndex et l'intégration des mesures dans les pipelines d'intégration et de déploiement continus.

Sur les indicateurs clés à mettre en place pour suivre une démarche numérique responsable, vous devrez citer le PUE et ses déclinaisons (CUE, WUE, ERE), le score EcoIndex des services web, le bilan carbone selon les trois Scopes du GHG Protocol, le taux d'utilisation des serveurs et la proportion de dark data éliminé.

La gestion de la fin de vie des équipements informatiques vous amènera à parler de la filière DEEE, des éco-organismes agréés, de la loi AGEC et de l'indice de réparabilité.

FinOps et GreenOps, complémentaires ou contradictoires ? La réponse est qu'ils sont fondamentalement complémentaires : éliminer les ressources inutilisées réduit simultanément les coûts et l'empreinte carbone.

---

## Points de vigilance

Le premier piège à éviter est de réduire la démarche environnementale du Système d'Information au seul PUE du datacenter. La réalité est que la fabrication des équipements représente soixante-dix à quatre-vingt pour cent de l'empreinte carbone numérique. Réduire le PUE sans allonger la durée de vie des terminaux n'est pas une démarche complète.

Le deuxième piège est l'effet rebond. On peut optimiser l'efficacité d'un serveur, réduire la consommation par requête, mais si les usages explosent en parallèle — comme c'est le cas avec l'intelligence artificielle générative — le gain net peut être nul ou négatif. La sobriété numérique implique de questionner l'utilité des usages, pas seulement leur performance.

Le troisième piège est de confondre sauvegarde et archivage. Ce sont deux processus différents : la sauvegarde protège les données actives contre les sinistres, l'archivage déplace les données inactives vers un stockage moins énergivore. Utiliser un SAN haute performance pour de l'archivage est un gaspillage coûteux et inutile.

Le quatrième piège est de négliger le Scope 3 dans les bilans carbone. Le Scope 3, qui inclut la fabrication des équipements, les déplacements et les données cloud, représente souvent soixante-dix à quatre-vingt pour cent du bilan carbone numérique d'une organisation. Un bilan qui n'intègre que les Scopes 1 et 2 est incomplet et donne une image fausse de la réalité.

Le cinquième piège est le greenwashing par absence de mesure. Déclarer une démarche numérique responsable sans indicateurs mesurables, sans objectifs quantifiés et sans reporting structuré n'est pas crédible face au jury ni face aux exigences de la directive CSRD. La mesure est le prérequis de la crédibilité.
