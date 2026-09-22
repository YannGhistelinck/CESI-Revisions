---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# TDD - BDD

![[N — TDD - BDD.mp3]]
## En bref
> **Définition** : Le **TDD** (Test-Driven Development) est une pratique de développement dans laquelle on écrit un test automatisé avant le code de production, puis on fait passer le test avec le minimum de code, puis on refactorise. Le **BDD** (Behavior-Driven Development) étend le TDD en exprimant les comportements attendus dans un langage naturel partagé avec les parties prenantes non techniques. Ces pratiques s'inscrivent dans un écosystème plus large incluant la revue de code et le pair programming.
> **Pourquoi c'est important** : Pour une DSI, le TDD et le BDD permettent de réduire les bugs en production, de documenter les comportements attendus, d'accélérer le refactoring en toute sécurité et d'améliorer la communication entre équipes techniques et métier. Ils sont des piliers de l'Extreme Programming et de l'agilité mature.
> **Chiffres clés** :
> - Les équipes pratiquant le TDD constatent une réduction des défauts de **40 à 80 %** en production (Microsoft Research / IBM, 2008).
> - La mise en place du TDD allonge le temps de développement de **15 à 35 %** à court terme, mais réduit le coût de maintenance de **40 à 90 %** à long terme (Nagappan et al., 2008).
> - **52 % des développeurs** utilisent le TDD régulièrement (Stack Overflow Developer Survey 2023).

## Approfondir

### Fonctionnement

#### TDD — Cycle Red-Green-Refactor (Kent Beck, 2003)
Le TDD est structuré autour d'un cycle très court (quelques minutes) en 3 phases :

1. **Red** : écrire un test qui échoue (le code n'existe pas encore). Le test définit le comportement attendu.
2. **Green** : écrire le minimum de code de production nécessaire pour faire passer le test (même si le code est "laid").
3. **Refactor** : améliorer la qualité du code (Clean Code, SOLID) sans modifier le comportement — les tests garantissent la non-régression.

```
Écrire test (Red) → Faire passer (Green) → Refactoriser (Refactor) → Écrire test suivant...
```

**Règles des 3 lois du TDD** (Robert C. Martin) :
1. On n'est pas autorisé à écrire du code de production avant d'avoir un test en échec.
2. On n'est pas autorisé à écrire plus de code de test que nécessaire pour échouer.
3. On n'est pas autorisé à écrire plus de code de production que nécessaire pour faire passer le test.

**Pyramid de tests** :
- **Tests unitaires** (base) : rapides, isolés, nombreux. TDD cible principalement ce niveau.
- **Tests d'intégration** (milieu) : vérifient les interactions entre composants.
- **Tests end-to-end / UI** (sommet) : lents, fragiles, peu nombreux.

#### BDD — Behavior-Driven Development (Dan North, 2006)
Dan North a formalisé le BDD comme une évolution du TDD, répondant à la question : "Comment savoir quel test écrire en premier ?"

Le BDD se concentre sur les **comportements** du système plutôt que sur les tests unitaires de bas niveau, en utilisant un langage partagé entre tous les acteurs.

**Format Gherkin** (Given-When-Then) :
```gherkin
Feature: Virement bancaire

  Scenario: Virement réussi entre deux comptes du même client
    Given le client "Alice" a un solde de 1000 EUR sur son compte courant
    And le client "Alice" a un compte épargne
    When Alice effectue un virement de 200 EUR vers son compte épargne
    Then le solde du compte courant d'Alice est de 800 EUR
    And le solde du compte épargne d'Alice est de 200 EUR
```

Le fichier `.feature` est lisible par les non-développeurs (PO, QA, métier). Les **step definitions** implémentent chaque étape en code.

**Outils BDD** :
- **Cucumber** (Java, Ruby, JavaScript) : le plus populaire.
- **SpecFlow** (.NET) : équivalent Cucumber pour C#.
- **Behave** (Python).
- **JBehave** (Java, créé par Dan North).
- **Playwright / Cypress** + plugins BDD pour les tests E2E.

#### ATDD — Acceptance Test-Driven Development
L'**ATDD** est une variante où les **tests d'acceptance** (définis avec le client) sont écrits **avant** le développement. BDD et ATDD se recoupent fortement : le BDD est souvent l'outil de l'ATDD.

Processus ATDD :
1. Discussion (3 amigos : développeur, QA, PO).
2. Rédaction des critères d'acceptance en Gherkin.
3. Implémentation guidée par ces critères.
4. Validation avec le client.

#### Revue de code (Code Review)
La **revue de code** est une pratique complémentaire dans laquelle un ou plusieurs développeurs examinent le code d'un pair avant intégration.

**Objectifs** :
- Détection des bugs et des problèmes de sécurité avant production.
- Partage des connaissances et réduction du bus factor.
- Respect des standards de code (Clean Code, conventions d'équipe).
- Amélioration collective de la qualité.

**Bonnes pratiques** :
- Pull Request de petite taille (< 400 lignes) : plus rapide à relire, moins de bugs.
- Revues en moins de 24h (éviter les blocages).
- Commentaires constructifs et factuels, pas personnels.
- Utiliser des checklists de revue.
- Distinguer "blocking" (doit être corrigé) de "suggestion" (amélioration optionnelle).

**Outils** : GitHub Pull Requests, GitLab Merge Requests, Gerrit, Bitbucket, Phabricator.

#### Pair Programming
Le **pair programming** est une pratique XP dans laquelle **deux développeurs** travaillent ensemble sur le même ordinateur simultanément :
- **Driver** : écrit le code, pense tactiquement.
- **Navigator** : observe, réfléchit stratégiquement, détecte les erreurs.

**Variantes** :
- **Mob Programming** : toute l'équipe travaille ensemble sur un même problème.
- **Ping-Pong** : un développeur écrit le test (TDD), l'autre écrit le code pour le faire passer, alternance.

**Avantages** : réduction des bugs (-15 % selon Laurie Williams, 2000), transfert de connaissances, meilleure conception. **Inconvénient** : deux personnes pour une tâche (ROI à justifier — généralement positif sur les tâches complexes).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| TDD : réduction drastique des bugs en production | TDD : investissement initial en temps de 15-35 % |
| BDD : alignement métier-technique via langage partagé | BDD : maintenance des scénarios Gherkin coûteuse |
| Refactoring sécurisé (filet de tests) | Difficulté à tester certains composants (UI, legacy) |
| Documentation vivante (tests = spec exécutable) | Courbe d'apprentissage (TDD requiert un changement de mindset) |
| Code Review : partage de connaissances et qualité | Code Review : peut créer des frictions et des blocages |
| Pair Programming : bus factor réduit | Pair Programming : résistance culturelle, coût apparent |

### Acteurs et solutions du marché
**Frameworks TDD/BDD** :
- **JUnit 5 + Mockito** (Java) : standard de facto pour les tests unitaires Java.
- **Jest** (JavaScript/TypeScript) : framework de test rapide, natif Node.js/React.
- **pytest** (Python) : flexible, très populaire dans l'écosystème data/ML.
- **NUnit / xUnit** (.NET) : tests unitaires C#.
- **Cucumber** (multi-langage) : BDD avec Gherkin.
- **Playwright / Cypress** : tests E2E automatisés.

**Outils de couverture** :
- **JaCoCo** (Java), **Istanbul/c8** (JS), **Coverage.py** (Python) : mesure de la couverture de code.
- **SonarQube** : intègre la couverture, seuils de quality gate.

**Intégration CI/CD** :
- **GitHub Actions, GitLab CI, Jenkins, CircleCI** : exécution automatique des tests à chaque commit.

### Cas d'usage concrets
1. **TDD sur une API REST** : une équipe développe une API de gestion de commandes. Pour chaque endpoint, elle commence par écrire un test d'intégration (fail), implémente le minimum de code (pass), refactorise. Résultat : 95 % de couverture, 0 bug de régression lors des 8 mois de développement et 12 releases.
2. **BDD pour une DSI bancaire** : une DSI met en place le BDD pour les fonctionnalités de conformité réglementaire. Les scénarios Gherkin sont rédigés par les juristes et les analystes métier, puis implémentés par les développeurs. Les scénarios servent à la fois de spécifications, de tests de recette et de documentation réglementaire. Le taux d'anomalies lors de la recette client chute de 70 %.
3. **Pair Programming chez Pivotal/VMware** : Pivotal Labs (aujourd'hui VMware Tanzu) pratique le pair programming **à 100 % du temps** de développement, avec rotation quotidienne des paires. Cette pratique élimine le bus factor et garantit que 2 personnes connaissent chaque ligne de code à tout moment.

### Chiffres et tendances
- **Microsoft, IBM et Google** ont démontré que le TDD réduit les bugs de 40-80 % (études de terrain 2008-2015).
- **GitHub** rapporte qu'une Pull Request de < 250 lignes est reviewée 3x plus rapidement et avec plus de commentaires pertinents.
- Le **BDD** est adopté par **34 % des équipes agiles** dans les grandes organisations (VersionOne / Digital.ai State of Agile 2023).

## Flashcards
#flashcards/Développement/TDD_BDD
Quelles sont les 3 phases du cycle TDD et que représente chacune ? :: **Red** (écrire un test qui échoue), **Green** (écrire le minimum de code pour faire passer le test), **Refactor** (améliorer la qualité du code sans changer le comportement).

Quelle est la différence entre TDD et BDD ? :: Le **TDD** se concentre sur les tests unitaires techniques ; le **BDD** (Dan North, 2006) étend le TDD en exprimant les comportements dans un **langage naturel** (Gherkin Given-When-Then) partagé avec les parties prenantes non techniques.

Qu'est-ce que le format Gherkin et quels mots-clés utilise-t-il ? :: Langage de description des comportements (BDD) : **Given** (contexte initial), **When** (action déclenchante), **Then** (résultat attendu). Lisible par tous (développeurs, PO, métier).

Quels sont les 3 niveaux de la pyramide de tests (du bas vers le haut) ? :: **Tests unitaires** (base : rapides, nombreux), **tests d'intégration** (milieu), **tests end-to-end / UI** (sommet : lents, peu nombreux).

Quelle est la règle pratique sur la taille d'une Pull Request pour une revue de code efficace ? :: Moins de **400 lignes** (idéalement < 250). Les PR trop grandes sont difficiles à relire et génèrent moins de commentaires utiles.

Qu'est-ce que le pair programming et quels sont les rôles du Driver et du Navigator ? :: Deux développeurs travaillent ensemble : le **Driver** écrit le code (tactique), le **Navigator** observe et réfléchit stratégiquement (détecte erreurs, pense à l'architecture). Alternance régulière des rôles.

De combien le TDD réduit-il les bugs en production selon les études Microsoft et IBM (2008) ? :: De **40 à 80 %** de réduction des défauts en production, avec un surcoût de développement initial de 15 à 35 %.

## Sources
- Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley.
- North, D. (2006). *Introducing BDD*. dannorth.net.
- Nagappan, N., Maximilien, E.M., Bhat, T., Williams, L. (2008). *Realizing quality improvement through test driven development*. Empirical Software Engineering, 13(3).
- Williams, L. & Kessler, R. (2000). *All I really need to know about pair programming I learned in kindergarten*. Communications of the ACM.
- Martin, R.C. (2011). *The Clean Coder*. Prentice Hall.
- Stack Overflow Developer Survey 2023.

## Notions liées
- [[Clean Code et refactoring]]
- [[Architecture logicielle]]
- [[Dette technique]]
- [[Analyse de code (SAST - DAST)]]
- [[CMMI]]
- [[Qualité logicielle — normes et modèles]]
