---
type: notion
thèmes:
  - Cybersécurité
  - IA
statut: pas vu
dernière_révision: 
---

# Ingénierie sociale

![[N — Ingénierie sociale.mp3]]
## En bref
> **Définition** : L'ingénierie sociale (social engineering) est l'ensemble des techniques de manipulation psychologique visant à amener une personne à divulguer des informations confidentielles ou à effectuer des actions compromettant la sécurité, sans recourir à des exploits techniques. Elle exploite les biais cognitifs humains (autorité, urgence, réciprocité, confiance).
> **Pourquoi c'est important** : Le maillon humain est systématiquement identifié comme le premier vecteur d'attaque. Aucun dispositif technique ne protège contre un employé manipulé. La DSI doit donc intégrer la dimension humaine (sensibilisation, formation, procédures) dans sa stratégie de défense.
> **Chiffres clés** :
> - 68 % des violations de données impliquent un facteur humain (Verizon DBIR 2024).
> - Les attaques de phishing ont augmenté de 58 % en 2023, amplifiées par les outils d'IA générative (Zscaler ThreatLabz 2024).
> - Les pertes liées au BEC dépassent 2,9 Md$ en 2023 aux États-Unis (FBI IC3 2023).

## Approfondir

### Fonctionnement

**Social engineering — principes psychologiques** : Robert Cialdini identifie 6 leviers d'influence exploités par les attaquants :
1. Autorité : usurper l'identité d'un dirigeant, d'un technicien IT, d'un auditeur.
2. Urgence : "Le virement doit être fait avant 17h ou nous perdons le contrat."
3. Réciprocité : offrir quelque chose (service, information) pour créer une obligation.
4. Similarité/sympathie : se faire passer pour un collègue, un ami commun.
5. Preuve sociale : "Tous vos collègues ont déjà validé."
6. Rareté : "Vous êtes le seul à pouvoir autoriser cette opération."

**Deepfake vocal et vidéo** : génération de contenu audio ou vidéo synthétique imitant une personne réelle (voix, visage, comportements) grâce aux réseaux de neurones (GAN, diffusion). Utilisé pour :
- Usurper un dirigeant lors d'un appel vidéo (vishing deepfake).
- Générer des messages vocaux frauduleux (instructions de virement, divulgation de mots de passe).
Cas réel : en 2024, un employé de la finance d'Arup (HK) a viré 25 M$ après une visioconférence deepfake avec de faux collègues.

**BEC (Business Email Compromise)** : compromission ou usurpation de boîte email professionnelle pour ordonner des actions frauduleuses (virements, modification de RIB fournisseurs, transmission de données RH). Vecteurs : phishing ciblé, credential stuffing, compromission de serveur mail.

**Phishing hyper-personnalisé par LLM** : les modèles de langage (GPT-4, etc.) permettent de générer des emails de spear phishing parfaitement rédigés, sans faute d'orthographe, adaptés au contexte professionnel de la cible (LinkedIn scraping, posts publics). Le coût de production d'une attaque ciblée de qualité s'effondre.

**Insider threat** : menace interne, intentionnelle (employé malveillant, mécontent, corrompu) ou non intentionnelle (erreur, négligence). L'insider légitime dispose déjà d'accès, ce qui rend la détection difficile. À distinguer de l'attaquant externe qui a compromis un compte interne.

### Avantages / Inconvénients
| Pour l'attaquant — Forces | Pour le défenseur — Réponses |
|-----------|---------------|
| Contourne les contrôles techniques | Sensibilisation et formation régulières |
| Faible coût, fort rendement (BEC) | Procédures de vérification hors-bande (rappel téléphonique) |
| Difficile à détecter a posteriori | Simulation de phishing (mesure du taux de clic) |
| Amplifié par l'IA (deepfake, LLM) | Détection comportementale (UEBA) |
| Exploite des biais universels | Culture de sécurité (human firewall) |

### Acteurs et solutions du marché

**Plateformes de sensibilisation et simulation** : KnowBe4, Proofpoint Security Awareness, Terranova Security (Française), Mailinblack Protect (France).

**Solutions anti-BEC / anti-phishing** : Microsoft Defender for Office 365, Proofpoint Targeted Attack Protection, Vade Secure (France), Mimecast.

**Détection des deepfakes** : Microsoft Azure AI Content Safety, Sentinel AI, Pindrop (authentification vocale).

**UEBA (User and Entity Behavior Analytics)** : Splunk UBA, Microsoft Sentinel, Varonis — détection des comportements anormaux des insiders.

### Cas d'usage concrets

1. **Fraude au président — Michelin (2021)** : des escrocs ont usurpé l'identité du PDG par email et appel téléphonique. La contrôleuse de gestion a initié un virement de 1,5 M€ avant que la fraude soit détectée.

2. **Twitch (2022) / Uber (2022)** : dans les deux cas, des attaquants du groupe LAPSUS$ ont manipulé des employés via l'ingénierie sociale (vishing, fatigue MFA) pour obtenir des accès VPN/AD et exfiltrer des données massives.

3. **Deepfake vocal — PDG britannique (2019)** : première fraude deepfake vocale documentée. Le directeur financier a viré 220 000 € en croyant obéir à son PDG, dont la voix avait été clonée.

### Chiffres et tendances
- 91 % des cyberattaques débutent par un email de phishing (PhishMe/Cofense).
- Les emails de phishing générés par IA ont un taux d'ouverture 2x supérieur aux emails non ciblés (IBM X-Force 2023).
- Le marché des outils deepfake criminels est évalué à plusieurs centaines de millions de dollars (Europol 2022).
- Coût moyen d'une fraude BEC pour une entreprise : 125 000 $ (Verizon DBIR 2024).

## Flashcards
#flashcards/Cybersécurité/Ingénierie_sociale #flashcards/IA/Ingénierie_sociale
Qu'est-ce que l'ingénierie sociale ? :: Ensemble de techniques de manipulation psychologique visant à amener une personne à divulguer des informations ou réaliser des actions compromettant la sécurité, sans exploit technique.

Quels sont les 3 principaux leviers psychologiques exploités ? :: Autorité (usurpation d'identité), urgence (pression temporelle), et confiance/similarité (faux collègue, faux contexte partagé).

Qu'est-ce qu'un deepfake vocal dans un contexte cyber ? :: Génération d'audio synthétique imitant la voix d'une personne réelle (dirigeant, collègue) grâce à l'IA, utilisé pour ordonner des virements ou divulguer des informations sensibles.

Comment le BEC se distingue-t-il d'un phishing classique ? :: Le BEC cible précisément des processus financiers ou RH internes via compromission ou usurpation d'email professionnel. Il est beaucoup plus personnalisé et les montants en jeu sont élevés.

Qu'est-ce qu'un insider threat ? :: Menace provenant de l'intérieur de l'organisation : employé malveillant, mécontent ou négligent ayant des accès légitimes au SI.

Quel est l'impact des LLM sur le phishing ? :: Les LLM permettent de générer des emails de phishing parfaitement rédigés, personnalisés et sans faute, à très faible coût, rendant les attaques ciblées accessibles à des acteurs moins sophistiqués.

Comment réduire le risque d'ingénierie sociale en entreprise ? :: Sensibilisation régulière, simulations de phishing, procédures de vérification hors-bande pour les demandes sensibles (virement, changement de RIB), et culture de sécurité (human firewall).

## Sources
- Verizon Data Breach Investigations Report (DBIR) 2024
- FBI IC3 — Internet Crime Report 2023 — www.ic3.gov
- Zscaler ThreatLabz Phishing Report 2024
- IBM X-Force Threat Intelligence Index 2023
- ANSSI — Guide de sensibilisation à la sécurité — www.ssi.gouv.fr
- Europol — Deepfakes and Synthetic Media report 2022
- Robert Cialdini — "Influence : The Psychology of Persuasion" (référence académique)

## Notions liées
- [[Menaces cyber]]
- [[Défense en profondeur]]
- [[Zero Trust]]
- [[SIEM]]
- [[SOAR]]
