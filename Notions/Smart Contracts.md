---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Smart Contracts

## En bref

### Définition
Un **smart contract** (contrat intelligent) est un programme autonome stocké sur une blockchain, qui s'exécute automatiquement lorsque des conditions prédéfinies sont remplies, sans intermédiaire. Le code est immuable une fois déployé. **Les DApps** (applications décentralisées) utilisent des smart contracts pour leur logique métier. Les **DAOs** (Organisations Autonomes Décentralisées) s'appuient sur des smart contracts pour gouverner collectivement.

### Pourquoi c'est important
Les smart contracts automatisent des accords complexes (prêts, échanges, votes) sans tiers de confiance, réduisant les coûts et les délais. Ils sont le fondement de la DeFi, des NFTs, des DAOs et de la tokenisation. Leur immutabilité est à la fois une force (résistance à la censure) et une faiblesse (les bugs sont permanents).

### Chiffres clés
- **1994** : concept inventé par Nick Szabo
- **2015** : Ethereum, première blockchain à généraliser les smart contracts (EVM — Ethereum Virtual Machine)
- **TVL (Total Value Locked) en smart contracts DeFi** : ~100-150 Mds$ (2024)
- **The DAO Hack (2016)** : 3,6 millions d'ETH volés via une faille de réentrance dans un smart contract
- **Gas fees Ethereum** : de quelques centimes à >100$ en période de congestion

---

## Approfondir

### Fonctionnement

**Déploiement d'un smart contract :**
1. Un développeur écrit le code (ex. Solidity pour Ethereum)
2. Le code est compilé en bytecode
3. Il est déployé sur la blockchain via une transaction (coûte du gas)
4. Le contrat reçoit une adresse permanente sur la blockchain
5. Toute interaction avec le contrat est une transaction on-chain

**Exécution :**
- Le contrat s'exécute sur l'EVM (Ethereum Virtual Machine) — chaque nœud exécute le même code
- Résultat déterministe : même entrée → même sortie sur tous les nœuds
- Turing-complet : capable d'exécuter n'importe quel calcul (boucles, conditions…)

**Gas fees :**
- Unité de mesure du coût computationnel d'une opération sur l'EVM
- Gas price (Gwei) × Gas used = coût en ETH
- Depuis EIP-1559 (2021) : base fee brûlée + tip pour le validateur
- Évite les attaques par boucles infinies (limite de gas par bloc)

**Oracle :**
- Problème : les smart contracts ne peuvent pas accéder directement à des données externes (prix, météo, résultats sportifs…)
- Solution : les oracles sont des services qui fournissent des données du monde réel on-chain
- **Chainlink** : principal réseau d'oracles décentralisés, sécurisé par un réseau de nœuds
- Oracle centralisé = point de défaillance unique → risque d'attaque

**DAO (Decentralized Autonomous Organization) :**
- Organisation gouvernée par des règles encodées dans des smart contracts
- Les décisions sont prises par vote des détenteurs de tokens de gouvernance
- Exemples : MakerDAO (gouverne le stablecoin DAI), Uniswap DAO, Compound

**DApp (Decentralized Application) :**
- Application dont le backend est un smart contract sur une blockchain
- Frontend généralement classique (web), mais interagit avec la blockchain via des wallets (MetaMask)
- Exemples : Uniswap (DEX), Aave (prêts), OpenSea (NFTs)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Automatisation sans intermédiaire | Bugs permanents (code is law) |
| Transparent et auditable | Code complexe, risque d'exploitation |
| Résistant à la censure | Dépendance aux oracles (garbage in, garbage out) |
| Exécution déterministe | Coûts de gas variables et potentiellement élevés |
| Composabilité (protocoles s'intègrent entre eux) | Pas d'accès aux données off-chain nativement |

### Acteurs et solutions

| Acteur | Solution | Rôle |
|--------|----------|------|
| **Ethereum** | EVM, Solidity | Plateforme principale de smart contracts |
| **Chainlink** | Oracles décentralisés | Données du monde réel on-chain |
| **OpenZeppelin** | Bibliothèques de smart contracts audités | Sécurité des développements |
| **MakerDAO** | DAI + smart contracts de prêt | DAO de référence |
| **Solana** | Programmes (smart contracts en Rust) | Alternative haute performance |
| **Certik / Trail of Bits** | Audit de smart contracts | Sécurité |

### Cas d'usage concrets
- **DeFi** : prêts automatiques (Aave), échanges décentralisés (Uniswap), stablecoins algorithmiques (MakerDAO)
- **NFTs** : création, transfert et royalties automatiques (ERC-721)
- **Supply Chain** : exécution automatique de paiements à la livraison confirmée par oracle IoT
- **Assurance paramétrique** : indemnisation automatique en cas de sinistre confirmé (ex. Etherisc)
- **Vote** : gouvernance de protocoles (Compound, Uniswap)

### Chiffres et tendances
- **Solidité du marché** : Ethereum héberge >3 000 DApps actives (2024)
- **The DAO Hack (2016)** : a conduit au hard fork Ethereum / Ethereum Classic
- **Attaques de réentrance** : toujours une des principales failles (ex. Ronin Network hack : 625M$ en 2022)
- **EIP-1559** : depuis août 2021, une partie des fees est brûlée → ETH devient déflationniste en période de forte activité

---

## Flashcards
#flashcards/Blockchain/Smart_Contracts

Qu'est-ce qu'un smart contract ? :: Programme autonome stocké sur une blockchain, qui s'exécute automatiquement lorsque ses conditions sont remplies, sans intermédiaire.

Qu'est-ce que le "gas" dans Ethereum ? :: Unité de mesure du coût computationnel d'une opération sur l'EVM. Le coût final = gas used × gas price (en Gwei), payé en ETH.

Qu'est-ce qu'un oracle et pourquoi est-il nécessaire ? :: Service fournissant des données du monde réel (prix, météo…) à des smart contracts, qui ne peuvent pas accéder eux-mêmes à des sources externes.

Qu'est-ce qu'une DAO ? :: Organisation Autonome Décentralisée gouvernée par des smart contracts ; les décisions sont prises par vote des détenteurs de tokens de gouvernance.

Qu'est-ce que "code is law" ? :: Principe selon lequel les smart contracts s'exécutent exactement comme codés, sans possibilité d'interprétation ou d'override — les bugs sont permanents et les transactions irréversibles.

Quel événement a illustré les risques des smart contracts en 2016 ? :: Le hack de "The DAO" : exploitation d'une faille de réentrance permettant de drainer 3,6M ETH, conduisant au hard fork Ethereum/Ethereum Classic.

---

## Sources
- Szabo, N. (1994). *Smart Contracts*. unenumerated.blogspot.com
- Ethereum Foundation — Solidity Documentation (docs.soliditylang.org)
- Chainlink — Oracle Documentation (docs.chain.link)
- OpenZeppelin — Security Best Practices
- Rekt.news — Historique des hacks de smart contracts

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[DeFi (Finance décentralisée)]]
- [[Tokens et tokenisation]]
- [[Web3 et wallets]]
- [[Forks et évolutions de protocole]]
- [[Mécanismes de consensus]]
