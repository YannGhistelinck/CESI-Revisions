---
type: notion
thèmes:
  - Big DATA
  - IA
statut: pas vu
dernière_révision: 
---

# Profilage et surveillance

![[N — Profilage et surveillance.mp3]]
## En bref
> **Définition** : Le **profilage automatisé** désigne tout traitement automatisé de données personnelles visant à évaluer, prédire ou influencer des aspects de la personnalité d'un individu (comportement, préférences, solvabilité, santé…). La **bulle de filtre** (Eli Pariser, 2011) est le phénomène par lequel les algorithmes de recommandation enferment l'utilisateur dans un espace informationnel homogène, en filtrant les contenus selon son profil. Le **capitalisme de surveillance** (Shoshana Zuboff, 2019) désigne le modèle économique fondé sur la captation, l'analyse et la monétisation des comportements humains comme matière première d'une économie de prédiction comportementale.
> **Pourquoi c'est important** : Ces phénomènes sont au cœur des débats sur la démocratie, l'autonomie individuelle et la responsabilité des plateformes. Pour un DSI ou un architecte Big Data, ils posent des questions de conception (article 22 RGPD sur les décisions automatisées) et de gouvernance (DSA, AI Act). Pour l'organisation, ils représentent à la fois une opportunité (personnalisation, marketing) et un risque juridique et réputationnel.
> **Chiffres clés** :
> - L'article 22 du RGPD donne aux personnes le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou significatifs.
> - Meta a généré 131,9 Md$ de revenus publicitaires en 2023, quasi intégralement fondés sur le profilage comportemental.
> - Cambridge Analytica a utilisé les profils psychographiques de 87 millions d'utilisateurs Facebook pour cibler des messages électoraux (scandale 2018).

## Approfondir

### Fonctionnement

**Profilage automatisé**
Défini à l'article 4(4) du RGPD comme "toute forme de traitement automatisé de données à caractère personnel consistant à utiliser ces données pour évaluer certains aspects personnels relatifs à une personne physique". Le profilage peut servir à : évaluer les performances au travail, la situation économique, la santé, les préférences personnelles, les intérêts, la fiabilité, le comportement, la localisation, les déplacements.

Techniques de profilage :
- **Segmentation comportementale** : regroupement d'utilisateurs selon leurs comportements (clics, achats, temps de lecture).
- **Scoring prédictif** : attribution d'un score de probabilité (risque crédit, probabilité d'achat, risque de churn).
- **Analyse de sentiment** : inférence des états émotionnels à partir de textes ou d'expressions faciales.
- **Graph analysis** : analyse des réseaux sociaux pour inférer des caractéristiques non déclarées (orientation politique, santé…).

Risques : discrimination algorithmique (refus de crédit, de logement), manipulation comportementale, violation de la vie privée par inférence de données sensibles non déclarées.

**Bulle de filtre (Filter Bubble)**
Mécanisme par lequel les algorithmes de recommandation (YouTube, Facebook, TikTok, Google News) personnalisent les contenus affichés selon l'historique et le profil de l'utilisateur, réduisant l'exposition à des points de vue divergents. Effets : polarisation politique, radicalisation progressive, désinformation (les contenus émotionnellement engageants sont algorithmiquement favorisés car ils génèrent plus d'interactions).

Mécanismes techniques : filtrage collaboratif (les utilisateurs similaires voient les mêmes contenus), filtrage basé sur le contenu (analyse des contenus consommés), modèles de deep learning prédisant l'engagement. Le "temps de visionnage" (watch time) de YouTube, optimisé par RL (reinforcement learning), a conduit à la recommandation de contenus de plus en plus extrêmes (rapport Wall Street Journal, 2021).

**Capitalisme de surveillance (Surveillance Capitalism)**
Concept théorisé par Shoshana Zuboff dans "The Age of Surveillance Capitalism" (2019). Modèle économique en trois étapes :
1. **Extraction** : captation massive des comportements humains (clics, déplacements, achats, conversations) via les services numériques gratuits.
2. **Prédiction** : transformation de ces données en "produits de prédiction" (probabilité qu'un utilisateur clique sur une publicité, achète un produit, vote pour un candidat).
3. **Vente** : ces produits de prédiction sont vendus aux annonceurs, qui achètent des garanties de résultats comportementaux.

Acteurs principaux : Google (brevets de "surveillance assets"), Meta, Amazon, les data brokers (Acxiom, Experian, Equifax) qui compilent des profils de milliards d'individus.

**Décisions automatisées (article 22 RGPD)**
Toute décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou significativement similaires doit être encadrée : droit d'opposition, droit à une intervention humaine, droit à l'explication. Exceptions : nécessité contractuelle, autorisation légale, consentement explicite. Concerne : scoring de crédit, sélection de candidats par CV parsing, tarification d'assurance dynamique, détection de fraude.

### Avantages / Inconvénients
| Perspective | Avantages | Inconvénients / Risques |
|-------------|-----------|------------------------|
| Entreprises | Personnalisation, efficacité marketing, réduction du churn | Risque juridique (article 22 RGPD), réputation, régulation croissante |
| Utilisateurs | Expérience personnalisée, recommandations pertinentes | Manipulation, perte d'autonomie, atteinte à la vie privée |
| Société | Optimisation de services publics | Polarisation, discrimination algorithmique, érosion de la démocratie |

### Acteurs et solutions du marché

- **Plateformes profilantes** : Google, Meta, TikTok (ByteDance), Amazon, Microsoft (LinkedIn)
- **Data brokers** : Acxiom, Experian, Epsilon — compilent des profils sur des milliards d'individus, y compris sans leur consentement direct
- **Outils de protection** : DuckDuckGo, Brave Browser (bloqueur de traceurs), Privacy Badger (EFF), uBlock Origin
- **Régulateurs** : CNIL, CEPD, FTC (USA) — enquêtes et sanctions contre les pratiques de profilage abusif
- **Chercheurs et ONG** : Shoshana Zuboff (Harvard), Eli Pariser (MoveOn.org), AlgorithmWatch (Berlin), NOYB (Max Schrems)
- **Cadres réglementaires limitant le profilage** : RGPD article 22, AI Act (systèmes à haut risque), DSA (transparence algorithmique)

### Cas d'usage concrets

1. **Scoring de crédit automatisé** : une banque utilise un modèle ML pour décider automatiquement l'octroi d'un prêt. Article 22 RGPD oblige à informer le demandeur, à lui permettre de contester et à prévoir une révision humaine. Le modèle doit être explicable (XAI — Explainable AI) pour répondre aux demandes de motivation.

2. **Recommandation YouTube et radicalisation** : le Wall Street Journal (2021) a documenté comment l'algorithme de recommandation YouTube conduisait systématiquement vers des contenus conspirationnistes ou extrémistes, car ces contenus génèrent plus d'engagement. Réponse de YouTube : introduction de "authoritative sources" et limitation des recommandations de contenus borderline.

3. **Cambridge Analytica** : exploitation des données de 87 millions d'utilisateurs Facebook (via une application de quiz collectant les données des amis sans consentement) pour construire des profils psychographiques OCEAN (Ouverture, Conscience, Extraversion, Agréabilité, Névrosisme) et cibler des messages électoraux personnalisés (élection Trump 2016, Brexit). Résultat : amende de 5 Md$ à Facebook (FTC, 2019), dissolution de Cambridge Analytica.

4. **Publicité comportementale programmatique** : une DSP (Demand-Side Platform) like Google DV360 achète en temps réel (RTB — Real-Time Bidding) des impressions publicitaires en utilisant les profils comportementaux des utilisateurs. Une enchère se déroule en moins de 100 ms entre l'affichage d'une page web et son chargement. Implique des centaines d'acteurs de l'adtech ayant accès aux données de comportement.

### Chiffres et tendances

- TikTok recommande des contenus uniquement basés sur le comportement in-app (pas de graphe social), ce qui le rend particulièrement efficace et addictif — temps moyen de 52 min/jour par utilisateur (2023).
- Une étude MIT (2018) montre que les fausses nouvelles se propagent 6 fois plus vite que les vraies sur Twitter, favorisées par les algorithmes d'engagement.
- L'AI Act classe les systèmes de profilage des personnes physiques à grande échelle et les systèmes de notation sociale comme interdits ou à haut risque.
- Le DSA impose aux très grandes plateformes (VLOP) de permettre aux utilisateurs de choisir un mode de recommandation non basé sur le profilage (depuis 2024).
- Les data brokers génèrent un marché mondial estimé à 300 Md$ en 2023 (IAPP).

## Flashcards
#flashcards/Big_DATA/Profilage_et_surveillance #flashcards/IA/Profilage_et_surveillance

Quelle est la définition du profilage automatisé selon le RGPD ? :: L'article 4(4) du RGPD définit le profilage comme tout traitement automatisé de données personnelles visant à évaluer des aspects personnels d'un individu (comportement, préférences, santé, situation économique, localisation…).

Qu'est-ce que la bulle de filtre et qui a théorisé ce concept ? :: Concept d'Eli Pariser (2011) désignant l'enfermement algorithmique de l'utilisateur dans un espace informationnel homogène, où les algorithmes de recommandation filtrent les contenus selon son profil, réduisant l'exposition à des points de vue divergents.

Qu'est-ce que le capitalisme de surveillance selon Shoshana Zuboff ? :: Modèle économique (Zuboff, 2019) fondé sur l'extraction des comportements humains comme matière première, leur transformation en produits de prédiction comportementale, et leur vente aux annonceurs — sans que les individus soient rémunérés pour leurs données.

Que prévoit l'article 22 du RGPD sur les décisions automatisées ? :: Il donne aux personnes le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou significatifs, avec droit à une intervention humaine, à l'explication et à la contestation.

Qu'est-ce que le Real-Time Bidding (RTB) et quel est son lien avec le profilage ? :: Mécanisme d'enchère publicitaire en temps réel (<100 ms) permettant d'acheter une impression publicitaire ciblée sur un profil comportemental précis. Implique des centaines d'acteurs de l'adtech ayant accès simultané aux données de comportement des internautes.

Quelle obligation le DSA impose-t-il aux grandes plateformes concernant les algorithmes de recommandation ? :: Depuis 2024, les très grandes plateformes (VLOP) doivent proposer aux utilisateurs au moins une option de recommandation non basée sur le profilage comportemental (article 38 DSA).

Qu'a révélé le scandale Cambridge Analytica et quelles ont été ses conséquences ? :: Cambridge Analytica a utilisé les données psychographiques de 87 millions d'utilisateurs Facebook pour cibler des messages électoraux personnalisés (Trump 2016, Brexit). Conséquences : amende de 5 Md$ à Facebook (FTC, 2019), dissolution de Cambridge Analytica, renforcement de la régulation des plateformes.

## Sources

- RGPD — Règlement (UE) 2016/679, articles 4(4) et 22 : https://eur-lex.europa.eu/
- Shoshana Zuboff, "The Age of Surveillance Capitalism", PublicAffairs, 2019
- Eli Pariser, "The Filter Bubble: What the Internet Is Hiding from You", Penguin Press, 2011
- CEPD, Lignes directrices 04/2022 sur le calcul des amendes administratives
- Wall Street Journal, "The Facebook Files" et "YouTube Radicalization", 2021
- FTC, "Facebook, Inc. — Complaint and Settlement", 2019 (5 Md$ d'amende)
- AlgorithmWatch — rapports sur les biais algorithmiques : https://algorithmwatch.org/
- DSA — Règlement (UE) 2022/2065, article 38 (systèmes de recommandation)

## Notions liées

- [[RGPD]]
- [[Privacy by Design]]
- [[DSA - DMA]]
- [[IA en cybersécurité]]
- [[Data Lifecycle Management]]
- [[Réglementations internationales sur les données]]
