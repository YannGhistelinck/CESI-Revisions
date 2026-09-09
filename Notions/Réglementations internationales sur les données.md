---
type: notion
thèmes:
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Réglementations internationales sur les données

## En bref
> **Définition** : Face à la fragmentation réglementaire mondiale, plusieurs grandes lois de protection des données personnelles coexistent avec le RGPD européen : le **CCPA** (California Consumer Privacy Act, 2020, renforcé par le CPRA en 2023), la **LGPD** (Lei Geral de Proteção de Dados, Brésil, 2020) et la **PIPL** (Personal Information Protection Law, Chine, 2021). Ces textes s'inspirent partiellement du RGPD tout en reflétant les spécificités juridiques et géopolitiques de leurs pays d'origine. Pour les organisations opérant à l'international, la gestion de cette pluralité réglementaire est un enjeu majeur de conformité et de gouvernance des données.
> **Pourquoi c'est important** : Une multinationale ou un éditeur SaaS commercialisant ses services en Californie, au Brésil et en Chine est simultanément soumis au RGPD, au CCPA, à la LGPD et à la PIPL. Les exigences varient : droits des personnes, bases légales, transferts internationaux, amendes. La convergence vers un modèle "RGPD-like" est réelle, mais des divergences structurelles persistent.
> **Chiffres clés** :
> - Plus de 160 pays ont adopté une législation de protection des données personnelles en 2023 (UNCTAD).
> - CCPA/CPRA : amendes jusqu'à 7 500 $ par violation intentionnelle ; le CPRA crée la California Privacy Protection Agency (CPPA), première agence dédiée aux USA.
> - LGPD : amendes jusqu'à 2 % du chiffre d'affaires de l'entreprise au Brésil, plafonnées à 50 M BRL par infraction (~9 M€).
> - PIPL : amendes jusqu'à 50 M CNY (~6,5 M€) ou 5 % du CA annuel en Chine ; responsables personnes physiques peuvent être personnellement sanctionnés.

## Approfondir

### Fonctionnement

**CCPA / CPRA (Californie, USA)**

Le **California Consumer Privacy Act** (CCPA) est entré en vigueur le 1er janvier 2020. Renforcé par le **California Privacy Rights Act** (CPRA) applicable depuis le 1er janvier 2023, qui crée une agence dédiée (California Privacy Protection Agency — CPPA) et aligne certains droits sur le RGPD.

Champ d'application : entreprises à but lucratif collectant des données de résidents californiens et dépassant l'un des seuils suivants — CA annuel > 25 M$, traitant les données de > 100 000 consommateurs/ménages par an, ou tirant > 50 % de leurs revenus de la vente de données personnelles.

Droits des consommateurs : droit de savoir (quelles données sont collectées), droit de suppression, droit d'opposition à la vente de données (opt-out), droit à la non-discrimination (ne pas être pénalisé pour l'exercice des droits), droit de corriger (ajouté par CPRA), droit de limiter l'utilisation des données sensibles (CPRA).

Spécificités vs RGPD : pas de base légale obligatoire (pas de consentement requis par défaut pour la collecte, sauf données sensibles), logique d'opt-out plutôt que d'opt-in, pas de DPO obligatoire, champ limité aux entreprises dépassant les seuils.

**LGPD (Brésil)**

La **Lei Geral de Proteção de Dados Pessoais** est entrée en vigueur en septembre 2020, avec application des sanctions depuis août 2021. Fortement inspirée du RGPD européen.

Similitudes avec le RGPD : 10 bases légales (dont consentement, intérêt légitime, objet contrat), droits des personnes (accès, rectification, effacement, portabilité, opposition, révocation du consentement), DPO ("Encarregado") recommandé (obligatoire pour les traitements à grande échelle), ANPD (Autoridade Nacional de Proteção de Dados) comme autorité de contrôle.

Différences notables : inclut des bases légales spécifiques au contexte brésilien (protection du crédit, tutelle de la santé), champ d'application territorial plus large (s'applique à tout traitement réalisé au Brésil ou dont les données traitées sont collectées au Brésil), régime de transfert international moins détaillé qu'en Europe.

**PIPL (Chine)**

La **Personal Information Protection Law** est entrée en vigueur le 1er novembre 2021 — première loi globale de protection des données en Chine. S'applique aux organisations traitant des données de personnes en Chine, y compris les entreprises étrangères.

Points clés : consentement comme base légale principale (distincts du RGPD qui donne 6 bases équivalentes), droits des personnes (accès, rectification, effacement, portabilité, explication des décisions automatisées), Évaluation de Protection des Informations Personnelles (EPIA) obligatoire pour les traitements à risque (analogue au DPIA), désignation d'un responsable de protection des données pour les grandes organisations.

Divergences majeures avec le RGPD : **transferts internationaux** soumis à des conditions strictes — certification de sécurité par l'autorité chinoise (CAC), conclusion d'un accord standard, ou avis de la CAC. La PIPL s'inscrit dans un cadre plus large incluant la **Cybersecurity Law** (2017) et la **Data Security Law** (2021), qui imposent des exigences de localisation des données pour certaines catégories (données critiques, données de santé) et de contrôle étatique.

Contexte géopolitique : la PIPL permet à la Chine de contrôler les transferts de données à l'étranger dans une logique de souveraineté numérique, tout en offrant une protection formelle aux citoyens chinois. La frontière avec la surveillance d'État reste floue.

**Comparaison synthétique**

| Critère | RGPD (UE) | CCPA/CPRA (Californie) | LGPD (Brésil) | PIPL (Chine) |
|---------|-----------|------------------------|---------------|--------------|
| En vigueur | Mai 2018 | Jan. 2020 / Jan. 2023 | Sept. 2020 | Nov. 2021 |
| Bases légales | 6 bases équivalentes | Pas de base légale obligatoire | 10 bases | Consentement central |
| Opt-in / Opt-out | Opt-in (consentement) | Opt-out (vente de données) | Opt-in (consentement) | Opt-in (consentement) |
| DPO / Équivalent | DPO (obligatoire sous conditions) | Pas d'équivalent | Encarregado (recommandé) | Responsable désigné |
| Autorité de contrôle | CEPD + autorités nationales | CPPA (Californie) | ANPD | CAC (Cyberspace Administration of China) |
| Amende max | 4 % CA mondial ou 20 M€ | 7 500 $ par violation intentionnelle | 2 % CA brésil (50 M BRL max) | 5 % CA Chine ou 50 M CNY |
| Transferts internationaux | Décision d'adéquation, CCT, BCR | Pas de régime spécifique | Standard contractuel, autorisation ANPD | Certification CAC, standard contractuel CAC |

### Avantages / Inconvénients
| Perspective | Avantages | Inconvénients |
|-------------|-----------|---------------|
| Organisations mondiales | Tendance à la convergence vers des standards communs | Complexité de la conformité multi-juridictionnelle |
| Individus | Protection croissante dans un nombre croissant de pays | Droits moins forts hors UE (notamment USA, hors Californie) |
| RGPD comme standard mondial | Effet d'entraînement positif sur les législations mondiales | Risque de fragmentation réglementaire ("splinternet") |

### Acteurs et solutions du marché

- **Autorités de contrôle** : CPPA (Californie), ANPD (Brésil), CAC (Chine — Cyberspace Administration of China)
- **Outils de conformité multi-juridictionnelle** : OneTrust, TrustArc, Securiti.ai — permettent de gérer les obligations RGPD + CCPA + LGPD + PIPL en parallèle
- **Cabinets juridiques spécialisés** : Bird & Bird, Fieldfisher, DLA Piper (expertise privacy internationale)
- **Frameworks de référence** : APEC Cross-Border Privacy Rules (CBPR) — cadre volontaire Asie-Pacifique, ISO 27701 (gestion de la protection des données, applicable quelle que soit la juridiction)
- **UNCTAD (ONU)** : publie un rapport annuel sur l'état des législations mondiales sur les données personnelles

### Cas d'usage concrets

1. **SaaS européen se déployant en Californie** : un éditeur de logiciel RH basé en France, déjà conforme au RGPD, se déploie aux USA. Il doit analyser si son chiffre d'affaires en Californie et le nombre de consommateurs californiens dépassent les seuils CCPA/CPRA. Si oui : ajout d'un lien "Do Not Sell or Share My Personal Information" sur le site, mise à jour de la politique de confidentialité, processus de gestion des droits californiens (délai de 45 jours).

2. **Expansion au Brésil** : un retailer français ouvre une plateforme e-commerce au Brésil. Il doit nommer un Encarregado (équivalent DPO), adapter sa politique de confidentialité en portugais avec les bases légales LGPD, mettre en place un mécanisme de recueil du consentement conforme à la LGPD, et s'assurer que les transferts de données vers l'Europe sont encadrés par des clauses standards ANPD (en développement).

3. **Entreprise française opérant en Chine** : un constructeur automobile implante une usine en Chine avec un système de gestion des employés. Les données des employés sont traitées en Chine et potentiellement transférées vers le siège en France. La PIPL exige : consentement explicite des employés, EPIA (étude d'impact), certification CAC ou contrat standard CAC pour le transfert vers la France. Les données critiques (selon la DSL) doivent rester en Chine.

### Chiffres et tendances

- En 2023, 71 % des pays dans le monde ont adopté une loi de protection des données personnelles, contre 40 % en 2010 (UNCTAD).
- Tendance à la "RGPD-isation" mondiale : Inde (DPDPA, 2023), Thaïlande (PDPA, 2022), Australie (révision du Privacy Act en cours), Canada (révision du PIPEDA via le projet C-27).
- L'Inde a adopté le **Digital Personal Data Protection Act** (DPDPA) en août 2023, applicable aux données traitées en Inde ou aux données indiennes traitées hors Inde pour offrir des biens/services.
- La fragmentation réglementaire engendre un coût estimé à 2-4 % du budget IT pour la conformité multi-juridictionnelle dans les grandes organisations (Gartner, 2023).

## Flashcards
#flashcards/Big_DATA/Réglementations_internationales_sur_les_données

Quels sont les seuils d'application du CCPA/CPRA pour une entreprise ? :: L'entreprise doit dépasser l'un des seuils : CA annuel > 25 M$, ou traitement des données de > 100 000 consommateurs/ménages californiens par an, ou > 50 % des revenus issus de la vente de données personnelles.

Quelle est la principale différence de logique entre le RGPD et le CCPA en matière de consentement ? :: Le RGPD est fondé sur l'opt-in (consentement préalable requis pour la collecte), tandis que le CCPA est fondé sur l'opt-out (la collecte est autorisée par défaut mais le consommateur peut s'y opposer, notamment à la "vente" de ses données).

Quelle est la LGPD et en quoi ressemble-t-elle au RGPD ? :: La Lei Geral de Proteção de Dados (Brésil, 2020) est fortement inspirée du RGPD : 10 bases légales, droits d'accès/rectification/effacement/portabilité, Encarregado (équivalent DPO), autorité de contrôle ANPD, DPIA pour les traitements à risque élevé.

Quelles sont les spécificités de la PIPL chinoise par rapport au RGPD ? :: La PIPL (Chine, 2021) place le consentement comme base légale centrale (vs 6 bases équivalentes dans le RGPD), impose des conditions strictes pour les transferts internationaux (certification CAC), s'inscrit dans un écosystème incluant la Cybersecurity Law et la Data Security Law, avec des exigences de localisation des données critiques.

Qu'est-ce que la CPPA et quel est son rôle ? :: La California Privacy Protection Agency est la première agence américaine dédiée à la protection des données personnelles, créée par le CPRA (2023). Elle est chargée d'appliquer le CCPA/CPRA, d'édicter des règlements et de prononcer des sanctions.

Quel est l'impact de la fragmentation réglementaire mondiale pour les DSI ? :: Obligation de gérer des conformités multiples et parfois contradictoires (RGPD + CCPA + LGPD + PIPL…), coût de conformité élevé (2-4 % du budget IT), nécessité d'outils dédiés (OneTrust, TrustArc) et d'expertise juridique internationale, risque de transferts de données non conformes.

## Sources

- RGPD — Règlement (UE) 2016/679 : https://eur-lex.europa.eu/
- CCPA/CPRA — California Office of the Attorney General : https://oag.ca.gov/privacy/ccpa
- LGPD — Lei n° 13.709/2018 (Brésil) : https://www.planalto.gov.br/
- ANPD (Brésil) : https://www.gov.br/anpd/
- PIPL — Cyberspace Administration of China : http://www.cac.gov.cn/
- UNCTAD, "Data Protection and Privacy Legislation Worldwide", 2023 : https://unctad.org/
- IAPP (International Association of Privacy Professionals) — comparateur de lois mondiales : https://iapp.org/resources/article/us-state-privacy-legislation-tracker/
- Inde — Digital Personal Data Protection Act, 2023 : https://www.meity.gov.in/

## Notions liées

- [[RGPD]]
- [[CLOUD Act et transferts de données]]
- [[Privacy by Design]]
- [[Souveraineté numérique]]
- [[DSA - DMA]]
- [[Normes ISO liées aux données]]
