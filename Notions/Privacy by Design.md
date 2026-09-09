---
type: notion
thèmes:
  - Big DATA
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Privacy by Design

## En bref
> **Définition** : Le **Privacy by Design** (PbD) est une approche méthodologique consistant à intégrer la protection de la vie privée dès la conception d'un système, d'un produit ou d'un processus — et non en correctif après coup. Le **Privacy by Default** (PbDD) impose que les paramètres par défaut soient les plus protecteurs possible. Ces deux principes sont consacrés à l'article 25 du RGPD. L'**anonymisation** rend irréversiblement impossible la ré-identification d'une personne ; la **pseudonymisation** remplace les identifiants directs par des pseudonymes, mais la ré-identification reste possible avec une clé. Le **DPIA** (Data Protection Impact Assessment) est l'étude d'impact sur la vie privée obligatoire pour les traitements à risque élevé.
> **Pourquoi c'est important** : Dans les projets Big Data, les volumes et la variété des données augmentent considérablement le risque de ré-identification. Intégrer le PbD dès l'architecture évite des correctifs coûteux, réduit les risques de sanctions RGPD et constitue un argument de confiance commerciale (privacy as a competitive advantage).
> **Chiffres clés** :
> - L'article 25 du RGPD impose le PbD et le PbDD à toute organisation traitant des données personnelles dans l'UE depuis mai 2018.
> - Le CEPD estime que 70 % des violations de données auraient pu être évitées ou atténuées par une approche PbD.
> - La CNIL a sanctionné des organisations pour absence de DPIA sur des traitements à risque élevé, avec des amendes pouvant atteindre 4 % du CA mondial.

## Approfondir

### Fonctionnement

**Privacy by Design — Les 7 principes fondateurs (Ann Cavoukian, 1995)**
1. **Proactif, pas réactif** : anticiper les atteintes à la vie privée avant qu'elles surviennent.
2. **Vie privée par défaut** : sans action de l'utilisateur, les paramètres les plus protecteurs s'appliquent.
3. **Vie privée intégrée à la conception** : la protection n'est pas un ajout, mais une composante architecturale.
4. **Fonctionnalité totale** : pas de compromis entre vie privée et fonctionnalité (jeu à somme positive).
5. **Sécurité de bout en bout** : protection sur tout le cycle de vie de la donnée.
6. **Visibilité et transparence** : composants et pratiques vérifiables par des tiers.
7. **Respect de la vie privée des utilisateurs** : centrage sur l'utilisateur, consentement éclairé.

**Privacy by Default (article 25 RGPD)**
Obligation de traiter, par défaut, uniquement les données strictement nécessaires à la finalité déclarée. Exemple : un formulaire d'inscription ne collecte pas le numéro de téléphone si ce n'est pas nécessaire au service. Les paramètres de partage sur les réseaux sociaux doivent être configurés sur "privé" par défaut.

**Anonymisation**
Traitement irréversible rendant impossible la ré-identification directe ou indirecte d'une personne. Une donnée véritablement anonymisée échappe au champ d'application du RGPD. Techniques : généralisation (remplacer une valeur précise par une plage), suppression, agrégation statistique, bruit différentiel (differential privacy). Critères CNIL/CEPD : résistance à la singularisation, à la liaison et à l'inférence.

**Pseudonymisation**
Remplacement des identifiants directs (nom, email) par un pseudonyme (hash, token). La ré-identification reste possible avec la table de correspondance. La donnée pseudonymisée reste une donnée personnelle au sens du RGPD, mais sa pseudonymisation est une mesure de sécurité reconnue à l'article 32. Exemples : tokenisation des numéros de carte bancaire (PCI-DSS), hashage des identifiants dans les logs.

**Ré-identification**
Processus de recombination de données supposément anonymes pour retrouver l'identité d'un individu. Exemples célèbres : Latanya Sweeney (1997) a ré-identifié 87 % des Américains avec code postal + date de naissance + sexe ; Netflix Prize dataset (2006) ré-identifié par corrélation avec IMDb. Risque particulièrement élevé dans les jeux de données Big Data (croisement de sources).

**DPIA — Data Protection Impact Assessment (article 35 RGPD)**
Étude d'impact obligatoire avant tout traitement susceptible d'engendrer un risque élevé pour les droits et libertés des personnes. Cas typiques : surveillance à grande échelle, profilage automatisé, traitement de données sensibles, traitement de données de personnes vulnérables. Contenu minimal : description du traitement et de sa finalité, évaluation de la nécessité/proportionnalité, identification et gestion des risques, mesures prévues. Si les risques résiduels restent élevés après mesures : consultation préalable de la CNIL obligatoire.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction des risques de violation de données | Coût de conception initial plus élevé |
| Conformité RGPD intégrée dès la conception | Complexité d'implémentation dans les systèmes legacy |
| Avantage concurrentiel (confiance utilisateurs) | L'anonymisation parfaite est souvent illusoire en Big Data |
| Réduction des coûts de mise en conformité tardive | Tension entre utilité analytique et minimisation des données |
| Protection contre les ré-identifications | Nécessite une culture data privacy dans toutes les équipes |

### Acteurs et solutions du marché

- **Outils de pseudonymisation/anonymisation** : ARX Data Anonymization Tool (open source), Privitar, BigID, Immuta
- **Differential Privacy** : Apple (iOS, données d'usage), Google (RAPPOR, DP Library), Apple/Google COVID-19 contact tracing
- **DPIA** : logiciels dédiés (OneTrust, TrustArc, Didomi), templates CNIL disponibles gratuitement
- **Autorités de référence** : CNIL (France), CEPD (Europe), ICO (Royaume-Uni) — publications de lignes directrices PbD
- **Organismes de certification** : certification PbD selon article 42 RGPD en développement (CNIL/CEPD)
- **Frameworks** : NIST Privacy Framework, ISO 31700 (Privacy by Design — publié en 2023)

### Cas d'usage concrets

1. **Système de santé et DPIA** : un hôpital déploie un entrepôt de données de santé pour la recherche. Le DPIA identifie un risque élevé de ré-identification (données rares, pathologies spécifiques). Mesures : pseudonymisation des identifiants patients, agrégation des données rares (k-anonymat k≥5), contrôle d'accès par rôle, journalisation des accès. Consultation CNIL préalable requise.

2. **Application mobile et Privacy by Default** : une application de fitness collecte par défaut uniquement les données strictement nécessaires (activité physique). Le partage de localisation et l'analyse comportementale sont désactivés par défaut et nécessitent un consentement explicite supplémentaire. Conformité article 25 RGPD.

3. **Data Lake et minimisation** : une DSI construit un data lake pour l'analytique. Approche PbD : hashage des identifiants à l'ingestion (pseudonymisation), suppression automatique des champs non nécessaires à la finalité analytique, politique de rétention différenciée par type de donnée, chiffrement au repos avec clés gérées par le client (BYOK).

4. **Anonymisation de logs réseau** : un RSSI anonymise les adresses IP dans les logs analytiques (suppression des 3 derniers octets) tout en conservant les logs bruts dans un silo sécurisé pour la forensique. La donnée analytique échappe au RGPD ; la donnée brute est soumise à des règles de rétention strictes.

### Chiffres et tendances

- ISO 31700 "Privacy by Design for Consumer Goods and Services" publié en janvier 2023 : premier standard international formalisant le PbD.
- L'avis 05/2014 du groupe de travail article 29 (WP29) définit les critères d'anonymisation valide : résistance à la singularisation, à la liaison et à l'inférence.
- Differential Privacy : Apple utilise la DP depuis 2016 pour collecter des statistiques d'usage iOS sans identifier les utilisateurs individuels.
- Selon Gartner, d'ici 2025, 75 % des organisations devront adopter des mécanismes de PbD pour leurs projets Big Data afin de respecter les réglementations mondiales croissantes.
- La CNIL a publié en 2023 un guide pratique sur les techniques d'anonymisation incluant le bruit différentiel et le k-anonymat.

## Flashcards
#flashcards

Quels sont les 7 principes fondateurs du Privacy by Design selon Ann Cavoukian ? :: 1. Proactif, pas réactif ; 2. Vie privée par défaut ; 3. Vie privée intégrée à la conception ; 4. Fonctionnalité totale (jeu à somme positive) ; 5. Sécurité de bout en bout ; 6. Visibilité et transparence ; 7. Respect centré sur l'utilisateur.

Quelle est la différence entre anonymisation et pseudonymisation ? :: L'anonymisation est irréversible (ré-identification impossible) et la donnée sort du champ du RGPD. La pseudonymisation remplace les identifiants par des pseudonymes mais la ré-identification reste possible avec la clé de correspondance — la donnée reste personnelle au sens du RGPD.

Qu'est-ce qu'un DPIA et quand est-il obligatoire ? :: Data Protection Impact Assessment : étude d'impact sur la protection des données, obligatoire (article 35 RGPD) avant tout traitement à risque élevé (surveillance à grande échelle, profilage, données sensibles). Si le risque résiduel reste élevé, la consultation préalable de la CNIL est requise.

Qu'imposent l'article 25 du RGPD et le Privacy by Default ? :: L'article 25 impose d'intégrer la protection des données dès la conception (PbD) et de configurer les paramètres les plus protecteurs par défaut (PbDD), sans action de l'utilisateur.

Quels sont les trois critères d'une anonymisation valide selon le WP29/CEPD ? :: Résistance à la singularisation (ne pas isoler un individu), résistance à la liaison (ne pas relier des enregistrements), résistance à l'inférence (ne pas déduire des informations sur un individu).

Qu'est-ce que la ré-identification et pourquoi est-elle particulièrement risquée en Big Data ? :: La ré-identification consiste à retrouver l'identité d'une personne à partir de données supposément anonymes par croisement de sources. En Big Data, la multiplicité des sources et la richesse des données augmentent exponentiellement ce risque (ex. : Sweeney — 87 % des Américains ré-identifiables avec 3 attributs).

Qu'est-ce que la differential privacy et qui l'utilise ? :: Technique mathématique ajoutant du bruit statistique aux données pour protéger l'identité individuelle tout en préservant la précision des statistiques agrégées. Utilisée par Apple (iOS depuis 2016), Google (RAPPOR), et dans les protocoles de contact tracing COVID-19.

## Sources

- RGPD — Règlement (UE) 2016/679, articles 25 et 35 : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679
- CEPD, Lignes directrices 4/2019 sur l'article 25 (Privacy by Design et by Default) : https://edpb.europa.eu/
- CNIL, Guide pratique sur l'anonymisation : https://www.cnil.fr/
- Ann Cavoukian, "Privacy by Design: The 7 Foundational Principles", 2009
- ISO 31700:2023, Privacy by Design for Consumer Goods and Services
- Latanya Sweeney, "Simple Demographics Often Identify People Uniquely", Carnegie Mellon University, 2000
- Groupe de travail article 29, Avis 05/2014 sur les techniques d'anonymisation

## Notions liées

- [[RGPD]]
- [[Profilage et surveillance]]
- [[Data Lifecycle Management]]
- [[ISO 27001 - 27002]]
- [[Normes ISO liées aux données]]
- [[CLOUD Act et transferts de données]]
- [[Réglementations internationales sur les données]]
