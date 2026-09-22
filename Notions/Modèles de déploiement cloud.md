---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Modèles de déploiement cloud

![[N — Modèles de déploiement cloud.mp3]]
## En bref
> **Définition** : Les modèles de déploiement cloud désignent la façon dont l'infrastructure cloud est hébergée et partagée : cloud public (mutualisé, géré par un fournisseur tiers), privé (dédié à une organisation), hybride (mix des deux) ou multi-cloud (plusieurs fournisseurs publics).
> **Pourquoi c'est important** : Le choix du modèle de déploiement conditionne la sécurité, la souveraineté des données, les coûts et la flexibilité. La DSI doit arbitrer entre contrôle et agilité, souvent en fonction des exigences réglementaires (RGPD, secteur financier, santé).
> **Chiffres clés** :
> - 87% des entreprises adoptent une stratégie multi-cloud en 2024 (Flexera State of the Cloud Report, 2024)
> - Le cloud hybride représente 44% des dépenses cloud d'entreprise (IDC, 2023)
> - Le marché du cloud privé atteindra 528 milliards de dollars en 2025 (Grand View Research)

## Approfondir

### Fonctionnement

**Cloud public**
Infrastructure mutualisée gérée par un fournisseur tiers (AWS, Azure, GCP). Les ressources sont partagées entre plusieurs clients (multi-tenancy) via une isolation logique. Accès via internet ou liaison dédiée (AWS Direct Connect, Azure ExpressRoute). Modèle pay-as-you-go.

**Cloud privé**
Infrastructure dédiée à une seule organisation, hébergée on-premise ou chez un hébergeur tiers (hosted private cloud). Donne un contrôle total sur la configuration, la sécurité et la localisation des données. Techniquement mis en oeuvre avec VMware vSphere, OpenStack, Nutanix ou Azure Stack.

**Cloud hybride**
Combinaison de cloud public et privé, interconnectés via VPN ou liaison dédiée. Permet de garder les workloads sensibles on-premise et de scaler sur le cloud public (cloud bursting). Nécessite une orchestration cohérente (ex. : Azure Arc, AWS Outposts, Google Anthos).

**Multi-cloud**
Utilisation de plusieurs fournisseurs cloud publics simultanément (ex. : AWS pour le compute, Azure pour la suite M365, GCP pour l'IA). Motivations : éviter le vendor lock-in, optimiser les coûts, résilience géographique.

**Multi-tenancy**
Architecture dans laquelle une même instance d'application ou d'infrastructure sert plusieurs clients avec isolation logique des données. Fondement économique du cloud public : mutualisation des coûts d'infrastructure.

**Scalabilité et élasticité**
- **Scalabilité verticale** (scale-up) : augmenter la puissance d'un noeud (CPU, RAM). Limitée par le matériel.
- **Scalabilité horizontale** (scale-out) : ajouter des noeuds supplémentaires. Base des architectures cloud-native.
- **Élasticité** : capacité à ajuster les ressources automatiquement en fonction de la charge, dans les deux sens (scale-out ET scale-in). Différent de la simple scalabilité qui ne va que dans un sens.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Cloud public : coût réduit, déploiement rapide | Cloud public : moins de contrôle, données hors site |
| Cloud privé : contrôle total, conformité facilitée | Cloud privé : investissement initial élevé (CAPEX) |
| Hybride : flexibilité, cloud bursting | Hybride : complexité de gestion, latence inter-cloud |
| Multi-cloud : résilience, pas de lock-in | Multi-cloud : silos, complexité opérationnelle accrue |
| Élasticité : pas de sur-provisionnement | Gestion de la sécurité cohérente entre clouds difficile |

### Acteurs et solutions du marché

- **Cloud public** : AWS, Microsoft Azure, Google Cloud Platform, Alibaba Cloud, OVHcloud
- **Cloud privé** : VMware vSphere/vSAN, OpenStack (open source), Nutanix, Microsoft Azure Stack Hub, HPE GreenLake
- **Cloud hybride** : AWS Outposts (hardware AWS on-premise), Azure Arc (gestion multi-cloud centralisée), Google Anthos, Red Hat OpenShift
- **Orchestration multi-cloud** : HashiCorp Terraform (IaC), Crossplane, Pulumi, Morpheus
- **Réseaux** : AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect (liaisons dédiées haut débit)

### Cas d'usage concrets

1. **Cloud hybride pour un groupe bancaire** : une banque conserve ses données clients et applicatifs core banking on-premise (contraintes ACPR/BCE), mais déploie ses applications analytiques et marketing sur Azure. L'interconnexion ExpressRoute garantit la performance.

2. **Multi-cloud pour un e-commerçant** : un retailer utilise AWS pour son infrastructure principale et GCP pour ses modèles de machine learning (BigQuery, Vertex AI). Objectif : bénéficier des meilleures solutions de chaque fournisseur sans dépendance unique.

3. **Cloud bursting** : une université héberge son SI de gestion on-premise. Lors des pics d'inscription (rentrée), elle scale automatiquement sur le cloud public AWS pour absorber la charge, puis réintègre les workloads. Facturation uniquement sur la période de pic.

### Chiffres et tendances

- Flexera 2024 : 72% des entreprises ont une stratégie cloud hybride, 87% multi-cloud
- Le cloud public (IaaS+PaaS) dépasse 600 milliards de dollars de dépenses mondiales en 2024 (Gartner)
- Tendance : "cloud repatriation" — retour partiel on-premise pour certains workloads stables à fort volume, pour des raisons économiques (ex. : Dropbox a rapatrié 600 To en 2016)
- Kubernetes est devenu le standard de facto pour l'orchestration de conteneurs en environnement hybride et multi-cloud

## Flashcards
#flashcards/Cloud_et_Virtualisation/Modèles_de_déploiement_cloud #flashcards/Optimisation_du_SI/Modèles_de_déploiement_cloud

Quelle est la différence entre élasticité et scalabilité ? :: La scalabilité est la capacité à monter en charge (scale-out/up). L'élasticité inclut aussi la capacité à réduire les ressources automatiquement quand la charge baisse (scale-in), sans intervention manuelle.

Qu'est-ce que le cloud bursting ? :: Mécanisme hybride permettant de déborder automatiquement sur le cloud public lors de pics de charge, tout en maintenant les workloads habituels on-premise.

Qu'est-ce que la multi-tenancy ? :: Architecture où une même infrastructure ou application sert plusieurs clients avec isolation logique des données. Fondement économique du cloud public.

Citez deux outils d'orchestration cloud hybride. :: Azure Arc (gestion centralisée multi-cloud/on-premise) et AWS Outposts (matériel AWS déployé on-premise). Aussi : Google Anthos, Red Hat OpenShift.

Quelles sont les deux principales motivations d'une stratégie multi-cloud ? :: Éviter le vendor lock-in (dépendance à un fournisseur unique) et optimiser les coûts/fonctionnalités en choisissant le meilleur service de chaque fournisseur.

Quel pourcentage d'entreprises utilisent une stratégie multi-cloud en 2024 ? :: 87% selon le rapport Flexera State of the Cloud 2024.

Qu'est-ce que le cloud repatriation ? :: Tendance consistant à rapatrier des workloads du cloud public vers une infrastructure on-premise ou privée, principalement pour des raisons économiques sur les workloads stables et prévisibles.

## Sources

- Flexera, "State of the Cloud Report 2024"
- IDC, "Cloud Computing Market Forecast", 2023
- Gartner, "Forecast: Public Cloud Services, Worldwide", 2024
- Grand View Research, "Private Cloud Market Size Report", 2023
- VMware, AWS, Azure, Google Cloud — documentations officielles

## Notions liées

- [[Modèles de service cloud]]
- [[Cloud souverain]]
- [[Économie du cloud]]
- [[Vendor lock-in et réversibilité]]
- [[FinOps]]
- [[Infrastructure des datacenters]]
