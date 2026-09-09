---
type: notion
thèmes:
  - SI et environnement
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# FinOps

## En bref
> **Définition** : Le FinOps (Financial Operations) est une pratique de gouvernance financière du cloud qui vise à optimiser les dépenses cloud en responsabilisant les équipes techniques sur les coûts. Il repose sur un cycle Informer – Optimiser – Opérer impliquant les équipes Finance, Tech et Métiers. Par extension, il converge avec le GreenOps pour réduire simultanément les coûts et l'empreinte environnementale.
> **Pourquoi c'est important** : Les dépenses cloud non maîtrisées (shadow IT, ressources sous-utilisées, mauvais dimensionnement) représentent en moyenne 30 à 35 % de gaspillage dans les organisations (FinOps Foundation). Les DSI doivent piloter le cloud comme un service à la consommation, avec une visibilité en temps réel sur les coûts et les ressources.
> **Chiffres clés** :
> - 30 à 35 % des dépenses cloud sont gaspillées en moyenne (FinOps Foundation, 2023)
> - Le marché mondial du cloud public dépasse 700 milliards $ en 2024 (Gartner)
> - Le rightsizing peut réduire les factures cloud de 20 à 40 % sans impact fonctionnel (études AWS/Azure)

## Approfondir

### Fonctionnement

**Les 3 phases du cycle FinOps**
1. **Informer** : obtenir une visibilité complète sur les dépenses cloud (tagging des ressources, attribution par équipe/projet, dashboards en temps réel)
2. **Optimiser** : identifier et éliminer les gaspillages (rightsizing, suppression des ressources inutilisées, achat de réservations ou de savings plans)
3. **Opérer** : institutionnaliser les pratiques, définir des processus, des rituels et des KPI pour maintenir l'optimisation dans le temps

**Rightsizing**
Processus d'ajustement de la taille des instances cloud (VM, conteneurs, bases de données) à leur utilisation réelle. Une instance surdimensionnée consomme inutilement des ressources et génère des coûts et une empreinte carbone superflus. Le rightsizing implique d'analyser les métriques d'utilisation (CPU, RAM, réseau) sur plusieurs semaines et de descendre en gamme si le taux d'utilisation est faible (<20-30 %).

**Showback / Chargeback**
- **Showback** : mécanisme de visibilité où chaque équipe/BU voit sa consommation cloud et ses coûts associés, sans refacturation formelle. Objectif : sensibiliser et responsabiliser.
- **Chargeback** : refacturation interne effective des coûts cloud aux équipes ou BU consommatrices. Crée une incitation économique directe à optimiser. Nécessite un système de tagging rigoureux et un référentiel de prix internes.

**Rationalisation applicative**
Démarche consistant à analyser le portefeuille applicatif pour identifier les applications à décommissionner, consolider, migrer ou moderniser. Dimensions : usage réel, coût de maintien, valeur métier, dette technique, compatibilité cloud. Elle réduit le nombre d'applications actives, diminuant les coûts et l'empreinte environnementale.

**Zombie applicatif**
Application ou ressource cloud toujours active et facturée mais qui n'est plus utilisée ou utile : serveurs oubliés après un projet, environnements de test non éteints, licences non résiliées, bases de données orphelines. Les zombies représentent 5 à 15 % des ressources cloud dans les grandes organisations. Les détecter nécessite un inventaire régulier et des règles d'auto-extinction (TTL, auto-shutdown).

**Convergence FinOps et GreenOps**
Le FinOps réduit les coûts en supprimant les ressources inutilisées. Ces mêmes ressources consomment de l'énergie inutilement. Le GreenOps étend cette logique en ajoutant :
- Le choix de régions cloud à faible intensité carbone (carbon-aware)
- La planification des traitements batch en dehors des pics de consommation du réseau électrique
- La mesure de l'empreinte carbone par workload (Cloud Carbon Footprint, outils natifs)

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction significative des coûts cloud (20-40 %) | Nécessite une culture de collaboration Finance-Tech-Métiers |
| Double bénéfice coût et environnement (GreenOps) | Mise en place du tagging souvent complexe dans les grandes organisations |
| Meilleure visibilité et gouvernance du SI cloud | Résistance des équipes tech à la "surveillance" des coûts |
| Accélère la rationalisation applicative | Risque de sous-dimensionnement impactant les performances |
| Responsabilise les équipes sur leur consommation | Nécessite des outils spécialisés et des compétences dédiées |

### Acteurs et solutions du marché
- **FinOps Foundation** : association professionnelle, cadre de référence FinOps, certification FOCP (FinOps Certified Practitioner)
- **Outils natifs cloud** : AWS Cost Explorer, Azure Cost Management, Google Cloud Billing — fonctionnalités de base gratuites
- **Outils tiers** : CloudHealth (VMware), Apptio Cloudability, Spot.io (NetApp), Infracost (open source)
- **Cloud Carbon Footprint** (open source) : croise coûts et empreinte carbone, compatible AWS/Azure/GCP
- **Lyrid / Finout / CAST.AI** : nouvelles plateformes FinOps avec fonctionnalités d'optimisation automatisée

### Cas d'usage concrets
1. **Spotify** : mise en place d'une culture FinOps avec des "cost champions" par squad, réduction de 20 % des dépenses cloud en 18 mois via rightsizing et suppression de ressources inutilisées.
2. **Société Générale** : déploiement d'un chargeback cloud interne pour chaque direction métier, avec dashboards en temps réel. Réduction de 30 % des zombie applicatifs en 1 an.
3. **Engie** : combinaison FinOps + GreenOps, choix des régions Azure à faible intensité carbone pour les workloads non critiques, économies de 25 % sur les coûts et réduction estimée de 15 % des émissions GES cloud.

### Chiffres et tendances
- 82 % des organisations pratiquant le FinOps déclarent réduire leurs coûts cloud (FinOps Foundation, State of FinOps 2024)
- Le FinOps est identifié comme priorité #1 des DSI pour la maîtrise des coûts cloud (Gartner, 2024)
- Moins de 30 % des organisations ont un chargeback cloud mature (FinOps Foundation)
- L'IA générative (LLMOps) crée une nouvelle catégorie de dépenses cloud non maîtrisées, demandant des extensions des pratiques FinOps

## Flashcards
#flashcards/SI_et_environnement/FinOps #flashcards/Cloud_et_Virtualisation/FinOps #flashcards/Optimisation_du_SI/FinOps

Quelles sont les 3 phases du cycle FinOps ? :: Informer (visibilité sur les coûts) – Optimiser (réduire les gaspillages) – Opérer (institutionnaliser les pratiques). Elles impliquent les équipes Finance, Tech et Métiers.

Qu'est-ce que le rightsizing ? :: L'ajustement de la taille des instances cloud (VM, bases de données) à leur utilisation réelle, en réduisant les ressources surdimensionnées. Peut réduire les coûts cloud de 20 à 40 %.

Quelle est la différence entre showback et chargeback ? :: Showback = visibilité des coûts par équipe sans refacturation formelle (sensibilisation). Chargeback = refacturation interne effective des coûts aux équipes consommatrices (incitation économique directe).

Qu'est-ce qu'un zombie applicatif ? :: Une application ou ressource cloud active et facturée mais non utilisée (serveur oublié, env de test non éteint, base de données orpheline). Représentent 5 à 15 % des ressources cloud dans les grandes organisations.

Comment le FinOps converge-t-il avec le GreenOps ? :: En éliminant les ressources inutilisées (réduction coût et conso énergie), en choisissant des régions cloud à faible intensité carbone, et en planifiant les batchs lors des plages à énergie renouvelable.

Quel est le gaspillage cloud moyen estimé par la FinOps Foundation ? :: 30 à 35 % des dépenses cloud sont gaspillées en moyenne dans les organisations.

## Sources
- FinOps Foundation — State of FinOps 2024 : https://data.finops.org
- FinOps Foundation — cadre et définitions : https://www.finops.org/introduction/what-is-finops/
- Cloud Carbon Footprint (open source) : https://www.cloudcarbonfootprint.org
- Gartner — Cloud cost management trends (rapports annuels)
- AWS — Rightsizing recommendations : https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/

## Notions liées
- [[Fiche 9 : Sobriété numérique]]
- [[Fiche 12 : Outils de mesure d'impact environnemental]]
- [[Fiche 13 : Cadre réglementaire environnemental du SI]]
