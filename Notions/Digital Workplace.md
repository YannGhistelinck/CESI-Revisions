---
type: notion
thèmes:
  - Mobilité
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Digital Workplace

![[N — Digital Workplace.mp3]]
## En bref
> **Définition** : La Digital Workplace (ou espace de travail numérique) désigne l'ensemble des outils, plateformes et services numériques mis à disposition des collaborateurs pour travailler, collaborer et communiquer, quel que soit leur lieu ou leur terminal. Elle vise à reproduire et enrichir numériquement l'environnement de travail physique du bureau, en intégrant communication unifiée, collaboration, accès aux applications et gestion de l'expérience employé.
> **Pourquoi c'est important** : La Digital Workplace est devenue un enjeu stratégique pour la DSI depuis la généralisation du télétravail. Elle conditionne directement la productivité, l'attractivité et la rétention des talents. Un mauvais environnement numérique dégrade l'expérience employé (DEX) et génère du shadow IT. La DSI est désormais productrice d'une expérience, pas seulement d'une infrastructure.
> **Chiffres clés** :
> - Le marché mondial de la Digital Workplace était estimé à **35 milliards USD en 2023**, avec une croissance annuelle de 21 % (Grand View Research, 2024)
> - **85 % des employés** se disent plus productifs avec les bons outils numériques (Microsoft Work Trend Index, 2023)
> - Les entreprises avec une Digital Workplace mature affichent un taux d'engagement des employés **25 % supérieur** à la moyenne (Gallup, 2022)

## Approfondir

### Fonctionnement

La Digital Workplace s'articule autour de plusieurs couches technologiques :

**UCaaS — Unified Communications as a Service**
Plateforme cloud qui unifie la téléphonie, la visioconférence, la messagerie instantanée et la collaboration en temps réel. Exemples : Microsoft Teams, Google Meet, Cisco Webex, Zoom.
- Remplacement des PABX et infrastructures téléphoniques on-premises
- Disponible sur tous les terminaux (PC, mobile, tablette)
- SLA de disponibilité garanti par le fournisseur cloud

**DaaS — Desktop as a Service**
Virtualisation du poste de travail hébergée dans le cloud. L'environnement de travail complet (OS, applications, données) est délivré en streaming sur n'importe quel terminal. Exemples : Azure Virtual Desktop, Amazon WorkSpaces, Citrix DaaS.
- Idéal pour le BYOD et les populations nomades
- Simplifie la gestion du parc (plus de PC physiques à maintenir)
- Voir aussi : [[VDI et client léger]]

**PWA — Progressive Web Apps**
Applications web qui adoptent des comportements d'applications natives : installation sur l'écran d'accueil, fonctionnement hors ligne (service workers), notifications push. Les PWA permettent de déployer des outils métier accessibles depuis n'importe quel navigateur sans passer par les stores Apple/Google.
- Avantage mobilité : une seule base de code pour tous les terminaux
- Mise à jour transparente (pas de déploiement via MDM)
- Limite : accès restreint à certaines API natives du terminal

**API-first**
Approche de conception dans laquelle toutes les fonctionnalités du SI sont exposées via des API documentées avant même de construire les interfaces. Dans le contexte Digital Workplace, elle permet l'intégration native entre outils (Teams + CRM + ERP) et la personnalisation de l'expérience collaborateur.

**Microsoft 365**
Suite SaaS de référence (Teams, SharePoint, OneDrive, Outlook, Power Platform) qui constitue le socle de nombreuses Digital Workplaces. Intégration native avec Azure AD, Intune (UEM), et un écosystème de 5 000+ applications partenaires.

**Google Workspace**
Alternative de Google (Gmail, Drive, Meet, Docs collaboratifs en temps réel). Fort sur la collaboration simultanée et le secteur éducatif. Positionnement cloud-native sans équivalent on-premises.

**DEX — Digital Employee Experience**
Mesure de la qualité de l'expérience numérique des collaborateurs. Indicateurs : temps de chargement des applications, taux de pannes, score de satisfaction, adoption des outils. Des plateformes comme Nexthink, Aternity ou 1E mesurent et améliorent le DEX en temps réel.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Accès aux outils depuis n'importe quel terminal et lieu | Dépendance à la connexion internet (résilience critique) |
| Collaboration en temps réel, réduction des silos | Risque de dispersion et de fatigue numérique (trop d'outils) |
| Réduction des coûts d'infrastructure on-premises | Coûts de licences SaaS récurrents et difficiles à maîtriser |
| Mises à jour automatiques, toujours en version courante | Shadow IT si les outils proposés ne satisfont pas les besoins |
| Améliore l'attractivité et la rétention des talents | Enjeux de souveraineté des données (cloud US : CLOUD Act) |
| Facilite l'intégration des collaborateurs à distance | Nécessite un accompagnement au changement |

### Acteurs et solutions du marché

| Acteur | Solution | Positionnement |
|--------|----------|----------------|
| Microsoft | Microsoft 365 + Teams | Leader mondial, suite la plus complète |
| Google | Google Workspace | Fort sur la collaboration temps réel et les startups |
| Citrix | Citrix DaaS + Virtual Apps | Spécialiste VDI/DaaS, secteurs réglementés |
| Salesforce | Slack + Salesforce Platform | Fort sur les équipes commerciales |
| Atlassian | Confluence + Jira | Référence pour les équipes IT et produit |
| ServiceNow | Employee Center | Portail collaborateur intégré à l'ITSM |
| Nexthink | Nexthink Infinity | Mesure et amélioration du DEX |

### Cas d'usage concrets

**1. Transformation Digital Workplace d'un groupe industriel**
Un groupe de 8 000 salariés migre de Lotus Notes et téléphonie PABX vers Microsoft 365. Teams remplace 100 % des appels téléphoniques internes. SharePoint devient le nouvel intranet. Power Automate automatise les processus RH (validation de congés, onboarding). Le DEX est mesuré via Nexthink : le score passe de 3,2/5 à 4,1/5 en 18 mois.

**2. Cabinet de conseil 100 % en télétravail**
Un cabinet de conseil adopte Google Workspace comme socle Digital Workplace. Toutes les réunions client sont en Google Meet, les propositions commerciales co-rédigées en temps réel dans Google Docs. Les consultants utilisent leurs propres appareils (BYOD) ; l'accès aux données sensibles passe par une PWA sécurisée avec authentification MFA.

**3. Déploiement DaaS pour une banque**
Une banque régionale remplace ses 3 000 postes de travail physiques par Azure Virtual Desktop. Les conseillers accèdent à leur poste complet depuis une tablette légère ou leur domicile. La DSI réduit ses coûts de maintenance matérielle de 40 % et simplifie la gestion de la conformité.

### Chiffres et tendances

- **Microsoft Teams** comptait **300 millions d'utilisateurs actifs mensuels** en 2023
- **59 % des DSI** considèrent l'amélioration du DEX comme une priorité stratégique pour 2024-2025 (Gartner)
- Le DaaS devrait représenter **12 milliards USD de marché en 2026** (IDC)
- Tendance : **AI-powered workplace** — intégration de Copilot (Microsoft), Duet AI (Google) directement dans les outils collaboratifs pour automatiser les tâches répétitives
- La **Digital Workplace souveraine** émerge en France : Citadel Team (Thales), Oodrive, suite collaborative Numerique.gouv.fr pour les administrations publiques

## Flashcards
#flashcards/Mobilité/Digital_Workplace #flashcards/Optimisation_du_SI/Digital_Workplace

Qu'est-ce que la Digital Workplace ? :: L'ensemble des outils, plateformes et services numériques mis à disposition des collaborateurs pour travailler depuis n'importe quel lieu et terminal. Elle intègre communication unifiée (UCaaS), virtualisation du poste (DaaS), collaboration et gestion de l'expérience employé (DEX).

Quelle est la différence entre UCaaS et DaaS ? :: L'UCaaS (Unified Communications as a Service) unifie les outils de communication (téléphonie, visio, messagerie) dans le cloud. Le DaaS (Desktop as a Service) virtualise le poste de travail complet (OS + applications + données) et le délivre en streaming sur n'importe quel terminal.

Qu'est-ce qu'une PWA et quel est son avantage pour la mobilité ? :: Une Progressive Web App est une application web qui se comporte comme une app native (installation, mode hors ligne, notifications). Son avantage mobilité : une seule base de code fonctionne sur tous les terminaux sans passer par les stores Apple/Google.

Qu'est-ce que le DEX (Digital Employee Experience) ? :: La mesure de la qualité de l'expérience numérique des collaborateurs : performance des applications, disponibilité des outils, satisfaction utilisateur. Des plateformes comme Nexthink ou Aternity mesurent et améliorent le DEX en temps réel.

Qu'est-ce que l'approche API-first dans le contexte Digital Workplace ? :: Concevoir toutes les fonctionnalités du SI sous forme d'API documentées avant de construire les interfaces. Cela permet l'intégration native entre outils (Teams + CRM + ERP) et la personnalisation de l'expérience collaborateur.

Quels sont les deux principaux risques de la Digital Workplace pour une DSI ? :: 1) La dépendance à Internet (la panne réseau paralyse tous les outils). 2) Le shadow IT si les outils proposés ne correspondent pas aux besoins réels des utilisateurs, qui cherchent alors des alternatives non validées par la DSI.

Citez un risque de souveraineté lié à la Digital Workplace cloud. :: Les solutions Microsoft 365 et Google Workspace sont soumises au CLOUD Act américain, qui permet aux autorités US d'accéder aux données hébergées par des entreprises américaines, même en Europe. Des alternatives souveraines existent (Citadel Team, Oodrive, suite Numerique.gouv.fr).

## Sources

- Grand View Research, "Digital Workplace Market Size", 2024
- Microsoft Work Trend Index 2023 — microsoft.com/worklab
- Gartner, "Top Strategic Technology Trends", 2024
- IDC, "Desktop as a Service Forecast", 2024
- Nexthink, "Digital Employee Experience Report", 2023
- Gallup, "State of the Global Workplace", 2022

## Notions liées
- [[Gestion de la mobilité (UEM)]]
- [[Télétravail et travail hybride]]
- [[VDI et client léger]]
- [[VPN et accès distant]]
- [[Low-code - No-code]]
- [[RPA (Robotic Process Automation)]]
- [[Cloud souverain]]
- [[SASE - SD-WAN]]
