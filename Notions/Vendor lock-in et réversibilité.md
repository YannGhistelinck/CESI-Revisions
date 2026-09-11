---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Vendor lock-in et réversibilité

## En bref
> **Définition** : Le vendor lock-in (dépendance fournisseur) désigne la situation dans laquelle une organisation ne peut pas changer de prestataire cloud sans coûts excessifs ou complexité technique majeure, en raison de formats propriétaires, de services exclusifs ou d'egress fees prohibitifs. La réversibilité est la capacité à quitter un fournisseur dans des conditions acceptables.
> **Pourquoi c'est important** : Le lock-in réduit le pouvoir de négociation de la DSI, expose l'organisation aux hausses de tarifs unilatérales et peut compromettre la continuité de service en cas de défaillance du fournisseur. La réversibilité est désormais une exigence réglementaire en Europe (Data Act, 2023).
> **Chiffres clés** :
> - 59% des entreprises identifient le vendor lock-in comme leur principale préoccupation cloud (Flexera, 2024)
> - Le coût moyen d'une migration cloud-to-cloud est estimé entre 15 et 35% du budget annuel IT concerné (Gartner)
> - Le Data Act européen impose la réversibilité gratuite d'ici 2027, avec suppression progressive des egress fees

## Approfondir

### Fonctionnement

**Mécanismes du vendor lock-in**

1. **Lock-in technique** : utilisation de services propriétaires sans équivalent standard (ex. : AWS DynamoDB, Azure Cosmos DB, Google BigQuery). La migration impose une réécriture applicative.

2. **Lock-in des données** : volumes massifs de données stockées dans le cloud du fournisseur. Les egress fees rendent la sortie financièrement dissuasive.

3. **Lock-in contractuel** : engagements pluriannuels (Reserved Instances, contrats EDP — Enterprise Discount Program) avec pénalités de sortie ou remises conditionnelles à la continuité.

4. **Lock-in des compétences** : les équipes sont formées sur les outils propriétaires du fournisseur (AWS certifications, Azure expertise). Requalification coûteuse.

5. **Lock-in des intégrations** : APIs propriétaires, connecteurs natifs entre services du même fournisseur créent une dépendance par l'écosystème.

**Réversibilité cloud**
Capacité d'une organisation à migrer ses workloads et données vers un autre fournisseur ou vers du on-premise. Elle implique :
- La portabilité des données (formats ouverts, export possible)
- La portabilité applicative (conteneurs, IaC standard)
- Des coûts de sortie acceptables (egress fees)
- Un délai de migration raisonnable

**Exit plan**
Document stratégique définissant, pour chaque service cloud critique, les conditions et la procédure de migration vers un fournisseur alternatif ou une solution on-premise. Inclut : identification des dépendances, estimation des coûts et délais de migration, solutions de remplacement identifiées. Bonne pratique recommandée par l'ANSSI et l'ENISA.

**Portabilité et standards ouverts**
Outils et standards permettant de réduire le lock-in :
- **Conteneurs** : Docker + Kubernetes (CNCF) — portable entre tous les clouds
- **IaC** : Terraform (HashiCorp) — abstraction multi-cloud
- **API standards** : OpenAPI, S3-compatible storage (MinIO, Ceph)
- **Formats ouverts** : Parquet, ORC (données), OVF/OVA (virtualisation)
- **Bases de données open source** : PostgreSQL, MySQL vs RDS Aurora propriétaire

**Data Act européen (2023)**
Règlement européen entré en vigueur en 2024. Obligations pour les fournisseurs cloud :
- Réversibilité technique et commerciale effective
- Suppression progressive des egress fees (horizon 2027)
- Interopérabilité entre services cloud
- Contrats clairs sur la portabilité des données

### Avantages / Inconvénients

| Avantages du lock-in (fournisseur) | Inconvénients pour le client |
|-----------------------------------|------------------------------|
| Services fortement intégrés et optimisés | Perte de pouvoir de négociation |
| Productivité développeur élevée | Dépendance aux hausses tarifaires |
| Écosystème riche et cohérent | Coût de migration très élevé |
| SLA garantis nativement | Risque de continuité si le fournisseur change de stratégie |

| Avantages de la réversibilité | Coûts de la réversibilité |
|-------------------------------|--------------------------|
| Pouvoir de négociation préservé | Complexité technique (multi-cloud) |
| Résilience accrue | Perte des optimisations propriétaires |
| Conformité réglementaire (Data Act) | Overhead d'abstraction (Terraform, K8s) |
| Adaptabilité stratégique | Compétences multiples à maintenir |

### Acteurs et solutions du marché

- **Orchestration portable** : Kubernetes (CNCF), OpenShift (Red Hat), Rancher (SUSE)
- **IaC multi-cloud** : Terraform (HashiCorp/IBM), Pulumi, Crossplane
- **Stockage compatible S3** : MinIO (open source), Ceph, Scality
- **Bases de données portables** : PostgreSQL, MySQL, MongoDB vs services managés propriétaires
- **Brokers multi-cloud** : Morpheus Data, CloudBolt
- **Solutions de migration** : AWS Migration Hub, Azure Migrate, Carbonite Migrate

### Cas d'usage concrets

1. **Stratégie anti-lock-in d'un opérateur télécom** : un opérateur déploie ses applications sur Kubernetes avec Terraform. Toute la configuration est décrite en IaC standard. L'application peut être redéployée sur GCP en 48h si Azure augmente ses tarifs. Exercice de bascule réalisé annuellement.

2. **Négociation renforcée par l'exit plan** : un groupe retail présente son exit plan documenté lors d'une renégociation de contrat AWS. La preuve que la migration est techniquement réalisable en 3 mois lui permet d'obtenir 22% de remise supplémentaire sur son EDP.

3. **Conformité Data Act** : une DSI de groupe bancaire documente la réversibilité de chaque service cloud en anticipation du Data Act. Les services identifiés comme fortement lock-in (propriétaires, sans alternative) font l'objet d'un plan de remplacement progressif par des équivalents open source.

### Chiffres et tendances

- AWS S3 est devenu le standard de facto du stockage objet : des dizaines de solutions open source (MinIO, Ceph) implémentent l'API S3 pour garantir la portabilité
- 73% des DSI déclarent vouloir réduire leur dépendance à un fournisseur cloud unique (IDC, 2023)
- Le Data Act (UE 2023/2854) est applicable depuis septembre 2025 pour les obligations de réversibilité
- Tendance : les "super-cloud" (Databricks, Snowflake) proposent des couches d'abstraction multi-cloud natives
- HashiCorp Terraform reste l'outil IaC multi-cloud le plus utilisé malgré le changement de licence (BSL) en 2023, qui a généré OpenTofu (fork open source CNCF)

## Flashcards
#flashcards

Quels sont les 5 mécanismes principaux du vendor lock-in cloud ? :: 1) Lock-in technique (services propriétaires), 2) Lock-in des données (egress fees), 3) Lock-in contractuel (RI, EDP), 4) Lock-in des compétences (certifications propriétaires), 5) Lock-in des intégrations (APIs propriétaires).

Qu'est-ce qu'un exit plan cloud ? :: Document stratégique définissant pour chaque service cloud critique les conditions, coûts, délais et alternatives pour migrer vers un autre fournisseur. Bonne pratique recommandée par l'ANSSI.

Quel règlement européen impose la réversibilité cloud et depuis quand ? :: Le Data Act (UE 2023/2854), applicable depuis septembre 2025. Il impose la réversibilité technique et commerciale, la suppression progressive des egress fees (horizon 2027) et l'interopérabilité.

Citez 3 outils ou standards permettant de réduire le vendor lock-in. :: Kubernetes (orchestration portable), Terraform/OpenTofu (IaC multi-cloud), MinIO/Ceph (stockage compatible S3), PostgreSQL (base de données portable).

Pourquoi les egress fees sont-ils un mécanisme de lock-in ? :: Ils rendent financièrement dissuasive la sortie des données du cloud. Plus le volume de données est important, plus le coût de migration est élevé, ce qui décourage le changement de fournisseur.

Qu'est-ce qu'OpenTofu et pourquoi a-t-il émergé ? :: Fork open source de Terraform, créé par la CNCF en 2023 après qu'HashiCorp a changé la licence de Terraform de MPL (open source) vers BSL (plus restrictive). Permet de continuer à utiliser l'outil sans dépendance commerciale à HashiCorp.

Pourquoi Kubernetes réduit-il le vendor lock-in ? :: Kubernetes est un standard open source (CNCF) qui fonctionne de manière identique sur tous les clouds (AKS, EKS, GKE) et on-premise. Une application conteneurisée peut migrer entre fournisseurs sans réécriture.

## Sources

- Flexera, "State of the Cloud Report 2024"
- Règlement (UE) 2023/2854, "Data Act", Journal officiel de l'UE
- ENISA, "Cloud Computing: Benefits, Risks and Recommendations for Information Security", mis à jour 2023
- ANSSI, guide "Sécurité et résilience des services cloud", 2022
- Gartner, "Managing Cloud Migration Costs and Risks", 2023

## Notions liées

- [[Économie du cloud]]
- [[Modèles de déploiement cloud]]
- [[Modèles de service cloud]]
- [[Cloud souverain]]
- [[CLOUD Act et transferts de données]]
- [[FinOps]]
