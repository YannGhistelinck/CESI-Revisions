---
type: notion
thèmes:
  - Cybersécurité
  - Cloud et Virtualisation
  - Mobilité
statut: pas vu
dernière_révision: 
---

# Authentification et gestion des accès (IAM)

## En bref
> **Définition** : L'IAM (Identity and Access Management) désigne l'ensemble des processus et technologies permettant de gérer les identités numériques et de contrôler les droits d'accès aux ressources informatiques. Il repose sur trois piliers : l'authentification (qui êtes-vous ?), l'autorisation (qu'avez-vous le droit de faire ?) et la traçabilité (qu'avez-vous fait ?).
> **Pourquoi c'est important** : Plus de 80 % des violations de données impliquent des identifiants compromis ou des accès mal configurés (Verizon DBIR, 2023). L'IAM est le premier rempart contre les cyberattaques et une exigence centrale des référentiels NIS2, ISO 27001 et des cyber-assureurs. Dans les environnements cloud et mobilité, la gestion des identités remplace le périmètre réseau comme frontière de sécurité.
> **Chiffres clés** :
> - 83 % des violations de données impliquent des acteurs externes, et 74 % utilisent des identifiants volés ou faibles (Verizon DBIR 2023)
> - Le marché mondial de l'IAM atteindra 34 Mds $ en 2028 (MarketsandMarkets, 2023)
> - L'adoption du MFA réduit de 99,9 % le risque de compromission de compte (Microsoft, 2023)

## Approfondir

### Fonctionnement

**Concepts fondamentaux :**

- **Identité** : représentation numérique d'un utilisateur, d'un service ou d'un appareil dans un système d'information (humain, machine, application).
- **Authentification** : processus de vérification de l'identité déclarée. Peut reposer sur :
  - Ce que l'on **sait** (mot de passe, PIN)
  - Ce que l'on **possède** (token, smartphone, carte à puce)
  - Ce que l'on **est** (biométrie : empreinte, reconnaissance faciale)
- **Autorisation** : définition des droits et permissions accordés à une identité authentifiée sur les ressources.
- **Traçabilité (Accounting)** : journalisation des accès et actions pour audit et investigation (logs, SIEM).

**MFA (Multi-Factor Authentication) :**
Combinaison d'au moins deux facteurs d'authentification différents. Exigé par NIS2, les cyber-assureurs, ISO 27001. Les formes incluent : OTP (One-Time Password), TOTP (Google Authenticator, Microsoft Authenticator), FIDO2/WebAuthn (clé physique YubiKey, Windows Hello), SMS (déconseillé — SIM swapping).

**SSO (Single Sign-On) :**
Authentification unique permettant à un utilisateur de se connecter une seule fois pour accéder à plusieurs applications. Améliore l'expérience utilisateur et réduit la fatigue des mots de passe. Protocoles : SAML 2.0, OAuth 2.0, OpenID Connect (OIDC). Exemple : connexion via Azure AD pour accéder à Office 365, Salesforce, ServiceNow.

**Principle of Least Privilege (moindre privilège) :**
Chaque utilisateur, service ou application ne dispose que des droits strictement nécessaires à l'exercice de ses fonctions. Réduit la surface d'attaque en limitant les dommages en cas de compromission.

**PAM (Privileged Access Management) :**
Sous-ensemble de l'IAM dédié aux comptes à privilèges (administrateurs, comptes de service, accès root). Fonctionnalités : coffre-fort de mots de passe, session recording, rotation automatique des credentials. Solutions : CyberArk, BeyondTrust, Delinea.

**RBAC vs ABAC :**
- **RBAC (Role-Based Access Control)** : droits attribués selon le rôle dans l'organisation. Simple à gérer. Ex : le profil "technicien support" a accès au helpdesk mais pas aux données financières.
- **ABAC (Attribute-Based Access Control)** : droits définis par des attributs contextuels (localisation, heure, appareil, sensibilité des données). Plus granulaire et adapté au Zero Trust.

**Zero Trust et IAM :**
Le modèle Zero Trust ("ne jamais faire confiance, toujours vérifier") place l'identité au centre de la sécurité. Chaque accès est authentifié, autorisé et audité, quel que soit le réseau. L'IAM devient le périmètre de sécurité dans les environnements cloud, hybrides et mobilité.

**Cycle de vie des identités (Identity Lifecycle Management) :**
- **Provisioning** : création du compte à l'arrivée (onboarding)
- **Modification** : adaptation des droits en cas de changement de poste
- **Déprovisioning** : suppression/désactivation du compte au départ (offboarding) — source majeure de failles si non automatisé

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction drastique du risque de compromission de compte | Complexité de déploiement dans les SI hétérogènes |
| Conformité NIS2, ISO 27001, RGPD | Coût des solutions enterprise (CyberArk, Okta) |
| Amélioration de l'expérience utilisateur (SSO) | Résistance au changement des utilisateurs (MFA) |
| Traçabilité et auditabilité des accès | Risque de point unique de défaillance (SSO) |
| Réduction des coûts de helpdesk (reset de mots de passe) | Gestion des identités non-humaines (machines, API) complexe |
| Adaptation native au cloud et au télétravail | Dépendance aux annuaires (Active Directory, LDAP) |

### Acteurs et solutions du marché
- **IDaaS (Identity as a Service)** : Microsoft Entra ID (ex-Azure AD), Okta, Ping Identity, Google Workspace Identity
- **PAM** : CyberArk (leader), BeyondTrust, Delinea (ex-Thycotic/Centrify), Wallix (français)
- **MFA** : Microsoft Authenticator, Google Authenticator, Duo Security (Cisco), YubiKey (FIDO2)
- **IAM open source** : Keycloak (Red Hat), FreeIPA, Shibboleth
- **Annuaires** : Microsoft Active Directory, OpenLDAP
- **Solutions ITSM avec IAM** : ServiceNow, SailPoint, Saviynt

### Cas d'usage concrets
1. **Télétravail et accès VPN** : Une entreprise déploie le MFA via Microsoft Authenticator sur tous les accès VPN et portails RH. Le taux de succès des attaques par credential stuffing chute à quasi zéro. La cyber-assurance accepte de maintenir la couverture grâce à cette mesure.
2. **Départ d'un administrateur système** : Sans déprovisioning automatisé, un ancien administrateur conserve ses accès pendant 3 mois après son départ. Un IAM avec provisioning automatisé (via connecteur RH → AD) désactive le compte en temps réel dès la sortie des effectifs.
3. **Migration cloud (Zero Trust)** : Un groupe industriel migre vers Microsoft 365 et Azure. L'IAM (Microsoft Entra ID + Conditional Access) remplace le périmètre réseau : chaque accès est évalué selon l'identité, l'appareil (conformité Intune), la localisation et la sensibilité de la ressource.

### Chiffres et tendances
- Gartner classe l'IAM parmi les 10 technologies de sécurité les plus importantes jusqu'en 2026
- L'adoption du MFA reste faible : seulement 40 % des entreprises françaises ont déployé le MFA sur l'ensemble de leurs accès (CESIN, 2023)
- Tendance 2024-2025 : montée du CIEM (Cloud Infrastructure Entitlement Management) pour gérer les droits dans les environnements multi-cloud
- L'IA est de plus en plus intégrée dans les solutions IAM pour détecter les comportements anormaux (UEBA — User and Entity Behavior Analytics)
- Passwordless (sans mot de passe) : montée en puissance de FIDO2/WebAuthn comme standard d'authentification forte sans mot de passe

## Flashcards
#flashcards
Qu'est-ce que l'IAM ? :: Identity and Access Management : ensemble des processus et technologies gérant les identités numériques et les droits d'accès. Repose sur trois piliers : authentification (qui êtes-vous ?), autorisation (que pouvez-vous faire ?) et traçabilité (qu'avez-vous fait ?).

Quels sont les 3 facteurs d'authentification ? :: Ce que l'on sait (mot de passe), ce que l'on possède (token, smartphone), ce que l'on est (biométrie). Le MFA combine au moins deux de ces facteurs.

Qu'est-ce que le SSO et quel est son risque principal ? :: Single Sign-On : authentification unique pour accéder à plusieurs applications. Le risque principal est le point unique de défaillance : si le compte SSO est compromis, tous les services sont exposés. D'où l'obligation de coupler le SSO au MFA.

Qu'est-ce que le Principle of Least Privilege ? :: Chaque utilisateur, service ou application ne dispose que des droits strictement nécessaires à ses fonctions. Réduit la surface d'attaque et limite les dommages en cas de compromission.

Quelle est la différence entre RBAC et ABAC ? :: RBAC (Role-Based) : droits selon le rôle dans l'organisation, simple. ABAC (Attribute-Based) : droits selon des attributs contextuels (localisation, heure, appareil), plus granulaire et adapté au Zero Trust.

Qu'est-ce que le PAM et pourquoi est-il critique ? :: Privileged Access Management : gestion des comptes à privilèges (admins, root, comptes de service). Ces comptes sont la cible prioritaire des attaquants. Le PAM inclut le coffre-fort de mots de passe, l'enregistrement de sessions et la rotation automatique des credentials.

Quel protocole est recommandé pour le MFA sans mot de passe ? :: FIDO2/WebAuthn, standard ouvert supporté par les navigateurs et OS majeurs. Il utilise de la cryptographie asymétrique et des clés physiques (YubiKey) ou biométrie (Windows Hello). Il est résistant au phishing.

## Sources
- Verizon Data Breach Investigations Report (DBIR) 2023
- Microsoft Digital Defense Report 2023
- Gartner — Magic Quadrant for Access Management 2023
- NIST SP 800-63B — Digital Identity Guidelines
- CESIN — Baromètre annuel de la cybersécurité des entreprises françaises 2023
- MarketsandMarkets — IAM Market Report 2023
- ANSSI — Recommandations relatives à l'authentification multifacteur

## Notions liées
- [[NIS2]]
- [[ISO 27001 - 27002]]
- [[NIST Cybersecurity Framework]]
- [[Outils de sécurité réseau]]
- [[Cyber-assurance]]
- [[ANSSI et acteurs de la cybersécurité]]
