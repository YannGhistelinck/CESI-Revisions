---
type: notion
thèmes:
  - Optimisation du SI
  - Développement
statut: pas vu
dernière_révision: 
---

# ChatOps

## En bref

### Définition
Le ChatOps est une pratique de collaboration qui centralise les opérations IT et DevOps dans une plateforme de messagerie d'équipe (Slack, Microsoft Teams). Des bots et intégrations permettent de déclencher des pipelines, consulter des alertes, gérer des incidents et partager du contexte directement dans le chat, rendant les opérations visibles et collaboratives.

### Pourquoi c'est important
Le ChatOps réduit les silos entre développement et opérations, améliore la visibilité en temps réel sur l'état des systèmes et accélère la résolution d'incidents (MTTR). Il constitue une évolution naturelle de la culture DevOps vers plus de transparence et d'automatisation conversationnelle.

### Chiffres clés
- Les équipes pratiquant le ChatOps réduisent leur **MTTR de 40 à 60 %** (PagerDuty, 2022)
- **75 % des équipes DevOps** utilisent Slack ou Microsoft Teams comme hub de collaboration (State of DevOps 2023)
- Le marché des plateformes de collaboration d'entreprise dépasse **50 Md$ en 2024**
- Un incident géré via ChatOps mobilise en moyenne **30 % moins de personnes** grâce à la visibilité partagée

---

## Approfondir

### Fonctionnement

Le ChatOps repose sur trois piliers :

1. **La plateforme de messagerie** — canal central (Slack, Teams, Mattermost)
2. **Le bot (chatbot opérationnel)** — agent qui écoute les commandes et interagit avec les outils (CI/CD, monitoring, ticketing)
3. **Les intégrations** — connecteurs entre le chat et les outils métier (GitHub, Jenkins, Datadog, PagerDuty, Jira)

#### Flux typique d'un incident en ChatOps

```
Alerte Datadog → #incidents (Slack)
  → @bot : /acknowledge INC-001
  → @bot : /deploy rollback service-api v2.3.1
  → @bot : /runbook INC-001
  → Post-mortem partagé dans le canal
```

#### Composants clés

| Composant | Rôle | Exemples |
|---|---|---|
| **Plateforme chat** | Hub de communication | Slack, Teams, Mattermost |
| **Bot framework** | Moteur d'exécution des commandes | Hubot, Lita, Errbot, Opsdroid |
| **CI/CD intégration** | Déclenchement de pipelines | Jenkins, GitHub Actions, GitLab CI |
| **Monitoring** | Alertes et métriques | Datadog, Grafana, PagerDuty |
| **Ticketing** | Gestion des incidents | Jira, ServiceNow, OpsGenie |

#### ChatOps vs approches traditionnelles

| Critère | Traditionnel | ChatOps |
|---|---|---|
| Communication | Email, téléphone | Canal dédié en temps réel |
| Contexte | Dispersé, silotisé | Centralisé et historisé |
| Actions | CLI, portails séparés | Commandes dans le chat |
| Visibilité | Limitée à l'opérateur | Toute l'équipe voit les actions |
| Onboarding | Lent | Rapide (lecture de l'historique) |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Visibilité totale des opérations en temps réel | Risque de surcharge d'alertes (alert fatigue) |
| Réduction du MTTR par mobilisation rapide | Sécurité : commandes sensibles dans le chat |
| Historique des actions et décisions | Dépendance à la plateforme (vendor lock-in) |
| Onboarding facilité (lisibilité de l'historique) | Courbe d'apprentissage pour les équipes |
| Automatisation conversationnelle sans CLI | Canaux mal organisés = chaos informationnel |

### Acteurs

- **Plateformes** : Slack (Salesforce), Microsoft Teams, Mattermost (open source)
- **Frameworks de bots** : Hubot (GitHub), Lita (Ruby), Errbot (Python), Opsdroid
- **Outils intégrés** : PagerDuty, OpsGenie, Datadog, GitHub, GitLab, Jenkins
- **Pionniers** : GitHub (créateur de Hubot, 2011) — ChatOps popularisé par Jesse Newland

### Cas d'usage

- **Gestion d'incidents** : réception d'alertes, acknowledge, rollback, post-mortem — tout depuis Slack
- **Déploiements** : `@bot deploy app v2.1 to production` avec confirmation et audit trail
- **Revue de code** : notifications PR, merge, blockers directement dans Teams
- **Reporting** : `@bot status dashboard` affiche les KPI en temps réel dans le canal
- **Sécurité** : alertes SIEM remontées dans un canal #security avec actions de confinement

### Chiffres complémentaires

- GitHub a introduit Hubot en **2011**, popularisant le concept de ChatOps
- Les entreprises utilisant ChatOps déploient **2x plus fréquemment** que celles qui ne le pratiquent pas
- **85 % des ingénieurs** estiment que la visibilité partagée via ChatOps améliore la culture d'équipe

---

## Flashcards
#flashcards

Qu'est-ce que le ChatOps ? :: Une pratique qui centralise les opérations IT dans une plateforme de messagerie (Slack, Teams) via des bots et intégrations, rendant les actions visibles et collaboratives.

Quel bot a popularisé le ChatOps et qui l'a créé ? :: Hubot, créé par GitHub en 2011 et développé par Jesse Newland.

Quels sont les 3 piliers du ChatOps ? :: La plateforme de messagerie, le bot opérationnel, et les intégrations avec les outils métier (CI/CD, monitoring, ticketing).

Quel est l'impact du ChatOps sur le MTTR ? :: Réduction de 40 à 60 % du Mean Time To Recover selon PagerDuty.

Quelle est la différence entre ChatOps et simple messagerie d'équipe ? :: Dans le ChatOps, des bots exécutent des commandes réelles (déploiement, rollback, consultation de métriques) directement depuis le chat — ce n'est pas seulement de la communication mais de l'action.

Quel est le principal risque de sécurité lié au ChatOps ? :: L'exposition de commandes sensibles dans les canaux de chat, pouvant inclure des secrets, des accès ou des actions destructrices visibles par de nombreuses personnes.

Quelle est la différence entre Mattermost et Slack/Teams du point de vue de la souveraineté ? :: Mattermost est open source et auto-hébergeable, permettant une maîtrise complète des données, contrairement à Slack (Salesforce) ou Teams (Microsoft) qui sont des solutions SaaS propriétaires.

---

## Sources

- PagerDuty — "The State of Incident Management" (2022)
- DORA — State of DevOps Report 2023
- Jesse Newland — "ChatOps at GitHub" (2012)
- Atlassian — "What is ChatOps?"
- Mattermost documentation

---

## Notions liées

[[DevOps]] · [[CI - CD]] · [[DORA Metrics]] · [[SLA - SLO - SLI]] · [[MTTR - MTBF]] · [[Observabilité]] · [[Platform Engineering]] · [[SRE (Site Reliability Engineering)]] · [[Système d'Information (SI)]]
