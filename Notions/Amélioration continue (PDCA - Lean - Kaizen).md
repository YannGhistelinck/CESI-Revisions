---
type: notion
thèmes:
  - Optimisation du SI
  - Management et stratégie
statut: pas vu
dernière_révision: 
---

# Amélioration continue (PDCA - Lean - Kaizen)

## En bref

### Définition
L'**amélioration continue** est une philosophie de gestion visant à optimiser de façon itérative et permanente les processus, produits et services d'une organisation. Elle repose sur plusieurs cadres complémentaires :
- **PDCA (Plan-Do-Check-Act)** : cycle de Deming, méthode scientifique d'amélioration en boucle
- **Lean IT** : application des principes lean (Toyota Production System) au SI — éliminer le gaspillage (muda), maximiser la valeur livrée
- **Kaizen** : philosophie japonaise du "changement en mieux", petits pas continus, impliquant tous les acteurs
- **CSI (Continual Service Improvement)** : étape dédiée du cycle de vie ITIL v3, reprise comme pratique dans ITIL 4
- **RCA (Root Cause Analysis)** : méthode d'analyse des causes profondes d'un incident (5 Pourquoi, diagramme d'Ishikawa)
- **Rétrospective agile** : cérémonie Scrum permettant à l'équipe de s'améliorer à chaque sprint

### Pourquoi c'est important
Dans un SI en évolution constante, l'amélioration continue permet d'éviter la dette technique, de réduire les incidents récurrents, d'optimiser les coûts et de maintenir l'alignement entre IT et métier. C'est le fondement de toute démarche qualité durable.

### Chiffres clés
- Toyota a réduit ses défauts de 50 % en 10 ans grâce au Kaizen systématique
- Les équipes pratiquant des rétrospectives régulières livrent 25 % plus rapidement (VersionOne State of Agile)
- ITIL 4 positionne l'amélioration continue comme l'une des 7 pratiques centrales de gestion des services

---

## Approfondir

### Fonctionnement

**Cycle PDCA (Deming) :**
1. **Plan** : identifier le problème, analyser les causes (RCA), définir l'objectif et le plan d'action
2. **Do** : mettre en œuvre le plan à petite échelle (pilote)
3. **Check** : mesurer les résultats vs objectifs (KPI, métriques)
4. **Act** : standardiser si succès / ajuster si échec → relancer un nouveau cycle

**Lean IT — les 7 gaspillages transposés au SI (muda) :**
- Surproduction (fonctionnalités non utilisées)
- Attente (files d'attente de tickets)
- Transports inutiles (transferts de données redondants)
- Sur-traitement (processus bureaucratiques excessifs)
- Stocks (backlog non priorisé)
- Mouvements (interfaces humaines non ergonomiques)
- Défauts (bugs, incidents)

**Kaizen en pratique IT :**
- Kaizen blitz (chantier court de 2-5 jours sur un processus précis)
- Cercles qualité (groupes de travail pluridisciplinaires)
- Suggestion board numérique (idées d'amélioration de toute l'équipe)

**CSI ITIL 4 :**
- S'appuie sur le modèle d'amélioration en 7 étapes : vision → situation actuelle → cible → plan → action → mesure → consolidation
- Intègre les métriques DORA comme indicateurs de performance du delivery

**RCA — méthodes :**
- **5 Pourquoi** : remonter la chaîne causale en posant "pourquoi ?" cinq fois
- **Ishikawa (arête de poisson)** : cartographier les causes par catégories (Méthodes, Matériels, Milieu, Main-d'œuvre, Mesures, Machines)
- **Post-mortem blameless** : culture no-blame pour analyser les incidents sans désigner de coupable

**Rétrospective agile (Scrum) :**
- Format classique : Qu'est-ce qui a bien fonctionné ? Qu'est-ce qui doit changer ? Quelles actions concrètes ?
- Fréquence : à chaque fin de sprint (1 à 4 semaines)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Réduction durable des incidents récurrents | Nécessite un engagement culturel fort et long terme |
| Optimisation des coûts opérationnels | Résistance au changement des équipes |
| Alignement continu IT/métier | Difficile à mesurer sur le court terme |
| Détection précoce des dérives qualité | Risque de "kaizen washing" (démarche superficielle) |
| Capitalisation sur les retours d'expérience | Nécessite des outils de suivi adaptés |

### Acteurs
- **W. Edwards Deming** : père du cycle PDCA
- **Taiichi Ohno** : fondateur du Toyota Production System (lean, kaizen)
- **AXELOS** : éditeur d'ITIL (CSI / amélioration continue)
- **Agile Alliance / Scrum Alliance** : promotion des pratiques agiles incluant les rétrospectives
- **Institut Lean France** : diffusion du lean en France

### Cas d'usage
- **ITSM** : réduction du Mean Time To Repair (MTTR) grâce à des post-mortems et RCA systématiques
- **DevOps** : mesure des métriques DORA (Deployment Frequency, Lead Time) pour piloter l'amélioration du pipeline CI/CD
- **Centre de services** : application du PDCA pour réduire le backlog de tickets de niveau 1
- **Projet agile** : rétrospective après chaque sprint pour améliorer la vélocité de l'équipe

### Chiffres complémentaires
- Les entreprises lean réduisent leurs délais de livraison de 50 % en moyenne (Lean Enterprise Institute)
- Le MTTR moyen des équipes pratiquant le post-mortem blameless est 30 % inférieur (DORA Report 2023)

---

## Flashcards
#flashcards

Que signifient les 4 étapes du cycle PDCA ? :: Plan (planifier), Do (faire), Check (vérifier), Act (agir/standardiser) — cycle de Deming d'amélioration continue.

Qu'est-ce que le Kaizen ? :: Philosophie japonaise du "changement en mieux" : amélioration continue par petits pas, impliquant tous les collaborateurs.

Citez les 7 types de gaspillages (muda) transposés au Lean IT. :: Surproduction, attente, transports inutiles, sur-traitement, stocks, mouvements inutiles, défauts.

Qu'est-ce que la RCA (Root Cause Analysis) et quelles sont ses méthodes principales ? :: Analyse des causes profondes d'un incident ; méthodes : 5 Pourquoi, diagramme d'Ishikawa, post-mortem blameless.

Comment le CSI s'intègre-t-il dans ITIL 4 ? :: C'est une pratique centrale en 7 étapes (vision → situation → cible → plan → action → mesure → consolidation) qui garantit l'amélioration permanente des services.

Quel est l'objectif d'une rétrospective agile ? :: Identifier ce qui a bien fonctionné, ce qui doit changer, et définir des actions concrètes d'amélioration pour le prochain sprint.

Quelle différence entre PDCA et Kaizen ? :: Le PDCA est un cycle méthodologique structuré ; le Kaizen est une culture de l'amélioration permanente par petits incréments — les deux sont complémentaires.

---

## Sources
- W. Edwards Deming, *Out of the Crisis*, MIT Press, 1982
- Taiichi Ohno, *Toyota Production System*, Productivity Press, 1988
- AXELOS, *ITIL 4 Foundation*, 2019
- DORA State of DevOps Report, 2023
- Lean Enterprise Institute — leaning.org
- Scrum Guide, Schwaber & Sutherland, 2020

---

## Notions liées
- [[VUCA et benchmark]]
- [[Value Stream Mapping]]
- [[ISO 9001 et qualité]]
- [[DORA Metrics]]
- [[VeriSM]]
- [[Outils ITSM]]
- [[DevOps]]
