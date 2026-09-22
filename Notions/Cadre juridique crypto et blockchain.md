---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# Cadre juridique crypto et blockchain

![[N — Cadre juridique crypto et blockchain.mp3]]
## En bref

La régulation des cryptoactifs et de la blockchain est en pleine construction, tiraillée entre l'impératif d'innovation et la nécessité de protéger les investisseurs, de lutter contre le blanchiment et de maintenir la stabilité financière. En Europe, le règlement **MiCA** (Markets in Crypto-Assets) constitue le cadre le plus complet au monde. En France, le statut **PSAN** (Prestataire de Services sur Actifs Numériques), remplacé par le **CASP** (Crypto-Asset Service Provider) issu de MiCA, encadre les acteurs du marché. La blockchain soulève également des tensions juridiques fondamentales : **droit à l'oubli vs. immutabilité**, et **RGPD vs. pseudonymisation**.

---

## Approfondir

### Fonctionnement

**Chronologie réglementaire française et européenne** :

- **Loi PACTE (2019)** : crée en France le statut PSAN et le visa AMF optionnel pour les ICO. Premier cadre légal crypto en Europe.
- **5e et 6e directives anti-blanchiment (AMLD5/6)** : soumettent les prestataires crypto aux obligations KYC/AML dès 2020.
- **Travel Rule (FATF/GAFI R.16)** : obligation de transmettre les informations sur l'émetteur et le bénéficiaire lors de transferts de cryptoactifs entre PSP. Implémenté en UE via le règlement TFR (Transfer of Funds Regulation) — applicable depuis décembre 2024.
- **Règlement MiCA (Markets in Crypto-Assets)** :
  - Adopté en juin 2023, applicable en totalité depuis décembre 2024.
  - Couvre les émetteurs de tokens (ARTs — Asset-Referenced Tokens, EMTs — E-Money Tokens) et les CASPs (Crypto-Asset Service Providers).
  - Harmonisation à l'échelle UE : passeport européen pour les CASPs.
  - Exclut les NFT unitaires et la DeFi (mais la Commission doit réexaminer d'ici 2025).
  - Obligation de white paper, exigences de capital, règles de marché, interdiction de manipulation.

**KYC/AML** :
- Know Your Customer : vérification de l'identité des clients (pièce d'identité, preuve d'adresse, origine des fonds).
- Anti-Money Laundering : surveillance des transactions suspectes, déclarations TRACFIN (France).
- Seuils : transactions > 1 000 € soumises à la Travel Rule.

**Tensions juridiques blockchain** :

- **Droit à l'oubli (RGPD Art. 17) vs. immutabilité** : la blockchain ne permet pas l'effacement des données. Solutions : ne stocker que des hashs on-chain (données hors chaîne), utilisation du chiffrement (les données existent mais sont illisibles si la clé est détruite — "effacement cryptographique").
- **Pseudonymisation vs. anonymisation** : les adresses de portefeuilles blockchain sont pseudonymes (pas anonymes) — les transactions sont publiques et traçables. Une adresse peut être reliée à une identité réelle (analyses on-chain, KYC des exchanges).
- **Responsabilité des smart contracts** : qui est responsable d'un smart contract défaillant ? Question juridique non totalement résolue.
- **Juridiction** : quelle loi s'applique à une transaction sur une blockchain sans frontière ?

### Avantages / Inconvénients

| Avantages de la régulation | Inconvénients / Tensions |
|---|---|
| Protection des investisseurs contre les arnaques | Risque de freiner l'innovation (compliance coûteuse) |
| Lutte efficace contre le blanchiment (AML/KYC) | Tensions avec la philosophie de décentralisation du Web3 |
| Harmonisation UE : marché unique crypto (MiCA) | Exclusion de la DeFi et des NFT de MiCA (incertitude) |
| Confiance institutionnelle accrue | Arbitrage réglementaire (fuite vers juridictions laxistes) |
| Passeport européen CASP = moins de doublons réglementaires | Travel Rule : difficultés techniques pour les wallets non-custodial |
| Clarté juridique pour les entreprises | Droit à l'oubli incompatible avec l'immutabilité blockchain |

### Acteurs

- **Autorité des Marchés Financiers (AMF)** : régulateur français, délivre les agréments PSAN/CASP
- **ACPR** : supervision prudentielle des acteurs crypto en France
- **ESMA** (European Securities and Markets Authority) : coordination MiCA à l'échelle UE
- **FATF/GAFI** : organisme intergouvernemental définissant les standards AML/CFT internationaux
- **TRACFIN** : cellule de renseignement financier française (déclarations de soupçon)
- **Binance, Coinbase, Kraken** : principaux CASPs enregistrés en Europe
- **Tether, Circle** : émetteurs de stablecoins (soumis aux règles AML/EMT sous MiCA)

### Cas d'usage / enjeux concrets

- **Enregistrement PSAN** : toute plateforme d'échange crypto opérant en France doit être enregistrée à l'AMF. Obligatoire depuis 2021, sous peine de sanctions pénales.
- **Travel Rule** : un exchange qui envoie 2 000 € en BTC à un autre exchange doit transmettre nom, adresse et numéro de compte du donneur d'ordre.
- **ICO sous MiCA** : emission de tokens utilitaires (utility tokens) soumise à publication d'un white paper conforme.
- **DeFi et MiCA** : protocoles DeFi non couverts par MiCA en 2024, mais sous surveillance — la Commission doit statuer avant fin 2025.
- **NFT** : les NFT "unitaires et non fongibles" sont exclus de MiCA, mais les collections à grande échelle pourraient être requalifiées en valeurs mobilières.

### Chiffres clés

- MiCA est le **premier cadre réglementaire complet** sur les cryptoactifs au monde — applicable depuis **décembre 2024**.
- La loi PACTE a été promulguée en **avril 2019** — la France pionnière en Europe.
- L'AMF recensait plus de **80 PSAN enregistrés** en France en 2024.
- La Travel Rule s'applique aux transferts **> 1 000 €** entre PSP au sein de l'UE (règlement TFR).
- Le GAFI a émis sa première guidance crypto en **2019**, révisée en **2021**.
- Les pertes liées aux fraudes et hacks crypto : **environ 2 Md$** en 2023 (Chainalysis).
- Binance a payé une amende record de **4,3 Md$** aux États-Unis (DOJ) en novembre 2023 pour violations AML.

---

## Flashcards
#flashcards/Blockchain/Cadre_juridique_crypto_et_blockchain

Qu'est-ce que le règlement MiCA et quelle est sa portée ? :: Markets in Crypto-Assets — premier cadre réglementaire complet de l'UE sur les cryptoactifs. Adopté en juin 2023, applicable depuis décembre 2024. Il harmonise les règles pour les émetteurs de tokens et les prestataires de services (CASPs) dans toute l'UE, avec un système de passeport européen.

Quelle est la différence entre PSAN et CASP ? :: Le PSAN (Prestataire de Services sur Actifs Numériques) est le statut français créé par la loi PACTE (2019). Le CASP (Crypto-Asset Service Provider) est le statut harmonisé au niveau européen introduit par MiCA (2023), qui remplace progressivement le PSAN.

Qu'est-ce que la Travel Rule dans le contexte crypto ? :: Inspirée de la recommandation R.16 du GAFI, elle impose aux prestataires de services crypto de transmettre les informations d'identification de l'émetteur et du bénéficiaire lors de transferts de cryptoactifs. En UE, elle est implémentée via le règlement TFR, applicable depuis décembre 2024 pour les transferts > 1 000 €.

Comment la blockchain est-elle en tension avec le droit à l'oubli du RGPD ? :: L'article 17 du RGPD garantit le droit à l'effacement des données personnelles. Or, les données inscrites sur une blockchain publique sont immuables et ne peuvent être supprimées. Solutions : stocker uniquement des hashs on-chain (données off-chain), ou recourir à l'"effacement cryptographique" (destruction de la clé de chiffrement rendant les données illisibles).

Pourquoi les adresses de portefeuilles blockchain ne sont-elles pas anonymes mais pseudonymes ? :: Toutes les transactions sont publiques et traçables sur une blockchain publique (Bitcoin, Ethereum). Une adresse peut être reliée à une identité réelle via les KYC des exchanges, des analyses de clustering on-chain ou des erreurs de l'utilisateur. La pseudonymisation n'est pas l'anonymisation.

Qu'est-ce que le KYC et pourquoi est-il obligatoire pour les plateformes crypto ? :: Know Your Customer — procédure de vérification d'identité des clients (pièce d'identité, justificatif de domicile, origine des fonds). Obligatoire en vertu des directives AML européennes pour prévenir le blanchiment d'argent et le financement du terrorisme.

Quels types de cryptoactifs sont exclus du règlement MiCA ? :: Les NFT "véritablement uniques et non fongibles", les cryptoactifs relevant de MiFID II (valeurs mobilières), et les protocoles DeFi entièrement décentralisés sont exclus du périmètre de MiCA — bien que la Commission doive réexaminer ces exclusions avant fin 2025.

---

## Sources

- Règlement MiCA (UE) 2023/1114 : https://eur-lex.europa.eu
- AMF — enregistrement PSAN : https://www.amf-france.org
- Loi PACTE n°2019-486 du 22 mai 2019
- GAFI — guidance crypto 2021 : https://www.fatf-gafi.org
- Règlement TFR (Transfer of Funds Regulation) : https://eur-lex.europa.eu
- CNIL — blockchain et RGPD : https://www.cnil.fr

---

## Notions liées

- [[Identité décentralisée (SSI)]]
- [[eIDAS 2.0 et identité numérique]]
- [[RGPD]]
- [[Interopérabilité blockchain]]
- [[Zero-Knowledge Proof (ZKP)]]
- [[NIS2]]
- [[Souveraineté numérique]]
