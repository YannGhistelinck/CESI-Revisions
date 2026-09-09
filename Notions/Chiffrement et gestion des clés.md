---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Chiffrement et gestion des clés

## En bref
> **Définition** : Le chiffrement est le processus de transformation de données lisibles en données illisibles sans clé de déchiffrement. Dans le cloud, on distingue le chiffrement at rest (données stockées), in transit (données en mouvement) et in use (données en cours de traitement). La gestion des clés (KMS) définit qui contrôle les clés et donc l'accès ultime aux données.
> **Pourquoi c'est important** : Pour une DSI, la question du chiffrement est centrale dans toute stratégie cloud, notamment pour la conformité RGPD, NIS2 et PCI-DSS. La gestion des clés détermine le niveau de dépendance vis-à-vis du fournisseur cloud et la capacité à révoquer l'accès aux données en cas d'incident ou de résiliation de contrat.
> **Chiffres clés** :
> - 82 % des violations de données impliquent des données stockées en clair ou insuffisamment chiffrées (Verizon DBIR 2023)
> - Le marché global du chiffrement des données devrait atteindre 38 Md$ en 2028 (MarketsandMarkets, 2023)
> - AES-256 est considéré sûr jusqu'en 2030+ par le NIST ; RSA-2048 est en cours de transition vers des algorithmes post-quantiques

## Approfondir

### Fonctionnement

**Chiffrement at rest**
Les données sont chiffrées lorsqu'elles sont stockées sur disque (bases de données, fichiers, sauvegardes). Les principaux algorithmes utilisés sont AES-256 (symétrique) et RSA (asymétrique pour les échanges de clés). Côté cloud, chaque CSP propose des mécanismes natifs : AWS S3 SSE (Server-Side Encryption), Azure Storage Service Encryption, GCP CMEK.

**Chiffrement in transit**
Les données sont chiffrées lors de leur transmission sur le réseau. Protocoles : TLS 1.2/1.3 (standard actuel), HTTPS, SFTP, IPSec (VPN). TLS 1.3 est recommandé par l'ANSSI depuis 2020. Le certificat SSL/TLS assure l'authenticité du serveur (PKI).

**Chiffrement in use (Confidential Computing)**
Technologie émergente permettant de chiffrer les données même pendant leur traitement en mémoire, via des Trusted Execution Environments (TEE) : Intel SGX, AMD SEV, ARM TrustZone. Permet le traitement de données sensibles dans un cloud non approuvé.

**BYOK — Bring Your Own Key**
Le client génère ses propres clés de chiffrement et les importe dans le KMS du fournisseur cloud. Les données sont chiffrées par la clé du client, mais celle-ci est stockée et gérée par le CSP. Niveau de contrôle intermédiaire : le client possède la clé, mais le CSP pourrait y accéder techniquement.

**HYOK — Hold Your Own Key**
Le client conserve ses clés de chiffrement sur une infrastructure qu'il contrôle entièrement (on-premise HSM). Le fournisseur cloud ne peut jamais accéder aux clés. Les opérations de chiffrement/déchiffrement impliquent un aller-retour vers l'infrastructure du client. Niveau de contrôle maximal, latence plus élevée.

**KMS — Key Management Service**
Service centralisé de génération, stockage, rotation et révocation des clés de chiffrement. Les HSM (Hardware Security Modules) sont des modules matériels certifiés FIPS 140-2/3 qui protègent les clés en les isolant physiquement. AWS KMS, Azure Key Vault et Google Cloud KMS sont les solutions cloud natives. HashiCorp Vault est la solution open-source de référence.

**Classification des données (Data Classification)**
Préalable indispensable au chiffrement. Permet d'appliquer les bons niveaux de protection selon la sensibilité : Public > Interne > Confidentiel > Secret. Chaque niveau implique des contraintes de chiffrement, d'accès et de localisation différentes.

**Rotation des clés**
Bonne pratique consistant à remplacer régulièrement les clés de chiffrement pour limiter la fenêtre d'exposition en cas de compromission. Automatisable via KMS (rotation annuelle recommandée par AWS). La rotation n'implique pas le re-chiffrement de toutes les données grâce à l'enveloppe de chiffrement (data encryption key chiffrée par une key encryption key).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Protection des données en cas de violation physique ou logique | Surcoût de performance (latence de chiffrement/déchiffrement) |
| Conformité réglementaire (RGPD, PCI-DSS, HDS, NIS2) | Complexité de gestion des clés à grande échelle |
| BYOK/HYOK : contrôle souverain sur les données | HYOK : latence accrue et infrastructure supplémentaire à maintenir |
| Révocabilité des accès (résilier = révoquer les clés) | Risque de perte de données si clé perdue sans backup |
| Confidential Computing : traitement sécurisé chez des tiers | Coût des HSM physiques (plusieurs milliers d'euros) |

### Acteurs et solutions du marché

| Solution | Type | Éditeur |
|----------|------|---------|
| AWS KMS + CloudHSM | KMS / HSM cloud | AWS |
| Azure Key Vault + Managed HSM | KMS / HSM cloud | Microsoft |
| Google Cloud KMS + Cloud HSM | KMS / HSM cloud | Google |
| HashiCorp Vault | KMS open-source | HashiCorp (IBM) |
| Thales CipherTrust | HSM physique + KMS | Thales |
| Entrust KeyControl | BYOK / HYOK | Entrust |
| IBM Hyper Protect Crypto Services | Confidential Computing | IBM |

### Cas d'usage concrets

1. **Hébergement de données de santé (HDS)** : Un éditeur de logiciels médicaux héberge des dossiers patients sur AWS. Il utilise AWS KMS avec BYOK pour conserver la maîtrise des clés. La certification HDS impose un chiffrement at rest et in transit. En cas de résiliation du contrat AWS, il révoque ses clés, rendant toutes les données illisibles immédiatement.

2. **Banque en multi-cloud avec HYOK** : Une grande banque européenne utilise Azure et AWS pour ses applications. Pour les données clients (niveau Secret), elle implémente HYOK : les clés restent dans son datacenter on-premise sur des HSM Thales certifiés FIPS 140-3. Azure ne peut jamais accéder aux clés, ce qui lui permet de démontrer sa conformité au régulateur bancaire.

3. **Rotation automatique des clés S3** : Une entreprise stockant des données personnelles sur S3 configure AWS KMS pour effectuer une rotation automatique annuelle des clés CMK. En cas de détection d'une fuite d'une ancienne clé, les données chiffrées avec les nouvelles clés restent protégées (segmentation temporelle).

### Chiffres et tendances

- TLS 1.0 et 1.1 sont officiellement dépréciés depuis 2021 (RFC 8996) — TLS 1.3 recommandé
- Le NIST a lancé en 2022 les premiers standards post-quantiques (CRYSTALS-Kyber, CRYSTALS-Dilithium) pour préparer la migration face aux ordinateurs quantiques
- L'ANSSI recommande l'utilisation de suites cryptographiques hybrides (classique + post-quantique) en phase de transition
- Le "Harvest Now, Decrypt Later" est une menace réelle : des acteurs malveillants collectent des données chiffrées aujourd'hui pour les déchiffrer lorsque les ordinateurs quantiques seront disponibles

## Flashcards
#flashcards/Cloud_et_Virtualisation/Chiffrement_et_gestion_des_clés #flashcards/Cybersécurité/Chiffrement_et_gestion_des_clés

Quelle est la différence entre chiffrement at rest et in transit ? :: At rest : données chiffrées lorsqu'elles sont stockées sur disque (BDD, fichiers, sauvegardes). In transit : données chiffrées pendant leur transmission sur le réseau (TLS, HTTPS, IPSec).

Qu'est-ce que BYOK et en quoi diffère-t-il de HYOK ? :: BYOK (Bring Your Own Key) : le client génère ses clés mais les stocke chez le CSP. HYOK (Hold Your Own Key) : le client conserve ses clés sur son infrastructure propre (HSM on-premise), le CSP n'y accède jamais.

Qu'est-ce qu'un HSM ? :: Hardware Security Module. Module matériel certifié FIPS 140-2/3 dédié à la génération, au stockage et à la protection des clés cryptographiques dans un environnement physiquement isolé.

Qu'est-ce que le Confidential Computing ? :: Technologie permettant de chiffrer les données même en cours de traitement en mémoire (RAM), via des Trusted Execution Environments (TEE) comme Intel SGX ou AMD SEV. Protège les données chez un tiers non entièrement de confiance.

Pourquoi la rotation des clés ne nécessite-t-elle pas de re-chiffrer toutes les données ? :: Grâce à l'enveloppe de chiffrement (key wrapping) : les données sont chiffrées par une DEK (Data Encryption Key). La DEK est elle-même chiffrée par la KEK (Key Encryption Key). Changer la KEK ne nécessite de rechiffrer que les DEKs, pas les données.

Qu'est-ce que la menace "Harvest Now, Decrypt Later" ? :: Des attaquants collectent aujourd'hui des données chiffrées avec des algorithmes classiques (RSA, AES), en anticipant qu'un ordinateur quantique leur permettra de les déchiffrer dans le futur. Cela justifie la migration vers la cryptographie post-quantique.

Quel algorithme de chiffrement symétrique est le standard actuel pour les données at rest ? :: AES-256 (Advanced Encryption Standard, clé 256 bits). Considéré sûr par le NIST jusqu'en 2030+ et résistant aux attaques par force brute même avec des supercalculateurs actuels.

## Sources

- NIST SP 800-57 : Recommendation for Key Management
- NIST FIPS 140-3 : Security Requirements for Cryptographic Modules
- ANSSI, "Recommandations de sécurité relatives à TLS", 2020
- NIST, Post-Quantum Cryptography Standards, 2022-2024
- Verizon, "Data Breach Investigations Report", 2023
- AWS Documentation : AWS Key Management Service
- RFC 8996 : Deprecating TLS 1.0 and TLS 1.1

## Notions liées
- [[Sécurité cloud (CSPM - CASB - CNAPP)]]
- [[Authentification et gestion des accès (IAM)]]
- [[Zero Trust]]
- [[ISO 27001 - 27002]]
- [[Data Lifecycle Management]]
- [[Infrastructure des datacenters]]
