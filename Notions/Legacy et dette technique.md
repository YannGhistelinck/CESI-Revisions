---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Développement
statut: pas vu
dernière_révision: 
---

# Legacy et dette technique

![[N — Legacy et dette technique.mp3]]
## En bref
> **Définition** : Un système legacy est une application ou une infrastructure ancienne, difficile à maintenir et à faire évoluer, mais qui reste en production car elle assure des fonctions métier critiques. La dette technique (concept de Ward Cunningham, 1992) désigne l'accumulation de compromis de conception et de développement qui ralentissent les futures évolutions et augmentent le coût de maintenance. Plus elle est ignorée, plus les "intérêts" à payer augmentent.
> **Pourquoi c'est important** : Pour une DSI, la dette technique et les systèmes legacy consomment entre 60 et 80 % du budget IT en maintenance, laissant peu de ressources pour l'innovation. La modernisation est un enjeu stratégique majeur, notamment pour préparer les migrations cloud et répondre aux exigences de performance et de sécurité modernes.
> **Chiffres clés** :
> - 60 à 80 % du budget IT des grandes entreprises est consacré à la maintenance des systèmes existants (Gartner, 2022)
> - La dette technique mondiale est estimée à 1 520 Md$ (1,52 trillion de dollars) par le CAST Research Labs en 2022
> - Le coût de correction d'un bug augmente d'un facteur 10 à chaque phase du cycle de vie où il n'est pas traité (NIST, étude classique)

## Approfondir

### Fonctionnement

**Définition de la dette technique (Ward Cunningham)**
Ward Cunningham a introduit la métaphore de la dette technique en 1992 : "Si on fait un code pas propre maintenant pour livrer plus vite, c'est comme emprunter de l'argent. On avancera vite à court terme, mais on devra rembourser avec des intérêts (ralentissement des développements futurs)." La dette peut être délibérée (choix conscient d'une solution rapide) ou accidentelle (manque de compétences ou de vision initiale).

**Les types de dette technique**
- **Dette de conception** : architecture mal pensée, couplage fort entre modules, absence de séparation des préoccupations
- **Dette de code** : code non testé, absence de documentation, duplication, non-respect des standards (code smell)
- **Dette de tests** : absence ou insuffisance des tests automatisés, tests manuels chronophages
- **Dette d'infrastructure** : serveurs obsolètes, OS en fin de vie (EOL), dépendances non mises à jour (failles de sécurité)
- **Dette de données** : schémas de bases de données rigides, données dupliquées ou incohérentes, absence de data quality

**Systèmes legacy : caractéristiques**
Un système est qualifié de legacy lorsqu'il cumule plusieurs des caractéristiques suivantes : technologie obsolète (COBOL, PowerBuilder, VB6), documentation inexistante ou incomplète, absence de tests automatisés, développeurs connaissant le système partis ou retraités, impossible à modifier sans régression, dépendances opaques, couplage fort avec d'autres systèmes. Il reste en production car il remplit une fonction critique et son remplacement est perçu comme trop risqué.

**Modernisation : les grandes approches**
1. **Maintenance pure** : corriger les bugs, mettre à jour les dépendances de sécurité, sans évolution fonctionnelle. Stratégie court terme.
2. **Refactoring (restructuration interne)** : améliorer la structure du code sans changer son comportement externe. Technique popularisée par Martin Fowler ("Refactoring: Improving the Design of Existing Code", 1999). Exemples : extraction de méthode, remplacement de conditions complexes par des patterns.
3. **Réarchitecture** : repenser l'architecture globale (passage de monolithe à microservices, adoption d'une architecture hexagonale).
4. **Remplacement** : remplacer l'application par une solution packagée (ERP, SaaS) ou en reconstruire une from scratch.
5. **Encapsulation/Wrapping** : encapsuler le système legacy derrière une API REST pour le consommer comme un service, sans toucher au code. Solution de façade.

**Refactoring stratégique**
Le refactoring n'est pas seulement technique : c'est une décision stratégique qui doit être arbitrée par la DSI. Il faut évaluer le ratio coût/bénéfice : refactorer un module peu utilisé est inutile, refactorer le cœur d'un système critique peut débloquer 2 ans de projets. La "Boy Scout Rule" (laisser le code plus propre qu'on l'a trouvé) est une pratique culturelle efficace pour gérer la dette de manière continue.

**Mesure de la dette technique**
Outils d'analyse statique de code : SonarQube (SQALE Rating), Coverity, Checkmarx. Métriques : Technical Debt Ratio (dette / coût de développement), code coverage, cyclomatic complexity, nombre de code smells. Le SQALE Rating de SonarQube note le code de A (très propre) à E (dette critique) et estime le temps de remboursement en jours-hommes.

### Avantages / Inconvénients
| Avantages du legacy (pourquoi il reste) | Inconvénients / coûts du legacy |
|------------------------------------------|----------------------------------|
| Stabilité éprouvée (tourne depuis 20 ans sans incident majeur) | Coût de maintenance croissant (développeurs rares, licences obsolètes) |
| Connaissance métier encodée dans le système | Impossibilité d'évoluer rapidement (time-to-market dégradé) |
| Intégration profonde avec les processus de l'entreprise | Risque de sécurité (failles non corrigées sur systèmes EOL) |
| Coût de remplacement perçu comme prohibitif | Frein à la migration cloud et à l'adoption des API |
| | Dépendance aux compétences rares (COBOL, AS/400) |

### Acteurs et solutions du marché

| Outil / Approche | Rôle | Éditeur |
|-----------------|------|---------|
| SonarQube / SonarCloud | Analyse statique et mesure de dette technique | SonarSource |
| Micro Focus Modernization Workbench | Modernisation COBOL | Micro Focus (OpenText) |
| IBM Mono2Micro | Migration monolithe vers microservices (IA) | IBM |
| AWS Mainframe Modernization | Modernisation applicative vers AWS | AWS |
| Strangler Fig Pattern | Pattern architectural de migration progressive | (Martin Fowler, 2004) |
| Architecture Hexagonale (Ports & Adapters) | Isolation du domaine métier | (Alistair Cockburn) |

### Cas d'usage concrets

1. **Ministère français et COBOL mainframe** : La DGFIP (Direction Générale des Finances Publiques) exploite encore des applications en COBOL sur mainframe IBM pour le traitement des déclarations fiscales. Ces systèmes traitent des centaines de milliards d'euros de transactions par an. La modernisation est planifiée sur 10 ans, en encapsulant progressivement les fonctions legacy derrière des APIs et en migrant les modules les moins critiques vers le cloud en premier.

2. **Banque régionale : refactoring par le Strangler Fig** : Une banque régionale possède un système de core banking développé en Java EE 2005, déployé sur JBoss. Elle applique le Strangler Fig Pattern : le module de paiements instantanés est le premier extrait et réécrit en microservice Spring Boot sur Kubernetes. Une API Gateway redirige les appels paiements vers le nouveau service, tandis que le monolithe gère le reste. Après 3 ans, 60 % des modules sont migrés.

3. **Startup scale-up et dette accumulée** : Une scale-up e-commerce a développé en 2 ans une plateforme sans tests ni documentation pour aller vite. En 2024, chaque déploiement provoque des régressions, le temps de onboarding d'un développeur dépasse 3 mois, et les incidents en production sont hebdomadaires. La DSI lance un programme "Tech Health" : gel des nouvelles fonctionnalités pendant 1 sprint par mois dédié au remboursement de dette (tests, refactoring, documentation).

### Chiffres et tendances

- 85 % des DSI considèrent la dette technique comme un frein à la transformation digitale (McKinsey, 2022)
- SonarQube est utilisé par plus de 400 000 organisations dans le monde (SonarSource, 2023)
- Le coût moyen d'une heure de développement perdue à cause de la dette technique est estimé à 23,50 $ (CAST, 2022)
- Les entreprises qui investissent dans la réduction de dette technique ont un time-to-market 20-40 % plus rapide (McKinsey, 2022)
- Le langage COBOL fait tourner 95 % des transactions ATM et 80 % des transactions en point de vente mondiales (Micro Focus, 2019)

## Flashcards
#flashcards/Cloud_et_Virtualisation/Legacy_et_dette_technique #flashcards/Développement/Legacy_et_dette_technique

Qui a inventé le concept de dette technique et quelle est la métaphore utilisée ? :: Ward Cunningham, en 1992. La métaphore est celle de la dette financière : un code mal conçu livré rapidement est un emprunt, dont les "intérêts" se paient en ralentissement des développements futurs.

Quelles sont les 5 grandes approches de modernisation d'un système legacy ? :: 1. Maintenance pure, 2. Refactoring (restructuration interne sans changer le comportement), 3. Réarchitecture (microservices, hexagonale), 4. Remplacement (SaaS ou réécriture), 5. Encapsulation/Wrapping (API façade).

Qu'est-ce que le refactoring et quel en est l'auteur de référence ? :: Amélioration de la structure interne du code sans modifier son comportement externe. Popularisé par Martin Fowler dans son livre "Refactoring: Improving the Design of Existing Code" (1999).

Quel outil mesure la dette technique avec un indice de A à E ? :: SonarQube (SonarSource), avec le rating SQALE. Le rating A indique une dette très faible, E indique une dette critique. Il estime aussi le temps de remboursement en jours-hommes.

Quel est le coût global estimé de la dette technique mondiale ? :: 1 520 milliards de dollars (CAST Research Labs, 2022).

Quelle est la "Boy Scout Rule" en développement logiciel ? :: Principe inspiré du scoutisme : "Laisser le camping plus propre qu'on ne l'a trouvé." En développement : à chaque modification du code, laisser le module dans un meilleur état qu'avant (renommer une variable, extraire une méthode, ajouter un test). Permet de gérer la dette de manière continue.

Quel pattern permet de moderniser un legacy sans réécriture big-bang risquée ? :: Le Strangler Fig Pattern (Martin Fowler) : développer progressivement de nouvelles fonctions cloud-native autour du système legacy et rediriger le trafic vers les nouveaux modules jusqu'à ce que l'ancien soit entièrement remplacé.

## Sources

- Ward Cunningham, "The WyCash Portfolio Management System", OOPSLA, 1992
- Martin Fowler, "Refactoring: Improving the Design of Existing Code", 1999 (2e éd. 2018)
- Martin Fowler, "Strangler Fig Application", martinfowler.com, 2004
- CAST Research Labs, "Software Intelligence Report", 2022
- McKinsey Digital, "Tech debt: Reclaiming tech equity", 2022
- Gartner, "Managing Technical Debt", 2022
- SonarSource, "SonarQube Documentation" : https://docs.sonarqube.org

## Notions liées
- [[Migration cloud (les 7R)]]
- [[Virtualisation]]
- [[FinOps]]
- [[Infrastructure des datacenters]]
- [[Technologies de stockage]]
