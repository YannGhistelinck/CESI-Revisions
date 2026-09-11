---
type: notion
thèmes:
  - Blockchain
  - Développement
statut: pas vu
dernière_révision: null
---

# RFID - NFC et IoT pour la traçabilité

## En bref

RFID (Radio Frequency Identification) et NFC (Near Field Communication) sont des technologies d'identification sans contact qui permettent de capturer automatiquement des données sur des objets physiques et de les injecter dans des systèmes d'information. Couplées à l'IoT industriel (IIoT) et à la blockchain, elles forment la couche de **collecte de données physiques** indispensable à toute traçabilité fiable. Elles transforment des objets du monde réel en entités numériques traçables en temps réel.

---

## Approfondir

### Fonctionnement

**RFID** :
- Un tag RFID (passif ou actif) est apposé sur un objet. Il contient une puce et une antenne.
- Un lecteur RFID émet une onde radio qui alimente le tag (passif) et déclenche la transmission de son identifiant unique (EPC — Electronic Product Code).
- Portée : quelques centimètres à plusieurs mètres selon la fréquence (LF, HF, UHF).
- Avantage majeur : lecture en masse sans ligne de vue (lecture simultanée de centaines de tags).

**NFC** :
- Sous-ensemble du RFID (fréquence HF, 13,56 MHz), portée très courte (< 10 cm).
- Protocoles : ISO/IEC 14443, ISO/IEC 15693.
- Utilisé pour les paiements sans contact, les badges d'accès, mais aussi l'authentification produits (tags NFC dans les vêtements, bouteilles de vin, médicaments).

**IoT industriel (IIoT) et capteurs** :
- Capteurs de température, d'humidité, de chocs, de géolocalisation (GPS) intégrés dans les emballages ou palettes.
- Transmission des données via protocoles IoT : MQTT, CoAP, LoRaWAN (longue portée, faible consommation), NB-IoT.
- Edge computing : traitement local des données avant envoi vers le cloud ou la blockchain.

**Articulation avec la blockchain** :
- Les données captées par RFID/NFC/capteurs sont horodatées et enregistrées sur la blockchain via des oracles IoT ou des gateways.
- Le standard **GS1 EPCIS 2.0** structure les événements de traçabilité (quoi, où, quand, pourquoi) avant leur inscription on-chain.
- La blockchain garantit l'intégrité et l'immuabilité des données collectées (mais pas leur véracité physique initiale).

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Lecture automatique et en masse (pas de code-barres à scanner un par un) | Coût des tags RFID actifs (batterie) plus élevé |
| Intégration temps réel dans les systèmes ERP/WMS | Interférences (eau, métal perturbent certaines fréquences) |
| Réduction des erreurs de saisie manuelle | Problèmes de vie privée (traçage des porteurs) |
| Couplage avec blockchain pour immuabilité | "Garbage in, garbage out" : tag falsifié = données fausses |
| Traçabilité en temps réel (capteurs IoT) | Standardisation encore incomplète entre écosystèmes |
| Tags NFC : interaction directe avec le consommateur (smartphone) | Infrastructure réseau IoT nécessaire (déploiement coûteux) |

### Acteurs

- **GS1** : organisme mondial de standardisation (EPC, EPCIS, GS1 Digital Link)
- **Impinj** : leader mondial des puces RFID UHF
- **Zebra Technologies** : lecteurs et solutions RFID industrielles
- **HID Global** : tags et systèmes d'identification
- **NXP Semiconductors** : puces NFC (NTAG, MIFARE)
- **Sigfox / Semtech (LoRa)** : réseaux LPWAN pour IoT longue portée
- **Auchan, Decathlon** : déploiements RFID massifs en retail
- **AWS IoT / Azure IoT Hub / Google Cloud IoT** : plateformes cloud IoT

### Cas d'usage

- **Logistique** : suivi automatique des palettes et colis en entrepôt — Decathlon a équipé 100 % de ses articles en RFID.
- **Agroalimentaire** : capteurs de température dans les camions frigorifiques (chaîne du froid) — données enregistrées sur blockchain pour conformité réglementaire.
- **Luxe / Authenticité** : tag NFC cousu dans un sac Hermès ou une sneaker pour certifier l'authenticité au consommateur via smartphone.
- **Pharmaceutique** : traçabilité des médicaments (sérialisation obligatoire en UE — directive falsified medicines).
- **Industrie** : suivi des outils et équipements en atelier (maintenance préventive, inventaire).
- **Recyclage** : tag RFID dans les emballages pour triage automatique en filière de recyclage (Digital Product Passport).

### Chiffres clés

- Le marché RFID mondial est estimé à **35 Md$** en 2030 (Grand View Research).
- Decathlon : **1,5 milliard** de tags RFID utilisés par an, inventaires réalisés en quelques minutes au lieu de plusieurs jours.
- La directive européenne sur les médicaments falsifiés (FMD) impose la **sérialisation à 100 %** des médicaments depuis 2019.
- Le standard EPCIS 2.0 a été publié par GS1 en **2022** avec support natif du JSON-LD et des Web APIs.
- Un tag RFID passif coûte entre **0,05 € et 0,50 €** selon la technologie et les volumes.
- Le marché IIoT est estimé à **1 100 Md$** en 2028 (Fortune Business Insights).

---

## Flashcards
#flashcards

Quelle est la différence entre RFID et NFC ? :: Le NFC est un sous-ensemble du RFID, limité à une portée de moins de 10 cm et à la fréquence 13,56 MHz (HF). Le RFID couvre un spectre plus large de fréquences (LF, HF, UHF) et des portées allant jusqu'à plusieurs mètres.

Qu'est-ce que le standard GS1 EPCIS ? :: Electronic Product Code Information Services — un standard GS1 qui définit la structure des événements de traçabilité (quoi = quels produits, où = localisation, quand = horodatage, pourquoi = raison de l'événement) échangés entre systèmes d'information.

Quel est le rôle d'un oracle IoT dans une architecture blockchain de traçabilité ? :: L'oracle IoT est un intermédiaire qui capture les données du monde physique (capteurs, RFID) et les soumet à la blockchain de manière fiable, résolvant le problème de connexion entre le monde physique et le registre distribué.

Pourquoi le RFID passif est-il préféré à l'actif dans le retail ? :: Le tag RFID passif ne nécessite pas de batterie (il est alimenté par l'onde du lecteur), ce qui le rend moins coûteux (0,05–0,50 €), plus léger et avec une durée de vie quasi illimitée — adapté aux articles de grande consommation.

Qu'est-ce que le protocole LoRaWAN et pourquoi est-il adapté à l'IoT de traçabilité ? :: LoRa Wide Area Network est un protocole de réseau sans fil longue portée (jusqu'à 15 km en zone rurale) à très faible consommation énergétique, idéal pour des capteurs de traçabilité déployés sur de grandes zones (champs, entrepôts) sans accès à l'électricité.

Qu'est-ce que la sérialisation dans la chaîne pharmaceutique ? :: L'attribution d'un identifiant unique à chaque unité de médicament (boîte), permettant de vérifier son authenticité à chaque étape jusqu'au patient — obligation réglementaire en Europe depuis 2019 (FMD).

Quel déploiement RFID Decathlon a-t-il réalisé ? :: Decathlon a équipé 100 % de ses articles de tags RFID, utilisant 1,5 milliard de tags par an. Cela permet des inventaires complets en quelques minutes (contre plusieurs jours auparavant) et une disponibilité produit améliorée.

---

## Sources

- GS1 EPCIS 2.0 : https://www.gs1.org/standards/epcis
- Decathlon RFID : https://www.decathlon.fr
- Directive médicaments falsifiés (FMD) UE 2011/62/CE
- LoRa Alliance : https://lora-alliance.org
- NXP — NFC standards : https://www.nxp.com/nfc

---

## Notions liées

- [[Blockchain et supply chain]]
- [[Industrie 4.0 et XR]]
- [[Digital Twin]]
- [[Edge Computing]]
- [[Identité décentralisée (SSI)]]
