---
type: notion
thèmes:
  - Transversal
statut: pas vu
dernière_révision: 
---

## En bref

### Définition
La matrice de Kraljic est un outil de segmentation des achats, créé par Peter Kraljic en **1983** (Harvard Business Review), permettant de classer les achats d'une organisation selon deux axes : l'**impact sur le résultat** (profit impact) et la **complexité du marché fournisseur** (supply risk). Elle oriente la stratégie achat pour chaque catégorie.

### Pourquoi c'est important
Tous les achats ne méritent pas la même attention. La matrice de Kraljic permet d'allouer les ressources achat là où elles créent le plus de valeur, de réduire les risques de dépendance fournisseur (ex. : lock-in cloud, fournisseur unique de licences critiques) et de définir des stratégies différenciées par catégorie.

### Chiffres clés
- Publiée pour la première fois en **1983** dans le HBR : *"Purchasing Must Become Supply Management"* — toujours une référence 40 ans après.
- La loi de Pareto s'applique aux achats : **20 % des fournisseurs** représentent **80 % de la valeur achetée**.
- Les dépenses IT représentent en moyenne **4 à 6 % du CA** des grandes entreprises (Gartner, 2024).

---

## Approfondir

### Fonctionnement

La matrice croise deux axes pour créer 4 quadrants :

|  | **Faible complexité marché fournisseur** | **Forte complexité marché fournisseur** |
|---|---|---|
| **Fort impact sur le résultat** | Achats **leviers** | Achats **stratégiques** |
| **Faible impact sur le résultat** | Achats **simples** (non-critiques) | Achats **critiques** (goulots) |

#### Les 4 quadrants en détail

**1. Achats simples (non-critiques)**
- Faible valeur, marché fournisseur abondant.
- Exemples IT : fournitures de bureau, câbles réseau standards, licences antivirales grand public.
- Stratégie : **automatiser et simplifier** (catalogues, commandes automatiques, e-procurement).

**2. Achats leviers**
- Fort impact sur le résultat, mais marché fournisseur avec de nombreuses alternatives.
- Exemples IT : serveurs standard (Dell, HPE, Lenovo interchangeables), licences Microsoft 365 (alternative Google Workspace), connectivité internet.
- Stratégie : **exploiter le pouvoir de négociation**. Mettre les fournisseurs en compétition, consolider les volumes.

**3. Achats critiques (goulots)**
- Faible impact financier mais marché fournisseur complexe ou limité.
- Exemples IT : composants électroniques spécifiques (semiconducteurs), logiciels métier très spécialisés avec un seul éditeur.
- Stratégie : **sécuriser l'approvisionnement**. Développer des fournisseurs alternatifs, établir des contrats MCO, clause d'escrow du code source.

**4. Achats stratégiques**
- Fort impact sur le résultat ET marché fournisseur complexe (peu d'alternatives, forte dépendance).
- Exemples IT : contrats cloud majeurs (AWS, Azure, GCP), ERP (SAP, Oracle), plateforme de cybersécurité, prestataires ESN sur des compétences rares.
- Stratégie : **partenariat long terme**. Construire une relation de confiance, co-innover, contractualiser des SLA solides, préparer une exit strategy.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Simplicité visuelle et opérationnelle | Classification parfois subjective des axes |
| Oriente clairement la stratégie par quadrant | Modèle statique : ne capte pas l'évolution du marché en temps réel |
| Applicable à tous les secteurs dont l'IT | Ne prend pas en compte la qualité ou l'innovation fournisseur |
| Optimise l'allocation des ressources achat | Peut créer une dépendance assumée mal gérée (quadrant stratégique) |
| Aide à identifier les risques de lock-in | Nécessite une connaissance fine des marchés fournisseurs |

### Acteurs / Outils
- **Qui l'utilise** : directeur des achats, category manager, DSI pour les achats IT, DAF.
- **Outils** : tableur Excel/Google Sheets pour la cartographie, outils de spend analysis (SAP Ariba, Ivalua, Coupa), Power BI pour la visualisation.
- **Compléments** : scorecard fournisseurs, audit fournisseur, segmentation de la base fournisseurs.

### Cas d'usage concrets en IT

**Segmentation d'un portefeuille achat IT type :**

| Catégorie achat | Quadrant | Stratégie appliquée |
|---|---|---|
| Licences SaaS CRM (Salesforce) | Stratégique | Négociation pluriannuelle, audit d'usage, étude d'alternatives (HubSpot) |
| Hébergement cloud (AWS) | Stratégique | Reserved Instances, négociation Enterprise Discount Program, stratégie multi-cloud |
| PC portables standards | Levier | Appel d'offres annuel, comparaison Dell/Lenovo/HP, volumes consolidés |
| Câblage réseau | Simple | Catalogue en ligne, commande automatique |
| Logiciel métier niche (1 éditeur) | Critique | Contrat MCO long terme, clause d'escrow du code source |
| Prestataires ESN (compétences IA/ML rares) | Stratégique | Partenariat cadre, plan de formation interne |

**Cas : gestion du lock-in cloud**
Une entreprise dont 90 % de l'infrastructure est sur un seul provider cloud (quadrant Stratégique) doit anticiper : négociation d'un Enterprise Discount Program, architecture portable (Kubernetes, Terraform), étude de multi-cloud pour les workloads non critiques.

### Chiffres et tendances
- Gartner (2024) : les dépenses mondiales en services cloud atteignent **679 milliards $**.
- Le phénomène de **vendor lock-in** cloud est cité par **72 %** des DSI comme un risque majeur (IDC, 2023).
- La réglementation **DORA** (Digital Operational Resilience Act, en vigueur 2025) impose aux institutions financières de cartographier leurs fournisseurs IT critiques — proche de la logique Kraljic.

---

## Flashcards
#flashcards/Transversal/Matrice_de_Kraljic

Quels sont les 4 quadrants de la matrice de Kraljic ? :: **Simples** (faible impact, marché facile), **Leviers** (fort impact, marché facile), **Critiques** (faible impact, marché complexe), **Stratégiques** (fort impact, marché complexe).

Quelle stratégie adopter pour les achats stratégiques en IT ? :: Construire un **partenariat long terme** avec le fournisseur, négocier des SLA solides, co-innover, mais aussi préparer une **exit strategy** (réversibilité, multi-sourcing) pour limiter le lock-in.

Quelle stratégie adopter pour les achats leviers ? :: Exploiter son **pouvoir de négociation** : mettre les fournisseurs en compétition, consolider les volumes pour obtenir des remises, standardiser les cahiers des charges.

Citez un exemple d'achat critique en IT. :: Un logiciel métier très spécialisé avec un seul éditeur disponible (ex. : logiciel SCADA industriel, ERP sectoriel niche). Faible montant mais risque de rupture élevé. Stratégie : contrat MCO long terme + clause d'escrow du code source.

Quels sont les deux axes de la matrice de Kraljic ? :: L'**impact sur le résultat** (valeur et volume des achats) et la **complexité du marché fournisseur** (nombre d'alternatives, risque de rupture, concentration du marché).

Qui est Peter Kraljic et quand a-t-il publié sa matrice ? :: Peter Kraljic est un consultant McKinsey qui a publié sa matrice en **1983** dans le Harvard Business Review, dans l'article *"Purchasing Must Become Supply Management"*.

En quoi DORA est-il lié à la logique de Kraljic ? :: Le règlement **DORA** (2025) impose aux institutions financières de l'UE de cartographier et de gérer leurs fournisseurs IT critiques (tiers ICT), ce qui correspond exactement au quadrant **stratégique et critique** de la matrice de Kraljic.

---

## Sources
- Kraljic, P. (1983) — *"Purchasing Must Become Supply Management"*, Harvard Business Review, sept.-oct. 1983.
- Gartner — *Forecast: Public Cloud Services, Worldwide, 2024*
- IDC Survey — *Cloud Strategy and Vendor Lock-in* (2023)
- Règlement UE 2022/2554 — DORA (Digital Operational Resilience Act)

---

## Notions liées
- [[VAN - TRI - Payback]]
- [[SWOT - PESTEL]]
- [[AMDEC]]
- [[Méthode MoSCoW]]
