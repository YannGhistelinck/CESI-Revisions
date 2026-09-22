---
type: notion
thèmes:
  - Cybersécurité
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Cyber-assurance

![[N — Cyber-assurance.mp3]]
## En bref
> **Définition** : La cyber-assurance (ou assurance cyber-risques) est un contrat d'assurance spécifique couvrant les pertes financières et les frais engagés par une organisation à la suite d'une cyberattaque ou d'un incident de sécurité informatique (ransomware, violation de données, interruption de service, etc.).
> **Pourquoi c'est important** : Face à l'explosion du coût des cyberattaques, la cyber-assurance est devenue un outil stratégique de transfert du risque résiduel. Elle est de plus en plus exigée par les donneurs d'ordre et les régulateurs, et constitue un filet de sécurité financier pour les DSI et RSSI qui ne peuvent éliminer tout risque cyber.
> **Chiffres clés** :
> - Le marché mondial de la cyber-assurance était estimé à 14 Mds $ en 2023, avec une croissance annuelle de 25 % (Munich Re)
> - En France, seulement 13 % des PME disposent d'une cyber-assurance (AMRAE, 2023)
> - Les primes d'assurance cyber ont augmenté de 50 à 100 % entre 2020 et 2022 avant de se stabiliser en 2023-2024

## Approfondir

### Fonctionnement

**Couvertures typiques d'une police cyber :**

- **Pertes propres (first-party) :**
  - Frais de réponse à incident (RSSI externe, forensics, cellule de crise)
  - Pertes d'exploitation liées à l'interruption du SI
  - Frais de restauration des données et des systèmes
  - Rançon payée (selon les polices et les pays)
  - Frais de notification aux personnes concernées (RGPD)
  - Atteinte à la réputation / gestion de crise communication

- **Responsabilité civile (third-party) :**
  - Réclamations de tiers pour violation de données (clients, fournisseurs)
  - Défense juridique et dommages et intérêts
  - Violations de la vie privée

**Exclusions fréquentes :**
- Guerre et cyberguerre (clause de cyber-guerre, très débattue depuis NotPetya/Ukraine)
- Fautes intentionnelles ou négligence grave
- Incidents survenus avant la souscription (vulnérabilités connues non corrigées)
- Pannes matérielles sans origine malveillante
- Infrastructure non déclarée dans le périmètre assuré

**Conditions d'éligibilité et d'audit :**
Les assureurs imposent désormais un niveau minimal de maturité cyber avant d'accorder une couverture :
- MFA (authentification multifacteur) obligatoire, notamment sur les accès distants et les comptes admin
- Sauvegardes régulières, testées, isolées (règle 3-2-1-1)
- Plan de réponse aux incidents documenté et testé
- Patch management à jour (pas de vulnérabilités critiques non corrigées)
- Segmentation réseau
- Formation des utilisateurs à la sensibilisation phishing
- Audit de sécurité récent (pentest, scan de vulnérabilités)

**Processus de souscription :**
1. Questionnaire détaillé sur la maturité cyber de l'organisation
2. Audit technique (parfois scan externe automatisé)
3. Évaluation du profil de risque et tarification
4. Définition des garanties, franchises et plafonds
5. Révision annuelle

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Transfert financier du risque résiduel | Primes élevées et en hausse constante |
| Accès à des experts cyber en cas d'incident | Exclusions nombreuses et interprétation contractuelle difficile |
| Conformité aux exigences des clients/donneurs d'ordre | Risque moral (moindre vigilance si assuré) |
| Prise en charge des frais de notification RGPD | Polices souvent inadaptées aux PME |
| Accompagnement en gestion de crise | Paiement de rançon controversé et parfois illégal |
| Incitation à améliorer la posture cyber | Processus de souscription complexe et chronophage |

### Acteurs et solutions du marché
- **Assureurs spécialisés cyber** : AXA XL, Allianz, Chubb, Beazley, Hiscox, AIG
- **Réassureurs** : Munich Re, Swiss Re (acteurs clés du marché mondial)
- **Courtiers spécialisés** : Marsh, Aon, Willis Towers Watson
- **Association professionnelle** : AMRAE (Association pour le Management des Risques et des Assurances de l'Entreprise) — publie des études de référence sur le marché français
- **Benchmark** : Rapport LUCY (LUmière sur la CYber assurance) publié annuellement par l'AMRAE

### Cas d'usage concrets
1. **Ransomware sur une PME industrielle** : Une PME de 200 salariés subit une attaque ransomware. La cyber-assurance prend en charge : les frais de l'équipe forensics (80 000 €), la perte d'exploitation sur 3 semaines (150 000 €) et la rançon (si couverte). Sans assurance, la PME aurait dû absorber seule ces coûts.
2. **Violation de données chez un prestataire de santé** : Suite à une exfiltration de données de patients, les frais de notification (obligation RGPD), d'assistance juridique et de gestion de crise médiatique sont couverts par la police cyber, évitant une charge financière supplémentaire à la crise opérationnelle.
3. **Litige NotPetya (Merck vs. Ace American)** : Merck a réclamé 1,4 Md $ à son assureur qui invoquait la clause d'acte de guerre (NotPetya étant attribué à la Russie). La Cour suprême du New Jersey a finalement donné raison à Merck en 2023, forçant le secteur à clarifier ses clauses de cyberguerre.

### Chiffres et tendances
- Rapport LUCY 2023 (AMRAE) : les grandes entreprises françaises représentent 74 % du marché cyber français, les ETI 16 %, les PME seulement 10 %
- Sinistralité en hausse : le ratio sinistres/primes a dépassé 100 % en 2020-2021, entraînant une sélection drastique des risques par les assureurs
- Tendance 2024-2025 : stabilisation des primes mais renforcement des exigences minimales de sécurité (MFA, sauvegardes isolées, EDR/XDR obligatoires)
- Le règlement DORA impose aux entités financières de gérer le risque cyber de leurs prestataires, créant de nouvelles obligations d'assurance

## Flashcards
#flashcards/Cybersécurité/Cyber_assurance #flashcards/Management_et_stratégie/Cyber_assurance
Qu'est-ce que la cyber-assurance ? :: Un contrat d'assurance couvrant les pertes financières et frais liés à un incident de sécurité informatique (ransomware, violation de données, interruption de service).

Que couvre une police cyber en first-party ? :: Les pertes directes de l'assuré : frais de réponse à incident, pertes d'exploitation, restauration des données, frais de notification RGPD, gestion de crise.

Quelles sont les 3 conditions d'éligibilité incontournables demandées par les assureurs ? :: MFA sur les accès sensibles, sauvegardes régulières et isolées testées, plan de réponse aux incidents documenté.

Qu'est-ce que la clause de cyberguerre et pourquoi est-elle controversée ? :: Elle exclut les dommages liés à des actes de guerre cyber (attaques étatiques). L'affaire Merck/NotPetya a montré son ambiguïté : les assureurs tentaient d'exclure NotPetya (attribué à la Russie) mais ont été condamnés à indemniser.

Quel est l'organisme de référence sur la cyber-assurance en France ? :: L'AMRAE (Association pour le Management des Risques et des Assurances de l'Entreprise), qui publie annuellement le rapport LUCY sur le marché français.

Quel est le taux de couverture cyber des PME françaises ? :: Environ 13 % des PME françaises disposent d'une cyber-assurance (AMRAE, 2023), ce qui laisse la grande majorité sans couverture face aux cyberattaques.

Qu'est-ce que la règle 3-2-1-1 pour les sauvegardes ? :: 3 copies des données, sur 2 types de supports différents, dont 1 hors site, et 1 copie immuable ou hors ligne (air-gap), pour résister aux ransomwares.

## Sources
- AMRAE — Rapport LUCY 2023 (LUmière sur la CYber assurance)
- Munich Re — Cyber Insurance Market Report 2023
- Hiscox Cyber Readiness Report 2023
- ANSSI — Panorama de la menace informatique 2023
- Décision Merck & Co. v. Ace American Insurance Co. — Cour suprême du New Jersey, 2023
- France Assureurs — Statistiques marché cyber 2023

## Notions liées
- [[PCA - PRA]]
- [[NIS2]]
- [[ISO 27001 - 27002]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[Authentification et gestion des accès (IAM)]]
