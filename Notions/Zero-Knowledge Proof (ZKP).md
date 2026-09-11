---
type: notion
thèmes:
  - Blockchain
  - Cybersécurité
statut: pas vu
dernière_révision: null
---

# Zero-Knowledge Proof (ZKP)

## En bref

Un Zero-Knowledge Proof (ZKP), ou preuve à divulgation nulle de connaissance, est un protocole cryptographique permettant à une partie (le prouveur) de convaincre une autre partie (le vérificateur) qu'elle possède une information ou satisfait une condition, **sans jamais révéler l'information elle-même**. Le ZKP constitue un outil fondamental pour concilier deux impératifs antagonistes : **transparence** et **confidentialité**, aussi bien en cybersécurité que dans les systèmes blockchain.

---

## Approfondir

### Fonctionnement

Un ZKP doit satisfaire trois propriétés :
1. **Complétude** : si l'énoncé est vrai, un prouveur honnête convaincra toujours le vérificateur.
2. **Solidité (Soundness)** : si l'énoncé est faux, aucun prouveur malhonnête ne peut convaincre le vérificateur (sauf avec une probabilité négligeable).
3. **Divulgation nulle (Zero-Knowledge)** : le vérificateur n'apprend rien de plus que le simple fait que l'énoncé est vrai.

**Analogie classique — La grotte d'Ali Baba** : Peggy connaît le mot de passe d'une grotte en anneau. Victor veut le vérifier. Peggy entre par un couloir et ressort par l'autre sur demande de Victor, prouvant qu'elle connaît le passage secret, sans jamais révéler le mot.

**Types principaux de ZKP** :

- **ZK-SNARKs** (Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge) :
  - Preuves très compactes et rapides à vérifier.
  - Nécessitent une phase de setup de confiance (trusted setup — cérémonie MPC).
  - Utilisés dans Zcash (confidentialité des transactions) et les rollups ZK d'Ethereum.

- **ZK-STARKs** (Zero-Knowledge Scalable Transparent Arguments of Knowledge) :
  - Pas de trusted setup (transparent setup via hash functions).
  - Résistants aux ordinateurs quantiques.
  - Preuves plus volumineuses mais plus scalables.
  - Utilisés par StarkWare / StarkNet.

- **PLONK, Groth16, Nova** : variantes de ZK-SNARKs avec différents compromis perf/taille.

**Applications blockchain** :
- **ZK-Rollups** : regroupent des centaines de transactions off-chain, génèrent une preuve ZK de validité, soumise on-chain. Scalabilité sans sacrifier la sécurité. Ex. : zkSync, StarkNet, Polygon zkEVM, Scroll.
- **Transactions privées** : Zcash (shielded transactions), Tornado Cash (mélangeur — sanctionné par l'OFAC en 2022).
- **Identité et credentials** : prouver qu'on est majeur sans révéler sa date de naissance (ZKP + SSI).
- **Compliance sans révélation** : prouver à un régulateur qu'on respecte une règle (ex. solvabilité) sans révéler les données brutes.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Confidentialité maximale des données | Complexité mathématique élevée (courbes elliptiques, théorie des champs) |
| Vérification sans révélation de l'information | Coût de calcul élevé pour générer les preuves (prouveur) |
| Scalabilité des blockchains (ZK-Rollups) | Trusted setup = point de vulnérabilité potentielle (ZK-SNARKs) |
| Résistance quantique possible (ZK-STARKs) | Taille des preuves STARK plus volumineuse |
| Auditabilité sans accès aux données brutes | Outils de développement encore complexes et en maturité |
| Interopérabilité avec SSI (divulgation sélective) | Risque d'usage détourné (blanchiment via transactions privées) |

### Acteurs

- **Zcash / Electric Coin Company** : pionniers des ZK-SNARKs en production (groth16)
- **StarkWare** : ZK-STARKs, StarkNet (L2 Ethereum)
- **Matter Labs** : zkSync Era (ZK-Rollup Ethereum)
- **Polygon Zero / Polygon zkEVM** : ZK scaling Ethereum
- **Scroll** : ZK-Rollup EVM-compatible
- **Aztec Network** : blockchain privée ZK
- **RISC Zero** : preuves ZK pour programmes arbitraires
- **Applied ZKP / Aleo** : langage de programmation dédié aux circuits ZK

### Cas d'usage

- **Paiements confidentiels** : transactions Zcash où montant, émetteur et destinataire sont masqués.
- **Scalabilité Ethereum** : les ZK-Rollups (zkSync, StarkNet) permettent des milliers de TPS avec sécurité L1.
- **Identité décentralisée** : présenter un credential sans révéler les attributs non nécessaires.
- **Vote électronique** : prouver qu'on a voté sans révéler son vote, et que le vote a été compté.
- **Santé** : partager un résultat médical (ex. test négatif) sans révéler le dossier complet.
- **Finance** : prouver sa solvabilité ou conformité réglementaire sans révéler le bilan complet.
- **Gaming** : prouver qu'on possède un item rare sans révéler sa stratégie de jeu.

### Chiffres clés

- Les ZK-Rollups ont atteint une TVL de plusieurs **milliards de dollars** sur Ethereum en 2024.
- zkSync Era a traité plus de **500 millions de transactions** depuis son lancement en 2023.
- StarkNet permet des débits théoriques de **10 000+ TPS** (contre ~15 TPS pour Ethereum L1).
- Tornado Cash : environ **7 Md$** de fonds mixés avant sanction OFAC en août 2022.
- Les preuves ZK-SNARK (Groth16) pèsent environ **200 octets** — comparé aux STARKs qui peuvent peser plusieurs KB.
- Zcash a été lancé en **2016**, première implémentation ZK-SNARKs en production à grande échelle.

---

## Flashcards
#flashcards

Qu'est-ce qu'une preuve à divulgation nulle de connaissance (ZKP) ? :: Un protocole cryptographique permettant à un prouveur de convaincre un vérificateur qu'une affirmation est vraie, sans révéler aucune information sur le secret lui-même. Trois propriétés : complétude, solidité, divulgation nulle.

Quelle est la différence entre ZK-SNARKs et ZK-STARKs ? :: Les SNARKs produisent des preuves très compactes et rapides à vérifier, mais nécessitent un trusted setup (cérémonie de confiance). Les STARKs n'ont pas de trusted setup et sont résistants aux quantiques, mais leurs preuves sont plus volumineuses.

Qu'est-ce qu'un ZK-Rollup ? :: Une solution de scalabilité L2 pour Ethereum qui regroupe des centaines de transactions off-chain, génère une preuve ZK de leur validité, et soumet uniquement cette preuve sur la blockchain L1 — réduisant drastiquement les coûts et augmentant le débit.

Qu'est-ce qu'un "trusted setup" et pourquoi est-il problématique ? :: Une cérémonie cryptographique (MPC) nécessaire pour initialiser certains systèmes ZK-SNARKs, générant des paramètres publics. Si les participants à la cérémonie colludent ou conservent des données secrètes, la sécurité du système est compromise.

Comment les ZKP s'articulent-ils avec l'identité décentralisée (SSI) ? :: Les ZKP permettent la divulgation sélective dans les Verifiable Credentials : prouver qu'on satisfait une condition (ex. être majeur) sans révéler l'attribut exact (date de naissance), grâce à des signatures comme BBS+.

Pourquoi Tornado Cash a-t-il été sanctionné par l'OFAC ? :: Tornado Cash est un protocole de mixage ZKP sur Ethereum qui rendait les transactions anonymes. L'OFAC (trésor américain) l'a sanctionné en août 2022 car il a été massivement utilisé pour blanchir des fonds issus de hacks (dont le groupe Lazarus nord-coréen).

Quelles sont les trois propriétés fondamentales d'un ZKP ? :: 1) Complétude : un prouveur honnête convainc toujours le vérificateur si l'énoncé est vrai. 2) Solidité : un prouveur malhonnête ne peut pas convaincre si l'énoncé est faux. 3) Divulgation nulle : le vérificateur n'apprend rien au-delà de la véracité de l'énoncé.

---

## Sources

- Zcash — explication ZK-SNARKs : https://z.cash/technology/zksnarks/
- StarkWare — ZK-STARKs : https://starkware.co/stark/
- Ethereum Foundation — ZK-Rollups : https://ethereum.org/en/developers/docs/scaling/zk-rollups/
- OFAC sanction Tornado Cash (août 2022) : https://ofac.treasury.gov
- Introduction ZKP — Vitalik Buterin blog : https://vitalik.eth.limo

---

## Notions liées

- [[Identité décentralisée (SSI)]]
- [[Interopérabilité blockchain]]
- [[Cadre juridique crypto et blockchain]]
- [[Chiffrement et gestion des clés]]
- [[Privacy by Design]]
- [[eIDAS 2.0 et identité numérique]]
