---
type: notion
thèmes:
  - Cybersécurité
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Cyber-résilience

## En bref
> **Définition** : La cyber-résilience désigne la capacité d'une organisation à préparer, résister, s'adapter et se remettre d'une cyberattaque, tout en maintenant la continuité de ses activités métier. Elle dépasse la simple défense technique : c'est une posture stratégique qui intègre la certitude que l'attaque aura lieu.
> **Pourquoi c'est important** : Dans un contexte où les ransomwares paralysent des hôpitaux et des industries entières, il ne s'agit plus de savoir "si" une organisation sera attaquée, mais "quand". La DSI doit construire un SI capable de survivre à une attaque et de redémarrer rapidement pour limiter l'impact opérationnel et financier.
> **Chiffres clés** :
> - Le délai moyen de reprise après un ransomware est de 21 jours (Coveware Q4 2023).
> - 93 % des entreprises qui perdent l'accès à leurs données pendant 10 jours ou plus font faillite dans l'année (National Archives & Records Administration, USA).
> - Le coût moyen d'une attaque ransomware (rançon + récupération + perte de CA) dépasse 1,8 M$ en 2023 (Sophos State of Ransomware 2023).

## Approfondir

### Fonctionnement

**Assume Breach (postulat de compromission)** : philosophie de sécurité qui consiste à concevoir l'architecture et les processus en partant du principe que l'attaquant est déjà présent dans le SI. Cela conduit à : micro-segmentation, surveillance interne intensive, plans de réponse activables immédiatement, exercices de simulation (red team, purple team).

**Kill Chain (Cyber Kill Chain, Lockheed Martin, 2011)** : modèle décrivant les 7 étapes d'une attaque cyber :
1. Reconnaissance
2. Armement (weaponization)
3. Livraison (delivery)
4. Exploitation
5. Installation
6. Commande & Contrôle (C2)
7. Actions sur l'objectif (exfiltration, chiffrement)
Utilisé pour identifier à quelle étape une attaque peut être interrompue et pour aligner les défenses sur chaque phase.

**Règle de sauvegarde 3-2-1** : standard fondamental des sauvegardes :
- 3 copies des données
- sur 2 supports différents (ex. : disque et bande)
- dont 1 copie hors site (offsite)
Étendue en 3-2-1-1-0 : + 1 copie hors ligne (offline/air gap) + 0 erreur vérifiée lors de la restauration.

**Sauvegardes immuables (WORM)** : sauvegardes en mode Write Once, Read Many — impossibles à modifier ou supprimer pendant une période définie, même par un administrateur avec des droits élevés ou un ransomware ayant compromis le compte admin. Technologie : Object Lock S3 (AWS), Azure Immutable Blob Storage, Veeam avec hardened repository.

**Air Gap** : isolation physique ou logique complète d'une copie de sauvegarde du réseau de production. Une sauvegarde air-gappée est inaccessible depuis le réseau et donc immunisée contre le ransomware. Peut être physique (bande magnétique en coffre) ou logique (réseau isolé sans connexion permanente).

**Cyber Recovery Vault** : environnement de récupération isolé, fortifié et déconnecté du réseau de production. Contient une copie propre des données critiques et des outils de restauration. Activé uniquement en cas de crise majeure. Exemples commerciaux : Dell EMC Cyber Recovery Vault, Pure Storage SafeMode.

**PRA / PCA (Plan de Reprise / Continuité d'Activité)** : le PRA définit les procédures pour reprendre les activités après un sinistre (RTO/RPO). Le PCA garantit la continuité pendant l'incident. Doivent être testés régulièrement (exercices, simulations).

**RTO (Recovery Time Objective)** : temps maximum acceptable avant que les systèmes soient restaurés après un incident.
**RPO (Recovery Point Objective)** : perte de données maximale acceptable, exprimée en durée (ex. : 4 heures = on peut perdre jusqu'à 4h de données).

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Continuité d'activité même en cas d'attaque réussie | Coût d'infrastructure de sauvegarde redondante |
| Réduction du RTO/RPO = perte réduite | Complexité des tests et de la validation régulière |
| Posture proactive ("assume breach") | Nécessite une gouvernance et des processus matures |
| Conformité réglementaire (NIS2, DORA) | Les sauvegardes air-gappées ralentissent la récupération |
| Réduction de l'incitation à payer la rançon | Difficulté d'aligner les métiers sur les exercices de crise |

### Acteurs et solutions du marché

**Sauvegarde et récupération** : Veeam (leader), Zerto, Commvault, Cohesity, Rubrik (spécialiste cyber recovery).

**Immutable storage** : AWS S3 Object Lock, Azure Immutable Blob, NetApp SnapLock, Pure Storage SafeMode.

**Cyber Recovery Vault** : Dell EMC Cyber Recovery, IBM Safeguarded Copy, Rubrik Security Cloud.

**Gestion de crise et PRA** : Everbridge, OnSolve, xMatters.

**Simulation et exercices** : services de red team / purple team (Wavestone, Intrinsec, CLUSIF), plateformes de simulation de crise (Crisis24).

**Référentiels** : ISO 22301 (continuité d'activité), NIST SP 800-34 (PCA/PRA), DORA (Digital Operational Resilience Act, secteur financier, 2025).

### Cas d'usage concrets

1. **CHU de Rouen (2019)** : ransomware ayant paralysé le SI de l'hôpital pendant plusieurs jours. Retour aux processus papier, report d'opérations non urgentes. Aurait pu être limité avec des sauvegardes isolées et un PRA testé.

2. **Maersk — NotPetya (2017)** : le groupe maritime a perdu la quasi-totalité de son SI (45 000 postes, 4 000 serveurs). Récupération en 10 jours grâce à une copie de sauvegarde AD retrouvée par hasard au Ghana (coupure réseau au moment de l'attaque = air gap involontaire). Perte : 300 M$.

3. **Sector financier — DORA (2025)** : le règlement européen DORA impose à toutes les entités financières (banques, assurances, PSFI) de démontrer leur résilience opérationnelle numérique, incluant des tests de pénétration basés sur la menace (TLPT) et des plans de réponse aux incidents testés annuellement.

### Chiffres et tendances
- Sophos (2023) : 46 % des organisations touchées par un ransomware ont payé la rançon, mais seulement 65 % ont récupéré leurs données.
- Gartner prédit que d'ici 2025, 75 % des entreprises auront un programme de cyber-résilience formalisé (contre 15 % en 2021).
- Le marché des solutions de cyber recovery devrait atteindre 21 Md$ en 2028 (MarketsandMarkets).
- DORA est entré en application le 17 janvier 2025 pour les 22 000 entités financières européennes.

## Flashcards
#flashcards
Qu'est-ce que la cyber-résilience ? :: Capacité d'une organisation à préparer, résister, s'adapter et se remettre d'une cyberattaque en maintenant la continuité de ses activités. Posture stratégique basée sur la certitude que l'attaque aura lieu.

Qu'est-ce que le principe "Assume Breach" ? :: Philosophie consistant à concevoir l'architecture et les processus en partant du postulat que l'attaquant est déjà présent dans le SI, afin de préparer des défenses internes et des plans de réponse immédiats.

Décrire la règle de sauvegarde 3-2-1 et son extension. :: 3 copies, sur 2 supports différents, dont 1 hors site. Étendue en 3-2-1-1-0 : + 1 copie hors ligne (air gap) + 0 erreur de restauration vérifiée.

Qu'est-ce qu'une sauvegarde immuable (WORM) ? :: Sauvegarde impossible à modifier ou supprimer pendant une période définie, même par un admin ou un ransomware. Technologie : S3 Object Lock, Azure Immutable Blob, Veeam Hardened Repository.

Qu'est-ce qu'un air gap dans le contexte des sauvegardes ? :: Isolation physique ou logique complète d'une copie de sauvegarde du réseau de production, la rendant inaccessible aux ransomwares qui auraient compromis le réseau.

Quelle est la différence entre RTO et RPO ? :: RTO (Recovery Time Objective) : durée maximale acceptable avant restauration des systèmes. RPO (Recovery Point Objective) : perte de données maximale acceptable, exprimée en durée.

Quelles sont les 7 étapes de la Cyber Kill Chain ? :: 1. Reconnaissance, 2. Armement, 3. Livraison, 4. Exploitation, 5. Installation, 6. Commande & Contrôle (C2), 7. Actions sur l'objectif.

## Sources
- ANSSI — Guide de gestion des crises cyber — www.ssi.gouv.fr
- NIST SP 800-34 — Contingency Planning Guide for Federal Information Systems
- ISO 22301 — Systèmes de management de la continuité d'activité
- Sophos — State of Ransomware 2023 — www.sophos.com
- Coveware — Ransomware Recovery Report Q4 2023 — www.coveware.com
- Règlement DORA (UE) 2022/2554 — eur-lex.europa.eu
- Lockheed Martin — Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns (Kill Chain, 2011)

## Notions liées
- [[Menaces cyber]]
- [[Défense en profondeur]]
- [[Zero Trust]]
- [[SIEM]]
- [[SOAR]]
- [[EDR - XDR - NDR]]
