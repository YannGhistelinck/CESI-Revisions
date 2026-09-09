---
type: notion
thèmes:
  - SI et environnement
statut: pas vu
dernière_révision: 
---

# Outils de mesure d'impact environnemental

## En bref
> **Définition** : Les outils de mesure d'impact environnemental du numérique permettent de quantifier la consommation de ressources (énergie, réseau, CPU, RAM) et les émissions de GES associées à un service numérique (site web, application, infrastructure). Ils constituent le prérequis indispensable à toute démarche d'écoconception ou de sobriété numérique : on ne peut optimiser que ce qu'on mesure.
> **Pourquoi c'est important** : Sans mesure, les démarches NR restent déclaratives et non vérifiables. Les DSI doivent outiller leurs équipes pour intégrer la mesure d'impact dans les cycles de développement et de pilotage du SI.
> **Chiffres clés** :
> - Un site web moyen génère 0,5 g CO₂ eq par page vue, contre plus de 5 g pour les sites les moins bien optimisés (données WebsiteCarbon.com)
> - EcoIndex classe les sites de A (meilleur) à G (pire) sur la base du poids de la page, du nombre de requêtes HTTP et de la complexité du DOM
> - Seules 14 % des entreprises françaises mesurent l'empreinte environnementale de leur SI (Cigref/Wavestone 2023)

## Approfondir

### Fonctionnement

**EcoIndex**
Outil open source créé par le Collectif Numérique Responsable (GreenIT.fr). Mesure l'impact d'une page web via 3 indicateurs : poids de la page (Ko), nombre de requêtes HTTP, complexité du DOM (nombre d'éléments). Produit un score de A à G, une estimation en g CO₂ eq et en litres d'eau consommés. Disponible en ligne (ecoindex.fr), en extension navigateur et en API.

**GreenIT-Analysis**
Extension navigateur (Chrome/Firefox) développée par la communauté GreenIT.fr. Analyse une page en temps réel et fournit : EcoIndex, consommation d'eau, émissions CO₂, taille de la page, nombre de requêtes, complexité DOM. Permet des audits rapides sans instrumentation. Utilisé en combinaison avec EcoIndex pour des analyses plus fines.

**Greenspector**
Solution commerciale spécialisée dans la mesure de la consommation énergétique des applications mobiles (Android, iOS) et web sur terminaux réels. Mesure la batterie, le CPU, la RAM, le réseau directement sur l'appareil. Permet de comparer des versions d'une app ou de benchmarker face à des concurrents. Utilisé pour valider les efforts d'écoconception mobile.

**Website Carbon Calculator**
Outil en ligne (websitecarbon.com) qui estime les émissions CO₂ d'une page web en combinant le poids de la page, le trafic estimé et le mix énergétique de l'hébergement. Simple, rapide, pédagogique. Moins précis qu'EcoIndex ou Greenspector mais très utile pour sensibiliser les équipes et les clients.

**Monitoring énergétique (infrastructure)**
Outils de monitoring de la consommation électrique des serveurs et datacenters :
- **DCIM (Data Center Infrastructure Management)** : Nlyte, Vertiv, Schneider EcoStruxure — pilotent le PUE, la température, la consommation par rack
- **Scaphandre** (open source, Hubblo) : agent de mesure de la consommation CPU par processus sur serveurs Linux, exportable vers Prometheus/Grafana
- **Kepler** (CNCF) : mesure la consommation énergétique des workloads Kubernetes
- **PowerAPI** (Inria/Spirals) : bibliothèque open source pour mesurer la consommation logicielle
- **Cloud natives** : AWS Customer Carbon Footprint Tool, Azure Emissions Insights, GCP Carbon Footprint

**Outils de mesure Scope 1/2/3 du SI**
- **Boavizta / Cloud-scanner** : mesure l'empreinte des instances cloud (fabrication + usage) selon la méthodologie Boavizta
- **Datavizta** : base de données open source des impacts environnementaux des équipements numériques (facteurs d'émission)

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Objectivent les démarches NR et permettent de prioriser | Méthodologies hétérogènes, résultats difficilement comparables entre outils |
| Permettent de suivre l'évolution dans le temps (KPI) | Complexité d'intégration dans les pipelines CI/CD |
| Sensibilisent les équipes par des métriques concrètes | Les outils en ligne ne mesurent pas l'usage réel (trafic, terminaux réels) |
| EcoIndex et GreenIT-Analysis sont gratuits et accessibles | Manque de consensus sur les facteurs d'émission à utiliser |
| Intégration possible dans des tableaux de bord (Grafana, Datadog) | Les outils mobiles (Greenspector) restent coûteux |

### Acteurs et solutions du marché
| Outil | Type | Cible | Coût |
|-------|------|--------|------|
| EcoIndex | Open source / en ligne | Pages web | Gratuit |
| GreenIT-Analysis | Extension navigateur | Pages web | Gratuit |
| Greenspector | Solution commerciale | Mobile + Web | Payant |
| Website Carbon Calculator | En ligne | Pages web | Gratuit |
| Scaphandre | Open source (agent) | Serveurs Linux | Gratuit |
| Kepler | Open source (CNCF) | Kubernetes | Gratuit |
| Cloud Carbon Footprint | Open source | Cloud multi-cloud | Gratuit |
| AWS/Azure/GCP Carbon Tools | Native cloud | Cloud | Inclus |

### Cas d'usage concrets
1. **SNCF** : intégration de GreenIT-Analysis dans les audits qualité des applications web internes, avec un seuil minimal d'EcoIndex C pour mise en production.
2. **Orange** : utilisation de Greenspector pour mesurer et réduire la consommation des applications mobiles Orange (réduction de 30 % de la consommation batterie sur certaines apps).
3. **OVHcloud** : publication de métriques d'empreinte carbone par instance (PUE, WUE, émissions) accessibles via API pour les clients.

### Chiffres et tendances
- Le DOM moyen d'une page web est passé de 700 à plus de 1 500 éléments entre 2015 et 2024 (HTTP Archive)
- Le poids moyen d'une page web desktop dépasse 2,5 Mo en 2024 (HTTP Archive)
- L'intégration de mesures d'impact dans les pipelines CI/CD reste marginale (<5 % des projets) mais progresse avec les pratiques GreenOps

## Flashcards
#flashcards/SI_et_environnement/Outils_de_mesure_d_impact_environnemental

Quels sont les 3 indicateurs utilisés par EcoIndex pour scorer une page web ? :: Le poids de la page (Ko), le nombre de requêtes HTTP et la complexité du DOM (nombre d'éléments HTML). Ces 3 critères produisent un score de A (meilleur) à G.

Quelle est la différence entre EcoIndex et GreenIT-Analysis ? :: EcoIndex est un outil en ligne et une API pour scorer des pages. GreenIT-Analysis est une extension navigateur qui fournit l'EcoIndex en temps réel lors de la navigation, avec des détails supplémentaires sur la page analysée.

Pourquoi Greenspector est-il différent des autres outils de mesure web ? :: Il mesure la consommation réelle sur terminaux mobiles physiques (batterie, CPU, RAM, réseau), pas seulement le poids de la page. Il est particulièrement adapté aux applications mobiles.

Qu'est-ce que Scaphandre ? :: Un agent open source (Hubblo) qui mesure la consommation électrique par processus sur des serveurs Linux, exportable vers Prometheus et Grafana pour un monitoring continu.

Quels sont les outils natifs des hyperscalers pour mesurer l'empreinte carbone cloud ? :: AWS Customer Carbon Footprint Tool, Azure Emissions Insights, Google Cloud Carbon Footprint. Ils agrègent les émissions Scope 1, 2 et 3 par service et région.

Qu'est-ce que le PUE et qui le mesure ? :: Power Usage Effectiveness = consommation totale du datacenter / consommation des équipements IT. Un PUE de 1 est idéal. Mesuré par les DCIM (Data Center Infrastructure Management). Les meilleurs datacenters cloud atteignent 1,1-1,2.

## Sources
- EcoIndex : https://www.ecoindex.fr
- GreenIT-Analysis (GitHub) : https://github.com/cnumr/GreenIT-Analysis
- Greenspector : https://greenspector.com
- Website Carbon Calculator : https://www.websitecarbon.com
- Scaphandre (GitHub) : https://github.com/hubblo-org/scaphandre
- Cloud Carbon Footprint : https://www.cloudcarbonfootprint.org
- Boavizta (outils open source) : https://boavizta.org
- HTTP Archive (stats web) : https://httparchive.org

## Notions liées
- [[Fiche 9 : Sobriété numérique]]
- [[Fiche 10 : Écoconception logicielle]]
- [[Fiche 13 : Cadre réglementaire environnemental du SI]]
- [[Fiche 15 : FinOps]]
- [[Fiche 16 : Acteurs du numérique responsable]]
