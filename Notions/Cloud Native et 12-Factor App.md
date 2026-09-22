---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Développement
statut: pas vu
dernière_révision: 
---

# Cloud Native et 12-Factor App

![[N — Cloud Native et 12-Factor App.mp3]]
## En bref
> **Définition** : Le terme "Cloud Native" désigne une approche de conception et d'exploitation d'applications qui exploite pleinement les capacités du cloud (élasticité, automatisation, résilience) en s'appuyant sur des microservices, des conteneurs, l'orchestration et des pratiques DevOps/CI-CD. La méthodologie **12-Factor App**, formalisée par Heroku (2012), définit 12 principes pour concevoir des applications cloud native portables, scalables et maintenables.
> **Pourquoi c'est important** : Une DSI qui adopte le cloud native réduit le time-to-market, améliore la résilience de ses services et optimise ses coûts via l'auto-scaling. Les applications "lift-and-shift" (migration sans refonte) ne bénéficient pas pleinement du cloud ; le cloud native en est l'exploitation maximale.
> **Chiffres clés** :
> - 79 % des entreprises déclarent que les applications cloud native sont leur priorité stratégique n°1 (Gartner, 2024).
> - Les entreprises cloud native déploient du code 208 fois plus fréquemment que les entreprises traditionnelles (DORA Report, 2023).
> - Le marché cloud native devrait atteindre 44 Md$ en 2027 (Allied Market Research).

## Approfondir

### Fonctionnement

**Cloud Native — Piliers fondamentaux**
La CNCF définit le cloud native autour de 4 piliers :
1. **Conteneurs** : empaquetage portable et reproductible des applications.
2. **Orchestration** : gestion dynamique des conteneurs à l'échelle (Kubernetes).
3. **Microservices** : architecture en services indépendants, déployables séparément, communiquant via API (REST, gRPC, événements).
4. **DevOps / CI-CD** : automatisation du cycle de vie applicatif (build, test, deploy) et culture de collaboration dev/ops.

Propriétés clés d'une application cloud native :
- **Auto-healing** : les orchestrateurs (K8s) redémarrent automatiquement les conteneurs défaillants et remplacent les nœuds morts.
- **Auto-scaling** : ajustement automatique du nombre d'instances en fonction de la charge (HPA, KEDA pour K8s ; Auto Scaling Groups pour AWS).
- **Immutabilité** : les conteneurs et infrastructures ne sont jamais modifiés en place (pas de SSH en prod), ils sont recréés depuis des artefacts versionnés (IaC, images Docker).
- **Observabilité** : les trois piliers — logs, métriques, traces — sont instrumentés dès la conception (OpenTelemetry).

**Les 12 Facteurs (12-Factor App)**

| # | Facteur | Principe |
|---|---------|----------|
| 1 | Codebase | Un dépôt de code unique par application, plusieurs déploiements (git) |
| 2 | Dependencies | Dépendances déclarées explicitement (requirements.txt, package.json) et isolées |
| 3 | Config | Configuration injectée via variables d'environnement, jamais dans le code |
| 4 | Backing Services | BDD, cache, MQ = services attachés, interchangeables via URL/config |
| 5 | Build, Release, Run | Séparation stricte des étapes de build, release et exécution |
| 6 | Processes | Processus sans état (stateless) ; l'état est externalisé (BDD, cache) |
| 7 | Port Binding | L'application expose ses services via un port (pas de dépendance à un container externe) |
| 8 | Concurrency | Mise à l'échelle par multiplication des processus (scale-out horizontal) |
| 9 | Disposability | Démarrage rapide, arrêt gracieux (SIGTERM géré) |
| 10 | Dev/Prod Parity | Environnements de dev et prod aussi similaires que possible |
| 11 | Logs | Logs traités comme des flux d'événements (stdout/stderr), agrégés externalement |
| 12 | Admin Processes | Tâches d'administration (migrations, scripts) exécutées en processus one-off |

**Évolution : Beyond 12-Factor**
La méthode a été étendue par Kevin Hoffman (2017) avec 3 facteurs supplémentaires : API First, Telemetry, et Authentication/Authorization, formant la méthode "15-Factor".

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Déploiements fréquents et fiables (CI/CD natif) | Complexité architecturale élevée (microservices, orchestration) |
| Résilience intégrée (auto-healing, auto-scaling) | Refactoring profond des applications legacy nécessaire |
| Portabilité inter-cloud et on-premise | Gestion des données distribuées complexe (transactions, cohérence) |
| Meilleure utilisation des ressources (scaling précis) | Compétences spécifiques requises (K8s, observabilité, DevOps) |
| Time-to-market réduit | Coûts initiaux de migration et de formation importants |
| Réduction de la dette technique (immutabilité) | Risque de "microservices sprawl" si mal gouverné |

### Acteurs et solutions du marché
| Catégorie | Solutions |
|-----------|-----------|
| Orchestration | Kubernetes (CNCF), AWS ECS/Fargate, Google Cloud Run |
| CI/CD | GitHub Actions, GitLab CI, Argo CD, Tekton, Jenkins X |
| Observabilité | Prometheus + Grafana, Datadog, New Relic, Dynatrace, OpenTelemetry |
| Service Mesh | Istio, Linkerd |
| Infrastructure as Code | Terraform, Pulumi, AWS CDK, Crossplane |
| Plateforme PaaS cloud native | Red Hat OpenShift, VMware Tanzu, Google Anthos |
| APM / Tracing | Jaeger, Zipkin, Tempo (Grafana) |

### Cas d'usage concrets
1. **Netflix** : pionnier du cloud native, Netflix a migré vers AWS entre 2008 et 2016. L'ensemble de la plateforme est basé sur des microservices auto-scalants (Chaos Engineering via Chaos Monkey pour tester la résilience). Résultat : 99,99 % de disponibilité pour 260 millions d'abonnés.
2. **La Redoute** : refonte de son SI e-commerce vers une architecture cloud native (microservices, K8s, CI/CD) ayant réduit de 70 % les délais de mise en production et amélioré la disponibilité lors des pics (Black Friday).
3. **Amadeus** : le système de réservation de voyages a migré ses 5 000+ microservices vers une plateforme cloud native pour gérer 5 milliards de transactions par an avec une haute disponibilité.

### Chiffres et tendances
- Les équipes avec des pratiques cloud native ont 6 fois moins d'incidents en production (DORA, 2023).
- 95 % des nouvelles applications seront cloud native en 2025 (Gartner).
- L'adoption d'OpenTelemetry (standard d'observabilité) a triplé entre 2021 et 2023 (CNCF).
- GitOps (Argo CD, Flux) devient le standard de déploiement cloud native : +120 % d'adoption en 2 ans.

## Flashcards
#flashcards/Cloud_et_Virtualisation/Cloud_Native_et_12_Factor_App #flashcards/Développement/Cloud_Native_et_12_Factor_App
- Quels sont les 4 piliers du cloud native selon la CNCF ? :: Conteneurs, orchestration (Kubernetes), microservices, et pratiques DevOps/CI-CD.
- Que dit le facteur n°3 (Config) de la 12-Factor App ? :: Toute configuration doit être injectée via des variables d'environnement, jamais codée en dur dans le code source.
- Qu'est-ce que l'auto-healing dans Kubernetes ? :: La capacité de K8s à détecter automatiquement les pods ou nœuds défaillants et à les redémarrer ou remplacer sans intervention humaine.
- Pourquoi le facteur n°6 (Stateless Processes) est-il essentiel au cloud native ? :: Un processus sans état peut être instancié, supprimé ou déplacé à tout moment, ce qui permet le scaling horizontal et la résilience (l'état étant dans des services externes : BDD, cache).
- Quelle est la différence entre "lift-and-shift" et cloud native ? :: Lift-and-shift migre une application sans la modifier (peu de bénéfices cloud) ; cloud native la refonde pour exploiter l'élasticité, l'auto-scaling et la résilience du cloud.
- Qu'est-ce que l'immutabilité de l'infrastructure ? :: Le principe selon lequel les serveurs/conteneurs ne sont jamais modifiés en place mais recréés depuis des artefacts versionnés (images Docker, IaC), garantissant reproductibilité et traçabilité.
- Qu'est-ce qu'OpenTelemetry ? :: Un standard open source (CNCF) pour instrumenter les applications et collecter logs, métriques et traces de façon unifiée et portable entre les outils d'observabilité.

## Sources
- CNCF Cloud Native Definition : https://github.com/cncf/toc/blob/main/DEFINITION.md
- The 12-Factor App : https://12factor.net/
- DORA State of DevOps Report 2023 : https://dora.dev/
- Gartner, "Cloud-Native Application Platforms", 2024
- Kevin Hoffman, *Beyond the 12-Factor App*, O'Reilly, 2017

## Notions liées
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Service Mesh]]
- [[FinOps]]
- [[Infrastructure des datacenters]]
- [[Acteurs cloud]]
