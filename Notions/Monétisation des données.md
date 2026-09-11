---
type: notion
thèmes:
  - Big DATA
  - IA
statut: pas vu
dernière_révision: 
---

# Monétisation des données

## En bref
> **Définition** : La monétisation des données désigne l'ensemble des mécanismes par lesquels des acteurs économiques tirent de la valeur financière des données personnelles ou comportementales. Elle prend deux formes principales : la monétisation **directe** (vente de données brutes ou enrichies par des data brokers) et la monétisation **indirecte** (amélioration des produits/services grâce aux données, ciblage publicitaire). Le concept de **capitalisme de surveillance** (Shoshana Zuboff) décrit la logique systémique d'extraction de données comportementales à des fins commerciales.
> **Pourquoi c'est important** : La monétisation des données est le modèle économique dominant d'Internet (Google, Meta, X). Elle soulève des enjeux éthiques majeurs — vie privée, manipulation comportementale, démocratie — illustrés de manière emblématique par le scandale Cambridge Analytica (2018).
> **Chiffres clés** :
> - Le marché mondial des data brokers pèse **365 Md$** en 2023 (IMARC Group)
> - **Google** tire **77 % de ses revenus** de la publicité ciblée (données comportementales)
> - **Meta** génère en moyenne **13,12 $ par utilisateur américain par trimestre** via la publicité (Q4 2023)
> - Le scandale Cambridge Analytica a exposé les données de **87 millions de profils** Facebook

## Approfondir

### Fonctionnement

#### Les deux formes de monétisation des données

**1. Monétisation directe**
Les données sont vendues ou louées à des tiers :
- **Data brokers** : entreprises spécialisées dans la collecte, l'agrégation et la revente de données sur des individus
- **Open Data commercial** : vente de datasets (Refinitiv pour les données financières, Nielsen pour les données de consommation)
- **Data sharing** : accords de partage de données entre entreprises (ex. : banques partageant des données transactionnelles avec des assureurs)

**2. Monétisation indirecte**
Les données améliorent des produits ou services qui génèrent des revenus :
- **Publicité ciblée** : le modèle Google/Meta — les données permettent de vendre des publicités ultra-ciblées à des annonceurs
- **Personnalisation** : Amazon, Netflix — les données d'usage améliorent les recommandations et augmentent les ventes/l'engagement
- **Tarification dynamique** : Uber, compagnies aériennes — les données de demande ajustent les prix en temps réel
- **Produits financiers** : les banques utilisent les données transactionnelles pour scorer le crédit et tarifer les assurances

#### Data Brokers — l'industrie de la revente de données

**Définition** : Entreprises dont le modèle économique repose entièrement sur la collecte, l'agrégation, l'enrichissement et la revente de données sur des individus, sans relation directe avec ces individus.

**Sources de données** :
- Données publiques : registres fonciers, actes de naissance/mariage, casiers judiciaires publics (US), réseaux sociaux publics
- Données transactionnelles achetées : programmes de fidélité, historiques d'achat
- Données comportementales : navigation web (cookies, pixels espions), applications mobiles
- Données télécoms : opérateurs vendant des données de géolocalisation (pratique illégale en Europe)

**Principaux data brokers** :
| Acteur | Spécialité |
|--------|-----------|
| **Acxiom** | Leader mondial, profils sur 2,5 milliards de personnes |
| **Experian** | Crédit scores + marketing data |
| **Equifax** | Données financières et d'identité |
| **LexisNexis** | Données légales, judiciaires, identité |
| **Epsilon** | Marketing data, ciblage publicitaire |
| **IRI / Circana** | Données de consommation (scannées en caisse) |

**Cadre légal** :
- **USA** : très peu régulé — le California Consumer Privacy Act (CCPA) est l'exception
- **Europe** : le RGPD impose un consentement explicite et le droit à l'effacement. Les data brokers doivent être capables de supprimer les données d'un individu sur demande.
- **France** : la CNIL a sanctionné plusieurs data brokers pour non-conformité RGPD

#### Capitalisme de surveillance — Shoshana Zuboff

**Auteure** : Shoshana Zuboff, professeure à Harvard Business School, ouvrage "The Age of Surveillance Capitalism" (2019).

**Thèse centrale** : Le capitalisme de surveillance est un nouvel ordre économique dans lequel l'expérience humaine est la matière première gratuite transformée en données comportementales, vendues comme "produits de prédiction" aux marchés publicitaires.

**Mécanisme** :
```
Comportement humain → Collecte de données → Modèles prédictifs → Produits de prédiction → Vente aux annonceurs
(navigation, achats,    (à l'insu de           (ML sur les         (probabilité de cliquer   (revenu publicitaire)
 clics, déplacements)    l'individu)             données)             sur une pub)
```

**Concepts clés de Zuboff** :
- **Surplus comportemental** : les données collectées au-delà de ce qui est nécessaire à l'amélioration du service (l'excédent est vendu)
- **Certitude comportementale** : objectif ultime des plateformes — prédire et modifier les comportements avec une précision croissante
- **Instruments de modification comportementale** : notifications, gamification, dark patterns — techniques conçues pour maximiser l'engagement et la collecte de données

**Critique** : Le capitalisme de surveillance est incompatible avec la démocratie car il repose sur l'asymétrie d'information et manipule les comportements à l'insu des individus.

#### Scandale Cambridge Analytica (2018)

**Contexte** : Cambridge Analytica (CA) est une société de conseil politique britannique spécialisée dans le ciblage comportemental pour les campagnes électorales.

**Mécanisme** :
1. Une application Facebook ("thisisyourdigitallife") collecte les données de 270 000 utilisateurs ayant consenti
2. Via les permissions de l'API Facebook de l'époque, elle collecte également les données des **amis** de ces utilisateurs — sans leur consentement
3. Au total : **87 millions de profils** Facebook exposés
4. Ces données sont utilisées pour construire des profils psychologiques (modèle OCEAN) et cibler des messages politiques ultra-personnalisés
5. Utilisé pour les campagnes **Brexit** (2016) et **Trump** (2016, pour Ted Cruz puis Donald Trump)

**Modèle OCEAN (Big Five)** :
- **O**penness (ouverture)
- **C**onscientiousness (consciencieux)
- **E**xtraversion
- **A**greeableness (agréabilité)
- **N**euroticism (névrosisme)

À partir de 10 likes Facebook, le modèle prédit la personnalité mieux qu'un collègue. À partir de 300, mieux que le conjoint.

**Conséquences** :
- Facebook condamné à une amende de **5 Md$** par la FTC (2019) — record historique
- Cambridge Analytica dissous en 2018
- Modification des règles d'accès à l'API Facebook
- Accélération de la prise de conscience sur la vie privée
- Inspiration directe du renforcement du RGPD en Europe

#### Dark Patterns et manipulation comportementale
Techniques de design d'interface conçues pour pousser l'utilisateur vers une action qu'il n'aurait pas choisie librement :
- **Confirmshaming** : honte de refuser ("Non merci, je ne veux pas économiser de l'argent")
- **Roach motel** : facile d'entrer, difficile de sortir (inscription en 1 clic, désinscription en 10 étapes)
- **Privacy zuckering** : paramètres de confidentialité délibérément obscurs pour maximiser le partage de données
- **Disguised ads** : publicités présentées comme du contenu éditorial

La CNIL française et la Commission européenne (Digital Services Act) ont commencé à sanctionner ces pratiques.

### Avantages / Inconvénients

| Avantages de la monétisation des données | Risques et inconvénients |
|------------------------------------------|--------------------------|
| Financement de services gratuits (Gmail, Maps, Facebook) | Atteinte à la vie privée et à l'autonomie individuelle |
| Personnalisation des expériences utilisateur | Manipulation comportementale à des fins commerciales et politiques |
| Stimulation de l'économie numérique | Asymétrie radicale : individus donnent tout, entreprises s'enrichissent |
| Innovation en analytics et IA | Concentration du pouvoir chez quelques plateformes (oligopole) |
| Open Data public créateur de valeur sociale | Risques pour la démocratie (Cambridge Analytica, fake news ciblées) |

### Acteurs et solutions du marché
- **Google (Alphabet)** : modèle publicitaire sur Search, YouTube, Gmail, Maps
- **Meta** : publicité ciblée sur Facebook, Instagram, WhatsApp
- **Acxiom** : leader mondial des data brokers B2B
- **Criteo** (France) : retargeting publicitaire, champion français de la data pub
- **The Trade Desk** : DSP (Demand-Side Platform) pour l'achat programmatique de publicité
- **Nielsen / Circana** : données de panel consommateurs
- **Palantir** : analytics de données sensibles (défense, renseignement, santé)

### Cas d'usage concrets
1. **Google** collecte des données de navigation sur l'ensemble du web via Google Analytics (présent sur 56 % des sites), les cookies publicitaires et Chrome. Ces données alimentent son système d'enchères publicitaires (Google Ads) qui génère 200 Md$/an de revenus. L'UE a sanctionné Google à hauteur de **8,25 Md€** en amendes depuis 2017 pour abus de position dominante liés aux données.
2. **Sephora** partage ses données de fidélité (comportements d'achat, préférences produits) avec des partenaires marques (L'Oréal, LVMH) en échange d'investissements publicitaires. Ce data sharing B2B est une forme de monétisation indirecte valorisant le programme fidélité à plusieurs centaines de millions d'euros.
3. **L'affaire Criteo** : la CNIL a infligé à Criteo une amende de **40 M€** en 2023 pour non-respect du RGPD (absence de consentement valide, cookies déposés sans accord). Premier cas majeur de sanction d'un acteur publicitaire français fondé sur la monétisation des données.

### Chiffres et tendances
- **365 Md$** : taille du marché data brokers mondial (2023)
- **5 Md$** : amende FTC à Facebook pour Cambridge Analytica (2019) — record mondial
- **40 M€** : amende CNIL à Criteo (2023)
- **8,25 Md€** : total des amendes européennes à Google sur 2017-2024 (antitrust + RGPD)
- Le **Privacy Sandbox** de Google (remplacement des cookies tiers) est un enjeu structurant pour l'avenir de la publicité digitale — report de la dépréciation des cookies à 2025

## Flashcards
#flashcards

Qu'est-ce qu'un data broker et comment collecte-t-il ses données ? :: Entreprise dont le modèle économique repose sur la collecte, l'agrégation et la revente de données sur des individus, sans relation directe avec eux. Sources : données publiques (registres, actes civils), programmes de fidélité rachetés, pixels de tracking web, applications mobiles, données télécoms.

Quelle est la thèse centrale du "capitalisme de surveillance" de Zuboff ? :: Le comportement humain est la matière première gratuite transformée en données comportementales, vendues comme "produits de prédiction" aux marchés publicitaires. Les plateformes ne vendent pas un service aux utilisateurs : elles vendent les prédictions comportementales des utilisateurs aux annonceurs.

Comment Cambridge Analytica a-t-elle obtenu les données de 87 millions de profils Facebook ? :: Via une application Facebook ("thisisyourdigitallife") consentie par 270 000 utilisateurs, mais qui exploitait les permissions de l'API Facebook de l'époque pour également collecter les données des amis de ces utilisateurs — sans leur consentement. Le modèle OCEAN construisait des profils psychologiques utilisés pour du ciblage politique.

Quelle est la différence entre la monétisation directe et indirecte des données ? :: Directe : les données sont vendues ou louées à des tiers (data brokers, data sharing B2B). Indirecte : les données améliorent des produits ou services qui génèrent des revenus (publicité ciblée, personnalisation, tarification dynamique) sans vente des données elles-mêmes.

Qu'est-ce que le "surplus comportemental" selon Zuboff ? :: Les données collectées au-delà de ce qui est nécessaire à l'amélioration du service (l'excédent). Par exemple, Google a besoin de savoir ce que vous cherchez pour vous donner des résultats pertinents, mais pas de connaître votre itinéraire, vos habitudes, vos états d'âme — cet excédent est capturé et vendu.

Qu'est-ce qu'un dark pattern et quel cadre réglementaire les combat ? :: Technique de design d'interface conçue pour pousser l'utilisateur vers une action non choisie librement (confirmshaming, roach motel, privacy zuckering). Le Digital Services Act (DSA) européen et les lignes directrices CNIL sanctionnent ces pratiques. La CNIL a émis des recommandations spécifiques sur les bannières cookies.

Pourquoi le modèle OCEAN est-il au cœur du scandale Cambridge Analytica ? :: Le modèle OCEAN (Big Five : Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) permet de prédire la personnalité d'un individu à partir de ses likes Facebook (10 likes = mieux qu'un collègue, 300 = mieux que le conjoint). Cambridge Analytica a utilisé ces profils pour cibler des messages politiques personnalisés lors des campagnes Brexit et Trump 2016.

## Sources
- Shoshana Zuboff – "The Age of Surveillance Capitalism" (PublicAffairs, 2019)
- CNIL – Décision Criteo 2023 : https://www.cnil.fr
- FTC – "FTC Imposes 5 Billion Penalty on Facebook" (2019) : https://www.ftc.gov
- IMARC Group – "Data Broker Market Report 2023" : https://www.imarcgroup.com
- The Guardian – Cambridge Analytica investigation : https://www.theguardian.com
- Commission européenne – Digital Services Act : https://eur-lex.europa.eu

## Notions liées
- [[Data Governance]]
- [[CLOUD Act et transferts de données]]
- [[Data Act]]
- [[Types d'analytics]]
- [[IA en cybersécurité]]
- [[Data Maturity et Data Literacy]]
