---
type: notion
thèmes:
  - Développement
  - Cybersécurité
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# DevSecOps

## En bref
> **Définition** : Le DevSecOps est l'extension du DevOps intégrant la sécurité (Sec) comme responsabilité partagée et continue tout au long du cycle de développement logiciel. Le principe central est le **shift-left security** : déplacer les contrôles de sécurité le plus tôt possible dans le pipeline (dès le code, voire la conception), plutôt que de les appliquer uniquement à la fin (audit avant mise en prod). La sécurité devient du code ("Security as Code") : automatisée, versionnée, testable.
> **Pourquoi c'est important** : Les applications sont la 1re surface d'attaque des entreprises (OWASP Top 10). Corriger une vulnérabilité en production coûte 30 fois plus cher qu'en phase de développement (NIST). Intégrer la sécurité dans le pipeline CI/CD permet de détecter les failles automatiquement, sans ralentir la livraison.
> **Chiffres clés** :
> - 76 % des applications testées présentent des vulnérabilités OWASP Top 10 (Veracode, 2024).
> - Le coût moyen d'une violation de données est de 4,88 M$ (IBM Cost of Data Breach, 2024).
> - Corriger une faille coûte 6x plus en phase de test qu'en développement, et 100x plus en production (NIST).

## Approfondir

### Fonctionnement

**Shift-Left Security**
Le "shift-left" consiste à déplacer les vérifications de sécurité vers la gauche de la chaîne DevOps (côté développement) plutôt qu'à droite (côté production). En pratique :
- Les développeurs utilisent des IDE plugins détectant les vulnérabilités en temps réel (Snyk, SonarLint)
- Les scans de sécurité sont intégrés dans le pipeline CI, bloquant les merges si des failles critiques sont détectées
- Les threat models sont réalisés dès la phase de conception

**Les types d'outils de sécurité dans un pipeline DevSecOps**

| Type | Acronyme | Rôle | Exemples |
|------|----------|------|---------|
| Analyse statique du code | SAST | Détecte les vulnérabilités dans le code source | SonarQube, Checkmarx, Semgrep |
| Analyse dynamique | DAST | Teste l'application en cours d'exécution (comme un attaquant) | OWASP ZAP, Burp Suite Enterprise |
| Analyse des dépendances | SCA | Détecte les CVE dans les bibliothèques tierces | Snyk, OWASP Dependency-Check, Dependabot |
| Analyse des images conteneurs | Container Scanning | Vérifie les images Docker pour les CVE | Trivy, Clair, Anchore |
| Scan IaC | IaC Scanning | Détecte les mauvaises configurations Terraform/K8s | Checkov, tfsec, Terrascan |
| Gestion des secrets | Secrets Detection | Détecte les clés API/mots de passe dans le code | GitLeaks, TruffleHog, detect-secrets |

**Security as Code**
Les politiques de sécurité sont définies sous forme de code (YAML, OPA Rego, Python) versionné dans Git :
- **Open Policy Agent (OPA)** : moteur de politique universel (K8s, API, Terraform)
- **Kyverno** : moteur de politique natif Kubernetes
- **Gating de pipeline** : les violations bloquent automatiquement les déploiements

**Intégration dans le pipeline CI/CD**
```
Commit → SAST + Secret Detection → SCA (dépendances) → Build → 
Container Scan → IaC Scan → DAST (staging) → 
Compliance Check → (gate) → Production → CSPM/Runtime Security
```

**Modèle de responsabilité : "You build it, you secure it"**
Les équipes de développement sont responsables de la sécurité de leurs services (shift-left), accompagnées par une équipe de sécurité en rôle de plateforme et de conseil (et non de gendarme en bout de chaîne).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection précoce des vulnérabilités (moins coûteux) | Résistances culturelles (sécurité perçue comme frein) |
| Sécurité continue, non ponctuelle | Nombre important de faux positifs (bruit dans les scans) |
| Conformité automatisée et traçable (audit) | Compétences hybrides Dev+Sec rares et coûteuses |
| Réduction du délai entre découverte et remédiation | Temps de pipeline allongé si outils mal configurés |
| Responsabilisation des développeurs | Risque de "security theater" (scan sans correction) |
| Cohérence avec NIS2, RGPD, ISO 27001 | Gestion des exceptions et des waivers complexe |

### Acteurs et solutions du marché
| Catégorie | Solutions |
|-----------|-----------|
| Plateformes DevSecOps | GitLab Ultimate (SAST, DAST, SCA intégrés), GitHub Advanced Security |
| SAST | SonarQube, Checkmarx, Veracode, Semgrep |
| DAST | OWASP ZAP, Burp Suite Enterprise, Invicti |
| SCA | Snyk, Black Duck, OWASP Dependency-Check, Dependabot |
| Container/IaC Scanning | Trivy, Checkov, Prisma Cloud, Wiz |
| Secrets Management | HashiCorp Vault, Azure Key Vault, AWS Secrets Manager |
| Runtime Security | Falco (CNCF), Sysdig, Aqua Security |

### Cas d'usage concrets
1. **Microsoft (Azure)** : Microsoft a intégré le Security Development Lifecycle (SDL) dans ses pipelines CI/CD. Azure DevOps intègre nativement des scans SAST et SCA, et les politiques de sécurité sont appliquées automatiquement via Azure Policy (OPA-based). Résultat : 50 % de réduction des vulnérabilités critiques entre 2020 et 2023.
2. **La Poste Groupe** : déploiement d'une plateforme DevSecOps (GitLab + Trivy + Vault) pour sécuriser les 200+ applications du groupe. Les scans automatiques ont permis d'identifier 3 000 vulnérabilités en 6 mois, dont 40 critiques, avec un MTTR divisé par 4.
3. **Capital One (USA)** : après la violation de données de 2019 (100 millions de clients exposés via une mauvaise config cloud), la banque a refondu son approche sécurité en intégrant du IaC scanning systématique (Checkov) et du CSPM dans tous les pipelines CI/CD.

### Chiffres et tendances
- 90 % des organisations déclarent vouloir intégrer davantage la sécurité dans leurs pipelines DevOps (Gartner, 2024).
- Le marché DevSecOps atteindra 23 Md$ en 2028 (MarketsandMarkets).
- SBOM (Software Bill of Materials) devient obligatoire pour les logiciels vendus au gouvernement américain (Executive Order 14028, 2021) et tend à se généraliser en Europe (CRA).
- Le Cyber Resilience Act (CRA) européen impose la sécurité by design et by default pour tous les produits numériques dès 2027.

## Flashcards
#flashcards
- Qu'est-ce que le "shift-left security" ? :: Le principe de déplacer les contrôles de sécurité le plus tôt possible dans le cycle de développement (dès le code, voire la conception) plutôt qu'en fin de chaîne, réduisant le coût et le délai de remédiation.
- Quelle est la différence entre SAST et DAST ? :: SAST (Static Application Security Testing) analyse le code source sans l'exécuter pour détecter des vulnérabilités. DAST (Dynamic Application Security Testing) teste l'application en cours d'exécution, simulant le comportement d'un attaquant.
- Qu'est-ce que le SCA (Software Composition Analysis) ? :: Un type d'analyse qui examine les bibliothèques et dépendances tierces d'une application pour détecter des vulnérabilités connues (CVE) et des problèmes de licence.
- Pourquoi corriger une faille en production est-il si coûteux ? :: Selon le NIST, corriger en production coûte 100x plus qu'en développement, car cela implique un hotfix urgent, une fenêtre de maintenance, des tests de non-régression, et potentiellement un incident de sécurité public avec impact réputationnel.
- Qu'est-ce que l'Open Policy Agent (OPA) ? :: Un moteur de politique open source permettant de définir et d'appliquer des règles de sécurité et de conformité sous forme de code (langage Rego), utilisé dans Kubernetes, les pipelines CI/CD et les APIs.
- Qu'est-ce qu'un SBOM ? :: Un Software Bill of Materials — un inventaire exhaustif des composants, bibliothèques et dépendances d'une application, permettant d'identifier rapidement les composants vulnérables (ex. : Log4Shell).
- Quelle réglementation européenne impose la sécurité by design pour les produits numériques ? :: Le Cyber Resilience Act (CRA), entré en vigueur en 2024, qui impose des exigences de cybersécurité pour tous les produits contenant des éléments numériques vendus dans l'UE, avec des obligations applicables à partir de 2027.

## Sources
- OWASP Top 10 : https://owasp.org/Top10/
- IBM Cost of a Data Breach Report 2024 : https://www.ibm.com/reports/data-breach
- NIST, "The Economic Impacts of Inadequate Infrastructure for Software Testing", 2002
- Gartner, "DevSecOps: How to Seamlessly Integrate Security Into DevOps", 2024
- Règlement européen Cyber Resilience Act (CRA), 2024

## Notions liées
- [[DevOps]]
- [[CI - CD]]
- [[ISO 27001 - 27002]]
- [[RGPD]]
- [[NIS2]]
- [[Défense en profondeur]]
- [[Zero Trust]]
- [[Infrastructure as Code (IaC)]]
