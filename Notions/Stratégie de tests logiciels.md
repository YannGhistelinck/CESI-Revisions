---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Stratégie de tests logiciels

![[N — Stratégie de tests logiciels.mp3]]
## En bref
> **Définition** : La stratégie de tests logiciels définit l'approche globale pour atteindre les objectifs de qualité d'un projet ou d'une organisation. Elle détermine les types de tests à réaliser, les niveaux d'abstraction, les critères d'entrée/sortie, les outils et les responsabilités. Elle se distingue du plan de test (opérationnel, projet-spécifique) et de la politique de test (directive organisationnelle).
> **Pourquoi c'est important** : Tester sans stratégie revient à couvrir les mêmes zones sans garantir la qualité globale. Pour un DSI, une stratégie de tests formalisée réduit les risques de régression en production, accélère les livraisons en CI/CD et fournit des preuves objectives de qualité aux parties prenantes métier.
> **Chiffres clés** :
> - Un bug détecté en production coûte en moyenne 30x plus cher qu'un bug détecté en phase de conception (IBM Systems Sciences Institute).
> - Les équipes qui suivent une stratégie de tests formalisée livrent 2,5x moins de défauts en production (DORA State of DevOps 2022).
> - Le marché des outils de test logiciel atteindra 60 Md$ en 2027 (Allied Market Research, 2022).

## Approfondir

### Fonctionnement

**La hiérarchie des documents de test (ISTQB)**

```
Politique de test (Test Policy)
    │
    ▼
Stratégie de test (Test Strategy)
    │
    ▼
Plan de test (Test Plan)
    │
    ▼
Campagne de tests / Cas de test
```

- **Politique de test** : Document de haut niveau définissant les principes et objectifs du test pour l'organisation entière. Répond à "Pourquoi on teste".
- **Stratégie de test** : Approche générale pour atteindre les objectifs définis dans la politique. Répond à "Comment on teste (en général)". Peut être commune à plusieurs projets.
- **Plan de test** : Document opérationnel projet-spécifique. Définit le périmètre, les ressources, le planning, les critères d'entrée/sortie, les risques. Répond à "Comment on teste ce projet".

**Les 7 principes fondamentaux de l'ISTQB**

1. **Les tests montrent la présence de défauts, pas leur absence** — On ne peut pas prouver qu'un logiciel est exempt de bugs.
2. **Les tests exhaustifs sont impossibles** — Il faut prioriser par risque et importance.
3. **Commencer les tests tôt** — Shift-left : plus tôt on détecte, moins ça coûte.
4. **Regroupement des défauts** — 80 % des bugs se concentrent dans 20 % du code (loi de Pareto).
5. **Le paradoxe du pesticide** — Les mêmes tests répétés deviennent inefficaces. Il faut les réviser.
6. **Les tests dépendent du contexte** — Une application médicale ne se teste pas comme un blog.
7. **L'illusion de l'absence de défaut** — Un logiciel sans bug mais inutile reste un échec.

**Types de tests**

| Type | Description | Exemple d'outil |
|------|-------------|-----------------|
| **Fonctionnel** | Vérifie que les fonctionnalités répondent aux exigences | Cucumber, FitNesse |
| **Performance** | Charge, stress, endurance, pics | JMeter, k6, Gatling |
| **Sécurité** | Vulnérabilités, conformité OWASP | OWASP ZAP, Burp Suite |
| **Compatibilité** | Navigateurs, OS, appareils | BrowserStack, Sauce Labs |
| **Utilisabilité (UX)** | Ergonomie, accessibilité (RGAA/WCAG) | Axe, Lighthouse |
| **Régression** | Vérification qu'aucune fonctionnalité existante n'est cassée | Tout framework automatisé |
| **Fumée (Smoke test)** | Vérification basique que le build est deployable | Pipeline CI/CD |
| **Sanity** | Vérification ciblée après correctif | Tests ciblés post-fix |

**Niveaux de tests**

| Niveau | Quoi | Qui | Quand |
|--------|------|-----|-------|
| **Composant / Unitaire** | Une unité de code isolée | Développeur | Sprint (en continu) |
| **Intégration** | Interaction entre composants ou services | Dev / QA | Sprint / intégration |
| **Système** | Application complète dans un environnement dédié | QA | Fin de sprint / RC |
| **Recette / Acceptation (UAT)** | Validation par les utilisateurs finaux | Métiers + QA | Avant mise en production |

**Tests statiques vs Dynamiques**

- **Tests statiques** : Examen du code/documentation sans l'exécuter. Revues de code (code review), inspections, analyse statique (SonarQube). Détectent des défauts tôt, sans avoir besoin d'un environnement.
- **Tests dynamiques** : Exécution du logiciel avec des données de test. Tous les autres types de tests (unitaires, intégration, E2E, performance...).

**Boîte noire vs Boîte blanche (vs Boîte grise)**

| | Boîte noire | Boîte blanche | Boîte grise |
|-|------------|---------------|-------------|
| Connaissance du code | Aucune | Totale | Partielle |
| Perspective | Utilisateur / attaquant | Développeur | Testeur expérimenté |
| Objectif | Valider les fonctionnalités et comportements | Couvrir tous les chemins du code | Combiner les deux approches |
| Exemple | Tests UAT, pentest externe | Tests unitaires, audit de code | Tests d'intégration avec connaissance API |

**Gestion des campagnes de tests**

Une campagne de tests est l'ensemble des activités de test planifiées pour une itération ou une mise en production :

1. **Préparation** : Identification des cas de test, priorisation par risque, préparation des données de test, configuration des environnements.
2. **Exécution** : Tests manuels et automatisés, journalisation des anomalies.
3. **Suivi** : Taux d'avancement (% cas exécutés), taux de succès, nombre d'anomalies ouvertes par criticité.
4. **Clôture** : Rapport de campagne, analyse des métriques, bilan et recommandations.

**Métriques de test importantes**

- **Taux de couverture de code** : % du code exécuté par les tests. Cible courante : > 80 % pour les composants critiques.
- **Densité de défauts** : Nombre de défauts / point de fonction ou KLOC.
- **Taux d'échappement des défauts** : % de bugs découverts en production vs en test.
- **Coût par défaut** : Budget de test / nombre de défauts détectés.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction des coûts de correction (défauts détectés plus tôt) | Investissement initial en temps et outillage |
| Confiance accrue lors des déploiements | Faux sentiment de sécurité si la couverture est mal ciblée |
| Documentation vivante des comportements attendus | Maintenance des tests automatisés = charge continue |
| Preuves objectives de qualité pour les parties prenantes | Difficulté à tester les systèmes legacy sans refactoring |
| Accélération CI/CD grâce aux tests de régression automatisés | Nécessite une culture qualité dans toute l'équipe |

### Acteurs et solutions du marché

**Gestion des tests (TMS)**
- Xray (Jira plugin), TestRail, Zephyr Scale, qTest.

**Frameworks d'automatisation**
- **Web** : Selenium, Playwright, Cypress.
- **API** : Postman, RestAssured, Karate.
- **Mobile** : Appium.
- **BDD** : Cucumber, SpecFlow.
- **Performance** : JMeter, k6, Gatling.

**Analyse qualité / couverture**
- SonarQube (qualité + couverture), JaCoCo (Java), Istanbul (JavaScript).

### Cas d'usage concrets

1. **Startup SaaS en croissance** : Mise en place d'une stratégie de tests en 3 niveaux (unitaire, intégration, E2E) dans la pipeline CI/CD. Réduction du taux d'échappement des défauts de 45 % à 8 % en 3 mois. Déploiements quotidiens sans régression.

2. **PME en transformation agile** : Passage des tests manuels à l'automatisation des cas de régression (800 cas sur 3 000 automatisés). Gain de 3 jours par sprint sur le cycle de recette. Les testeurs se concentrent sur les nouveaux scénarios exploratoires.

3. **Projet de modernisation d'un SI bancaire** : Stratégie de tests multi-niveaux avec UAT formalisée sur 6 semaines impliquant les équipes métier. Matrice de traçabilité exigences/cas de test permettant de garantir la couverture fonctionnelle complète avant mise en production.

### Chiffres et tendances

- 41 % des équipes n'ont pas de stratégie de tests formalisée (World Quality Report, Capgemini 2022).
- Les tests automatisés représentent en moyenne 32 % de l'effort total de test dans les entreprises matures (World Quality Report 2023).
- L'IA est intégrée dans les outils de test par 62 % des grandes entreprises en 2023 (Gartner, 2023) : génération automatique de cas de test, auto-healing des scripts.

## Flashcards
#flashcards/Développement/Stratégie_de_tests_logiciels

Quelle est la hiérarchie des 3 documents de test ISTQB ? :: 1. Politique de test (principes org.), 2. Stratégie de test (approche générale), 3. Plan de test (opérationnel projet-spécifique).

Citez les 7 principes fondamentaux de l'ISTQB. :: 1. Tests montrent la présence, pas l'absence de défauts. 2. Tests exhaustifs impossibles. 3. Tester tôt. 4. Regroupement des défauts (Pareto). 5. Paradoxe du pesticide. 6. Tests dépendent du contexte. 7. Illusion de l'absence de défaut.

Quels sont les 4 niveaux de tests (du plus bas au plus haut) ? :: Composant/Unitaire → Intégration → Système → Recette/Acceptation (UAT).

Quelle est la différence entre tests statiques et dynamiques ? :: Statiques : examen du code sans l'exécuter (revue de code, SAST). Dynamiques : exécution du logiciel avec données de test (unitaires, intégration, E2E, performance…).

Qu'est-ce que le "paradoxe du pesticide" (principe ISTQB n°5) ? :: Les mêmes tests répétés indéfiniment deviennent inefficaces car les bugs s'y adaptent. Il faut régulièrement réviser et enrichir les cas de test pour maintenir leur efficacité.

Quelle est la différence entre boîte noire, blanche et grise ? :: Boîte noire : aucune connaissance du code (perspective utilisateur). Boîte blanche : connaissance totale du code (perspective développeur). Boîte grise : connaissance partielle (API connue, code interne non connu).

Qu'est-ce qu'un test de fumée (smoke test) ? :: Vérification minimale et rapide que le build déployé fonctionne sur les chemins critiques, avant de lancer la suite complète de tests. Exécuté à chaque déploiement dans la CI/CD.

Citez 3 métriques clés pour piloter une campagne de tests. :: Taux de couverture de code (%), taux d'échappement des défauts (bugs en production vs en test), densité de défauts (nombre de bugs / point de fonction).

Pourquoi dit-on que "les tests exhaustifs sont impossibles" ? :: Le nombre de combinaisons d'entrées, d'états et de chemins d'exécution est infini. Il faut prioriser par risque et criticité métier plutôt que viser une couverture exhaustive illusoire.

## Sources
- ISTQB — *Foundation Level Syllabus v4.0* (2023) — https://www.istqb.org
- Capgemini — *World Quality Report 2022-2023* — https://www.capgemini.com/research/world-quality-report/
- DORA — *State of DevOps Report 2022* — https://dora.dev/research/
- IBM Systems Sciences Institute — *Relative Cost of Fixing Defects*.
- Gartner — *Hype Cycle for Agile and DevOps* (2023).

## Notions liées
- [[Tests logiciels]]
- [[TDD - BDD]]
- [[CI - CD]]
- [[DevOps]]
- [[DevSecOps]]
- [[OWASP Top 10 et sécurité applicative]]
- [[Qualité logicielle — normes et modèles]]
- [[Analyse de code (SAST - DAST)]]
