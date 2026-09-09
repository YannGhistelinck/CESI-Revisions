# Blockchain — Guide de révision complet

## Introduction

La blockchain est souvent réduite à Bitcoin ou aux cryptomonnaies dans le débat public, mais pour un manager IT ou un architecte logiciel, elle représente une technologie fondamentalement plus large : un registre distribué, immuable et décentralisé, capable de transformer la traçabilité en supply chain, l'identité numérique, la finance d'entreprise et les contrats automatisés. Ce thème couvre les fondamentaux techniques de la blockchain, ses mécanismes de consensus, les smart contracts, la DeFi, les blockchains d'entreprise, l'interopérabilité, les enjeux juridiques avec le règlement MiCA, l'identité décentralisée avec eIDAS 2.0, et l'impact environnemental. Il soulève aussi des questions philosophiques sur la confiance, la décentralisation et la gouvernance numérique.

---

## Notions clés à maîtriser

### Blockchain — Fondamentaux

Une blockchain est une base de données distribuée et décentralisée, structurée en blocs de données chaînés par des fonctions de hachage cryptographiques. Elle constitue un type de DLT, pour Distributed Ledger Technology, un registre partagé et répliqué sur un réseau de nœuds sans autorité centrale. Le bitcoin whitepaper a été publié en 2008 par l'entité pseudonyme Satoshi Nakamoto, et le marché global de la blockchain est estimé à 28 milliards de dollars en 2024, avec des projections atteignant 825 milliards de dollars en 2032.

Le fonctionnement est le suivant : un utilisateur diffuse une transaction signée numériquement sur le réseau. Les nœuds valident la transaction et la relaient. Les mineurs ou validateurs regroupent les transactions en attente dans un bloc. Le réseau s'accorde sur le bloc valide via un mécanisme de consensus. Le bloc validé est ajouté à la chaîne et diffusé à tous les nœuds. L'immutabilité est garantie car modifier un bloc invaliderait tous les blocs suivants puisque chaque bloc contient le hash du précédent.

La structure d'un bloc comprend un en-tête contenant le hash du bloc précédent, un nonce, un timestamp et la racine de Merkle, ainsi qu'un corps contenant la liste des transactions. Le hash cryptographique SHA-256 utilisé par Bitcoin est une fonction à sens unique, déterministe et avec un effet avalanche : un seul bit modifié produit un hash totalement différent. Le Merkle Tree est un arbre binaire de hachages permettant de résumer toutes les transactions d'un bloc en une seule valeur, et de vérifier l'inclusion d'une transaction sans télécharger tout le bloc.

Le trilemme blockchain, concept de Vitalik Buterin, est fondamental : il est impossible d'atteindre simultanément décentralisation maximale, sécurité maximale et scalabilité maximale. Bitcoin traite environ 7 transactions par seconde contre 24 000 pour Visa.

### Mécanismes de consensus

Un mécanisme de consensus est l'ensemble des règles permettant à des nœuds distribués, sans autorité centrale, de s'accorder sur l'état valide de la blockchain. Le choix du mécanisme détermine la sécurité, la scalabilité, la consommation énergétique et la décentralisation du réseau.

Le Proof of Work, ou preuve de travail, est le mécanisme de Bitcoin. Les mineurs s'affrontent pour résoudre un puzzle cryptographique en trouvant un nonce tel que le hash du bloc soit inférieur à une cible. La difficulté s'ajuste automatiquement pour maintenir un temps de bloc constant d'environ dix minutes. Le premier mineur à trouver la solution reçoit la récompense. Une attaque dite à 51 % nécessiterait de posséder plus de 50 % de la puissance de calcul mondiale, ce qui représente un coût prohibitif. Bitcoin consomme environ 120 à 150 térawattheures par an, comparable à la consommation de la Pologne.

Le halving Bitcoin se produit tous les 210 000 blocs, soit environ tous les quatre ans. La récompense initiale était de 50 BTC par bloc en 2009, elle est passée à 25 en 2012, 12,5 en 2016, 6,25 en 2020 et 3,125 BTC depuis avril 2024. Objectif : limiter l'inflation avec un plafond de 21 millions de BTC.

Le Proof of Stake, ou preuve d'enjeu, est le mécanisme d'Ethereum depuis The Merge de septembre 2022. Les validateurs verrouillent une quantité de cryptomonnaies comme garantie, le staking. La probabilité d'être sélectionné pour valider un bloc est proportionnelle au montant staké. En cas de comportement malveillant, le slashing entraîne une perte partielle ou totale du stake. The Merge a réduit la consommation d'Ethereum de 99,95 %, de 80 térawattheures par an à moins de 0,01 térawattheure par an.

Le Delegated Proof of Stake, utilisé par EOS et TRON, fait voter les détenteurs de tokens pour élire un nombre limité de délégués qui valident les blocs. C'est plus rapide mais moins décentralisé. Le Proof of Authority, utilisé dans les blockchains d'entreprise comme Hyperledger, implique un ensemble d'autorités pré-identifiées qui valident les blocs. Très performant mais centralisé.

### Forks et Layer 2

Un fork désigne une modification des règles du protocole d'une blockchain. Un hard fork est une modification incompatible avec les anciennes versions pouvant créer deux chaînes distinctes. Le hard fork de Bitcoin ayant créé Bitcoin Cash en 2017 est l'exemple canonique : un désaccord sur la taille des blocs a conduit les partisans d'une augmentation à 8 mégaoctets à créer une chaîne séparée. Un soft fork est une modification rétrocompatible, les anciens nœuds continuent d'accepter les nouveaux blocs.

Les solutions Layer 2 sont construites au-dessus de la blockchain principale, ou Layer 1, en héritant de sa sécurité tout en traitant les transactions hors-chaîne. Le Lightning Network est la solution Layer 2 de Bitcoin basée sur des canaux de paiement bilatéraux permettant des transactions quasi-instantanées à très faibles frais. Pour Ethereum, les ZK-Rollups regroupent des centaines de transactions off-chain, génèrent une preuve cryptographique de validité et soumettent uniquement cette preuve sur la chaîne principale, réduisant les frais de 10 à 100 fois. Les Rollups Optimistes, comme Arbitrum et Optimism, supposent la validité des transactions et laissent un délai de sept jours pour contester.

### Smart Contracts

Un smart contract, ou contrat intelligent, est un programme autonome stocké sur une blockchain qui s'exécute automatiquement lorsque des conditions prédéfinies sont remplies, sans intermédiaire. Le concept a été inventé par Nick Szabo en 1994, et Ethereum a été la première blockchain à les généraliser en 2015 avec l'EVM, l'Ethereum Virtual Machine.

Le déploiement d'un smart contract suit ces étapes : un développeur écrit le code en Solidity, le compile en bytecode, le déploie sur la blockchain via une transaction payant du gas, et le contrat reçoit une adresse permanente. Toute interaction avec le contrat est une transaction on-chain. L'exécution est déterministe : même entrée produit même sortie sur tous les nœuds. Le gas est l'unité de mesure du coût computationnel d'une opération sur l'EVM. Depuis EIP-1559 en 2021, la base fee est brûlée et un tip va au validateur.

Le problème des oracles est fondamental : les smart contracts ne peuvent pas accéder directement à des données externes comme les prix, la météo ou les résultats sportifs. Chainlink est le principal réseau d'oracles décentralisés qui fournissent des données du monde réel on-chain. Un oracle centralisé est un point de défaillance unique.

Les DAO, pour Decentralized Autonomous Organizations ou Organisations Autonomes Décentralisées, sont gouvernées par des règles encodées dans des smart contracts. Les décisions sont prises par vote des détenteurs de tokens de gouvernance. Les DApps, pour Decentralized Applications, utilisent des smart contracts pour leur logique métier. Le hack de The DAO en 2016 a conduit au vol de 3,6 millions d'ETH via une faille de réentrance et a conduit au hard fork créant Ethereum Classic. Les Gas fees peuvent varier de quelques centimes à plus de 100 dollars en période de congestion.

### Tokens et tokenisation

Un token est une unité numérique émise sur une blockchain, représentant un actif, un droit ou une utilité. La différence entre coin et token est importante : le coin est l'actif natif d'une blockchain comme BTC ou ETH, tandis que le token est créé via un smart contract sur une blockchain existante comme USDT sur Ethereum.

Les standards Ethereum sont fondamentaux. ERC-20 est le standard des tokens fongibles, interchangeables et divisibles comme USDT, LINK et UNI. ERC-721 est le standard des NFT, pour Non-Fungible Tokens, des tokens uniques et indivisibles. ERC-1155 est un standard multi-token mixant fongible et non fongible.

Les NFT, pour Non-Fungible Tokens, ont connu un pic de marché à 25 milliards de dollars en 2021 avant une correction majeure à 1,5 milliard de dollars en 2023. Une confusion courante : posséder un NFT ne donne pas nécessairement les droits d'auteur sur l'œuvre, car le contenu est généralement stocké hors-chaîne sur IPFS.

Les types de tokens se classifient en utility tokens donnant accès à un service, security tokens représentant des actifs financiers réglementés, governance tokens donnant le droit de vote dans une DAO, et stablecoins dont la valeur est indexée sur un actif comme le dollar. Les RWA, pour Real World Assets, désignent la tokenisation d'actifs physiques : immobilier, matières premières, bons du Trésor. Le BlackRock BUIDL Fund tokenisé sur Ethereum représentait environ 500 millions de dollars en 2024. Le marché des RWA tokenisés est estimé à 10 milliards de dollars en 2024 avec des projections supérieures à 16 000 milliards de dollars d'ici 2030.

### DeFi — Finance décentralisée

La DeFi, pour Decentralized Finance, désigne l'ensemble des services financiers construits sur des blockchains publiques via des smart contracts, sans intermédiaire centralisé. Le TVL, pour Total Value Locked, mesure la valeur totale des actifs déposés dans les protocoles DeFi. Il a atteint un pic de 180 milliards de dollars en novembre 2021 et se stabilisait autour de 100 à 120 milliards de dollars en 2024.

Les DEX, pour Decentralized Exchanges, fonctionnent via des liquidity pools et un AMM, ou Automated Market Maker. La formule de base est x multiplié par y égale une constante k. Les liquidity providers déposent des actifs dans les pools et perçoivent une fraction des frais. L'impermanent loss est la perte relative subie par un fournisseur de liquidité lorsque les prix des actifs varient par rapport au moment du dépôt. Uniswap est le plus grand DEX avec plus de 1 500 milliards de dollars de volume cumulé échangé.

Les protocoles de prêt comme Aave et Compound permettent des emprunts sur-collatéralisés avec des taux algorithmiques. Les Flash Loans d'Aave sont des prêts sans collatéral exécutés et remboursés au sein d'une seule transaction blockchain.

Les stablecoins se classifient en trois catégories. Les stablecoins fiat-collatéralisés comme USDT et USDC sont adossés à des réserves en dollars. Les stablecoins crypto-collatéralisés comme DAI de MakerDAO sont sur-collatéralisés en cryptos. Les stablecoins algorithmiques maintiennent leur parité par algorithme sans collatéral direct, un modèle très risqué illustré par l'effondrement de Terra UST en mai 2022 avec une perte de 40 milliards de dollars.

Les CBDC, pour Central Bank Digital Currencies, sont des monnaies numériques émises et garanties par une banque centrale. Plus de 130 pays sont en phase d'exploration ou de déploiement selon la BIS en 2024. L'e-CNY chinois est le déploiement le plus avancé.

### Web3 et wallets

Le Web3 désigne la vision d'un internet décentralisé où les utilisateurs contrôlent leurs données et actifs numériques grâce à la blockchain, sans dépendre de plateformes centralisées. La distinction entre Web1, Web2 et Web3 est pédagogique : le Web1 des années 1990 était statique, le Web2 actuel est interactif mais centralisé sur les GAFAM, le Web3 vise la décentralisation et la propriété des données.

Un wallet crypto est un outil gérant les clés cryptographiques privées d'un utilisateur. La clé privée, un nombre de 256 bits, permet de signer les transactions. La clé publique en est dérivée et est partageable. L'adresse est un hash de la clé publique. Le wallet ne contient pas de cryptomonnaies : il contient les clés permettant de prouver la propriété des fonds enregistrés sur la blockchain.

La seed phrase, ou phrase mnémotechnique, est une séquence de 12 ou 24 mots permettant de régénérer toutes les clés privées d'un wallet. Sa compromission entraîne la perte irréversible de tous les actifs. La règle d'or est de ne jamais la stocker numériquement.

Les wallets hot sont connectés à Internet comme MetaMask, pratiques mais moins sécurisés. Les wallets cold ou hardware wallets comme Ledger et Trezor stockent les clés hors ligne et offrent une sécurité maximale. Les wallets custodiaux, proposés par les exchanges comme Coinbase ou Binance, délèguent la gestion des clés à un tiers, ce que résume la formule "not your keys, not your coins". La faillite de FTX en novembre 2022 avec 8 milliards de dollars de fonds clients inaccessibles illustre ce risque.

### Blockchains d'entreprise

Les blockchains d'entreprise sont des réseaux permissionnés dont l'accès est restreint à des participants autorisés. Elles répondent aux contraintes entreprises : confidentialité des transactions, conformité réglementaire, performances élevées et gouvernance contrôlée.

Hyperledger Fabric est le framework open-source de la Linux Foundation contribué par IBM. Il utilise une architecture modulaire avec des canaux permettant des transactions privées entre sous-ensembles de membres, des chaincodes ou smart contracts en Go, Java ou Node.js, et un MSP pour la gestion des identités. Il ne possède pas de cryptomonnaie native. Walmart a réduit de 7 jours à 2,2 secondes le temps pour tracer l'origine d'une mangue grâce à IBM Food Trust sur Hyperledger Fabric.

R3 Corda est conçu spécifiquement pour la finance et les contrats légaux. Contrairement aux autres blockchains, Corda ne partage les transactions qu'entre les parties directement concernées, garantissant une confidentialité maximale. Plus de 300 banques et institutions financières l'utilisent dont BNP Paribas et HSBC.

Quorum est un fork d'Ethereum créé par JPMorgan en 2016 et cédé à Consensys en 2020. Compatible EVM, il supporte les smart contracts Solidity et ajoute des transactions privées via Tessera. VeChain est orientée supply chain et IoT avec un mécanisme de consensus Proof of Authority, utilisé par LVMH, BMW et Walmart China.

Le BaaS, pour Blockchain as a Service, permet aux entreprises de déployer des blockchains sans gérer l'infrastructure, proposé par AWS, Microsoft Azure et IBM.

### Interopérabilité blockchain

L'interopérabilité blockchain désigne la capacité de plusieurs blockchains indépendantes à communiquer et échanger de la valeur sans intermédiaire centralisé. Les bridges, ou ponts, sont des contrats intelligents qui verrouillent des actifs sur la chaîne source et émettent des tokens équivalents, les wrapped tokens, sur la chaîne de destination. Les bridges sont les cibles privilégiées des hackers : le Ronin Bridge a subi le plus grand hack de l'histoire, avec 625 millions de dollars volés en mars 2022, et Wormhole a perdu 320 millions de dollars en février 2022.

Polkadot utilise une architecture Relay Chain avec des parachains, des blockchains spécialisées qui partagent la sécurité de la Relay Chain et communiquent via le protocole XCM pour Cross-Consensus Messaging. Cosmos connecte des blockchains souveraines et indépendantes via le protocole IBC, pour Inter-Blockchain Communication, sans sécurité partagée imposée. L'écosystème Cosmos représente plus de 60 blockchains interconnectées.

### Blockchain et supply chain

La blockchain appliquée à la supply chain crée un registre immuable et partagé de toutes les étapes de la vie d'un produit. Elle répond au problème fondamental de la chaîne logistique : la fragmentation de l'information entre acteurs multiples. Elle assure une single source of truth partagée par tous les participants.

La traçabilité ascendante permet de remonter d'un produit fini vers son origine. La traçabilité descendante permet, à partir d'une matière première, d'identifier tous les produits finis qui en contiennent pour faciliter les rappels. Les smart contracts automatisent les paiements ou déclenchent des alertes dès qu'une condition est remplie comme un dépassement de température.

Le Digital Product Passport, ou passeport numérique produit, est un concept européen du règlement ESPR, pour Ecodesign for Sustainable Products Regulation, qui devra accompagner chaque produit tout au long de son cycle de vie. Il est obligatoire pour plusieurs catégories à partir de 2027. Le Battery Passport pour les batteries de véhicules électriques est imposé par le règlement UE 2023/1542 dès 2027.

Attention au problème du "garbage in, garbage out" : la blockchain garantit l'intégrité des données enregistrées, mais ne peut pas vérifier que ces données reflètent fidèlement la réalité physique. L'échec de TradeLens, malgré le soutien d'IBM et Maersk, illustre que l'adoption collective est le principal défi des plateformes blockchain B2B.

### RFID, NFC et IoT pour la traçabilité

Le RFID, pour Radio Frequency Identification, et le NFC, pour Near Field Communication, sont des technologies d'identification sans contact qui forment la couche de collecte de données physiques indispensable à toute traçabilité fiable.

Le RFID utilise des tags passifs ou actifs : un lecteur émet une onde radio qui alimente le tag passif et déclenche la transmission de son identifiant unique, l'EPC pour Electronic Product Code. L'avantage majeur est la lecture en masse sans ligne de vue, permettant de lire simultanément des centaines de tags. Decathlon utilise 1,5 milliard de tags RFID par an, permettant des inventaires complets en quelques minutes contre plusieurs jours auparavant.

Le NFC est un sous-ensemble du RFID limité à une portée inférieure à 10 centimètres, utilisé pour les paiements sans contact et l'authentification produits. Le standard GS1 EPCIS 2.0 structure les événements de traçabilité selon quatre dimensions : quoi, où, quand et pourquoi, avant leur inscription on-chain. Les protocoles IoT comme LoRaWAN permettent une communication longue portée à faible consommation énergétique pour des capteurs déployés sur de grandes zones.

### Identité décentralisée — SSI

La SSI, pour Self-Sovereign Identity ou identité auto-souveraine, est un paradigme dans lequel l'individu contrôle entièrement ses propres données d'identité sans dépendre d'un tiers centralisé. Elle repose sur trois piliers.

Les DID, pour Decentralized Identifiers, sont des identifiants uniques et persistants enregistrés sur une blockchain. Le format est did:method:identifiant-unique. Le standard W3C DID Core 1.0 a été publié en juillet 2022. Les Verifiable Credentials, ou attestations vérifiables, sont des attestations numériques signées cryptographiquement par un émetteur. Le triangle de confiance implique trois rôles : l'Issuer ou émetteur qui signe le credential, le Holder ou porteur qui le conserve dans son wallet, et le Verifier ou vérificateur qui valide la signature. La divulgation sélective permet au porteur de ne révéler qu'une partie des attributs d'un credential, par exemple prouver qu'on est majeur sans révéler sa date de naissance. Le wallet d'identité est l'application qui stocke les credentials.

L'EBSI, pour European Blockchain Services Infrastructure, est l'infrastructure blockchain déployée par la Commission européenne pour des cas d'usage publics comme les diplômes vérifiables. L'UE vise 80 % des citoyens équipés d'un portefeuille d'identité numérique EUDI d'ici 2030.

### Zero-Knowledge Proof — ZKP

Une preuve à divulgation nulle de connaissance est un protocole cryptographique permettant à une partie, le prouveur, de convaincre une autre partie, le vérificateur, qu'elle possède une information ou satisfait une condition, sans jamais révéler l'information elle-même. L'analogie de la grotte d'Ali Baba l'illustre bien : Peggy peut prouver à Victor qu'elle connaît le mot de passe secret d'une grotte en anneau en entrant par un couloir et en ressortant par l'autre sur demande, sans jamais révéler le mot.

Les trois propriétés fondamentales d'un ZKP sont la complétude, la solidité et la divulgation nulle. Les ZK-SNARKs, pour Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge, produisent des preuves très compactes et rapides à vérifier, mais nécessitent une phase de setup de confiance. Les ZK-STARKs, pour Zero-Knowledge Scalable Transparent Arguments of Knowledge, n'ont pas de trusted setup et sont résistants aux ordinateurs quantiques, mais leurs preuves sont plus volumineuses.

Les ZK-Rollups utilisent ces preuves pour la scalabilité d'Ethereum : ils regroupent des centaines de transactions off-chain, génèrent une preuve ZK de leur validité et soumettent uniquement cette preuve sur la chaîne principale. zkSync a traité plus de 500 millions de transactions depuis son lancement en 2023. StarkNet permet des débits théoriques de 10 000 transactions par seconde contre 15 pour Ethereum Layer 1.

### Cadre juridique crypto et blockchain

Le règlement MiCA, pour Markets in Crypto-Assets, adopté en juin 2023 et applicable depuis décembre 2024, est le premier cadre réglementaire complet au monde sur les cryptoactifs. Il couvre les émetteurs de tokens et les CASP, pour Crypto-Asset Service Providers. Il permet un passeport européen pour les prestataires de services. Les NFT véritablement uniques et la DeFi entièrement décentralisée sont exclus du périmètre de MiCA.

En France, la loi PACTE de 2019 a créé le statut PSAN, pour Prestataire de Services sur Actifs Numériques. Ce statut est remplacé progressivement par le CASP de MiCA. Plus de 80 PSAN étaient enregistrés auprès de l'AMF en 2024. La Travel Rule, inspirée de la recommandation R.16 du GAFI, impose aux prestataires de transmettre les informations d'identification de l'émetteur et du bénéficiaire lors de transferts supérieurs à 1 000 euros.

La tension blockchain et RGPD est fondamentale : l'article 17 du RGPD garantit le droit à l'effacement des données, mais les données inscrites sur une blockchain publique sont immuables. Les solutions sont de stocker uniquement des hashs on-chain avec les données off-chain, ou de recourir à l'"effacement cryptographique" en détruisant la clé de chiffrement. Les adresses de portefeuilles ne sont pas anonymes mais pseudonymes : toutes les transactions sont publiques et traçables, et une adresse peut être reliée à une identité réelle.

### eIDAS 2.0 et identité numérique européenne

eIDAS 2.0, pour Electronic IDentification, Authentication and trust Services version 2.0, est le règlement européen révisé adopté en mars 2024 qui refonde le cadre d'identification électronique dans l'UE. Sa grande nouveauté est l'EUDI Wallet, le portefeuille d'identité numérique européen, que chaque État membre devra proposer à ses citoyens d'ici 2026.

L'EUDI Wallet permettra de stocker et présenter des attributs d'identité : pièce d'identité, permis de conduire, diplômes, prescriptions médicales. Il sera utilisable auprès de services publics et privés dans toute l'UE. Les grandes plateformes comme les banques, les télécoms et les réseaux sociaux devront accepter l'EUDI Wallet comme moyen d'authentification. L'architecture repose sur les standards SSI avec les DID, les Verifiable Credentials et le protocole OID4VC pour OpenID for Verifiable Credentials. L'objectif est que 80 % des citoyens de l'UE soient équipés d'un EUDI Wallet d'ici 2030.

L'ISO/TC 307 est le comité technique de l'ISO créé en 2016 pour la normalisation internationale des technologies blockchain. Il a publié plus de 15 normes sur la terminologie, l'architecture de référence, les smart contracts et la privacy.

### Impact environnemental de la blockchain

Bitcoin consomme environ 120 à 150 térawattheures par an selon le CBECI, le Cambridge Bitcoin Electricity Consumption Index, comparable à la consommation de la Pologne ou de l'Argentine. Le Proof of Work repose sur une compétition de calcul avec des ASICs, des puces spécialisées, dont la quasi-totalité de la puissance est dissipée en chaleur. La difficulté s'ajuste pour maintenir un bloc toutes les dix minutes quelle que soit la puissance déployée, ce qui signifie que plus de mineurs entraîne plus de consommation sans gain de productivité.

The Merge d'Ethereum en septembre 2022 a démontré qu'une réduction radicale est techniquement possible : la consommation est passée de 80 térawattheures à moins de 0,01 térawattheure par an, une réduction de 99,95 %. Cela place Ethereum parmi les blockchains les plus efficientes en énergie.

Le Bitcoin Mining Council, une coalition de mineurs créée en 2021, déclare environ 58 % d'énergie durable pour ses membres, mais ses données sont auto-déclaratives et non auditées, d'où des accusations de greenwashing. Le Crypto Climate Accord vise 100 % d'énergies renouvelables pour l'industrie crypto d'ici 2030. L'État de New York a adopté un moratoire de deux ans sur les nouvelles fermes de mining Proof of Work alimentées par des énergies fossiles en novembre 2022. La Chine a interdit le mining en 2021, entraînant une migration massive vers les États-Unis, le Kazakhstan et la Russie.

Pour nuancer, le secteur bancaire traditionnel consomme environ 250 térawattheures par an selon Digiconomist. Le green mining valorise des énergies renouvelables excédentaires, et des projets comme Qarnot Computing en France récupèrent la chaleur des serveurs de mining pour chauffer des appartements.

---

## Questions que le jury pourrait poser

- Qu'est-ce que la blockchain et comment fonctionne-t-elle concrètement ?
- Proof of Work versus Proof of Stake : quelles différences et quel impact environnemental ?
- Comment la blockchain peut-elle améliorer la traçabilité en supply chain ?
- Smart contracts : quels cas d'usage concrets en entreprise ?
- Blockchain permissionnée versus publique : laquelle choisir pour une entreprise ?
- Quels sont les enjeux juridiques de la blockchain, MiCA, loi PACTE, droit à l'oubli ?
- Comment la blockchain répond-elle aux enjeux de la confiance numérique ?
- DeFi : opportunité ou menace pour le système financier traditionnel ?
- Quel est le bilan environnemental de la blockchain et comment l'améliorer ?
- Identité décentralisée SSI : comment ça fonctionne et quel intérêt pour l'entreprise ?

---

## Points de vigilance

Premier point de vigilance : confondre blockchain et Bitcoin. La blockchain est la technologie sous-jacente ; Bitcoin en est la première application. Ethereum, Hyperledger Fabric et R3 Corda sont d'autres blockchains avec des objectifs radicalement différents. Ne pas réduire la blockchain à la spéculation sur les cryptomonnaies.

Deuxième point de vigilance : ignorer le problème du "garbage in, garbage out" dans la traçabilité supply chain. La blockchain garantit que les données enregistrées ne sont pas modifiées, mais elle ne peut pas vérifier que ces données correspondent à la réalité physique. Si un acteur enregistre de fausses informations, elles seront "certifiées" immutablement sur la chaîne.

Troisième point de vigilance : présenter les smart contracts comme infaillibles parce qu'automatisés. Le hack de The DAO en 2016 avec 3,6 millions d'ETH volés et le hack de Ronin avec 625 millions de dollars en 2022 illustrent que les bugs dans les smart contracts sont permanents et catastrophiques. L'audit de code est indispensable.

Quatrième point de vigilance : croire que les adresses blockchain garantissent l'anonymat. Les adresses sont pseudonymes, pas anonymes. Toutes les transactions sont publiques et traçables. Les analyses on-chain permettent de relier une adresse à une identité réelle, notamment via les KYC des exchanges.

Cinquième point de vigilance : opposer blockchain publique et blockchain d'entreprise comme deux univers séparés. La tendance 2024-2025 est à la convergence : des entreprises comme la Société Générale émettent des obligations tokenisées sur Ethereum public, et des protocoles comme Polygon se positionnent spécifiquement pour les usages enterprise sur des blockchains publiques.
