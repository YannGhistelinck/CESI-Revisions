---
type: notion
thèmes:
  - Cybersécurité
  - Cloud et Virtualisation
  - Mobilité
statut: pas vu
dernière_révision: 
---

# NIS2

## En bref
> **Définition** : La directive NIS2 (Network and Information Security 2) est une directive européenne adoptée en janvier 2023 (2022/2555/UE), remplaçant la directive NIS1 de 2016. Elle élargit le champ des entités soumises à des obligations de cybersécurité et renforce significativement les exigences, notamment en matière de gouvernance, de gestion des risques et de notification des incidents.
> **Pourquoi c'est important** : NIS2 impose des obligations contraignantes à un périmètre beaucoup plus large d'organisations (estimé à 10 000 à 15 000 entités en France), avec des sanctions pouvant atteindre 10 M€ ou 2 % du CA mondial. La DSI doit piloter la mise en conformité et anticiper les exigences techniques et organisationnelles.
> **Chiffres clés** :
> - NIS1 couvrait environ 500 entités en France ; NIS2 en cible 10 000 à 15 000 (ANSSI, 2023)
> - Sanctions pour les entités essentielles : jusqu'à 10 M€ ou 2 % du CA mondial annuel
> - Sanctions pour les entités importantes : jusqu'à 7 M€ ou 1,4 % du CA mondial annuel
> - Délai de notification d'un incident majeur : 24 heures pour l'alerte précoce, 72 heures pour la notification initiale

## Approfondir

### Fonctionnement

**Champ d'application — deux catégories d'entités :**

- **Entités Essentielles (EE)** : Secteurs hautement critiques. Inclut énergie, transports, banque, infrastructures des marchés financiers, santé, eau potable, eaux usées, infrastructure numérique (IXP, DNS, TLD, datacenters, cloud, réseaux de communications électroniques), administration publique, espace.
  - Seuil : grandes entreprises (≥ 250 employés OU CA ≥ 50 M€ ET bilan ≥ 43 M€) dans ces secteurs.

- **Entités Importantes (EI)** : Secteurs critiques. Inclut services postaux, gestion des déchets, chimie, alimentation, fabrication (dispositifs médicaux, équipements électroniques, véhicules à moteur, etc.), fournisseurs numériques (places de marché en ligne, moteurs de recherche, réseaux sociaux).
  - Seuil : entreprises moyennes (≥ 50 employés OU CA/bilan ≥ 10 M€) dans ces secteurs.

**Obligations clés :**

1. **Gouvernance** : La direction (PDG, DG) est personnellement responsable de la mise en conformité. Formation obligatoire des dirigeants à la cybersécurité.

2. **Gestion des risques** : Mise en place d'une politique de sécurité formalisée, analyse des risques, mesures techniques et organisationnelles proportionnées.

3. **Mesures minimales obligatoires** (article 21) :
   - Politique de sécurité des systèmes d'information
   - Gestion des incidents
   - Continuité des activités (PCA/PRA, sauvegardes)
   - Sécurité de la chaîne d'approvisionnement (supply chain)
   - Sécurité dans l'acquisition, le développement et la maintenance des SI
   - Politiques et procédures pour évaluer l'efficacité des mesures
   - Formation et sensibilisation à la cybersécurité
   - Cryptographie et chiffrement
   - Sécurité des ressources humaines, contrôle d'accès, gestion des actifs
   - Authentification multifacteur (MFA) et communications sécurisées

4. **Notification des incidents** :
   - Alerte précoce : dans les 24 heures suivant la prise de connaissance d'un incident significatif
   - Notification initiale : dans les 72 heures
   - Rapport final : dans le mois suivant

5. **Sécurité de la chaîne d'approvisionnement** : Obligation d'évaluer les risques liés aux fournisseurs et prestataires numériques.

**Transposition en France :**
La directive devait être transposée avant le 17 octobre 2024. La France a procédé à cette transposition via une loi et des règlements spécifiques, avec l'ANSSI comme autorité compétente nationale.

**Différences NIS1 vs NIS2 :**
| NIS1 (2016) | NIS2 (2023) |
|-------------|-------------|
| ~500 entités en France | ~10 000-15 000 entités |
| OIV uniquement | EE + EI (périmètre élargi) |
| Désignation par l'État | Auto-identification obligatoire |
| Sanctions limitées | Jusqu'à 10 M€ ou 2 % CA |
| Responsabilité direction absente | Responsabilité personnelle des dirigeants |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Harmonisation européenne de la cybersécurité | Charge de conformité importante pour les PME/ETI |
| Élévation du niveau de sécurité global | Coûts de mise en conformité élevés |
| Responsabilisation des dirigeants | Complexité du périmètre d'application |
| Sécurisation de la chaîne d'approvisionnement | Risque de sanction sur des délais de notification courts |
| Coopération renforcée entre États membres (EU-CyCLONe) | Manque de ressources expertes sur le marché |

### Acteurs et solutions du marché
- **Autorité nationale** : ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) — autorité NIS2 en France
- **Réseau européen** : ENISA (Agence de l'Union européenne pour la cybersécurité), réseau des CSIRT nationaux
- **Cabinets de conseil en conformité NIS2** : Wavestone, Deloitte Cyber, PwC, Synetis, Intrinsec
- **Plateforme de notification** : portail ANSSI (en cours de déploiement pour les déclarations NIS2)
- **Outils de gestion des risques** : EBIOS Risk Manager (méthode ANSSI), ISO 27005

### Cas d'usage concrets
1. **Hôpital public (entité essentielle)** : Un CHU doit désormais notifier l'ANSSI dans les 24 heures en cas de ransomware, désigner un responsable cybersécurité, et s'assurer que ses fournisseurs de logiciels médicaux respectent des exigences de sécurité minimales.
2. **ESN (entité importante)** : Une entreprise de services numériques de 300 personnes, prestataire de services cloud pour des administrations, entre dans le périmètre NIS2. Elle doit mettre en place un SMSI, réaliser des audits réguliers et former sa direction.
3. **Industriel (chaîne d'approvisionnement)** : Un fabricant automobile (entité importante) doit évaluer et documenter les risques cyber liés à ses équipementiers et sous-traitants, et imposer des exigences contractuelles de cybersécurité.

### Chiffres et tendances
- NIS2 s'applique à 18 secteurs (vs 7 pour NIS1) et couvre pour la première fois les administrations publiques
- L'ANSSI estime que 60 % des entités NIS2 n'ont pas encore engagé leur démarche de conformité (2024)
- Le marché des services de conseil NIS2 est estimé à plusieurs centaines de millions d'euros en France
- NIS2 est complémentaire avec DORA (secteur financier), CRA (Cyber Resilience Act pour les produits connectés) et RGPD

## Flashcards
#flashcards
Quelle est la différence entre une entité essentielle et une entité importante dans NIS2 ? :: Les entités essentielles (EE) opèrent dans des secteurs hautement critiques (énergie, santé, banque, infrastructure numérique) et sont soumises à une supervision proactive. Les entités importantes (EI) couvrent des secteurs critiques élargis (chimie, alimentation, fournisseurs numériques) et font l'objet d'une supervision réactive.

Quels sont les délais de notification d'un incident NIS2 ? :: Alerte précoce dans les 24 heures, notification initiale dans les 72 heures, rapport final dans le mois suivant la prise de connaissance de l'incident.

Quelles sont les sanctions maximales prévues par NIS2 ? :: Pour les entités essentielles : 10 M€ ou 2 % du CA mondial. Pour les entités importantes : 7 M€ ou 1,4 % du CA mondial.

Quelle est la nouveauté majeure de NIS2 concernant les dirigeants ? :: NIS2 instaure la responsabilité personnelle des dirigeants en matière de cybersécurité. Ils doivent approuver les mesures de gestion des risques et sont tenus de suivre des formations à la cybersécurité.

Quels sont les 3 points clés de l'article 21 de NIS2 ? :: Mesures de gestion des risques cyber (politique de sécurité, continuité, supply chain), MFA obligatoire, et notification des incidents dans les délais prescrits.

Quelle autorité française est compétente pour NIS2 ? :: L'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information), qui est l'autorité nationale compétente et le point de contact unique pour NIS2 en France.

En quoi NIS2 change-t-elle la gestion de la supply chain ? :: Elle oblige les entités à évaluer les risques cyber liés à leurs fournisseurs et sous-traitants, et à imposer des exigences contractuelles de cybersécurité, élargissant ainsi la responsabilité au-delà du périmètre direct de l'organisation.

## Sources
- Directive (UE) 2022/2555 du Parlement européen et du Conseil (NIS2) — 27 décembre 2022
- ANSSI — Guide de mise en conformité NIS2 (anssi.gouv.fr)
- ENISA — NIS2 Directive Overview
- Wavestone — Baromètre de la cybersécurité des grandes entreprises 2023
- Journal officiel de l'Union européenne — L 333/80

## Notions liées
- [[ISO 27001 - 27002]]
- [[PCA - PRA]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[Authentification et gestion des accès (IAM)]]
- [[NIST Cybersecurity Framework]]
- [[Cyber-assurance]]
