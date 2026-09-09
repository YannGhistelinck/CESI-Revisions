---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: null
---

# Identité décentralisée (SSI)

## En bref

La Self-Sovereign Identity (SSI), ou identité auto-souveraine, est un paradigme dans lequel l'individu contrôle entièrement ses propres données d'identité, sans dépendre d'un tiers centralisé (État, GAFAM, banque). Elle repose sur trois piliers : les **DID** (Decentralized Identifiers — identifiants décentralisés), les **Verifiable Credentials** (attestations vérifiables) et les **wallets d'identité** (portefeuilles numériques). La blockchain joue le rôle de registre ancré de confiance pour la résolution des DID.

---

## Approfondir

### Fonctionnement

**Architecture SSI en trois couches** :

1. **DID (Decentralized Identifiers)** :
   - Identifiants uniques, persistants et résolvables, enregistrés sur une blockchain ou un registre décentralisé.
   - Format : `did:method:identifiant-unique` (ex. `did:ebsi:2A9RkiYZJsBHT1nSB3HZAwYMNfgM7Psveyodqm8a3GKL`)
   - Standard W3C DID Core 1.0 (recommandation officielle depuis juillet 2022).
   - Le DID Document associé contient les clés publiques de l'entité et les services d'endpoint.

2. **Verifiable Credentials (VC)** :
   - Attestations numériques signées cryptographiquement par un émetteur (Issuer).
   - Structure : Issuer (émetteur) → Holder (porteur) → Verifier (vérificateur) — triangle de confiance.
   - Standard W3C Verifiable Credentials Data Model 2.0.
   - Exemples : diplôme, permis de conduire, certificat de vaccination, attestation d'âge.
   - **Verifiable Presentations** : le Holder compose et présente des VC au Verifier, potentiellement en divulgation sélective (n'afficher que l'âge, pas la date de naissance complète).

3. **Wallet d'identité** :
   - Application (mobile ou web) qui stocke les VC du porteur et génère les Verifiable Presentations.
   - Gère les clés privées DID du porteur.

**Protocoles et standards** :
- **DIDComm** : protocole de messagerie sécurisée entre agents SSI.
- **OpenID for Verifiable Credentials (OID4VC)** : extension d'OpenID Connect pour l'émission et la présentation de VC — retenu par l'UE pour le portefeuille EUDI.
- **BBS+ signatures** : signatures à divulgation sélective sans révéler quelles attributs ont été omis.

**DEEP** (Decentralized Identity for European Progressive Ecosystem) : projet européen visant à expérimenter l'identité décentralisée dans des cas d'usage publics.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Contrôle total de l'utilisateur sur ses données | Responsabilité totale de l'utilisateur (perte du wallet = perte d'identité) |
| Divulgation sélective : ne partager que le strict nécessaire | Interopérabilité encore complexe entre méthodes DID |
| Pas de honeypot centralisé (moins de risques de fuite) | Adoption lente : nécessite infrastructure, formation, réglementation |
| Réutilisation des credentials entre services | Révocation des credentials complexe à gérer |
| Respect du RGPD (data minimisation, privacy by design) | Résistance des acteurs dominants (GAFAM, États) |
| Authentification sans mot de passe | Maturité technique encore en cours |

### Acteurs

- **W3C** : standardisation DID et Verifiable Credentials
- **Decentralized Identity Foundation (DIF)** : consortium technique SSI
- **European Blockchain Services Infrastructure (EBSI)** : infrastructure blockchain de l'UE pour les diplômes, identités
- **Microsoft (Entra Verified ID)** : solution SSI entreprise basée sur DID
- **Spruce Systems, Trinsic, Walt.id** : plateformes SSI open source
- **ESSIF (European Self-Sovereign Identity Framework)** : cadre européen SSI
- **Sovrin Foundation** : réseau blockchain public dédié à l'identité

### Cas d'usage

- **Diplômes numériques** : EBSI permet aux universités européennes d'émettre des diplômes vérifiables que les étudiants portent dans leur wallet (projet EBP — European Blockchain Partnership).
- **KYC bancaire** : un utilisateur vérifié une fois par une banque peut réutiliser sa VC KYC auprès d'autres institutions.
- **Accès aux services publics** : connexion à une administration sans créer de compte, en présentant un VC d'identité nationale.
- **Santé** : carnet de vaccination, dossier médical partagé sélectivement avec les médecins.
- **Ressources humaines** : portfolio de certifications professionnelles vérifiables (LinkedIn Verified Skills).
- **Contrôle d'âge** : prouver qu'on est majeur sans révéler sa date de naissance (divulgation sélective).

### Chiffres clés

- W3C DID Core 1.0 est devenu une recommandation officielle en **juillet 2022**.
- L'UE vise **80 % des citoyens** équipés d'un portefeuille d'identité numérique EUDI d'ici **2030** (via eIDAS 2.0).
- Plus de **100 méthodes DID** enregistrées dans le registre W3C en 2024.
- EBSI a émis des dizaines de milliers de **diplômes vérifiables** dans des pilotes avec des universités européennes.
- Marché de l'identité décentralisée estimé à **6,8 Md$** en 2030 (MarketsandMarkets).
- Microsoft Entra Verified ID : plus de **1 000 organisations** utilisatrices en 2024.

---

## Flashcards
#flashcards

Qu'est-ce qu'un DID (Decentralized Identifier) ? :: Un identifiant unique, persistant et auto-souverain enregistré sur un registre décentralisé (blockchain ou autre). Il est contrôlé par son propriétaire et résolvable sans autorité centrale. Format : did:method:identifiant.

Qu'est-ce qu'un Verifiable Credential (VC) ? :: Une attestation numérique signée cryptographiquement par un émetteur (diplôme, carte d'identité, certificat), que le porteur conserve dans son wallet et peut présenter à des vérificateurs de manière sélective et vérifiable.

Quels sont les trois rôles du triangle de confiance SSI ? :: Issuer (émetteur qui signe le credential), Holder (porteur qui le conserve dans son wallet), Verifier (vérificateur qui valide la signature et la validité du credential).

Qu'est-ce que la divulgation sélective dans le contexte SSI ? :: La capacité pour un porteur de ne révéler qu'une partie des attributs d'un Verifiable Credential — par exemple, prouver qu'on est majeur sans divulguer sa date de naissance exacte, grâce à des techniques cryptographiques comme BBS+.

Quel est le rôle de la blockchain dans une architecture SSI ? :: La blockchain sert de registre ancré de confiance pour la publication et la résolution des DID Documents (contenant les clés publiques des entités). Elle n'héberge pas les credentials eux-mêmes, qui restent dans les wallets des utilisateurs.

Qu'est-ce qu'EBSI ? :: European Blockchain Services Infrastructure — infrastructure blockchain déployée par la Commission européenne dans les États membres pour des cas d'usage publics comme les diplômes vérifiables, l'identité et la traçabilité.

Pourquoi la SSI est-elle compatible avec le RGPD ? :: Car elle applique les principes de data minimisation (divulgation sélective), privacy by design, et évite la création de bases de données centralisées massives (honeypots). Le porteur contrôle quelles données il partage et avec qui.

---

## Sources

- W3C DID Core 1.0 : https://www.w3.org/TR/did-core/
- W3C Verifiable Credentials : https://www.w3.org/TR/vc-data-model/
- EBSI : https://ec.europa.eu/digital-building-blocks/ebsi
- Decentralized Identity Foundation : https://identity.foundation
- Microsoft Entra Verified ID : https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-verified-id

---

## Notions liées

- [[eIDAS 2.0 et identité numérique]]
- [[Zero-Knowledge Proof (ZKP)]]
- [[Cadre juridique crypto et blockchain]]
- [[RGPD]]
- [[Authentification et gestion des accès (IAM)]]
- [[Privacy by Design]]
