---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Blockchains d'entreprise

## En bref

### Définition
Une **blockchain permissionnée** (ou privée/de consortium) est un réseau blockchain dont l'accès est restreint à des participants autorisés, contrairement aux blockchains publiques. **Hyperledger Fabric** (Linux Foundation), **R3 Corda**, **Quorum** (JPMorgan, fork Ethereum privé) et **VeChain** sont les principales solutions d'entreprise. Le **BaaS** (Blockchain as a Service) permet aux entreprises de déployer des blockchains sans gérer l'infrastructure.

### Pourquoi c'est important
Les entreprises ont des contraintes que les blockchains publiques ne satisfont pas : confidentialité des transactions, conformité réglementaire (RGPD), performances élevées, gouvernance contrôlée. Les blockchains d'entreprise offrent les bénéfices de la DLT (traçabilité, immutabilité, automatisation) sans les inconvénients des réseaux publics (volatilité, consommation, anonymat).

### Chiffres clés
- **Marché blockchain d'entreprise** : ~11 Mds$ en 2024, projections ~470 Mds$ en 2030
- **Hyperledger Fabric** : utilisé par IBM, Walmart, Maersk, plus de 400 membres de la Linux Foundation
- **VeChain** : >200 entreprises partenaires, dont LVMH, BMW, Walmart China
- **BaaS** : proposé par AWS (Amazon Managed Blockchain), Microsoft Azure, IBM Blockchain Platform

---

## Approfondir

### Fonctionnement

**Taxonomie des blockchains :**
| Type | Accès | Validation | Exemples |
|------|-------|------------|---------|
| **Publique** | Ouvert à tous | Tout nœud peut valider | Bitcoin, Ethereum |
| **Privée** | Contrôlé par une entité | Seuls les nœuds autorisés valident | Hyperledger Fabric (cas d'usage interne) |
| **Consortium / Permissionnée** | Groupe d'organisations | Membres du consortium valident | R3 Corda, Quorum |
| **Hybride** | Mix public/privé | Partiel | Dragonchain |

**Hyperledger Fabric :**
- Framework open-source sous la Linux Foundation (contribué par IBM)
- Architecture modulaire : consensus (Raft, PBFT), MSP (Membership Service Provider) pour l'identité, chaincode (smart contracts en Go, Java, Node.js)
- Canaux (channels) : sous-réseaux permettant des transactions privées entre sous-ensembles de membres
- Pas de cryptomonnaie native → purement B2B
- Utilisateurs : IBM Food Trust (traçabilité alimentaire), TradeLens (Maersk, ports mondiaux)

**R3 Corda :**
- Conçu spécifiquement pour la finance et les contrats légaux
- Pas de blockchain globale : seules les parties concernées par une transaction voient ses données (confidentialité totale)
- Flows : automatisation des processus multi-parties
- Utilisateurs : >300 banques et institutions financières (BNP Paribas, HSBC, SEB)
- Cas d'usage : règlement de titres, financement du commerce international (trade finance)

**Quorum (ConsenSys) :**
- Fork d'Ethereum adapté pour les entreprises (créé par JPMorgan en 2016, cédé à Consensys en 2020)
- Compatibilité EVM : smart contracts Solidity réutilisables
- Transactions privées : via Tessera (gestionnaire de données privées)
- Consensus : IBFT (Istanbul Byzantine Fault Tolerance) ou Raft
- Utilisateurs : JPMorgan (Interbank Information Network, devenu Liink), Covantis (négoce agricole)

**VeChain :**
- Blockchain publique permissionnée orientée supply chain et IoT
- VeChainThor : deux tokens — VET (valeur/paiements) et VTHO (gas/frais de transaction)
- Mécanisme de consensus : PoA (Proof of Authority) avec 101 master nodes
- Identifiants NFC/RFID/QR connectés à la blockchain pour traçabilité physique
- Utilisateurs : LVMH (anti-contrefaçon), BMW (données véhicules), Walmart China (sécurité alimentaire)

**BaaS (Blockchain as a Service) :**
- Service cloud gérant l'infrastructure blockchain (nœuds, réseau, mises à jour)
- L'entreprise se concentre sur la logique métier (chaincode, smart contracts)
- Offres principales :
  - **Amazon Managed Blockchain** : Hyperledger Fabric + Ethereum
  - **Azure Blockchain Service** (arrêté 2021, migré vers ConsenSys Quorum)
  - **IBM Blockchain Platform** : basé sur Hyperledger Fabric
  - **Oracle Blockchain Platform** : Hyperledger Fabric

### Avantages / Inconvénients

| Aspect | Blockchains d'entreprise | Blockchains publiques |
|--------|--------------------------|----------------------|
| **Performances** | Élevées (>1 000 tx/s) | Limitées (7-4000 tx/s) |
| **Confidentialité** | Transactions privées possibles | Transparence totale |
| **Gouvernance** | Contrôlée et réglementable | Décentralisée, communautaire |
| **Conformité** | RGPD, KYC/AML intégrables | Difficile (pseudonymat) |
| **Décentralisation** | Limitée (consortium) | Maximale |
| **Coût** | Prévisible (pas de gas volatil) | Variable (gas fees) |

### Acteurs et solutions

| Solution | Fondateur/Éditeur | Secteurs cibles |
|----------|-------------------|-----------------|
| **Hyperledger Fabric** | IBM / Linux Foundation | Supply chain, santé, finance |
| **R3 Corda** | R3 (consortium bancaire) | Finance, assurance, trade finance |
| **Quorum** | JPMorgan → ConsenSys | Finance, banque, énergie |
| **VeChain** | VeChain Foundation | Supply chain, luxe, automobile |
| **DAML (Digital Asset)** | Digital Asset | Finance, marchés de capitaux |
| **Stellar** | Stellar Foundation | Paiements internationaux, inclusion financière |

### Cas d'usage concrets
- **IBM Food Trust (Hyperledger Fabric)** : Walmart réduit de 7 jours à 2,2 secondes le traçage d'une mangue du champ à l'étal
- **TradeLens (Maersk + IBM)** : digitisation du commerce maritime — intégration de >175 acteurs (ports, douanes, transporteurs) [arrêté en 2022 faute d'adoption]
- **Interbank Information Network (JPMorgan/Quorum)** : résolution de rejets de paiements entre banques, désormais intégré dans Liink
- **LVMH (VeChain)** : certificats d'authenticité numériques pour les produits de luxe (Aura Blockchain Consortium)
- **Projet Jura (BNS + BCE)** : règlement DvP (Delivery vs Payment) de titres entre banques centrales via DLT

### Chiffres et tendances
- **Aura Blockchain Consortium** (LVMH, Prada, Richemont) : >40 millions de produits de luxe trackés (2024)
- **Trade Finance** : marché de 9 000 Mds$/an, encore très papier — R3 Corda cible ce marché
- **Marco Polo Network** (R3 Corda) : réseau de financement commercial impliquant +30 banques mondiales
- **Tendance 2024** : convergence blockchain publique/privée (ex. Polygon pour entreprises, tokenisation RWA sur Ethereum)

---

## Flashcards
#flashcards/Blockchain/Blockchains_d_entreprise

Quelle est la différence entre une blockchain publique et permissionnée ? :: Une blockchain publique est ouverte à tous (Bitcoin, Ethereum) ; une blockchain permissionnée restreint l'accès et la validation à des participants autorisés — offrant plus de confidentialité et de performance.

Qu'est-ce qu'Hyperledger Fabric et qui en est à l'origine ? :: Framework open-source de blockchain d'entreprise développé par IBM et contribué à la Linux Foundation. Il utilise des canaux (channels) pour isoler les transactions entre sous-groupes de membres.

En quoi R3 Corda diffère-t-il des autres blockchains ? :: Corda ne partage les transactions qu'entre les parties directement concernées (pas de ledger global) — garantissant une confidentialité maximale, clé pour la finance et les contrats légaux.

Qu'est-ce que Quorum et quelle est son origine ? :: Fork d'Ethereum créé par JPMorgan en 2016, cédé à ConsenSys en 2020. Compatible EVM (smart contracts Solidity), il ajoute des transactions privées et un consensus adapté aux entreprises.

Qu'est-ce que le BaaS (Blockchain as a Service) ? :: Service cloud permettant aux entreprises de déployer et gérer des blockchains sans gérer l'infrastructure sous-jacente. Proposé par AWS, IBM, Microsoft.

Quel est le cas d'usage d'IBM Food Trust avec Walmart ? :: Grâce à Hyperledger Fabric, Walmart peut tracer l'origine d'une mangue en 2,2 secondes au lieu de 7 jours, en interrogeant un registre partagé entre tous les acteurs de la chaîne alimentaire.

---

## Sources
- Hyperledger Foundation — Documentation Fabric (hyperledger.org)
- R3 — Corda Documentation (docs.r3.com)
- ConsenSys — Quorum Documentation
- VeChain Foundation — Whitepaper (vechain.org)
- IBM — "Food Trust: Blockchain for the World's Food Supply" (2018)
- Gartner — "Hype Cycle for Blockchain and Web3" (2023)
- Markets and Markets — Enterprise Blockchain Market Report (2024)

---

## Notions liées
- [[Blockchain — fondamentaux]]
- [[Mécanismes de consensus]]
- [[Smart Contracts]]
- [[Tokens et tokenisation]]
- [[DeFi (Finance décentralisée)]]
- [[Data Governance]]
- [[RGPD]]
