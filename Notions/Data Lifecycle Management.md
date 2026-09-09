---
type: notion
thèmes:
  - SI et environnement
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Data Lifecycle Management

## En bref
> **Définition** : Le Data Lifecycle Management (DLM) désigne l'ensemble des politiques, processus et technologies permettant de gérer les données tout au long de leur cycle de vie, depuis leur création jusqu'à leur destruction définitive. Il inclut la classification des données selon leur "température" (hot/warm/cold), les règles de rétention et les politiques d'archivage.
> **Pourquoi c'est important** : Sans DLM, les entreprises accumulent du "dark data" (données inutilisées mais stockées à coût plein), ce qui augmente inutilement la consommation électrique, les risques légaux (RGPD) et les coûts. Le DLM est le levier le plus opérationnel pour réduire l'empreinte du stockage.
> **Chiffres clés** :
> - **55 % des données** stockées en entreprise sont du dark data (Gartner)
> - **90 % des données** ne sont plus consultées après 90 jours de création (Veritas)
> - Supprimer 1 To de dark data évite l'émission d'environ **1,5 tonne de CO₂e** sur 3 ans (estimation Verdantix)

## Approfondir

### Fonctionnement

#### Le cycle de vie des données
Les données passent par différentes phases avec des besoins d'accès décroissants :

```
Création → Utilisation active → Utilisation rare → Archivage → Destruction
   (hot)         (hot/warm)          (warm/cold)      (cold)     (purge)
```

#### Classification par "température"
| Catégorie | Définition | Fréquence d'accès | Support adapté |
|-----------|------------|-------------------|----------------|
| **Hot data** | Données en production, actives | Quotidienne à temps réel | SSD NVMe, RAM |
| **Warm data** | Données récentes peu consultées | Hebdomadaire à mensuelle | HDD, SSD SATA |
| **Cold data** | Données rarement accédées | Annuelle ou moins | LTO, stockage objet froid |
| **Frozen data** | Archives à conservation légale | Quasi jamais | LTO robotique, S3 Glacier Deep Archive |

#### Dark Data
Les dark data sont des données collectées, stockées mais jamais (ou quasiment jamais) utilisées. Sources fréquentes :
- Logs applicatifs non analysés
- Emails et pièces jointes accumulés
- Données de capteurs IoT brutes non traitées
- Fichiers dupliqués sur des partages réseau
- Anciennes versions de documents

Impact : stockées sur des supports énergivores (SAN SSD/HDD actifs), elles génèrent une empreinte carbone sans valeur ajoutée.

#### Data Retention (rétention des données)
Politique définissant combien de temps chaque type de donnée doit être conservé, en conformité avec :
- **RGPD** : données personnelles conservées uniquement le temps nécessaire à la finalité
- **Obligations légales françaises** :
  - Contrats commerciaux : 5 ans
  - Documents comptables : 10 ans
  - Données de paie : 5 ans
  - Emails professionnels : 5 ans recommandés

Une politique de rétention structurée déclenche automatiquement la purge ou l'archivage à l'échéance, évitant l'accumulation de dark data.

#### Archivage
L'archivage est distinct de la sauvegarde :
- **Sauvegarde** : copie de données actives pour restauration en cas de sinistre (données vivantes)
- **Archivage** : déplacement de données inactives vers un stockage moins coûteux et moins énergivore pour conservation longue durée (données mortes pour l'activité)

Bonnes pratiques d'archivage :
- Stratégie **3-2-1** : 3 copies, sur 2 supports différents, dont 1 hors site
- Vérification d'intégrité régulière (checksum SHA-256)
- Documentation des formats de fichier pour la lisibilité à long terme

#### Outils DLM
- **Microsoft Information Protection** : classification et étiquetage automatique des données
- **Varonis** : cartographie du dark data, détection des données sensibles orphelines
- **Veritas Data Insight** : analyse de l'utilisation effective des données
- **Commvault** : gestion unifiée du cycle de vie (sauvegarde, archivage, restauration)
- **IBM Spectrum Protect** : tiering automatique et archivage sur LTO

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Réduction significative du volume de stockage actif | Classification initiale coûteuse en temps et expertise |
| Conformité RGPD et obligations légales assurée | Risque de supprimer des données encore utiles si mal classifiées |
| Réduction des coûts de stockage et d'énergie | Résistance culturelle ("garder au cas où") |
| Amélioration de la qualité et pertinence du patrimoine data | Outils DLM coûteux à déployer et maintenir |
| Réduction de la surface d'attaque (moins de données = moins de risques) | Nécessite une gouvernance data mature |

### Acteurs et solutions du marché
- **Veritas** : Data Insight, Enterprise Vault, NetBackup (DLM intégré)
- **Commvault** : plateforme unifiée sauvegarde + archivage + cloud
- **Microsoft** : Azure Information Protection, Microsoft Purview
- **IBM** : Spectrum Protect, Watson Knowledge Catalog
- **Aparavi** : spécialisé analyse et nettoyage du dark data
- **Atempo** : solution française de gestion du cycle de vie des données

### Cas d'usage concrets
1. **Société Générale** a déployé une politique de rétention automatisée sur ses systèmes de messagerie, réduisant son volume d'emails stockés de 40 % en 18 mois, avec un impact direct sur sa facture de stockage et son empreinte carbone.
2. **CHU de Bordeaux** a réalisé un audit de son dark data et identifié que 60 % de son stockage SAN hébergeait des données non accédées depuis plus de 3 ans. Migration vers LTO avec économie de 200 kW de puissance installée.
3. **Renault** utilise Microsoft Purview pour classifier automatiquement ses données selon leur sensibilité et déclencher les politiques de rétention, en conformité avec le RGPD et les obligations secteur automobile (traçabilité 10 ans).

### Chiffres et tendances
- Le marché du DLM devrait atteindre **5,3 Md$ en 2027** (MarketsandMarkets)
- **80 % des entreprises** déclarent ne pas avoir de politique formelle de data lifecycle (IDG)
- Réduire le dark data de 50 % peut représenter **30 à 40 % d'économies** sur la facture de stockage
- La mise en conformité RGPD est aujourd'hui le principal driver d'adoption des politiques DLM en Europe

## Flashcards
#flashcards/SI_et_environnement/Data_Lifecycle_Management #flashcards/Big_DATA/Data_Lifecycle_Management

Quelle est la différence entre sauvegarde et archivage ? :: La sauvegarde protège les données actives contre les sinistres (restauration rapide). L'archivage déplace les données inactives vers un stockage moins coûteux pour conservation long terme. Objectifs et supports différents.

Qu'est-ce que le dark data ? :: Données collectées et stockées mais jamais (ou quasiment jamais) utilisées (logs, emails, doublons, capteurs IoT bruts). Elles génèrent une empreinte carbone sans valeur ajoutée.

Quelle est la règle de rétention des documents comptables en France ? :: 10 ans (Code de commerce). Les contrats commerciaux : 5 ans. Les données personnelles : durée nécessaire à la finalité (RGPD).

Comment définit-on le hot, warm et cold data ? :: Hot = données actives, accédées quotidiennement (SSD). Warm = données peu consultées, accès hebdomadaire/mensuel (HDD). Cold = données rarement accédées, archivage annuel (LTO, S3 Glacier).

Quelle est la stratégie de sauvegarde de référence ? :: La règle 3-2-1 : 3 copies des données, sur 2 supports différents, dont 1 copie hors site.

Quel est l'impact du dark data sur l'empreinte carbone ? :: Des données stockées sur des supports actifs (HDD/SSD sous tension) consomment de l'énergie en permanence même inutilisées. Supprimer 1 To de dark data peut éviter ~1,5 tCO₂e sur 3 ans.

Quel texte réglementaire oblige les entreprises à limiter la durée de conservation des données personnelles ? :: Le RGPD (Règlement Général sur la Protection des Données, 2018), qui impose le principe de limitation de la conservation (article 5.1.e).

## Sources
- RGPD – Règlement UE 2016/679 : https://eur-lex.europa.eu
- CNIL – Guide pratique conservation des données : https://www.cnil.fr
- Gartner – "The State of Dark Data" : https://www.gartner.com
- Veritas – "2023 Data Management Report" : https://www.veritas.com
- GreenIT.fr – Sobriété numérique et gestion des données : https://www.greenit.fr
- ADEME – "La face cachée du numérique" : https://www.ademe.fr

## Notions liées
- [[Technologies de stockage]]
- [[Indicateurs environnementaux du SI]]
- [[Analyse du Cycle de Vie (ACV)]]
- [[Infrastructure des datacenters]]
