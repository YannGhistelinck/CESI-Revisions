---
type: notion
thèmes:
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Migration cloud (les 7R)

![[N — Migration cloud (les 7R).mp3]]
## En bref
> **Définition** : Les 7R (ou parfois 6R) sont un cadre de stratégies de migration cloud permettant à une DSI de décider comment traiter chaque application lors d'un passage vers le cloud. Ils vont du simple déplacement à l'identique (Rehost) à la suppression de l'application (Retire), en passant par la refonte complète (Rebuild). Ce framework, popularisé par AWS et Gartner, structure la phase de cloud readiness assessment et le wave planning.
> **Pourquoi c'est important** : La migration cloud ne se résume pas à un "lift & shift" générique. Appliquer la mauvaise stratégie à une application peut entraîner des surcoûts importants, des problèmes de performance ou une dette technique accrue. Un DSI doit être capable de justifier la stratégie choisie pour chaque application à partir d'une analyse de valeur métier et de complexité technique.
> **Chiffres clés** :
> - 80 % des entreprises signalent que les migrations cloud ont dépassé le budget initial prévu (Flexera, State of the Cloud 2023)
> - 47 % des workloads d'entreprise seront dans le cloud public en 2026 (IDC, 2023)
> - Les projets qui intègrent un cloud readiness assessment formel réduisent de 35 % les risques de dépassement de budget (McKinsey, 2022)

## Approfondir

### Fonctionnement

**Les 7 stratégies de migration (7R)**

| Stratégie | Nom courant | Description |
|-----------|-------------|-------------|
| **Rehost** | Lift & Shift | Migrer l'application sans la modifier dans une VM cloud. Rapide, sans optimisation. |
| **Replatform** | Lift, Tinker & Shift | Migrer avec des optimisations mineures (ex : passer de MySQL on-premise à RDS). Pas de refonte du code. |
| **Repurchase** | Drop & Shop | Remplacer l'application par une solution SaaS équivalente (ex : CRM Siebel → Salesforce). |
| **Refactor / Re-architect** | Re-architecture | Revoir en profondeur l'architecture pour exploiter les services cloud-native (microservices, serverless, conteneurs). |
| **Retire** | — | Désactiver l'application. Elle n'apporte plus de valeur métier ou est couverte par une autre. |
| **Retain** | Revisit | Conserver l'application on-premise pour l'instant (dépendances non résolues, coût de migration > bénéfice). |
| **Relocate** | Hypervisor Lift & Shift | Migrer l'infrastructure virtualisée vers le cloud sans modifier l'OS ni les VMs (ex : VMware Cloud on AWS). |

**Cloud Readiness Assessment**
Évaluation de la maturité d'une application et de son organisation pour une migration cloud. Couvre : l'inventaire applicatif (CMDB), les dépendances entre applications, la criticité métier, les contraintes réglementaires (données souveraines, HDS, PCI-DSS), le niveau de dette technique et les compétences disponibles. Produit une matrice de priorisation par application (complexité vs. valeur).

**Wave Planning**
Organisation de la migration en vagues successives. La vague 1 (Wave 1) contient les applications les plus simples et les moins critiques (Quick Wins, typiquement Rehost/Retire). Les vagues suivantes traitent les applications plus complexes (Refactor, Repurchase). Objectif : apprendre et ajuster la méthode au fil des vagues, réduire le risque.

**Lift & Shift (Rehost) — avantages et limites**
Avantages : rapidité (semaines vs. mois), faible risque fonctionnel, idéal pour sortir rapidement d'un datacenter en fin de contrat. Limites : ne bénéficie pas des avantages cloud-native (scalabilité, élasticité, résilience), peut coûter plus cher que le on-premise si l'instance n'est pas redimensionnée.

**Strangler Fig Pattern**
Pattern de modernisation progressive d'une application legacy. On développe de nouvelles fonctionnalités autour du système existant (comme le figuier étrangleur autour d'un arbre), en redirigeant progressivement le trafic vers le nouveau système jusqu'à ce que l'ancien soit complètement remplacé. Évite la réécriture big-bang risquée. Proposé par Martin Fowler.

**FinOps et optimisation post-migration**
La migration ne suffit pas : sans optimisation, le cloud coûte souvent plus cher que le on-premise. Le FinOps (Financial Operations) est une discipline qui aligne ingénierie, finance et métier pour optimiser les coûts cloud. Actions : rightsizing, Reserved Instances, Savings Plans, suppression des ressources inutilisées.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Framework structuré pour décisions objectives | Complexité d'inventaire dans les grandes organisations (legacy peu documenté) |
| Priorisation possible des applications à forte valeur | Rehost seul n'optimise pas les coûts cloud sur le long terme |
| Réduction du risque via les vagues | Wave planning peut allonger la durée globale de migration |
| Retire et Repurchase réduisent le nombre d'applications à maintenir | Refactor nécessite des compétences cloud-native souvent à acquérir |
| Adapté à une approche agile de la migration | Résistance organisationnelle aux changements de processus (Repurchase) |

### Acteurs et solutions du marché

| Outil / Service | Rôle | Éditeur |
|-----------------|------|---------|
| AWS Migration Hub | Pilotage centralisé de migrations | AWS |
| AWS Application Discovery Service | Inventaire et dépendances | AWS |
| Azure Migrate | Évaluation + migration | Microsoft |
| Google Cloud Migrate | Migration VMs vers GCP | Google |
| Movere (racheté par Microsoft) | Cloud readiness assessment | Microsoft |
| CloudEndure Migration | Réplication en continu (Rehost) | AWS |
| Carbonite Migrate | Migration serveurs physiques/virtuels | OpenText |

### Cas d'usage concrets

1. **DSI d'une PME : sortie de datacenter en 6 mois** : Une PME de 200 personnes doit libérer son datacenter colocalisé. Le cloud readiness assessment classe 12 applications : 5 en Retire (obsolètes), 4 en Rehost (ERP, serveur de fichiers), 2 en Repurchase (messagerie → Microsoft 365, RH → Workday), 1 en Refactor (portail client). Les vagues 1 et 2 (Retire + Rehost) sont réalisées en 3 mois, permettant la libération du datacenter dans les délais.

2. **Groupe industriel : modernisation par Strangler Fig** : Un groupe industriel possède un ERP monolithique développé en interne en 2003. Plutôt qu'une réécriture complète (risque élevé), il applique le Strangler Fig Pattern : chaque module (facturation, stock, achats) est progressivement remplacé par un microservice cloud-native, exposé via une API Gateway. Le système legacy coexiste 3 ans avec les nouveaux modules avant d'être désactivé.

3. **Banque régionale : wave planning sur 18 mois** : Une banque avec 80 applications planifie sa migration en 4 vagues. Wave 1 (3 mois) : 20 applications Retire + 15 Rehost (non critiques). Wave 2 (4 mois) : 12 Replatform (bases de données → RDS). Wave 3 (6 mois) : 8 Repurchase (GRC, collaboration). Wave 4 (5 mois) : 5 Refactor (applications métier critiques en microservices). Résultat : 90 % des workloads dans le cloud en 18 mois.

### Chiffres et tendances

- Le framework 5R initial vient de Gartner (2010), étendu à 6R par AWS (2012) puis 7R avec l'ajout de "Relocate"
- En moyenne, 30 % des applications identifiées lors d'un assessment sont candidats au Retire (McKinsey)
- 60 % des migrations cloud commencent par du Rehost mais évoluent vers du Refactor dans les 2 ans (IDC)
- Le coût d'une migration cloud bien planifiée est typiquement amorti en 2-3 ans par les économies réalisées (moins de datacenter, élasticité, réduction des licences)

## Flashcards
#flashcards/Cloud_et_Virtualisation/Migration_cloud_les_7R

Quelles sont les 7 stratégies de migration cloud (7R) ? :: Rehost (Lift & Shift), Replatform, Repurchase (SaaS), Refactor/Re-architect, Retire, Retain, Relocate (Hypervisor Lift & Shift).

Quelle est la différence entre Rehost et Replatform ? :: Rehost = migration à l'identique sans modification (Lift & Shift). Replatform = migration avec optimisations mineures sans refonte du code (ex : passer d'une BDD on-premise à un service managé RDS).

Qu'est-ce qu'un Cloud Readiness Assessment ? :: Évaluation de la maturité d'une application pour le cloud. Couvre l'inventaire applicatif, les dépendances, la criticité métier, les contraintes réglementaires et la dette technique. Produit une matrice complexité vs. valeur pour prioriser les migrations.

Qu'est-ce que le Wave Planning ? :: Organisation de la migration en vagues successives, des applications les plus simples (Wave 1, Quick Wins) aux plus complexes. Permet d'apprendre et d'ajuster la méthode au fil des vagues, et de réduire le risque global.

Qu'est-ce que le Strangler Fig Pattern ? :: Pattern de modernisation progressive : on développe de nouvelles fonctionnalités cloud-native autour du système legacy et on redirige progressivement le trafic vers le nouveau système, jusqu'à ce que l'ancien soit désactivé. Évite la réécriture big-bang.

Quel est le principal risque d'un Rehost sans optimisation ? :: Le coût : une application migrée à l'identique dans le cloud peut coûter plus cher que on-premise si l'instance n'est pas redimensionnée (rightsizing) et si les avantages cloud-native (élasticité, services managés) ne sont pas exploités.

Quelle stratégie adopter pour remplacer un CRM legacy par Salesforce ? :: Repurchase (Drop & Shop) : on abandonne l'application legacy et on la remplace par une solution SaaS équivalente du marché. C'est la stratégie la plus rapide pour se débarrasser d'une application standard à faible différenciation.

## Sources

- AWS, "6 Strategies for Migrating Applications to the Cloud", 2012 (mise à jour 7R, 2021)
- Gartner, "Key Criteria for Evaluating Cloud Migration Tools", 2023
- McKinsey, "Cloud's trillion-dollar prize is up for grabs", 2021
- Flexera, "State of the Cloud Report", 2023
- IDC, "Cloud Migration Market Trends", 2023
- Martin Fowler, "Strangler Fig Application", martinfowler.com

## Notions liées
- [[Virtualisation]]
- [[Legacy et dette technique]]
- [[FinOps]]
- [[Infrastructure des datacenters]]
- [[Sécurité cloud (CSPM - CASB - CNAPP)]]
