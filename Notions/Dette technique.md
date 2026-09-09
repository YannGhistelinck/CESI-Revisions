---
type: notion
thèmes:
  - Développement
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Dette technique

## En bref
> **Définition** : La dette technique désigne l'ensemble des compromis techniques délibérés ou accidentels accumulés dans un système logiciel, qui nécessiteront un travail futur supplémentaire ("intérêts") pour être corrigés. Métaphore introduite par Ward Cunningham en 1992, elle permet de communiquer les enjeux techniques aux décideurs non techniques.
> **Pourquoi c'est important** : Pour une DSI, la dette technique non maîtrisée ralentit les évolutions, augmente les coûts de maintenance, crée des risques opérationnels et peut conduire à l'obsolescence des systèmes. La quantifier et la gérer est un enjeu stratégique autant que technique.
> **Chiffres clés** :
> - La dette technique mondiale est estimée à **1 500 Md$** (CAST Software, 2022).
> - Les développeurs consacrent en moyenne **33 % de leur temps** à gérer la dette technique (Stripe Developer Survey, 2018).
> - Un taux de dette technique > **5 % du coût de développement** annuel est considéré comme critique (CAST Highlight).

## Approfondir

### Fonctionnement

#### Origine du concept (Ward Cunningham, 1992)
Ward Cunningham, co-auteur du Manifeste Agile et inventeur du wiki, a introduit la métaphore dans une conférence OOPSLA en 1992 :
> "Shipping first-time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a refactoring."

La métaphore financière est puissante pour les décideurs : la dette a un **principal** (le travail technique à faire) et des **intérêts** (le surcoût quotidien qu'elle impose sur chaque développement).

#### Taxonomie de la dette technique (Fowler / McConnell)
Martin Fowler distingue 4 quadrants selon 2 axes :
- **Délibérée vs Accidentelle** : la dette a-t-elle été choisie consciemment ?
- **Imprudente vs Prudente** : l'équipe savait-elle ce qu'elle faisait ?

| | Délibérée | Accidentelle |
|---|---|---|
| **Imprudente** | "On n'a pas le temps pour des designs" | "C'est quoi le clean code ?" |
| **Prudente** | "On livre maintenant et on corrige après" | "On a fait de notre mieux avec nos connaissances d'alors" |

La dette **délibérée prudente** (compromis conscient) est la seule acceptable — si elle est remboursée rapidement.

Steve McConnell (2007) distingue aussi la **dette non technique** (tests, documentation, processus).

#### Sources courantes de dette technique
- Code dupliqué (violation DRY).
- Couplage fort entre modules.
- Absence ou insuffisance de tests.
- Dépendances obsolètes (bibliothèques non mises à jour).
- Architecture monolithique difficile à faire évoluer.
- Documentation absente ou périmée.
- Utilisation de technologies en fin de vie (Java 6, .NET Framework 3.5, jQuery 1.x).
- Non-respect des standards de code (SOLID, Clean Code).

#### Bus Factor (facteur bus)
Le **bus factor** (ou truck factor) mesure le nombre minimum de personnes dont la perte (accident de bus) mettrait le projet en péril. C'est une forme de dette organisationnelle :
- **Bus factor = 1** : une seule personne connaît un composant critique → risque maximal.
- Indicateurs : commits ultra-concentrés sur un développeur, absence de documentation, code illisible.
- Remèdes : pair programming, revues de code, documentation, rotation des responsabilités.

#### Mesure et quantification de la dette technique
- **Indice de maintenabilité** (Halstead) : formule mathématique basée sur le volume et la complexité.
- **SQALE** (Software Quality Assessment based on Lifecycle Expectations) : modèle de mesure utilisé par SonarQube, exprimant la dette en **jours×homme** de remboursement.
- **Technical Debt Ratio** (SonarQube) : `dette / coût de réécriture complète`. Un ratio > 20 % = code non maintenable.
- **CAST Highlight** : évalue la dette à l'échelle d'un portefeuille applicatif en analysant le code source.

#### Gestion et remboursement de la dette
Stratégies de gestion :
1. **Prévention** : standards de code, revues, TDD, CI/CD.
2. **Détection** : outils d'analyse statique (SonarQube, CAST).
3. **Priorisation** : cartographier la dette et prioriser selon impact business + risque.
4. **Remboursement planifié** : allouer un pourcentage fixe de chaque sprint au refactoring (ex. : 20 % — "règle des 20 %").
5. **Décision de remplacement** : quand la dette est trop élevée, arbitrer entre refactoring et réécriture.

### Avantages / Inconvénients
| Avantages (de la dette maîtrisée) | Inconvénients (de la dette non maîtrisée) |
|-----------|---------------|
| Permet d'accélérer les livraisons à court terme | Ralentit progressivement toutes les évolutions futures |
| Métaphore efficace pour communiquer avec les décideurs | Accumulation des "intérêts" : coûts exponentiels |
| Dette délibérée et prudente est un levier tactique légitime | Augmente le risque de bugs et d'incidents en production |
| Peut financer l'innovation (time-to-market) | Diminue la motivation et la rétention des développeurs |
| Quantifiable et pilotable avec les bons outils | Bus factor élevé = risque opérationnel critique |

### Acteurs et solutions du marché
- **SonarQube / SonarCloud** : mesure de la dette technique en jours×homme (modèle SQALE), calcul du Technical Debt Ratio.
- **CAST Software** (CAST Highlight, CAST Imaging) : analyse de portefeuille, estimation de la dette, cartographie des dépendances.
- **CodeClimate** : mesure de la maintenabilité, visualisation de la dette par composant.
- **NDepend** (.NET) : analyse de la dette, métriques de couplage, règles personnalisables.
- **Jira** : suivi des tickets "dette technique" dans le backlog, intégration avec les outils d'analyse.
- **GitHub Insights** : identification du bus factor via l'analyse des contributeurs par fichier.

### Cas d'usage concrets
1. **Communication DSI–Direction** : une DSI utilise le modèle SQALE de SonarQube pour présenter à la direction la dette technique d'un ERP maison : "3 500 jours×homme de dette, soit 7 M€ d'effort de remboursement". Cet argument chiffré convainc la direction de financer un programme de modernisation sur 3 ans.
2. **Gestion du bus factor** : une startup identifie que 90 % des commits du module de paiement sont réalisés par un seul développeur (bus factor = 1). Elle met en place des sessions de pair programming hebdomadaires et une documentation systématique. En 6 mois, le bus factor passe à 4.
3. **Règle des 20 % en Scrum** : une équipe Scrum intègre dans sa Definition of Done l'obligation de rembourser de la dette technique à chaque sprint en allouant 20 % de la vélocité à des tickets de refactoring. Après 6 sprints, le Technical Debt Ratio passe de 18 % à 9 %.

### Chiffres et tendances
- **Stripe Developer Survey (2018)** : 33 % du temps des développeurs consacré à la dette technique, coût estimé à **85 Md$ par an** de perte de productivité aux États-Unis.
- **Gartner (2021)** : la dette technique représente en moyenne **20 à 40 % du patrimoine applicatif** des grandes entreprises.
- La **transformation digitale** accélère l'accumulation de dette : les projets livrés en urgence pendant le COVID-19 ont généré une vague de dette technique sans précédent.

## Flashcards
#flashcards
Qui a introduit la métaphore de la dette technique et en quelle année ? :: **Ward Cunningham**, co-auteur du Manifeste Agile, en **1992** lors d'une conférence OOPSLA.

Quels sont les 4 quadrants de la taxonomie de la dette technique (Fowler) ? :: Délibérée/Imprudente ("on n'a pas le temps"), Délibérée/Prudente ("on livre et on corrige après"), Accidentelle/Imprudente ("on ne sait pas coder"), Accidentelle/Prudente ("on a fait de notre mieux").

Qu'est-ce que le bus factor et comment le mesure-t-on ? :: Nombre minimum de personnes dont la perte mettrait le projet en péril. Se mesure en analysant la concentration des commits par contributeur sur chaque fichier/composant.

Comment SonarQube mesure-t-il la dette technique ? :: Via le modèle **SQALE** : la dette est exprimée en **jours×homme** de travail nécessaire pour la corriger. Le **Technical Debt Ratio** = dette / coût de réécriture complète.

Quelle est la règle pratique pour rembourser la dette technique en mode agile ? :: Allouer **20 % de la vélocité de chaque sprint** à des tickets de refactoring et de remboursement de dette (règle des 20 %).

À partir de quel Technical Debt Ratio SonarQube considère-t-il le code comme non maintenable ? :: Au-delà de **20 %** (ratio dette / coût de réécriture), le code est considéré non maintenable.

Quel est le coût annuel de la dette technique selon Stripe (2018) ? :: **85 Md$** de perte de productivité par an aux États-Unis, avec 33 % du temps des développeurs consacré à la gérer.

## Sources
- Cunningham, W. (1992). *The WyCash Portfolio Management System*. OOPSLA 1992.
- Fowler, M. (2009). *TechnicalDebtQuadrant*. martinfowler.com.
- McConnell, S. (2007). *Managing Technical Debt*. Construx Software.
- CAST Software (2022). *CAST Highlight State of Software Intelligence Report*.
- Stripe (2018). *The Developer Coefficient*.
- Gartner (2021). *Technical Debt: The Silent Killer of Digital Transformation*.

## Notions liées
- [[Clean Code et refactoring]]
- [[Maintenance logicielle]]
- [[Analyse de code (SAST - DAST)]]
- [[CMMI]]
- [[Architecture logicielle]]
- [[Legacy et dette technique]]
