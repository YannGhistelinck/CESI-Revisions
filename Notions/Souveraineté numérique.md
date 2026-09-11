---
type: notion
thèmes:
  - Big DATA
  - Cloud et Virtualisation
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Souveraineté numérique

## En bref
> **Définition** : La **souveraineté numérique** désigne la capacité d'un État, d'une organisation ou d'un individu à exercer un contrôle effectif sur ses systèmes numériques, ses infrastructures, ses données et ses technologies — en maintenant une autonomie de décision face aux dépendances technologiques étrangères. La **souveraineté des données** en est la composante centrale : elle concerne la juridiction applicable aux données et la capacité à garantir qu'elles ne sont accessibles qu'aux parties autorisées. Ces concepts s'inscrivent dans des **enjeux géopolitiques** majeurs : la rivalité technologique USA-Chine, le risque d'extraterritorialité (CLOUD Act, USA PATRIOT Act), et la volonté européenne de construire une autonomie stratégique dans le numérique.
> **Pourquoi c'est important** : Pour les DSI et décideurs, la souveraineté numérique conditionne les choix d'architecture (cloud souverain, on-premise, chiffrement BYOK), les stratégies de réduction du vendor lock-in, et la conformité aux réglementations (RGPD, DORA, NIS2). C'est également un argument commercial croissant : secteur public, santé, défense et finance privilégient de plus en plus des solutions souveraines certifiées.
> **Chiffres clés** :
> - 73 % du marché mondial du cloud est détenu par 3 acteurs américains : AWS (31 %), Azure (25 %), Google Cloud (11 %) — Synergy Research, T1 2024.
> - La France a lancé le plan "Cloud au Centre" en 2021 : toute donnée sensible de l'État doit être hébergée sur un cloud qualifié SecNumCloud ou sur des serveurs de l'État.
> - Le label SecNumCloud (ANSSI) a été obtenu par moins de 10 fournisseurs en France en 2024, dont OVHcloud, Outscale (Dassault Systèmes), et Oodrive.

## Approfondir

### Fonctionnement

**Définitions et niveaux de souveraineté**

La souveraineté numérique s'applique à plusieurs niveaux :
- **Souveraineté étatique** : capacité d'un État à réguler, contrôler et développer ses infrastructures numériques (réseaux, câbles sous-marins, datacenters, algorithmes). Enjeu : réduire la dépendance aux technologies étrangères pour des fonctions régaliennes (défense, justice, santé, éducation).
- **Souveraineté des données (data sovereignty)** : garantie que les données d'une organisation ou d'un État restent sous juridiction contrôlée et ne sont accessibles qu'aux parties autorisées. Différent de la data residency (localisation physique) qui n'est pas suffisante si l'opérateur est étranger.
- **Souveraineté technologique** : capacité à produire et maîtriser les technologies clés (semiconducteurs, OS, navigateurs, protocoles) plutôt que de dépendre de fournisseurs étrangers.

**Enjeux géopolitiques**

*Rivalité USA-Chine* : la guerre technologique se joue sur les semiconducteurs (embargo TSMC sur Huawei, 2020 ; CHIPS Act américain, 2022), les réseaux 5G (exclusion de Huawei par de nombreux pays occidentaux), les modèles d'IA (régulation de l'export des puces GPU vers la Chine), et les données des citoyens (TikTok — soupçons de transfert de données vers la Chine, interdiction sur les téléphones gouvernementaux dans de nombreux pays).

*Extraterritorialité américaine* : le CLOUD Act (2018) permet aux autorités américaines d'accéder aux données détenues par des opérateurs américains, quel que soit le pays de stockage. FISA Section 702 étend la surveillance aux ressortissants étrangers. Ces lois créent un risque direct pour les organisations européennes utilisant AWS, Azure ou Google Cloud pour des données sensibles.

*Projet européen de souveraineté numérique* : l'UE cherche à construire une autonomie stratégique numérique via : Gaia-X (infrastructure de données européenne), le Cloud souverain (labels nationaux — SecNumCloud en France, C5 en Allemagne), la réglementation (RGPD, Data Act, AI Act, DSA/DMA), et les investissements dans les technologies clés (European Chips Act — 43 Md€ d'ici 2030, IPCEI cloud et microélectronique).

**Cloud souverain et SecNumCloud**

Le **cloud souverain** désigne un service cloud où les données et les infrastructures sont sous juridiction et contrôle national ou européen — sans risque d'accès par des autorités étrangères. Deux approches :
- **Cloud de confiance** (approche française) : un opérateur européen (OVHcloud, Thales) opère une infrastructure cloud basée sur la technologie d'un éditeur américain (Azure, Google Workspace), mais sans que l'éditeur américain ait accès aux données ou aux clés de chiffrement. Exemple : S3NS (Thales + Google Cloud), Bleu (Orange + Capgemini + Microsoft).
- **Cloud natif souverain** : infrastructure entièrement européenne, sans composant technologique américain. Exemple : Outscale (Dassault Systèmes), NutanixCloud via partenariats européens.

**SecNumCloud** (ANSSI) : qualification française définissant les exigences techniques et juridiques pour un cloud souverain. Critères clés : opérateur de droit européen avec capital majoritairement européen, données chiffrées avec clés gérées en Europe, aucune donnée accessible à des entités hors UE/EEE, audit de sécurité par l'ANSSI. Qualification valable 3 ans, renouvelable.

**Gaia-X**
Initiative européenne lancée en 2020 (France + Allemagne) visant à créer un écosystème de partage de données souverain et interopérable en Europe. Non un cloud unifié, mais un **cadre de confiance** définissant des règles de fédération, de portabilité et de transparence pour les services cloud. Plus de 350 membres en 2024 (entreprises, États, institutions). Critiquée pour sa lenteur et l'adhésion de membres américains (AWS, Microsoft, Google) qui diluent son caractère souverain.

**Stratégies organisationnelles**

- **BYOK (Bring Your Own Key)** : l'organisation conserve ses propres clés de chiffrement, séparées de l'opérateur cloud. Même un opérateur américain ne peut lire les données chiffrées avec des clés BYOK dont il n'a pas la possession. Limite : l'opérateur peut toujours être contraint de fournir les données chiffrées, mais leur intelligibilité dépend des clés.
- **HYOK (Hold Your Own Key)** : variante où les clés ne quittent jamais l'environnement de l'organisation (HSM on-premise), même pour le chiffrement/déchiffrement (réalisé localement avant envoi au cloud).
- **Multi-cloud et réversibilité** : stratégie de diversification des fournisseurs cloud pour réduire la dépendance à un seul acteur et améliorer la résilience. Articulée avec le Data Act (réduction des switching fees).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Protection contre l'extraterritorialité étrangère (CLOUD Act) | Coût supérieur des solutions souveraines vs GAFAM |
| Conformité RGPD et réglementations sectorielles (HDS, SecNumCloud) | Écosystème souverain moins mature (moins de services, d'intégrations) |
| Réduction du risque géopolitique (coupure, sanction) | Risque de protectionnisme numérique nuisant à l'innovation |
| Argument commercial pour les marchés publics et secteurs sensibles | Difficulté de migrer les systèmes existants vers des solutions souveraines |
| Renforcement de la filière numérique européenne | Gaia-X : gouvernance complexe, adoption lente |

### Acteurs et solutions du marché

- **Fournisseurs cloud souverains français** : OVHcloud (SecNumCloud pour certains services), Outscale (Dassault Systèmes — SecNumCloud), Oodrive (SecNumCloud), Docaposte
- **Modèles de cloud de confiance** : S3NS (Thales + Google Cloud), Bleu (Orange + Capgemini + Microsoft Azure), T-Systems (Deutsche Telekom + Google Cloud — Allemagne)
- **Initiatives européennes** : Gaia-X (France + Allemagne), IPCEI Cloud (Important Projects of Common European Interest), European Alliance for Industrial Data, Edge and Cloud
- **Labels et qualifications** : SecNumCloud (ANSSI, France), C5 (BSI, Allemagne), ENS (Espagne), HDS (Hébergeur de Données de Santé — pour le secteur santé en France)
- **Organismes de politique** : ENISA (Agence de l'UE pour la cybersécurité), ANSSI (France), direction interministérielle du numérique (DINUM)
- **Câbles sous-marins souverains** : PEACE Cable, Dunant (Google), 2Africa (Meta) — la propriété des câbles est un enjeu croissant de souveraineté des infrastructures

### Cas d'usage concrets

1. **Plan "Cloud au Centre" de l'État français** : depuis 2021, les administrations françaises doivent héberger leurs données sensibles sur des clouds qualifiés SecNumCloud ou sur les infrastructures de l'État (cloud interne). La circulaire interministérielle distingue 3 niveaux de sensibilité : données publiques (cloud standard), données sensibles (SecNumCloud ou cloud interne), données très sensibles (cloud classifié — Défense).

2. **Hôpital et données de santé (HDS + SecNumCloud)** : un CHU migre ses dossiers patients vers le cloud. La réglementation impose un hébergeur certifié HDS (Hébergeur de Données de Santé). Pour les données les plus sensibles (psychiatrie, VIH), le CHU opte pour Oodrive (certifié HDS + SecNumCloud), évitant tout risque d'accès par des autorités étrangères via le CLOUD Act.

3. **Multinationale et stratégie BYOK** : un groupe industriel français utilise Azure pour son ERP. Pour les données de R&D les plus sensibles (brevets, formules), il déploie une stratégie BYOK : les clés de chiffrement sont stockées dans un HSM on-premise géré par la DSI. Azure ne peut jamais lire ces données en clair. La clé ne quitte jamais le périmètre de l'entreprise (HYOK).

4. **Souveraineté des données en contexte sino-européen** : une entreprise automobile européenne implantée en Chine doit respecter la PIPL (localisation des données des employés chinois en Chine) et le RGPD (protection des données des employés européens). Elle déploie une architecture multi-cloud régionale : données chinoises sur Alibaba Cloud (conforme PIPL), données européennes sur OVHcloud (SecNumCloud), sans flux trans-frontaliers des données sensibles.

### Chiffres et tendances

- European Chips Act (2023) : 43 Md€ d'investissements publics et privés pour porter la part de l'Europe dans la production mondiale de semiconducteurs à 20 % d'ici 2030 (contre ~10 % en 2023).
- 95 % des données mondiales transitent par des câbles sous-marins dont la majorité est propriété de consortiums où les GAFAM ont une participation croissante (2TbE, Dunant, Grace Hopper).
- La Chine a fixé à 70 % la part des technologies "locales" dans les infrastructures sensibles d'ici 2025 (politique "Xinchuang" — substitution informatique).
- En France, le marché du cloud souverain représentait 1,2 Md€ en 2023 et devrait dépasser 3 Md€ en 2027 (PAC, 2023).
- TikTok a lancé le projet "Clover" en 2023 pour stocker les données des utilisateurs européens en Europe (Irlande, Norvège) et couper l'accès de ByteDance (Chine) à ces données — réponse aux préoccupations de souveraineté.

## Flashcards
#flashcards/Big_DATA/Souveraineté_numérique #flashcards/Cloud_et_Virtualisation/Souveraineté_numérique #flashcards/Management_et_stratégie/Souveraineté_numérique

Quelle est la différence entre souveraineté des données et data residency ? :: La data residency désigne la localisation physique des données (ex. : datacenter en France). La souveraineté des données désigne la juridiction applicable et la garantie que les données ne sont accessibles qu'aux parties autorisées. Un opérateur américain peut héberger des données en France (data residency = FR) mais rester soumis au CLOUD Act (souveraineté = insuffisante).

Qu'est-ce que le label SecNumCloud et quels sont ses critères principaux ? :: Qualification délivrée par l'ANSSI définissant les exigences d'un cloud souverain : opérateur de droit européen à capital majoritairement européen, données chiffrées avec clés gérées en Europe, aucune donnée accessible à des entités hors UE/EEE. Valable 3 ans, renouvelable. Obtenu par OVHcloud, Outscale, Oodrive notamment.

Quelle est la différence entre un cloud souverain "natif" et un cloud "de confiance" ? :: Le cloud souverain natif utilise une infrastructure entièrement européenne sans composant américain (ex. : Outscale). Le cloud de confiance est un modèle hybride où un opérateur européen opère une infrastructure basée sur la technologie d'un éditeur américain, mais sans que cet éditeur accède aux données ou aux clés de chiffrement (ex. : S3NS = Thales + Google Cloud).

Qu'est-ce que Gaia-X et quelle est sa principale limite ? :: Initiative franco-allemande (2020) créant un cadre de confiance pour un écosystème de données souverain et interopérable en Europe (règles de fédération, portabilité, transparence). Principale limite : gouvernance complexe, adoption lente, et adhésion de membres américains (AWS, Microsoft, Google) qui diluent son caractère souverain.

Qu'est-ce que le BYOK et comment renforce-t-il la souveraineté des données dans le cloud ? :: Bring Your Own Key : l'organisation conserve ses propres clés de chiffrement, séparées de l'opérateur cloud. Un opérateur américain ne peut pas lire les données chiffrées avec des clés BYOK qu'il ne détient pas. HYOK (Hold Your Own Key) est la variante où les clés ne quittent jamais l'environnement de l'organisation.

Quels sont les 3 enjeux géopolitiques principaux de la souveraineté numérique ? :: 1. Rivalité USA-Chine (semiconducteurs, 5G, IA, données) ; 2. Extraterritorialité américaine (CLOUD Act, FISA 702) permettant l'accès aux données des entreprises étrangères via des opérateurs américains ; 3. Construction de l'autonomie stratégique européenne (Gaia-X, SecNumCloud, European Chips Act, réglementation DSA/DMA/AI Act).

Qu'impose le plan "Cloud au Centre" de l'État français ? :: Depuis 2021, les administrations françaises doivent héberger leurs données selon leur niveau de sensibilité : données publiques sur cloud standard, données sensibles sur cloud qualifié SecNumCloud ou cloud interne de l'État, données très sensibles sur cloud classifié défense.

## Sources

- Circulaire interministérielle n° 6282/SG du 5 juillet 2021 — "Cloud au Centre" : https://www.numerique.gouv.fr/
- ANSSI — référentiel SecNumCloud v3.2 : https://www.ssi.gouv.fr/
- Gaia-X — association officielle : https://gaia-x.eu/
- European Chips Act — Commission européenne : https://digital-strategy.ec.europa.eu/
- Synergy Research Group — Cloud Market Share Q1 2024
- Shoshana Zuboff, "The Age of Surveillance Capitalism", 2019 (contexte capitalisme de surveillance)
- ENISA, "Cloud Cybersecurity Market Analysis", 2023
- PAC (Pierre Audoin Consultants), "Le marché du cloud souverain en France", 2023

## Notions liées

- [[Cloud souverain]]
- [[CLOUD Act et transferts de données]]
- [[RGPD]]
- [[Certifications et normes cloud]]
- [[Acteurs cloud]]
- [[Normes ISO liées aux données]]
- [[Data Act]]
- [[DSA - DMA]]
- [[Vendor lock-in et réversibilité]]
