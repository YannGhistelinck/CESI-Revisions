---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: 
---

# eIDAS 2.0 et identité numérique

![[N — eIDAS 2.0 et identité numérique.mp3]]
## En bref

eIDAS 2.0 (Electronic IDentification, Authentication and trust Services) est le règlement européen révisé (2024) qui refonde le cadre d'identification électronique et de services de confiance dans l'UE. Sa grande nouveauté est le **portefeuille d'identité numérique européen** (EUDI Wallet — European Digital Identity Wallet), que chaque État membre devra proposer à ses citoyens d'ici **2026**. Ce règlement articule plusieurs technologies : standards d'identité décentralisée, cryptographie, et potentiellement blockchain — encadrées par les travaux de l'**ISO/TC 307** (comité technique blockchain de l'ISO).

---

## Approfondir

### Fonctionnement

**eIDAS 1.0 (2014)** : premier règlement européen sur l'identification électronique. Il établit la reconnaissance mutuelle des eIDs nationaux (ex. France Connect) et des services de confiance (signature électronique, cachet, horodatage). Limites : interopérabilité insuffisante, faible adoption transfrontalière.

**eIDAS 2.0 (règlement UE 2024/1183, adopté en mars 2024)** :

1. **EUDI Wallet (European Digital Identity Wallet)** :
   - Application mobile/web fournie ou certifiée par chaque État membre.
   - Permet de stocker et présenter des attributs d'identité : pièce d'identité, permis de conduire, diplômes, prescriptions médicales, cartes de fidélité.
   - Utilisable auprès de services publics ET privés dans toute l'UE.
   - Architecture basée sur les standards SSI : DID, Verifiable Credentials (ou équivalents), OID4VC (OpenID for Verifiable Credentials).
   - **Formats de données** : mdoc (ISO 18013-5, pour le permis de conduire mobile) et SD-JWT VC (pour les credentials web).

2. **Niveaux d'assurance** (LoA — Level of Assurance) maintenus d'eIDAS 1.0 :
   - **Faible** : ex. login/mot de passe basique
   - **Substantiel** : ex. authentification à deux facteurs
   - **Élevé** : vérification physique de l'identité (utilisé pour les signatures qualifiées)

3. **Services de confiance étendus** : eIDAS 2.0 ajoute de nouveaux services qualifiés :
   - Archivage électronique qualifié
   - Gestion de dispositifs d'authentification à distance
   - Journaux d'enregistrement électronique qualifiés (potentiellement compatibles blockchain)
   - Attestation électronique d'attributs qualifiée (QEAA) — le socle légal des credentials vérifiables

4. **Obligations pour le secteur privé** : les grandes plateformes (services bancaires, transports, télécoms, réseaux sociaux) devront accepter l'EUDI Wallet comme moyen d'authentification dès 2026.

**ISO/TC 307 — Blockchain et technologies de registres distribués** :
- Comité technique de l'ISO créé en 2016, secrétariat assuré par l'Australie.
- Produit des normes internationales sur la blockchain : terminologie, référentiels d'architecture, smart contracts, privacy, interopérabilité.
- Normes clés : ISO 22739 (terminologie blockchain), ISO 23257 (architecture de référence), ISO 23258 (taxonomie des blockchains).
- Les travaux ISO/TC 307 encadrent les choix techniques des États membres pour l'implémentation de l'EUDI Wallet.

**Large Scale Pilots (LSP)** : la Commission européenne finance 4 projets pilotes à grande échelle pour tester l'EUDI Wallet :
- **POTENTIAL** (22 pays, conduit par France/Allemagne)
- **EWC** (European Wallet Consortium)
- **DC4EU** (éducation et affaires sociales)
- **NOBID** (paiements)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Identité numérique universelle dans toute l'UE | Risque de surveillance de masse si mal implémenté |
| Réduction des frictions d'identification cross-border | Dépendance aux États membres pour la qualité du wallet |
| Base légale pour les Verifiable Credentials (QEAA) | Complexité d'implémentation technique et juridique |
| Objectif d'autonomie numérique européenne (souveraineté) | Interopérabilité avec les systèmes légacy existants |
| Divulgation sélective des attributs (privacy by design) | Risque de fragmentation si chaque État fait son propre wallet |
| Obligation d'acceptation par les grandes plateformes | Délais d'adoption des citoyens et des entreprises |

### Acteurs

- **Commission européenne / DG CONNECT** : pilote d'eIDAS 2.0 et des LSP
- **ENISA** : Agence de l'UE pour la cybersécurité — spécifications techniques de sécurité du wallet
- **ISO/TC 307** : normalisation internationale blockchain
- **W3C** : standards DID et Verifiable Credentials intégrés dans l'architecture EUDI Wallet
- **Agence nationale (France)** : DINUM — France Identity / AgentConnect
- **Google / Apple** : wallets mobiles devront se conformer à eIDAS 2.0 pour le marché UE
- **NXP, Thales, IN Groupe** : fabricants de composants sécurisés pour les wallets

### Cas d'usage

- **Ouverture de compte bancaire** entièrement digitale et sécurisée avec l'EUDI Wallet (KYC simplifié).
- **Présentation du permis de conduire numérique** lors d'un contrôle routier dans un autre État membre.
- **Accès à l'université** d'un autre pays UE avec son diplôme émis en Verifiable Credential.
- **Prescription médicale numérique** présentée dans une pharmacie d'un autre État membre.
- **Connexion à des services en ligne** sans créer de compte (remplacement du "Se connecter avec Google/Facebook").
- **Signature de contrats** immobiliers ou professionnels avec signature qualifiée depuis le wallet.

### Chiffres clés

- eIDAS 2.0 adopté par le Parlement européen en **février 2024**, publié au JOUE en **avril 2024**.
- Objectif : **80 % des citoyens** de l'UE équipés d'un EUDI Wallet d'ici **2030**.
- **4 pilotes LSP** financés à hauteur de **46 M€** par la Commission européenne.
- Plus de **250 entités** participent aux Large Scale Pilots dans 26 États membres.
- ISO/TC 307 a publié plus de **15 normes** sur la blockchain depuis 2016.
- L'architecture de référence de l'EUDI Wallet (ARF — Architecture Reference Framework) est disponible en open source sur GitHub depuis 2022.

---

## Flashcards
#flashcards/Blockchain/eIDAS_2_0_et_identité_numérique

Qu'est-ce qu'eIDAS 2.0 et quelle est sa principale nouveauté par rapport à eIDAS 1.0 ? :: eIDAS 2.0 (règlement UE 2024/1183) est la révision du règlement européen sur l'identification électronique. Sa principale nouveauté est l'EUDI Wallet, un portefeuille d'identité numérique que chaque État membre doit proposer à ses citoyens, utilisable partout dans l'UE auprès des services publics et privés.

Qu'est-ce qu'une QEAA dans le cadre d'eIDAS 2.0 ? :: Qualified Electronic Attestation of Attributes — attestation électronique qualifiée d'attributs. C'est le cadre légal sous eIDAS 2.0 qui donne valeur juridique aux Verifiable Credentials émis par des prestataires qualifiés (ex. diplômes, permis de conduire numériques).

Quels sont les deux formats de données standardisés pour l'EUDI Wallet ? :: mdoc (ISO 18013-5), utilisé notamment pour le permis de conduire mobile (mDL), et SD-JWT VC (Selective Disclosure JWT), format web pour les credentials avec divulgation sélective.

Quel est le rôle de l'ISO/TC 307 ? :: Le comité technique 307 de l'ISO est responsable de la normalisation internationale des technologies blockchain et de registres distribués. Il produit des standards sur la terminologie (ISO 22739), l'architecture de référence (ISO 23257), les smart contracts et la privacy en contexte blockchain.

Quelle est la différence entre eIDAS 1.0 et eIDAS 2.0 concernant le secteur privé ? :: eIDAS 1.0 se concentrait sur la reconnaissance mutuelle des eIDs nationaux entre États membres. eIDAS 2.0 va plus loin en obligeant les grandes plateformes privées (banques, télécom, réseaux sociaux) à accepter l'EUDI Wallet comme moyen d'identification.

Qu'est-ce qu'un Large Scale Pilot (LSP) dans le contexte eIDAS 2.0 ? :: Un projet pilote à grande échelle financé par la Commission européenne pour tester l'EUDI Wallet dans des cas d'usage réels (identité, éducation, santé, paiements) impliquant plusieurs États membres. Quatre LSP sont en cours : POTENTIAL, EWC, DC4EU, NOBID.

Pourquoi l'EUDI Wallet est-il considéré comme un enjeu de souveraineté numérique européenne ? :: L'EUDI Wallet vise à offrir aux citoyens européens un moyen d'identification numérique souverain, réduisant la dépendance aux systèmes d'identification privés (Google, Apple, Facebook), conformément aux objectifs de la boussole numérique 2030 de l'UE.

---

## Sources

- Règlement eIDAS 2.0 (UE) 2024/1183 : https://eur-lex.europa.eu
- Architecture Reference Framework EUDI Wallet : https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework
- Commission européenne — EUDI Wallet : https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet
- ISO/TC 307 : https://www.iso.org/committee/6266604.html
- ENISA — eIDAS 2.0 security : https://www.enisa.europa.eu

---

## Notions liées

- [[Identité décentralisée (SSI)]]
- [[Cadre juridique crypto et blockchain]]
- [[Zero-Knowledge Proof (ZKP)]]
- [[RGPD]]
- [[Souveraineté numérique]]
- [[Authentification et gestion des accès (IAM)]]
- [[Privacy by Design]]
