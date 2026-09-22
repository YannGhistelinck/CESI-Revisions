---
type: notion
thèmes:
  - Mobilité
statut: pas vu
dernière_révision: 
---

# Gestion de la mobilité (UEM)

![[N — Gestion de la mobilité (UEM).mp3]]
## En bref
> **Définition** : L'UEM (Unified Endpoint Management) est une approche unifiée de gestion de l'ensemble des terminaux d'une organisation (smartphones, tablettes, PC, objets connectés) depuis une console centrale. Elle fait converger MDM, MAM et MCM en un seul outil pour administrer le cycle de vie des appareils, des applications et des contenus mobiles.
> **Pourquoi c'est important** : Dans une DSI, la multiplication des terminaux et des usages mobiles crée des risques de sécurité majeurs (perte/vol, fuite de données, shadow IT). L'UEM permet d'appliquer des politiques de sécurité cohérentes tout en maintenant la productivité des collaborateurs, qu'ils utilisent des équipements professionnels ou personnels.
> **Chiffres clés** :
> - Le marché mondial de l'UEM était estimé à **4,7 milliards USD en 2023**, avec une croissance annuelle de ~20 % (MarketsandMarkets, 2024)
> - **72 % des entreprises** ont subi une violation de données liée à un terminal mobile entre 2020 et 2023 (Verizon DBIR, 2023)
> - Un employé utilise en moyenne **3 à 4 appareils** pour travailler (Gartner, 2023)

## Approfondir

### Fonctionnement

L'évolution de la gestion de la mobilité suit une progression logique :

**MDM (Mobile Device Management)** — gestion au niveau du matériel : enrôlement des appareils, configuration à distance, verrouillage, wipe complet. La DSI contrôle l'appareil entier.

**MAM (Mobile Application Management)** — gestion au niveau des applications : déploiement, mise à jour, révocation d'apps professionnelles sans toucher aux données personnelles.

**MCM (Mobile Content Management)** — gestion des contenus : accès sécurisé aux documents d'entreprise depuis les terminaux mobiles.

**EMM (Enterprise Mobility Management)** — combine MDM + MAM + MCM. Introduit la notion de containerisation.

**UEM (Unified Endpoint Management)** — étend l'EMM à tous les types de terminaux (PC Windows/macOS, IoT, etc.) dans une console unique.

**Mécanismes clés :**

- **Enrôlement OTA (Over-The-Air)** : déploiement des profils de configuration et politiques sans contact physique avec l'appareil, via des protocoles comme Apple DEP, Android Enterprise ou Windows Autopilot.
- **Containerisation mobile** : création d'un espace chiffré et isolé sur le terminal (container professionnel) qui cloisonne données pro et perso. Les applications du container ne peuvent pas communiquer avec les apps personnelles.
- **Wipe sélectif** : suppression des seules données et applications professionnelles du container, sans effacer les données personnelles de l'utilisateur. Essentiel en contexte BYOD.
- **Geofencing** : définition de zones géographiques virtuelles. Des actions automatiques se déclenchent quand un appareil entre ou sort d'une zone (activation du VPN, blocage de la caméra dans une zone sensible, etc.).
- **Conformité et remédiation automatique** : un terminal non conforme (OS non à jour, jailbreak détecté, application non autorisée) peut être automatiquement mis en quarantaine ou avoir ses accès révoqués.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Gestion centralisée de tous les terminaux depuis une seule console | Coût de licence élevé (par terminal et par mois) |
| Réduction de la surface d'attaque par les politiques de conformité | Complexité de déploiement et de paramétrage initial |
| Wipe sélectif préserve la vie privée en BYOD | Résistance des utilisateurs (sentiment de surveillance) |
| Déploiement OTA rapide des configurations et patches | Dépendance à un fournisseur (vendor lock-in) |
| Visibilité complète sur le parc de terminaux | Nécessite une connectivité pour les opérations à distance |
| Intégration avec les annuaires d'entreprise (Azure AD, LDAP) | Peut dégrader les performances des appareils anciens |

### Acteurs et solutions du marché

| Solution | Éditeur | Positionnement |
|----------|---------|----------------|
| **Microsoft Intune** | Microsoft | Leader, intégré à Microsoft 365 / Azure AD, très répandu en entreprise |
| **VMware Workspace ONE** | Broadcom (ex-VMware) | Leader Gartner Magic Quadrant, fort sur les flottes mixtes |
| **Jamf** | Jamf | Spécialiste Apple (Mac, iPhone, iPad), très utilisé dans les ESN et le secteur éducatif |
| **MobileIron / Ivanti** | Ivanti | Historique du MDM, désormais intégré dans la suite Ivanti |
| **Citrix Endpoint Management** | Citrix | Intégré à l'écosystème Citrix (VDI, DaaS) |
| **IBM MaaS360** | IBM | Fort sur les industries réglementées |
| **SOTI MobiControl** | SOTI | Spécialiste mobilité terrain (logistique, santé) |

### Cas d'usage concrets

**1. Flotte de commerciaux terrain (COPE)**
Une grande enseigne de distribution équipe ses 5 000 commerciaux terrain de smartphones fournis par l'entreprise. Workspace ONE déploie automatiquement les applications CRM et catalogue produits via OTA, bloque l'accès aux stores personnels, et peut wiper un appareil en cas de perte. Le geofencing active le VPN dès que le terminal quitte le réseau WiFi d'un entrepôt.

**2. Hôpital en contexte BYOD**
Un CHU autorise les médecins à utiliser leurs iPhones personnels pour consulter les dossiers patients. Microsoft Intune crée un container chiffré contenant uniquement les apps hospitalières (DMP, messagerie sécurisée HDS). En cas de départ du praticien, seul le container est effacé (wipe sélectif), les photos personnelles restent intactes.

**3. Usine connectée (IoT/kiosque)**
Un constructeur automobile gère 2 000 tablettes en mode kiosque (COSU) sur les lignes d'assemblage via MDM. Les appareils sont verrouillés sur une seule application de suivi de production ; tout écart de configuration déclenche une alerte et une remédiation automatique.

### Chiffres et tendances

- **Croissance du marché UEM** : +18 % par an jusqu'en 2028, porté par la généralisation du travail hybride (IDC, 2024)
- **67 % des DSI** prévoient d'unifier la gestion endpoints sous une seule plateforme UEM d'ici 2025 (Gartner)
- **Microsoft Intune** gère plus de **150 millions de terminaux** dans le monde (Microsoft, 2024)
- Le coût moyen d'un incident lié à un terminal mobile perdu ou volé est estimé à **26 000 € par incident** pour une PME (Ponemon Institute, 2022)
- Tendance : convergence UEM + **ZTNA** (Zero Trust Network Access) pour une gestion unifiée des accès et des terminaux

## Flashcards
#flashcards/Mobilité/Gestion_de_la_mobilité_UEM

Qu'est-ce que l'UEM et en quoi diffère-t-il de l'EMM ? :: L'UEM (Unified Endpoint Management) unifie la gestion de tous les types de terminaux (PC, mobiles, IoT) dans une seule console, là où l'EMM se limitait aux appareils mobiles. L'UEM est l'évolution naturelle de l'EMM.

Qu'est-ce que le wipe sélectif et dans quel contexte est-il indispensable ? :: Le wipe sélectif supprime uniquement les données et applications professionnelles d'un terminal, sans toucher aux données personnelles. Il est indispensable en contexte BYOD pour préserver la vie privée du collaborateur tout en sécurisant les données de l'entreprise.

Quelle est la différence entre MDM et MAM ? :: Le MDM (Mobile Device Management) gère l'appareil entier (configuration, verrouillage, wipe complet). Le MAM (Mobile Application Management) gère uniquement les applications professionnelles sans contrôler l'appareil, ce qui est moins intrusif pour l'utilisateur.

Qu'est-ce que l'enrôlement OTA ? :: L'enrôlement OTA (Over-The-Air) permet de déployer les profils de configuration et les politiques de sécurité sur les terminaux à distance, sans contact physique, via des programmes comme Apple DEP, Android Enterprise ou Windows Autopilot.

Comment fonctionne la containerisation mobile ? :: Elle crée un espace chiffré et isolé sur le terminal (le container pro) qui cloisonne totalement les données et applications professionnelles des données personnelles. Les applications du container ne peuvent pas interagir avec les apps hors container.

Qu'est-ce que le geofencing en contexte MDM ? :: Le geofencing définit des zones géographiques virtuelles et déclenche automatiquement des actions lorsqu'un appareil entre ou sort d'une zone : activation du VPN, blocage de la caméra en zone sensible, restriction d'accès aux données confidentielles.

Citez deux leaders du marché UEM et leur positionnement. :: Microsoft Intune : leader intégré à l'écosystème Microsoft 365/Azure AD, très répandu dans les entreprises utilisant Microsoft. VMware Workspace ONE (Broadcom) : leader Gartner, fort sur les flottes mixtes et les grandes organisations.

## Sources

- Gartner Magic Quadrant for Unified Endpoint Management Tools, 2023-2024
- MarketsandMarkets, "Unified Endpoint Management Market", 2024
- Verizon Mobile Security Index (DBIR), 2023
- Microsoft Intune documentation — learn.microsoft.com
- Ponemon Institute, "Cost of Insider Threats", 2022
- IDC, "Worldwide Unified Endpoint Management Forecast", 2024

## Notions liées
- [[Politiques de terminaux (BYOD - COPE)]]
- [[Zero Trust]]
- [[VPN et accès distant]]
- [[Télétravail et travail hybride]]
- [[Digital Workplace]]
- [[Thème 2 — Cybersécurité]]
