---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# EBIOS RM et gestion des risques cyber

![[N — EBIOS RM et gestion des risques cyber.mp3]]
## En bref
> **Définition** : EBIOS Risk Manager (EBIOS RM) est la méthode française d'analyse et de traitement des risques de sécurité des systèmes d'information, publiée par l'ANSSI en 2018. Elle permet d'identifier les risques numériques pesant sur une organisation, d'évaluer leur criticité et de définir les mesures de traitement adaptées. Elle s'inscrit dans un ensemble de cadres de gestion des risques cyber incluant ISO 27005, NIST RMF et FAIR.
> **Pourquoi c'est important** : La gestion des risques cyber est la colonne vertébrale de toute stratégie de sécurité. Sans analyse de risques structurée, les investissements sécurité sont dispersés et non prioritarisés. EBIOS RM est la référence recommandée par l'ANSSI pour les OIV, les OES et les entités soumises à NIS2. Elle permet au RSSI de justifier ses choix au COMEX avec une approche rationnelle.
> **Chiffres clés** :
> - Les organisations sans programme formel de gestion des risques dépensent 2,7x plus en réponse aux incidents qu'en prévention (Ponemon, 2022).
> - EBIOS RM est utilisée par plus de 80 % des OIV français dans leurs analyses de risques (ANSSI, 2023).
> - 68 % des entreprises françaises de plus de 500 salariés ont réalisé une analyse de risques formelle en 2023 (CESIN Baromètre 2024).

## Approfondir

### Fonctionnement

**EBIOS RM — Les 5 ateliers**

EBIOS RM (Risk Manager) est structurée en 5 ateliers successifs, chacun produisant des livrables servant aux ateliers suivants :

**Atelier 1 — Cadrage et socle de sécurité**
- Définition du périmètre de l'étude (organisation, SI, missions).
- Identification des valeurs métier (processus et informations critiques pour l'organisation).
- Inventaire et évaluation des biens supports (SI, serveurs, réseaux, prestataires).
- Identification des mesures de sécurité existantes et du socle de sécurité (référentiels applicables : ISO 27001, NIS2, LPM, RGPD).
- Livrable : cartographie des valeurs métier et des biens supports.

**Atelier 2 — Sources de risques**
- Identification des sources de risques pertinentes (cybercriminels, États, concurrents, insiders, hacktivistes).
- Définition des objectifs visés (accès aux données clients, sabotage de la production, rançon, espionnage).
- Sélection des couples Source de Risque / Objectif Visé (SR/OV) les plus vraisemblables et pertinents pour l'organisation.
- Livrable : cartographie des SR/OV retenus pour la suite de l'analyse.

**Atelier 3 — Scénarios stratégiques**
- Pour chaque SR/OV, construction de scénarios stratégiques : chemins d'attaque à haut niveau (ex : compromission d'un fournisseur de confiance, attaque de la chaîne d'approvisionnement).
- Évaluation de la vraisemblance et de la gravité de chaque scénario.
- Identification des parties prenantes à risque (prestataires, partenaires, fournisseurs de cloud).
- Livrable : cartographie des scénarios stratégiques avec niveaux de risque.

**Atelier 4 — Scénarios opérationnels**
- Déclinaison des scénarios stratégiques en scénarios opérationnels détaillés : séquences d'actions techniques (modes opératoires), mappés sur MITRE ATT&CK.
- Évaluation de la vraisemblance technique de chaque scénario.
- Identification des chemins d'attaque les plus probables.
- Livrable : cartographie des scénarios opérationnels avec probabilités techniques.

**Atelier 5 — Traitement du risque**
- Pour chaque risque, définition de la stratégie de traitement : Acceptation, Réduction, Transfert (assurance cyber), Refus (ne pas déployer la solution trop risquée).
- Définition du plan de traitement des risques (PTR) : mesures de sécurité à mettre en place, responsables, délais, budget.
- Définition du risque résiduel accepté par le top management.
- Livrable : Plan de Traitement des Risques + tableau de risques résiduels.

**La notion de risque en cybersécurité**

Un risque = Menace × Vulnérabilité × Impact.

- **Menace** : action potentielle d'un acteur malveillant ou d'un événement accidentel.
- **Vulnérabilité** : faiblesse exploitable dans le SI ou l'organisation.
- **Impact** : conséquences sur les objectifs de l'organisation (financier, réputationnel, opérationnel, réglementaire).
- **Vraisemblance** : probabilité que le scénario se réalise.

Les critères DICT (Disponibilité, Intégrité, Confidentialité, Traçabilité) sont utilisés pour évaluer les besoins de sécurité de chaque valeur métier.

**ISO 27005**

Norme internationale de gestion des risques de sécurité de l'information. Elle décrit un processus cyclique : Contexte → Appréciation du risque (identification, estimation, évaluation) → Traitement → Acceptation → Communication → Surveillance. ISO 27005 est compatible avec EBIOS RM et s'inscrit dans le cadre du SMSI ISO 27001. Plus générique qu'EBIOS RM, elle ne prescrit pas de méthode spécifique.

**NIST Risk Management Framework (RMF)**

Cadre américain de gestion des risques, obligatoire pour les agences fédérales américaines (FISMA). En 7 étapes : Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor. Très utilisé par les organisations ayant des activités aux États-Unis ou travaillant avec le DoD. Compatible avec le NIST CSF (Cybersecurity Framework).

**FAIR (Factor Analysis of Information Risk)**

Modèle quantitatif de gestion des risques cyber, basé sur des probabilités et des montants financiers (USD/EUR) plutôt que sur des échelles qualitatives (faible/moyen/élevé). Permet de calculer une perte annuelle prévue (Annual Loss Expectancy) et de comparer le coût des mesures de sécurité au risque financier évité. Permet un dialogue RSSI-CFO en termes financiers. Complémentaire à EBIOS RM pour la valorisation financière des risques.

**Le Plan de Traitement des Risques (PTR)**

Le PTR est l'output concret de l'analyse de risques : liste des mesures de sécurité à mettre en place, priorisées par niveau de risque résiduel. Il inclut : la mesure, le responsable, le délai, le coût estimé, le risque couvert, et le risque résiduel attendu après mise en oeuvre. Il est validé par le management et révisé annuellement.

**Risk Acceptance et appétence au risque**

Toute organisation doit définir son appétence au risque (risk appetite) : le niveau de risque qu'elle est prête à accepter. Certains risques résiduels sont acceptés par le management (ex : risque d'une interruption de service < 4h une fois par an est jugé acceptable). Cette acceptation formelle est documentée et validée par le COMEX ou le CA.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Approche structurée, répétable et documentée | Processus long (atelier 1 à 5 : 3 à 6 mois pour une analyse complète) |
| Alignement avec les exigences réglementaires françaises (ANSSI, NIS2) | Nécessite des experts méthodologiques qualifiés |
| Prise en compte des menaces réelles via CTI (Atelier 2) | Risque de résultats trop théoriques si les ateliers ne sont pas bien animés |
| Implication du management dans l'acceptation des risques résiduels | L'approche qualitative ne permet pas de comparaison financière directe (FAIR est meilleur pour ça) |
| Compatible ISO 27001/27005 | Nécessite des ateliers avec des acteurs métier souvent peu disponibles |
| Carte des risques utilisable pour le reporting COMEX | La mise à jour annuelle est souvent négligée faute de ressources |

### Acteurs et solutions du marché

**Outils EBIOS RM**
- **EBIOS RM Tool** (ANSSI) : outil gratuit officiel de l'ANSSI pour mener les 5 ateliers.
- **Optimyss** : outil commercial français dédié à EBIOS RM, plus ergonomique.
- **SECTEUR 47** : outil de gestion des risques compatible EBIOS RM et ISO 27005.
- **Piloter.io** : plateforme GRC française incluant EBIOS RM.

**Outils GRC (Governance, Risk & Compliance)**
- **ServiceNow GRC** : plateforme enterprise de gestion des risques et de la conformité.
- **OneTrust** : très fort sur la conformité RGPD et la gestion des risques tiers.
- **Archer** (RSA) : référence en GRC enterprise.
- **MyComplianceOffice**, **MetricStream** : acteurs GRC internationaux.

**Cabinets de conseil**
- **Wavestone**, **Sia Partners**, **Deloitte Cyber**, **KPMG Cyber** : accompagnement EBIOS RM et ISO 27001.
- **AMOSSYS**, **Synetis** : spécialistes cybersécurité français.

### Cas d'usage concrets

**1. Analyse EBIOS RM pour un OIV du secteur énergie (NIS2/LPM)**
Un opérateur d'infrastructure critique (réseau de distribution d'électricité) réalise une analyse EBIOS RM annuelle imposée par l'ANSSI dans le cadre de la LPM. Les 5 ateliers sont menés en 4 mois avec les équipes opérationnelles, la DSI et les partenaires métier. L'atelier 2 identifie 3 SR/OV prioritaires dont un groupe APT étatique ciblant les SCADA. Le Plan de Traitement des Risques priorise la segmentation OT/IT et le déploiement d'une solution de détection industrielle (Claroty). Le risque résiduel est validé par le COMEX.

**2. Analyse de risques tiers EBIOS RM (secteur bancaire)**
Une banque intègre l'analyse de risques de ses prestataires cloud critiques (hébergement AWS, paiement Stripe) dans son analyse EBIOS RM (Atelier 3 — parties prenantes). Pour chaque prestataire, elle évalue la vraisemblance d'une compromission de la chaîne d'approvisionnement et ses impacts sur les processus métier critiques. Les prestataires jugés à risque élevé sont soumis à des audits de sécurité annuels et à des clauses contractuelles DORA-compliant.

**3. Analyse quantitative FAIR pour justifier un investissement SOC**
Une DSI industrielle souhaite investir 2 M€ dans un SOC managé (MDR). Elle utilise FAIR pour quantifier le risque actuel : probabilité de 40 % d'un incident ransomware en 12 mois, impact moyen de 8 M€. Valeur à risque annuelle : 3,2 M€. L'investissement de 2 M€ sur 3 ans réduit la probabilité à 10 % (nouvelle valeur à risque : 800 k€). ROI = (3 200 k€ - 800 k€) × 3 - 2 000 k€ = 5,2 M€ sur 3 ans. Cet argumentaire FAIR convainc le CFO d'approuver le budget.

### Chiffres et tendances
- EBIOS RM est recommandée par l'ANSSI pour toutes les entités soumises à NIS2 et LPM (environ 15 000 entités en France après NIS2).
- ISO 27001 (dernière version 2022) exige une analyse de risques formelle comme condition de certification — EBIOS RM est l'une des méthodes les plus utilisées pour y répondre.
- DORA (Digital Operational Resilience Act, applicable en 2025) impose des analyses de risques ICT trimestrielles pour les entités financières systémiques.
- La gestion des risques liés aux tiers (TPRM — Third Party Risk Management) est en forte croissance : 60 % des incidents impliquent un prestataire ou la chaîne d'approvisionnement (CrowdStrike, 2024).
- La quantification financière du risque cyber (FAIR, CVSS financier) progresse : 35 % des RSSI l'utilisent désormais pour dialoguer avec leur CFO (Gartner, 2024).

## Flashcards
#flashcards/Cybersécurité/EBIOS_RM_et_gestion_des_risques_cyber

Quels sont les 5 ateliers d'EBIOS RM ? :: 1. Cadrage et socle de sécurité (périmètre, valeurs métier, biens supports) → 2. Sources de risques (couples SR/OV) → 3. Scénarios stratégiques (chemins d'attaque à haut niveau, parties prenantes) → 4. Scénarios opérationnels (détails techniques, MITRE ATT&CK) → 5. Traitement du risque (PTR, risque résiduel).

Quelle est la différence entre EBIOS RM et ISO 27005 ? :: EBIOS RM est une méthode française prescriptive (5 ateliers structurés, livrables définis, orientée CTI et scénarios). ISO 27005 est une norme internationale générique décrivant un processus de gestion des risques sans prescrire de méthode. ISO 27005 est le "quoi", EBIOS RM est le "comment" à la française.

Qu'est-ce que FAIR et en quoi complète-t-il EBIOS RM ? :: Factor Analysis of Information Risk : modèle de quantification financière des risques cyber (Annual Loss Expectancy en €/$). EBIOS RM donne une évaluation qualitative (faible/moyen/élevé). FAIR permet de calculer un risque en euros, de comparer le coût d'une mesure à la réduction de risque financière, et de dialoguer avec le CFO. Les deux sont complémentaires.

Qu'est-ce qu'un Plan de Traitement des Risques (PTR) ? :: Livrable de l'Atelier 5 d'EBIOS RM : liste des mesures de sécurité à mettre en place, priorisées par niveau de risque. Inclut pour chaque mesure : le responsable, le délai, le coût estimé, le risque couvert et le risque résiduel attendu. Validé par le management, révisé annuellement.

Quelles sont les 4 stratégies de traitement d'un risque ? :: 1. Réduction (mettre en place des mesures de sécurité pour diminuer la probabilité ou l'impact) → 2. Transfert (assurance cyber, clause contractuelle) → 3. Acceptation (risque jugé tolérable par le management) → 4. Refus/Évitement (ne pas lancer le projet ou le service trop risqué).

Qu'est-ce que le NIST RMF et dans quel contexte est-il utilisé ? :: Risk Management Framework du NIST américain, obligatoire pour les agences fédérales US (FISMA). 7 étapes : Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor. Utilisé par les organisations travaillant avec le gouvernement américain ou le DoD. Compatible avec le NIST CSF.

Qu'est-ce que l'appétence au risque (risk appetite) et qui la définit ? :: Le niveau de risque résiduel qu'une organisation est prête à accepter. Elle est définie par le top management (COMEX, CA) et documentée formellement. Ex : "Nous acceptons un risque d'interruption de service < 4h une fois par an mais n'acceptons aucun risque de divulgation de données de paiement." Elle guide les décisions de traitement en Atelier 5.

## Sources
- ANSSI — Guide EBIOS Risk Manager (https://www.ssi.gouv.fr/guide/la-methode-ebios-risk-manager)
- ANSSI — Club EBIOS (https://www.club-ebios.org)
- ISO/IEC 27005:2022 — Information security risk management
- NIST Risk Management Framework — https://csrc.nist.gov/projects/risk-management
- FAIR Institute — https://www.fairinstitute.org
- CESIN — Baromètre de la cybersécurité 2024
- Ponemon Institute — The Economics of Cybersecurity 2022
- CrowdStrike — Global Threat Report 2024 (supply chain attacks)
- Gartner — Risk Quantification Trends 2024

## Notions liées
- [[SOC]]
- [[Threat Intelligence et Threat Hunting]]
- [[Métriques de sécurité]]
- [[Sensibilisation et facteur humain]]
- [[Red Team - Blue Team - Purple Team]]
- [[Forensics]]
