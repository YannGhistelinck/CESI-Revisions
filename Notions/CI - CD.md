---
type: notion
thèmes:
  - Développement
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# CI - CD

## En bref
> **Définition** : La CI/CD (Continuous Integration / Continuous Delivery ou Deployment) est un ensemble de pratiques d'automatisation du cycle de livraison logicielle. La **CI** (Intégration Continue) automatise la vérification du code à chaque commit (build, tests). La **CD Delivery** automatise la livraison d'artefacts prêts à déployer. La **CD Deployment** automatise la mise en production sans intervention humaine. Un **pipeline** CI/CD enchaîne ces étapes de façon reproductible et traçable.
> **Pourquoi c'est important** : Sans CI/CD, les intégrations de code sont rares et douloureuses ("integration hell"), les tests manuels ralentissent les livraisons et les déploiements sont des événements risqués. La CI/CD transforme le déploiement en opération courante, sûre et réversible, réduisant drastiquement le lead time et le taux d'incidents.
> **Chiffres clés** :
> - Les organisations Elite déploient à la demande avec un lead time inférieur à 1 heure (DORA, 2023).
> - La CI/CD réduit le change failure rate de 4 fois par rapport aux déploiements manuels.
> - 69 % des équipes de développement utilisent des pipelines CI/CD en 2024 (Stack Overflow Survey).

## Approfondir

### Fonctionnement

**Intégration Continue (CI)**
Pratique consistant à intégrer le code de tous les développeurs dans le tronc principal (main branch) plusieurs fois par jour. À chaque push, un pipeline automatique déclenche :
1. **Compilation/Build** : vérification que le code compile
2. **Tests unitaires** : validation de chaque unité de code isolément
3. **Analyse statique** (SAST, linting) : qualité et sécurité du code
4. **Tests d'intégration** : validation des interactions entre composants
5. **Construction de l'artefact** : image Docker, JAR, package npm…

**Continuous Delivery vs Continuous Deployment**
| Aspect | Continuous Delivery | Continuous Deployment |
|--------|--------------------|-----------------------|
| Définition | Artefact toujours prêt à déployer | Déploiement automatique en production à chaque commit |
| Validation humaine | Oui (bouton "deploy" manuel) | Non (100 % automatisé) |
| Adapté à | Secteurs réglementés, produits B2B | SaaS, web apps, microservices |
| Exemples | Banque, aéronautique | Netflix, Facebook, Etsy |

**Anatomie d'un pipeline CI/CD typique**
```
Commit → Build → Unit Tests → SAST → Docker Build → 
Integration Tests → Staging Deploy → E2E Tests → 
(approbation) → Production Deploy → Smoke Tests → Monitoring
```

**Trunk-Based Development (TBD)**
Pratique recommandée pour la CI : tous les développeurs travaillent directement sur le tronc (main) ou via des branches éphémères (durée de vie < 24h). Évite l'accumulation de divergences et les "merge hell". Alternative : GitFlow (branches long-lived), plus adapté aux cycles de release planifiés.

**Feature Flags (feature toggles)**
Mécanisme permettant d'activer ou désactiver une fonctionnalité en production sans déploiement. Utilisé pour :
- Déployer du code "dark" (non visible utilisateurs)
- Faire des tests A/B
- Rollback instantané sans redéploiement
- Canary releases ciblées (% d'utilisateurs)
Solutions : LaunchDarkly, Unleash, Flagsmith, OpenFeature (standard CNCF).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection précoce des bugs (shift-left testing) | Investissement initial important (écriture des tests, pipelines) |
| Lead time réduit (heures vs semaines) | Maintenance des pipelines et des tests (flaky tests) |
| Déploiements moins risqués et réversibles | Culture de la qualité nécessaire (discipline des développeurs) |
| Feedback rapide aux développeurs | Infrastructure de CI/CD à maintenir (agents, runners) |
| Traçabilité complète (quel commit = quel déploiement) | Tests E2E lents pouvant bloquer le pipeline |
| Collaboration améliorée (intégration fréquente) | Gestion des secrets et des environnements complexe |

### Acteurs et solutions du marché
| Outil | Éditeur | Caractéristiques |
|-------|---------|-----------------|
| Jenkins | Open source (Linux Foundation) | Très extensible (2 000+ plugins), self-hosted, courbe d'apprentissage élevée |
| GitLab CI/CD | GitLab | Intégré à la plateforme, YAML-based, GitLab Runners, free tier |
| GitHub Actions | GitHub (Microsoft) | Natif GitHub, marketplace d'actions, cloud ou self-hosted |
| Azure DevOps Pipelines | Microsoft | Intégration Azure, YAML ou GUI, agents Microsoft-hosted |
| CircleCI | CircleCI | Cloud-first, rapide à configurer, orbs (réutilisabilité) |
| Tekton | CNCF | Pipelines Kubernetes-native, standard cloud native |
| ArgoCD / Argo Workflows | Intuit / CNCF | CI/CD GitOps-oriented pour Kubernetes |

### Cas d'usage concrets
1. **Etsy** : pionnier de la CI/CD, Etsy effectue jusqu'à 50 déploiements par jour en production grâce à un pipeline entièrement automatisé et des feature flags. Leur pratique "Continuous Deployment" a été documentée dans de nombreux ouvrages.
2. **Airbus (CyberAir)** : dans l'industrie aéronautique, la CI est utilisée pour les logiciels embarqués avec des pipelines incluant des validations DO-178C (certification aéro) — démontrant l'adaptation de la CI aux secteurs réglementés (Continuous Delivery, pas Deployment).
3. **BNP Paribas** : déploiement de GitLab CI pour les équipes de développement interne, permettant de passer de cycles de release trimestriels à des déploiements hebdomadaires, avec des gates de sécurité automatisées (SAST, DAST).

### Chiffres et tendances
- Les équipes pratiquant la CI/CD ont 5 fois moins de burn-out (DORA, 2023).
- Le marché des outils CI/CD atteindra 9,3 Md$ en 2030 (Grand View Research).
- GitHub Actions est passé de 0 à 30 % de parts de marché CI/CD entre 2019 et 2024.
- 62 % des pipelines CI/CD incluent désormais des étapes de sécurité automatisées (Snyk, 2024).

## Flashcards
#flashcards/Développement/CI_CD #flashcards/Cloud_et_Virtualisation/CI_CD #flashcards/Optimisation_du_SI/CI_CD
- Quelle est la différence entre Continuous Delivery et Continuous Deployment ? :: Continuous Delivery maintient l'artefact prêt à déployer mais nécessite une validation humaine avant la mise en production. Continuous Deployment pousse automatiquement en production à chaque commit validé par les tests.
- Qu'est-ce que le "trunk-based development" ? :: Une pratique où tous les développeurs intègrent leur code directement dans le tronc principal (main) ou via des branches éphémères de moins de 24h, évitant les divergences longues et les "merge hell".
- À quoi servent les feature flags en CI/CD ? :: Ils permettent de déployer du code sans l'activer pour les utilisateurs, de faire des tests A/B, d'effectuer des rollbacks instantanés et de cibler progressivement les utilisateurs (canary release) sans redéploiement.
- Citez 3 outils CI/CD majeurs et leur éditeur. :: Jenkins (open source, Linux Foundation), GitLab CI/CD (GitLab), GitHub Actions (Microsoft/GitHub), Azure DevOps Pipelines (Microsoft).
- Qu'est-ce qu'un pipeline CI/CD ? :: Une chaîne automatisée d'étapes (build, tests, analyse, packaging, déploiement) déclenchée à chaque commit, permettant de livrer du code de façon reproductible, traçable et rapide.
- Qu'est-ce que l'"integration hell" que la CI résout ? :: L'accumulation de divergences entre les branches des développeurs, rendant les fusions (merges) extrêmement difficiles et génératrices de nombreux conflits lorsqu'elles sont trop espacées dans le temps.
- Qu'est-ce qu'un "flaky test" et pourquoi est-ce un problème en CI/CD ? :: Un test qui échoue de manière aléatoire (non déterministe), sans bug réel dans le code. Il érode la confiance dans le pipeline et force les développeurs à relancer les builds, ralentissant la livraison.

## Sources
- Jez Humble, David Farley, *Continuous Delivery*, Addison-Wesley, 2010
- DORA State of DevOps Report 2023 : https://dora.dev/
- Paul Hammond, "Deploying at Etsy", Velocity Conference, 2010
- Stack Overflow Developer Survey 2024 : https://survey.stackoverflow.co/2024/

## Notions liées
- [[DevOps]]
- [[GitOps]]
- [[DevSecOps]]
- [[Stratégies de déploiement]]
- [[Infrastructure as Code (IaC)]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Cloud Native et 12-Factor App]]
