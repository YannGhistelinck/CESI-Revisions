---
type: notion
thèmes:
  - Cybersécurité
  - Mobilité
statut: pas vu
dernière_révision: 
---

# Sensibilisation et facteur humain

## En bref
> **Définition** : La sensibilisation à la sécurité (Security Awareness) désigne l'ensemble des programmes, formations et pratiques visant à modifier les comportements humains pour réduire le risque cyber lié au facteur humain. Elle englobe la formation, la communication, les simulations d'attaques et la création d'une culture de sécurité durable au sein de l'organisation.
> **Pourquoi c'est important** : Le facteur humain est impliqué dans 74 % des incidents de sécurité (Verizon DBIR 2024). Aucun investissement technologique ne peut compenser des comportements à risque : cliquer sur un phishing, réutiliser des mots de passe, utiliser des applications non autorisées (shadow IT). Le RSSI doit donc former et engager les collaborateurs autant qu'il protège les systèmes.
> **Chiffres clés** :
> - 74 % des violations de données impliquent le facteur humain (Verizon DBIR 2024).
> - Le ROI moyen d'un programme de sensibilisation mature est de 37:1 (pour 1 € investi, 37 € de pertes évitées — Ponemon Institute, 2022).
> - Les organisations avec un programme de sensibilisation mature réduisent le taux de clics phishing de 32 % à 5 % en 12 mois (KnowBe4, 2023).

## Approfondir

### Fonctionnement

**Security Awareness Program (SAP)**

Un programme de sensibilisation efficace ne se limite pas à une formation annuelle obligatoire. Il suit le modèle SANS Security Awareness Maturity Model en 5 niveaux :
1. **Niveau 1 (Compliance-focused)** : formation annuelle pour cocher la case réglementaire — inefficace.
2. **Niveau 2 (Promoting awareness and behavior change)** : contenu varié, fréquence accrue, mesures d'impact.
3. **Niveau 3 (Long-term sustainment)** : programme continu, culture de sécurité intégrée.
4. **Niveau 4 (Metrics framework)** : métriques précises (CTR, report rate) guidant les décisions.
5. **Niveau 5 (Robust framework)** : programme intégré à la culture d'entreprise, executives engagés.

Les composantes d'un SAP mature :
- **Formations** : e-learning modulaires, courtes (3-5 min), accessibles en mobilité.
- **Simulations de phishing** : campagnes régulières (mensuelle ou trimestrielle) avec formation immédiate post-clic.
- **Communications** : newsletters sécurité, affiches, screensavers, messages lors du verrouillage d'écran.
- **Événements** : Mois européen de la cybersécurité (octobre), cybersecurity day interne.
- **Métriques** : CTR, report rate, scores de quiz, évolution dans le temps.

**Micro-learning**

Approche pédagogique consistant à délivrer des contenus de formation courts (1-5 minutes), ciblés sur un seul comportement ou risque, à intervalles réguliers. Basée sur la courbe de l'oubli d'Ebbinghaus : sans répétition espacée, 80 % des informations sont oubliées en 30 jours. Le micro-learning maintient la rétention par des rappels réguliers et contextuels.
- Exemples : notification push après une tentative de phishing détectée, micro-module sur la gestion des mots de passe après une alerte de violation.
- Plateformes : KnowBe4, Proofpoint PSAT, Cofense, Terranova.

**Gamification**

Intégration de mécaniques de jeu dans la formation :
- **Points et classements** : leaderboards entre équipes ou départements.
- **Badges et certifications** : reconnaissance des comportements sécurisés.
- **CTF (Capture The Flag) internes** : défis techniques pour les équipes IT.
- **Simulations gamifiées** : jeux de rôle autour de scénarios d'incident.
- Impact : augmentation de l'engagement de 60 % et de la rétention de 40 % vs formations classiques (Gartner, 2023).

**Security Champion**

Un Security Champion est un référent sécurité bénévole au sein d'une équipe métier ou de développement, qui n'est pas un spécialiste de sécurité mais qui joue le rôle d'ambassadeur :
- Relai entre la DSI/RSSI et les équipes opérationnelles.
- Premier point de contact pour les questions de sécurité au quotidien.
- Participe aux revues de code (sécurité applicative) ou aux analyses de risques projet.
- Formation spécifique (OWASP, bonnes pratiques) et communauté interne.
- Ce modèle est particulièrement efficace dans les organisations DevSecOps.

**Nudge (architecture de choix)**

Inspiré des sciences comportementales (Thaler & Sunstein), le nudge en cybersécurité consiste à modifier l'environnement de choix pour orienter naturellement vers le comportement sécurisé, sans interdire ni obliger :
- Activation du MFA par défaut (plutôt que de le laisser optionnel).
- Pré-remplissage des paramètres de sécurité stricts dans les applications.
- Notification contextuelle au moment de télécharger un document sensible ("Ce fichier contient des données confidentielles — êtes-vous sûr de vouloir l'envoyer en externe ?").
- Friction ajoutée pour les actions risquées (virement urgent > 10 000 € : double confirmation et délai de 24h).

**Insider Threat**

L'insider threat désigne les risques posés par des personnes ayant un accès légitime au SI :
- **Malveillant** : employé ou prestataire exfiltrant des données intentionnellement (espionnage industriel, vengeance, profit).
- **Négligent** : employé causant un incident par inattention (mauvaise configuration, clic sur phishing, perte d'un appareil).
- **Compromis** : compte légitime pris en main par un attaquant externe.

Mesures de détection : UEBA (comportements anormaux), DLP (Data Loss Prevention), journalisation des accès aux données sensibles, politiques de moindre privilège. La prévention passe aussi par la culture d'entreprise, le management et les RH (détection des signaux faibles : démotivation, conflit, départ imminent).

**Shadow IT**

Applications et services utilisés par les employés sans autorisation de la DSI (Dropbox personnel, WhatsApp pour des échanges professionnels, outils IA en ligne traitant des données sensibles). Le Shadow IT expose l'organisation à des fuites de données, des vulnérabilités non patchées et des non-conformités RGPD.
- 80 % des employés utilisent au moins un outil non autorisé (Gartner, 2023).
- Solutions : CASB (Cloud Access Security Broker) pour détecter le Shadow IT, politique BYOD claire, offre d'alternatives approuvées attractives.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction directe du taux de clic phishing (KPI mesurable) | ROI difficile à démontrer à court terme |
| Création d'une culture de sécurité durable | Résistance au changement dans certaines cultures d'entreprise |
| Transformation des employés en capteurs humains (report rate) | Formations perçues comme contraignantes si mal conçues |
| Réduction du Shadow IT par l'éducation et les alternatives | Micro-learning nécessite une infrastructure de delivery (plateformes) |
| Conformité NIS2, RGPD, ISO 27001 (exigences de sensibilisation) | La gamification peut trivialiser des sujets sérieux |
| Complémentaire aux contrôles techniques (couche humaine) | Les Security Champions nécessitent du temps et des ressources formation |

### Acteurs et solutions du marché

**Plateformes de sensibilisation**
- **KnowBe4** : leader mondial — phishing simulé + formations + métriques. Très répandu.
- **Proofpoint Security Awareness Training** : intégration forte avec la sécurité email.
- **Cofense** : spécialiste phishing simulé + incident response (bouton de signalement Outlook).
- **Terranova Security** (Fortra) : acteur fort en Europe, contenus en français.
- **Hoxhunt** : gamification avancée, contenu adaptatif.

**DLP (Data Loss Prevention)**
- **Microsoft Purview** (ex-Azure Information Protection) : classification et protection des données.
- **Symantec DLP**, **Forcepoint DLP** : solutions enterprise.

**CASB (Cloud Access Security Broker)**
- **Microsoft Defender for Cloud Apps** : intégré à l'écosystème Microsoft.
- **Netskope**, **Zscaler** : leaders du marché CASB.

**Détection insider threat**
- **Microsoft Insider Risk Management** (Purview) : corrélation comportementale.
- **Varonis** : analyse des accès aux données et comportements anormaux.
- **Exabeam**, **Securonix** : UEBA pour la détection des menaces internes.

### Cas d'usage concrets

**1. Programme de sensibilisation après un incident phishing (secteur assurance)**
Une compagnie d'assurance subit un incident après qu'un commercial clique sur un phishing imitant son outil CRM. La DSI déploie KnowBe4 : campagnes mensuelles de phishing simulé ciblant les comportements les plus à risque, micro-modules de 3 min déclenchés immédiatement après un clic simulé, dashboard de suivi par département. En 12 mois : CTR passe de 28 % à 6 %, report rate de 3 % à 22 %. Le programme est étendu aux prestataires.

**2. Programme Security Champion dans une DSI bancaire (DevSecOps)**
Une banque identifie 25 développeurs volontaires comme Security Champions. Chaque champion reçoit 2 jours de formation OWASP Top 10 et participe à des sessions mensuelles avec le RSSI. Ils intègrent des contrôles de sécurité dans les user stories (ASVS) et font des code reviews orientées sécurité. Résultat : réduction de 40 % des vulnérabilités en production en 18 mois.

**3. Détection d'un insider threat via UEBA (secteur pharmaceutique)**
Un chercheur en R&D, apprenant son licenciement imminent, commence à télécharger massivement des données de recherche confidentielles vers son Dropbox personnel. Le CASB (Microsoft Defender for Cloud Apps) détecte l'usage de Dropbox (Shadow IT) et le volume anormal de transferts. L'alerte UEBA est croisée avec le contexte RH (notification de licenciement). Les accès sont révoqués avant l'exfiltration complète des données.

### Chiffres et tendances
- 74 % des violations de données impliquent le facteur humain (Verizon DBIR 2024).
- 85 % des incidents de phishing réussis visaient des utilisateurs n'ayant pas reçu de formation dans les 6 mois précédents (Proofpoint, 2023).
- 80 % des organisations constatent une réduction significative des incidents après 12 mois de programme de sensibilisation (SANS Institute, 2023).
- Le marché mondial de la sensibilisation à la sécurité atteindra 10 milliards de dollars en 2027 (KnowBe4, MarketsandMarkets).
- NIS2 et ISO 27001 exigent explicitement des programmes de sensibilisation pour toutes les entités concernées.
- Les attaques d'ingénierie sociale ciblant spécifiquement les dirigeants (whaling, BEC) ont augmenté de 65 % en 2023 (FBI IC3).

## Flashcards
#flashcards/Cybersécurité/Sensibilisation_et_facteur_humain #flashcards/Mobilité/Sensibilisation_et_facteur_humain

Qu'est-ce qu'un Security Champion et quel est son rôle ? :: Référent sécurité bénévole au sein d'une équipe métier ou de développement. Il n'est pas un expert sécurité mais joue le rôle d'ambassadeur : relai entre DSI/RSSI et équipes, premier contact pour les questions sécurité, participation aux revues de code. Particulièrement efficace en DevSecOps.

Qu'est-ce que le micro-learning en cybersécurité et pourquoi est-il efficace ? :: Approche pédagogique basée sur des contenus courts (1-5 min), ciblés et répétés à intervalles réguliers. Efficace car basé sur la courbe de l'oubli d'Ebbinghaus : sans répétition, 80 % des infos sont oubliées en 30 jours. Le micro-learning maintient la rétention par des rappels contextuels et réguliers.

Qu'est-ce que le nudge en cybersécurité ? :: Application des sciences comportementales pour orienter naturellement vers le comportement sécurisé sans contraindre. Ex : MFA activé par défaut, notification contextuelle avant d'envoyer un fichier sensible en externe, friction ajoutée pour les virements urgents. Influence le comportement sans interdire.

Quelle est la différence entre un insider threat malveillant, négligent et compromis ? :: Malveillant : exfiltre intentionnellement des données (espionnage, profit, vengeance). Négligent : cause un incident par inattention (clic phishing, perte d'appareil, mauvaise config). Compromis : compte légitime utilisé par un attaquant externe. Chaque type nécessite des contrôles différents.

Qu'est-ce que le Shadow IT et comment le gérer ? :: Applications utilisées sans autorisation DSI (Dropbox perso, WhatsApp professionnel, outils IA en ligne). Risques : fuite de données, vulnérabilités, non-conformité RGPD. Solutions : CASB pour détecter et contrôler, politique BYOD claire, offre d'alternatives approuvées attractives (ex : SharePoint vs Dropbox).

Quels sont les 5 niveaux du SANS Security Awareness Maturity Model ? :: 1. Compliance-focused (formation annuelle "pour cocher la case") → 2. Behavior change (contenu varié, mesures) → 3. Long-term sustainment (culture intégrée) → 4. Metrics framework (métriques guidant les décisions) → 5. Robust framework (culture d'entreprise, executives engagés).

Quel est le ROI d'un programme de sensibilisation mature et comment le mesurer ? :: ROI moyen de 37:1 (Ponemon, 2022). Se mesure via : réduction du CTR phishing, augmentation du report rate, réduction du nombre d'incidents liés au facteur humain, coût des incidents évités. Difficile à mesurer à court terme mais démontrable sur 12-24 mois avec des métriques.

## Sources
- Verizon Data Breach Investigations Report (DBIR) 2024
- KnowBe4 — Annual Phishing by Industry Benchmarking Report 2023
- SANS Institute — Security Awareness Maturity Model (https://www.sans.org/security-awareness-training)
- Ponemon Institute — The Value of Security Awareness Training 2022
- Proofpoint — State of the Phish 2023
- Gartner — Market Guide for Security Awareness Computer-Based Training 2023
- FBI IC3 — Internet Crime Report 2023
- ANSSI — Guide de sensibilisation des employés (https://www.ssi.gouv.fr)

## Notions liées
- [[SOC]]
- [[Métriques de sécurité]]
- [[IA en cybersécurité]]
- [[EBIOS RM et gestion des risques cyber]]
- [[Threat Intelligence et Threat Hunting]]
