---
type: notion
thèmes:
  - Mobilité
statut: pas vu
dernière_révision: 
---

# Politiques de terminaux (BYOD - COPE)

## En bref
> **Définition** : Les politiques de terminaux définissent qui possède et qui contrôle les appareils utilisés par les collaborateurs dans le cadre professionnel. Elles se déclinent en plusieurs modèles : BYOD (l'employé apporte son propre appareil), COPE (l'entreprise fournit l'appareil mais l'employé peut l'utiliser à titre personnel), COBO, CYOD et COSU. Chaque modèle implique un niveau de contrôle, de responsabilité et de contraintes juridiques différents.
> **Pourquoi c'est important** : Le choix du modèle de terminal conditionne la politique de sécurité, les obligations légales (RGPD, droit à la vie privée), les coûts IT et l'expérience collaborateur. La DSI doit trouver l'équilibre entre contrôle des données d'entreprise et respect de la vie privée, notamment encadré par la charte informatique.
> **Chiffres clés** :
> - **82 % des entreprises** permettent à leurs employés d'accéder aux ressources professionnelles depuis leurs appareils personnels (Syntec Numérique, 2023)
> - Le BYOD peut générer **jusqu'à 1 300 € d'économies par an et par employé** sur les coûts de terminal (Cisco, 2012 — chiffre fondateur, toujours cité)
> - **38 % des entreprises** ayant adopté le BYOD ont subi une violation de données liée à des appareils personnels (IBM Security, 2022)

## Approfondir

### Fonctionnement

**BYOD — Bring Your Own Device**
L'employé utilise son propre terminal (smartphone, PC, tablette) pour accéder aux ressources de l'entreprise. L'entreprise ne possède pas l'appareil mais peut installer un profil de gestion (MDM/MAM) dans un container cloisonné. Le wipe sélectif est indispensable pour ne supprimer que les données pro en cas de départ.

- Avantage utilisateur : confort d'utilisation de son propre appareil
- Risque DSI : surface d'attaque élargie, contrôle limité de l'OS et des mises à jour
- Enjeu juridique : l'employeur doit respecter la vie privée, seul le container pro peut être contrôlé

**COPE — Corporate-Owned, Personally Enabled**
L'entreprise achète et gère l'appareil, mais autorise l'employé à l'utiliser à titre personnel (réseaux sociaux, apps personnelles). La DSI maintient un contrôle total sur la couche professionnelle.

- Compromis équilibré : contrôle total de l'appareil + satisfaction utilisateur
- Coût plus élevé que le BYOD (achat du matériel par l'entreprise)
- Modèle le plus répandu dans les grandes entreprises françaises

**COBO — Corporate-Owned, Business Only**
Appareil propriété de l'entreprise, réservé exclusivement à un usage professionnel. Aucune application personnelle n'est autorisée.

- Contrôle maximal de la DSI
- Résistance des utilisateurs (obligation de porter deux téléphones)
- Utilisé dans les secteurs très réglementés (défense, banque, santé)

**CYOD — Choose Your Own Device**
L'entreprise propose un catalogue d'appareils homologués parmi lesquels l'employé choisit. L'entreprise achète et gère l'appareil.

- Liberté de choix limitée mais contrôle DSI préservé
- Simplifie le support IT (parc homogène)

**COSU — Corporate-Owned, Single Use**
Appareils dédiés à un seul usage (tablette de caisse, terminal logistique, borne interactive). Verrouillés en mode kiosque, ils n'exécutent qu'une seule application.

- Usage : retail, logistique, santé, industrie
- Géré en mode kiosque via MDM

**La charte informatique**
Document contractuel qui définit les règles d'utilisation du système d'information et des terminaux. Elle doit :
- Être annexée au règlement intérieur pour avoir une valeur contraignante (Cour de cassation, 2010)
- Préciser les droits et obligations de l'utilisateur
- Mentionner les moyens de contrôle et de surveillance mis en place
- Être connue et signée par le collaborateur
- En BYOD : définir la frontière entre sphère pro et sphère personnelle

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| **BYOD** : économies sur le matériel, satisfaction utilisateur | Risque sécuritaire élevé, fragmentation des OS |
| **COPE** : contrôle IT + confort utilisateur | Coût d'achat du matériel pour l'entreprise |
| **COBO** : sécurité maximale, contrôle total | Mécontentement utilisateur (double téléphone) |
| **CYOD** : parc homogène, support simplifié | Liberté de choix restreinte |
| **COSU** : parfait pour les usages dédiés | Aucune flexibilité d'usage |

### Acteurs et solutions du marché

Les politiques de terminaux s'implémentent via des solutions UEM/MDM :

- **Microsoft Intune** : gère tous les modèles (BYOD via MAM sans enrôlement, COPE, COBO)
- **VMware Workspace ONE** : fort sur le COPE et les flottes d'entreprise
- **Jamf** : référence Apple pour les politiques BYOD et COPE sur iPhone/Mac
- **SOTI** : spécialiste COSU pour la logistique et l'industrie
- **Preuve de conformité** : les solutions BYOD modernes proposent une attestation de conformité de l'appareil (OS à jour, chiffrement actif) avant d'accorder l'accès aux ressources

### Cas d'usage concrets

**1. Cabinet de conseil en BYOD**
Un cabinet de conseil de 500 personnes adopte le BYOD pour éviter les coûts de terminal. Microsoft Intune déploie un profil MAM sans enrôlement sur les smartphones personnels des consultants : les applications Office 365 sont encapsulées dans un container chiffré. En cas de départ, l'accès aux données pro est révoqué sans wipe de l'appareil personnel. La charte informatique précise les obligations de l'employé (mise à jour OS, code PIN).

**2. Banque en COBO**
Une banque d'investissement impose le COBO à ses traders et gérants de portefeuille pour se conformer aux réglementations MIF II (traçabilité des communications). Les smartphones fournis par la banque sont intégralement contrôlés, les communications sont archivées, et aucune application personnelle n'est installable.

**3. Enseigne de grande distribution en COSU**
2 000 tablettes Android verrouillées en mode kiosque sont déployées sur les caisses et rayons. Le MDM bloque tout usage autre que l'application de caisse, assure les mises à jour silencieuses et peut redémarrer à distance les appareils défaillants.

### Chiffres et tendances

- **BYOD** représente le modèle dominant dans les PME françaises, notamment depuis la généralisation du télétravail post-Covid
- **COPE** est le modèle de référence dans les grandes entreprises du CAC 40 et du secteur bancaire
- La CNIL a publié des recommandations spécifiques sur le BYOD : l'employeur ne peut accéder aux données personnelles présentes sur l'appareil
- Tendance 2024-2025 : convergence vers le **COPE léger** — l'entreprise achète des terminaux reconditionnés pour réduire les coûts tout en maintenant le contrôle

## Flashcards
#flashcards

Quelle est la différence entre BYOD et COPE ? :: En BYOD, l'employé utilise son propre terminal à des fins professionnelles ; en COPE, l'entreprise fournit le terminal mais autorise un usage personnel. Le COPE offre un meilleur contrôle IT tout en préservant le confort de l'utilisateur.

Qu'est-ce que le COSU et dans quel secteur est-il utilisé ? :: Le COSU (Corporate-Owned, Single Use) désigne des appareils d'entreprise dédiés à un seul usage, verrouillés en mode kiosque. Il est utilisé dans le retail (tablettes de caisse), la logistique (terminaux de scan) et la santé (bornes de pointage).

Pourquoi la charte informatique doit-elle être annexée au règlement intérieur ? :: Pour avoir une valeur contraignante, opposable aux salariés et utilisable comme base disciplinaire. Sans cette formalité, la Cour de cassation a estimé que la charte n'est qu'un document de recommandation sans portée juridique.

Quel mécanisme technique est indispensable en BYOD pour protéger la vie privée du collaborateur ? :: Le wipe sélectif, qui permet de supprimer uniquement les données et applications professionnelles du container, sans effacer les données personnelles de l'utilisateur.

Qu'est-ce que le CYOD ? :: Le CYOD (Choose Your Own Device) permet à l'employé de choisir son terminal parmi un catalogue d'appareils homologués et achetés par l'entreprise. Il combine la liberté de choix de l'utilisateur et le contrôle du parc par la DSI.

Quels sont les principaux risques juridiques liés au BYOD ? :: Risque RGPD si l'employeur accède aux données personnelles ; difficulté à prouver la responsabilité en cas d'incident ; impossibilité d'imposer certaines contraintes (mise à jour OS) sur un appareil personnel sans base légale.

## Sources

- CNIL, "Le BYOD et les risques en matière de protection des données", cnil.fr
- Syntec Numérique, Baromètre du numérique, 2023
- IBM Security, "Cost of a Data Breach Report", 2022
- Cour de cassation, chambre sociale, arrêt du 17 mai 2005 (charte informatique)
- Microsoft Intune documentation — learn.microsoft.com/intune
- Gartner, "Magic Quadrant for Unified Endpoint Management", 2023

## Notions liées
- [[Gestion de la mobilité (UEM)]]
- [[RGPD]]
- [[Télétravail et travail hybride]]
- [[Zero Trust]]
- [[VPN et accès distant]]
- [[Digital Workplace]]
