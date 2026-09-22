---
type: notion
thèmes:
  - Optimisation du SI
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Tableau de Bord DSI

![[N — Tableau de Bord DSI.mp3]]
## En bref
> **Définition** : Le tableau de bord DSI est un outil de pilotage qui centralise les indicateurs clés permettant de mesurer la performance, la disponibilité, la sécurité et la valeur métier du Système d'Information. Il existe à plusieurs niveaux : stratégique (alignement sur la stratégie d'entreprise), tactique (suivi des projets et ressources), et opérationnel (supervision des systèmes en temps réel).
> **Pourquoi c'est important** : Le DSI doit rendre des comptes au CODIR sur la valeur générée par le SI et justifier ses investissements. Un TDB bien construit transforme la DSI de centre de coûts en partenaire stratégique, en rendant visible l'impact du SI sur la performance globale de l'entreprise.
> **Chiffres clés** :
> - 72 % des DSI déclarent que la mesure de la valeur métier du SI est leur principal défi de gouvernance (Gartner, 2023).
> - Les entreprises dotées d'un TDB SI formalisé réduisent de 30 % le temps de prise de décision sur les arbitrages IT (IDC, 2022).
> - Le marché des outils de BI et dashboarding atteindra 43 Md$ en 2028, avec une croissance de 8 % par an (MarketsandMarkets, 2023).

## Approfondir

### Fonctionnement

**Les trois niveaux de pilotage**

| Niveau | Horizon | Audience | Exemples d'indicateurs |
|--------|---------|----------|------------------------|
| Stratégique | Annuel / pluriannuel | CODIR, DG | Alignement SI/stratégie, % projets livrés, ROI global SI |
| Tactique | Mensuel / trimestriel | DSI, directions métier | Respect budgets, satisfaction utilisateurs, portefeuille projets |
| Opérationnel | Temps réel / quotidien | Équipes IT, NOC | Disponibilité systèmes, taux d'incidents, SLA |

**La Balanced Scorecard (BSC) appliquée au SI — Kaplan & Norton**

Adapté du modèle original (1992), la BSC IT structure les indicateurs en 4 axes complémentaires :

1. **Axe Financier** : coût total de possession (TCO), ROI des projets, respect du budget, réduction des coûts d'exploitation.
2. **Axe Clients/Métiers** : satisfaction utilisateurs (NPS interne), taux de disponibilité des applications métier, délai de livraison des projets.
3. **Axe Processus internes** : temps de résolution des incidents (MTTR), taux de succès des déploiements (Change Success Rate), couverture sécurité.
4. **Axe Apprentissage/Innovation** : % budget R&D/Innovation, niveau de dette technique, montée en compétence des équipes, adoption des nouvelles technologies.

**Types d'indicateurs**

- **KPI (Key Performance Indicator)** : mesure l'atteinte d'un objectif (ex : taux de disponibilité = 99,9 %).
- **KRI (Key Risk Indicator)** : alerte sur un risque potentiel avant qu'il se matérialise (ex : % d'actifs non patchés).
- **KQI (Key Quality Indicator)** : mesure la qualité d'un service ou d'un processus (ex : taux de défauts en production).

**Construction d'un TDB DSI**

1. Identifier les objectifs stratégiques de l'entreprise et leur traduction SI.
2. Sélectionner les indicateurs : SMART (Spécifique, Mesurable, Atteignable, Réaliste, Temporel), en nombre limité (5 à 10 par axe maximum).
3. Définir les sources de données et la fréquence de collecte (automatisation recommandée).
4. Choisir les visualisations adaptées : courbes (tendance), jauges (seuils), heatmaps (risques).
5. Définir les seuils d'alerte (vert / orange / rouge) et les responsables de chaque indicateur.
6. Réviser régulièrement la pertinence des indicateurs (au moins annuellement).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Visibilité en temps réel sur la performance SI | Risque de sur-indicatorisation (trop d'indicateurs = perte de focus) |
| Aide à la décision et à la priorisation | Qualité des données sources souvent insuffisante |
| Communication fluide avec le CODIR | Coût de mise en place et de maintenance |
| Responsabilisation des équipes (ownership des KPI) | Indicateurs mal choisis peuvent créer des comportements non désirés |
| Alignement visible SI/stratégie d'entreprise | Nécessite une culture data mature dans la DSI |

### Acteurs et solutions du marché

**Outils BI / Dashboarding**
- **Power BI** (Microsoft) — standard en entreprise, intégration native M365.
- **Tableau** (Salesforce) — puissance analytique, usage data scientist.
- **Qlik Sense** — approche associative, bonne pour l'exploration.
- **Grafana** — dashboards techniques temps réel, monitoring/observabilité.
- **Datadog / Dynatrace / New Relic** — observabilité et TDB opérationnel IT.

**Référentiels associés**
- **ITIL v4** — cadre de référence pour les métriques de service IT.
- **COBIT 2019** — gouvernance SI et indicateurs de maturité.
- **ISO/IEC 38500** — principes de gouvernance des SI.

### Cas d'usage concrets

1. **PME industrielle (200 salariés)** : mise en place d'un TDB mensuel présenté au CODIR avec 4 indicateurs phares (disponibilité ERP, respect budget IT, satisfaction utilisateurs, nombre d'incidents critiques). Permet d'objectiver les demandes de budget.

2. **ESN en croissance** : TDB portefeuille projets alimenté automatiquement depuis Jira (avancement, budget brûlé, risques). Réduction du temps de préparation des reportings de 6h à 30 min par semaine.

3. **Groupe retail** : TDB sécurité hebdomadaire pour le RSSI (nombre de vulnérabilités critiques non corrigées, % endpoints protégés, résultats phishing simulé) permettant une priorisation objective du backlog sécurité.

### Chiffres et tendances

- 68 % des entreprises utilisent encore des tableurs Excel comme principal outil de reporting SI (Gartner, 2022) — illustre le gisement de modernisation.
- La valorisation des outils AIOps pour l'automatisation des TDB opérationnels croît de 33 % par an (IDC, 2023).
- Le "time to insight" moyen est de 3,5 jours dans les entreprises sans TDB formalisé, contre 4 heures avec des outils connectés (McKinsey, 2023).

## Flashcards
#flashcards/Optimisation_du_SI/Tableau_de_Bord_DSI #flashcards/Management_et_stratégie/Tableau_de_Bord_DSI

Quels sont les 4 axes de la Balanced Scorecard appliquée au SI ? :: Financier (TCO, ROI), Clients/Métiers (satisfaction, disponibilité), Processus internes (MTTR, déploiements), Apprentissage/Innovation (dette technique, R&D).

Quelle est la différence entre KPI, KRI et KQI ? :: KPI mesure l'atteinte d'un objectif, KRI alerte sur un risque avant qu'il se matérialise, KQI mesure la qualité d'un service ou processus.

Quels sont les 3 niveaux d'un tableau de bord SI ? :: Stratégique (CODIR, horizon annuel), Tactique (DSI, mensuel/trimestriel), Opérationnel (équipes IT, temps réel/quotidien).

Quelles sont les 5 étapes de construction d'un TDB DSI ? :: 1. Identifier les objectifs stratégiques, 2. Sélectionner des KPI SMART, 3. Définir sources et fréquence, 4. Choisir les visualisations, 5. Définir les seuils d'alerte et les responsables.

Qu'est-ce que la Balanced Scorecard et qui l'a créée ? :: Outil de pilotage stratégique créé par Kaplan & Norton (1992) structurant la performance en 4 axes : Financier, Clients, Processus internes, Apprentissage/Innovation.

Comment un DSI justifie-t-il la valeur du SI devant le CODIR ? :: En s'appuyant sur un TDB avec des indicateurs alignés sur la stratégie d'entreprise : ROI des projets, satisfaction métiers, disponibilité des systèmes critiques et respect du budget.

Citez 3 indicateurs opérationnels typiques d'un TDB DSI. :: Taux de disponibilité des systèmes (ex : 99,9 %), MTTR (Mean Time To Repair), taux de succès des déploiements (Change Success Rate).

Quel est le risque principal d'un tableau de bord avec trop d'indicateurs ? :: La sur-indicatorisation : perte de focus, difficulté à identifier les signaux d'alerte, et comportements non désirés (optimiser un indicateur au détriment d'un autre).

Quels référentiels de gouvernance sont associés aux TDB SI ? :: COBIT 2019 (indicateurs de maturité), ITIL v4 (métriques de service IT), ISO/IEC 38500 (gouvernance des SI).

## Sources
- Kaplan, R.S. & Norton, D.P. — *The Balanced Scorecard* (1996), Harvard Business School Press.
- Gartner — *IT Metrics: IT Spending and Staffing Report* (2023).
- COBIT 2019 — ISACA — https://www.isaca.org/resources/cobit
- ITIL v4 — Axelos — https://www.axelos.com/certifications/itil-service-management
- IDC — *IT Performance Dashboard Benchmark Study* (2022).

## Notions liées
- [[VAN - TRI - Payback]]
- [[Indicateurs financiers du SI]]
- [[SLA - SLO - SLI]]
- [[MTTR - MTBF]]
- [[RACI et outils de gouvernance projet]]
- [[Qualité logicielle — normes et modèles]]
- [[Outils ITSM]]
- [[Système d'Information (SI)]]
