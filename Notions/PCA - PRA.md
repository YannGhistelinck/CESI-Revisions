---
type: notion
thèmes:
  - Cybersécurité
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# PCA - PRA

## En bref
> **Définition** : Le Plan de Continuité d'Activité (PCA) définit l'ensemble des dispositions permettant à une organisation de maintenir ou de reprendre ses activités critiques en cas de sinistre ou d'incident majeur. Le Plan de Reprise d'Activité (PRA) est le volet informatique du PCA : il décrit les procédures pour restaurer les systèmes d'information après une interruption.
> **Pourquoi c'est important** : Pour une DSI, l'absence de PCA/PRA expose l'organisation à des pertes financières considérables, à des obligations réglementaires non respectées (NIS2, RGPD) et à une atteinte irrémédiable à sa réputation. Les cyberattaques (ransomwares notamment) rendent ces plans indispensables.
> **Chiffres clés** :
> - 60 % des PME victimes d'une cyberattaque majeure mettent la clé sous la porte dans les 18 mois (CESIN, 2023)
> - Le coût moyen d'un incident de sécurité pour une entreprise française est de 59 000 € (Hiscox, 2023)
> - Seulement 40 % des entreprises françaises disposent d'un PCA formalisé et testé (Wavestone, 2022)

## Approfondir

### Fonctionnement

**Concepts clés :**

- **BIA (Business Impact Analysis)** : Analyse d'Impact sur les Activités. Étape fondatrice qui identifie les processus critiques, leurs dépendances et les impacts d'une interruption (financiers, réglementaires, réputationnels). Elle permet de définir les priorités de reprise.
- **RTO (Recovery Time Objective)** : Durée maximale d'interruption tolérable. Exemple : "Le SI doit être opérationnel sous 4 heures."
- **RPO (Recovery Point Objective)** : Perte de données maximale acceptable, exprimée en temps. Exemple : "On accepte de perdre au maximum 1 heure de transactions."
- **MTPD (Maximum Tolerable Period of Disruption)** : Durée maximale au-delà de laquelle l'activité ne peut plus être reprise sans conséquences irréversibles.
- **PCA (Plan de Continuité d'Activité / BCP - Business Continuity Plan)** : Plan global couvrant toutes les ressources (humaines, locaux, IT, communication). Vise à maintenir un niveau de service minimal pendant la crise.
- **PRA (Plan de Reprise d'Activité / DRP - Disaster Recovery Plan)** : Sous-ensemble du PCA, centré sur le SI. Décrit les procédures techniques de restauration des systèmes, données et applications.

**Cycle de vie d'un PCA/PRA :**
1. Analyse des risques et BIA
2. Définition des RTO/RPO/MTPD par processus
3. Rédaction des procédures de continuité et de reprise
4. Tests et exercices (simulation, test de basculement)
5. Maintien en condition opérationnelle (MCO) et révision annuelle

**Stratégies techniques de PRA :**
- **Sauvegarde/restauration classique** : RPO élevé (plusieurs heures), RTO long. Solution économique.
- **Site de repli à chaud (hot site)** : Environnement miroir opérationnel en temps réel. RTO < 1 heure, RPO quasi nul. Coût élevé.
- **Site de repli à froid (cold site)** : Infrastructure disponible mais à configurer. RTO > 24 heures.
- **PRA cloud** : Réplication vers un cloud public (AWS, Azure, OVHcloud). Flexibilité et coût maîtrisé.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction du temps d'arrêt et des pertes financières | Coût de mise en place et de maintien élevé |
| Conformité réglementaire (NIS2, ISO 22301, DORA) | Complexité organisationnelle |
| Résilience face aux cyberattaques (ransomware) | Risque de plans obsolètes si non maintenus |
| Confiance des clients et partenaires | Nécessite des tests réguliers perturbateurs |
| Réduction du risque assurantiel | Mobilisation importante des équipes IT et métier |

### Acteurs et solutions du marché
- **Éditeurs de solutions de PRA** : Zerto, Veeam, Commvault, IBM Resiliency, VMware Site Recovery
- **Cloud providers avec DRaaS** : AWS Elastic Disaster Recovery, Azure Site Recovery, OVHcloud Disaster Recovery
- **Cabinets de conseil spécialisés** : Wavestone, Deloitte, Synetis
- **Normes de référence** : ISO 22301 (continuité d'activité), ISO 27001 (sécurité de l'information)

### Cas d'usage concrets
1. **Attaque ransomware sur un hôpital** : En 2021, le CH de Dax a subi une attaque par ransomware paralysant tout le SI. L'absence d'un PRA testé a allongé la durée de reprise à plusieurs semaines, forçant un retour au papier pour les soins.
2. **Sinistre datacenter** : Un incendie partiel d'un datacenter OVHcloud à Strasbourg (mars 2021) a mis hors service des milliers de serveurs. Les clients disposant d'un PRA avec réplication sur un autre site ont repris en quelques heures, les autres en plusieurs jours ou semaines.
3. **Pandémie COVID-19** : Les organisations ayant un PCA incluant le télétravail ont pu basculer en moins de 48 heures, là où d'autres ont mis plusieurs semaines à s'adapter.

### Chiffres et tendances
- Le marché mondial du DRaaS (Disaster Recovery as a Service) atteindra 23,3 Mds $ en 2027 (Markets and Markets)
- 93 % des entreprises sans PRA ferment définitivement dans l'année suivant une perte de données majeure (Veeam, 2022)
- La directive DORA (Digital Operational Resilience Act), applicable depuis janvier 2025, impose des PCA/PRA stricts au secteur financier européen
- NIS2 (transposée en France fin 2024) impose des obligations similaires aux entités essentielles et importantes

## Flashcards
#flashcards
PCA vs PRA :: Le PCA couvre la continuité globale de l'activité (humains, locaux, IT) ; le PRA est le volet IT du PCA, focalisé sur la restauration des systèmes d'information.

Qu'est-ce que le RTO ? :: Recovery Time Objective : durée maximale d'interruption tolérée. Ex : les systèmes doivent être opérationnels dans les 4 heures.

Qu'est-ce que le RPO ? :: Recovery Point Objective : perte de données maximale acceptable, exprimée en temps. Ex : on tolère de perdre au maximum 1 heure de données.

Qu'est-ce que le BIA ? :: Business Impact Analysis : analyse qui identifie les processus critiques et l'impact financier, opérationnel et réglementaire de leur interruption. C'est l'étape fondatrice du PCA.

Qu'est-ce que le MTPD ? :: Maximum Tolerable Period of Disruption : durée maximale au-delà de laquelle l'activité ne peut plus être reprise sans conséquences irréversibles pour l'organisation.

Quels sont les types de sites de repli ? :: Hot site (miroir temps réel, RTO < 1h), warm site (partiellement configuré, RTO quelques heures), cold site (infrastructure disponible mais à configurer, RTO > 24h).

Quelle norme internationale encadre la continuité d'activité ? :: L'ISO 22301 définit les exigences pour un Système de Management de la Continuité d'Activité (SMCA). Elle est complémentaire à l'ISO 27001 pour la sécurité de l'information.

## Sources
- ANSSI — Guide de l'hygiène informatique et recommandations PCA
- ISO 22301:2019 — Sécurité et résilience — Systèmes de management de la continuité d'activité
- Veeam Data Protection Report 2023
- Wavestone — Panorama de la Cyber 2023
- CESIN — Baromètre annuel de la cybersécurité des entreprises françaises 2023
- Hiscox Cyber Readiness Report 2023
- Règlement DORA (Digital Operational Resilience Act) — UE 2022/2554

## Notions liées
- [[NIS2]]
- [[ISO 27001 - 27002]]
- [[Cyber-assurance]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[NIST Cybersecurity Framework]]
