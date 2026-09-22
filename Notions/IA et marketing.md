---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 
---

# IA et marketing

![[N — IA et marketing.mp3]]
## En bref

### Définition
L'IA transforme le marketing en rendant possible la **personnalisation à l'échelle individuelle** (hyper-personnalisation), l'**automatisation des campagnes** (marketing automation), la **recommandation algorithmique** et le ciblage publicitaire en temps réel (**programmatic advertising / RTB**). Le **marketing prédictif** anticipe les comportements futurs des clients (achat, churn, réponse à une offre). Les **CDP** (Customer Data Platforms) centralisent les données client pour alimenter ces algorithmes.

### Pourquoi c'est important
Le marketing est l'un des secteurs où le ROI de l'IA est le plus mesurable et rapide. L'hyper-personnalisation est devenue un standard attendu par les consommateurs (71 % attendent une expérience personnalisée — McKinsey). Pour le MAALSI, c'est l'intersection entre la transformation digitale du SI et la valeur business concrète.

### Chiffres clés
- **71 %** des consommateurs attendent une expérience personnalisée (McKinsey, 2023)
- Les entreprises avec personnalisation avancée génèrent **40 % de revenus supplémentaires** (McKinsey)
- Le programmatic advertising représente **~90 %** des achats publicitaires digitaux en 2024
- La recommandation IA génère **35 %** du CA d'Amazon et **80 %** des contenus vus sur Netflix
- Marketing automation : +**451 %** de leads qualifiés (Annuitas Group)

---

## Approfondir

### Fonctionnement

#### Marketing prédictif
Application du ML pour anticiper les comportements futurs à partir de données historiques :
- **Propension à l'achat** : quelle proba qu'un client achète tel produit dans les 30 jours ?
- **Churn prédictif** : quelle proba qu'un client résilie ? (voir fiche Métriques)
- **Meilleure offre suivante (Next Best Offer/Action)** : quelle offre présenter maintenant ?
- **Optimisation du timing** : quel est le meilleur moment pour contacter ce client ?

**Algorithmes courants :** régression logistique, Random Forest, Gradient Boosting (XGBoost), réseaux de neurones, modèles séquentiels (LSTM pour séries temporelles).

#### Hyper-personnalisation
Personnalisation en temps réel à l'échelle individuelle (vs segmentation par groupe) :

| Niveau | Approche | Exemple |
|---|---|---|
| **Segmentation** | Groupes de clients similaires | Newsletter par segment démographique |
| **Personnalisation** | Adaptée au profil individuel | Email avec prénom + produits achetés |
| **Hyper-personnalisation** | Temps réel, contexte, comportement live | Notification push au moment où le client passe devant le magasin |

**Données utilisées :** historique d'achat, comportement web/app, données RFM (Récence, Fréquence, Montant), données contextuelles (météo, heure, localisation), données déclaratives (zero-party data).

#### Marketing Automation
Automatisation des workflows marketing déclenchés par des événements comportementaux :
- **Welcome series** : séquence d'e-mails à l'inscription
- **Abandon de panier** : e-mail 1h, 24h, 72h après abandon
- **Re-engagement** : campagne si inactif depuis N jours
- **Score-based nurturing** : contenu adapté au score de maturité du lead

**Outils :** Salesforce Marketing Cloud, HubSpot, Marketo, Adobe Campaign, Brevo.

#### Recommandation algorithmique

| Type | Méthode | Exemple |
|---|---|---|
| **Collaborative filtering** | "Les utilisateurs similaires à vous ont aimé…" | Netflix, Spotify |
| **Content-based** | "Basé sur ce que vous avez aimé…" | YouTube, Pocket |
| **Hybride** | Combinaison des deux | Amazon, Booking.com |
| **Contextuel** | Prise en compte du contexte temps réel | Recommandation météo, localisation |

#### CDP — Customer Data Platform

```
Sources de données        CDP                    Activation
─────────────────         ───                    ──────────
CRM               →
Site web          →  Profil client       →  Email
App mobile        →  unifié temps réel   →  Ads (Facebook, Google)
POS magasin       →  (first-party data)  →  Chatbot
Call center       →                     →  Personnalisation web
```

**CDP vs CRM :**
- CRM : gestion de la relation client, centré sur les interactions commerciales
- CDP : unification de toutes les données client (comportementales, transactionnelles, offline) pour l'activation marketing en temps réel

#### Programmatic Advertising et RTB (Real-Time Bidding)

**Processus RTB en ~100 ms :**
1. L'utilisateur charge une page web
2. Le SSP (éditeur) envoie une enchère aux DSP (annonceurs)
3. Chaque DSP évalue l'utilisateur avec ses modèles IA (DMP, profil)
4. Le DSP le plus offrant remporte l'espace publicitaire
5. La publicité personnalisée s'affiche

**Enjeux IA dans le programmatic :**
- Modèles de **bid optimization** (maximiser les conversions pour le budget)
- **Look-alike audiences** : cibler des profils similaires aux meilleurs clients
- **Prévention de la fraude** (IVT — Invalid Traffic) : détection de bots

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| ROI mesurable et optimisable en temps réel | Dépendance aux données first-party (post-cookies) |
| Personnalisation à l'échelle individuelle | Risques RGPD et vie privée (consentement) |
| Réduction des coûts d'acquisition (meilleur ciblage) | Effet "bulle de filtre" — réduction de la diversité |
| Automatisation des tâches répétitives (campagnes) | Complexité tech et coût des plateformes |
| Détection précoce du churn | Déshumanisation perçue par certains clients |
| A/B testing à grande échelle | Hallucinations si IA générative mal contrôlée |

### Acteurs
- **CDP** : Salesforce Data Cloud, Adobe Experience Platform, Segment (Twilio), Tealium
- **Marketing automation** : HubSpot, Salesforce Marketing Cloud, Marketo (Adobe), Brevo, Klaviyo
- **Programmatic** : Trade Desk (DSP), Google DV360, Xandr (Microsoft), PubMatic (SSP)
- **Recommandation** : AWS Personalize, Google Recommendations AI, Coveo, Algolia
- **IA créative/contenu** : Jasper, Copy.ai, Adobe Firefly, Canva AI

### Cas d'usage
- **E-commerce** : recommandation produits, abandon panier, pricing dynamique, personnalisation de la home
- **Banque/Assurance** : Next Best Offer, détection de churn, scoring de leads
- **Retail** : promotions géolocalisées, optimisation des stocks selon la demande prédite
- **Médias** : recommandation de contenus (Netflix, Spotify, Deezer)
- **B2B** : lead scoring, contenu adapté à la maturité du prospect

### Chiffres complémentaires
- Spotify : l'IA génère les playlists de **230 M utilisateurs** chaque semaine (Discover Weekly)
- Amazon : chaque point de % de taux de conversion = **+~1 Md$** de CA annuel
- Abandon de panier : 69 % des paniers abandonnés, un e-mail de relance récupère 5-15 %

---

## Flashcards
#flashcards/IA/IA_et_marketing

Qu'est-ce que l'hyper-personnalisation et en quoi diffère-t-elle de la segmentation ? :: La segmentation regroupe des clients en catégories et leur envoie le même message. L'hyper-personnalisation adapte le message, l'offre et le canal en temps réel au contexte et au comportement individuel de chaque client, grâce à l'IA.

Qu'est-ce qu'un CDP et en quoi diffère-t-il d'un CRM ? :: Le CDP (Customer Data Platform) unifie toutes les données client (comportementales, transactionnelles, offline) en un profil temps réel pour l'activation marketing. Le CRM gère les interactions commerciales et la relation client. Le CDP alimente le CRM et les outils d'activation.

Expliquez le processus RTB (Real-Time Bidding) en 4 étapes. :: 1) Un utilisateur visite une page → le SSP publie l'espace disponible. 2) Les DSP reçoivent la demande et évaluent l'utilisateur via leurs modèles IA. 3) Enchère en ~100 ms : le DSP le plus offrant remporte l'espace. 4) La publicité personnalisée s'affiche.

Qu'est-ce que le marketing prédictif ? Donnez 2 exemples. :: Application du ML pour anticiper les comportements futurs des clients. Exemples : prédiction de churn (probabilité de résiliation), prédiction de propension à l'achat (quel produit acheter dans les 30 jours), optimisation du timing d'envoi.

Quelle est la différence entre le collaborative filtering et le content-based filtering ? :: Collaborative filtering : recommande en se basant sur les préférences d'utilisateurs similaires ("les gens comme vous ont aimé…"). Content-based filtering : recommande des items similaires à ce que l'utilisateur a déjà aimé (basé sur les attributs du contenu).

Qu'est-ce que le marketing automation ? Donnez 2 exemples de workflows. :: Automatisation de campagnes déclenchées par des événements comportementaux. Exemples : email d'abandon de panier envoyé 1h après l'abandon, séquence de bienvenue sur 7 jours après inscription, campagne de réengagement si inactif 30 jours.

---

## Sources
- McKinsey — *The value of getting personalization right—or wrong*, 2023
- eMarketer — Programmatic Advertising Outlook, 2024
- Salesforce — State of Marketing Report, 2024
- Amazon — Annual Report (chiffres recommandation)
- Gartner — Magic Quadrant for Customer Data Platforms, 2024

---

## Notions liées
- [[Intelligence Artificielle — fondamentaux]]
- [[Métriques marketing et IA]]
- [[Chatbots et assistants virtuels]]
- [[IA générative et LLM]]
