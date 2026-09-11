---
type: notion
thèmes:
  - Blockchain
statut: pas vu
dernière_révision: null
---

# Blockchain et supply chain

## En bref

La blockchain appliquée à la supply chain permet de créer un registre immuable et partagé de toutes les étapes de la vie d'un produit, de sa production à sa livraison au consommateur. Elle répond à un problème fondamental de la chaîne logistique : la **fragmentation de l'information** entre acteurs multiples (producteurs, transporteurs, douanes, distributeurs). En assurant une **single source of truth** (SSOT), elle renforce la traçabilité, lutte contre la contrefaçon et améliore la gestion des crises (rappels produits).

---

## Approfondir

### Fonctionnement

La traçabilité blockchain en supply chain repose sur :

1. **Enregistrement des événements** : chaque événement de la chaîne (récolte, transformation, expédition, réception, vente) est enregistré comme une transaction dans un bloc.
2. **Identifiants numériques** : chaque lot, palette ou produit est associé à un identifiant unique (QR code, RFID, NFC) qui pointe vers son historique blockchain.
3. **Traçabilité ascendante** : remonter du produit fini vers l'origine (retrouver le champ d'où vient une salade contaminée).
4. **Traçabilité descendante** : partant d'une matière première, identifier tous les produits finis qui en contiennent (utile pour les rappels).
5. **Smart contracts** : automatisation des paiements ou alertes dès qu'une condition est remplie (température dépassée, délai dépassé).
6. **Digital Product Passport (DPP)** : concept européen (règlement Ecodesign for Sustainable Products Regulation – ESPR) d'un passeport numérique accompagnant chaque produit tout au long de son cycle de vie.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Traçabilité de bout en bout infalsifiable | Problème du "garbage in, garbage out" : la blockchain ne vérifie pas la réalité physique des données saisies |
| Réduction du temps de détection lors des rappels produits | Coût d'intégration et de formation élevé pour les PME |
| Lutte contre la contrefaçon (luxe, médicaments) | Nécessite l'adhésion de tous les acteurs de la chaîne |
| Automatisation via smart contracts (paiements, alertes) | Problèmes d'interopérabilité entre systèmes ERP existants |
| Confiance accrue des consommateurs | Scalabilité et performance des blockchains publiques |
| Réduction des fraudes documentaires | Gouvernance complexe dans les consortiums |

### Acteurs

- **IBM Food Trust** (réseau Hyperledger Fabric) : utilisé par Walmart, Carrefour, Nestlé — traçabilité alimentaire
- **TradeLens** (IBM + Maersk) : traçabilité fret maritime — arrêté en 2022 faute d'adoption suffisante
- **Everledger** : traçabilité des diamants, vins, batteries
- **Aura Blockchain Consortium** : luxe (LVMH, Prada, Cartier) — authentification des produits
- **GS1** : organisme international de standardisation des identifiants produits (codes EAN, EPCIS)
- **Carrefour** : pionnier de la filière blockchain alimentaire en France (poulets, œufs, saumons)
- **De Beers** (Tracr) : traçabilité des diamants bruts
- **Minviro / OriginTrail** : traçabilité des matières premières critiques pour la transition énergétique

### Cas d'usage

- **Alimentaire** : traçabilité du champ à l'assiette — Walmart a réduit de 7 jours à 2,2 secondes le temps pour retrouver l'origine d'une mangue.
- **Pharmaceutique** : lutte contre les médicaments contrefaits (Drug Supply Chain Security Act aux États-Unis).
- **Luxe** : certificats d'authenticité infalsifiables pour sacs, montres, bijoux.
- **Automobile** : traçabilité des batteries de véhicules électriques (future obligation réglementaire UE — Battery Passport).
- **Textile** : prouver l'origine éthique et la durabilité des vêtements.
- **Commerce international** : dématérialisation des lettres de crédit et des documents douaniers.

### Chiffres clés

- Walmart : temps de traçabilité réduit de **7 jours à 2,2 secondes** grâce à IBM Food Trust.
- Le marché de la blockchain dans la supply chain est estimé à **9,9 Md$** en 2030 (MarketsandMarkets).
- Les fraudes alimentaires coûtent environ **40 Md$** par an dans le monde.
- Le règlement européen ESPR impose le **Digital Product Passport** pour plusieurs catégories de produits à partir de 2027.
- TradeLens a traité plus de **300 millions d'événements** avant sa fermeture en 2022.
- L'Union Européenne impose la traçabilité des batteries via le **Battery Passport** dès 2027 (règlement UE 2023/1542).

---

## Flashcards
#flashcards

Qu'est-ce que la traçabilité ascendante en supply chain ? :: La capacité à remonter d'un produit fini vers son origine (matières premières, fournisseurs, lots), par exemple pour identifier la source d'une contamination alimentaire.

Qu'est-ce qu'une "single source of truth" dans le contexte blockchain ? :: Un registre unique, partagé et immuable auquel tous les acteurs d'une chaîne logistique accèdent, éliminant les divergences entre systèmes d'information hétérogènes.

Quel est le principal problème ("garbage in, garbage out") de la blockchain en supply chain ? :: La blockchain garantit l'intégrité des données enregistrées, mais ne peut pas vérifier que ces données reflètent fidèlement la réalité physique. Si un acteur saisit de fausses informations, elles seront "certifiées" à tort.

Qu'est-ce que le Digital Product Passport (DPP) ? :: Un passeport numérique prévu par le règlement européen ESPR (Ecodesign for Sustainable Products Regulation) qui devra accompagner chaque produit tout au long de son cycle de vie, contenant données de durabilité, de réparabilité et de traçabilité.

Pourquoi TradeLens a-t-il échoué malgré son ambition ? :: Malgré le soutien d'IBM et Maersk, TradeLens n'a pas réussi à convaincre suffisamment d'acteurs du secteur maritime de rejoindre le consortium, illustrant que l'adoption collective est le principal défi des plateformes blockchain B2B.

Quel standard GS1 est utilisé pour la traçabilité des événements produits ? :: EPCIS (Electronic Product Code Information Services), un standard GS1 qui décrit les événements de traçabilité (quoi, où, quand, pourquoi) associés à des identifiants EPC.

En combien de temps Walmart peut-il désormais retracer l'origine d'une mangue grâce à IBM Food Trust ? :: En 2,2 secondes, contre 7 jours auparavant avec les méthodes traditionnelles basées sur des documents papier.

---

## Sources

- IBM Food Trust : https://www.ibm.com/fr-fr/products/supply-chain-intelligence-suite/food-trust
- Règlement européen ESPR (Digital Product Passport) : https://ec.europa.eu/
- GS1 EPCIS standard : https://www.gs1.org/standards/epcis
- Gartner — Blockchain in Supply Chain reports
- Carrefour filière qualité blockchain : https://www.carrefour.com/fr/groupe/food-transition/blockchain

---

## Notions liées

- [[RFID - NFC et IoT pour la traçabilité]]
- [[Interopérabilité blockchain]]
- [[Cadre juridique crypto et blockchain]]
- [[Digital Twin]]
- [[Industrie 4.0 et XR]]
