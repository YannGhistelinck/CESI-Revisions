---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Blockchain — fondamentaux

## En bref

### Définition
Une **blockchain** est une base de données distribuée et décentralisée, structurée en blocs de données chaînés par des fonctions de hachage cryptographiques. Elle constitue un type de **DLT** (Distributed Ledger Technology) — un registre partagé et répliqué sur un réseau de nœuds sans autorité centrale.

### Pourquoi c'est important
La blockchain permet des échanges de valeur et d'information sans tiers de confiance (banque, notaire, État), garantissant l'intégrité et l'immutabilité des données grâce à des mécanismes cryptographiques. Elle est au cœur des cryptomonnaies, des smart contracts et de la tokenisation d'actifs.

### Chiffres clés
- **2008** : publication du whitepaper de Bitcoin par Satoshi Nakamoto
- **~19 000** nœuds actifs sur le réseau Bitcoin (2024)
- **Marché global blockchain** : ~28 Mds$ en 2024, projections ~825 Mds$ en 2032
- **Bitcoin** : ~210 000 blocs minés par cycle de halving (≈ 4 ans)

---

## Approfondir

### Fonctionnement

1. **Transaction initiée** : un utilisateur diffuse une transaction signée numériquement sur le réseau.
2. **Propagation aux nœuds** : les nœuds (ordinateurs participant au réseau) valident la transaction et la relaient.
3. **Regroupement en bloc** : les mineurs/validateurs regroupent les transactions en attente (mempool) dans un bloc.
4. **Consensus** : le réseau s'accorde sur le bloc valide via un mécanisme de consensus (PoW, PoS…).
5. **Ajout à la chaîne** : le bloc validé est ajouté à la chaîne et diffusé à tous les nœuds.
6. **Immutabilité** : modifier un bloc invaliderait tous les blocs suivants (changement de hash).

**Structure d'un bloc :**
- En-tête : hash du bloc précédent, nonce, timestamp, racine de Merkle
- Corps : liste des transactions

**Hash cryptographique (SHA-256 pour Bitcoin) :**
- Fonction à sens unique : impossible de retrouver l'entrée à partir de la sortie
- Déterministe : même entrée → même hash
- Effet avalanche : 1 bit modifié = hash totalement différent

**Merkle Tree :**
- Arbre binaire de hachages permettant de résumer toutes les transactions d'un bloc en une seule valeur (Merkle Root)
- Permet de vérifier l'inclusion d'une transaction sans télécharger tout le bloc (SPV — Simplified Payment Verification)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Décentralisation : pas de point de défaillance unique | Scalabilité limitée (ex. Bitcoin : ~7 tx/s) |
| Immutabilité et auditabilité des données | Consommation énergétique élevée (PoW) |
| Transparence (blockchains publiques) | Irréversibilité des transactions (erreurs permanentes) |
| Résistance à la censure | Complexité technique d'implémentation |
| Élimination des intermédiaires | Problème du trilemme : sécurité / décentralisation / scalabilité |

### Acteurs et solutions

| Acteur | Rôle |
|--------|------|
| **Bitcoin** | 1ère blockchain publique, référence pour la décentralisation |
| **Ethereum** | 2ème blockchain publique, pionnière des smart contracts |
| **Hyperledger** | Frameworks blockchain d'entreprise (Linux Foundation) |
| **Chainlink** | Infrastructure d'oracles décentralisés |
| **Consensys** | Studio de développement sur Ethereum (MetaMask, Infura) |

**Types de nœuds :**
- **Nœud complet (full node)** : stocke l'intégralité de la blockchain, valide toutes les transactions
- **Nœud léger (light node / SPV)** : ne stocke que les en-têtes de blocs, fait confiance aux full nodes
- **Mineur** (PoW) : nœud qui résout le puzzle cryptographique pour créer un bloc
- **Validateur** (PoS) : nœud qui verrouille (stake) des cryptos pour participer à la validation

### Cas d'usage concrets
- **Finance** : transferts internationaux (Ripple/XRP), paiements Bitcoin
- **Traçabilité** : suivi de chaîne d'approvisionnement (Walmart + IBM Food Trust)
- **Identité numérique** : identité auto-souveraine (SSI)
- **Cadastre** : registres fonciers immutables (projet en Géorgie, Honduras)
- **Santé** : partage sécurisé de dossiers médicaux

### Chiffres et tendances
- **Taille de la blockchain Bitcoin** : ~600 Go (2024)
- **Temps de bloc Bitcoin** : ~10 minutes ; Ethereum : ~12 secondes
- **Trilemme blockchain** (Vitalik Buterin) : impossible d'atteindre simultanément décentralisation, sécurité ET scalabilité maximales
- **51% attack** : un attaquant contrôlant >50% de la puissance de calcul peut réécrire l'historique récent

---

## Flashcards
#flashcards/Blockchain/Blockchain_fondamentaux

Qu'est-ce qu'une blockchain ? :: Base de données distribuée, décentralisée, structurée en blocs chaînés par hachage cryptographique, sans autorité centrale.

Quelle est la différence entre DLT et blockchain ? :: La blockchain est un type de DLT (registre distribué), mais tous les DLT ne sont pas des blockchains (ex. DAG d'IOTA).

Quel est le rôle du Merkle Tree dans un bloc ? :: Résumer toutes les transactions du bloc en une seule valeur (Merkle Root), permettant la vérification rapide d'une transaction sans télécharger tout le bloc.

Qu'est-ce que l'immutabilité dans une blockchain ? :: Une fois un bloc confirmé, il est pratiquement impossible de le modifier sans invalider tous les blocs suivants, car chaque bloc contient le hash du précédent.

Qu'est-ce que le trilemme blockchain ? :: Concept de Vitalik Buterin : impossible d'atteindre simultanément décentralisation maximale, sécurité maximale et scalabilité maximale.

Quelle est la différence entre un mineur et un validateur ? :: Un mineur (PoW) résout un puzzle mathématique pour créer un bloc ; un validateur (PoS) verrouille des cryptos comme garantie pour participer à la validation.

Qu'est-ce qu'une attaque à 51% ? :: Un attaquant contrôlant plus de 50% de la puissance de calcul (PoW) ou du stake (PoS) peut tenter de réécrire l'historique récent de la blockchain.

---

## Sources
- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. bitcoin.org
- Buterin, V. (2014). *Ethereum Whitepaper*. ethereum.org
- Antonopoulos, A. (2017). *Mastering Bitcoin*. O'Reilly
- Banque de France — Publications sur les technologies DLT
- Grand View Research — Blockchain Market Size Report (2024)

---

## Notions liées
- [[Mécanismes de consensus]]
- [[Smart Contracts]]
- [[Forks et évolutions de protocole]]
- [[Tokens et tokenisation]]
- [[DeFi (Finance décentralisée)]]
- [[Web3 et wallets]]
- [[Blockchains d'entreprise]]
- [[Chiffrement et gestion des clés]]
