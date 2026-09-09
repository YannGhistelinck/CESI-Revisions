---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Mécanismes de consensus

## En bref

### Définition
Un **mécanisme de consensus** est l'ensemble des règles permettant à des nœuds distribués — sans autorité centrale — de s'accorder sur l'état valide de la blockchain. Il garantit que tous les participants partagent le même historique de transactions, même en présence de nœuds malveillants (tolérance aux pannes byzantines).

### Pourquoi c'est important
Le consensus est le cœur de la décentralisation : il remplace la confiance en un tiers par un protocole mathématique. Le choix du mécanisme détermine la sécurité, la scalabilité, la consommation énergétique et la décentralisation du réseau.

### Chiffres clés
- **Bitcoin (PoW)** : ~150 EH/s (exahashes/seconde) de puissance de calcul (2024)
- **Ethereum (PoS post-Merge)** : ~1 million de validateurs actifs (2024), 32 ETH requis pour valider
- **The Merge (sept. 2022)** : réduction de 99,95% de la consommation d'Ethereum
- **Bitcoin halving** : tous les ~210 000 blocs (~4 ans), réduction de 50% de la récompense de minage

---

## Approfondir

### Fonctionnement

**Proof of Work (PoW) :**
- Les mineurs s'affrontent pour résoudre un puzzle cryptographique (trouver un nonce tel que le hash du bloc soit inférieur à une cible)
- La difficulté s'ajuste automatiquement pour maintenir un temps de bloc constant (~10 min pour Bitcoin)
- Le premier mineur à trouver la solution diffuse le bloc et reçoit la récompense (block reward + frais de transaction)
- Sécurité : une attaque à 51% nécessite de posséder >50% de la puissance de calcul mondiale → coût prohibitif

**Proof of Stake (PoS) :**
- Les validateurs verrouillent (stake) une quantité de cryptomonnaies comme garantie
- La probabilité d'être sélectionné pour valider un bloc est proportionnelle au montant staké
- En cas de comportement malveillant : slashing (perte partielle ou totale du stake)
- Beaucoup moins énergivore que le PoW (pas de calcul intensif)

**Delegated Proof of Stake (DPoS) :**
- Les détenteurs de tokens votent pour élire un nombre limité de délégués (witnesses/block producers)
- Seuls les délégués élus valident les blocs → plus rapide, moins décentralisé
- Utilisé par : EOS, TRON, BitShares

**Proof of Authority (PoA) :**
- Un ensemble d'autorités pré-identifiées et approuvées valident les blocs
- Très performant et efficace, mais centralisé
- Utilisé dans les blockchains d'entreprise (Quorum, VeChain) et certains testnets publics (Goerli)

**Proof of Space (PoSp) / Proof of Capacity :**
- Utilise l'espace disque disponible plutôt que la puissance de calcul
- Les mineurs pré-calculent des "plots" sur disque dur
- Utilisé par : Chia Network (XCH)

### Avantages / Inconvénients

| Mécanisme | Avantages | Inconvénients |
|-----------|-----------|---------------|
| **PoW** | Sécurité prouvée, décentralisation | Consommation énergétique massive, lent |
| **PoS** | Éco-responsable, scalable | Risque de centralisation (gros stakers), "rien n'est en jeu" |
| **DPoS** | Très rapide, peu énergivore | Centralisation autour des délégués élus |
| **PoA** | Performance maximale | Totalement centralisé, non permissionless |
| **PoSp** | Moins énergivore que PoW | Surconsommation de disques SSD, moins testé |

### Acteurs et solutions

| Blockchain | Consensus | Particularité |
|------------|-----------|---------------|
| **Bitcoin** | PoW (SHA-256) | Référence en termes de sécurité |
| **Ethereum** | PoS (post-Merge 2022) | ~1M validateurs, 32 ETH de stake minimum |
| **Cardano** | PoS (Ouroboros) | Consensus PoS formellement prouvé |
| **Solana** | PoH + PoS | Proof of History : horodatage cryptographique, ~65 000 tx/s |
| **EOS / TRON** | DPoS | 21 block producers élus |
| **Hyperledger Fabric** | PBFT / Raft | Consensus d'entreprise, pas de mining |

**Halving Bitcoin :**
- Récompense initiale : 50 BTC/bloc (2009)
- 2012 : 25 BTC | 2016 : 12,5 BTC | 2020 : 6,25 BTC | **2024 : 3,125 BTC**
- Prochain halving : ~2028 (1,5625 BTC)
- Objectif : limiter l'inflation, plafond de 21 millions de BTC

### Cas d'usage concrets
- **Bitcoin (PoW)** : stockage de valeur, "or numérique", sécurité maximale
- **Ethereum (PoS)** : smart contracts, DeFi, NFT — transition exemplaire vers un consensus vert
- **Solana (PoH+PoS)** : applications nécessitant un débit élevé (jeux, NFTs, paiements)
- **Hyperledger (PBFT)** : supply chain, finance d'entreprise

### Chiffres et tendances
- **Consommation Bitcoin** : ~120-150 TWh/an (comparable à l'Argentine)
- **Consommation Ethereum (post-Merge)** : ~0,01 TWh/an
- **Solana** : ~65 000 transactions/seconde théoriques, ~2 000 en pratique
- **Seuil de tolérance Byzantine** : PBFT tolère jusqu'à (n-1)/3 nœuds malveillants

---

## Flashcards
#flashcards

Qu'est-ce que le Proof of Work ? :: Un mécanisme de consensus où les mineurs s'affrontent pour résoudre un puzzle cryptographique (trouver un nonce valide), consommant de l'énergie pour sécuriser le réseau.

Qu'est-ce que le slashing dans le Proof of Stake ? :: La pénalité appliquée à un validateur PoS qui se comporte de manière malveillante ou incorrecte — il perd une partie ou la totalité de son stake.

Quelle est la différence entre PoS et DPoS ? :: Dans le PoS, tous les stakers peuvent être sélectionnés pour valider ; dans le DPoS, les stakers votent pour élire un nombre limité de délégués qui valident à leur place.

Qu'est-ce que le halving Bitcoin et quand a-t-il lieu ? :: Tous les ~210 000 blocs (~4 ans), la récompense de minage est divisée par 2. En avril 2024 : passage de 6,25 à 3,125 BTC/bloc.

Qu'est-ce que "The Merge" d'Ethereum ? :: La transition d'Ethereum du Proof of Work au Proof of Stake en septembre 2022, réduisant sa consommation énergétique de 99,95%.

Quel est le principal avantage du PoA (Proof of Authority) ? :: Performance et efficacité maximales, car un ensemble restreint de validateurs pré-approuvés valident les blocs sans calcul intensif. Inconvénient : centralisation totale.

---

## Sources
- Bitcoin Whitepaper — Nakamoto, S. (2008)
- Ethereum Foundation — "The Merge" documentation (2022)
- Cardano — Ouroboros Protocol Paper (IOHK)
- Cambridge Centre for Alternative Finance — Bitcoin Electricity Consumption Index
- Investopedia — "Proof of Stake vs Proof of Work"

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[Forks et évolutions de protocole]]
- [[Smart Contracts]]
- [[Blockchains d'entreprise]]
- [[DeFi (Finance décentralisée)]]
