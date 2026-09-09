---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Forks et évolutions de protocole

## En bref

### Définition
Un **fork** désigne une modification des règles du protocole d'une blockchain. Un **hard fork** est une modification incompatible avec les anciennes versions (scission possible de la chaîne) ; un **soft fork** est une modification rétrocompatible. Les notions de **layer 1** (protocole de base) et **layer 2** (solutions superposées) permettent d'aborder la scalabilité sans modifier le cœur du réseau.

### Pourquoi c'est important
L'évolutivité des blockchains publiques est un défi majeur : Bitcoin traite ~7 transactions/seconde, contre 24 000 pour Visa. Les forks et les layers 2 sont les deux grandes stratégies pour faire évoluer un protocole tout en préservant (ou non) la communauté existante.

### Chiffres clés
- **Bitcoin Cash (2017)** : hard fork de Bitcoin augmentant la taille des blocs de 1 Mo à 8 Mo
- **The Merge (2022)** : soft fork/upgrade majeur d'Ethereum (PoW → PoS), réduction de ~99,95% de la consommation énergétique
- **Lightning Network** : capacité de plusieurs millions de transactions/seconde en théorie, ~5 000 BTC de capacité (2024)
- **Ethereum** : taille des blocs variable, ~1,2 million de transactions/jour (2024)

---

## Approfondir

### Fonctionnement

**Hard Fork :**
1. Des développeurs proposent une modification incompatible du protocole (ex. augmentation de la taille des blocs).
2. Les nœuds qui adoptent le nouveau protocole et ceux qui gardent l'ancien divergent.
3. Deux chaînes distinctes coexistent (ex. Bitcoin / Bitcoin Cash).
4. Les détenteurs de l'ancienne cryptomonnaie reçoivent l'équivalent sur la nouvelle chaîne.

**Soft Fork :**
1. Modification rétrocompatible : les anciens nœuds continuent d'accepter les nouveaux blocs.
2. Pas de scission de chaîne si une majorité de mineurs/validateurs adopte la mise à jour.
3. Exemple : SegWit (2017) sur Bitcoin — réorganisation des données de transaction pour augmenter la capacité.

**Layer 1 :**
- La blockchain principale (Bitcoin, Ethereum, Solana…)
- Toute modification passe par un fork du protocole de base
- Limites : scalabilité, décentralisation, sécurité (trilemme)

**Layer 2 :**
- Solutions construites au-dessus du layer 1, héritant de sa sécurité
- Traitent les transactions hors-chaîne (off-chain) et ne soumettent que le résultat au layer 1
- Exemples : Lightning Network (Bitcoin), Rollups (Ethereum — Optimism, Arbitrum)

**Types de Layer 2 (Ethereum) :**
| Type | Fonctionnement | Exemples |
|------|----------------|---------|
| State Channels | Canal de paiement bilatéral | Lightning Network |
| Rollups Optimistes | Exécute off-chain, suppose la validité, délai de contestation | Optimism, Arbitrum |
| ZK-Rollups | Preuve cryptographique de validité (zero-knowledge) | zkSync, StarkNet |
| Plasma | Chaînes enfants rattachées au layer 1 | OMG Network |

### Avantages / Inconvénients

| Aspect | Avantages | Inconvénients |
|--------|-----------|---------------|
| **Hard Fork** | Liberté d'innovation, nouvelles fonctionnalités majeures | Scission de la communauté, duplication des actifs, confusion |
| **Soft Fork** | Pas de scission, rétrocompatible | Modifications limitées, consensus difficile à atteindre |
| **Layer 2** | Scalabilité sans toucher au layer 1, frais réduits | Complexité, risques propres (bugs de smart contracts) |

### Acteurs et solutions

| Acteur | Solution | Type |
|--------|----------|------|
| Lightning Labs | Lightning Network | L2 Bitcoin — State Channels |
| Optimism Foundation | Optimism (OP Mainnet) | L2 Ethereum — Rollup Optimiste |
| Offchain Labs | Arbitrum | L2 Ethereum — Rollup Optimiste |
| Matter Labs | zkSync | L2 Ethereum — ZK-Rollup |
| StarkWare | StarkNet | L2 Ethereum — ZK-Rollup |
| Polygon | Polygon PoS, zkEVM | L2 Ethereum — Sidechain + ZK-Rollup |

### Cas d'usage concrets
- **Lightning Network** : paiements Bitcoin quasi-instantanés et à très faibles frais (El Salvador, Strike)
- **Arbitrum / Optimism** : utilisation massive pour la DeFi (Uniswap, Aave) à des frais inférieurs à Ethereum mainnet
- **The Merge (Ethereum, sept. 2022)** : passage de PoW à PoS sans hard fork destructeur — réduction de 99,95% de la consommation
- **Bitcoin Cash (2017)** : hard fork controversé pour augmenter la capacité de transaction, soutenu par Roger Ver

### Chiffres et tendances
- **SegWit (2017)** : adoption par ~85% des transactions Bitcoin en 2024
- **Rollups Ethereum** : réduction des frais de transaction de 10x à 100x par rapport au mainnet
- **TVL (Total Value Locked) en L2** : ~40 Mds$ (2024), dominé par Arbitrum et Optimism
- **Ethereum Danksharding** (EIP-4844 / Proto-Danksharding) : upgrade 2024 visant à réduire davantage le coût des rollups

---

## Flashcards
#flashcards

Quelle est la différence entre un hard fork et un soft fork ? :: Un hard fork est une modification incompatible pouvant créer deux chaînes distinctes ; un soft fork est rétrocompatible, les anciens nœuds acceptent toujours les nouveaux blocs.

Qu'est-ce qu'un Layer 2 ? :: Une solution construite au-dessus d'une blockchain (layer 1) qui traite des transactions hors-chaîne pour améliorer la scalabilité, tout en héritant de la sécurité du layer 1.

Donnez un exemple de hard fork célèbre et son origine. :: Bitcoin Cash (août 2017), né d'un désaccord sur la taille des blocs : les partisans d'une augmentation à 8 Mo ont forké Bitcoin.

Comment fonctionne le Lightning Network ? :: Il crée des canaux de paiement bidirectionnels entre deux parties, permettant des transactions off-chain quasi-instantanées ; seul l'ouverture et la fermeture du canal sont enregistrées sur Bitcoin.

Quelle est la différence entre un ZK-Rollup et un Rollup Optimiste ? :: Le ZK-Rollup fournit une preuve cryptographique de validité immédiate ; le Rollup Optimiste suppose la validité et laisse un délai (7 jours) pour contester.

Qu'est-ce que The Merge pour Ethereum ? :: La transition d'Ethereum du Proof of Work vers le Proof of Stake en septembre 2022, réduisant la consommation énergétique de ~99,95%.

---

## Sources
- Lightning Network Whitepaper — Poon, J. & Dryja, T. (2016)
- Ethereum Foundation — Documentation sur les Layer 2 (l2beat.com)
- Coindesk — "Bitcoin Cash Hard Fork Explained"
- L2BEAT.com — TVL et statistiques Layer 2
- EIP-4844 (Proto-Danksharding) — ethereum.org

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[Mécanismes de consensus]]
- [[Smart Contracts]]
- [[DeFi (Finance décentralisée)]]
- [[Tokens et tokenisation]]
