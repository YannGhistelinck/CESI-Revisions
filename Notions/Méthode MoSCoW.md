---
type: notion
thèmes:
  - Transversal
statut: pas vu
dernière_révision: 
---

## En bref

### Définition
MoSCoW est une technique de priorisation des exigences et des fonctionnalités, structurée en quatre catégories : **Must have** (obligatoire), **Should have** (important mais non bloquant), **Could have** (souhaitable si le temps le permet), **Won't have (this time)** (exclu de la version actuelle). Développée par Dai Clegg chez Oracle en 1994, popularisée par la méthode DSDM.

### Pourquoi c'est important
Tout projet IT est soumis à des contraintes de périmètre, de délai et de budget (triangle de fer). MoSCoW permet d'objectiver le débat sur les priorités, d'éviter le scope creep (dérive du périmètre) et de garantir que les fonctionnalités les plus critiques sont livrées en premier. C'est un outil de dialogue entre équipe projet et parties prenantes.

### Chiffres clés
- La priorisation MoSCoW est l'une des techniques recommandées par le **DSDM Agile Project Framework** et le **PMI** (PMBOK 7e éd.).
- Le scope creep est cité comme cause principale de dépassement de budget dans **52 %** des projets IT (PMI Pulse of the Profession, 2023).
- Règle empirique : les **Must have** ne doivent pas dépasser **60 %** du périmètre total estimé pour laisser une marge de manœuvre.

---

## Approfondir

### Fonctionnement

Chaque exigence ou user story est classée dans l'une des quatre catégories :

| Catégorie | Signification | Critère de classement |
|---|---|---|
| **Must have** | Indispensable — sans cela, le produit est inutilisable ou le projet échoue | Bloquant pour la mise en production ; exigence légale, sécurité, fonctionnalité cœur |
| **Should have** | Important mais non bloquant — le produit fonctionne sans, mais avec une gêne significative | Forte valeur métier, pas de workaround acceptable à long terme |
| **Could have** | Souhaitable si le temps et le budget le permettent — amélioration du confort ou de l'expérience | Faible impact si absent, workaround acceptable |
| **Won't have (this time)** | Explicitement exclu de la version actuelle — pourra être reconsidéré dans une itération future | Hors périmètre de la release, demande future documentée |

**Points de vigilance :**
- **"Won't have"** ne signifie pas "jamais" — c'est un report assumé et documenté, pas un rejet définitif.
- La catégorie **Could have** est souvent appelée "nice to have" mais doit tout de même être estimée pour ne pas être incluse par défaut.
- Le **Must have** doit être challengé : si tout est Must have, la priorisation est inopérante.

### Utilisation en contexte projet

**Cadrage projet (phase initiation)**
Lors du recueil des besoins, MoSCoW permet de structurer les ateliers avec les MOA/MOE et d'obtenir un consensus documenté sur le périmètre de la version 1. Elle alimente directement le cahier des charges ou la charte de projet.

**Sprint planning (contexte Scrum)**
En début de sprint, le Product Owner utilise MoSCoW pour prioriser le Sprint Backlog : les Must have sont traités en priorité, les Should have si la capacité le permet, les Could have en fin de sprint ou reportés.

**Gestion de périmètre (change request)**
Quand une nouvelle demande arrive en cours de projet, MoSCoW force à la question : "Si on ajoute ça, qu'est-ce qu'on sort ?" Elle formalise le arbitrage périmètre/délai/budget devant le comité de pilotage.

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Simple à comprendre et à expliquer aux non-initiés | Manque de granularité (4 cases seulement) |
| Facilite le consensus entre parties prenantes | Subjectif : le "Must" de l'un est le "Could" de l'autre |
| Adaptable à Agile et à la gestion de projet classique | Ne prend pas en compte la dépendance entre exigences |
| Réduit le scope creep en explicitant ce qui est exclu | Risque de sur-catégorisation en "Must have" sous pression |
| Documente les arbitrages et les décisions | Nécessite une animation rigoureuse et un facilitateur neutre |

### Comparaison avec d'autres méthodes de priorisation

| Méthode | Logique | Usage privilégié |
|---|---|---|
| **MoSCoW** | Catégorisation par nécessité | Cadrage projet, sprint planning, gestion du périmètre |
| **Matrice d'Eisenhower** | Urgent × Important (4 quadrants) | Gestion du temps individuel et des tâches opérationnelles |
| **Méthode de Kano** | Satisfaction client selon 3 types (basique, performance, enchantement) | Conception produit, UX, priorisation orientée valeur client |
| **WSJF (Weighted Shortest Job First)** | Coût du délai / durée | SAFe, priorisation fine dans les programmes agiles à l'échelle |
| **ICE Scoring** | Impact × Confidence × Ease | Growth hacking, startups, priorisation rapide |

**MoSCoW vs Eisenhower** : Eisenhower priorise selon l'urgence et l'importance (temporel et personnel), MoSCoW priorise selon la valeur et la nécessité (produit et périmètre). Les deux sont complémentaires.

**MoSCoW vs Kano** : Kano analyse la satisfaction client (ce qui enchante vs ce qui est attendu), MoSCoW classe selon la nécessité pour le bon fonctionnement du système. Kano est plus riche pour la conception produit, MoSCoW plus adapté à la gestion de projet.

### Acteurs / Outils
- **Qui anime** : chef de projet, Product Owner, business analyst, facilitateur.
- **Qui participe** : MOA (maîtrise d'ouvrage), utilisateurs clés, sponsor, équipe technique.
- **Outils** : Jira (labels MoSCoW sur les user stories), Confluence (tableau de priorisation), Miro/Mural (atelier de priorisation visuel), simple tableau Excel.

### Cas d'usage concrets en IT

**Cas 1 : Développement d'un portail client (e-commerce)**
| Fonctionnalité | Catégorie MoSCoW | Justification |
|---|---|---|
| Authentification sécurisée | Must have | Obligation légale + sécurité |
| Catalogue produits avec filtres | Must have | Fonctionnalité cœur |
| Recommandations personnalisées (IA) | Could have | Valeur ajoutée, pas bloquant |
| Chat en temps réel avec conseiller | Should have | Forte valeur, workaround email |
| Programme de fidélité gamifié | Won't have (this time) | Report à V2 |

**Cas 2 : Migration ERP — sprint planning**
Les Must have couvrent 55 % de la capacité du sprint (flux comptables, paie), les Should have 30 % (reporting RH), les Could have 15 % (tableau de bord exécutif). Si l'équipe prend du retard, les Could have sautent sans remettre en cause la livraison.

### Chiffres et tendances
- DSDM (Dynamic Systems Development Method), cadre agile qui a formalisé MoSCoW, est certifié par l'**APMG International**.
- Le **PMBOK 7e édition** (2021) intègre explicitement MoSCoW comme technique de priorisation des exigences dans le domaine "Stakeholders".
- Dans une enquête Scrum.org (2023), **43 %** des Product Owners déclarent utiliser MoSCoW comme principal outil de priorisation du backlog.

---

## Flashcards
#flashcards/Transversal/Méthode_MoSCoW

Que signifie l'acronyme MoSCoW ? :: **M**ust have (obligatoire), **S**hould have (important), **C**ould have (souhaitable), **W**on't have this time (exclu de la version actuelle). La casse des lettres reflète l'acronyme : les O sont en minuscule pour former le mot "Moscow".

Que signifie "Won't have (this time)" dans MoSCoW ? :: Ce n'est pas un refus définitif mais un **report explicite et documenté** à une version future. L'expression "this time" est importante : la demande est reconnue mais hors périmètre de la release actuelle.

Quelle règle empirique s'applique aux Must have dans MoSCoW ? :: Les **Must have ne doivent pas dépasser 60 %** de l'effort total estimé du projet ou du sprint, pour conserver une marge de manœuvre et éviter que le projet ne soit bloqué dès le départ.

Quelle est la différence entre MoSCoW et la matrice d'Eisenhower ? :: Eisenhower classe selon **urgence × importance** (gestion du temps, tâches individuelles). MoSCoW classe selon la **nécessité pour le périmètre produit** (cadrage projet, backlog). Les deux sont complémentaires mais servent des usages différents.

Dans quel cadre méthodologique MoSCoW a-t-elle été formalisée ? :: Dans le cadre **DSDM** (Dynamic Systems Development Method), une méthode agile britannique développée dans les années 1990. Elle est aussi référencée dans le **PMBOK 7e édition** et dans **SAFe**.

Comment MoSCoW réduit-il le scope creep ? :: En classifiant explicitement ce qui est **hors périmètre (Won't have)**, MoSCoW oblige à un arbitrage formel pour toute nouvelle demande : ajouter quelque chose impose de définir ce qu'on sort ou comment on ajuste les délais/budget.

Quelle est la différence entre MoSCoW et la méthode de Kano ? :: **Kano** analyse la satisfaction utilisateur selon 3 types d'attributs (basique/performance/enchantement), orienté **conception produit et UX**. **MoSCoW** classe les exigences selon leur nécessité, orienté **gestion du périmètre projet**. Kano est plus riche pour innover, MoSCoW plus pratique pour livrer.

---

## Sources
- Clegg, D. & Barker, R. (1994) — *CASE Method Fast-Track: A RAD Approach*, Addison-Wesley.
- DSDM Consortium — *DSDM Agile Project Framework Handbook* (2014).
- PMI — *PMBOK Guide, 7e édition* (2021).
- PMI — *Pulse of the Profession 2023*.
- Scrum.org — *State of Scrum Report 2023*.

---

## Notions liées
- [[Scrum]]
- [[SWOT - PESTEL]]
- [[VAN - TRI - Payback]]
- [[Conduite du changement]]
