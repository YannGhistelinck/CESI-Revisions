---
type: notion
thèmes:
  - Management et stratégie
  - Transversal
statut: pas vu
dernière_révision: 
catégorie: framework
---

# Matrice d'Ansoff

![[N — Matrice d'Ansoff.mp3]]
## En bref
> **Définition** : La matrice d'Ansoff (ou matrice produit-marché) est un outil de stratégie créé par Igor Ansoff en 1957. Elle croise deux axes — produits (existants/nouveaux) et marchés (existants/nouveaux) — pour identifier 4 stratégies de croissance : pénétration de marché, développement de marché, développement de produit et diversification. C'est l'un des frameworks stratégiques les plus utilisés pour structurer les décisions de croissance.
> **Pourquoi c'est important** : En tant que manager IT/DSI, les décisions de croissance impactent directement le SI : un nouveau marché nécessite une internationalisation du SI, un nouveau produit requiert de nouvelles architectures, une diversification impose une transformation digitale. La matrice d'Ansoff permet de structurer l'analyse des enjeux SI associés à chaque stratégie de croissance.
> **Chiffres clés** :
> - 73 % des entreprises du CAC 40 utilisent la matrice d'Ansoff dans leur planification stratégique (McKinsey, 2022).
> - La diversification est la stratégie la plus risquée : taux d'échec de 50-70 % (Harvard Business Review).
> - La pénétration de marché représente 60 % des stratégies de croissance des PME (Bpifrance, 2023).

## Approfondir

### Fonctionnement

**La matrice 2×2**

|  | **Marché existant** | **Nouveau marché** |
|---|---|---|
| **Produit existant** | **Pénétration de marché** | **Développement de marché** |
| **Nouveau produit** | **Développement de produit** | **Diversification** |

---

#### 1. Pénétration de marché (risque faible)
Vendre plus du même produit sur le même marché.
- **Leviers** : augmentation de la part de marché, fidélisation, hausse de fréquence d'achat, réduction des prix.
- **Impact SI** : optimisation du CRM, analytics marketing, automatisation commerciale.
- **Exemple** : un éditeur SaaS français qui augmente sa part de marché en France via des offres freemium et du marketing digital.

#### 2. Développement de marché (risque modéré)
Vendre le même produit sur de nouveaux marchés (géographiques, segments, canaux).
- **Leviers** : internationalisation, nouveaux segments clients, nouveaux canaux de distribution.
- **Impact SI** : internationalisation du SI (multi-langues, multi-devises, conformité locale — RGPD, lois locales), infrastructure globale (CDN, cloud multi-régions).
- **Exemple** : un éditeur ERP français qui s'étend en Afrique francophone — adaptation du SI aux réglementations fiscales locales.

#### 3. Développement de produit (risque modéré)
Créer de nouveaux produits pour les marchés existants.
- **Leviers** : innovation, R&D, extension de gamme, digitalisation de services.
- **Impact SI** : nouvelles architectures (microservices, API), plateformes d'innovation, DevOps, time-to-market.
- **Exemple** : une banque traditionnelle qui lance une app mobile de paiement — nécessite une architecture API-first et un SI ouvert.

#### 4. Diversification (risque élevé)
Nouveau produit sur un nouveau marché. Deux types :
- **Diversification liée (concentrique)** : synergies avec l'activité existante. Ex : Amazon (e-commerce → AWS cloud).
- **Diversification non liée (conglomérale)** : aucune synergie. Ex : Virgin (musique → aviation → espace).
- **Impact SI** : transformation complète, intégration de SI hétérogènes, M&A tech.

### Lien avec d'autres outils stratégiques

| Outil | Complémentarité avec Ansoff |
|-------|----------------------------|
| **SWOT** | Identifier les forces/faiblesses internes avant de choisir une stratégie Ansoff |
| **PESTEL** | Analyser l'environnement externe pour évaluer la faisabilité de chaque quadrant |
| **BCG** | Positionner les produits existants (vache à lait, étoile) avant de décider de la croissance |
| **Porter (5 forces)** | Évaluer l'attractivité d'un nouveau marché avant un développement de marché |
| **Matrice de Kraljic** | Adapter la stratégie d'achats IT en fonction de la stratégie de croissance choisie |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Simple et visuel, facile à communiquer au CODIR | Simplification excessive (4 cases pour toute la stratégie) |
| Structure la réflexion stratégique | Ne prend pas en compte la concurrence |
| Évalue le niveau de risque de chaque option | Pas de dimension temporelle |
| Applicable à toutes les tailles d'entreprise | Ne quantifie pas le ROI de chaque option |
| Facilite le dialogue DSI/Direction | Frontière floue entre "nouveau" et "existant" |

### Cas d'usage concrets

1. **PME éditeur de logiciel** : une PME de 80 salariés éditant un logiciel de gestion pour les artisans utilise la matrice d'Ansoff pour sa stratégie à 3 ans. Le CODIR identifie : pénétration (intensifier le marketing digital — budget CRM × 2), développement de marché (extension en Belgique — adaptation du SI à la fiscalité belge), et développement de produit (ajout d'un module de facturation électronique — architecture microservices). La diversification (nouveau produit sur un nouveau marché) est écartée comme trop risquée.

2. **ETI industrielle en transformation digitale** : une ETI de 2 000 salariés dans l'industrie utilise Ansoff pour structurer sa transformation numérique. Le développement de produit (IoT + maintenance prédictive) nécessite une plateforme cloud, des compétences data et une architecture edge. Le DSI utilise la matrice pour justifier l'investissement IT auprès du CODIR en le reliant directement à la stratégie de croissance.

### Chiffres et tendances
- Igor Ansoff est considéré comme le père de la stratégie d'entreprise (Corporate Strategy, 1965).
- La matrice reste l'outil stratégique le plus enseigné en MBA (Financial Times, 2023).
- Dans le contexte de la transformation digitale, la "diversification numérique" (nouveau produit digital sur de nouveaux marchés) est la stratégie la plus courante des entreprises traditionnelles.
- 80 % des échecs de diversification sont liés à une sous-estimation des enjeux d'intégration SI (Bain & Company, 2022).

## Flashcards
#flashcards/Management_et_stratégie/Matrice_Ansoff #flashcards/Transversal/Matrice_Ansoff

Quelles sont les 4 stratégies de la matrice d'Ansoff ? :: 1. **Pénétration de marché** (produit existant, marché existant — risque faible), 2. **Développement de marché** (produit existant, nouveau marché — risque modéré), 3. **Développement de produit** (nouveau produit, marché existant — risque modéré), 4. **Diversification** (nouveau produit, nouveau marché — risque élevé).

Quel est l'impact SI d'une stratégie de développement de marché ? :: Internationalisation du SI : multi-langues, multi-devises, conformité aux réglementations locales (RGPD, fiscalité), infrastructure cloud multi-régions, CDN pour la performance.

Quelle est la différence entre diversification liée et non liée ? :: Diversification liée (concentrique) : synergies avec l'activité existante (ex : Amazon e-commerce → AWS). Diversification non liée (conglomérale) : aucune synergie (ex : Virgin musique → aviation).

Comment la matrice d'Ansoff complète-t-elle le SWOT ? :: Le SWOT identifie les forces/faiblesses internes et opportunités/menaces externes. La matrice d'Ansoff utilise ces résultats pour choisir la stratégie de croissance la plus adaptée au contexte de l'entreprise.

Pourquoi la matrice d'Ansoff est-elle utile pour un DSI ? :: Chaque stratégie de croissance a un impact direct sur le SI : pénétration (CRM, analytics), développement de marché (internationalisation SI), développement produit (nouvelles architectures), diversification (intégration SI hétérogènes). Elle permet de justifier les investissements IT auprès du CODIR.

## Sources
- Ansoff, H.I. (1957) — *"Strategies for Diversification"*, Harvard Business Review
- Ansoff, H.I. (1965) — *Corporate Strategy*, McGraw-Hill
- Johnson, G., Whittington, R. — *Exploring Strategy*, Pearson, 12e éd.
- Bpifrance — *PME et stratégies de croissance*, 2023

## Notions liées
- [[SWOT - PESTEL]]
- [[VUCA et benchmark]]
- [[Matrice de Kraljic]]
- [[Gouvernance IT]]
- [[KPI et pilotage de la performance]]
- [[Indicateurs financiers du SI]]
- [[VAN - TRI - Payback]]
