---
type: notion
thèmes:
  - Big DATA
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Normes ISO liées aux données

![[N — Normes ISO liées aux données.mp3]]
## En bref
> **Définition** : Plusieurs normes ISO encadrent spécifiquement la protection des données personnelles et des données dans le cloud, en complément de l'ISO 27001 (SMSI généraliste). L'**ISO 27701** (2019) étend le SMSI de l'ISO 27001 à la gestion de la protection des données personnelles (PIMS — Privacy Information Management System) et s'articule directement avec le RGPD. L'**ISO 27018** (2019) définit un code de conduite pour la protection des données personnelles dans le cloud public. L'**ISO 27040** (2015, révisée 2024) fournit des lignes directrices pour la sécurité du stockage des données. Ces normes permettent aux organisations de démontrer leur conformité de manière certifiable et internationale.
> **Pourquoi c'est important** : Dans un contexte Big Data et cloud, ces normes fournissent un cadre technique et organisationnel auditable pour la protection des données. L'ISO 27701 facilite la conformité RGPD (accountability, article 25, article 32) et peut servir de base à une certification article 42 RGPD. L'ISO 27018 est particulièrement utilisée par les grands fournisseurs cloud (AWS, Azure, Google Cloud) pour démontrer leur engagement sur la protection des données personnelles hébergées.
> **Chiffres clés** :
> - ISO 27701 : publiée en août 2019, première norme internationale sur le PIMS (Privacy Information Management System), déjà adoptée par des milliers d'organisations mondiales.
> - ISO 27018 : adoptée par AWS, Microsoft Azure et Google Cloud comme engagement contractuel envers leurs clients dans leurs DPA (Data Processing Agreements).
> - ISO 27040 : révisée en 2024 pour intégrer les nouveaux contextes (cloud, NVMe, stockage défini par logiciel), couvrant aussi bien les supports physiques que le stockage cloud.

## Approfondir

### Fonctionnement

**ISO/IEC 27701:2019 — Privacy Information Management System (PIMS)**

Extension de l'ISO 27001 et de l'ISO 27002, ajoutant des contrôles spécifiques à la protection des données personnelles. Elle fournit un cadre applicable aussi bien pour le **responsable de traitement** (Controller) que pour le **sous-traitant** (Processor) au sens du RGPD.

Structure :
- Étend les exigences de l'ISO 27001 (système de management) avec des exigences PIMS supplémentaires.
- Étend les contrôles de l'ISO 27002 (mesures de sécurité) avec des contrôles privacy spécifiques (droits des personnes, consentement, minimisation, transferts).
- Annexes informatives faisant le mapping avec le RGPD, ISO 29100 (cadre privacy), et d'autres réglementations.

Articulaton avec le RGPD :
- L'Annexe D de l'ISO 27701 fait un mapping explicite entre les contrôles de la norme et les articles du RGPD.
- Une organisation certifiée ISO 27701 peut utiliser ce certificat comme élément de preuve de conformité RGPD (article 5(2) — accountability), sans que cela équivaille à une certification RGPD formelle.
- La CNIL reconnaît l'ISO 27701 comme un cadre de référence pertinent pour structurer la gouvernance privacy.

Certification : l'ISO 27701 se certifie en combinaison avec l'ISO 27001 (pas de certification ISO 27701 autonome). L'audit de certification est réalisé par un organisme accrédité (COFRAC en France).

**ISO/IEC 27018:2019 — Code de conduite pour la protection des données personnelles dans le cloud**

Norme spécifiquement conçue pour les **fournisseurs de services cloud** traitant des données personnelles pour le compte de clients (rôle de sous-traitant/Processor).

Principes clés :
- **Consentement** : les données personnelles ne sont pas utilisées à des fins publicitaires sans le consentement du client.
- **Contrôle** : le client conserve le contrôle sur ses données ; le fournisseur cloud ne peut pas les utiliser pour son propre compte.
- **Transparence** : le fournisseur cloud publie ses politiques de traitement et est transparent sur les sous-traitants utilisés.
- **Communication des violations** : le fournisseur notifie le client de toute violation de données personnelles.
- **Retour des données** : le fournisseur restitue ou supprime les données à la fin du contrat.
- **Divulgation aux autorités** : le fournisseur ne divulgue pas les données aux autorités sans informer le client (sauf interdiction légale — CLOUD Act).

Certification ISO 27018 : certifiés — AWS (depuis 2015), Microsoft Azure (depuis 2014), Google Cloud (depuis 2015), IBM Cloud, Oracle Cloud. Elle est souvent mentionnée dans les DPA (Data Processing Agreements) comme garantie contractuelle.

Limites : l'ISO 27018 ne protège pas contre le CLOUD Act (un opérateur américain certifié ISO 27018 peut toujours être contraint de divulguer des données par les autorités américaines).

**ISO/IEC 27040:2015 (révisée 2024) — Sécurité du stockage**

Norme de référence pour la sécurité des dispositifs et systèmes de stockage des données. Couvre tous les types de stockage : DAS (Direct Attached Storage), NAS (Network Attached Storage), SAN (Storage Area Network), stockage cloud, stockage défini par logiciel (SDS), stockage sur bande.

Domaines couverts :
- **Classification des données** selon leur sensibilité et définition des mesures de protection correspondantes.
- **Contrôles de sécurité** : chiffrement au repos, contrôle d'accès, intégrité des données, journalisation, gestion des médias amovibles.
- **Sanitisation des supports** (data sanitization) : procédures de suppression sécurisée avant réutilisation ou destruction des supports (NIST SP 800-88 comme référence complémentaire).
- **Sauvegarde et récupération** : exigences de sécurité pour les sauvegardes (chiffrement des backups, test de restauration, stockage hors site).
- **Stockage cloud** : sécurité spécifique du stockage en tant que service (STaaS), contrôles de la chaîne d'approvisionnement.

Révision 2024 : intégration du stockage NVMe (NVMe-oF, NVMe over Fabrics), du stockage distribué (Ceph, HDFS) et des exigences de sécurité pour le stockage dans les environnements conteneurisés (Kubernetes Persistent Volumes).

**Autres normes ISO pertinentes pour les données**

| Norme | Objet |
|-------|-------|
| ISO/IEC 29100:2011 (rév. 2024) | Cadre de protection de la vie privée (Privacy Framework) — terminologie et principes de haut niveau |
| ISO/IEC 29101:2013 | Architecture de référence pour la protection de la vie privée |
| ISO/IEC 29134:2017 | Lignes directrices pour l'évaluation d'impact sur la vie privée (équivalent au DPIA RGPD) |
| ISO/IEC 29151:2017 | Code de conduite pour la protection des données personnelles (contrôles complémentaires à 27002) |
| ISO 31700:2023 | Privacy by Design pour les produits de consommation |
| ISO/IEC 27001:2022 | SMSI (Système de Management de la Sécurité de l'Information) — base de toutes les extensions ISO 27xxx |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Démonstration auditable de la conformité (accountability RGPD) | Coût de certification élevé (audit, consultants, maintien) |
| Reconnaissance internationale (hors UE) | La certification ne garantit pas la conformité légale RGPD |
| Cadre structuré pour la gouvernance des données | Complexité d'implémentation pour les petites structures |
| Exigence fréquente dans les appels d'offres (cloud, DPA) | ISO 27018 ne protège pas contre le CLOUD Act |
| ISO 27701 : mapping RGPD facilite l'articulation droit/technique | Nécessite une ISO 27001 déjà en place (prérequis pour 27701) |
| ISO 27040 : couvre des sujets souvent négligés (sanitisation, backup chiffré) | Norme 27040 révisée en 2024 — mises à jour des systèmes requises |

### Acteurs et solutions du marché

- **Fournisseurs cloud certifiés ISO 27018** : AWS, Microsoft Azure, Google Cloud, IBM Cloud, Oracle Cloud Infrastructure
- **Éditeurs de SMSI/PIMS** : OneTrust (module ISO 27701), Vanta, Drata, Tugboat Logic — automatisation de la conformité ISO
- **Organismes de certification accrédités (France)** : Bureau Veritas, AFNOR Certification, SGS, BSI Group — accrédités COFRAC pour ISO 27001/27701
- **Outils de sanitisation des supports** : Blancco, Ontrack Eraser (conformité ISO 27040 pour la suppression sécurisée)
- **Références complémentaires** : NIST SP 800-88 (sanitisation des supports), NIST SP 800-209 (sécurité du stockage) — souvent utilisés conjointement avec l'ISO 27040

### Cas d'usage concrets

1. **DPA avec un fournisseur cloud (ISO 27018)** : une entreprise française signe un DPA avec AWS pour l'hébergement de données clients. AWS mentionne sa certification ISO 27018 comme garantie que les données ne seront pas utilisées à des fins publicitaires et que les violations seront notifiées. La DSI utilise ce certificat comme élément de diligence raisonnable dans son registre des sous-traitants (article 28 RGPD).

2. **Certification ISO 27701 et conformité RGPD** : une société de traitement de la paie (sous-traitant au sens RGPD) obtient la certification ISO 27701. Cette certification lui permet de démontrer à ses clients que son PIMS est aligné sur le RGPD, de remporter des appels d'offres nécessitant des garanties de conformité privacy, et de réduire la charge des questionnaires de due diligence de ses clients.

3. **Plan de sanitisation des supports (ISO 27040)** : une banque renouvelle son parc de serveurs de stockage. Avant le retour des anciens serveurs au constructeur, un plan de sanitisation conforme à l'ISO 27040 est appliqué : écrasement multi-passes (DoD 5220.22-M) pour les disques HDD, destruction physique pour les SSD NVMe (effacement cryptographique insuffisant sur certains modèles). Certificats de destruction délivrés par un prestataire accrédité.

4. **Évaluation d'impact privacy (ISO 29134 / DPIA)** : une DSI utilise les lignes directrices ISO 29134 pour structurer ses DPIA internes. La méthode ISO 29134 s'articule avec les exigences de l'article 35 RGPD et fournit un cadre d'évaluation des risques plus précis que le seul guide CNIL. Le rapport DPIA suit la structure ISO 29134 et est soumis au DPO.

### Chiffres et tendances

- ISO 27001 : plus de 70 000 certifications mondiales en 2022 (ISO Survey), en croissance de 20 % par rapport à 2021.
- ISO 27701 : première norme ISO sur la privacy à connaître une adoption aussi rapide — plusieurs milliers d'organisations certifiées en 3 ans.
- AWS est certifié ISO 27018 depuis 2015 et maintient la certification pour plus de 100 services dans toutes ses régions mondiales.
- La révision 2022 de l'ISO 27001 a renforcé l'alignement avec l'ISO 27701 et intégré de nouveaux contrôles (threat intelligence, sécurité cloud, gestion des identités).
- L'ENISA recommande l'ISO 27701 comme cadre de référence pour la conformité RGPD des sous-traitants dans ses lignes directrices sur les mesures techniques et organisationnelles.

## Flashcards
#flashcards/Big_DATA/Normes_ISO_liées_aux_données #flashcards/Cloud_et_Virtualisation/Normes_ISO_liées_aux_données

Qu'est-ce que l'ISO 27701 et quel est son prérequis ? :: Norme internationale (2019) définissant un système de management de la protection des données personnelles (PIMS), extension de l'ISO 27001. Son prérequis est d'avoir une ISO 27001 en place — la certification ISO 27701 se réalise toujours conjointement avec ISO 27001.

Comment l'ISO 27701 s'articule-t-elle avec le RGPD ? :: L'Annexe D de l'ISO 27701 fait un mapping explicite entre les contrôles de la norme et les articles du RGPD. Une certification ISO 27701 constitue un élément de preuve d'accountability au sens de l'article 5(2) RGPD, sans équivaloir à une certification RGPD formelle.

À qui s'adresse l'ISO 27018 et quels sont ses principes clés ? :: Aux fournisseurs de services cloud traitant des données personnelles pour le compte de clients (rôle de Processor RGPD). Principes : pas d'utilisation des données à des fins publicitaires, contrôle par le client, transparence, notification des violations, restitution des données en fin de contrat.

Quels sont les 4 grands domaines couverts par l'ISO 27040 ? :: Classification des données et contrôles correspondants, contrôles de sécurité (chiffrement au repos, contrôle d'accès, journalisation), sanitisation des supports (suppression sécurisée), sécurité des sauvegardes.

Quelle est la limite principale de la certification ISO 27018 pour les fournisseurs cloud américains ? :: L'ISO 27018 ne protège pas contre le CLOUD Act : un fournisseur américain certifié ISO 27018 peut toujours être contraint par les autorités américaines de divulguer des données sans en informer le client (en cas de gag order).

Qu'est-ce que la sanitisation des supports selon l'ISO 27040 et pourquoi est-elle importante ? :: La sanitisation est la suppression sécurisée et irréversible des données d'un support avant sa réutilisation ou destruction, pour éviter la récupération des données par un tiers. L'ISO 27040 définit les méthodes acceptables selon le type de support (écrasement, dégaussage, destruction physique, effacement cryptographique).

Quelle norme ISO encadre spécifiquement l'évaluation d'impact sur la vie privée (PIA/DPIA) ? :: L'ISO/IEC 29134:2017 fournit des lignes directrices pour la réalisation des évaluations d'impact sur la vie privée (PIA), alignées avec les exigences du DPIA de l'article 35 RGPD.

## Sources

- ISO/IEC 27701:2019 — https://www.iso.org/standard/71670.html
- ISO/IEC 27018:2019 — https://www.iso.org/standard/76559.html
- ISO/IEC 27040:2015 (révisée 2024) — https://www.iso.org/standard/44404.html
- ISO/IEC 29134:2017 (PIA) — https://www.iso.org/standard/62289.html
- ISO 31700:2023 (Privacy by Design) — https://www.iso.org/standard/84977.html
- CNIL — reconnaissance de l'ISO 27701 : https://www.cnil.fr/
- ENISA — recommandations sur les mesures techniques et organisationnelles (article 32 RGPD)
- AWS — liste des certifications et conformité : https://aws.amazon.com/compliance/iso-certified/
- NIST SP 800-88 Rev. 1, "Guidelines for Media Sanitization", 2014

## Notions liées

- [[ISO 27001 - 27002]]
- [[RGPD]]
- [[Privacy by Design]]
- [[CLOUD Act et transferts de données]]
- [[Certifications et normes cloud]]
- [[Data Lifecycle Management]]
- [[Chiffrement et gestion des clés]]
- [[Technologies de stockage]]
