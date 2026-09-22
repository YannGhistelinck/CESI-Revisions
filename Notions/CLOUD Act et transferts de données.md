---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Big DATA
  - Mobilité
statut: pas vu
dernière_révision: 
---

# CLOUD Act et transferts de données

![[N — CLOUD Act et transferts de données.mp3]]
## En bref
> **Définition** : Le CLOUD Act (Clarifying Lawful Overseas Use of Data Act, 2018) est une loi fédérale américaine permettant aux autorités américaines de contraindre des entreprises de droit américain à fournir des données stockées à l'étranger. Il s'inscrit dans un cadre plus large incluant FISA Section 702 (surveillance des non-Américains) et génère des conflits de juridiction avec le RGPD européen, illustrés par les arrêts Schrems I et II.
> **Pourquoi c'est important** : Toute organisation utilisant AWS, Azure, Google Cloud ou Microsoft 365 utilise des services d'entreprises soumises au CLOUD Act. Les données peuvent donc théoriquement être accessibles par les autorités américaines, indépendamment de leur localisation physique. C'est l'argument central du cloud souverain.
> **Chiffres clés** :
> - 900+ demandes CLOUD Act adressées à Microsoft entre 2018 et 2022 (Microsoft Transparency Report)
> - L'arrêt Schrems II (2020) a invalidé le Privacy Shield, cadre utilisé pour 5 300 entreprises transférant des données UE vers les USA
> - Le Data Privacy Framework (successeur du Privacy Shield) a été adopté en juillet 2023 et compte déjà 3 500+ entreprises certifiées

## Approfondir

### Fonctionnement

**CLOUD Act (2018)**
Loi américaine qui modifie le Stored Communications Act. Elle permet à des agences gouvernementales américaines (FBI, DEA…) d'obtenir par ordonnance judiciaire (warrant) des données détenues par des opérateurs américains, même stockées hors des États-Unis. L'opérateur peut contester si les données concernent un ressortissant étranger et si la divulgation viole le droit de ce pays, mais la charge de la preuve lui appartient.

Mécanisme des "Executive Agreements" : le CLOUD Act prévoit des accords bilatéraux (ex. : USA-Royaume-Uni, 2019) permettant aux autorités d'un pays signataire d'accéder directement aux données détenues par des opérateurs de l'autre pays. Pas d'accord USA-UE à ce jour.

**FISA Section 702 (Foreign Intelligence Surveillance Act)**
Permet à la NSA et au FBI de surveiller les communications de ressortissants étrangers localisés hors des USA, sans mandat individuel, en contraignant les fournisseurs de services américains. Mécanismes : PRISM (collecte auprès des fournisseurs) et UPSTREAM (collecte sur les câbles internet). Renouvelé en 2024 pour 2 ans.

**Schrems II (Arrêt CJUE, 16 juillet 2020)**
La Cour de Justice de l'UE invalide le Privacy Shield (cadre de transfert UE-USA) au motif que la surveillance américaine (FISA 702, EO 12333) ne respecte pas les standards européens de protection des données. Conséquences : 
- Les Clauses Contractuelles Types (CCT) restent valides mais nécessitent une évaluation de transfert (TIA — Transfer Impact Assessment)
- Les entreprises doivent documenter pourquoi le pays destinataire offre une protection équivalente au RGPD

**Data Privacy Framework (DPF, juillet 2023)**
Successeur du Privacy Shield, négocié après Schrems II. Repose sur le décret exécutif américain (EO 14086) créant un mécanisme de recours pour les ressortissants européens contre la surveillance américaine (Cour de révision de la protection des données — DPRC). Critique principale : Max Schrems a annoncé un recours devant la CJUE, estimant que les garanties sont insuffisantes (possibilité d'un "Schrems III").

**Data residency**
Obligation ou choix de conserver les données dans une région géographique spécifique. Ne protège pas contre le CLOUD Act (un opérateur américain peut toujours être contraint), mais réduit les risques de certaines formes de surveillance et facilite la conformité RGPD. Différent de la souveraineté des données (qui concerne la juridiction applicable).

**Conflits de juridiction CLOUD Act vs RGPD**
Un opérateur américain stockant des données européennes est soumis simultanément au CLOUD Act (droit américain) et au RGPD (droit européen). En cas de réponse à une demande CLOUD Act sans notification de la personne concernée, l'opérateur peut violer le RGPD (obligation d'information). Ce conflit n'est pas résolu à ce jour.

### Avantages / Inconvénients
| Impact du CLOUD Act | Pour les organisations européennes |
|--------------------|-----------------------------------|
| Accès légitimé pour les enquêtes criminelles (argument USA) | Risque d'accès aux données sensibles par autorités étrangères |
| Accords bilatéraux pour la coopération judiciaire | Aucun accord USA-UE : asymétrie persistante |
| Transparence relative (transparency reports des GAFAM) | Ordonnances de non-divulgation (gag orders) interdisant d'informer le client |
| — | Conflict avec le RGPD non résolu |

### Acteurs et solutions du marché

- **Fournisseurs soumis au CLOUD Act** : AWS (Amazon), Microsoft Azure, Google Cloud, Meta, Apple — toutes entités de droit américain
- **Alternatives européennes hors CLOUD Act** : OVHcloud, Outscale (Dassault), IONOS (Deutsche Telekom), Exoscale (Suisse), Hetzner
- **Outils de conformité aux transferts** : DPA (Data Processing Agreements), TIA (Transfer Impact Assessment), CCT (Clauses Contractuelles Types) — modèles CEPD
- **Chiffrement souverain** : HSM (Hardware Security Module) avec clés sous contrôle du client (BYOK — Bring Your Own Key), S3NS/Bleu comme modèles "cloud de confiance"
- **Surveillance** : CEPD (Comité Européen de la Protection des Données), CNIL en France, Max Schrems / NOYB (association de défense)

### Cas d'usage concrets

1. **Hôpital français sur Microsoft 365** : un CHU utilise Microsoft 365. Microsoft est une entité américaine soumise au CLOUD Act. Même si les données sont hébergées en France (datacenter Azure West Europe), une ordonnance américaine pourrait contraindre Microsoft à fournir des données médicales sans en informer le CHU ni les patients (gag order). Réponse : migration vers Oodrive (SecNumCloud) pour les données sensibles.

2. **Multinationale et TIA** : un groupe français transfère des données RH vers une filiale américaine utilisant Workday (SaaS américain). La DSI réalise un Transfer Impact Assessment pour documenter que les CCT + mesures supplémentaires (chiffrement, pseudonymisation) offrent une protection équivalente au RGPD. Document conservé pour audit CNIL.

3. **Startup et Data Privacy Framework** : une startup SaaS française utilisant des sous-traitants américains vérifie qu'ils sont certifiés DPF (dataprivacyframework.gov). Elle documente cette vérification dans son registre des traitements. Risque résiduel : invalidation du DPF par la CJUE ("Schrems III").

### Chiffres et tendances

- FISA Section 702 : environ 250 000 "selectors" (identifiants surveillés) en 2022 (rapport annuel ODNI)
- DPF (Data Privacy Framework) : 3 500+ entreprises certifiées en 2024, mais recours de NOYB déjà déposé devant la CJUE
- En 2023, le Parlement européen a voté une résolution non contraignante critiquant le DPF comme "inadéquat"
- Tendance : émergence du "data sovereignty by design" — architecture applicative intégrant la souveraineté des données dès la conception (chiffrement client, BYOK, données jamais en clair chez le fournisseur)
- Le Executive Order 14086 (Biden, 2022) crée la DPRC pour les recours des européens, mais son indépendance est contestée

## Flashcards
#flashcards/Cloud_et_Virtualisation/CLOUD_Act_et_transferts_de_données #flashcards/Big_DATA/CLOUD_Act_et_transferts_de_données #flashcards/Mobilité/CLOUD_Act_et_transferts_de_données

Qu'est-ce que le CLOUD Act et à qui s'applique-t-il ? :: Loi américaine de 2018 permettant aux autorités US d'obtenir des données détenues par des opérateurs américains, quel que soit le pays de stockage. S'applique à toute entité de droit américain (AWS, Microsoft, Google…).

Qu'a invalidé l'arrêt Schrems II et pour quelle raison ? :: La CJUE a invalidé le Privacy Shield en juillet 2020, estimant que la surveillance américaine (FISA 702, EO 12333) ne garantit pas un niveau de protection équivalent au RGPD pour les données des européens transférées aux USA.

Qu'est-ce que le Data Privacy Framework et quel est son risque principal ? :: Successeur du Privacy Shield adopté en juillet 2023, basé sur l'EO 14086 créant un mécanisme de recours (DPRC). Risque principal : possible invalidation par la CJUE (recours NOYB — "Schrems III").

Quelle est la différence entre data residency et souveraineté des données ? :: La data residency désigne la localisation physique des données (région géographique). La souveraineté désigne la juridiction juridique applicable. Un opérateur américain peut héberger des données en France (data residency = FR) mais rester soumis au CLOUD Act (souveraineté = USA).

Qu'est-ce qu'un gag order dans le contexte CLOUD Act ? :: Ordonnance de non-divulgation accompagnant une demande d'accès aux données, interdisant à l'opérateur d'informer le client ou la personne concernée. Incompatible avec l'obligation RGPD d'informer les personnes de l'accès à leurs données.

Qu'est-ce que FISA Section 702 ? :: Disposition du Foreign Intelligence Surveillance Act permettant à la NSA/FBI de surveiller les communications de ressortissants étrangers hors USA, sans mandat individuel, via les fournisseurs américains (PRISM, UPSTREAM). Renouvelé en 2024.

Qu'est-ce qu'un Transfer Impact Assessment (TIA) ? :: Évaluation documentée réalisée par l'exportateur de données pour justifier que les CCT + mesures supplémentaires assurent une protection équivalente au RGPD dans le pays destinataire. Requis depuis Schrems II pour les transferts vers des pays sans décision d'adéquation.

## Sources

- CLOUD Act, Public Law 115-141, March 2018 (texte officiel)
- CJUE, arrêt C-311/18, "Data Protection Commissioner v Facebook Ireland Limited and Maximillian Schrems" (Schrems II), 16 juillet 2020
- Décision d'adéquation UE-USA (Data Privacy Framework), Commission européenne, 10 juillet 2023
- CEPD, "Recommandations 01/2020 sur les mesures qui complètent les outils de transfert"
- Microsoft, "Law Enforcement Requests Report", 2022
- NOYB (Max Schrems), communiqués officiels sur le DPF

## Notions liées

- [[Cloud souverain]]
- [[Vendor lock-in et réversibilité]]
- [[Modèles de déploiement cloud]]
- [[Data Lifecycle Management]]
- [[NIS2]]
- [[ISO 27001 - 27002]]
