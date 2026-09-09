---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Web3 et wallets

## En bref

### Définition
Le **Web3** désigne la vision d'un internet décentralisé, où les utilisateurs contrôlent leurs données et actifs numériques grâce à la blockchain, sans dépendre de plateformes centralisées (GAFAM). Un **wallet** (portefeuille crypto) est un outil gérant les clés cryptographiques privées d'un utilisateur — c'est la porte d'entrée vers le Web3. La **seed phrase** (phrase mnémotechnique de 12 ou 24 mots) permet de régénérer toutes les clés d'un wallet.

### Pourquoi c'est important
Le wallet est l'identité numérique de l'utilisateur Web3 : il lui permet de signer des transactions, interagir avec des DApps, détenir des tokens et NFTs sans intermédiaire. La seed phrase est la clé maîtresse — sa compromission entraîne la perte irréversible de tous les actifs.

### Chiffres clés
- **MetaMask** : ~30 millions d'utilisateurs actifs mensuels (2022, pic)
- **Adresses Ethereum actives** : >250 millions d'adresses créées (2024)
- **Pertes liées aux seed phrases compromises** : des centaines de millions $ par an
- **Web3** : terme popularisé par Gavin Wood (co-fondateur Ethereum) en 2014

---

## Approfondir

### Fonctionnement

**Web1 → Web2 → Web3 :**
| Génération | Caractéristiques | Exemples |
|------------|-----------------|---------|
| Web1 (~1990-2004) | Statique, lecture seule | Sites HTML, annuaires |
| Web2 (~2004-présent) | Interactif, plateformes centralisées | Facebook, Google, YouTube |
| Web3 (émergent) | Décentralisé, propriété des données, blockchain | Uniswap, ENS, Lens Protocol |

**Cryptographie asymétrique (base des wallets) :**
- **Clé privée** : nombre aléatoire de 256 bits, gardée secrète par l'utilisateur → permet de signer les transactions
- **Clé publique** : dérivée de la clé privée (courbe elliptique ECDSA), partageable
- **Adresse** : hash de la clé publique (ex. 0x1234...abcd sur Ethereum) → identifiant public
- Le wallet ne "contient" pas de cryptos : il contient les clés permettant de prouver la propriété des fonds enregistrés sur la blockchain

**Seed phrase (BIP-39) :**
- Séquence de 12 ou 24 mots tirés d'une liste standardisée de 2048 mots
- Génère de manière déterministe toutes les clés privées d'un wallet HD (Hierarchical Deterministic)
- Standard BIP-32/44 : une seed génère une arborescence infinie de paires de clés
- **Règle d'or** : ne jamais la stocker numériquement, jamais la communiquer, jamais la photographier

**Types de wallets :**
| Type | Description | Sécurité | Praticité | Exemples |
|------|-------------|----------|-----------|---------|
| **Hot wallet (logiciel)** | Connecté à internet, clés en ligne | Moyen | Élevée | MetaMask, Trust Wallet |
| **Cold wallet (hardware)** | Hors ligne, clés sur appareil physique | Élevée | Faible | Ledger, Trezor |
| **Paper wallet** | Clés imprimées sur papier | Très élevée (si sécurisé) | Très faible | QR code généré hors ligne |
| **Custodial wallet** | Clés gérées par un tiers (exchange) | Dépend du tiers | Très élevée | Coinbase, Binance |

**"Not your keys, not your coins" :**
- Si les clés privées sont détenues par un exchange (Binance, FTX…), l'utilisateur ne contrôle pas réellement ses actifs
- FTX (novembre 2022) : faillite de l'exchange → ~8 Mds$ de fonds clients inaccessibles
- Recommandation : auto-custody via wallet non-custodial pour les actifs importants

**ENS (Ethereum Name Service) :**
- Système de noms de domaine décentralisé sur Ethereum
- Permet de remplacer une adresse complexe (0x1234…) par un nom lisible (ex. vitalik.eth)
- Analogue au DNS, mais on-chain et décentralisé

**Identité décentralisée (DID / SSI) :**
- DID (Decentralized Identifier) : identifiant numérique auto-souverain, non contrôlé par un tiers
- SSI (Self-Sovereign Identity) : l'utilisateur contrôle ses propres données d'identité
- Standards W3C DID, protocoles : Ceramic, SpruceID

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Contrôle total de ses actifs | Responsabilité totale (perte de seed = perte d'actifs) |
| Pseudonymat | Complexité pour les non-initiés |
| Interopérabilité (1 wallet = N DApps) | UX mauvaise comparée au Web2 |
| Pas de censure | Phishing et arnaques très répandus |
| Identité portable | Scalabilité et vitesse encore limitées |

### Acteurs et solutions

| Acteur | Solution | Rôle |
|--------|----------|------|
| **MetaMask (Consensys)** | Hot wallet navigateur + mobile | Standard de facto Web3 |
| **Ledger** | Hardware wallet | Sécurité maximale, leader du marché |
| **Trezor** | Hardware wallet | Alternative open-source à Ledger |
| **Rainbow / Rabby** | Hot wallets alternatifs | UX améliorée |
| **Coinbase Wallet** | Non-custodial + intégration exchange | Pont entre CeFi et DeFi |
| **ENS Domains** | Noms de domaine Ethereum | Identité lisible Web3 |

### Cas d'usage concrets
- **Sign-in with Ethereum (SIWE)** : se connecter à un site web en signant un message avec son wallet, sans mot de passe ni compte centralisé
- **Lens Protocol** : réseau social décentralisé où le profil (followers, posts) appartient à l'utilisateur via NFT
- **ENS** : vitalik.eth utilisé comme adresse de réception, nom de profil Web3
- **Phishing MetaMask** : attaques visant à récupérer la seed phrase via faux sites ou extensions malveillantes — vecteur d'attaque #1
- **Account Abstraction (EIP-4337)** : wallets "smart contract" permettant de récupérer l'accès sans seed phrase, de payer les frais en stablecoins

### Chiffres et tendances
- **FTX (nov. 2022)** : faillite illustrant les risques des wallets custodiaux — ~8 Mds$ de pertes clients
- **Ledger** : >6 millions de hardware wallets vendus (2024)
- **Account Abstraction** (EIP-4337, déployé 2023) : révolution UX pour les wallets — wallets programmables, récupération sociale, paiement de gas en stablecoins
- **Adoption Web3** : ~420 millions de détenteurs de cryptos dans le monde (2023, Triple-A Research)

---

## Flashcards
#flashcards

Quelle est la différence entre un wallet custodial et non-custodial ? :: Dans un wallet custodial (ex. Coinbase), les clés privées sont gérées par l'exchange ; dans un non-custodial (ex. MetaMask), l'utilisateur détient lui-même ses clés ("not your keys, not your coins").

Qu'est-ce qu'une seed phrase et pourquoi est-elle critique ? :: Séquence de 12 ou 24 mots permettant de régénérer toutes les clés privées d'un wallet HD. Sa compromission entraîne la perte irréversible de tous les actifs associés.

Le wallet stocke-t-il des cryptomonnaies ? :: Non. Le wallet stocke les clés privées permettant de prouver la propriété des fonds. Les cryptos existent sur la blockchain, pas dans le wallet.

Quelle est la différence entre Web2 et Web3 ? :: Le Web2 repose sur des plateformes centralisées (GAFAM) contrôlant les données des utilisateurs ; le Web3 vise un internet décentralisé basé sur la blockchain, où l'utilisateur contrôle ses données et actifs.

Qu'est-ce que l'ENS (Ethereum Name Service) ? :: Système de noms de domaine décentralisé sur Ethereum permettant d'associer un nom lisible (ex. vitalik.eth) à une adresse blockchain complexe.

Qu'est-ce que l'Account Abstraction (EIP-4337) ? :: Standard Ethereum permettant de créer des wallets "smart contract" avec des fonctionnalités avancées : récupération sociale, paiement du gas en stablecoins, transactions groupées.

---

## Sources
- Wood, G. (2014). "ĐApps: What Web 3.0 Looks Like" — gavwood.com
- MetaMask — Documentation officielle (metamask.io)
- Ledger — Security Model Documentation
- W3C — Decentralized Identifiers (DID) Specification
- EIP-4337 — Account Abstraction (eips.ethereum.org)
- Triple-A Research — Global Crypto Ownership Report (2023)

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[Smart Contracts]]
- [[DeFi (Finance décentralisée)]]
- [[Tokens et tokenisation]]
- [[Chiffrement et gestion des clés]]
