---
type: notion
thèmes:
  - SI et environnement
  - Développement
statut: pas vu
dernière_révision: 
---

# Écoconception logicielle

![[N — Écoconception logicielle.mp3]]
## En bref
> **Définition** : L'écoconception logicielle consiste à intégrer les critères environnementaux dès la conception d'un service numérique afin de minimiser son empreinte tout au long de son cycle de vie. Elle agit sur la consommation de ressources matérielles (CPU, RAM, réseau, stockage) et prolonge la compatibilité avec des équipements anciens.
> **Pourquoi c'est important** : Un logiciel "lourd" accélère l'obsolescence des terminaux, principal poste d'impact du numérique. La DSI peut réduire significativement l'empreinte environnementale et les coûts d'infrastructure en appliquant des pratiques d'écoconception sur les services internes et les applications métiers.
> **Chiffres clés** :
> - Le RGESN compte 79 critères organisés en 9 thématiques (version 2024, DINUM/MTE)
> - Le GR491 (référentiel de l'INR) liste 491 bonnes pratiques pour les services numériques responsables
> - Un site web moyen émet environ 0,5 g de CO₂ par page vue ; un site mal conçu peut dépasser 5 g (WebsiteCarbon.com)

## Approfondir

### Fonctionnement

**Les principes fondamentaux**
L'écoconception logicielle vise à réduire la consommation de ressources à chaque couche du service :
- **Réseau** : réduire le poids des pages, optimiser les requêtes, limiter les appels superflus
- **Serveur** : optimiser les algorithmes, utiliser des langages/frameworks moins gourmands, éviter le sur-provisionnement
- **Client** : limiter le JavaScript exécuté côté navigateur, réduire la complexité des rendus
- **UX/fonctionnel** : supprimer les fonctionnalités inutiles, éviter l'auto-play vidéo, la lecture infinie, les notifications superflues

**RGESN — Référentiel Général d'Écoconception de Services Numériques**
Référentiel officiel publié par la DINUM et le Ministère de la Transition Écologique. Version 2024 : 79 critères répartis en 9 thématiques (stratégie, spécifications, architecture, UX/UI, contenus, frontend, backend, hébergement, contenu hors-ligne). Applicable aux services numériques publics, utilisé de plus en plus dans le secteur privé.

**GR491 — Guide de Référence de Conception Responsable de Services Numériques**
Publié par l'INR (Institut du Numérique Responsable). 491 bonnes pratiques organisées par cycle de vie et rôle (chef de projet, designer, développeur, ops). Plus exhaustif que le RGESN, sert de base à des audits approfondis et à la formation.

**Obsolescence logicielle**
Un logiciel est dit "obsosolète" quand il nécessite du matériel plus récent pour fonctionner correctement, forçant le renouvellement des équipements. L'écoconception vise à maintenir la compatibilité avec des équipements de 5-7 ans pour réduire les achats de terminaux.

**Démarche pratique**
1. Mesurer l'état initial (EcoIndex, Greenspector, GreenIT-Analysis)
2. Identifier les points critiques (pages les plus consultées, fonctionnalités les plus gourmandes)
3. Prioriser les actions correctives selon impact/effort
4. Intégrer les critères en amont dans les specs et les critères d'acceptation
5. Suivre les indicateurs dans la CI/CD (automatisation des mesures)

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction de l'empreinte environnementale du SI | Nécessite une montée en compétences des équipes |
| Amélioration des performances (pages plus légères = UX meilleure) | Peut allonger les cycles de développement si non intégré dès le début |
| Allongement de la durée de vie des équipements utilisateurs | Arbitrages difficiles entre richesse fonctionnelle et sobriété |
| Conformité aux obligations légales (REEN pour le public) | Manque d'outillage mature dans les IDE et pipelines CI/CD |
| Réduction des coûts d'hébergement (moins de ressources consommées) | Résistance des équipes habituées à des frameworks lourds |

### Acteurs et solutions du marché
- **DINUM / MTE** : publient et maintiennent le RGESN
- **INR** : GR491, label NR, formations certifiantes
- **Collectif Numérique Responsable** : EcoIndex (outil de mesure)
- **Greenspector** : solution de mesure de l'impact des applications mobiles et web
- **Frugal** : plugin VSCode pour guider l'écoconception en temps réel
- **Ecodesign-checklist** (Lunatech) : checklists pratiques pour les équipes dev

### Cas d'usage concrets
1. **La MAIF** : refonte de son espace client avec une démarche d'écoconception intégrée, réduction du poids des pages de 60 %, amélioration du score EcoIndex de E à B.
2. **Direction Interministérielle du Numérique (DINUM)** : déploiement du RGESN sur services.gouv.fr, audit régulier des services en ligne de l'État.
3. **Décathlon** : optimisation du site e-commerce avec réduction des scripts tiers et du poids des images ; gain mesuré en temps de chargement et en score Lighthouse.

### Chiffres et tendances
- Le JavaScript est responsable d'une large part de la consommation CPU côté client ; des frameworks comme Svelte ou Astro consomment 3 à 10x moins qu'un SPA React équivalent
- Un transfert de données de 1 Mo via réseau mobile émet environ 0,4 g CO₂ eq (réseau 4G, valeur moyenne)
- Les images représentent en moyenne 50-60 % du poids des pages web (HTTP Archive, 2024)
- La loi REEN (2021) impose aux communes de plus de 50 000 habitants une stratégie NR incluant l'écoconception des services publics numériques

## Flashcards
#flashcards/SI_et_environnement/Écoconception_logicielle #flashcards/Développement/Écoconception_logicielle

Qu'est-ce que le RGESN ? :: Le Référentiel Général d'Écoconception de Services Numériques, publié par la DINUM et le MTE. Il comporte 79 critères organisés en 9 thématiques pour réduire l'empreinte des services numériques.

Quelle est la différence entre le RGESN et le GR491 ? :: Le RGESN (79 critères, DINUM) est le référentiel officiel français ciblant les services numériques publics. Le GR491 (491 bonnes pratiques, INR) est plus exhaustif et couvre l'ensemble du cycle de vie d'un service numérique responsable.

Pourquoi l'écoconception logicielle réduit-elle l'obsolescence matérielle ? :: Un logiciel sobre consomme moins de CPU/RAM et reste compatible avec des équipements anciens, réduisant le besoin de renouvellement des terminaux, principal poste d'impact du numérique.

Citez 3 leviers techniques d'écoconception logicielle. :: 1) Réduire le poids des pages (images, JS, CSS). 2) Optimiser les algorithmes côté serveur. 3) Supprimer les fonctionnalités inutiles et les requêtes réseau superflues.

Quelle loi impose l'écoconception aux services numériques publics en France ? :: La loi REEN (Réduction de l'Empreinte Environnementale du Numérique), adoptée en novembre 2021.

Comment intégrer l'écoconception dans un pipeline CI/CD ? :: En automatisant des mesures d'impact (EcoIndex, Lighthouse, Greenspector) à chaque build/déploiement et en définissant des seuils d'alerte ou de blocage dans la pipeline.

## Sources
- RGESN officiel (DINUM/MTE) : https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/
- GR491 (INR) : https://gr491.isit-europe.org
- Collectif numérique responsable / EcoIndex : https://www.ecoindex.fr
- Loi REEN (Légifrance) : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044327272
- HTTP Archive (stats poids pages web) : https://httparchive.org/reports/page-weight

## Notions liées
- [[Fiche 9 : Sobriété numérique]]
- [[Fiche 12 : Outils de mesure d'impact environnemental]]
- [[Fiche 13 : Cadre réglementaire environnemental du SI]]
- [[Fiche 14 : Normes ISO environnementales]]
- [[Fiche 16 : Acteurs du numérique responsable]]
