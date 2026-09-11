---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Industrie 4.0 et XR

## En bref
> **Définition** : L'Industrie 4.0 désigne la quatrième révolution industrielle, caractérisée par la convergence des technologies numériques (IoT, IA, big data, robotique, cloud, XR) avec les systèmes de production physiques. La réalité étendue (XR) y joue un rôle central en transformant la formation des opérateurs, la maintenance des équipements et la conception des lignes de production.
> **Pourquoi c'est important** : Les DSI industrielles font face à un double défi : moderniser des systèmes OT (Operational Technology) souvent vieux de 20 à 30 ans tout en formant une main-d'œuvre sur des équipements complexes. Le XR adresse ces deux enjeux en rendant la formation immersive, la maintenance guidée et la conception collaborative sans nécessiter d'arrêt de production.
> **Chiffres clés** :
> - Le marché mondial de l'Industrie 4.0 atteindra 377 Md$ en 2029 (Fortune Business Insights, 2023).
> - L'utilisation du XR en formation industrielle réduit le temps de formation de 40 % et améliore la rétention de 75 % par rapport aux méthodes traditionnelles (PwC, 2022).
> - Boeing a réduit ses temps de câblage d'avion de 25 % grâce à la RA (AR) avec HoloLens (2019).

## Approfondir

### Fonctionnement

**Les quatre révolutions industrielles**
- Industrie 1.0 (fin XVIIIe) : vapeur, mécanisation
- Industrie 2.0 (fin XIXe) : électricité, production de masse
- Industrie 3.0 (années 1970) : automatisation, électronique, informatique
- Industrie 4.0 (depuis 2011) : cyber-physique, IoT, IA, big data, XR — terme forgé par le gouvernement allemand (Klaus Schwab, WEF)

**Piliers technologiques de l'Industrie 4.0**
1. **IoT industriel (IIoT)** : capteurs connectés sur les machines pour monitorer en temps réel.
2. **Big Data et IA** : analyse des données machines pour la maintenance prédictive et l'optimisation.
3. **Cloud et Edge Computing** : traitement des données au plus près des machines (edge) ou dans le cloud.
4. **Robotique collaborative (cobots)** : robots partageant l'espace de travail avec les humains.
5. **Fabrication additive (impression 3D)** : prototypage rapide et production de pièces complexes.
6. **Cybersécurité OT/IT** : convergence des réseaux informatiques et opérationnels.
7. **Réalité étendue (XR)** : formation immersive, maintenance guidée, conception collaborative.

**Formation immersive en VR**
La VR permet de former les opérateurs industriels sur des scénarios inaccessibles en conditions réelles : intervention sur équipements haute tension, procédures d'urgence (incendie, déversement chimique), montage de machines complexes. Avantages : répétition illimitée sans risque, sans mobiliser l'équipement réel, disponibilité 24/7, traçabilité automatique de la progression.
Plateformes : Immerse (formation VR enterprise), Strivr, Pixaera, interne Unity/Unreal Engine.

**Maintenance augmentée en RA**
Un technicien portant des lunettes AR (HoloLens 2, RealWear) voit des instructions étape par étape superposées sur l'équipement réel, des vues explosées des composants, des alertes en temps réel depuis les capteurs IoT, et peut partager son point de vue avec un expert distant (Remote Assist). Élimine le besoin de consulter des manuels papier et réduit drastiquement les erreurs.
Outils : PTC Vuforia Expert Capture, TeamViewer Frontline (ex-ubimax), Scope AR, Microsoft Dynamics 365 Remote Assist.

**Conception et simulation en XR**
La RA/RM permet aux ingénieurs de visualiser un équipement ou une ligne de production en taille réelle dans l'espace physique avant sa fabrication (maquette numérique 1:1). La VR permet de simuler l'ergonomie des postes de travail, de tester les flux de production, et de former les équipes avant l'ouverture d'une nouvelle usine (digital twin + XR).

**Dispositifs clés**

*Microsoft HoloLens 2*
Casque de réalité mixte (RM) autonome, résolution 2K par œil, champ de vision 52°, main tracking, eye tracking. Le référentiel enterprise en RM. Plateforme : Windows Mixed Reality, Azure, Mesh. Cas d'usage : maintenance guidée, télé-expertise, visualisation BIM. Prix : environ 3 500 €.

*Meta Quest (2, 3, Pro)*
Casque VR/MR standalone grand public et enterprise. Le Meta Quest 3 intègre le passthrough couleur (RA via caméras) avec 4K par œil. Très utilisé pour la formation VR enterprise grâce à son prix accessible (< 600 €). Plateforme : Android (Meta Horizon OS), Meta Business Suite.

*Apple Vision Pro*
Casque de spatial computing (visionOS, 2024). Résolution micro-OLED 4K par œil, eye tracking, hand tracking, passthrough haute fidélité. Positionné sur les usages professionnels haut de gamme (visualisation 3D, collaboration spatiale). Prix : 3 500 $.

*RealWear Navigator*
Lunettes AR rugged montées sur la tête (head-mounted), mains libres, résistantes IP66, contrôle vocal. Conçues pour les environnements industriels difficiles (bruit, eau, chaleur). Leader sur le marché de la maintenance industrielle AR mains-libres.

**Unity et Unreal Engine dans l'Industrie 4.0**
- **Unity** : moteur de développement XR dominant (70 % des expériences XR). Intégration native HoloLens, Quest, iOS/Android AR. Package XR Interaction Toolkit. Utilisé par Volkswagen, Porsche, Renault pour leurs simulateurs et formations XR.
- **Unreal Engine** (Epic Games) : haute fidélité graphique, photoréalisme. Utilisé pour les digital twins d'usines (Omniverse + Unreal), les simulations de lignes de production, les présentations clients interactives. Intégration NVIDIA RTX et ray tracing.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Formation sans risque et sans mobiliser l'équipement | Coût de création du contenu XR élevé (60 000 à 200 000 € par module) |
| Réduction des erreurs de maintenance (guidage étape par étape) | Résistance au changement des opérateurs expérimentés |
| Collaboration expert-technicien à distance (télé-expertise) | Ergonomie des dispositifs limitée pour les longues sessions |
| Traçabilité automatique des interventions | Interopérabilité OT/IT complexe (protocoles industriels legacy) |
| Réduction des déplacements d'experts (impact carbone) | Cybersécurité OT : exposition des systèmes industriels via les connexions XR |

### Acteurs et solutions du marché
| Acteur | Offre |
|--------|-------|
| Microsoft | HoloLens 2, Dynamics 365 Remote Assist, Dynamics 365 Guides, Azure Mixed Reality |
| Meta | Quest 3 / Quest Pro, Meta Horizon Workrooms, Meta Business Suite |
| Apple | Vision Pro, ARKit, RealityKit, visionOS SDK |
| PTC | Vuforia (RA industrielle n°1), Vuforia Expert Capture, ThingWorx |
| TeamViewer | Frontline (ex-ubimax) — wearables AR pour logistique et industrie |
| Scope AR | WorkLink — plateforme de maintenance AR guidée |
| Immerse / Strivr | Plateformes de formation VR enterprise |
| Unity Technologies | Unity Engine, Unity Simulation Pro |
| Epic Games | Unreal Engine, MetaHuman (avatars photoréalistes) |
| RealWear | Navigator 520 — lunettes AR rugged industrielles |
| Siemens | SIMATIC, Teamcenter, intégration XR dans la chaîne PLM |

### Cas d'usage concrets
1. **Boeing** : utilise la RA (HoloLens) pour le câblage des ailes d'avion, réduisant le temps de câblage de 25 % et les erreurs de 50 % en guidant les techniciens étape par étape avec des instructions holographiques superposées sur les harnais réels.
2. **Renault Group** : déploie des formations VR sur Meta Quest pour former les mécaniciens à l'entretien de ses véhicules électriques (Zoé, Mégane E-Tech) dans ses centres de formation mondiaux, remplaçant les véhicules démonstrateurs physiques coûteux.
3. **Thales** : utilise la VR (Unity + Varjo) pour former les pilotes de chasse et les opérateurs de radar dans des environnements virtuels reproduisant des scénarios de combat inaccessibles en conditions réelles, avec un niveau de fidélité militaire.
4. **SNCF** : déploie des formations en VR (Meta Quest) pour la maintenance des voies ferrées et les procédures d'urgence en tunnel, avec traçabilité des compétences intégrée dans le LMS corporate.

### Chiffres et tendances
- Le marché de la formation industrielle en VR est estimé à 6,3 Md$ en 2027 (Allied Market Research, 2022).
- 30 % des accidents du travail en industrie pourraient être évités grâce à une meilleure formation (OIT, 2022) — la VR est identifiée comme un levier clé.
- L'adoption du XR dans l'industrie automobile a progressé de 120 % entre 2020 et 2023 (IDC).
- Les technologies XR génèrent 60 % de réduction du temps de diagnostic lors des interventions de maintenance guidée (PTC, 2023).

## Flashcards
#flashcards/Développement/Industrie_4_0_et_XR
- Qu'est-ce que l'Industrie 4.0 ? :: La quatrième révolution industrielle (depuis 2011), caractérisée par la convergence du numérique (IoT, IA, cloud, XR, robotique) avec les systèmes de production physiques.
- Quels sont les trois principaux usages du XR dans l'industrie ? :: La formation immersive (VR), la maintenance augmentée (RA), et la conception collaborative (RM/VR sur maquette numérique).
- Quelle est la différence entre HoloLens 2 et Meta Quest 3 ? :: HoloLens 2 est un casque de réalité mixte enterprise (hologrammes dans l'espace réel, ~3 500 €) ; Meta Quest 3 est un casque VR/MR grand public et enterprise (passthrough couleur, < 600 €).
- Qu'est-ce que la maintenance augmentée ? :: L'utilisation de lunettes AR (HoloLens, RealWear) pour guider un technicien étape par étape lors d'une intervention, avec instructions superposées sur l'équipement réel et télé-expertise à distance.
- Quel est l'avantage de la formation VR par rapport à la formation classique ? :: Répétition illimitée sans risque, sans mobiliser l'équipement réel, disponibilité 24/7, traçabilité automatique, et rétention 75 % supérieure (PwC, 2022).
- Qu'est-ce que Vuforia (PTC) ? :: La plateforme de réalité augmentée industrielle leader (PTC), intégrant la reconnaissance d'équipements, les instructions de maintenance guidée et la connexion aux données IoT/digital twin.
- Quel résultat Boeing a-t-il obtenu avec la RA sur HoloLens ? :: Réduction de 25 % du temps de câblage des ailes et de 50 % des erreurs, grâce aux instructions holographiques superposées sur les harnais réels.

## Sources
- PwC Seeing is Believing — The power of VR/AR 2022 : https://www.pwc.com/us/en/tech-effect/ai-analytics/augmented-and-virtual-reality.html
- Fortune Business Insights — Industry 4.0 Market Report 2023 : https://www.fortunebusinessinsights.com/industry-4-0-market-102375.html
- Microsoft HoloLens 2 : https://www.microsoft.com/en-us/hololens
- PTC Vuforia : https://www.ptc.com/en/products/vuforia
- Boeing AR Wiring Assembly Study (2019) : https://news.microsoft.com/transform/boeing-hololens/
- Meta Quest for Business : https://www.meta.com/en-gb/quest/business/
- Apple Vision Pro : https://www.apple.com/apple-vision-pro/

## Notions liées
- [[Réalité étendue (XR)]]
- [[Digital Twin]]
- [[IA en cybersécurité]]
- [[Écoconception logicielle]]
- [[Big Data — fondamentaux]]
- [[Infrastructure des datacenters]]
