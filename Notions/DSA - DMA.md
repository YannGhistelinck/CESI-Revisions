---
type: notion
thèmes:
  - Big DATA
  - IA
statut: pas vu
dernière_révision: 
---

# DSA - DMA

![[N — DSA - DMA.mp3]]
## En bref
> **Définition** : Le **Digital Services Act** (DSA — Règlement UE 2022/2065) et le **Digital Markets Act** (DMA — Règlement UE 2022/1925) sont deux règlements européens formant le "paquet numérique" adopté en 2022, applicables respectivement depuis 2024. Le **DSA** régule la responsabilité des plateformes pour les contenus illicites, impose la transparence des algorithmes et protège les utilisateurs. Le **DMA** vise à contester le pouvoir de marché des grandes plateformes ("gatekeepers") pour garantir des marchés numériques équitables et contestables.
> **Pourquoi c'est important** : Pour les DSI et architectes data, le DSA impose des obligations techniques (transparence des systèmes de recommandation, accès aux données pour les chercheurs) et le DMA contraint les pratiques de collecte de données des gatekeepers (interopérabilité, partage de données, consentement). Ces textes ont un impact direct sur les modèles économiques des GAFAM en Europe et sur les droits des entreprises utilisant leurs plateformes.
> **Chiffres clés** :
> - DMA : 10 % du CA mondial annuel en cas de non-conformité (20 % en cas de récidive), voire démantèlement structurel.
> - DSA : 6 % du CA mondial annuel pour les très grandes plateformes (VLOP) en cas de non-conformité.
> - 17 gatekeepers désignés par la Commission européenne fin 2023 (Alphabet, Amazon, Apple, ByteDance, Meta, Microsoft, Booking.com).
> - 19 très grandes plateformes (VLOP) et moteurs de recherche (VLOSE) désignés au titre du DSA (>45 millions d'utilisateurs mensuels dans l'UE).

## Approfondir

### Fonctionnement

**Digital Services Act (DSA — Règlement UE 2022/2065)**

Applicable depuis le 17 février 2024 pour toutes les plateformes ; depuis août 2023 pour les VLOP/VLOSE.

Objectif : moderniser la directive e-commerce de 2000 en encadrant la responsabilité des plateformes pour les contenus et services illicites, et en renforçant les droits des utilisateurs dans l'espace numérique européen.

Architecture à paliers :
- **Tous les intermédiaires** : obligations de base (point de contact unique, rapport de transparence annuel, coopération avec les autorités).
- **Plateformes d'hébergement** : mécanisme de signalement et suppression des contenus illicites (notice-and-action), protection des signaleurs de confiance (trusted flaggers).
- **Grandes plateformes** (>45 M utilisateurs UE — VLOP) : obligations renforcées — systèmes de recommandation transparents (choix non basé sur le profilage), rapport de transparence sur la publicité ciblée, accès des chercheurs aux données, interdit de publicité ciblée pour les mineurs et basée sur des données sensibles.
- **Très grandes plateformes (VLOP) et moteurs de recherche (VLOSE)** : obligation d'évaluation annuelle des risques systémiques (désinformation, violence, santé mentale), audit indépendant annuel, partage de données avec les autorités et chercheurs, "Digital Services Coordinator" dans chaque État membre.

Supervision : la Commission européenne supervise directement les VLOP/VLOSE ; les coordinateurs nationaux des services numériques (CSN) — en France, l'ARCOM — supervisent les plateformes de taille intermédiaire.

**Digital Markets Act (DMA — Règlement UE 2022/1925)**

Applicable depuis le 2 mai 2023 ; première désignation des gatekeepers en septembre 2023.

Objectif : garantir la contestabilité et l'équité des marchés numériques en encadrant le comportement des "gatekeepers" — grandes plateformes systémiques contrôlant des "services de plateforme essentiels" (moteurs de recherche, réseaux sociaux, marketplaces, systèmes d'exploitation, navigateurs, assistants virtuels, publicité en ligne).

Critères de désignation gatekeeper : CA annuel européen ≥ 7,5 Md€ (ou valorisation ≥ 75 Md€), + service de plateforme essentiel avec ≥ 45 M d'utilisateurs mensuels actifs dans l'UE et ≥ 10 000 entreprises utilisatrices annuelles dans l'UE.

Obligations des gatekeepers ("dos") :
- Permettre l'interopérabilité avec les services tiers (messagerie : WhatsApp doit pouvoir échanger avec d'autres messageries)
- Partager les données avec les entreprises utilisatrices (marchands sur Amazon, développeurs sur App Store)
- Garantir la portabilité des données aux utilisateurs finaux
- Permettre aux entreprises de promouvoir leurs offres et conclure des contrats hors plateforme

Interdictions des gatekeepers ("don'ts") :
- Interdit de combiner les données personnelles entre différents services du gatekeeper sans consentement (ex : Meta ne peut plus croiser Facebook/Instagram/WhatsApp sans consentement explicite)
- Interdit de favoriser ses propres services dans les classements (auto-préférence — ex : Google Shopping)
- Interdit de préinstaller des applications de façon exclusive ou d'empêcher leur désinstallation
- Interdit de tracer les utilisateurs hors plateforme sans consentement (trackwall)

**Articulation DSA / DMA / RGPD**
| Texte | Objet | Autorité |
|-------|-------|----------|
| RGPD | Protection des données personnelles | CNIL, CEPD |
| DSA | Contenus illicites, transparence algorithmique, droits utilisateurs | Commission UE (VLOP), ARCOM (France) |
| DMA | Concurrence, équité des marchés numériques, gatekeepers | Commission UE (DG COMP) |
| AI Act | Systèmes d'IA à risque | Autorités nationales de surveillance IA |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction des contenus illicites (haine, désinformation) | Charge de conformité élevée pour les grandes plateformes |
| Transparence des algorithmes de recommandation | Risque de réduction des services personnalisés pour les utilisateurs |
| Ouverture des marchés numériques (DMA — interopérabilité) | Complexité d'implémentation de l'interopérabilité technique |
| Protection des mineurs (publicité ciblée interdite) | Possible ralentissement de l'innovation des petits acteurs par effet normatif |
| Accès des chercheurs aux données des VLOP | Résistance des gatekeepers (recours juridiques multiples) |
| Réduction du vendor lock-in des app stores | Risque de sécurité liée à l'ouverture des écosystèmes (sideloading) |

### Acteurs et solutions du marché

- **Gatekeepers désignés DMA (2023)** : Alphabet (Google Search, Maps, Shopping, Play, Android, Chrome, YouTube, Google Ads), Amazon (Marketplace, Amazon Ads), Apple (App Store, iOS, Safari, iMessage), ByteDance (TikTok), Meta (Facebook, Instagram, WhatsApp, Meta Ads), Microsoft (Windows, LinkedIn, Teams), Booking.com
- **VLOP/VLOSE désignés DSA** : les mêmes + Snapchat, Twitter/X, Zalando (a contesté sa désignation), Wikipedia (exemptée au titre de l'intérêt général)
- **Autorités de supervision** : Commission européenne (DG CONNECT pour le DSA, DG COMP pour le DMA), ARCOM (France — coordinateur DSN)
- **Chercheurs et ONG** : AlgorithmWatch, Mozilla, la Quadrature du Net — bénéficient de l'accès aux données DSA
- **Bénéficiaires DMA** : développeurs tiers, marchands sur marketplaces, concurrents des services des gatekeepers

### Cas d'usage concrets

1. **Interopérabilité WhatsApp (DMA)** : depuis 2024, Meta doit permettre aux utilisateurs d'autres messageries (Signal, Telegram, iMessage) d'envoyer des messages à des utilisateurs WhatsApp sans avoir un compte WhatsApp. Défi technique : harmoniser les protocoles de chiffrement de bout en bout. Meta a ouvert une API d'interopérabilité mais les premières implémentations montrent des limitations pratiques.

2. **Choix du moteur de recherche (DMA — Apple/Google)** : Apple et Google doivent proposer un écran de choix de moteur de recherche aux nouveaux utilisateurs de leurs OS/navigateurs, sans pré-sélectionner leur propre moteur. Mesure similaire au "ballot screen" imposé à Microsoft pour les navigateurs en 2009 (UE).

3. **Transparence des recommandations YouTube (DSA)** : YouTube doit proposer aux utilisateurs européens une option de recommandation non basée sur le profilage comportemental. Les chercheurs accrédités peuvent accéder aux données sur le fonctionnement de l'algorithme via l'API de recherche de données DSA.

4. **Publicité ciblée sur les mineurs (DSA)** : Meta a annoncé la suppression de la publicité ciblée basée sur des données personnelles pour les utilisateurs de moins de 18 ans en Europe, conformément à l'article 28(b) DSA. Résultat : réduction du revenu publicitaire sur ce segment, mais conformité légale.

5. **Audit des risques systémiques (DSA — TikTok)** : TikTok, désigné VLOP, doit réaliser une évaluation annuelle des risques systémiques de sa plateforme (désinformation, santé mentale des adolescents, ingérence électorale). La Commission européenne a ouvert une procédure formelle contre TikTok en 2024 pour soupçon de non-conformité DSA.

### Chiffres et tendances

- La Commission européenne a ouvert des procédures formelles DMA contre Alphabet, Apple et Meta en 2024 pour non-conformité.
- Apple a été condamné à une amende de 1,8 Md€ par la Commission européenne en 2024 pour restrictions anticoncurrentielles sur l'App Store (article 102 TFUE, préfigurant le DMA).
- TikTok : procédure DSA ouverte en 2024, notamment sur la protection des mineurs et les contenus illicites.
- Le "sideloading" imposé par le DMA sur iOS (possibilité d'installer des apps hors App Store) est actif depuis mars 2024 dans l'UE — Apple a contesté cette mesure devant les tribunaux européens.
- Zalando a contesté sa désignation comme VLOP devant la CJUE (2023), arguant que sa plateforme n'est pas systémique comme les GAFAM. La CJUE a maintenu sa désignation.

## Flashcards
#flashcards/Big_DATA/DSA_DMA #flashcards/IA/DSA_DMA

Quelle est la différence fondamentale entre le DSA et le DMA ? :: Le DSA régule la responsabilité des plateformes pour les contenus illicites et protège les utilisateurs (transparence algorithmique, droits en ligne). Le DMA régule la concurrence sur les marchés numériques en imposant des obligations aux gatekeepers pour garantir des marchés équitables et contestables.

Quels sont les critères de désignation d'un gatekeeper au sens du DMA ? :: CA européen annuel ≥ 7,5 Md€ ou valorisation ≥ 75 Md€, ET service de plateforme essentiel avec ≥ 45 M utilisateurs actifs mensuels dans l'UE et ≥ 10 000 entreprises utilisatrices dans l'UE.

Quelles sont les sanctions maximales prévues par le DSA et le DMA ? :: DSA : 6 % du CA mondial annuel pour les VLOP/VLOSE. DMA : 10 % du CA mondial (20 % en cas de récidive), avec possibilité de remèdes structurels (démantèlement) en cas de violation systémique.

Qu'interdit le DMA en matière de combinaison de données personnelles ? :: Le DMA interdit aux gatekeepers de combiner les données personnelles issues de différents services (ex : Facebook + Instagram + WhatsApp) sans consentement explicite et éclairé de l'utilisateur.

Qu'est-ce qu'une VLOP et quelles obligations spécifiques lui impose le DSA ? :: Very Large Online Platform : plateforme avec > 45 M utilisateurs actifs mensuels dans l'UE. Obligations spécifiques : évaluation annuelle des risques systémiques, audit indépendant, accès des chercheurs aux données, choix de recommandation non basée sur le profilage, interdiction de publicité ciblée pour les mineurs.

Qu'est-ce que l'obligation d'interopérabilité imposée par le DMA et quel est l'exemple concret ? :: Les gatekeepers proposant des services de messagerie doivent permettre l'interopérabilité avec d'autres messageries. Exemple concret : WhatsApp doit permettre aux utilisateurs de Signal ou Telegram de lui envoyer des messages sans avoir un compte WhatsApp, via une API d'interopérabilité ouverte depuis 2024.

Quelle est l'autorité française compétente pour le DSA et comment s'appelle-t-elle ? :: L'ARCOM (Autorité de Régulation de la Communication Audiovisuelle et Numérique) est le coordinateur national des services numériques (CSN) en France au titre du DSA.

## Sources

- DSA — Règlement (UE) 2022/2065 : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R2065
- DMA — Règlement (UE) 2022/1925 : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R1925
- Commission européenne — liste des gatekeepers et VLOP : https://digital-markets-act.ec.europa.eu/
- ARCOM — coordinateur DSN France : https://www.arcom.fr/
- Commission européenne, procédures DMA 2024 contre Alphabet, Apple, Meta
- AlgorithmWatch — rapports sur les algorithmes des VLOP : https://algorithmwatch.org/

## Notions liées

- [[RGPD]]
- [[Profilage et surveillance]]
- [[Souveraineté numérique]]
- [[Réglementations internationales sur les données]]
- [[Data Act]]
- [[NIS2]]
- [[IA en cybersécurité]]
