---
type: notion
thèmes:
  - Développement
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# DORA Metrics

## En bref
> **Définition** : Les DORA Metrics (DevOps Research and Assessment) sont quatre indicateurs clés permettant de mesurer la performance des équipes de livraison logicielle. Issus d'un programme de recherche mené par Google depuis 2014, ils distinguent les équipes "Elite", "High", "Medium" et "Low" en termes de performance DevOps.
> **Pourquoi c'est important** : Pour une DSI, ces métriques offrent un référentiel objectif pour piloter l'amélioration continue des pipelines CI/CD, justifier des investissements d'outillage, et aligner la performance technique avec les objectifs métier.
> **Chiffres clés** :
> - Les équipes "Elite" déploient 973x plus fréquemment que les équipes "Low" (State of DevOps Report 2021).
> - Leur MTTR est 6 570x plus rapide.
> - 60 % des organisations considèrent les DORA Metrics comme leur principal référentiel de performance DevOps en 2023 (DORA, Google).

## Approfondir

### Fonctionnement

Les quatre métriques DORA couvrent deux dimensions : la **vélocité** (vitesse de livraison) et la **stabilité** (fiabilité du système).

**1. Deployment Frequency (DF) — Fréquence de déploiement**
Mesure la fréquence à laquelle une organisation déploie du code en production. Une haute fréquence traduit des cycles courts, un faible batch size et une confiance élevée dans le pipeline CI/CD.
- Elite : plusieurs déploiements par jour
- Low : moins d'une fois par mois

**2. Lead Time for Changes (LT) — Délai de mise en production**
Mesure le temps entre le premier commit et la mise en production. Inclut la revue de code, les tests automatisés, le déploiement. C'est un indicateur clé de l'efficacité du pipeline CI/CD.
- Elite : moins d'une heure
- Low : plus de six mois

**3. Change Failure Rate (CFR) — Taux d'échec des changements**
Pourcentage de déploiements entraînant une dégradation de service nécessitant un rollback, un hotfix ou un patch. Reflète la qualité des tests et des processus de validation.
- Elite : 0–15 %
- Low : 46–60 %

**4. Mean Time to Restore (MTTR) — Temps moyen de rétablissement**
Temps moyen pour restaurer le service après un incident en production. Mesure la capacité de détection, diagnostic et correction rapide des incidents.
- Elite : moins d'une heure
- Low : entre une semaine et un mois

**Grille de classification DORA (2021)**
| Niveau | DF | LT | CFR | MTTR |
|--------|----|----|-----|------|
| Elite | Plusieurs/jour | < 1 heure | 0–15 % | < 1 heure |
| High | 1/jour – 1/semaine | 1 jour – 1 semaine | 16–30 % | < 1 jour |
| Medium | 1/semaine – 1/mois | 1 semaine – 1 mois | 16–30 % | 1 jour – 1 semaine |
| Low | < 1/mois | > 6 mois | 16–60 % | > 1 semaine |

En 2023, DORA a introduit une cinquième métrique : la **Reliability** (respect des objectifs de niveau de service — SLO).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Référentiel objectif et validé par la recherche | Risque de "goodhart's law" : optimiser la métrique sans améliorer le fond |
| Couvre à la fois la vitesse et la stabilité | Ne mesure pas la valeur métier livrée ni l'expérience développeur |
| Langage commun entre DSI et direction générale | Nécessite une instrumentation outillée (pipeline CI/CD, observabilité) |
| Facilite la priorisation des investissements DevOps | Peut pénaliser les équipes gérant des systèmes legacy complexes |
| Comparaison avec les benchmarks industriels | Les données sont auto-déclarées dans les surveys DORA (biais possibles) |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Google / DORA | Programme de recherche annuel, State of DevOps Report |
| LinearB | Plateforme de métriques ingénierie (DORA + SPACE framework) |
| Sleuth | Outil dédié au suivi des DORA Metrics (intégrations GitHub, Jira, PagerDuty) |
| GitLab | DORA Metrics intégrées nativement dans le tableau de bord CI/CD |
| Faros AI | Plateforme d'ingénierie data connectant les outils DevOps pour calculer les DORA Metrics |
| Cortex | Developer portal avec suivi DORA, scorecard de maturité |
| Datadog | Suivi DORA via DORA Metrics integration (basé sur les déploiements et incidents) |

### Cas d'usage concrets
1. **ING Bank** : a adopté les DORA Metrics pour mesurer l'impact de sa transformation DevOps, réduisant son lead time de plusieurs semaines à quelques heures après automatisation des tests et du déploiement.
2. **Capital One** : utilise les DORA Metrics couplés à un internal developer portal pour piloter la performance de 3 000+ développeurs et identifier les équipes ayant besoin de support.
3. **Société Générale** : intègre les DORA Metrics dans ses OKR de transformation numérique, avec un suivi mensuel au niveau COMEX pour justifier les investissements CI/CD.

### Chiffres et tendances
- Les équipes Elite ont 2,5x plus de probabilité de surpasser leurs objectifs commerciaux (State of DevOps 2022).
- 83 % des équipes Elite pratiquent le trunk-based development contre 21 % des équipes Low (DORA, 2022).
- L'adoption du continuous deployment augmente de 20 % par an dans les entreprises "High" et "Elite".
- En 2023, DORA a ajouté la dimension "Reliability" (SLO-based) comme cinquième métrique officielle.

## Flashcards
#flashcards
- Que signifie l'acronyme DORA ? :: DevOps Research and Assessment — programme de recherche Google mesurant la performance des équipes de livraison logicielle.
- Quelles sont les 4 métriques DORA ? :: Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Restore.
- Qu'est-ce que le Lead Time for Changes ? :: Le temps entre le premier commit et le déploiement en production ; mesure l'efficacité du pipeline CI/CD.
- Qu'est-ce que le MTTR ? :: Mean Time to Restore — temps moyen pour rétablir le service après un incident en production.
- Quelle est la performance d'une équipe "Elite" en Deployment Frequency ? :: Plusieurs déploiements par jour en production.
- Quelle loi risque-t-on d'enfreindre en optimisant uniquement les DORA Metrics ? :: La loi de Goodhart : "quand une mesure devient un objectif, elle cesse d'être une bonne mesure."
- Quelle est la cinquième métrique introduite par DORA en 2023 ? :: La Reliability — mesurée par le respect des SLO (Service Level Objectives).

## Sources
- DORA State of DevOps Report 2023 : https://dora.dev/research/
- DORA State of DevOps Report 2021 : https://www.devops-research.com/research.html
- GitLab DORA Metrics Documentation : https://docs.gitlab.com/ee/user/analytics/dora_metrics.html
- Sleuth DORA Metrics Guide : https://www.sleuth.io/post/dora-metrics
- Google Cloud — Understanding DORA Metrics : https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance

## Notions liées
- [[Legacy et dette technique]]
- [[Cyber-résilience]]
- [[Tests logiciels]]
- [[Platform Engineering]]
- [[Conteneurisation (Docker - Kubernetes)]]
