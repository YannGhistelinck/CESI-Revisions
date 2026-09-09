---
type: notion
thèmes:
  - Big DATA
  - Cybersécurité
  - Cloud et Virtualisation
  - Mobilité
  - IA
statut: pas vu
dernière_révision: 
---

# RGPD

## En bref
> **Définition** : Le **RGPD** (Règlement Général sur la Protection des Données — Règlement UE 2016/679) est le cadre réglementaire européen régissant le traitement des données à caractère personnel, applicable depuis le 25 mai 2018. Il repose sur 7 principes fondamentaux, 6 bases légales, un ensemble de droits pour les personnes et des obligations pour les responsables de traitement. Il s'applique à toute organisation traitant des données de résidents européens, quel que soit le pays d'établissement de l'organisation (principe d'extraterritorialité).
> **Pourquoi c'est important** : Le RGPD est la colonne vertébrale de la gouvernance des données en Europe. Il conditionne la conception des SI (Privacy by Design), l'usage du cloud, les projets IA (AI Act s'y articule), la mobilité (apps mobiles) et les transferts internationaux. Les sanctions peuvent atteindre 20 M€ ou 4 % du CA mondial annuel, au plus élevé des deux montants.
> **Chiffres clés** :
> - 4 % du CA mondial ou 20 M€ d'amende maximale (niveau le plus élevé)
> - Amazon : 746 M€ d'amende au Luxembourg (2021) — plus grosse amende RGPD à ce jour
> - Meta : 1,2 Md€ d'amende par la DPC irlandaise (2023) pour transferts illicites USA
> - Plus de 1 600 amendes RGPD prononcées en Europe depuis 2018 (CNIL, CEPD — bilan 2023)

## Approfondir

### Fonctionnement

**Les 7 principes fondamentaux (article 5 RGPD)**
1. **Licéité, loyauté, transparence** : traitement licite, loyal et transparent envers la personne concernée.
2. **Limitation des finalités** : données collectées pour des finalités déterminées, explicites et légitimes, non traitées de façon incompatible.
3. **Minimisation des données** : données adéquates, pertinentes et limitées à ce qui est nécessaire (principe du moindre privilège appliqué aux données).
4. **Exactitude** : données exactes et tenues à jour.
5. **Limitation de la conservation** : données conservées sous forme identifiable uniquement le temps nécessaire.
6. **Intégrité et confidentialité** : traitement assurant la sécurité appropriée (chiffrement, pseudonymisation…).
7. **Responsabilité (accountability)** : le responsable de traitement doit être en mesure de démontrer le respect de ces principes.

**Les 6 bases légales (article 6 RGPD)**
1. Consentement (libre, spécifique, éclairé, univoque — et révocable)
2. Exécution d'un contrat
3. Obligation légale
4. Sauvegarde des intérêts vitaux
5. Mission d'intérêt public
6. Intérêts légitimes du responsable de traitement (ne s'applique pas aux organismes publics)

**Droits des personnes concernées**
- **Article 13-14** : droit à l'information (lors de la collecte)
- **Article 15** : droit d'accès (copie des données traitées)
- **Article 16** : droit de rectification
- **Article 17** : droit à l'effacement ("droit à l'oubli")
- **Article 18** : droit à la limitation du traitement
- **Article 20** : droit à la portabilité (format structuré, lisible par machine)
- **Article 21** : droit d'opposition (notamment au profilage à des fins de marketing direct)
- **Article 22** : droit de ne pas faire l'objet d'une décision automatisée

**DPO — Délégué à la Protection des Données (articles 37-39)**
Désignation obligatoire pour : les autorités publiques, les organisations dont l'activité principale nécessite un suivi régulier et à grande échelle des personnes, ou le traitement à grande échelle de données sensibles. Mission : conseil, contrôle de la conformité, interface avec l'autorité de contrôle. Le DPO ne peut pas être sanctionné pour l'exercice de ses missions (indépendance fonctionnelle).

**CNIL (Commission Nationale de l'Informatique et des Libertés)**
Autorité de contrôle française (article 51 RGPD). Missions : contrôle du respect du RGPD, traitement des plaintes, publication de lignes directrices, prononcé de sanctions. Membre du CEPD (Comité Européen de la Protection des Données) pour la coordination européenne. Guichet unique (one-stop shop) : une entreprise établie dans un État membre traite avec l'autorité de contrôle de son principal établissement.

**Article 22 — Décisions automatisées et profilage**
Droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou significatifs. Exceptions : nécessité contractuelle, autorisation légale, consentement explicite. Dans les cas autorisés : obligation d'intervention humaine sur demande, droit à l'explication, droit de contester la décision. Particulièrement pertinent pour le scoring de crédit, la sélection de candidats, les décisions de tarification automatique.

**Article 28 — Sous-traitants**
Tout traitement par un sous-traitant doit faire l'objet d'un contrat (DPA — Data Processing Agreement) imposant au sous-traitant : agir uniquement sur instruction du responsable, garantir la confidentialité, mettre en place des mesures de sécurité, aider le responsable pour les droits des personnes et les DPIA, supprimer ou restituer les données en fin de contrat. Le sous-traitant peut recourir à un sous-traitant ultérieur sous réserve d'autorisation du responsable.

**Transferts de données hors UE (articles 44-49)**
Conditions pour transférer des données vers un pays tiers : décision d'adéquation de la Commission européenne (ex. : Japon, Canada, Royaume-Uni, Data Privacy Framework USA depuis 2023), clauses contractuelles types (CCT) avec Transfer Impact Assessment (TIA), règles d'entreprise contraignantes (BCR), dérogations spécifiques (consentement explicite, nécessité contractuelle…).

**Registre des traitements (article 30)**
Obligation pour tout responsable de traitement et sous-traitant de tenir un registre documentant tous les traitements : finalité, catégories de données et de personnes, destinataires, transferts, délais de conservation, mesures de sécurité. Exemption partielle pour les PME <250 salariés sauf si traitement régulier, à risque élevé ou portant sur des données sensibles.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Harmonisation réglementaire à l'échelle européenne | Complexité et coût de mise en conformité |
| Protection renforcée des droits des individus | Risque de surconformité (paralysie décisionnelle) |
| Avantage concurrentiel (confiance) | Charge administrative importante (registre, DPO, DPIA) |
| Extraterritorialité : protège les données des Européens mondialement | Interprétations divergentes entre États membres |
| Sanctions dissuasives | Difficulté d'application aux acteurs non-européens |

### Acteurs et solutions du marché

- **Autorités de contrôle** : CNIL (France), AEPD (Espagne), DPC (Irlande — compétente pour les GAFAM), BfDI (Allemagne), ICO (Royaume-Uni — RGPD UK post-Brexit)
- **Coordination européenne** : CEPD (Comité Européen de la Protection des Données) — lignes directrices, avis, règlement des litiges transfrontaliers
- **Outils de conformité** : OneTrust, TrustArc, Didomi (gestion du consentement), Privitar (anonymisation), BigID (découverte et classification des données)
- **Gestionnaires de consentement (CMP)** : Didomi, Axeptio, Cookiebot — pour la conformité des cookies et du consentement en ligne
- **Organismes de certification** : certification RGPD article 42 (en déploiement par les CNIL nationales)
- **Association de défense** : NOYB (None Of Your Business — Max Schrems), La Quadrature du Net

### Cas d'usage concrets

1. **DPA avec un prestataire SaaS** : une entreprise française utilise Salesforce CRM. Salesforce est sous-traitant au sens de l'article 28. Un DPA est obligatoire, précisant que Salesforce traite uniquement sur instruction du client, garantit la sécurité, permet les audits et restitue les données en fin de contrat. Transferts vers les USA encadrés par les CCT et le DPF.

2. **Exercice du droit à l'effacement** : un utilisateur demande la suppression de son compte et de toutes ses données personnelles. L'organisation dispose de 30 jours pour répondre. Elle doit supprimer les données dans tous ses systèmes (CRM, data warehouse, backups) ou justifier une exception (obligation légale de conservation). Les données anonymisées conservées pour la statistique ne sont pas concernées.

3. **DPIA pour une application de géolocalisation** : une app mobile de livraison trace la position en temps réel des livreurs et des clients. La DPIA identifie des risques élevés (données de localisation à grande échelle, personnes vulnérables). Mesures : minimisation de la fréquence de collecte, chiffrement, rétention limitée, information des personnes, droit d'opposition au suivi hors livraison active.

4. **Scoring automatique de candidats (article 22)** : un RH utilise un outil de tri automatique des CV. Il doit informer les candidats, leur permettre de demander une révision humaine et expliquer les critères utilisés. L'outil ne peut pas décider seul d'exclure un candidat sans possibilité de recours.

### Chiffres et tendances

- Bilan CEPD 2023 : 1 600+ amendes prononcées depuis 2018 pour un total de plus de 4,2 Md€.
- Les secteurs les plus sanctionnés : télécoms, médias, finance, santé.
- Meta : 1,2 Md€ (DPC Irlande, 2023) pour transferts USA illicites — amende record.
- 72 heures : délai maximal pour notifier une violation de données à l'autorité de contrôle (article 33 RGPD).
- Plus de 160 pays ont adopté une législation inspirée du RGPD depuis 2018 (UNCTAD, 2023).
- Le Data Privacy Framework (2023) établit une décision d'adéquation USA-UE, mais son avenir reste incertain (recours NOYB).

## Flashcards
#flashcards/Big_DATA/RGPD #flashcards/Cybersécurité/RGPD #flashcards/Cloud_et_Virtualisation/RGPD #flashcards/Mobilité/RGPD #flashcards/IA/RGPD

Quels sont les 7 principes fondamentaux du RGPD (article 5) ? :: Licéité/loyauté/transparence, limitation des finalités, minimisation des données, exactitude, limitation de la conservation, intégrité et confidentialité, responsabilité (accountability).

Quelles sont les 6 bases légales du traitement selon l'article 6 du RGPD ? :: Consentement, exécution d'un contrat, obligation légale, sauvegarde des intérêts vitaux, mission d'intérêt public, intérêts légitimes du responsable de traitement.

Quand la désignation d'un DPO est-elle obligatoire ? :: Pour les autorités publiques, les organisations dont l'activité principale implique un suivi régulier et à grande échelle des personnes, ou le traitement à grande échelle de données sensibles (catégories particulières).

Qu'impose l'article 28 du RGPD sur les sous-traitants ? :: Tout traitement par un sous-traitant doit être encadré par un contrat (DPA) imposant : agir uniquement sur instruction, garantir la confidentialité, mettre en place des mesures de sécurité, aider pour les droits des personnes et les DPIA, restituer ou supprimer les données en fin de contrat.

Quel est le délai pour notifier une violation de données à l'autorité de contrôle ? :: 72 heures à compter de la prise de connaissance de la violation (article 33 RGPD), sauf si la violation ne présente pas de risque pour les droits et libertés des personnes.

Quelles sont les conditions pour transférer des données hors UE ? :: Décision d'adéquation, clauses contractuelles types (CCT) avec TIA, règles d'entreprise contraignantes (BCR), ou dérogations spécifiques (consentement explicite, nécessité contractuelle…).

Quelle est la sanction maximale prévue par le RGPD ? :: 20 millions d'euros ou 4 % du chiffre d'affaires mondial annuel, le montant le plus élevé étant retenu. Pour les infractions moins graves : 10 M€ ou 2 % du CA mondial.

Qu'est-ce que le principe d'accountability dans le RGPD ? :: L'obligation pour le responsable de traitement de ne pas seulement respecter le RGPD, mais d'être en mesure de démontrer ce respect à tout moment (documentation, registre, DPO, politiques internes, audits).

## Sources

- Règlement (UE) 2016/679 — RGPD : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679
- CNIL — guides et fiches pratiques : https://www.cnil.fr/
- CEPD — lignes directrices : https://edpb.europa.eu/
- CEPD, "Bilan des sanctions RGPD 2023"
- DPC, décision contre Meta (transferts USA), mai 2023 : https://www.dataprotection.ie/
- CMS RGPD Enforcement Tracker : https://www.enforcementtracker.com/

## Notions liées

- [[Privacy by Design]]
- [[Profilage et surveillance]]
- [[CLOUD Act et transferts de données]]
- [[Réglementations internationales sur les données]]
- [[DSA - DMA]]
- [[Normes ISO liées aux données]]
- [[Data Lifecycle Management]]
- [[NIS2]]
- [[Souveraineté numérique]]
