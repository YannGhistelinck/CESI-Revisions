---
type: notion
thèmes:
  - Cloud et Virtualisation
  - Big DATA
statut: pas vu
dernière_révision: 
---

# Data Act

![[N — Data Act.mp3]]
## En bref
> **Définition** : Le **Data Act** est un règlement européen entré en vigueur le 11 janvier 2024 (applicable à partir de septembre 2025) qui régit le partage, l'accès et l'utilisation des données générées par les produits connectés (IoT) et les services associés. Il complète le **Data Governance Act** (DGA, en application depuis septembre 2023), qui encadre quant à lui les mécanismes de partage volontaire de données entre entreprises, avec le secteur public et via des intermédiaires de données (data intermediaries).
> **Pourquoi c'est important** : Pour une DSI, le Data Act impose de nouvelles obligations sur les fabricants de produits connectés et les fournisseurs de services cloud : portabilité des données, droits d'accès des utilisateurs, changement de fournisseur cloud facilité. Il redessine les règles du marché européen de la donnée et renforce la souveraineté numérique de l'UE.
> **Chiffres clés** :
> - L'UE estime que le Data Act libérera 270 Md€ de valeur économique d'ici 2028 (Commission européenne).
> - 80 % des données industrielles ne sont jamais utilisées ni réutilisées (Commission européenne, 2020).
> - Le marché européen de la donnée devrait atteindre 829 Md€ en 2025 (European Data Market Study).

## Approfondir

### Fonctionnement

**Data Act (Règlement UE 2023/2854)**

Entré en vigueur le 11 janvier 2024, applicable à partir du **12 septembre 2025**.

Principes clés :
1. **Droit d'accès aux données des produits connectés** : les utilisateurs (particuliers et entreprises) ont le droit d'accéder aux données générées par les produits IoT qu'ils utilisent (voitures connectées, machines industrielles, appareils ménagers intelligents). Jusqu'ici, ces données appartiennent de facto au fabricant.
2. **Droit au partage de données** : les utilisateurs peuvent demander que les fabricants partagent ces données avec des tiers (prestataires de service, concurrents du fabricant pour la maintenance, etc.).
3. **Obligations pour les fournisseurs cloud (switching facilité)** : les fournisseurs cloud doivent supprimer les obstacles au changement de fournisseur (vendor lock-in). Ils doivent garantir la portabilité technique des données et services, et réduire progressivement à zéro les frais de migration (switching fees) d'ici 2027.
4. **B2G (Business-to-Government) data sharing** : en cas de nécessité publique (crise, catastrophe naturelle), les autorités peuvent demander aux entreprises de partager des données pertinentes.
5. **Protection des secrets commerciaux** : le Data Act ne contraint pas au partage de données qui constitueraient des secrets commerciaux, sous conditions.
6. **Conditions contractuelles équitables** : encadrement des contrats de partage de données B2B pour éviter les clauses abusives (protège surtout les PME face aux grandes plateformes).

**Data Governance Act (DGA — Règlement UE 2022/868)**

En application depuis le **23 septembre 2023**.

Complémentaire au Data Act, il se concentre sur les mécanismes de confiance pour le partage de données :
1. **Réutilisation des données du secteur public** : encadrement de la mise à disposition de données publiques protégées (données personnelles, confidentielles) pour une réutilisation dans l'intérêt général.
2. **Intermédiaires de données (data intermediaries)** : création d'un statut réglementé pour les entités facilitant le partage de données entre acteurs (elles ne peuvent pas utiliser les données elles-mêmes — neutralité).
3. **Altruisme des données (data altruism)** : cadre légal pour que des personnes ou entreprises partagent volontairement leurs données pour l'intérêt général (recherche médicale, bien commun).
4. **Comité européen de l'innovation dans le domaine des données (CEID)** : organe consultatif pour coordonner les pratiques de gouvernance des données dans l'UE.

**Articulation des textes européens sur la donnée :**
| Texte | Portée | En vigueur |
|-------|--------|------------|
| RGPD (2018) | Données personnelles | Mai 2018 |
| Data Governance Act (2022) | Partage de données, intermédiaires | Sept. 2023 |
| Data Act (2023) | IoT, cloud switching, B2B/B2G | Janv. 2024 (applicable sept. 2025) |
| AI Act (2024) | Données d'entraînement IA | 2024-2026 (déploiement progressif) |
| EHDS (European Health Data Space) | Données de santé | En négociation |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Droit d'accès aux données IoT pour les utilisateurs | Complexité de mise en conformité pour les fabricants IoT |
| Réduction du vendor lock-in cloud (portabilité) | Risque de freiner l'innovation si le partage est mal encadré |
| Ouverture du marché des services de maintenance (concurrence) | Tensions avec la protection des secrets commerciaux |
| Renforcement de la souveraineté numérique européenne | Incertitude sur les modalités techniques de portabilité cloud |
| Stimulation d'un marché européen de la donnée | Adaptation des systèmes d'information potentiellement coûteuse |
| Protection des PME contre les clauses B2B abusives | Délais d'application courts pour certains acteurs |

### Acteurs et solutions du marché
| Acteur / Rôle | Impact Data Act |
|--------------|-----------------|
| AWS, Azure, GCP | Obligation de supprimer les switching fees d'ici 2027 et garantir la portabilité |
| OVHcloud, Scaleway | Positionnement favorable : déjà engagés sur la portabilité et la transparence |
| Fabricants IoT (Bosch, Siemens, constructeurs auto) | Obligation de partager les données produit avec les utilisateurs |
| Gaia-X | Initiative européenne d'infrastructure de données qui s'appuie sur le DGA/Data Act |
| IDSA (International Data Spaces Association) | Fournit des standards techniques (connecteurs IDS) pour le partage sécurisé de données |
| Intermédiaires de données (ex : Dawex, Data Pitch) | Nouveau statut réglementé par le DGA |

### Cas d'usage concrets
1. **Véhicule connecté / données de conduite** : avant le Data Act, les données télématiques d'un véhicule (vitesse, consommation, diagnostics) appartiennent au constructeur. Après le Data Act, le conducteur peut demander à les partager avec son assureur, un garagiste indépendant ou une application tierce — brisant le monopole du constructeur sur ces données.
2. **Machine industrielle (Industrie 4.0)** : un fabricant de machine-outil génère des données de performance et de maintenance. Le Data Act permet à l'acheteur de la machine d'accéder à ces données pour optimiser sa maintenance prédictive, sans dépendre exclusivement du fabricant pour les contrats de service.
3. **Migration cloud** : une entreprise souhaitant quitter AWS pour OVHcloud ne pourra plus se voir facturer des frais de transfert excessifs. AWS devra fournir les outils techniques pour exporter toutes les données et configurations dans un format interopérable.

### Chiffres et tendances
- Les frais de sortie cloud (egress fees) représentaient en moyenne 8-15 % du budget cloud des entreprises avant le Data Act (CISPE, 2022).
- CISPE (Cloud Infrastructure Services Providers in Europe) a signé un code de conduite en 2022 anticipant les exigences du Data Act sur la portabilité.
- L'IDSA recense plus de 140 organisations membres dans 23 pays impliquées dans le développement de standards d'échange de données conformes.
- Gaia-X compte plus de 350 membres en Europe (2024) et développe des cas d'usage sectoriels (santé, mobilité, agriculture, industrie).

## Flashcards
#flashcards/Cloud_et_Virtualisation/Data_Act #flashcards/Big_DATA/Data_Act
- Qu'est-ce que le Data Act et quand est-il applicable ? :: C'est un règlement européen (UE 2023/2854) entré en vigueur le 11 janvier 2024, applicable à partir du 12 septembre 2025, qui régit l'accès et le partage des données des produits connectés (IoT) et impose la portabilité aux fournisseurs cloud.
- Quelle est la différence entre le Data Act et le Data Governance Act ? :: Le Data Governance Act (sept. 2023) encadre les mécanismes de partage volontaire et les intermédiaires de données ; le Data Act (sept. 2025) impose des droits d'accès aux données IoT et la portabilité cloud.
- Qu'est-ce que le B2G data sharing dans le Data Act ? :: La possibilité pour les autorités publiques d'accéder, en cas de nécessité (crise, catastrophe), aux données détenues par des entreprises privées dans l'intérêt général.
- Que sont les intermédiaires de données selon le Data Governance Act ? :: Des entités réglementées qui facilitent le partage de données entre acteurs sans pouvoir utiliser elles-mêmes les données (principe de neutralité). Exemples : Dawex, Data Pitch.
- Comment le Data Act combat-il le vendor lock-in cloud ? :: Il oblige les fournisseurs cloud à supprimer progressivement les frais de migration et à garantir la portabilité technique des données et services, jusqu'à leur suppression totale en 2027.
- Qu'est-ce que Gaia-X et quel est son lien avec le Data Act ? :: Gaia-X est une initiative européenne (350+ membres) visant à créer une infrastructure de données souveraine et interopérable en Europe, dont les travaux s'appuient sur les cadres réglementaires DGA et Data Act.
- Qu'est-ce que l'altruisme des données selon le DGA ? :: Un cadre légal permettant à des personnes ou entreprises de partager volontairement leurs données pour l'intérêt général (recherche médicale, bien commun), via des organisations certifiées.

## Sources
- Règlement (UE) 2023/2854 — Data Act : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32023R2854
- Règlement (UE) 2022/868 — Data Governance Act : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R0868
- Commission européenne — Stratégie européenne des données : https://digital-strategy.ec.europa.eu/fr/policies/strategy-data
- CISPE Code of Conduct : https://cispe.cloud/code-of-conduct/
- International Data Spaces Association : https://internationaldataspaces.org/
- Gaia-X : https://gaia-x.eu/

## Notions liées
- [[Certifications et normes cloud]]
- [[Acteurs cloud]]
- [[Data Lifecycle Management]]
- [[NIS2]]
- [[FinOps]]
