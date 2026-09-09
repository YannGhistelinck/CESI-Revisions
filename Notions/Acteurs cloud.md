---
type: notion
thèmes:
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Acteurs cloud

## En bref
> **Définition** : Le marché du cloud computing est structuré autour de fournisseurs d'infrastructure (IaaS), de plateformes (PaaS) et de logiciels (SaaS), ainsi que d'acteurs spécialisés en sécurité cloud. On distingue les hyperscalers américains (AWS, Azure, GCP), les acteurs européens souverains (OVHcloud, Scaleway, 3DS Outscale) et les spécialistes de la sécurité cloud (Wiz, Palo Alto Prisma Cloud).
> **Pourquoi c'est important** : Pour une DSI, le choix d'un fournisseur cloud engage la stratégie de l'entreprise sur plusieurs années : coûts, souveraineté des données, conformité (RGPD, HDS, SecNumCloud), résilience et capacités d'innovation. La concentration du marché sur 3 hyperscalers crée des risques de dépendance que les acteurs européens cherchent à contrebalancer.
> **Chiffres clés** :
> - AWS, Azure et GCP représentent 67 % du marché mondial du cloud en 2024 (Synergy Research Group).
> - Le marché mondial du cloud a atteint 680 Md$ en 2024 (Gartner).
> - OVHcloud est le 1er opérateur cloud européen avec 43 datacenters et 1,6 M de serveurs dans 12 pays (OVHcloud, 2024).

## Approfondir

### Fonctionnement

**AWS (Amazon Web Services)**
- Pionnier du cloud public (lancé en 2006), leader mondial incontesté.
- Part de marché : ~31 % du marché IaaS/PaaS mondial (Synergy, 2024).
- Offre : 200+ services (EC2 pour les VM, S3 pour le stockage objet, RDS, Lambda, EKS, SageMaker, etc.).
- Certifications : ISO 27001/17/18, SOC 2 Type II, PCI-DSS, HDS (régions Paris), FedRAMP.
- Points forts : profondeur de l'offre, réseau mondial (32 régions, 102 zones de disponibilité), innovation rapide.
- Limite souveraineté : soumis au CLOUD Act américain — les autorités US peuvent exiger l'accès aux données même hébergées en Europe.

**Microsoft Azure**
- 2e acteur mondial, intégration profonde avec l'écosystème Microsoft (M365, Active Directory, Visual Studio).
- Part de marché : ~25 % (Synergy, 2024).
- Offre : VM (Azure VMs), stockage (Blob), bases de données, IA (Azure OpenAI Service), K8s (AKS), analytics (Synapse).
- Certifications : ISO 27001/17/18, SOC 2 Type II, HDS (France Central), FedRAMP.
- Points forts : hybride (Azure Arc, Azure Stack), identité (Entra ID), IA/ML avec OpenAI.
- Limite souveraineté : même exposition CLOUD Act qu'AWS. Initiative **Microsoft Cloud for Sovereignty** en réponse aux exigences européennes.

**GCP (Google Cloud Platform)**
- 3e acteur mondial, fort sur les données, le ML et l'open source.
- Part de marché : ~11 % (Synergy, 2024).
- Offre : GKE (premier K8s managé), BigQuery (analytics), Vertex AI, Spanner (BDD distribuée).
- Certifications : ISO 27001/17/18, SOC 2 Type II, HDS.
- Points forts : infrastructure réseau propriétaire (fibre sous-marine), open source (K8s, TensorFlow, Istio sont nés chez Google), data analytics.
- Limite souveraineté : CLOUD Act, même si Google a lancé **Sovereign Cloud** avec des partenaires locaux.

**OVHcloud**
- 1er opérateur cloud européen, fondé en 1999 à Roubaix (France).
- Acteur souverain : sièges social, juridique et technique en France. Pas soumis au CLOUD Act.
- Offre : IaaS (serveurs dédiés, VPS, Public Cloud), Object Storage (S3-compatible), K8s managé, databases.
- Certifications : ISO 27001, HDS, **SecNumCloud qualifié** (offre cloud interne, 2022), SOC 2.
- Points forts : souveraineté, coût-compétitivité (notamment bare metal), engagement open source.
- Limite : profondeur de l'offre et innovation plus limitées que les hyperscalers.

**Scaleway**
- Filiale du groupe Iliad (Free), cloud français souverain fondé en 1999.
- Offre : VMs, Object Storage (S3-compatible), K8s managé (Kapsule), bases de données managées, fonctions serverless.
- Certifications : ISO 27001, HDS.
- Points forts : positionnement développeur (API-first, CLI), tarification transparente, engagement environnemental (énergie verte, datacenter innovant à Paris).
- Cible : startups, scale-ups, PME tech européennes.

**3DS Outscale (Dassault Systèmes)**
- Cloud souverain français, filiale de Dassault Systèmes.
- Offre orientée entreprises et secteur public : IaaS, PaaS, stockage.
- Certifications : ISO 27001, **SecNumCloud qualifié**, HDS.
- Points forts : un des rares acteurs avec la double qualification SecNumCloud + HDS, très orienté secteur public et OIV (Opérateurs d'Importance Vitale).
- Membre fondateur de Gaia-X.

**Wiz**
- Startup américaine de sécurité cloud fondée en 2020, valorisée 12 Md$ en 2024.
- Spécialité : **CNAPP (Cloud-Native Application Protection Platform)**.
- Fonctionnement : scan agentless (sans agent) du cloud multi, analyse les risques en corrélant misconfigurations, vulnérabilités, permissions excessives (CIEM) et exposition réseau.
- Points forts : déploiement en 15 minutes, visualisation du "Wiz Security Graph" (cartographie des chemins d'attaque), couverture AWS/Azure/GCP/OCI/K8s.
- Clients : 40 % des entreprises du Fortune 100 (2024).

**Palo Alto Prisma Cloud**
- Solution CNAPP de Palo Alto Networks, l'un des leaders historiques de la cybersécurité.
- Offre : CSPM (Cloud Security Posture Management), CWPP (Cloud Workload Protection), CIEM (Cloud Infrastructure Entitlement Management), IaC Security, API Security.
- Points forts : couverture très large (conteneurs, serverless, VMs, IaC), intégration avec les outils DevSecOps (pipeline CI/CD), présence mondiale et support enterprise.
- Référence dans les grandes entreprises et banques pour la sécurisation multi-cloud.

### Avantages / Inconvénients
| Avantages hyperscalers (AWS/Azure/GCP) | Inconvénients |
|----------------------------------------|---------------|
| Profondeur et diversité de l'offre | Soumis au CLOUD Act américain |
| Innovation rapide (IA, serverless, IoT) | Risque de vendor lock-in |
| Réseau mondial ultra-résilient | Coûts de sortie (egress fees) élevés |
| Certifications HDS disponibles | Faible transparence sur la sous-traitance |

| Avantages acteurs souverains européens | Inconvénients |
|---------------------------------------|---------------|
| Souveraineté juridique (droit français/européen) | Offre plus limitée en services managés |
| SecNumCloud qualifié (OVH, Outscale) | Moins d'innovation en IA/ML |
| Conformité RGPD native | Réseau et zones de disponibilité moins étendus |
| Engagement open source et environnemental | Moins de certifications internationales |

### Acteurs et solutions du marché
| Acteur | Type | Part de marché / Position |
|--------|------|--------------------------|
| AWS | Hyperscaler américain | ~31 % mondial |
| Microsoft Azure | Hyperscaler américain | ~25 % mondial |
| Google Cloud (GCP) | Hyperscaler américain | ~11 % mondial |
| Alibaba Cloud | Hyperscaler chinois | ~4 % mondial, dominant en Asie |
| OVHcloud | Souverain européen | 1er acteur cloud européen |
| Scaleway | Souverain français | Leader PME/Dev en France |
| 3DS Outscale | Souverain français | Spécialiste secteur public/OIV |
| Wiz | Sécurité CNAPP | Licorne, 40% Fortune 100 |
| Palo Alto Prisma Cloud | Sécurité CNAPP | Leader enterprise CNAPP |

### Cas d'usage concrets
1. **Secteur bancaire (BNP Paribas)** : stratégie multi-cloud AWS + Azure pour les workloads non-sensibles, OVHcloud / solution souveraine pour les données réglementées. Usage de Prisma Cloud pour la conformité centralisée multi-cloud.
2. **Startup SaaS** : Scaleway pour le déploiement initial (coût, API-first, K8s managé), puis migration partielle vers AWS au passage à l'échelle mondiale, Wiz pour l'audit de posture de sécurité cloud.
3. **Ministère de la Santé** : OVHcloud ou Outscale (SecNumCloud + HDS) pour les données de santé, avec vérification de conformité CIS Benchmarks via outils CSPM.

### Chiffres et tendances
- La stratégie multi-cloud est adoptée par 87 % des entreprises (Flexera State of the Cloud, 2024).
- Les dépenses cloud dans les entreprises françaises ont augmenté de 22 % en 2023 (IDC France).
- Wiz a atteint 350 M$ d'ARR en moins de 4 ans — la croissance la plus rapide de l'histoire du logiciel d'entreprise.
- L'IA générative devient le principal moteur de croissance cloud : AWS, Azure et GCP ont chacun lancé des offres d'IA générative managée en 2023-2024 (Amazon Bedrock, Azure OpenAI, Vertex AI).
- Le marché CNAPP (Wiz, Prisma Cloud, Orca Security) devrait atteindre 9 Md$ en 2027 (IDC).

## Flashcards
#flashcards
- Quels sont les 3 hyperscalers cloud dominants et leurs parts de marché approximatives en 2024 ? :: AWS (~31 %), Microsoft Azure (~25 %), Google Cloud (~11 %) — ensemble 67 % du marché mondial (Synergy Research).
- Qu'est-ce que le CLOUD Act et pourquoi impacte-t-il les choix cloud européens ? :: Le CLOUD Act (2018) est une loi américaine permettant aux autorités US d'exiger l'accès aux données hébergées par des entreprises américaines, même sur des serveurs en Europe — ce qui explique la préférence pour des acteurs souverains européens pour les données sensibles.
- Quels acteurs cloud français disposent de la qualification SecNumCloud ? :: OVHcloud et 3DS Outscale (filiale de Dassault Systèmes) sont les seuls à disposer d'offres cloud qualifiées SecNumCloud en 2024.
- Qu'est-ce qu'une CNAPP et quels en sont les principaux acteurs ? :: Cloud-Native Application Protection Platform : solution de sécurité cloud intégrant CSPM, CWPP et CIEM. Principaux acteurs : Wiz, Palo Alto Prisma Cloud, Orca Security, Lacework.
- Qu'est-ce que le CSPM ? :: Cloud Security Posture Management : outil qui analyse en continu la configuration des environnements cloud pour détecter les écarts par rapport aux référentiels de sécurité (CIS Benchmarks, bonnes pratiques CSP).
- Quelle est la différence entre OVHcloud et Scaleway ? :: OVHcloud est le 1er opérateur cloud européen, fort sur le bare metal et les grandes entreprises, avec SecNumCloud. Scaleway (Iliad/Free) est plus orienté développeurs et startups, API-first, avec un engagement environnemental fort.
- Qu'est-ce que Gaia-X ? :: Une initiative européenne (350+ membres) visant à créer une infrastructure de données et cloud souveraine, interopérable et conforme aux valeurs européennes — 3DS Outscale en est membre fondateur.

## Sources
- Synergy Research Group, Cloud Market Share Q4 2024
- Flexera State of the Cloud Report 2024 : https://www.flexera.com/blog/cloud/cloud-computing-trends-flexera-2024-state-of-the-cloud-report/
- OVHcloud : https://www.ovhcloud.com/fr/
- Scaleway : https://www.scaleway.com/fr/
- 3DS Outscale : https://www.outscale.com/
- Wiz : https://www.wiz.io/
- Palo Alto Prisma Cloud : https://www.paloaltonetworks.fr/prisma/cloud
- Gartner, "Forecast: Public Cloud Services, Worldwide, 2024"

## Notions liées
- [[Certifications et normes cloud]]
- [[Cloud Native et 12-Factor App]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[FinOps]]
- [[Data Act]]
- [[Zero Trust]]
- [[Infrastructure des datacenters]]
