---
type: notion
thèmes:
  - Transversal
  - Développement
statut: pas vu
dernière_révision: 
---

![[N — Scrum.mp3]]
## En bref

### Définition
Scrum est un framework agile léger permettant de développer, livrer et soutenir des produits complexes de manière itérative et incrémentale. Il est défini par le **Scrum Guide**, co-écrit par Ken Schwaber et Jeff Sutherland (créateurs), dont la dernière version date de **novembre 2020**. Scrum n'est pas une méthode prescriptive : c'est un cadre délibérément incomplet qui doit être complété par les pratiques de l'équipe.

### Pourquoi c'est important
Scrum est le framework agile le plus utilisé dans le monde. Il permet de livrer de la valeur rapidement, de s'adapter aux changements d'exigences et de réduire les risques par des boucles de feedback courtes. Il est devenu la référence dans le développement logiciel et s'étend à d'autres domaines (marketing, RH, gestion de projet IT non-technique).

### Chiffres clés
- **87 %** des équipes agiles utilisent Scrum ou un dérivé (Scrum.org State of Scrum 2023).
- Un sprint dure généralement **1 à 4 semaines** (2 semaines est la durée la plus répandue).
- Le marché des outils de gestion agile (Jira, Azure DevOps, etc.) est estimé à **8,9 milliards $** en 2024 (Grand View Research).
- Le Scrum Guide 2020 est passé de **19 à 13 pages** — simplification volontaire et réduction du prescriptif.

---

## Approfondir

### Fonctionnement

Scrum repose sur **3 piliers empiriques** : Transparence, Inspection, Adaptation (TIA).

Il intègre **5 valeurs** : Courage, Focus, Engagement, Respect, Ouverture.

---

#### Les 3 rôles (Scrum 2020 : "Accountabilities")

| Rôle | Responsabilités clés |
|---|---|
| **Product Owner (PO)** | Maximise la valeur du produit. Seul responsable du Product Backlog : il le crée, l'ordonne, le clarifie. Représente les parties prenantes et les besoins métier. |
| **Scrum Master (SM)** | Garant de la bonne compréhension et de l'application de Scrum. Coach de l'équipe et de l'organisation. Supprime les obstacles (impediments). Facilite les événements Scrum. |
| **Developers (équipe de développement)** | Créent l'Increment à chaque Sprint. Auto-organisés et pluridisciplinaires. Définissent et respectent la Definition of Done. Responsables du Sprint Backlog. |

**Note Scrum 2020** : le terme "équipe de développement" a été remplacé par "Developers" pour éviter la confusion avec les seuls développeurs logiciels — cela inclut designers, testeurs, analystes, etc.

---

#### Les 5 événements (Events)

| Événement | Durée max (sprint 4 semaines) | Objectif |
|---|---|---|
| **Sprint** | 4 semaines maximum | Conteneur de tous les autres événements. Durée fixe et constante (time-box). Produit un Increment potentiellement livrable. |
| **Sprint Planning** | 8 heures | Définir l'objectif du sprint (Sprint Goal) et sélectionner les éléments du Product Backlog à réaliser. Créer le Sprint Backlog. |
| **Daily Scrum** | 15 minutes | Synchronisation quotidienne de l'équipe. Inspecter l'avancement vers le Sprint Goal et adapter le plan du jour. |
| **Sprint Review** | 4 heures | Présenter l'Increment aux parties prenantes. Inspecter le résultat, collecter le feedback, adapter le Product Backlog. |
| **Sprint Retrospective** | 3 heures | Inspecter le fonctionnement de l'équipe (processus, interactions, outils). Identifier des améliorations pour le prochain sprint. |

**Distinction Review / Retrospective :**
- **Review** : axée sur le **produit** (qu'est-ce qu'on a livré ?).
- **Retrospective** : axée sur l'**équipe et le processus** (comment on a travaillé ?).

---

#### Les 3 artefacts (Artifacts)

| Artefact | Contenu | Engagement associé |
|---|---|---|
| **Product Backlog** | Liste ordonnée de tout ce qui pourrait être fait pour améliorer le produit. Vivant, jamais figé. | **Product Goal** — l'objectif long terme du produit |
| **Sprint Backlog** | Subset du Product Backlog sélectionné pour le sprint + plan pour le réaliser. Propriété des Developers. | **Sprint Goal** — l'objectif du sprint |
| **Increment** | Somme de tout le travail "Done" du sprint + tous les sprints précédents. Doit respecter la Definition of Done. | **Definition of Done** |

**Nouveauté Scrum 2020** : introduction du concept d'**engagement** (commitment) pour chaque artefact — Product Goal, Sprint Goal, Definition of Done — pour renforcer la transparence.

---

#### Definition of Done (DoD)

La Definition of Done est un ensemble de critères que doit respecter chaque Increment pour être considéré comme "terminé". Elle est formalisée par l'équipe Scrum (ou l'organisation si plusieurs équipes). Elle garantit la qualité et la transparence.

Exemples de critères DoD :
- Code revu par un pair (code review).
- Tests unitaires rédigés et passants (couverture > 80 %).
- Tests d'intégration passants.
- Documentation technique mise à jour.
- Déployé en environnement de staging.
- Validé fonctionnellement par le PO.

---

#### Vélocité

La vélocité est une **métrique empirique** qui mesure la quantité de travail (en points de story / story points) qu'une équipe Scrum complète en un sprint. Elle s'utilise pour :
- **Planifier** les sprints futurs (capacité prévisionnelle).
- **Projeter** la date de fin d'un projet (Product Backlog restant / vélocité moyenne).

**Précaution** : la vélocité est un outil d'équipe, pas un outil de comparaison entre équipes. Comparer les vélocités de deux équipes n'a aucun sens (les estimations sont relatives à chaque équipe).

---

### Scrum vs Kanban

| Dimension | Scrum | Kanban |
|---|---|---|
| **Structure temporelle** | Sprints (time-boxed, durée fixe) | Flux continu (pas de time-box) |
| **Rôles définis** | Oui (PO, SM, Developers) | Non (rôles existants conservés) |
| **Planification** | Sprint Planning obligatoire | Au fil de l'eau (pull system) |
| **Indicateur clé** | Vélocité (story points/sprint) | Lead time et cycle time |
| **WIP limit** | Non défini (géré via le Sprint Goal) | Limiteur de WIP explicite par colonne |
| **Changements en cours** | Non recommandés pendant le sprint | Acceptés à tout moment |
| **Adapté à** | Projets à périmètre évolutif, équipes de dev | Maintenance, support, flux de travail continu |
| **Cadre** | Prescriptif (événements, artefacts, rôles définis) | Évolutif (on part de l'existant) |

**Scrumban** : hybride combinant la structure de Scrum et les limites WIP de Kanban — utilisé pour les équipes en transition ou les contextes mixtes dev/maintenance.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Livraison rapide de valeur (chaque sprint) | Nécessite une disponibilité réelle du PO |
| Feedback régulier des parties prenantes | Difficile à scaler sans framework complémentaire (SAFe, LeSS) |
| Amélioration continue via la rétrospective | Peut créer une pression excessive sur l'équipe (velocity fever) |
| Transparence sur l'avancement | Pas adapté aux projets très stables et prévisibles (certains projets industriels) |
| Réduction des risques par itérations courtes | La Definition of Done mal définie → dette technique |

### Acteurs / Outils
- **Certifications** : PSM (Professional Scrum Master, Scrum.org), CSM (Certified ScrumMaster, Scrum Alliance), PSPO (Product Owner).
- **Outils** : Jira (backlog, sprint board, burndown charts), Azure DevOps, Linear, Trello, Miro (retrospectives), Notion.
- **Scaling** : SAFe (Scaled Agile Framework), LeSS (Large-Scale Scrum), Nexus (extension Scrum officielle de Scrum.org) pour plusieurs équipes Scrum.

### Cas d'usage concrets

**Cas 1 : Développement d'une application mobile (fintech)**
- Sprint de 2 semaines. PO = product manager côté client. SM = consultant agile externe.
- Sprint 1 : authentification + onboarding (Must have MoSCoW).
- Sprint 2 : tableau de bord portefeuille.
- Sprint Review avec les investisseurs à J+14 → feedback intégré dans le Product Backlog.

**Cas 2 : Transformation DSI avec Scrum of Scrums**
- 4 équipes Scrum sur 4 chantiers (infrastructure, sécurité, data, applicatifs métier).
- Scrum of Scrums hebdomadaire pour synchroniser les dépendances inter-équipes.
- Program Increment Planning trimestriel (pratique SAFe).

### Chiffres et tendances
- Le **Scrum Guide 2020** a supprimé les notions de "servant leader" et d'"équipe de développement" au profit de formulations plus directes sur les responsabilités.
- **SAFe** (Scaled Agile Framework) est adopté par **35 %** des entreprises qui scalent Scrum (State of Agile Report, 2023).
- Les équipes Scrum bien formées réduisent le time-to-market de **37 %** en moyenne (McKinsey Digital, 2022).

---

## Flashcards
#flashcards/Transversal/Scrum #flashcards/Développement/Scrum

Quels sont les 3 rôles Scrum définis dans le Scrum Guide 2020 ? :: **Product Owner** (maximise la valeur, responsable du Product Backlog), **Scrum Master** (garant de Scrum, coach, lève les obstacles), **Developers** (créent l'Increment, auto-organisés, pluridisciplinaires).

Quels sont les 5 événements Scrum et leur rôle ? :: **Sprint** (conteneur, 1-4 semaines), **Sprint Planning** (définir le Sprint Goal et le Sprint Backlog), **Daily Scrum** (synchronisation quotidienne 15 min), **Sprint Review** (inspecter l'Increment avec les parties prenantes), **Sprint Retrospective** (améliorer le fonctionnement de l'équipe).

Quelle est la différence entre Sprint Review et Sprint Retrospective ? :: La **Review** est centrée sur le **produit** (qu'a-t-on livré ? quel feedback ?). La **Retrospective** est centrée sur l'**équipe et le processus** (comment a-t-on travaillé ? que peut-on améliorer ?).

Quels sont les 3 artefacts Scrum et leurs engagements associés ? :: **Product Backlog** → engagement : Product Goal. **Sprint Backlog** → engagement : Sprint Goal. **Increment** → engagement : Definition of Done.

Qu'est-ce que la Definition of Done (DoD) ? :: Un ensemble de critères que doit respecter chaque Increment pour être considéré comme "terminé" (ex. : code revu, tests passants, déployé en staging, validé par le PO). Elle garantit la qualité et la transparence.

Quelles sont les 3 principales différences entre Scrum et Kanban ? :: Scrum utilise des **sprints** (time-box fixe), des **rôles définis** et mesure la **vélocité**. Kanban est un **flux continu**, sans rôles prescrits, et utilise des **limites WIP** et le **lead time** comme indicateurs.

Quelle est la nouveauté principale du Scrum Guide 2020 par rapport aux versions précédentes ? :: Introduction du concept d'**engagement** (commitment) pour chaque artefact (Product Goal, Sprint Goal, Definition of Done), et remplacement de "équipe de développement" par "**Developers**". Le guide est aussi passé de 19 à 13 pages (simplification).

---

## Sources
- Schwaber, K. & Sutherland, J. — *The Scrum Guide* (novembre 2020). Disponible sur scrumguides.org.
- Scrum.org — *State of Scrum Report 2023*.
- McKinsey Digital — *The five trademarks of agile organizations* (2018, mise à jour 2022).
- State of Agile Report 2023 (Digital.ai).

---

## Notions liées
- [[Méthode MoSCoW]]
- [[Conduite du changement]]
- [[AMDEC]]
- [[SWOT - PESTEL]]
