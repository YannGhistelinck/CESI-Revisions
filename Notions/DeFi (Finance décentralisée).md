---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# DeFi (Finance décentralisée)

## En bref

### Définition
La **DeFi** (Decentralized Finance) désigne l'ensemble des services financiers (prêts, échanges, épargne, assurance) construits sur des blockchains publiques via des smart contracts, sans intermédiaire centralisé. Le **TVL** (Total Value Locked) mesure la valeur totale des actifs déposés dans les protocoles DeFi. Les **stablecoins** sont des tokens à valeur stable (indexée USD, or…). Les **CBDC** sont les équivalents étatiques numériques des monnaies fiduciaires.

### Pourquoi c'est important
La DeFi vise à rendre accessibles à tous — sans KYC ni compte bancaire — les services financiers traditionnels. Elle introduit de nouveaux modèles (yield farming, liquidity pools) mais aussi de nouveaux risques (hacks, volatilité, régulation). Les CBDC représentent la réponse des États à la montée des cryptos.

### Chiffres clés
- **TVL DeFi (pic)** : ~180 Mds$ en novembre 2021
- **TVL DeFi (2024)** : ~100-120 Mds$ (Ethereum dominant, ~60%)
- **Marché stablecoins** : ~160 Mds$ de capitalisation (2024)
- **CBDC** : >130 pays en phase d'exploration ou de déploiement (BIS, 2024)
- **Uniswap** : >1 500 Mds$ de volume cumulé échangé depuis 2018

---

## Approfondir

### Fonctionnement

**Architecture DeFi :**
- Couche 1 : blockchain de base (Ethereum, Solana…)
- Couche 2 : protocoles DeFi (smart contracts de prêt, échange, épargne)
- Couche 3 : agrégateurs et interfaces utilisateur (1inch, Zapper)

**DEX (Decentralized Exchange) et Liquidity Pools :**
- Dans un DEX classique (type Uniswap), pas de carnet d'ordres (order book)
- Les échanges se font contre des **liquidity pools** : réserves d'actifs déposées par des **liquidity providers** (LP)
- Formule AMM (Automated Market Maker) : x × y = k (constante de produit)
- Les LP perçoivent une fraction des frais de transaction en récompense
- Risque : **impermanent loss** (perte relative vs détention simple due à la variation de prix)

**Yield Farming :**
- Stratégie consistant à déplacer ses actifs entre protocoles pour maximiser les rendements
- Rendements issus de : frais de transaction, récompenses en tokens de gouvernance
- Peut atteindre des APY (rendements annuels) très élevés (>100%), mais aussi très risqués
- Souvent liés aux **liquidity mining** : protocoles distribuent leurs tokens pour attirer des liquidités

**Protocoles de prêt (Lending) :**
- Les emprunteurs déposent du collatéral (>valeur du prêt → surcollatéralisation)
- Les prêteurs déposent leurs actifs et perçoivent des intérêts
- Taux d'intérêt algorithmiques, ajustés selon l'offre et la demande
- Exemples : Aave (Flash Loans, prêts sans collatéral sur une seule transaction), Compound

**Stablecoins :**
| Type | Mécanisme | Exemples | Risques |
|------|-----------|---------|---------|
| Fiat-collatéralisé | 1 token = 1$ en réserve fiduciaire | USDT, USDC | Risque de contrepartie (émetteur centralisé) |
| Crypto-collatéralisé | Collatéral en cryptos (surcollatéralisé) | DAI (MakerDAO) | Liquidation en cas de chute des prix |
| Algorithmique | Maintien du peg par algorithme | Terra UST (effondré 2022) | Très risqué, spirale de mort possible |

**CBDC (Central Bank Digital Currency) :**
- Monnaie numérique émise et garantie par une banque centrale
- Peut être basée sur DLT ou non
- Exemples : e-CNY (Chine, déployé), e-Euro (BCE, en test), dollar numérique (en étude)
- Différence vs cryptos : centralisée, contrôlée, pas permissionless

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Accès universel (pas de KYC) | Risques de hacks de smart contracts |
| Transparence totale (code public) | Volatilité des actifs sous-jacents |
| Composabilité (protocoles s'empilent) | Impermanent loss pour les LP |
| Rendements potentiellement élevés | Réglementation incertaine |
| Pas d'intermédiaire, pas de censure | Complexité pour les non-initiés |

### Acteurs et solutions

| Protocole | Catégorie | Particularité |
|-----------|-----------|---------------|
| **Uniswap** | DEX (AMM) | Plus grand DEX, >1 500 Mds$ volume cumulé |
| **Aave** | Lending | Flash Loans, multi-chaînes |
| **Compound** | Lending | Pioneer du yield farming avec COMP token |
| **MakerDAO** | Stablecoin | DAI — stablecoin décentralisé, collatéralisé |
| **Curve Finance** | DEX | Optimisé pour les stablecoins, faible slippage |
| **1inch** | Agrégateur | Optimise les routes d'échange entre DEX |

### Cas d'usage concrets
- **Flash Loans** (Aave) : emprunt sans collatéral sur une seule transaction — utilisé pour l'arbitrage, mais aussi pour des attaques
- **Yield farming** sur Curve + Convex : optimisation des rendements stablecoins pour fonds institutionnels
- **e-CNY** : utilisé pour les paiements du quotidien en Chine, distribué via des wallets d'applications (WeChat Pay, Alipay)
- **DAI** : utilisé comme dollar stable décentralisé dans l'ensemble de la DeFi
- **Effondrement de Terra/UST (mai 2022)** : disparition de ~40 Mds$ en quelques jours — illustration des risques des stablecoins algorithmiques

### Chiffres et tendances
- **Hacks DeFi** : >3 Mds$ volés en 2022 (Ronin Network : 625M$, Wormhole : 320M$)
- **TVL Ethereum DeFi** : ~60% du total, reste réparti sur BNB Chain, Solana, Arbitrum
- **Réglementation MiCA (EU, 2024)** : encadre les stablecoins, impose des réserves aux émetteurs
- **RWA en DeFi** : intégration croissante d'actifs réels (bons du Trésor) comme collatéral dans les protocoles DeFi

---

## Flashcards
#flashcards

Qu'est-ce que le TVL en DeFi ? :: Total Value Locked : valeur totale des actifs déposés (bloqués en collatéral ou en liquidité) dans les smart contracts d'un protocole DeFi.

Comment fonctionne un AMM (Automated Market Maker) ? :: Il utilise des liquidity pools et une formule mathématique (ex. x × y = k) pour déterminer le prix des actifs à l'échange, sans carnet d'ordres traditionnel.

Qu'est-ce qu'un Flash Loan ? :: Prêt DeFi sans collatéral, exécuté et remboursé au sein d'une seule et même transaction blockchain — s'il n'est pas remboursé, la transaction entière est annulée.

Quelle est la différence entre un stablecoin fiat-collatéralisé et algorithmique ? :: Le fiat-collatéralisé (USDT, USDC) est adossé à des réserves en dollars réelles ; l'algorithmique maintient sa parité par algorithme, sans collatéral direct — très risqué (cf. Terra UST 2022).

Qu'est-ce qu'une CBDC ? :: Central Bank Digital Currency : monnaie numérique émise et garantie par une banque centrale, différente des cryptomonnaies car centralisée et contrôlée par l'État.

Qu'est-ce que l'impermanent loss ? :: Perte relative subie par un fournisseur de liquidité dans un AMM lorsque le prix des actifs déposés varie par rapport au moment du dépôt — perdu vs simple détention.

---

## Sources
- DeFi Pulse / DefiLlama — TVL Data (defillama.com)
- Uniswap Whitepaper v2 & v3 (uniswap.org)
- Aave Protocol Documentation
- BIS — "CBDCs: An Opportunity for the Monetary System" (2021)
- Règlement MiCA — EUR-Lex (2023)
- Chainalysis — Crypto Crime Report 2023

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[Smart Contracts]]
- [[Tokens et tokenisation]]
- [[Web3 et wallets]]
- [[Mécanismes de consensus]]
- [[Forks et évolutions de protocole]]
