---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 
---

# Métriques marketing et IA

## En bref

### Définition
Les métriques marketing pilotées par l'IA permettent de quantifier, prédire et optimiser la valeur client. Les principales sont : le **CLV** (Customer Lifetime Value — valeur vie client), le **churn** (taux d'attrition), le **lead scoring** (qualification prédictive des prospects), le **pricing dynamique** (tarification en temps réel), et les données **first-party / zero-party** (alternatives aux cookies tiers dans un contexte post-RGPD). L'IA transforme ces métriques de mesures rétrospectives en leviers prédictifs et actionnables.

### Pourquoi c'est important
Dans un contexte de fin des cookies tiers et de pression sur les budgets marketing, la maîtrise des données propriétaires et la prédiction comportementale sont des avantages concurrentiels décisifs. Pour le Grand Oral MAALSI, ces métriques illustrent concrètement comment l'IA crée de la valeur business mesurable.

### Chiffres clés
- Augmenter la rétention client de **5 %** augmente les profits de **25 à 95 %** (Bain & Company)
- Un modèle de churn prédictif peut identifier **70-80 %** des churners 30 jours avant la résiliation
- Le lead scoring IA améliore le taux de conversion des leads de **30 %** (Salesforce)
- Le pricing dynamique augmente le revenu de **2 à 5 %** en moyenne (McKinsey)
- Fin des cookies tiers Chrome : initialement 2024, reportée à 2025, désormais incertaine — mais **82 % des annonceurs** investissent déjà dans les alternatives first-party

---

## Approfondir

### Fonctionnement

#### CLV — Customer Lifetime Value (Valeur Vie Client)

**Définition :** valeur totale des revenus qu'un client génère pour l'entreprise sur toute la durée de la relation.

**Formule simplifiée :**
```
CLV = (Valeur moyenne d'achat × Fréquence d'achat × Durée de la relation)
      - Coût d'acquisition (CAC) - Coût de rétention
```

**CLV prédictif avec IA :**
- Modèles probabilistes (BG/NBD, Pareto/NBD) + ML pour prédire les achats futurs
- Segmentation RFM (Récence, Fréquence, Montant) enrichie par des features comportementales
- Prédiction à 6, 12, 24 mois pour orienter les investissements d'acquisition et rétention

**Applications :**
- Allouer le budget publicitaire aux segments à plus fort CLV
- Fixer le CAC maximum acceptable par segment
- Prioriser les actions de rétention sur les clients à fort CLV à risque de churn

#### Churn — Modèles prédictifs

**Churn** : résiliation, désabonnement, abandon d'un client.

**Types :**
- **Churn volontaire** : le client résilie activement (abonnement télécom, SaaS)
- **Churn involontaire** : échec de paiement, carte expirée
- **Churn comportemental** : baisse progressive d'engagement avant la résiliation formelle

**Pipeline de prédiction du churn :**
```
Features comportementales         Modèle ML           Actions
───────────────────────           ─────────           ───────
Fréquence de connexion     →
Montant des achats         →  Score de churn   →  Offre de rétention personnalisée
NPS / satisfaction         →  (0 à 100 %)      →  Appel proactif (fort risque)
Interactions support       →                   →  Email de réactivation
Utilisation des features   →
```

**Algorithmes utilisés :** Logistic Regression (baseline), Random Forest, XGBoost, LightGBM, réseaux récurrents (LSTM) pour séries temporelles.

**Métriques d'évaluation du modèle churn :**
- **Précision / Rappel** : équilibre faux positifs (contacté inutilement) vs faux négatifs (churner manqué)
- **AUC-ROC** : performance globale du modèle (>0,80 = bon)
- **Lift** : amélioration vs ciblage aléatoire

#### Lead Scoring

**Définition :** attribution d'un score de maturité/qualité à chaque prospect pour prioriser les efforts commerciaux.

| Type | Méthode | Données utilisées |
|---|---|---|
| **Scoring traditionnel** | Règles manuelles + points | Titre de poste, taille entreprise, comportement email |
| **Scoring prédictif IA** | ML entraîné sur les leads convertis | Données comportementales web, CRM, données tierces |
| **Scoring d'intention** | Signaux d'achat en temps réel | Recherches, visites de pages prix, téléchargements |

**Dimensions du scoring (modèle BANT enrichi) :**
- **Fit** : correspondance avec le profil client idéal (ICP)
- **Engagement** : niveau d'interaction avec les contenus
- **Intent** : signaux d'intention d'achat
- **Timing** : maturité dans le cycle d'achat

**Impact :** les équipes commerciales se concentrent sur les 20 % de leads qui génèrent 80 % du CA (Pareto).

#### Pricing Dynamique

**Définition :** ajustement automatique des prix en temps réel en fonction de l'offre, de la demande, de la concurrence et du profil client.

| Secteur | Facteurs IA pris en compte | Exemple |
|---|---|---|
| **Transport aérien** | Demande temps réel, anticipation, date de départ | Billet Air France |
| **Hôtellerie** | Taux d'occupation, événements locaux, météo | Booking.com |
| **E-commerce** | Prix concurrents, stock, profil client, historique | Amazon (ajustements toutes les ~10 min) |
| **Énergie** | Consommation réseau, production renouvelable | EDF, prix spot |
| **Assurance** | Profil de risque individuel, télématique | Pay-as-you-drive |

**Algorithmes :** optimisation par renforcement, modèles de demande (élasticité prix), arbres de décision.

#### First-party et Zero-party Data

**Contexte :** fin progressive des cookies tiers (RGPD, ITP Safari, Privacy Sandbox Google) → les annonceurs perdent leur capacité de tracking cross-sites.

| Type | Définition | Exemple | Avantage |
|---|---|---|---|
| **Third-party data** | Données collectées par des tiers (cookies, DMP) | Profils comportementaux cross-sites | Volumineuse mais mourant |
| **Second-party data** | Données d'un partenaire (accord direct) | Données retail media d'un distributeur | Qualité intermédiaire |
| **First-party data** | Données collectées directement par l'entreprise | Historique d'achat, comportement site/app | Fiable, conforme RGPD |
| **Zero-party data** | Données déclarées volontairement par le client | Préférences dans un quiz, profil configuré | Consentement explicit, haute qualité |

**Stratégies de collecte first-party / zero-party :**
- Programmes de fidélité (collecte d'actes d'achat)
- Quizz de personnalisation (zero-party)
- Newsletters avec préférences thématiques
- Portails clients / espaces perso
- Données CRM enrichies

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Prédiction précise des comportements clients | Qualité des modèles dépendante de la qualité des données |
| Optimisation du budget marketing (focus sur valeur) | Risque de discrimination dans le pricing dynamique |
| Rétention proactive = économies sur l'acquisition | Complexité de mise en oeuvre (data science + CRM + activation) |
| Personnalisation des offres de rétention | RGPD : consentement et transparence obligatoires |
| Pricing dynamique = optimisation du revenu | Perception négative possible du pricing dynamique par les clients |
| Zero-party data : haute qualité, conforme RGPD | Collecte zero-party lente et nécessite une valeur échangée |

### Acteurs
- **CRM + scoring** : Salesforce (Einstein AI), HubSpot, Microsoft Dynamics 365
- **Plateformes CLV/Churn** : Amplitude, Mixpanel, Braze, Iterable
- **Pricing dynamique** : Pros, Zilliant, Pricefx, Omnia Retail
- **CDP (first-party)** : Segment (Twilio), Salesforce Data Cloud, Adobe Experience Platform
- **Retail Media** : Amazon Ads, Carrefour Links, Criteo Commerce Media

### Cas d'usage
- **Télécoms** : prédiction du churn sur les abonnés, offre de rétention ciblée 30 jours avant résiliation prévue
- **SaaS** : CLV par cohorte pour guider l'acquisition, lead scoring pour prioriser les demos
- **E-commerce** : pricing dynamique sur 500 000 SKU, segmentation CLV pour les campagnes loyalty
- **Banque** : churn prédictif sur les clients inactifs, scoring crédit ML

### Chiffres complémentaires
- Amazon modifie ses prix **2,5 millions de fois par jour** grâce à l'IA
- Un modèle de churn bien calibré génère en moyenne **3 à 8x ROI** sur les actions de rétention
- Le CLV moyen d'un client fidèle est **5x supérieur** à celui d'un nouveau client

---

## Flashcards
#flashcards/IA/Métriques_marketing_et_IA

Qu'est-ce que le CLV et comment l'IA le transforme-t-il ? :: Le CLV (Customer Lifetime Value) est la valeur totale des revenus générés par un client sur toute la relation. L'IA le transforme de métrique rétrospective en prédiction : modèles probabilistes (BG/NBD) et ML permettent d'estimer le CLV futur à 6/12/24 mois pour orienter budget et actions de rétention.

Qu'est-ce que le churn prédictif et quelles données utilise-t-il ? :: Le churn prédictif est un modèle ML qui calcule la probabilité qu'un client résilie dans une fenêtre temporelle donnée. Il utilise : fréquence de connexion, montant des achats, interactions support, NPS, utilisation des features, historique de paiement.

Quelle est la différence entre first-party data et zero-party data ? :: First-party data : données collectées par l'entreprise via ses propres canaux (historique achat, comportement site/app). Zero-party data : données déclarées volontairement par le client (quiz de préférences, profil configuré). La zero-party est de plus haute qualité et présuppose un consentement explicite.

Qu'est-ce que le lead scoring prédictif et en quoi améliore-t-il le lead scoring traditionnel ? :: Le lead scoring prédictif utilise le ML entraîné sur les leads historiquement convertis pour calculer automatiquement la probabilité de conversion. Il dépasse le scoring traditionnel (règles manuelles) en capturant des patterns non-linéaires et en intégrant des signaux d'intention en temps réel.

Donnez 3 secteurs où le pricing dynamique est utilisé avec l'IA. :: Transport aérien (prix selon la demande et la date), e-commerce (Amazon ajuste 2,5M prix/jour), hôtellerie (taux d'occupation + événements locaux), énergie (prix spot), assurance (télématique pay-as-you-drive).

Pourquoi la fin des cookies tiers est-elle un enjeu pour le marketing digital ? :: Les cookies tiers permettaient le suivi cross-sites et le ciblage publicitaire précis. Leur disparition (RGPD, ITP Safari, Privacy Sandbox) oblige les annonceurs à se concentrer sur les données first-party et zero-party, avec des alternatives comme les clean rooms et le ciblage contextuel.

Qu'est-ce que le RFM et comment est-il utilisé avec l'IA ? :: RFM = Récence (dernier achat), Fréquence (nombre d'achats), Montant (valeur totale). Segmentation classique enrichie par l'IA : les features RFM sont intégrées dans des modèles ML de CLV ou de churn, combinées avec des données comportementales et contextuelles pour une segmentation plus fine.

---

## Sources
- Bain & Company — *Prescription for Cutting Costs* (fidélisation / profit)
- McKinsey — *The value of getting personalization right*, 2023
- Salesforce — State of Sales Report, 2024
- Harvard Business Review — *The Elements of Value*, 2016
- Gartner — Hype Cycle for Digital Marketing, 2024

---

## Notions liées
- [[IA et marketing]]
- [[Chatbots et assistants virtuels]]
- [[Intelligence Artificielle — fondamentaux]]
- [[MLOps - DataOps]]
