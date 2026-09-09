---
type: notion
thèmes:
  - Développement
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Analyse de code (SAST - DAST)

## En bref
> **Définition** : L'analyse de code regroupe les techniques permettant de détecter automatiquement des défauts, des vulnérabilités et des violations de bonnes pratiques dans un logiciel. Le SAST (Static Application Security Testing) analyse le code source sans l'exécuter ; le DAST (Dynamic Application Security Testing) analyse l'application en cours d'exécution en simulant des attaques externes.
> **Pourquoi c'est important** : Dans un contexte de DevSecOps, l'intégration de l'analyse de code dans les pipelines CI/CD permet de détecter les vulnérabilités au plus tôt (shift-left), réduisant drastiquement le coût de correction et limitant l'exposition aux cyberattaques.
> **Chiffres clés** :
> - Le coût de correction d'un bug est **6 fois plus élevé** en phase de test qu'en phase de développement, et **100 fois plus élevé** en production (IBM Systems Sciences Institute).
> - **70 % des vulnérabilités** critiques dans les applications web proviennent de failles connues et détectables par SAST/DAST (OWASP).
> - Le marché des outils AST (Application Security Testing) atteint **9,5 Md$ en 2025**, croissance annuelle de 18 % (Gartner).

## Approfondir

### Fonctionnement

#### SAST — Analyse statique
Le SAST analyse le code source, le bytecode ou le binaire **sans exécuter** l'application. Il fonctionne par :
- **Parsing et construction d'AST** (Abstract Syntax Tree) : représentation structurée du code.
- **Analyse de flux de données** (data flow analysis) : suivi des données depuis les sources (entrées utilisateur) jusqu'aux puits (sorties sensibles).
- **Analyse de flux de contrôle** (control flow analysis) : détection de chemins d'exécution problématiques.
- **Correspondance de règles** : application de règles prédéfinies (CWE, OWASP Top 10) pour signaler les vulnérabilités.

Avantage principal : analyse **exhaustive** du code, détection précoce (CI/CD). Limite : taux élevé de **faux positifs** (entre 20 % et 50 % selon les outils).

#### DAST — Analyse dynamique
Le DAST teste l'application **en cours d'exécution** (boîte noire), en simulant le comportement d'un attaquant externe :
- Envoi de requêtes malformées (injections SQL, XSS, CSRF…).
- Analyse des réponses pour identifier des vulnérabilités.
- Exploration automatisée (crawling) de l'application.

Avantage : détecte les vulnérabilités réelles dans l'environnement d'exécution, peu de faux positifs. Limite : ne couvre pas le code non atteignable depuis l'interface, nécessite un environnement d'exécution.

#### IAST et RASP — compléments
- **IAST** (Interactive AST) : instrumentation de l'application pendant les tests fonctionnels, combinant avantages SAST et DAST (moins de faux positifs, coverage élevé).
- **RASP** (Runtime Application Self-Protection) : protection en temps réel intégrée à l'application, bloquant les attaques à l'exécution.
- **SCA** (Software Composition Analysis) : analyse des dépendances open source et de leurs vulnérabilités connues (CVE).

#### Intégration dans le cycle DevSecOps
```
Code → [SAST] → Build → [SCA] → Test → [DAST/IAST] → Deploy → [RASP]
```
Le principe **shift-left** consiste à intégrer SAST dès l'IDE (plugins) et dans les pipelines CI, et DAST dans les environnements de staging avant production.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection précoce des vulnérabilités (shift-left) | SAST génère un taux élevé de faux positifs |
| Automatisation dans CI/CD (Quality Gate) | DAST nécessite un environnement d'exécution et peut être lent |
| Couverture exhaustive du code source (SAST) | DAST ne couvre pas le code non exposé aux entrées externes |
| DAST proche des conditions réelles d'attaque | Nécessite une expertise pour trier et prioriser les alertes |
| Complémentarité SAST + DAST + SCA | Coût des licences outils (Checkmarx, Veracode) |

### Acteurs et solutions du marché
- **SonarQube / SonarCloud** (Sonar) : SAST open source + commercial, très répandu, intégration native CI/CD. Couvre qualité de code + sécurité.
- **Checkmarx** : SAST et IAST enterprise, référence dans les grands comptes et secteurs réglementés.
- **CAST** : analyse de portefeuille applicatif, SAST orienté maintenabilité et conformité, fort en France.
- **Veracode** : plateforme cloud SAST + DAST + SCA, utilisée par de nombreuses banques et assurances.
- **Snyk** : spécialisé SCA (vulnérabilités des dépendances open source), très populaire en DevOps.
- **OWASP ZAP** (Zed Attack Proxy) : DAST open source de référence.
- **Burp Suite** (PortSwigger) : DAST semi-automatisé, référence des pentesters.
- **GitLab / GitHub Advanced Security** : intégration native SAST, DAST, SCA dans les plateformes de gestion de code.
- **Semgrep** : SAST open source, règles personnalisables, très rapide.

### Cas d'usage concrets
1. **Quality Gate CI/CD** : une banque configure SonarQube et Checkmarx dans son pipeline Jenkins. Tout push déclenche une analyse SAST ; si des vulnérabilités critiques (CWE top 25, OWASP A01-A10) sont détectées, le pipeline bloque le merge. Le taux de vulnérabilités en production a diminué de 60 % en 18 mois.
2. **Audit de sécurité avant mise en production** : une DSI mandate un pentest sur une nouvelle application web en staging. L'équipe utilise Burp Suite (DAST) combiné à OWASP ZAP automatisé pour identifier 3 injections SQL et 2 failles XSS non détectées par le SAST, car elles dépendaient de la configuration du serveur.
3. **Gestion des dépendances open source** : une startup SaaS utilise Snyk intégré à GitHub pour surveiller ses 400+ dépendances npm. Quand une CVE critique est publiée (ex. : Log4Shell), Snyk génère automatiquement une pull request avec la version corrigée.

### Chiffres et tendances
- **OWASP Top 10** (2021) : les 10 risques les plus critiques pour les applications web ; A03 (Injection) et A02 (Cryptographic Failures) sont détectables par SAST.
- La directive **NIS2** (2023) et la **DORA** (2025, secteur financier) imposent des exigences de sécurité applicative renforcées, accélérant l'adoption du SAST/DAST.
- **48 % des organisations** ont intégré le SAST dans leur pipeline CI/CD en 2023 (Gartner DevSecOps Survey).

## Flashcards
#flashcards
Quelle est la différence fondamentale entre SAST et DAST ? :: **SAST** analyse le code source **sans l'exécuter** (boîte blanche, shift-left) ; **DAST** teste l'application **en cours d'exécution** en simulant des attaques externes (boîte noire).

Qu'est-ce que le principe "shift-left" en sécurité applicative ? :: Intégrer les tests de sécurité le plus **tôt possible** dans le cycle de développement (dès l'IDE et le CI), pour réduire le coût de correction des vulnérabilités.

Quelle est la principale limite du SAST ? :: Un taux élevé de **faux positifs** (alertes sur du code qui n'est pas réellement vulnérable), nécessitant un tri manuel coûteux.

Que signifie SCA et quel problème résout-il ? :: **Software Composition Analysis** : analyse les **dépendances open source** d'une application pour détecter les vulnérabilités connues (CVE). Résout le problème des bibliothèques tierces non maintenues ou vulnérables.

Quels sont les 4 types d'analyse de sécurité applicative et leurs acronymes ? :: **SAST** (statique), **DAST** (dynamique), **IAST** (interactif, instrumentation à l'exécution), **RASP** (protection runtime embarquée dans l'application).

Quel outil DAST open source de référence est maintenu par l'OWASP ? :: **OWASP ZAP** (Zed Attack Proxy).

Citez 3 outils SAST commerciaux utilisés en entreprise. :: **SonarQube** (Sonar), **Checkmarx**, **Veracode** (également **CAST** en France pour les portefeuilles applicatifs).

## Sources
- OWASP. *OWASP Top 10 2021*. owasp.org.
- Gartner. *Magic Quadrant for Application Security Testing*. 2023.
- IBM Systems Sciences Institute. *Relative Cost of Fixing Defects*.
- NIST. *National Vulnerability Database (NVD)* — CWE/CVE.
- Directive NIS2 (UE) 2022/2555.
- DORA — Règlement (UE) 2022/2554 (Digital Operational Resilience Act).

## Notions liées
- [[Qualité logicielle — normes et modèles]]
- [[CMMI]]
- [[Clean Code et refactoring]]
- [[Dette technique]]
- [[Zero Trust]]
- [[Défense en profondeur]]
