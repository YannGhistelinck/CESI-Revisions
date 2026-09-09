---
type: notion
thèmes:
  - Développement
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# DevOps

## En bref
> **Définition** : Le DevOps est un mouvement culturel et organisationnel né de la conférence Agile 2008 et formalisé par Patrick Debois en 2009 (première DevOpsDays à Gand). Il vise à abattre le cloisonnement entre les équipes de développement (Dev) et d'exploitation (Ops) pour livrer des logiciels plus rapidement, de façon plus fiable et plus sûre. Gene Kim (co-auteur de *The Phoenix Project*, 2013) a théorisé les **3 voies** qui en constituent le cadre intellectuel.
> **Pourquoi c'est important** : Dans une DSI classique, le "mur de la confusion" entre Dev (vitesse) et Ops (stabilité) génère des délais, des incidents et de la dette technique. Le DevOps supprime ce mur via l'automatisation, la collaboration et la mesure continue, permettant des déploiements fréquents sans sacrifier la qualité.
> **Chiffres clés** :
> - Les organisations "Elite DevOps" déploient 973 fois plus fréquemment et restaurent le service 6 570 fois plus vite que les organisations à faible performance (DORA Report, 2023).
> - 83 % des DSI considèrent le DevOps comme une priorité stratégique (Gartner, 2024).
> - Le marché des outils DevOps atteindra 25,5 Md$ en 2028 (MarketsandMarkets).

## Approfondir

### Fonctionnement

**Les 3 voies de Gene Kim**

| Voie | Principe | Pratiques |
|------|----------|-----------|
| 1re voie — Flow | Accélérer le flux de valeur de gauche (dev) à droite (prod) | CI/CD, automatisation des tests, small batches, limiter le WIP |
| 2e voie — Feedback | Créer des boucles de retour d'information rapides de droite à gauche | Monitoring, alerting, tests automatisés, feature flags |
| 3e voie — Apprentissage | Culture d'amélioration continue et d'expérimentation | Blameless post-mortem, chaos engineering, Game Days, partage de connaissances |

**Le modèle CALMS**
Framework d'évaluation de la maturité DevOps (Damon Edwards & John Willis, popularisé par Jez Humble) :
- **C**ulture : collaboration, confiance, responsabilité partagée (fin du "c'est pas mon problème")
- **A**utomation : automatiser tout ce qui est répétable (tests, build, déploiement, infrastructure)
- **L**ean : réduire les gaspillages, limiter le WIP (Work In Progress), amélioration continue (Kaizen)
- **M**easurement : mesurer tout — déploiements, taux d'échec, MTTR, lead time — pour décider par les données
- **S**haring : partager les outils, les pratiques, les post-mortems et les succès entre Dev et Ops

**Les 4 métriques DORA (indicateurs de performance DevOps)**
1. **Deployment Frequency** : fréquence des déploiements en production
2. **Lead Time for Changes** : délai entre le commit et la mise en production
3. **Change Failure Rate** : pourcentage de déploiements causant un incident
4. **Time to Restore Service** (MTTR) : temps de rétablissement après incident

**Cycle de vie DevOps (boucle infinie)**
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → (retour à Plan)

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Time-to-market drastiquement réduit | Transformation culturelle longue et difficile |
| Meilleure qualité logicielle (tests automatisés) | Résistances organisationnelles et silos établis |
| Résilience accrue (feedback rapide, MTTR réduit) | Investissement initial en outils et formation important |
| Collaboration et satisfaction des équipes améliorées | Risque de "DevOps washing" (outils sans culture) |
| Réduction des coûts opérationnels à long terme | Sécurité pouvant être négligée si non intégrée (d'où DevSecOps) |
| Traçabilité et auditabilité complètes | Complexité des chaînes d'outils (toolchain sprawl) |

### Acteurs et solutions du marché
| Catégorie | Solutions |
|-----------|-----------|
| Plateformes DevOps complètes | GitLab, Azure DevOps, GitHub (Actions + Packages) |
| CI/CD | Jenkins, GitHub Actions, GitLab CI, CircleCI, TeamCity |
| Gestion de configuration / IaC | Ansible, Terraform, Chef, Puppet |
| Conteneurisation & orchestration | Docker, Kubernetes, OpenShift |
| Monitoring / Observabilité | Prometheus, Grafana, Datadog, Dynatrace |
| Collaboration | Jira, Confluence, Slack, Microsoft Teams |

### Cas d'usage concrets
1. **ING Bank** : la banque néerlandaise a adopté le modèle de squads autonomes (inspiré de Spotify) couplé au DevOps. Résultat : passage de 1 déploiement par an à plusieurs par semaine, réduction des incidents de 50 %.
2. **Amazon** : déploie en production toutes les 11,6 secondes en moyenne (soit des milliers de déploiements par jour), rendu possible par des pipelines CI/CD entièrement automatisés et des équipes autonomes (architecture "two-pizza teams").
3. **SNCF Digital** : transformation DevOps progressif pour les applications passagers (SNCF Connect). Adoption de GitLab CI et de conteneurs Docker/Kubernetes pour réduire le lead time de plusieurs semaines à quelques heures.

### Chiffres et tendances
- Les organisations Elite DevOps ont un taux d'échec des changements inférieur à 5 % (DORA, 2023).
- Le DevOps réduit le lead time de plusieurs semaines à quelques heures dans les cas de maturité élevée.
- 45 % des entreprises sont encore au stade "medium" ou "low" de maturité DevOps (DORA, 2023).
- L'émergence de Platform Engineering (équipes dédiées à créer des "Internal Developer Platforms") est la tendance 2024-2025 pour industrialiser le DevOps à grande échelle.

## Flashcards
#flashcards/Développement/DevOps #flashcards/Optimisation_du_SI/DevOps
- Qui a inventé le terme "DevOps" et quand ? :: Patrick Debois lors de la première DevOpsDays à Gand (Belgique) en 2009.
- Quelles sont les 3 voies de Gene Kim ? :: Flow (accélérer la livraison de gauche à droite), Feedback (boucles de retour rapides), et Learning/Continual Experimentation (amélioration continue et culture d'apprentissage).
- Que signifie l'acronyme CALMS ? :: Culture, Automation, Lean, Measurement, Sharing — framework d'évaluation de la maturité DevOps.
- Quelles sont les 4 métriques DORA ? :: Deployment Frequency, Lead Time for Changes, Change Failure Rate, et Time to Restore Service (MTTR).
- Quelle est la différence entre DevOps et Agile ? :: Agile concerne la méthode de développement (itérations courtes, collaboration client) ; DevOps étend cette philosophie à l'exploitation et au déploiement, en automatisant l'ensemble du cycle de livraison.
- Qu'est-ce que le "mur de la confusion" en DevOps ? :: L'opposition traditionnelle entre les Dev (qui veulent livrer vite) et les Ops (qui veulent la stabilité), générant des conflits, des délais et des incidents lors des mises en production.
- Qu'est-ce que le "DevOps washing" ? :: L'adoption d'outils DevOps (Jenkins, GitLab…) sans transformation culturelle réelle — les silos Dev/Ops persistent malgré l'outillage.

## Sources
- Gene Kim, Jez Humble, Patrick Debois, John Willis, *The DevOps Handbook*, IT Revolution Press, 2016
- Gene Kim, Kevin Behr, George Spafford, *The Phoenix Project*, IT Revolution Press, 2013
- DORA State of DevOps Report 2023 : https://dora.dev/
- Gartner, "DevOps Maturity Assessment", 2024

## Notions liées
- [[CI - CD]]
- [[DevSecOps]]
- [[GitOps]]
- [[Infrastructure as Code (IaC)]]
- [[SRE (Site Reliability Engineering)]]
- [[Observabilité]]
- [[Cloud Native et 12-Factor App]]
