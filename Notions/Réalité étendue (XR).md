---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Réalité étendue (XR)

![[N — Réalité étendue (XR).mp3]]
## En bref
> **Définition** : La réalité étendue (Extended Reality — XR) est un terme générique désignant l'ensemble des technologies qui altèrent ou enrichissent la perception de la réalité par superposition ou immersion numérique. Elle englobe la réalité augmentée (RA), la réalité virtuelle (RV) et la réalité mixte (RM), positionnées sur le continuum de Milgram entre le monde réel pur et l'environnement virtuel total.
> **Pourquoi c'est important** : Pour une DSI, le XR représente un levier de transformation des usages professionnels (formation, maintenance, collaboration distante, conception) et grand public (retail, santé, éducation). Il constitue la couche d'interface entre le monde physique et les jumeaux numériques, le Metaverse industriel et le spatial computing.
> **Chiffres clés** :
> - Le marché mondial du XR atteindra 1 700 Md$ en 2030 (Grand View Research, 2023).
> - 14,4 millions de casques XR vendus en 2023 dans le monde, dont 80 % en RV standalone (Meta Quest) (IDC, 2024).
> - 75 % des entreprises du Fortune 500 utilisent déjà une forme de XR pour la formation ou la maintenance (PTC, 2023).

## Approfondir

### Fonctionnement

**Le continuum de Milgram (1994)**
Paul Milgram et Fumio Kishino ont défini un spectre allant du monde réel (à gauche) à l'environnement virtuel total (à droite) :
`Réalité → Réalité Augmentée → Réalité Mixte → Réalité Virtuelle`
- **Réalité augmentée (RA / AR)** : superpose des éléments numériques 2D ou 3D sur le monde réel via une caméra (smartphone, lunettes). Le monde réel reste prépondérant. Exemples : Pokémon GO, IKEA Place, marqueurs de navigation Google Maps.
- **Réalité mixte (RM / MR)** : les objets numériques interagissent avec le monde réel en temps réel (ancrage spatial, occlusion). Exemple : HoloLens 2 (Microsoft) — un objet 3D peut se cacher derrière une table réelle.
- **Réalité virtuelle (RV / VR)** : immersion totale dans un environnement 100 % numérique via un casque opaque. Le monde réel est totalement occulté. Exemples : Meta Quest 3, PlayStation VR2, Valve Index.

**Technologies clés**

*SLAM (Simultaneous Localization and Mapping)*
Algorithme fondamental du XR : le dispositif cartographie son environnement en temps réel tout en se localisant dedans, sans GPS. Permet l'ancrage précis des objets virtuels dans l'espace physique. Variantes : Visual SLAM (caméras), LiDAR SLAM (Apple ProLiDAR), Dense SLAM.

*Spatial Computing*
Terme popularisé par Apple avec le Vision Pro (2024). Désigne le paradigme dans lequel l'interface utilisateur s'étend dans l'espace tridimensionnel de l'utilisateur, en combinant vision, audio spatial, suivi des mains et des yeux. Représente l'évolution de l'ordinateur personnel vers l'ordinateur ambiant.

*Inside-out tracking vs Outside-in tracking*
- **Inside-out** : les capteurs sont sur le casque lui-même (caméras, IMU). Aucune infrastructure externe nécessaire. Dominant dans les casques modernes (Meta Quest, HoloLens).
- **Outside-in** : des balises externes (base stations) localisent le casque. Précision maximale mais installation complexe (Valve Index, anciens PS VR).

*Hand tracking et Eye tracking*
Les casques modernes (Meta Quest 3, Apple Vision Pro) détectent les mains et le regard sans contrôleur physique. L'eye tracking permet le "foveated rendering" (rendu haute résolution uniquement là où l'œil regarde), réduisant drastiquement la charge GPU.

*Passthrough*
Caméras couleur sur le casque transmettant une vue en temps réel du monde réel à l'intérieur du casque VR. Permet de passer de la VR à une RA de haute qualité sans changer de dispositif (Meta Quest 3, Apple Vision Pro).

**Moteurs de développement XR**
- **Unity** : moteur de jeu 3D dominant en XR (70 % des expériences XR développées avec Unity). Supporte toutes les plateformes XR via le XR Interaction Toolkit et OpenXR.
- **Unreal Engine** (Epic Games) : moteur haute fidélité utilisé pour les expériences XR photoréalistes (visualisation architecturale, formation militaire, films virtuels).
- **WebXR** : API W3C permettant les expériences XR dans le navigateur sans installation (A-Frame, Babylon.js).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Apprentissage par l'expérience (meilleure rétention) | Coût élevé des dispositifs et du développement de contenu |
| Réduction des risques (formation sur scénarios dangereux) | Risques de cybersickness (nausée, désorientation) |
| Collaboration distante en espace partagé virtuel | Maturité variable selon les secteurs d'usage |
| Ancrage dans l'espace physique (maintenance guidée) | Problèmes d'ergonomie et de confort pour les longues sessions |
| Visualisation de données complexes en 3D | Confidentialité et sécurité des données spatiales (cartographie de l'espace privé) |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Meta | Quest 3 (RV/MR grand public), Presence Platform (hand tracking, passthrough) |
| Microsoft | HoloLens 2 (RM enterprise), Azure Mixed Reality (Spatial Anchors, Remote Rendering) |
| Apple | Vision Pro (spatial computing, visionOS), Apple ARKit |
| Google | ARCore (framework RA Android), Google Glass Enterprise Edition |
| PTC | Vuforia (plateforme RA industrielle, n°1 marché enterprise) |
| Unity Technologies | Unity Engine (XR), Unity Simulation Pro |
| Epic Games | Unreal Engine (XR haute fidélité) |
| Varjo | Casques VR/XR ultra haute résolution pour usage professionnel |

### Cas d'usage concrets
1. **Airbus** : utilise la RA (HoloLens 2 + Vuforia) pour guider les techniciens dans le câblage des ailes d'avion, réduisant les erreurs de 40 % et le temps de formation de 30 % par rapport aux manuels papier.
2. **SNCF** : déploie des formations en réalité virtuelle pour simuler des situations d'urgence ferroviaire (incendie en tunnel, évacuation) que l'on ne peut pas recréer en conditions réelles, avec un taux de rétention de 75 % supérieur aux formations classiques.
3. **Renault** : utilise le jumeau numérique XR pour la conception des usines — les ingénieurs se déplacent virtuellement dans l'usine avant sa construction pour valider l'ergonomie des postes de travail.

### Chiffres et tendances
- Apple Vision Pro a généré 200 000 applications visionOS dans sa première année de commercialisation (2024).
- Le SLAM est désormais intégré dans tous les smartphones haut de gamme (ARCore, ARKit) touchant 3 milliards d'appareils.
- Le WebXR rend les expériences XR accessibles sans casque sur 2 milliards de navigateurs compatibles.
- 40 % des cas d'usage XR enterprise concernent la formation et l'onboarding (IDC, 2023).

## Flashcards
#flashcards/Développement/Réalité_étendue_XR
- Que signifie XR ? :: Extended Reality (réalité étendue) — terme générique englobant la réalité augmentée (RA), la réalité mixte (RM) et la réalité virtuelle (RV).
- Qu'est-ce que le continuum de Milgram ? :: Un spectre (Milgram & Kishino, 1994) allant du monde réel pur à l'environnement virtuel total, avec la RA et la RM comme points intermédiaires.
- Quelle est la différence entre RA et RM ? :: En RA, les éléments numériques sont superposés sur le réel sans interaction physique ; en RM, les objets numériques interagissent avec l'environnement réel en temps réel (occlusion, ancrage spatial).
- Qu'est-ce que le SLAM ? :: Simultaneous Localization and Mapping — algorithme qui cartographie l'environnement et localise le dispositif en temps réel sans GPS, fondamental pour ancrer les objets XR dans l'espace.
- Qu'est-ce que le Spatial Computing ? :: Un paradigme (popularisé par Apple Vision Pro) où l'interface s'étend dans l'espace tridimensionnel via combinaison de vision, audio spatial, suivi des mains et des yeux.
- Quelle est la différence entre inside-out et outside-in tracking ? :: Inside-out : capteurs sur le casque, aucune infrastructure externe. Outside-in : balises externes pour localiser le casque avec une précision maximale.
- Qu'est-ce que le Foveated Rendering ? :: Technique qui rend en haute résolution uniquement la zone regardée par l'œil (détectée par eye tracking), réduisant la charge GPU de 50 à 80 %.

## Sources
- Grand View Research — Extended Reality Market Report 2023 : https://www.grandviewresearch.com/industry-analysis/extended-reality-market
- IDC — Worldwide AR/VR Headset Tracker 2024 : https://www.idc.com/
- Apple Vision Pro — visionOS Developer Documentation : https://developer.apple.com/visionos/
- Microsoft HoloLens 2 : https://www.microsoft.com/en-us/hololens
- Unity XR Interaction Toolkit : https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@latest
- Milgram, P. & Kishino, F. (1994). A Taxonomy of Mixed Reality Visual Displays. IEICE Transactions on Information Systems.

## Notions liées
- [[Digital Twin]]
- [[Industrie 4.0 et XR]]
- [[Écoconception logicielle]]
- [[Cloud Native et 12-Factor App]]
- [[Virtualisation]]
