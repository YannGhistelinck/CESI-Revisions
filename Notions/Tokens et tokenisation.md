---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Tokens et tokenisation

![[N — Tokens et tokenisation.mp3]]
## En bref

### Définition
Un **token** est une unité numérique émise sur une blockchain, représentant un actif, un droit ou une utilité. La **tokenisation** consiste à représenter un actif réel ou numérique sous forme de tokens on-chain. On distingue les **tokens fongibles** (ERC-20 : interchangeables) des **NFTs** (ERC-721 : non fongibles, uniques). Les **ICO** (Initial Coin Offering) et **STO** (Security Token Offering) sont des modes de levée de fonds via tokens. Les **RWA** (Real World Assets) désignent la tokenisation d'actifs physiques.

### Pourquoi c'est important
La tokenisation est la promesse de rendre tout actif (immobilier, art, actions, dette) liquide, fractionnable et échangeable 24h/24 sur des marchés mondiaux. Elle remodèle la finance (DeFi), la propriété intellectuelle (NFTs) et l'investissement (RWA).

### Chiffres clés
- **Marché NFT** : pic à ~25 Mds$ en 2021, ~1,5 Mds$ en 2023 (correction majeure)
- **Marché RWA tokenisés** : ~10 Mds$ (2024), projections >16 000 Mds$ d'ici 2030 (Boston Consulting Group)
- **ICO 2017-2018** : ~20 Mds$ levés, majoritairement sans réglementation
- **Ethereum ERC-20** : standard dominant, des milliers de tokens créés

---

## Approfondir

### Fonctionnement

**Token vs Coin :**
- **Coin** (cryptomonnaie) : actif natif d'une blockchain (BTC sur Bitcoin, ETH sur Ethereum)
- **Token** : actif créé via un smart contract sur une blockchain existante (USDT sur Ethereum, UNI sur Ethereum)

**Standards de tokens (Ethereum) :**
| Standard | Type | Description | Exemples |
|----------|------|-------------|---------|
| ERC-20 | Fongible | Token interchangeable, divisible | USDT, LINK, UNI |
| ERC-721 | Non fongible (NFT) | Token unique, indivisible | CryptoPunks, BAYC |
| ERC-1155 | Multi-token | Mélange fongible et non fongible | Jeux blockchain (Enjin) |

**NFT (Non-Fungible Token) :**
- Chaque NFT a un identifiant unique (tokenId)
- Le smart contract ERC-721 stocke le propriétaire de chaque tokenId
- Le contenu (image, vidéo) est généralement stocké hors-chaîne (IPFS ou serveur centralisé) — seul le hash ou l'URL est on-chain
- Droits de propriété ≠ droits d'auteur : posséder un NFT ne donne pas nécessairement les droits sur l'œuvre

**Types de tokens selon leur usage :**
| Type | Description | Exemple |
|------|-------------|---------|
| **Utility token** | Donne accès à un service/réseau | Filecoin (FIL), Basic Attention Token (BAT) |
| **Security token** | Représente un actif financier réglementé | Actions tokenisées, obligations |
| **Governance token** | Droit de vote dans une DAO | UNI (Uniswap), COMP (Compound) |
| **Stablecoin** | Valeur stable indexée sur actif (USD, or) | USDT, USDC, DAI |

**ICO (Initial Coin Offering) :**
- Levée de fonds via émission de tokens, sans cadre réglementaire strict (2017-2018)
- Similaire à une IPO mais non réglementée → nombreuses arnaques (exit scams)
- Remplacée en grande partie par les IDO (Initial DEX Offering) et IEO (Initial Exchange Offering)

**STO (Security Token Offering) :**
- Émission de tokens qualifiés de valeurs mobilières, soumis à la réglementation financière (SEC, AMF)
- Représente des actions, obligations, parts de fonds d'investissement
- Avantage : légalité et protection des investisseurs | Inconvénient : processus lourd et coûteux

**RWA (Real World Assets) :**
- Tokenisation d'actifs physiques : immobilier, matières premières, œuvres d'art, fonds d'État
- Fractionnement : permettre d'acheter 0,001% d'un immeuble
- Exemples : Ondo Finance (bons du Trésor américains tokenisés), Maple Finance (crédit privé)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Fractionnabilité des actifs | Volatilité extrême (hors stablecoins) |
| Liquidité 24/7 sur marchés mondiaux | Arnaques ICO, rug pulls |
| Programmabilité (smart contracts) | Cadre réglementaire incertain |
| Traçabilité et transparence | Risques de custodie (perte de clés) |
| Accès à des marchés habituellement fermés | NFT : droits réels souvent flous |

### Acteurs et solutions

| Acteur | Solution | Domaine |
|--------|----------|---------|
| **OpenSea / Blur** | Marketplace NFT | Marché secondaire NFT |
| **Ondo Finance** | Tokenisation de bons du Trésor US | RWA |
| **Polymath / Securitize** | Plateforme STO | Security Tokens |
| **Circle (USDC) / Tether (USDT)** | Stablecoins fiat | Tokens de valeur stable |
| **Uniswap** | DEX pour tokens ERC-20 | Échange décentralisé |
| **Bpifrance / Société Générale** | Obligations tokenisées | Finance institutionnelle |

### Cas d'usage concrets
- **NFTs dans les jeux** : Axie Infinity (play-to-earn), actifs in-game propriétaires
- **Royalties automatiques** : artistes percevant des royalties sur chaque revente via smart contract
- **Immobilier tokenisé** : RealT (propriétés américaines tokenisées en ERC-20)
- **Obligations tokenisées** : Société Générale — émission de covered bonds sur Ethereum (2019, 2021)
- **Tokenisation de fonds** : BlackRock BUIDL Fund sur Ethereum (~500M$ en 2024)

### Chiffres et tendances
- **BlackRock BUIDL** : plus grand fonds tokenisé, ~500M$ (2024)
- **Marché stablecoins** : ~160 Mds$ de capitalisation (2024, USDT + USDC dominants)
- **Ethereum** : standard ERC-20 héberge des milliers de tokens, dont les 10 plus grands représentent ~80% des volumes
- **Réglementation MiCA (EU, 2024)** : premier cadre réglementaire global pour les crypto-actifs, dont les stablecoins

---

## Flashcards
#flashcards/Blockchain/Tokens_et_tokenisation

Quelle est la différence entre un token fongible et un NFT ? :: Un token fongible (ERC-20) est interchangeable et divisible (1 USDT = 1 USDT) ; un NFT (ERC-721) est unique et indivisible, représentant un actif spécifique.

Qu'est-ce qu'un security token et en quoi diffère-t-il d'un utility token ? :: Un security token représente un actif financier réglementé (action, obligation) soumis au droit boursier ; un utility token donne accès à un service sans être une valeur mobilière.

Qu'est-ce qu'une ICO ? :: Initial Coin Offering : levée de fonds par émission de tokens cryptographiques, sans cadre réglementaire strict. Pratique popularisée en 2017-2018, souvent associée à des arnaques.

Qu'est-ce que la tokenisation des RWA ? :: Représentation sur blockchain d'actifs physiques (immobilier, bons du Trésor, matières premières) sous forme de tokens, permettant fractionnement et liquidité.

Quel est le standard Ethereum pour les NFTs ? :: ERC-721 : standard définissant un token avec identifiant unique (tokenId) non interchangeable avec un autre token du même contrat.

Quelle est la différence entre un ICO et un STO ? :: Un ICO émet des utility tokens sans cadre réglementaire ; un STO émet des security tokens qualifiés de valeurs mobilières, soumis à la réglementation financière.

---

## Sources
- Ethereum Foundation — ERC Standards (eips.ethereum.org)
- Boston Consulting Group — "Relevance of On-chain Asset Tokenization" (2022)
- AMF France — Doctrine ICO/STO
- Règlement MiCA — EUR-Lex (2023)
- CoinGecko — Stablecoin Market Report (2024)

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[Smart Contracts]]
- [[DeFi (Finance décentralisée)]]
- [[Web3 et wallets]]
- [[Mécanismes de consensus]]
