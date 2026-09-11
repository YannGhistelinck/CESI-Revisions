---
type: notion
thèmes:
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Certifications et normes cloud

## En bref
> **Définition** : Les certifications et normes cloud sont des référentiels techniques et organisationnels qui permettent aux fournisseurs cloud de démontrer leur niveau de sécurité, de conformité et de protection des données. Elles constituent des garanties contractuelles et réglementaires pour les organisations qui externalisent leurs données et services.
> **Pourquoi c'est important** : Pour une DSI, le choix d'un fournisseur cloud certifié est un prérequis légal et de gouvernance : RGPD pour les données personnelles, HDS pour les données de santé, SecNumCloud pour les données sensibles de l'État. Ces certifications réduisent les risques contractuels, facilitent les audits et démontrent la due diligence aux régulateurs.
> **Chiffres clés** :
> - 94 % des DSI considèrent la conformité cloud comme une priorité critique (IDC, 2023).
> - La certification HDS concerne plus de 300 hébergeurs en France (ANS, 2024).
> - Le coût moyen d'une non-conformité cloud est de 5,9 M$ (IBM Cost of a Data Breach, 2023).

## Approfondir

### Fonctionnement

**ISO 27017 — Sécurité des services cloud**
- Extension de l'ISO 27001 spécifique au cloud. Définit des contrôles de sécurité supplémentaires pour les fournisseurs et clients cloud.
- Couvre : séparation des environnements virtuels, gestion des actifs cloud, journalisation, suppression sécurisée des données.
- Applicable aux CSP (Cloud Service Providers) et à leurs clients.
- Obtenue par AWS, Azure, GCP, OVHcloud, Scaleway, etc.

**ISO 27018 — Protection des données personnelles dans le cloud**
- Premier standard international dédié à la protection des données à caractère personnel (PII) dans le cloud public.
- Complète ISO 27001 et 27017. Aligné avec les principes du RGPD.
- Exigences clés : consentement explicite avant utilisation des données, interdiction d'utiliser les données clients à des fins commerciales, notification des violations, transparence sur les sous-traitants.
- Obtenue par les principaux CSP mondiaux.

**CSA STAR (Security, Trust, Assurance and Registry)**
- Programme de certification de la **Cloud Security Alliance (CSA)**, organisation internationale dédiée à la sécurité cloud.
- 3 niveaux :
  - **STAR Level 1** : auto-évaluation via le questionnaire CAIQ (Consensus Assessment Initiative Questionnaire) — publique et gratuite.
  - **STAR Level 2** : audit indépendant basé sur ISO 27001 + Cloud Controls Matrix (CCM). Équivalent à une certification tierce partie.
  - **STAR Level 3** : surveillance continue (en développement).
- La **Cloud Controls Matrix (CCM)** est le référentiel de contrôles de sécurité cloud de la CSA (197 contrôles sur 17 domaines).

**SOC 2 Type II (System and Organization Controls)**
- Rapport d'audit américain (norme AICPA) évaluant les contrôles internes d'un fournisseur sur 5 critères : Sécurité, Disponibilité, Intégrité des traitements, Confidentialité, Vie privée.
- **Type I** : évaluation à un instant T. **Type II** : évaluation sur une période (6-12 mois), bien plus significatif car il démontre la permanence des contrôles.
- Très demandé par les clients américains et les grandes entreprises internationales.
- Les rapports SOC 2 Type II sont généralement confidentiels (partagés sous NDA).

**CIS Benchmarks (Center for Internet Security)**
- Référentiels de configuration sécurisée pour les systèmes et services cloud (AWS, Azure, GCP, K8s, Docker, etc.).
- Deux niveaux : **Level 1** (recommandations de base, impact opérationnel minimal) et **Level 2** (hardening renforcé, peut impacter certains usages).
- Utilisés comme base de conformité dans les audits de sécurité et les outils de CSPM (Cloud Security Posture Management) comme Wiz, Prisma Cloud, AWS Security Hub.
- Référence dans les appels d'offres pour qualifier la posture de sécurité d'un environnement cloud.

**HDS (Hébergement de Données de Santé)**
- Certification française obligatoire pour tout hébergeur traitant des données de santé à caractère personnel (dossiers patients, images médicales, etc.).
- Délivrée par des organismes accrédités (COFRAC), sur la base de l'ISO 27001 + référentiel HDS spécifique.
- Régi par l'article L.1111-8 du Code de la santé publique.
- **6 activités certifiables** : infrastructure physique, infrastructure virtuelle, infra hébergée, sauvegarde, infogérance, messagerie sécurisée.
- Titulaires en France : AWS (régions Paris), Azure (France Central), OVHcloud, Outscale, Orange Business, Atos, etc.

**SecNumCloud (ANSSI)**
- Visa de sécurité français délivré par l'ANSSI, le plus exigeant pour les données sensibles de l'État.
- Exige la souveraineté juridique (droit français, pas de loi extraterritoriale comme le CLOUD Act américain).
- En 2024, seules OVHcloud et 3DS Outscale disposent d'offres cloud qualifiées SecNumCloud.
- Obligatoire pour certains systèmes d'information de l'État (OIV, OSE, administrations sensibles).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Garantie formelle du niveau de sécurité du CSP | Coût et durée des audits (ISO 27001 : 6-18 mois, >100 k€) |
| Réduction du risque de non-conformité RGPD/NIS2 | Les certifications ne couvrent pas l'ensemble de l'offre cloud |
| Facilitation des due diligences et appels d'offres | Périmètre de certification parfois limité (zones géographiques, services) |
| Confiance des clients et partenaires | La certification ne garantit pas l'absence de failles applicatives |
| Référentiel commun pour les audits internes | Renouvellement annuel contraignant |
| Exigence légale pour HDS et SecNumCloud | Peu de fournisseurs qualifiés SecNumCloud (marché limité) |

### Acteurs et solutions du marché
| Certification | Organisme | Portée |
|--------------|-----------|--------|
| ISO 27017/27018 | ISO / AFNOR (France) | Internationale |
| CSA STAR Level 2 | Cloud Security Alliance | Internationale |
| SOC 2 Type II | AICPA | USA / Internationale |
| CIS Benchmarks | Center for Internet Security | Technique / Configuration |
| HDS | ANS + COFRAC | France (données de santé) |
| SecNumCloud | ANSSI | France (données sensibles État) |
| PCI-DSS | PCI Security Standards Council | Paiement / Internationale |
| EUCS (en cours) | ENISA | Europe (en discussion) |

### Cas d'usage concrets
1. **Hôpital public (CHU)** : pour migrer le dossier patient informatisé (DPI) vers le cloud, le CHU doit obligatoirement choisir un hébergeur certifié HDS. Il vérifiera ISO 27017, ISO 27018 et le rapport SOC 2 Type II du fournisseur pour valider la due diligence.
2. **Startup SaaS B2B** : pour signer avec des clients grandes entreprises américaines, l'éditeur fait certifier sa plateforme SOC 2 Type II, gage de maturité opérationnelle et de confiance.
3. **Ministère (OIV)** : pour héberger ses applications sensibles, il exige SecNumCloud et vérifie l'absence de flux de données vers des pays soumis au CLOUD Act, imposant OVHcloud ou Outscale.

### Chiffres et tendances
- En 2024, l'EUCS (European Union Cybersecurity Certification Scheme for Cloud Services) est en cours de finalisation par l'ENISA, avec 3 niveaux (Basic, Substantial, High). Niveau High = équivalent SecNumCloud.
- La question de la souveraineté cloud pousse 62 % des entreprises européennes à exiger des certifications locales (IDC Europe, 2023).
- Le marché CSPM (Cloud Security Posture Management), qui automatise la vérification des CIS Benchmarks, devrait atteindre 9 Md$ en 2027.
- La Commission européenne a exclu les fournisseurs non souverains de certains marchés publics sensibles depuis 2023.

## Flashcards
#flashcards
- Quelle est la différence entre ISO 27017 et ISO 27018 ? :: ISO 27017 couvre la sécurité générale des services cloud ; ISO 27018 est spécifique à la protection des données personnelles (PII) dans le cloud, aligné avec le RGPD.
- Qu'est-ce que SOC 2 Type II et en quoi diffère-t-il du Type I ? :: SOC 2 Type II est un audit sur une période de 6-12 mois démontrant la permanence des contrôles de sécurité ; le Type I n'évalue qu'un instant T, ce qui est moins significatif.
- Qu'est-ce que la certification HDS et pour qui est-elle obligatoire ? :: C'est la certification française obligatoire pour tout hébergeur traitant des données de santé à caractère personnel, délivrée par des organismes accrédités COFRAC sur base ISO 27001 + référentiel HDS.
- Qu'est-ce que SecNumCloud et qui peut l'obtenir ? :: C'est le visa de sécurité de l'ANSSI pour les données sensibles de l'État, exigeant la souveraineté juridique française. En 2024, seuls OVHcloud et 3DS Outscale l'ont obtenu.
- Qu'est-ce que la Cloud Controls Matrix (CCM) de la CSA ? :: Un référentiel de 197 contrôles de sécurité cloud sur 17 domaines, utilisé comme base pour la certification CSA STAR et les audits de sécurité cloud.
- Que sont les CIS Benchmarks et comment sont-ils utilisés ? :: Des guides de configuration sécurisée (Level 1 et 2) pour systèmes et services cloud (AWS, Azure, K8s, Docker), utilisés comme référence dans les audits et les outils CSPM.
- Qu'est-ce que l'EUCS ? :: L'European Union Cybersecurity Certification Scheme for Cloud Services, en cours de finalisation par l'ENISA, qui établira un cadre européen de certification cloud en 3 niveaux, dont le niveau High équivalent à SecNumCloud.

## Sources
- ANSSI — SecNumCloud : https://www.ssi.gouv.fr/qualification/secnumcloud/
- ANS — HDS : https://esante.gouv.fr/offres-services/hds/
- Cloud Security Alliance — CCM & STAR : https://cloudsecurityalliance.org/
- ISO 27017 : https://www.iso.org/standard/43757.html
- ISO 27018 : https://www.iso.org/standard/76559.html
- CIS Benchmarks : https://www.cisecurity.org/cis-benchmarks
- AICPA SOC 2 : https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2

## Notions liées
- [[Acteurs cloud]]
- [[ISO 27001 - 27002]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[NIS2]]
- [[Zero Trust]]
- [[Data Act]]
