---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Tests logiciels

![[N — Tests logiciels.mp3]]
## En bref
> **Définition** : Les tests logiciels désignent l'ensemble des activités visant à évaluer la qualité d'un système informatique en vérifiant qu'il se comporte conformément aux exigences fonctionnelles et non fonctionnelles. Ils couvrent des niveaux allant du code unitaire à l'intégration système, et des types allant de la performance à la sécurité.
> **Pourquoi c'est important** : La qualité logicielle est un enjeu stratégique : un bug en production coûte en moyenne 30x plus cher à corriger qu'un bug détecté en phase de développement (IBM Systems Sciences Institute). Les tests permettent de livrer plus vite avec plus de confiance, condition nécessaire au DevOps et au déploiement continu.
> **Chiffres clés** :
> - Les bugs logiciels coûtent environ 2 400 Md$ par an à l'économie mondiale (Consortium for Information and Software Quality — CISQ, 2022).
> - Les entreprises qui automatisent leurs tests déploient 208x plus fréquemment (DORA State of DevOps 2021).
> - La couverture de tests > 80 % est corrélée avec un Change Failure Rate 3x inférieur (DORA, 2022).

## Approfondir

### Fonctionnement

**La pyramide des tests (Mike Cohn)**
Structure hiérarchique guidant la répartition des tests : beaucoup de tests unitaires (base), moins de tests d'intégration (milieu), peu de tests end-to-end (sommet). Plus on monte, plus les tests sont lents, coûteux et fragiles.

**Niveaux de tests**
1. **Tests unitaires** : testent une unité isolée de code (fonction, méthode, classe) en mockant les dépendances. Rapides (< 1 ms par test), nombreux. Frameworks : JUnit (Java), pytest (Python), Jest (JavaScript), NUnit (.NET).
2. **Tests d'intégration** : testent l'interaction entre plusieurs composants (service + base de données, service + API externe). Détectent les problèmes de contrat d'interface. Frameworks : Testcontainers, Spring Boot Test.
3. **Tests fonctionnels / end-to-end (E2E)** : simulent le parcours complet d'un utilisateur à travers l'interface. Outils : Selenium, Playwright, Cypress, Puppeteer.
4. **Tests de contrat (Consumer-Driven Contract)** : valident que deux services communiquent conformément à un contrat défini (ex : Pact). Essentiels dans les architectures microservices.

**Types de tests spécialisés**
- **Tests de performance** : mesurent le temps de réponse, le débit et la stabilité sous charge. Outils : JMeter, k6, Gatling, Locust.
- **Tests de sécurité (SAST / DAST)** : SAST (Static Application Security Testing) analyse le code source sans exécution ; DAST (Dynamic Application Security Testing) attaque l'application en cours d'exécution. Outils : SonarQube, OWASP ZAP, Burp Suite, Checkmarx.
- **Tests de régression** : s'assurent qu'une modification n'a pas introduit de régressions sur les fonctionnalités existantes. Souvent automatisés et intégrés au pipeline CI/CD.
- **Mutation Testing** : injecte des mutations délibérées dans le code source (ex : remplace `>` par `>=`) et vérifie que les tests existants les détectent. Mesure la qualité réelle des tests, pas seulement leur couverture. Outils : PIT (Java), Mutmut (Python), Stryker (JavaScript).
- **Fuzzing (Fuzz Testing)** : génère des entrées aléatoires ou semi-aléatoires pour découvrir des comportements inattendus (crashs, vulnérabilités). Utilisé par Google (OSS-Fuzz), Microsoft, Apple. Outils : AFL++, libFuzzer, Atheris.

**Normes et certifications**
- **ISTQB (International Software Testing Qualifications Board)** : certification de référence internationale pour les testeurs logiciels. Niveaux Foundation, Advanced (Analyst, Technical, Manager), Expert. 1,2 million de certifiés dans le monde.
- **ISO/IEC 29119** : norme internationale sur les processus, la documentation et les techniques de test logiciel. Remplace les anciennes normes IEEE 829 et BS 7925.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection précoce des bugs (shift-left testing) | Investissement initial en temps et outillage élevé |
| Confiance accrue pour le déploiement continu | Tests mal écrits peuvent donner une fausse confiance |
| Documentation vivante du comportement attendu | Maintenance des tests end-to-end coûteuse (fragilité) |
| Réduction du coût de correction des bugs | Couverture élevée ≠ absence de bugs (faux sentiment de sécurité) |
| Feedback immédiat sur les régressions en CI/CD | Le mutation testing et le fuzzing sont coûteux en ressources de calcul |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| JUnit / pytest / Jest | Frameworks de tests unitaires Java, Python, JavaScript |
| Playwright / Cypress / Selenium | Automatisation de tests E2E et UI |
| SonarQube | Analyse statique de la qualité et sécurité du code |
| OWASP ZAP | Scanner de sécurité applicative DAST open source |
| k6 / Gatling / JMeter | Tests de charge et de performance |
| Pact | Tests de contrat pour architectures microservices |
| PIT Mutation Testing | Framework de mutation testing pour Java |
| Testcontainers | Tests d'intégration avec des conteneurs Docker éphémères |
| xRay (Jira) | Gestion des plans de test intégrée à Jira |

### Cas d'usage concrets
1. **Google** : pratique le "Testing at Scale" avec des centaines de millions de tests automatisés exécutés chaque jour. Utilise OSS-Fuzz pour tester plus de 650 projets open source critiques en continu.
2. **Airbus** : applique les normes DO-178C (certification logicielle aéronautique) imposant une couverture MC/DC (Modified Condition/Decision Coverage) de 100 % sur les logiciels critiques. Tests de mutation obligatoires pour les systèmes de contrôle de vol.
3. **ING Bank** : a mis en place une stratégie "shift-left" avec des tests de sécurité SAST intégrés à chaque pull request, réduisant les vulnérabilités détectées en production de 60 % en 18 mois.

### Chiffres et tendances
- Le coût moyen d'un incident de production dû à un bug est de 300 000 $ pour une grande entreprise (CISQ, 2022).
- Les tests de sécurité (SAST/DAST) sont intégrés dans les pipelines CI/CD de 58 % des organisations (GitLab DevSecOps Survey 2023).
- L'adoption du mutation testing progresse de 30 % par an dans les équipes avancées.
- Le fuzzing est désormais requis dans les programmes de Bug Bounty des GAFAM.

## Flashcards
#flashcards/Développement/Tests_logiciels
- Qu'est-ce que la pyramide des tests ? :: Un modèle (Mike Cohn) préconisant beaucoup de tests unitaires (rapides, fiables), moins de tests d'intégration, et peu de tests E2E (lents, fragiles, coûteux).
- Quelle est la différence entre SAST et DAST ? :: SAST analyse le code source statiquement (sans exécution) ; DAST attaque l'application en cours d'exécution pour détecter des vulnérabilités dynamiques.
- Qu'est-ce que le mutation testing ? :: Une technique qui injecte des mutations dans le code source pour vérifier que les tests existants les détectent ; mesure la qualité réelle des tests.
- Qu'est-ce que le fuzzing ? :: Une technique qui génère des entrées aléatoires ou semi-aléatoires pour découvrir des comportements inattendus (crashs, vulnérabilités) dans un programme.
- Qu'est-ce que l'ISTQB ? :: L'International Software Testing Qualifications Board — organisme de certification de référence pour les testeurs logiciels, avec 1,2 million de certifiés.
- Qu'est-ce qu'un test de contrat (Consumer-Driven Contract) ? :: Un test qui valide que deux services communiquent conformément à un contrat défini ; essentiel dans les architectures microservices (outil : Pact).
- Pourquoi la couverture de code à 100 % n'est-elle pas suffisante ? :: Elle mesure les lignes exécutées, pas la pertinence des assertions. Le mutation testing révèle si les tests détectent réellement les bugs.

## Sources
- ISTQB Glossary : https://glossary.istqb.org/
- ISO/IEC 29119 Software Testing : https://www.iso.org/standard/81291.html
- CISQ Cost of Poor Software Quality in the US, 2022 : https://www.it-cisq.org/
- DORA State of DevOps Report 2022 : https://dora.dev/research/
- Google OSS-Fuzz : https://github.com/google/oss-fuzz
- OWASP Testing Guide : https://owasp.org/www-project-web-security-testing-guide/

## Notions liées
- [[DORA Metrics]]
- [[IA et automatisation des tests]]
- [[Chaos Engineering]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[ISO 27001 - 27002]]
- [[Défense en profondeur]]
