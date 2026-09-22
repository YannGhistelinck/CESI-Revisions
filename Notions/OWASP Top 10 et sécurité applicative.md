---
type: notion
thèmes:
  - Cybersécurité
  - Développement
statut: pas vu
dernière_révision: 
---

# OWASP Top 10 et sécurité applicative

![[N — OWASP Top 10 et sécurité applicative.mp3]]
## En bref
> **Définition** : L'OWASP (Open Web Application Security Project) est une fondation internationale qui produit des référentiels de sécurité applicative. L'OWASP Top 10 est la liste des 10 risques de sécurité les plus critiques pour les applications web, mise à jour tous les 3 à 4 ans. C'est le standard de référence mondial pour la sécurisation des applications.
> **Pourquoi c'est important** : 75 % des cyberattaques exploitent des vulnérabilités applicatives (OWASP, 2023). La sécurité applicative est le périmètre où le développeur a le plus d'impact. Pour un DSI, intégrer la sécurité dès la conception (shift-left) réduit le coût de correction des vulnérabilités d'un facteur 30 par rapport à une correction post-production.
> **Chiffres clés** :
> - 84 % des brèches de sécurité exploitent des vulnérabilités applicatives (Verizon DBIR, 2023).
> - Le coût moyen d'une violation de données est de 4,45 M$ en 2023 (IBM Cost of a Data Breach Report 2023).
> - Les injections (SQL, NoSQL, commandes OS) restent présentes dans 94 % des applications testées (OWASP, 2021).

## Approfondir

### Fonctionnement

**OWASP Top 10 — Version 2021**

| Rang | Catégorie | Description |
|------|-----------|-------------|
| A01 | **Broken Access Control** | Contrôles d'accès insuffisants permettant à un utilisateur d'accéder à des ressources non autorisées. Exemple : IDOR (Insecure Direct Object Reference). |
| A02 | **Cryptographic Failures** | Données sensibles mal protégées : chiffrement faible, stockage en clair de mots de passe, TLS désactivé. |
| A03 | **Injection** | Insertion de code malveillant dans une requête : SQL Injection, NoSQL Injection, LDAP Injection, OS Command Injection. |
| A04 | **Insecure Design** | Défauts de conception sécurité : absence de threat modeling, fonctionnalités non sécurisées dès l'architecture. |
| A05 | **Security Misconfiguration** | Configurations par défaut non modifiées, ports ouverts inutilement, messages d'erreur verbeux, services inutiles activés. |
| A06 | **Vulnerable and Outdated Components** | Utilisation de librairies/frameworks avec des CVE connues non patchées. |
| A07 | **Identification and Authentication Failures** | Absence de MFA, mots de passe faibles acceptés, sessions non invalidées, credential stuffing possible. |
| A08 | **Software and Data Integrity Failures** | CI/CD compromis, mises à jour non signées, désérialisation non sécurisée. |
| A09 | **Security Logging and Monitoring Failures** | Absence de journaux d'audit, alertes non configurées, impossibilité de détecter et de répondre à une attaque. |
| A10 | **Server-Side Request Forgery (SSRF)** | Le serveur est trompé pour effectuer des requêtes vers des ressources internes non exposées. |

**OWASP Top 10 CI/CD Risks (2022)**

Référentiel spécifique aux pipelines DevOps :
- **CICD-SEC-1** : Insufficient Flow Control Mechanisms (approbations insuffisantes).
- **CICD-SEC-2** : Inadequate Identity and Access Management.
- **CICD-SEC-3** : Dependency Chain Abuse (typosquatting, dépendances malveillantes).
- **CICD-SEC-8** : Ungoverned Usage of 3rd Party Services.

**Threat Modeling avec STRIDE**

Le threat modeling est une méthode structurée pour identifier les menaces sur une application dès la conception.

| Lettre | Menace | Description | Exemple |
|--------|--------|-------------|---------|
| S | **Spoofing** | Usurpation d'identité | Faux certificat SSL, session hijacking |
| T | **Tampering** | Altération de données | Modification de paramètres HTTP, altération de fichiers |
| R | **Repudiation** | Déni d'action | Absence de logs permettant de nier une action |
| I | **Information Disclosure** | Fuite d'informations | Messages d'erreur verbeux, données en clair |
| D | **Denial of Service** | Déni de service | Épuisement des ressources, requêtes malformées |
| E | **Elevation of Privilege** | Escalade de privilèges | Injection SQL permettant l'accès admin |

**Scoring DREAD**

Méthode de scoring des menaces identifiées par STRIDE (chaque critère noté de 1 à 10) :
- **D**amage potential (potentiel de dommage)
- **R**eproducibility (facilité de reproduction)
- **E**xploitability (facilité d'exploitation)
- **A**ffected users (nombre d'utilisateurs affectés)
- **D**iscoverability (facilité de découverte)

Score DREAD = Moyenne des 5 critères. > 7 = critique, 4-7 = moyen, < 4 = faible.

**SDL — Secure Development Lifecycle**

Le SDL (initié par Microsoft) intègre la sécurité à chaque phase du cycle de développement :

1. **Formation** — Sensibilisation des développeurs à la sécurité.
2. **Exigences** — Définition des exigences de sécurité et de confidentialité.
3. **Conception** — Threat modeling, réduction de la surface d'attaque.
4. **Implémentation** — Outils d'analyse statique (SAST), conventions de code sécurisé.
5. **Vérification** — Tests de sécurité (DAST, fuzzing, pentest).
6. **Déploiement** — Plan de réponse aux incidents, processus de patch.
7. **Réponse** — Processus de gestion des vulnérabilités signalées.

**Shift-Left Security**

Principe consistant à intégrer la sécurité le plus tôt possible dans le cycle de développement plutôt que de la traiter en bout de chaîne. S'applique via :
- Analyse de code statique (SAST) dans l'IDE et le pipeline CI/CD (ex : SonarQube, Checkmarx).
- Analyse des dépendances (SCA) : Snyk, OWASP Dependency-Check.
- Tests d'intrusion applicatif (DAST) : OWASP ZAP, Burp Suite.
- Revues de code orientées sécurité.

**Pentest applicatif vs Audit de code**

| | Pentest applicatif | Audit de code |
|-|-------------------|---------------|
| Approche | Boîte noire ou grise (attaquant externe) | Boîte blanche (accès au code source) |
| Objectif | Exploiter des vulnérabilités existantes | Identifier des défauts de conception et d'implémentation |
| Résultat | Preuves de compromission (PoC) | Liste exhaustive de vulnérabilités avec localisation dans le code |
| Outils | Burp Suite, OWASP ZAP, Metasploit | SonarQube, Checkmarx, Fortify, revue manuelle |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Référentiel universel, reconnu et gratuit | Peut donner un faux sentiment de sécurité si limité au Top 10 |
| Aide à prioriser les efforts de sécurisation | Nécessite une montée en compétence des équipes de développement |
| Shift-left réduit drastiquement le coût des corrections | Ralentissement apparent du développement si mal intégré |
| Threat modeling améliore la conception dès l'origine | DREAD est subjectif si non calibré avec des experts |
| Applicable dans tous les langages et frameworks | Top 10 mis à jour tous les 3-4 ans : peut être décalé avec les menaces émergentes |

### Acteurs et solutions du marché

**Outils SAST (Static Application Security Testing)**
- SonarQube / SonarCloud (open-source/cloud).
- Checkmarx, Fortify (Micro Focus), Veracode.
- Semgrep (règles communautaires).

**Outils DAST (Dynamic Application Security Testing)**
- OWASP ZAP (Zed Attack Proxy) — open-source de référence.
- Burp Suite Pro (PortSwigger) — standard industrie pentest.
- Nikto, Nuclei.

**Plateformes de sécurité applicative**
- Snyk (SCA + SAST) — très populaire DevSecOps.
- GitHub Advanced Security (CodeQL).
- GitLab Ultimate (SAST, DAST, Secret Detection intégrés).

### Cas d'usage concrets

1. **PME e-commerce** : Audit OWASP Top 10 avant mise en production d'un site de paiement. Découverte d'une injection SQL sur le moteur de recherche produit (A03) et d'un contrôle d'accès défaillant sur les commandes (A01). Correction avant lancement.

2. **Entreprise en mode DevSecOps** : Intégration de SonarQube dans la pipeline Jenkins. Blocage automatique des merges si score de sécurité < B. Réduction de 60 % des vulnérabilités détectées en production en 6 mois.

3. **Threat modeling sur une API bancaire** : Application de STRIDE sur les flux d'authentification. Identification d'un risque d'Elevation of Privilege (E) via manipulation du JWT. Implémentation du signing RS256 avec rotation des clés.

### Chiffres et tendances

- Le coût moyen d'une attaque par injection SQL est de 1,6 M$ (IBM, 2023).
- 82 % des applications web présentent au moins une vulnérabilité OWASP Top 10 (WhiteHat Security, 2022).
- Le marché des outils de sécurité applicative (AppSec) atteindra 13,2 Md$ en 2026 (MarketsandMarkets, 2022).

## Flashcards
#flashcards/Cybersécurité/OWASP_Top_10_et_sécurité_applicative #flashcards/Développement/OWASP_Top_10_et_sécurité_applicative

Citez les 5 premières catégories de l'OWASP Top 10 2021. :: A01 Broken Access Control, A02 Cryptographic Failures, A03 Injection, A04 Insecure Design, A05 Security Misconfiguration.

Que signifie STRIDE dans le threat modeling ? :: Spoofing (usurpation), Tampering (altération), Repudiation (déni), Information Disclosure (fuite), Denial of Service, Elevation of Privilege.

Qu'est-ce que le "shift-left security" ? :: Principe consistant à intégrer la sécurité le plus tôt possible dans le cycle de développement (dès la conception et le code) plutôt qu'en fin de chaîne, réduisant le coût de correction d'un facteur 30.

Quelle est la différence entre SAST et DAST ? :: SAST (Static) analyse le code source sans l'exécuter (boîte blanche). DAST (Dynamic) teste l'application en cours d'exécution comme un attaquant externe (boîte noire).

Qu'est-ce que le SDL (Secure Development Lifecycle) ? :: Processus initié par Microsoft intégrant la sécurité à chaque phase du développement : formation, exigences, conception (threat modeling), implémentation (SAST), vérification (pentest), déploiement et réponse aux incidents.

Qu'est-ce qu'une injection SQL et comment la prévenir ? :: Insertion de code SQL malveillant dans une entrée utilisateur pour manipuler la base de données. Prévention : requêtes paramétrées/préparées, ORM, validation des entrées, principe du moindre privilège sur les comptes DB.

Qu'est-ce que le SSRF (A10 OWASP) ? :: Server-Side Request Forgery : l'attaquant manipule le serveur pour qu'il effectue des requêtes vers des ressources internes (ex : metadata cloud AWS, services internes non exposés).

Citez 3 outils DAST de référence pour tester la sécurité d'une application web. :: OWASP ZAP (open-source), Burp Suite Pro (PortSwigger), Nikto.

Pourquoi l'OWASP Top 10 A01 (Broken Access Control) est-il en première position depuis 2021 ? :: Il est désormais la vulnérabilité la plus répandue (présente dans 94 % des applications testées), notamment via les IDOR (Insecure Direct Object Reference) permettant d'accéder aux données d'autres utilisateurs.

## Sources
- OWASP Top 10 2021 — https://owasp.org/Top10/
- OWASP Top 10 CI/CD Risks — https://owasp.org/www-project-top-10-ci-cd-security-risks/
- Microsoft SDL — https://www.microsoft.com/en-us/securityengineering/sdl
- IBM — *Cost of a Data Breach Report 2023* — https://www.ibm.com/reports/data-breach
- Verizon — *Data Breach Investigations Report 2023* — https://www.verizon.com/business/resources/reports/dbir/

## Notions liées
- [[DevSecOps]]
- [[Analyse de code (SAST - DAST)]]
- [[CI - CD]]
- [[Défense en profondeur]]
- [[Red Team - Blue Team - Purple Team]]
- [[Authentification et gestion des accès (IAM)]]
- [[Tests logiciels]]
- [[Stratégie de tests logiciels]]
