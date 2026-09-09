---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Clean Code et refactoring

## En bref
> **Définition** : Le Clean Code désigne un ensemble de principes et pratiques permettant d'écrire un code lisible, maintenable et évolutif. Le refactoring consiste à restructurer le code existant sans modifier son comportement observable, afin d'améliorer sa qualité interne. Ces deux approches constituent le socle des pratiques d'ingénierie logicielle de qualité.
> **Pourquoi c'est important** : Dans une équipe de développement, un code difficile à lire coûte cher : un développeur passe en moyenne **70 % de son temps à lire du code** plutôt qu'à en écrire. Le Clean Code et le refactoring permettent de réduire la dette technique, d'accélérer l'onboarding et de diminuer les bugs de régression lors des évolutions.
> **Chiffres clés** :
> - Les développeurs passent **58 % de leur temps** à comprendre du code existant (developersurvey.com / études IEEE).
> - Un code avec une complexité cyclomatique > 10 présente un risque de défauts **40 % plus élevé** (McCabe & Associates).
> - Le refactoring représente environ **25 % du temps de développement** dans les équipes pratiquant l'agilité mature (VersionOne / Digital.ai Survey).

## Approfondir

### Fonctionnement

#### Clean Code — principes fondamentaux (Robert C. Martin, 2008)
Robert C. Martin ("Uncle Bob") a formalisé les principes du Clean Code dans son ouvrage éponyme. Les règles principales :

**Nommage**
- Les noms doivent être **révélateurs d'intention** : `calculateMonthlyInterest()` plutôt que `calc()`.
- Éviter les abréviations cryptiques, les préfixes hongrois.
- Les noms de classes sont des noms, les méthodes des verbes.

**Fonctions**
- Une fonction doit faire **une seule chose** (Single Responsibility Principle).
- Taille idéale : **5 à 10 lignes maximum**.
- Pas plus de **3 paramètres** (au-delà, créer un objet paramètre).
- Pas d'effets de bord cachés.

**Commentaires**
- Le bon code se documente lui-même via les noms. Les commentaires sont un **signe d'échec** à écrire du code clair.
- Exceptions : Javadoc API, explications d'algorithmes complexes, TODO temporaires.

**Formatage**
- Cohérence dans toute l'équipe (via des outils : Prettier, ESLint, Checkstyle).
- Principe de la **règle du journal** : le code se lit de haut en bas comme un article (fonctions de haut niveau en premier).

**Gestion des erreurs**
- Préférer les exceptions aux codes d'erreur.
- Ne jamais retourner `null` — utiliser Optional (Java) ou Maybe (Haskell/F#).
- Logger les erreurs sans les masquer.

#### Principes SOLID (Martin, 2000)
- **S** — Single Responsibility Principle : une classe = une raison de changer.
- **O** — Open/Closed Principle : ouvert à l'extension, fermé à la modification.
- **L** — Liskov Substitution Principle : les sous-classes sont substituables aux classes parentes.
- **I** — Interface Segregation Principle : préférer plusieurs interfaces spécifiques à une interface générale.
- **D** — Dependency Inversion Principle : dépendre des abstractions, pas des implémentations.

#### YAGNI, DRY, KISS
- **YAGNI** (You Aren't Gonna Need It) : ne pas développer des fonctionnalités qui ne sont pas encore nécessaires. Principe XP (Kent Beck).
- **DRY** (Don't Repeat Yourself) : toute connaissance doit avoir une représentation unique et non ambiguë dans le système. Éviter la duplication.
- **KISS** (Keep It Simple, Stupid) : la solution la plus simple est généralement la meilleure.

#### Code Smell (Martin Fowler)
Les **code smells** sont des symptômes de mauvaise conception qui ne sont pas nécessairement des bugs, mais qui indiquent un problème structurel :

| Code Smell | Description |
|------------|-------------|
| Duplicated Code | Code copié-collé à plusieurs endroits |
| Long Method | Méthode trop longue (> 20 lignes) |
| Large Class | Classe avec trop de responsabilités |
| Long Parameter List | Méthode avec trop de paramètres |
| Divergent Change | Une classe modifiée pour des raisons très différentes |
| Shotgun Surgery | Une modification nécessite des changements dans de nombreuses classes |
| Feature Envy | Une méthode qui utilise trop les données d'une autre classe |
| Data Clumps | Groupes de données qui apparaissent toujours ensemble |
| Primitive Obsession | Utilisation de types primitifs à la place d'objets |
| Switch Statements | Utilisation excessive de switch/if-else polymorphique |

#### Complexité cyclomatique (McCabe, 1976)
La **complexité cyclomatique** (CC) mesure le nombre de chemins linéairement indépendants dans le code :
- `CC = E - N + 2P` (E = arêtes, N = noeuds, P = composantes connexes)
- En pratique : CC = nombre de branches conditionnelles (if, for, while, case) + 1.

| CC | Risque |
|----|--------|
| 1-10 | Faible, code simple |
| 11-20 | Modéré, attention |
| 21-50 | Élevé, refactoring conseillé |
| > 50 | Très élevé, refactoring urgent |

#### Refactoring (Martin Fowler, 1999)
Le refactoring est un processus **discipliné** de restructuration du code :
- Chaque refactoring est **atomique** et préservé par les tests.
- Catalogue de **refactorings** (Fowler) : Extract Method, Extract Class, Rename, Move Method, Replace Temp with Query, Introduce Parameter Object, etc.
- **Règle du Boy Scout** (Martin) : toujours laisser le code dans un meilleur état qu'on l'a trouvé.
- Nécessite une **couverture de tests suffisante** pour garantir la non-régression.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduit la dette technique et les coûts de maintenance | Nécessite discipline et culture d'équipe forte |
| Améliore la lisibilité et réduit le temps de compréhension | Le refactoring sans tests est risqué (régression possible) |
| Facilite l'onboarding des nouveaux développeurs | Résistance au refactoring ("ça marche, on ne touche pas") |
| Réduit les bugs de régression lors des évolutions | Difficulté à justifier le temps passé au refactoring (ROI indirect) |
| Base nécessaire pour le TDD et l'intégration continue | Application stricte peut devenir dogmatique (sur-engineering) |

### Acteurs et solutions du marché
- **SonarQube** : détection automatisée des code smells, calcul de la complexité cyclomatique, mesure de la duplication.
- **ReSharper** (JetBrains, .NET) : refactoring assisté, détection de code smell en temps réel dans l'IDE.
- **IntelliJ IDEA** (JetBrains) : refactoring automatisé pour Java/Kotlin (Extract Method, Rename, Move).
- **ESLint / Prettier** (JavaScript/TypeScript) : formatage et règles de style.
- **Checkstyle / PMD** (Java) : vérification des règles de nommage et de complexité.
- **CodeClimate** : analyse de la maintenabilité, détection des code smells.

### Cas d'usage concrets
1. **Refactoring d'une méthode complexe** : une équipe découvre une méthode de 300 lignes (God Method) avec une complexité cyclomatique de 45. Après extraction de 12 sous-méthodes nommées explicitement, la complexité tombe à 4 pour la méthode principale. Les 847 tests existants n'ont aucune régression.
2. **Application du principe YAGNI** : une équipe de startup évite d'implémenter un système de plugins "pour le futur" qui n'était pas demandé dans le cahier des charges. Six mois plus tard, le besoin n'est toujours pas apparu, économisant 3 semaines de développement et de maintenance.
3. **Culture Clean Code dans une ESN** : Sopra Steria impose à ses équipes des règles Clean Code automatiquement vérifiées en CI (SonarQube). Les revues de code incluent une checklist Clean Code. Le taux de défauts en production a diminué de 35 % en un an sur les projets appliquant ces pratiques.

### Chiffres et tendances
- Le livre *Clean Code* de Robert C. Martin est l'un des ouvrages techniques les plus vendus, avec plus de **500 000 exemplaires** vendus.
- **87 % des développeurs** estiment que la qualité du code est plus importante que la rapidité de livraison (Stack Overflow Developer Survey 2023).
- L'adoption du **Clean Code dans les formations initiales** (écoles d'ingénieurs, IUT) est en forte progression depuis 2015.

## Flashcards
#flashcards/Développement/Clean_Code_et_refactoring
Quelle est la règle fondamentale du Clean Code concernant les fonctions ? :: Une fonction doit faire **une seule chose** (Single Responsibility), avec idéalement 5-10 lignes et maximum 3 paramètres.

Que signifie YAGNI et à quel mouvement appartient ce principe ? :: **You Aren't Gonna Need It** — n'implémentez pas ce qui n'est pas nécessaire maintenant. Principe issu de l'**Extreme Programming** (Kent Beck).

Qu'est-ce que la complexité cyclomatique et quel est le seuil à partir duquel un refactoring est conseillé ? :: Métrique de **McCabe (1976)** mesurant le nombre de chemins d'exécution indépendants. Refactoring conseillé dès **CC > 20**, urgent au-delà de 50.

Citez 4 code smells identifiés par Martin Fowler. :: Parmi : Duplicated Code, Long Method, Large Class, Long Parameter List, Feature Envy, Shotgun Surgery, Divergent Change, Primitive Obsession.

Que signifie DRY et comment l'appliquer ? :: **Don't Repeat Yourself** : toute connaissance doit avoir une représentation **unique et non ambiguë** dans le système. En pratique : extraire les duplications en fonctions ou classes réutilisables.

Quels sont les 5 principes SOLID ? :: **S**ingle Responsibility, **O**pen/Closed, **L**iskov Substitution, **I**nterface Segregation, **D**ependency Inversion.

Quelle est la "règle du Boy Scout" appliquée au code ? :: Toujours laisser le code dans un **meilleur état** qu'on l'a trouvé — même si on ne fait qu'un petit refactoring lors de chaque modification.

## Sources
- Martin, R.C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
- Fowler, M. (1999, 2e éd. 2018). *Refactoring: Improving the Design of Existing Code*. Addison-Wesley.
- McCabe, T.J. (1976). *A Complexity Measure*. IEEE Transactions on Software Engineering.
- Beck, K. (1999). *Extreme Programming Explained*. Addison-Wesley.
- Stack Overflow Developer Survey 2023.

## Notions liées
- [[Dette technique]]
- [[TDD - BDD]]
- [[Analyse de code (SAST - DAST)]]
- [[Architecture logicielle]]
- [[Qualité logicielle — normes et modèles]]
- [[Maintenance logicielle]]
