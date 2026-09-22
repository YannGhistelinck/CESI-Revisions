---
type: notion
thèmes:
  - Optimisation du SI
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Audit SI

![[N — Audit SI.mp3]]
## En bref
> **Définition** : L'audit SI est un processus d'évaluation indépendant et systématique visant à vérifier la conformité, la performance, la sécurité et l'organisation du Système d'Information par rapport à des référentiels définis. Il produit un diagnostic objectif et des recommandations d'amélioration destinés à la direction.
> **Pourquoi c'est important** : Dans un contexte de multiplication des cybermenaces (NIS2, RGPD, ISO 27001), l'audit SI est devenu un outil de gouvernance incontournable. Pour un DSI, il permet d'objectiver les risques, de justifier les investissements sécurité et d'assurer la conformité réglementaire auprès du CODIR et des régulateurs.
> **Chiffres clés** :
> - 67 % des entreprises françaises ont subi un incident de sécurité en 2023 (Baromètre CESIN, 2024).
> - Le coût moyen d'un audit SI externe pour une PME est de 15 000 à 50 000 € selon le périmètre (Wavestone, 2023).
> - Les entreprises certifiées ISO 27001 réduisent en moyenne de 40 % le coût de leurs incidents de sécurité (BSI Group, 2022).

## Approfondir

### Fonctionnement

**Les types d'audit SI**

| Type | Objectif | Périmètre typique |
|------|----------|-------------------|
| **Audit de conformité** | Vérifier le respect de normes, lois ou politiques internes | RGPD, ISO 27001, NIS2, politique interne |
| **Audit de performance** | Évaluer l'efficacité et l'efficience du SI | Coûts, délais, qualité de service |
| **Audit de sécurité** | Identifier les vulnérabilités et évaluer le niveau de protection | Infrastructure, applications, organisation |
| **Audit organisationnel** | Évaluer les processus, la gouvernance, les ressources humaines SI | RACI, processus ITIL, maturité DSI |
| **Audit technique** | Analyse approfondie de l'infrastructure ou du code | Configurations, architecture réseau, code source |

**Les phases d'un audit SI**

1. **Planification** : Définition du périmètre, des objectifs, des critères d'évaluation, du calendrier. Désignation de l'équipe d'audit et des interlocuteurs côté audité. Revue documentaire préliminaire (politiques SI, PSSI, cartographies existantes).

2. **Terrain / Collecte** : Entretiens avec les équipes SI et métier, observation des pratiques, collecte de preuves (logs, configurations, procédures, contrats). Tests techniques si audit de sécurité.

3. **Analyse** : Comparaison avec le référentiel choisi, identification des écarts (gaps), qualification des risques associés, hiérarchisation des constats.

4. **Rapport** : Rédaction du rapport d'audit avec synthèse pour la direction (Executive Summary), liste détaillée des constats avec niveau de criticité, recommandations priorisées et plan d'amélioration.

5. **Suivi** : Vérification de la mise en œuvre des recommandations lors d'audits de suivi. Mesure de l'amélioration dans le temps.

**La cartographie du SI**

La cartographie est un prérequis fondamental à tout audit. Elle décrit le SI selon plusieurs couches :

- **Couche applicative** : Inventaire des applications, leurs interdépendances, données traitées, criticité métier.
- **Couche technique** : Infrastructure (serveurs, réseau, stockage), systèmes d'exploitation, versions.
- **Couche données** : Flux de données, classification, localisations, traitements (essentiel RGPD).
- **Couche réseau** : Topologie réseau, zones de confiance (DMZ, LAN, WAN), points d'accès, interconnexions.

*Outils de cartographie* : BlueKenue, CMDB ServiceNow, LeanIX, Mega HOPEX.

**Les référentiels d'audit SI**

| Référentiel | Domaine | Usage |
|------------|---------|-------|
| **ISO 19011** | Lignes directrices pour l'audit des systèmes de management | Méthodologie audit |
| **ISO/IEC 27001** | Management de la sécurité de l'information (SMSI) | Audit sécurité SI |
| **ISO/IEC 27002** | Bonnes pratiques de contrôles sécurité | Référentiel de contrôles |
| **COBIT 2019** | Gouvernance et management des SI | Audit gouvernance/IT |
| **ITIL v4** | Gestion des services IT | Audit processus ITSM |
| **RGPD** | Protection des données personnelles | Audit conformité données |
| **NIS2** | Sécurité des réseaux et des systèmes | Audit entités essentielles/importantes |
| **Guide ANSSI** | Sécurité des SI pour organismes français | Audit sécurité France |

**Audit interne vs Audit externe**

| Critère | Audit interne | Audit externe |
|---------|--------------|---------------|
| Réalisé par | Équipe interne ou audit interne de l'entreprise | Cabinet indépendant (Big4, Wavestone, Intrinsec…) |
| Indépendance | Relative (connaissance du contexte) | Totale (regard neuf, crédibilité externe) |
| Coût | Plus faible | Plus élevé (15 000 à 500 000€ selon périmètre) |
| Fréquence | Continue / régulière | Ponctuelle (certification, incident, fusion) |
| Livrables | Rapport interne, plan d'actions | Rapport certifié, lettre de direction |
| Objectif | Amélioration continue | Certification, conformité réglementaire, tiers de confiance |

**Livrables d'un audit SI**

- **Rapport d'audit** : Constats factuels, preuves, écarts par rapport au référentiel, recommandations.
- **Plan d'amélioration (PAP)** : Actions priorisées, responsables, délais, indicateurs de suivi.
- **Executive Summary** : Synthèse destinée à la direction (1 à 2 pages), sans jargon technique.
- **Matrice des risques** : Cartographie des risques identifiés (probabilité × impact), priorisés.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Diagnostic objectif et documenté des risques | Mobilisation importante des équipes SI pendant l'audit |
| Preuve de diligence vis-à-vis des régulateurs | Coût significatif pour les PME |
| Base solide pour prioriser les investissements sécurité | Résultats peuvent être anxiogènes si mal communiqués |
| Crédibilité auprès des partenaires et clients (certification ISO 27001) | Risque de "compliance washing" : cocher des cases sans amélioration réelle |
| Amélioration continue de la maturité SI | Photo à un instant T : le SI évolue plus vite que les recommandations |

### Acteurs et solutions du marché

**Cabinets d'audit SI en France**
- Grands cabinets : Wavestone, Deloitte Cyber, KPMG Advisory, PwC Cybersecurity.
- Spécialistes sécurité : Intrinsec, Synacktiv, Sekoia (ANSSI PRIS).
- Pour PME : Cabinets régionaux labellisés ANSSI.

**Outils d'audit**
- **GRC (Governance, Risk, Compliance)** : ServiceNow GRC, Archer, OneTrust.
- **Scanners de vulnérabilités** : Nessus (Tenable), Qualys, OpenVAS.
- **CMDB / ITSM** : ServiceNow, iTop (open-source).

### Cas d'usage concrets

1. **PME industrielle sous-traitante défense** : Audit de conformité ISO 27001 réalisé par un cabinet externe pour obtenir la certification exigée par un client grand compte. 6 mois de préparation, 12 jours d'audit. Obtention de la certification après correction de 23 non-conformités mineures.

2. **Collectivité territoriale après incident** : Suite à une cyberattaque par ransomware, audit de sécurité complet (infrastructure, AD, sauvegardes, sensibilisation). Plan de remédiation sur 18 mois avec soutien ANSSI.

3. **DSI d'un groupe de distribution** : Audit de maturité COBIT annuel pour objectiver le niveau de gouvernance SI et construire le plan stratégique triennal. Score global passé de niveau 2 à 3 sur 5 en 3 ans.

### Chiffres et tendances

- 34 % des entreprises françaises réalisent un audit SI au moins une fois par an (CESIN, 2023).
- La demande d'audits de conformité NIS2 a augmenté de 180 % en Europe depuis la transposition de la directive en 2024 (ENISA, 2024).
- Le nombre d'entreprises certifiées ISO 27001 a progressé de 24 % en France entre 2021 et 2023 (ISO Survey, 2023).

## Flashcards
#flashcards/Optimisation_du_SI/Audit_SI #flashcards/Cybersécurité/Audit_SI

Quelles sont les 5 phases d'un audit SI ? :: 1. Planification (périmètre, objectifs), 2. Terrain/Collecte (entretiens, preuves), 3. Analyse (écarts, risques), 4. Rapport (constats, recommandations), 5. Suivi (mise en œuvre, mesure).

Quels sont les 4 types principaux d'audit SI ? :: Audit de conformité (normes/lois), audit de performance (efficacité), audit de sécurité (vulnérabilités), audit organisationnel (gouvernance/processus).

Citez 3 référentiels utilisés pour un audit SI. :: ISO/IEC 27001 (sécurité de l'information), COBIT 2019 (gouvernance IT), ISO 19011 (méthodologie d'audit des systèmes de management). Aussi : ITIL v4, RGPD, NIS2.

Quelle est la différence entre audit interne et audit externe ? :: L'audit interne est réalisé par les équipes de l'entreprise (moins coûteux, continu), l'audit externe par un cabinet indépendant (crédibilité externe, certification, conformité réglementaire).

Quelles sont les 4 couches de la cartographie du SI ? :: Couche applicative (inventaire des applications), couche technique (infrastructure), couche données (flux, classification), couche réseau (topologie, zones de confiance).

Qu'est-ce qu'un SMSI (ISO 27001) et quel est son lien avec l'audit ? :: Système de Management de la Sécurité de l'Information. ISO 27001 définit les exigences du SMSI ; un audit externe permet d'obtenir la certification qui atteste de la conformité.

Quels sont les livrables attendus d'un audit SI ? :: Rapport d'audit (constats, preuves, recommandations), plan d'amélioration (PAP) avec actions priorisées, executive summary pour la direction, matrice des risques.

Pourquoi la cartographie du SI est-elle un prérequis à l'audit ? :: Elle permet d'identifier le périmètre exact à auditer, les dépendances entre systèmes, les flux de données sensibles et les points d'entrée potentiels, sans quoi l'audit serait incomplet et les risques mal évalués.

## Sources
- ISO/IEC 27001:2022 — https://www.iso.org/standard/27001
- ISO 19011:2018 — Lignes directrices pour l'audit des systèmes de management.
- COBIT 2019 — ISACA — https://www.isaca.org/resources/cobit
- ANSSI — Guide d'hygiène informatique — https://www.ssi.gouv.fr
- CESIN — Baromètre annuel de la cybersécurité en entreprise (2024).
- BSI Group — *The Business Benefits of ISO 27001* (2022).

## Notions liées
- [[NIST Cybersecurity Framework]]
- [[NIS2]]
- [[RGPD]]
- [[Défense en profondeur]]
- [[RSSI - CISO]]
- [[Système d'Information (SI)]]
- [[Tableau de Bord DSI]]
- [[Qualité logicielle — normes et modèles]]
- [[SIEM]]
