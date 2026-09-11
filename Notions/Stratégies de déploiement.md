---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Stratégies de déploiement

## En bref
> **Définition** : Les stratégies de déploiement sont des patterns permettant de livrer de nouvelles versions d'une application en production tout en minimisant les risques d'interruption de service et d'impact utilisateur. Les principales stratégies sont : **blue-green deployment** (basculement entre deux environnements identiques), **canary release** (exposition progressive à un sous-ensemble d'utilisateurs), **rolling update** (remplacement progressif des instances), et **feature flags** (activation/désactivation de fonctionnalités sans redéploiement).
> **Pourquoi c'est important** : Le déploiement est historiquement la phase la plus risquée du cycle de livraison. Ces stratégies permettent de déployer fréquemment (DevOps), de limiter le blast radius en cas de problème, et d'assurer une continuité de service totale — objectif central des SRE et des engagements SLA/SLO.
> **Chiffres clés** :
> - 45 % des incidents de production sont causés par des déploiements (Puppet, 2023).
> - Les organisations Elite DORA déploient à la demande avec un change failure rate < 5 %.
> - Netflix effectue des centaines de canary releases par jour sur ses microservices.

## Approfondir

### Fonctionnement

**1. Recreate (ou "Big Bang")**
Arrêt complet de l'ancienne version, puis déploiement de la nouvelle. Simple, mais génère une indisponibilité. Réservé aux environnements non-critiques ou aux breaking changes impossibles à rendre compatibles.

**2. Rolling Update (déploiement progressif)**
Remplacement des instances une à une (ou par lot) de l'ancienne version par la nouvelle, sans interruption de service. À tout moment, des instances des deux versions coexistent.

| Caractéristique | Détail |
|----------------|--------|
| Indisponibilité | Aucune (si min-replicas respecté) |
| Rollback | Possible mais lent (reverse rolling) |
| Risque | Coexistence de deux versions (compatibilité API) |
| Outil natif | `kubectl rollout` (Kubernetes), AWS ECS rolling update |

**3. Blue-Green Deployment**
Deux environnements identiques (Blue = actuel, Green = nouveau) sont maintenus en parallèle. Le traffic est basculé instantanément du Blue vers le Green via un load balancer ou un DNS switch.

```
Users → Load Balancer → [Blue v1.0] (actif)
                      → [Green v1.1] (inactif, en cours de validation)
          ↓ switch
Users → Load Balancer → [Blue v1.0] (idle, rollback possible)
                      → [Green v1.1] (actif)
```

| Caractéristique | Détail |
|----------------|--------|
| Indisponibilité | Zéro (basculement instantané) |
| Rollback | Instantané (re-basculement vers Blue) |
| Coût | Double infrastructure pendant la transition |
| Usage | Migrations critiques, bases de données, conformité |

**4. Canary Release**
Déploiement progressif sur un faible pourcentage des utilisateurs ou des serveurs (5-10 %), puis augmentation progressive si les métriques sont bonnes (taux d'erreur, latence). Inspiré des "canaris dans les mines de charbon" (alerte précoce).

```
100% users → v1.0
↓ canary à 5%
95% users → v1.0 | 5% users → v1.1 (monitoring)
↓ si métriques OK → 25% → 50% → 100%
↓ si métriques KO → rollback immédiat vers 0%
```

| Caractéristique | Détail |
|----------------|--------|
| Indisponibilité | Aucune |
| Rollback | Rapide (réduction du % de trafic) |
| Détection | Impact limité (blast radius réduit) |
| Outil | Argo Rollouts, Flagger, AWS CodeDeploy, Istio |

**5. A/B Testing vs Canary**
| Aspect | Canary | A/B Testing |
|--------|--------|-------------|
| Objectif | Stabilité technique (erreurs, latence) | Comportement utilisateur (taux de clic, conversion) |
| Durée | Heures à jours | Jours à semaines |
| Routing | % aléatoire | Segmentation ciblée (géo, profil, cohort) |
| Décision | Métriques techniques | Métriques produit (KPI business) |

**6. Feature Flags (Feature Toggles)**
Mécanisme applicatif (et non infra) permettant d'activer ou désactiver une fonctionnalité sans redéploiement. Types :
- **Release toggles** : déployer du code non finalisé (trunk-based dev)
- **Experiment toggles** : A/B testing
- **Ops toggles** : circuit breaker, kill switch en production
- **Permission toggles** : accès conditionnel (premium users)

Solutions : LaunchDarkly, Unleash, Flagsmith, Growthbook, OpenFeature (standard CNCF).

**Shadow Deployment (Traffic Mirroring)**
La nouvelle version reçoit une copie du trafic de production en temps réel mais ne renvoie pas de réponse aux utilisateurs. Permet de tester le comportement en conditions réelles sans risque. Utilisé par Netflix (Diffy), LinkedIn.

### Avantages / Inconvénients par stratégie
| Stratégie | Avantages | Inconvénients |
|-----------|-----------|---------------|
| Recreate | Simple, pas de compatibilité à gérer | Indisponibilité (downtime) |
| Rolling Update | Zéro downtime, peu de surcoût infra | Coexistence de versions, rollback lent |
| Blue-Green | Rollback instantané, tests complets en prod-like | Double coût infra, état de la BDD complexe |
| Canary | Blast radius minimal, détection précoce | Orchestration complexe, métriques à surveiller |
| Feature Flags | Découplage déploiement/release, kill switch | Dette technique (flags à nettoyer), complexité du code |

### Acteurs et solutions du marché
| Catégorie | Solutions |
|-----------|-----------|
| Orchestration K8s | Argo Rollouts, Flagger (Weaveworks), Spinnaker |
| Feature Flags | LaunchDarkly, Unleash, Flagsmith, Growthbook |
| Service Mesh (trafic) | Istio, Linkerd, AWS App Mesh |
| Cloud natif | AWS CodeDeploy, Azure Deployment Slots, GCP Traffic Splitting |
| CI/CD intégré | GitHub Actions (environments), GitLab (environments), Harness |

### Cas d'usage concrets
1. **Facebook** : utilise intensivement les feature flags ("Gatekeeper" system) pour contrôler l'exposition de chaque fonctionnalité. Chaque feature est d'abord activée pour les employés Facebook, puis pour 1 %, 10 %, 50 % des utilisateurs. Cela permet des déploiements quotidiens sans downtime pour 3 milliards d'utilisateurs.
2. **Booking.com** : pionnier du A/B testing à grande échelle (1 000+ expériences simultanées). Utilise des canary releases combinées à des feature flags pour déployer des changements sur son moteur de recommandation, mesurant l'impact sur le taux de réservation avant rollout complet.
3. **Zalando** : utilise le blue-green deployment pour ses mises en production des services de paiement, garantissant un rollback en moins de 30 secondes en cas d'anomalie détectée par les métriques de taux d'erreur.

### Chiffres et tendances
- 78 % des équipes utilisant des canary releases rapportent une réduction des incidents de production (DORA, 2023).
- Progressive Delivery (canary + feature flags + observabilité) est la tendance post-CI/CD (Jez Humble, 2021).
- Argo Rollouts a été adopté par 40 % des équipes K8s utilisant des déploiements avancés (CNCF Survey, 2024).
- Le marché des feature flag management atteindra 1,2 Md$ en 2028.

## Flashcards
#flashcards
- Quelle est la différence entre un canary release et un A/B test ? :: Le canary release vise la stabilité technique (erreurs, latence) avec un % aléatoire d'utilisateurs pendant quelques heures. L'A/B test vise à mesurer un comportement utilisateur (conversion, clic) avec une segmentation ciblée sur plusieurs semaines.
- Comment fonctionne le blue-green deployment ? :: Deux environnements identiques (Blue = actif, Green = nouveau) coexistent. Le trafic est basculé instantanément via un load balancer du Blue vers le Green une fois validé. Le Blue reste disponible pour un rollback immédiat.
- Quel est le principal inconvénient du blue-green deployment ? :: Le double coût d'infrastructure (deux environnements complets maintenus en parallèle) et la complexité de gestion de l'état de la base de données (migrations de schéma compatibles avec les deux versions).
- Qu'est-ce qu'un "ops toggle" dans les feature flags ? :: Un toggle utilisé comme kill switch opérationnel en production — il permet de désactiver immédiatement une fonctionnalité défaillante sans redéploiement, réduisant le MTTR à quelques secondes.
- Qu'est-ce que le "shadow deployment" (traffic mirroring) ? :: Une technique où la nouvelle version reçoit une copie du trafic de production en temps réel mais ne renvoie pas de réponse aux utilisateurs. Elle permet de tester en conditions réelles sans risque d'impact.
- Pourquoi la coexistence de versions est-elle un défi dans le rolling update ? :: Pendant la transition, des instances de l'ancienne et de la nouvelle version traitent simultanément des requêtes. Les APIs et les schémas de BDD doivent être rétrocompatibles pour éviter les erreurs (principe d'expand-contract).
- Qu'est-ce que le "Progressive Delivery" ? :: Une évolution de la CI/CD qui combine déploiement progressif (canary), feature flags et observabilité pour contrôler finement le rollout des fonctionnalités, réduisant le risque tout en maintenant une haute fréquence de livraison.

## Sources
- Jez Humble, "Progressive Delivery", 2018 : https://redmonk.com/jgovernor/2018/08/06/towards-progressive-delivery/
- Argo Rollouts documentation : https://argoproj.github.io/rollouts/
- Martin Fowler, "Feature Toggles (aka Feature Flags)" : https://martinfowler.com/articles/feature-toggles.html
- DORA State of DevOps Report 2023 : https://dora.dev/
- Flagger (Progressive Delivery for Kubernetes) : https://flagger.app/

## Notions liées
- [[CI - CD]]
- [[DevOps]]
- [[GitOps]]
- [[SRE (Site Reliability Engineering)]]
- [[Observabilité]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Service Mesh]]
