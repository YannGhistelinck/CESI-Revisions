---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Cloud souverain

## En bref
> **Définition** : Le cloud souverain désigne une offre cloud garantissant que les données sont hébergées et traitées sur le territoire national, par des entités soumises exclusivement au droit français ou européen, sans possibilité de transfert vers des juridictions étrangères. Il se distingue du simple "cloud de confiance" par le niveau de garantie juridique et technique offert.
> **Pourquoi c'est important** : Dans un contexte de tensions géopolitiques et de législations extraterritoriales (CLOUD Act américain), les DSI des OIV, administrations et organisations sensibles doivent s'assurer que leurs données ne sont pas accessibles par des autorités étrangères. La doctrine "Cloud au centre" de l'État français en fait un enjeu stratégique national.
> **Chiffres clés** :
> - Le marché français du cloud souverain est estimé à 8 milliards d'euros en 2027 (Pierre Audoin Consultants, 2023)
> - SecNumCloud : seulement 4 qualifications délivrées par l'ANSSI en 2024 (Outscale, OVHcloud, Oodrive, 3DS Outscale)
> - La doctrine "Cloud au centre" concerne l'ensemble des 800+ applications de l'État français

## Approfondir

### Fonctionnement

**Cloud de confiance vs cloud souverain**
Le "cloud de confiance" est un label intermédiaire : l'infrastructure peut être opérée par un acteur non-européen, mais avec des protections contractuelles et techniques pour isoler les données (chiffrement, clés sous contrôle français). Il ne garantit pas l'immunité totale aux lois extraterritoriales. Le cloud souverain va plus loin : l'opérateur doit être une entité de droit français ou européen, sans capital ni dépendance technologique étrangère significative.

**SecNumCloud**
Qualification délivrée par l'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information). Référentiel le plus exigeant en France. Impose :
- Hébergement exclusif sur le territoire de l'UE
- Opérateur de droit français, sans subordination à une loi étrangère
- Cloisonnement technique entre clients
- Audits réguliers et transparence des sous-traitants

Requis pour les Données de Santé (HDS), les OIV (Opérateurs d'Importance Vitale) et recommandé pour les données sensibles de l'État.

**Principales offres souveraines françaises**

| Offre | Opérateur | Technologie de base | Statut SecNumCloud |
|-------|-----------|--------------------|--------------------|
| S3NS | Thales + Google | Google Cloud | En cours de qualification |
| Bleu | Capgemini + Orange | Microsoft Azure | En cours de qualification |
| NumSpot | Banques/assurances | Open source (Outscale) | Candidat |
| Outscale | Dassault Systèmes | Propriétaire | Qualifié |
| OVHcloud | OVH | Propriétaire | Qualifié (certains services) |

**Gaia-X**
Initiative européenne lancée en 2019 par la France et l'Allemagne pour créer un écosystème de données européen interopérable. Objectif : établir des standards communs de portabilité, de transparence et de souveraineté des données. N'est pas une offre cloud mais un cadre de gouvernance et de labellisation. Résultats mitigés : adoption lente, critiques sur la complexité et la participation d'acteurs américains.

**Doctrine "Cloud au centre"**
Circulaire de la Direction Interministérielle du Numérique (DINUM) de 2021 : les nouvelles applications de l'État ou leurs évolutions significatives doivent être hébergées sur le cloud (cloud public qualifié ou cloud de confiance). Priorise les offres SecNumCloud pour les données sensibles. A accéléré le développement des offres souveraines françaises.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Immunité aux lois extraterritoriales (CLOUD Act) | Offre moins mature que les hyperscalers américains |
| Conformité RGPD facilitée | Coûts souvent plus élevés |
| Confiance accrue pour les données sensibles | Catalogue de services plus limité |
| Enjeu stratégique national (indépendance) | Qualifications SecNumCloud rares et longues à obtenir |
| Réduction du risque géopolitique | Risque de dépendance technologique maquillée (S3NS, Bleu) |

### Acteurs et solutions du marché

- **Qualifiés SecNumCloud** : Outscale (3DS), OVHcloud (périmètre restreint), Oodrive (SaaS collaboratif)
- **En qualification** : S3NS (Thales/Google), Bleu (Capgemini/Orange/Microsoft)
- **Européens alternatifs** : IONOS (Deutsche Telekom), Exoscale (Suisse), Cleura (Suède)
- **Offres HDS (Hébergement de Données de Santé)** : OVHcloud, Outscale, Microsoft Azure (avec garanties spécifiques)
- **Gouvernance** : ANSSI (qualification), DINUM (doctrine), CNIL (conformité RGPD)

### Cas d'usage concrets

1. **Ministère de la Santé — données HDS** : hébergement des données de santé sur une plateforme qualifiée SecNumCloud. L'objectif est d'empêcher qu'une assignation judiciaire américaine (CLOUD Act) puisse contraindre un opérateur à fournir des données médicales de citoyens français.

2. **Groupe bancaire français** : une banque soumise à la supervision de l'ACPR choisit OVHcloud pour ses workloads réglementés, tout en conservant AWS pour ses applications non-sensibles. Cette approche hybride sépare les données selon leur niveau de sensibilité.

3. **Administration publique** : suite à la doctrine "Cloud au centre", un ministère migre ses outils collaboratifs vers Oodrive (qualifié SecNumCloud), remplaçant Microsoft 365 pour les communications internes sensibles.

### Chiffres et tendances

- En 2024, la France est le pays européen le plus avancé sur la qualification cloud souverain (ANSSI)
- Gaia-X compte 300+ membres en 2024, dont des acteurs US (AWS, Microsoft, Google), ce qui soulève des questions sur la véritable indépendance du cadre
- Le modèle "cloud de confiance" (S3NS, Bleu) fait débat : certains experts (dont des membres de l'ANSSI) estiment qu'il ne protège pas réellement contre le CLOUD Act si la dépendance technologique aux acteurs US subsiste
- Tendance : multiplication des offres "souveraines" en Europe (UK Sovereign Cloud, Gaia-X nodes nationaux)

## Flashcards
#flashcards

Qu'est-ce que SecNumCloud ? :: Référentiel de qualification de l'ANSSI pour les offres cloud souveraines. Impose l'hébergement en UE, un opérateur de droit français sans subordination étrangère, des audits réguliers. Le plus haut niveau de garantie souveraine en France.

Quelle est la différence entre cloud souverain et cloud de confiance ? :: Le cloud souverain garantit une indépendance totale (opérateur, technologie, droit). Le cloud de confiance est un niveau intermédiaire : un opérateur européen peut opérer une technologie non-européenne avec des protections contractuelles et techniques, sans garantie totale face au CLOUD Act.

Qu'est-ce que Gaia-X ? :: Initiative franco-allemande lancée en 2019 visant à établir des standards européens d'interopérabilité et de souveraineté des données cloud. Ce n'est pas un fournisseur cloud mais un cadre de gouvernance et de labellisation.

Citez deux offres de cloud de confiance françaises en cours de qualification SecNumCloud. :: S3NS (Thales + Google Cloud) et Bleu (Capgemini + Orange + Microsoft Azure).

Qu'est-ce que la doctrine "Cloud au centre" ? :: Circulaire DINUM de 2021 imposant que les nouvelles applications de l'État soient hébergées sur le cloud (cloud public qualifié ou cloud de confiance), avec priorité aux offres SecNumCloud pour les données sensibles.

Pourquoi le modèle S3NS fait-il débat en termes de souveraineté ? :: Parce que S3NS repose technologiquement sur Google Cloud. Si la dépendance technologique à un acteur américain subsiste, certains experts estiment que la protection contre le CLOUD Act n'est pas garantie malgré l'opération par Thales.

Quel est le principal risque juridique que le cloud souverain cherche à éviter ? :: Le CLOUD Act américain, qui permet aux autorités américaines de contraindre des opérateurs ayant des liens avec les USA à fournir des données, y compris hébergées à l'étranger.

## Sources

- ANSSI, "Référentiel SecNumCloud", version 3.2, 2022
- DINUM, "Doctrine d'utilisation de l'informatique en nuage par l'État", 2021
- Pierre Audoin Consultants (PAC), "Cloud souverain en France", 2023
- Gaia-X Association, rapports officiels 2023-2024
- Sénat français, rapport d'information "Souveraineté numérique", 2022

## Notions liées

- [[CLOUD Act et transferts de données]]
- [[Modèles de déploiement cloud]]
- [[Vendor lock-in et réversibilité]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[NIS2]]
- [[Économie du cloud]]
