---
type: notion
thèmes:
  - Cybersécurité
  - Cloud et Virtualisation
  - Mobilité
statut: pas vu
dernière_révision: 
---

# ANSSI et acteurs de la cybersécurité

## En bref
> **Définition** : L'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) est l'autorité nationale française en matière de cybersécurité, créée en 2009 sous tutelle du Premier Ministre. Elle assure la défense des SI de l'État et des opérateurs d'importance vitale (OIV), publie des recommandations, qualifie des produits et prestataires, et coordonne la réponse aux incidents majeurs.
> **Pourquoi c'est important** : L'ANSSI est l'interlocuteur de référence pour toute DSI soumise à des obligations réglementaires (NIS2, LPM). Ses guides, qualifications et labels structurent les achats de sécurité de l'État et des grandes entreprises. Connaître ses publications et référentiels est indispensable pour piloter la cybersécurité en France.
> **Chiffres clés** :
> - L'ANSSI a traité 3 703 événements de sécurité signalés en 2023 (Rapport d'activité ANSSI 2023)
> - 187 opérations de cyberdéfense menées par l'ANSSI en 2023
> - cybermalveillance.gouv.fr a enregistré 3,8 millions de visiteurs et 280 000 demandes d'assistance en 2023

## Approfondir

### Fonctionnement

**L'ANSSI — missions et organisation :**

L'ANSSI exerce quatre grandes missions :
1. **Défense** : protection des systèmes d'information de l'État, des OIV et des entités critiques. Centre gouvernemental de veille, alerte et réponse aux attaques informatiques (CERT-FR).
2. **Régulation** : autorité compétente pour NIS2 en France, délivrance de qualifications et de visas de sécurité.
3. **Promotion** : publication de guides, référentiels et méthodes (EBIOS, guides thématiques), sensibilisation du grand public.
4. **Coordination internationale** : représentation de la France auprès de l'ENISA (UE), de l'OTAN et des réseaux CSIRT européens.

**LPM (Loi de Programmation Militaire) et OIV :**
- La LPM (articles 22 et suivants) impose depuis 2013 des obligations de sécurité aux Opérateurs d'Importance Vitale (OIV). Ces organisations opèrent des infrastructures critiques pour la nation (énergie, eau, transport, santé, télécommunications, finance, etc.).
- L'ANSSI peut imposer aux OIV des règles de sécurité, réaliser des contrôles et exiger des rapports d'audit. Les OIV doivent notifier les incidents de sécurité à l'ANSSI.
- NIS2 élargit cette logique à un périmètre beaucoup plus large (entités essentielles et importantes).

**SecNumCloud :**
Qualification délivrée par l'ANSSI aux prestataires de services cloud garantissant un niveau de sécurité élevé, conforme aux exigences des entités les plus sensibles (administrations, OIV, données de santé).
- Référentiel exigeant : sécurité technique, résilience, mais aussi immunité aux lois extra-territoriales étrangères (Cloud Act américain)
- Prestataires qualifiés SecNumCloud (2024) : OVHcloud (Public Cloud, Private Cloud), Outscale (Dassault Systèmes), Oodrive, S3NS (Google Cloud + Thales)
- Exigé pour héberger les données sensibles de l'État (doctrine cloud de l'État : "cloud au centre")

**Label ExpertCyber :**
Label délivré par cybermalveillance.gouv.fr aux prestataires de cybersécurité (ESN, cabinets de conseil) attestant de leur compétence et de leur éthique pour accompagner les PME/collectivités en matière de sécurité.
- Exigences : certifications, références clients, déontologie, assurance professionnelle
- Objectif : aider les petites structures à identifier des prestataires de confiance

**cybermalveillance.gouv.fr :**
Dispositif national d'assistance aux victimes de cybermalveillance, co-piloté par l'ANSSI et le SGDSN. Cible : particuliers, entreprises (surtout TPE/PME) et collectivités.
- Diagnostic en ligne, mise en relation avec des prestataires labellisés ExpertCyber
- Ressources pédagogiques, kits de sensibilisation
- Observatoire des menaces cyber (statistiques annuelles)

**Guide PA-054 (ANSSI) :**
Le guide PA-054 (référence interne ANSSI) correspond aux recommandations relatives à la sécurité des systèmes d'information en santé, ou plus généralement aux guides sectoriels publiés par l'ANSSI. Dans le contexte MAALSI, le terme "PA-054" peut désigner le guide d'aide à la prestation de réponse à incidents (PRIS), référentiel encadrant les prestataires de réponse aux incidents de sécurité qualifiés par l'ANSSI (PRIS qualification). Les PRIS qualifiés sont des prestataires en capacité d'intervenir sur les incidents majeurs avec un niveau de confiance garanti.

**Autres acteurs clés de l'écosystème cybersécurité français :**
- **CERT-FR** : équipe de réponse aux incidents opérée par l'ANSSI, publie alertes, avis et indicateurs de compromission
- **CNIL** : régulateur des données personnelles, complémentaire à l'ANSSI sur les violations de données (notification RGPD)
- **BPI France** : financement des PME et ETI pour leurs projets de cybersécurité
- **Campus Cyber** : lieu de référence de la cybersécurité française (La Défense), rassemblant ANSSI, entreprises, chercheurs et startups. Inauguré en 2022.
- **CLUSIF / CESIN** : associations professionnelles regroupant RSSI et experts cyber français
- **Pôle d'excellence cyber** (Rennes) : cluster de recherche et d'industrie cyber en lien avec la DGA

**Acteurs européens et internationaux :**
- **ENISA** : agence européenne de cybersécurité (Athènes), publie des rapports de menaces et coordonne les CSIRT nationaux
- **EUROPOL / EC3** : European Cybercrime Centre, coopération policière internationale
- **Interpol** : opérations mondiales contre la cybercriminalité
- **CISA** (USA) : homologue américain de l'ANSSI

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Référence et autorité de confiance en France | Ressources limitées face à l'ampleur des menaces |
| Guides et référentiels gratuits et de qualité | Processus de qualification long et coûteux |
| Qualification SecNumCloud = sécurité et souveraineté | SecNumCloud : catalogue de services encore limité |
| cybermalveillance.gouv.fr accessible aux PME | Label ExpertCyber peu connu des TPE/PME |
| Coordination européenne via ENISA | Fragmentation des acteurs (ANSSI, CNIL, COMCYBER) |
| Campus Cyber : dynamique de l'écosystème | Dépendance aux budgets de l'État |

### Acteurs et solutions du marché
- **ANSSI** : anssi.gouv.fr — autorité nationale, CERT-FR, qualifications, guides
- **cybermalveillance.gouv.fr** : dispositif d'assistance aux victimes
- **Campus Cyber** : campuscyber.fr — hub de l'écosystème cyber français
- **ENISA** : enisa.europa.eu — agence européenne
- **CLUSIF** : clusif.fr — association professionnelle française
- **CESIN** : cesin.fr — club des experts de la sécurité de l'information et du numérique
- **Prestataires qualifiés ANSSI** : liste disponible sur le site ANSSI (PDIS, PRIS, PASSI)

### Cas d'usage concrets
1. **Cyberattaque sur un hôpital** : Le CH de Versailles (2022) subit une cyberattaque majeure. L'ANSSI déploie une équipe d'intervention (PRIS qualifié mandaté), publie un retour d'expérience public et contribue à l'élaboration d'une offre de sécurité spécifique au secteur santé (cellule Acyma Santé).
2. **Hébergement de données de l'État** : Un ministère souhaite migrer ses applications vers le cloud. La doctrine "cloud au centre" impose d'utiliser un prestataire qualifié SecNumCloud. OVHcloud (qualifié SecNumCloud en 2021) est retenu pour héberger les données sensibles.
3. **PME victime de ransomware** : Une PME de 50 salariés subit un ransomware. Elle se connecte à cybermalveillance.gouv.fr, réalise un diagnostic en ligne et est mise en relation avec un prestataire labellisé ExpertCyber dans sa région pour la réponse à incident et la reconstruction du SI.

### Chiffres et tendances
- Budget ANSSI 2024 : environ 230 M€, 660 agents (en forte augmentation depuis 2017)
- ANSSI Rapport d'activité 2023 : 3 703 événements signalés, 187 opérations de cyberdéfense, 14 secteurs d'activité d'importance vitale couverts
- Campus Cyber : 200 organisations membres, 3 000 experts rassemblés
- SecNumCloud : objectif du gouvernement d'étendre le catalogue de services qualifiés d'ici 2026
- Tendance : montée de la coopération européenne (EU-CyCLONe, Joint Cyber Unit) dans la gestion des crises cyber transfrontalières

## Flashcards
#flashcards
Quelles sont les 4 missions principales de l'ANSSI ? :: Défense (protection des SI critiques, CERT-FR), Régulation (autorité NIS2, qualifications), Promotion (guides, sensibilisation) et Coordination internationale (ENISA, OTAN).

Qu'est-ce qu'un OIV et quel est le cadre réglementaire associé ? :: Opérateur d'Importance Vitale : organisation opérant des infrastructures critiques pour la nation (énergie, santé, transport...). Soumis à la LPM (Loi de Programmation Militaire) qui impose des règles de sécurité renforcées et la notification des incidents à l'ANSSI.

Qu'est-ce que SecNumCloud ? :: Qualification ANSSI pour les prestataires de services cloud garantissant un haut niveau de sécurité et de souveraineté (immunité aux lois extra-territoriales étrangères). Exigé pour héberger les données sensibles de l'État (doctrine "cloud au centre").

À quoi sert cybermalveillance.gouv.fr ? :: Dispositif national d'assistance aux victimes de cybermalveillance (particuliers, PME, collectivités). Propose un diagnostic en ligne, une mise en relation avec des prestataires labellisés ExpertCyber et des ressources pédagogiques.

Qu'est-ce que le label ExpertCyber ? :: Label délivré par cybermalveillance.gouv.fr aux prestataires de cybersécurité (ESN, cabinets) attestant de leur compétence et éthique pour accompagner les petites structures (TPE, PME, collectivités).

Qu'est-ce que le CERT-FR ? :: Computer Emergency Response Team français, opéré par l'ANSSI. Publie des alertes de sécurité, des avis sur les vulnérabilités (CVE), des indicateurs de compromission et coordonne la réponse aux incidents majeurs en France.

Quelle est la différence entre ANSSI et CNIL en matière de cybersécurité ? :: L'ANSSI est l'autorité de cybersécurité (protection des SI, NIS2, OIV). La CNIL est l'autorité de protection des données personnelles (RGPD). En cas de violation de données, les deux peuvent être impliquées : ANSSI pour l'incident technique, CNIL pour la notification RGPD.

## Sources
- ANSSI — Rapport d'activité 2023 (anssi.gouv.fr)
- ANSSI — Guide de l'hygiène informatique (42 mesures)
- ANSSI — Référentiel SecNumCloud v3.2
- cybermalveillance.gouv.fr — Rapport d'activité 2023
- Loi de Programmation Militaire 2019-2025 (LPM)
- ENISA — Threat Landscape 2023
- Campus Cyber — Rapport d'activité 2023

## Notions liées
- [[NIS2]]
- [[ISO 27001 - 27002]]
- [[PCA - PRA]]
- [[Cyber-assurance]]
- [[NIST Cybersecurity Framework]]
- [[Outils de sécurité réseau]]
- [[Authentification et gestion des accès (IAM)]]
