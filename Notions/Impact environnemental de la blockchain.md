---
type: notion
thèmes:
  - Blockchain
  - SI et environnement
statut: pas vu
dernière_révision: 
---

# Impact environnemental de la blockchain

## En bref

La blockchain, et Bitcoin en particulier, est régulièrement critiquée pour son empreinte énergétique considérable liée au mécanisme de consensus **Proof of Work (PoW)**. Cette consommation est mesurée et contestée, des initiatives comme le **Bitcoin Mining Council** et le **Crypto Climate Accord** tentant de greenwasher ou de véritablement verdir le secteur. Face aux enjeux climatiques, plusieurs États ont adopté des mesures restrictives (moratoire de New York), tandis que la transition d'Ethereum vers le **Proof of Stake (PoS)** en 2022 a montré qu'une réduction radicale de la consommation était techniquement possible.

---

## Approfondir

### Fonctionnement

**Pourquoi la blockchain consomme-t-elle autant d'énergie ?**

- Le **Proof of Work (PoW)** — mécanisme de consensus de Bitcoin — repose sur une compétition entre mineurs pour résoudre un problème mathématique (hash). Cette course nécessite une puissance de calcul croissante (hashrate) dont la quasi-totalité est dissipée en chaleur.
- La difficulté s'ajuste automatiquement pour maintenir un bloc toutes les ~10 minutes, quelle que soit la puissance déployée — ce qui signifie que plus de mineurs = plus de consommation sans gain de vitesse.
- Le matériel utilisé : des **ASICs** (Application-Specific Integrated Circuits) dédiés au mining, consommant des milliers de watts chacun, regroupés dans des fermes de mining.

**Proof of Stake (PoS) et alternatives** :
- Le PoS remplace la compétition de calcul par un mécanisme de validation par les détenteurs de tokens (validators qui "stakent" des fonds en garantie).
- **The Merge (Ethereum, septembre 2022)** : migration d'Ethereum de PoW vers PoS — réduction de la consommation d'Ethereum d'environ **99,95 %**.
- Autres mécanismes : Proof of History (Solana), Proof of Space (Chia), Delegated PoS (Tron, EOS).

**Mesure de la consommation** :
- **CBECI (Cambridge Bitcoin Electricity Consumption Index)** : outil de référence de l'Université de Cambridge estimant la consommation électrique annuelle de Bitcoin en temps réel.
- Méthodologie : estimation basse (mineurs les plus efficaces), haute (matériel le plus énergivore) et valeur centrale.
- Également suivi : l'empreinte carbone (dépend du mix électrique des pays mineurs).

**Green Mining et initiatives sectorielles** :
- **Bitcoin Mining Council (BMC)** : coalition de mineurs créée en 2021 (sur initiative d'Elon Musk et Michael Saylor). Publie trimestriellement des données sur le mix énergétique de ses membres. Controversé : accusations de greenwashing et faible représentativité.
- **Crypto Climate Accord (CCA)** : inspiré de l'Accord de Paris, initiative visant à décarboner l'industrie crypto d'ici 2030 (100 % énergies renouvelables) et net zéro d'ici 2040.
- **Green mining** : installation de fermes de mining à proximité de sources d'énergie renouvelable excédentaire (barrages en Islande, géothermie, énergie éolienne curtailée).
- Récupération de chaleur : utilisation de la chaleur des ASICs pour chauffer des bâtiments ou des serres (projets en Suède, France — Qarnot Computing).

**Réponses réglementaires** :
- **Moratoire de New York (2022)** : l'État de New York a adopté une loi imposant un moratoire de 2 ans sur l'installation de nouvelles fermes de mining PoW alimentées par des énergies fossiles — première restriction legislative de ce type aux États-Unis.
- **Proposition de ban UE (2022)** : la proposition d'interdire le PoW dans l'UE (portée par des parlementaires européens) a été rejetée lors du vote du règlement MiCA, mais la Commission doit réévaluer en 2025.
- La Chine a interdit le mining en 2021, entraînant une migration massive vers les États-Unis, Kazakhstan et Russie.

### Avantages / Inconvénients

| Arguments pour (nuances) | Arguments contre |
|---|---|
| Mix énergétique renouvelable croissant (BMC estime ~60 % pour ses membres) | Consommation absolue comparable à certains pays (Pays-Bas, Argentine) |
| Valorisation d'énergies fatales/excédentaires non commercialisables | Bilan carbone variable et difficile à auditer |
| Comparaison : le secteur bancaire traditionnel consomme aussi massivement | Stimule la construction de centrales fossiles dans certains pays |
| Incitation à développer les renouvelables (mining comme acheteur de dernier recours) | E-déchets : les ASICs deviennent obsolètes rapidement (durée de vie ~18 mois) |
| Preuve de Stake réduit la conso de 99,95 % (Ethereum) | Impact eau pour le refroidissement des datacenters de mining |
| Projets concrets de récupération de chaleur | Opacité des données réelles des mineurs (BMC = auto-déclaratif) |

### Acteurs

- **Cambridge Centre for Alternative Finance (CCAF)** : publie le CBECI
- **Bitcoin Mining Council (BMC)** : coalition de mineurs (Marathon Digital, Riot Platforms, MicroStrategy…)
- **Crypto Climate Accord** : initiative de décarbonation (soutenu par Rocky Mountain Institute)
- **Greenpeace / Sierra Club** : campagne "Change the Code, Not the Climate" pour changer Bitcoin vers PoS
- **État de New York** : premier moratoire légal sur le mining PoW fossile
- **Ethereum Foundation** : The Merge — migration réussie vers PoS en 2022
- **Qarnot Computing (France)** : valorisation de la chaleur de serveurs/mining pour le chauffage

### Cas d'usage / exemples concrets

- **Iceland** : fermes de mining alimentées à 100 % par géothermie et hydroélectrique — énergie verte et abondante.
- **Texas** : mineurs qui s'arrêtent lors des pics de consommation du réseau électrique (demand response) — service de flexibilité pour le grid.
- **Qarnot (France)** : radiateurs-serveurs qui chauffent des appartements grâce à la chaleur des calculs de mining ou de rendu 3D.
- **Chia Network** : mining par Proof of Space (disques durs) — critique : obsolescence accélérée des SSD.
- **El Salvador** : mining par énergie géothermique volcanique (Bitcóin Office).

### Chiffres clés

- Bitcoin consomme environ **120-150 TWh/an** (CBECI 2024), comparable à la consommation de la **Pologne** ou de l'**Argentine**.
- **The Merge (Ethereum, 15 septembre 2022)** : réduction de la consommation d'Ethereum de **~99,95 %** (de ~80 TWh/an à ~0,01 TWh/an).
- Le Bitcoin Mining Council déclare ~**58 % d'énergie durable** pour ses membres (Q3 2024, auto-déclaratif).
- La Chine représentait **~65 % du hashrate** mondial avant le ban de 2021 ; les États-Unis sont devenus le premier pays mineur (>35 % du hashrate).
- Moratoire de New York : adopté en **novembre 2022**, durée 2 ans.
- Les ASICs de dernière génération (Antminer S21) : efficacité de ~**17-20 J/TH** (contre 100+ J/TH pour les modèles de 2016).
- Le secteur bancaire mondial est estimé consommer environ **250 TWh/an** (Digiconomist / Galaxy Digital).

---

## Flashcards
#flashcards/Blockchain/Impact_environnemental_de_la_blockchain #flashcards/SI_et_environnement/Impact_environnemental_de_la_blockchain

Qu'est-ce que le CBECI et à quoi sert-il ? :: Cambridge Bitcoin Electricity Consumption Index — outil de l'Université de Cambridge qui estime en temps réel la consommation électrique annuelle du réseau Bitcoin, en proposant des estimations basse, haute et centrale selon l'efficacité énergétique des mineurs.

Pourquoi le Proof of Work consomme-t-il autant d'énergie ? :: Le PoW repose sur une compétition de calcul entre mineurs pour valider les blocs. La difficulté s'ajuste pour maintenir un rythme constant (1 bloc / 10 min), peu importe la puissance totale déployée — plus de mineurs signifie plus de consommation sans gain de productivité du réseau.

Quelle a été l'impact de "The Merge" sur la consommation d'Ethereum ? :: La migration d'Ethereum du Proof of Work vers le Proof of Stake (The Merge, 15 septembre 2022) a réduit la consommation électrique du réseau d'environ 99,95 %, passant de ~80 TWh/an à moins de 0,1 TWh/an.

Qu'est-ce que le Bitcoin Mining Council et pourquoi est-il controversé ? :: Le BMC est une coalition volontaire de mineurs de Bitcoin créée en 2021, qui publie des données trimestrielles sur le mix énergétique de ses membres. Il est controversé car ses données sont auto-déclaratives, non auditées, et ne représentent qu'une fraction du hashrate mondial — d'où des accusations de greenwashing.

Qu'est-ce que le Crypto Climate Accord ? :: Initiative volontaire inspirée de l'Accord de Paris, visant à décarboner entièrement l'industrie des cryptoactifs d'ici 2030 (100 % énergies renouvelables) et à atteindre la neutralité carbone d'ici 2040. Soutenu par des entreprises du secteur et des ONG environnementales.

En quoi consiste le moratoire de New York sur le mining ? :: Adopté en novembre 2022, cet État américain a imposé un moratoire de 2 ans sur la délivrance de nouveaux permis pour les fermes de mining PoW alimentées par des énergies fossiles, dans l'attente d'une étude d'impact environnemental complète.

Comment le mining peut-il valoriser des énergies renouvelables excédentaires ? :: Les fermes de mining peuvent s'installer à proximité de sources d'énergie renouvelable qui produisent parfois plus que la demande locale (éolien, hydraulique, géothermie). En consommant cet excédent qui serait sinon perdu (curtailment), elles rendent les projets renouvelables plus rentables et réduisent leur propre empreinte carbone.

---

## Sources

- CBECI — Cambridge Centre for Alternative Finance : https://ccaf.io/cbnsi/cbeci
- Bitcoin Mining Council : https://bitcoinminingcouncil.com
- Crypto Climate Accord : https://cryptoclimate.org
- Ethereum — The Merge : https://ethereum.org/en/roadmap/merge/
- Loi de l'État de New York sur le mining (S6486D/A7389C, 2022)
- Digiconomist — Bitcoin Energy Consumption : https://digiconomist.net

---

## Notions liées

- [[Cadre réglementaire environnemental du SI]]
- [[Indicateurs environnementaux du SI]]
- [[Écoconception logicielle]]
- [[Sobriété numérique]]
- [[Cadre juridique crypto et blockchain]]
- [[Infrastructure des datacenters]]
- [[Refroidissement des datacenters]]
