---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Économie du cloud

## En bref
> **Définition** : L'économie du cloud repose sur la transformation des dépenses informatiques de CAPEX (investissements) en OPEX (charges opérationnelles), avec un modèle pay-as-you-go. Elle introduit des mécanismes d'optimisation spécifiques (reserved instances, savings plans) et des coûts cachés (egress fees) qu'une DSI doit maîtriser pour éviter le dérapage budgétaire.
> **Pourquoi c'est important** : Le cloud ne réduit pas mécaniquement les coûts. Sans gouvernance FinOps, les entreprises constatent fréquemment une dérive de 30 à 40% par rapport aux prévisions. La maîtrise des modèles tarifaires est un enjeu stratégique pour la DSI.
> **Chiffres clés** :
> - 32% du budget cloud est gaspillé en ressources inutilisées ou surdimensionnées (Flexera, 2024)
> - Les egress fees représentent en moyenne 5 à 15% de la facture cloud totale d'une entreprise (FinOps Foundation, 2023)
> - Le marché mondial du cloud computing dépasse 650 milliards de dollars en 2024 (Gartner)

## Approfondir

### Fonctionnement

**CAPEX vs OPEX**
- **CAPEX (Capital Expenditure)** : investissement en immobilisations (serveurs, licences perpétuelles, bâtiments). Amorti sur plusieurs années. Avantage : prévisibilité long terme. Inconvénient : rigidité, sur-provisionnement fréquent.
- **OPEX (Operating Expenditure)** : charge d'exploitation mensuelle ou annuelle (abonnements SaaS, facturation cloud à l'usage). Avantage : flexibilité, pas d'investissement initial. Inconvénient : accumulation sur la durée potentiellement coûteuse.

Le cloud convertit structurellement le CAPEX en OPEX. Cette transformation impacte la comptabilité, la fiscalité (charges déductibles immédiatement) et la planification budgétaire.

**Pay-as-you-go (à l'usage)**
Modèle de facturation par défaut des clouds publics : facturation à la seconde ou à la minute selon la consommation réelle. Idéal pour les workloads imprévisibles ou variables. Tarif le plus élevé à l'unité.

**Reserved Instances (RI)**
Engagement de 1 ou 3 ans sur un type d'instance spécifique, en échange d'une réduction de 30 à 70% par rapport au tarif à l'usage. Adapté aux workloads stables et prévisibles. Variante AWS : Convertible Reserved Instances (flexibilité de changement d'instance).

**Savings Plans (SP)**
Engagement de dépense horaire sur 1 ou 3 ans (ex. : 10$/h minimum), sans engagement sur un type d'instance spécifique. Plus flexible que les RI. Disponible chez AWS et Azure. Réductions de 20 à 66%.

**Spot Instances / Preemptible VMs**
Ressources non utilisées vendues avec une décote de 70 à 90%. L'instance peut être interrompue avec un préavis court (2 minutes chez AWS). Adapté aux workloads tolérants aux interruptions : batch, rendu 3D, ML training.

**Egress fees (frais de sortie)**
Facturation du trafic de données sortant du cloud vers internet ou vers d'autres régions. Le trafic entrant est généralement gratuit. Les egress fees créent une asymétrie qui rend la sortie coûteuse et favorise le vendor lock-in. En 2024, AWS, Azure et GCP ont réduit leurs egress fees sous la pression réglementaire européenne (Data Act).

**Cloud repatriation**
Tendance consistant à rapatrier certains workloads du cloud public vers une infrastructure on-premise ou en colocation, lorsque l'analyse économique montre qu'un workload stable et prévisible est moins cher on-premise sur 3-5 ans. Exemple célèbre : Dropbox (2016, économie de 75 millions de dollars sur 2 ans).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Pas d'investissement initial (CAPEX → OPEX) | Coûts OPEX cumulés supérieurs au CAPEX sur le long terme |
| Paiement à l'usage (flexibilité) | Egress fees : coût de sortie peu visible mais élevé |
| Réductions significatives via RI/SP (jusqu'à 70%) | Complexité des modèles tarifaires (des centaines de lignes) |
| Élasticité financière (scale-in possible) | Sur-provisionnement fréquent sans gouvernance FinOps |
| Spot instances pour workloads tolérants | Risque de dérapage budgétaire sans pilotage |

### Acteurs et solutions du marché

- **Optimisation de coûts cloud** : AWS Cost Explorer, Azure Cost Management, Google Cloud Billing, Spot.io (maintenant NetApp), Apptio Cloudability, CloudHealth (VMware)
- **FinOps** : FinOps Foundation (organisation de référence), outils open source Infracost (estimation IaC)
- **Comparateurs de prix cloud** : cloudprice.net, infracost.io, ec2instances.info
- **Marché de RI d'occasion** : AWS Marketplace, Reserved Instance Marketplace (revente de RI non utilisées)
- **Analyse d'egress fees** : CloudZero, ProsperOps

### Cas d'usage concrets

1. **Optimisation RI pour un groupe industriel** : une DSI analyse ses workloads de production stables (ERP, bases de données). Conversion de 60% de la facturation à l'usage en Reserved Instances 3 ans. Économie réalisée : 48% sur ce périmètre, soit 200 000 euros/an.

2. **Spot instances pour ML** : une équipe data science utilise des instances Spot AWS pour entraîner ses modèles de ML la nuit. Les jobs sont conçus pour être interruptibles (checkpointing). Réduction de 75% du coût de calcul GPU par rapport au tarif on-demand.

3. **Cloud repatriation partielle** : une scale-up SaaS hébergeait toute sa base de données sur RDS (AWS). Après analyse, les workloads de bases de données relationnelles stables sont rapatriés sur des serveurs en colocation. Économie de 40% sur 3 ans. Les couches applicatives restent sur AWS pour la flexibilité.

### Chiffres et tendances

- Le coût de l'egress chez AWS est de 0,09 $/Go vers internet (Europe), gratuit vers S3 dans la même région
- En 2024, sous l'impulsion du Data Act européen, AWS, Azure et GCP ont annoncé des suppressions ou réductions importantes des egress fees pour les clients quittant le cloud
- 60% des entreprises ont dépassé leur budget cloud en 2023 (Flexera)
- Reserved Instances : ROI typique de 30-50% sur 1 an, 50-70% sur 3 ans vs on-demand
- Tendance : émergence du FinOps comme discipline à part entière (certification FinOps Certified Practitioner de la FinOps Foundation)

## Flashcards
#flashcards

Quelle est la différence entre CAPEX et OPEX dans le contexte cloud ? :: CAPEX = investissement en immobilisation (serveurs physiques, licences perpétuelles), amorti sur plusieurs années. OPEX = charge opérationnelle courante (abonnements, facturation à l'usage). Le cloud convertit structurellement le CAPEX en OPEX.

Qu'est-ce qu'une Reserved Instance et pour quel usage est-elle adaptée ? :: Engagement de 1 ou 3 ans sur un type d'instance spécifique en échange d'une réduction de 30 à 70%. Adaptée aux workloads stables et prévisibles (production, bases de données).

Qu'est-ce qu'un Savings Plan et en quoi diffère-t-il d'une Reserved Instance ? :: Le Savings Plan est un engagement sur un montant de dépense horaire (et non sur un type d'instance), plus flexible. Réductions similaires aux RI mais applicable à différents types de services et instances.

Qu'est-ce qu'une Spot Instance et quels workloads peut-elle héberger ? :: Instance sur capacité non utilisée du cloud, vendue avec 70-90% de réduction mais pouvant être interrompue à tout moment (préavis 2 min). Adaptée aux traitements batch, ML training, rendu, workloads tolérants aux interruptions.

Qu'est-ce qu'un egress fee et pourquoi est-il problématique ? :: Frais facturés pour les données sortant du cloud vers internet ou une autre région. Rend la sortie coûteuse et contribue au vendor lock-in. Peu visible dans les budgets initiaux.

Pourquoi le cloud ne réduit-il pas automatiquement les coûts IT ? :: Sans gouvernance FinOps, les ressources mal dimensionnées, les instances oubliées et les egress fees génèrent des surcoûts. 32% du budget cloud est gaspillé en moyenne (Flexera, 2024).

Qu'est-ce que le cloud repatriation et dans quel contexte économique a-t-il du sens ? :: Retour de workloads cloud vers du on-premise. Pertinent quand un workload est stable, prévisible et volumétrique : le TCO on-premise sur 3-5 ans peut être inférieur au coût cloud continu.

## Sources

- Flexera, "State of the Cloud Report 2024"
- FinOps Foundation, "State of FinOps 2023"
- Gartner, "Public Cloud Services Forecast Worldwide", 2024
- AWS, Azure, Google Cloud — pages officielles de tarification
- Andreessen Horowitz (a16z), "The Cost of Cloud", 2021 (article de référence sur le cloud repatriation)

## Notions liées

- [[FinOps]]
- [[Modèles de service cloud]]
- [[Modèles de déploiement cloud]]
- [[Vendor lock-in et réversibilité]]
- [[Infrastructure des datacenters]]
