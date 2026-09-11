---
type: notion
thèmes:
  - Développement
  - IA
statut: pas vu
dernière_révision: 
---

# IA et automatisation des tests

## En bref
> **Définition** : L'IA appliquée aux tests logiciels désigne l'ensemble des techniques d'intelligence artificielle (machine learning, LLM, vision par ordinateur) utilisées pour automatiser, améliorer et accélérer les activités de test : génération automatique de cas de test, auto-guérison des tests cassés (auto-healing), sélection prédictive des tests à exécuter, et détection d'anomalies visuelles dans les interfaces.
> **Pourquoi c'est important** : La maintenance des tests automatisés est l'un des principaux freins à l'adoption du test automation — notamment les tests E2E qui se cassent à chaque modification d'interface. L'IA réduit ce fardeau, permet de couvrir plus de cas sans effort humain proportionnel, et rend les pipelines CI/CD plus intelligents.
> **Chiffres clés** :
> - 70 % des équipes QA citent la maintenance des tests comme leur défi principal (Capgemini World Quality Report 2023).
> - Les outils d'auto-healing réduisent le temps de maintenance des tests de 40 à 60 % (études Testim, Mabl, 2023).
> - Le marché de l'AI Testing est estimé à 2,3 Md$ en 2024, avec une croissance de 18 % par an jusqu'en 2030 (Allied Market Research).

## Approfondir

### Fonctionnement

**Auto-healing des tests (self-healing tests)**
Problème : les tests E2E (Selenium, Playwright) échouent souvent après un changement d'interface car les sélecteurs CSS ou XPath ne correspondent plus à l'élément cible.
Solution IA : l'outil apprend plusieurs façons d'identifier un élément (ID, texte, position, voisinage visuel, ML-based fingerprint). Quand un sélecteur échoue, il essaie les alternatives et met à jour automatiquement le test. Outils : Testim, Mabl, Healenium (open source), Applitools.

**Génération automatique de cas de test**
- **Basée sur LLM** : des modèles comme GitHub Copilot, Tabnine, ou des outils spécialisés (CodiumAI, Diffblue Cover) génèrent des tests unitaires à partir du code source ou d'une description en langage naturel.
- **Basée sur le comportement observé** : certains outils enregistrent les interactions utilisateurs réelles et génèrent automatiquement des tests E2E (Testim Record, Katalon).
- **Basée sur les spécifications** : des outils parsent les spécifications (OpenAPI, Gherkin/BDD) pour générer des tests de contrat ou d'API (Postman, Schemathesis).

**Predictive Test Selection (sélection prédictive des tests)**
Problème : en CI/CD, exécuter toute la suite de tests à chaque commit est trop lent.
Solution : des modèles ML analysent l'historique d'exécution (quels tests ont échoué quand tel fichier a changé) et prédisent les tests les plus susceptibles d'échouer pour un changement donné. Seuls ces tests sont exécutés, réduisant le feedback loop. Utilisé par : Meta (interne), Launchable, Microsoft (Azure DevOps Test Impact Analysis).

**Tests visuels par IA (Visual AI Testing)**
Comparaison des screenshots de l'interface avec une baseline. L'IA distingue les différences visuelles significatives (bug) des différences intentionnelles (mise à jour de style). Évite les faux positifs des comparaisons pixel-à-pixel. Outil leader : Applitools Eyes.

**Analyse de log et détection d'anomalies**
Des modèles ML analysent les logs de test et de production pour détecter des patterns anormaux sans règle prédéfinie. Outils : Elastic Observability, Dynatrace Davis AI, New Relic AI.

**LLM et test génératif**
Les LLM (GPT-4, Claude) permettent de générer des cas de test depuis des user stories en langage naturel, de suggérer des cas limites (edge cases) oubliés, et d'expliquer les échecs de tests en langage compréhensible pour les non-techniques. Intégrations : CodiumAI, Qodo, Diffblue Cover.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction drastique de la maintenance des tests | Les tests générés par IA peuvent manquer de pertinence métier |
| Accélération du feedback loop en CI/CD | Risque de dépendance à des outils propriétaires coûteux |
| Détection d'anomalies difficiles à capturer manuellement | L'auto-healing peut masquer des régressions réelles |
| Génération de cas limites (edge cases) souvent oubliés | Nécessite un historique de données conséquent pour la sélection prédictive |
| Accessibilité des tests aux équipes non techniques (BDD + LLM) | Les tests générés par LLM doivent être revus par un humain |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Applitools | Visual AI Testing, auto-healing, smart test recorder |
| Mabl | Plateforme de test intelligent (auto-healing, analyse de risque) |
| Testim | Tests E2E avec auto-healing basé sur ML |
| Diffblue Cover | Génération automatique de tests unitaires Java par IA |
| CodiumAI / Qodo | Génération de tests par LLM (VS Code plugin) |
| Launchable | Predictive Test Selection pour réduire la durée des pipelines CI |
| Microsoft (Test Impact Analysis) | Sélection prédictive intégrée à Azure DevOps / Azure Pipelines |
| Healenium | Auto-healing open source pour Selenium |
| GitHub Copilot | Suggestion de tests unitaires inline dans l'IDE |

### Cas d'usage concrets
1. **Meta** : utilise un système interne de Predictive Test Selection qui réduit de 80 % le nombre de tests exécutés par commit, tout en détectant 99,5 % des régressions. Cela permet de maintenir un cycle CI de moins de 10 minutes malgré des millions de tests.
2. **Société Générale** : a déployé Applitools pour les tests visuels de ses interfaces bancaires mobiles, réduisant de 75 % le temps passé à analyser les échecs de tests UI après chaque release.
3. **Volkswagen Digital Solutions** : utilise Diffblue Cover pour générer automatiquement des tests unitaires sur sa base de code Java legacy, atteignant 70 % de couverture sur du code préalablement non testé en quelques semaines.

### Chiffres et tendances
- 68 % des organisations utilisent ou prévoient d'utiliser l'IA pour les tests logiciels d'ici 2025 (Capgemini World Quality Report 2023).
- Les LLM réduisent de 30 à 50 % le temps de rédaction des cas de test en BDD (études pilotes, 2023-2024).
- La sélection prédictive de tests réduit en moyenne la durée des pipelines CI de 40 à 80 % selon les projets.
- Les tests visuels basés sur l'IA réduisent les faux positifs de 90 % par rapport aux comparaisons pixel-à-pixel (Applitools, 2023).

## Flashcards
#flashcards
- Qu'est-ce que l'auto-healing dans les tests logiciels ? :: Une technique IA par laquelle un test E2E cassé (sélecteur modifié) se corrige automatiquement en identifiant l'élément cible par des méthodes alternatives apprises par ML.
- Qu'est-ce que la Predictive Test Selection ? :: Un mécanisme ML qui prédit quels tests sont susceptibles d'échouer pour un changement de code donné, afin de n'exécuter qu'un sous-ensemble pertinent des tests en CI/CD.
- Quel outil open source implémente l'auto-healing pour Selenium ? :: Healenium.
- Qu'est-ce que le Visual AI Testing ? :: Une approche utilisant l'IA pour comparer des screenshots d'interfaces et détecter les régressions visuelles significatives en évitant les faux positifs des comparaisons pixel-à-pixel.
- Comment les LLM peuvent-ils aider dans les tests logiciels ? :: En générant des cas de test depuis des user stories en langage naturel, en suggérant des edge cases, en expliquant les échecs de tests, et en produisant du code de test unitaire.
- Quel est le principal risque de l'auto-healing des tests ? :: Masquer des régressions réelles en adaptant automatiquement le test à un comportement modifié qui aurait dû être signalé comme un bug.
- Quel outil propose la génération automatique de tests unitaires Java par IA ? :: Diffblue Cover.

## Sources
- Capgemini World Quality Report 2023 : https://www.capgemini.com/insights/research-library/world-quality-report-2023/
- Applitools Visual AI Testing : https://applitools.com/
- Launchable Predictive Test Selection : https://www.launchableinc.com/
- CodiumAI (Qodo) : https://www.codium.ai/
- Diffblue Cover : https://www.diffblue.com/
- Microsoft Test Impact Analysis : https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis

## Notions liées
- [[Tests logiciels]]
- [[DORA Metrics]]
- [[IA en cybersécurité]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Platform Engineering]]
