---
type: notion
thèmes:
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Value Stream Mapping

![[N — Value Stream Mapping.mp3]]
## En bref

### Définition
La **Value Stream Mapping (VSM)** ou cartographie de la chaîne de valeur est un outil visuel issu du Lean Manufacturing (Toyota Production System) permettant de représenter l'ensemble des étapes — à valeur ajoutée et sans valeur ajoutée — nécessaires pour délivrer un produit ou service à un client. Appliquée au SI (Lean IT / Lean Six Sigma), elle modélise les flux d'information et de travail pour identifier les gaspillages (muda), les goulots d'étranglement et les délais d'attente.

Le **Lean Six Sigma** combine les principes lean (élimination des gaspillages) et le Six Sigma (réduction de la variabilité par l'approche DMAIC : Define, Measure, Analyze, Improve, Control).

### Pourquoi c'est important
Dans un SI complexe, les processus de delivery (développement, déploiement, gestion des incidents) comportent souvent 70 à 80 % de temps sans valeur ajoutée. La VSM rend ces inefficacités visibles et fournit une base factuelle pour prioriser les chantiers d'optimisation.

### Chiffres clés
- En moyenne, seulement 20 à 30 % du temps d'un processus IT est à valeur ajoutée (Lean IT Institute)
- Les organisations ayant cartographié leur value stream réduisent leur Lead Time de 50 % en moyenne
- Le marché du Lean Six Sigma consulting est évalué à plus de 5 Md$ mondialement

---

## Approfondir

### Fonctionnement

**Étapes de réalisation d'une VSM :**
1. **Sélectionner le flux à cartographier** : choisir un produit/service représentatif (ex. traitement d'une demande de changement)
2. **Cartographier l'état actuel (current state)** : documenter chaque étape, les temps de cycle, les temps d'attente, les stocks, les acteurs
3. **Calculer les indicateurs clés** :
   - **Lead Time** : temps total de bout en bout
   - **Process Time** (ou Value-Added Time) : temps effectivement travaillé
   - **Takt Time** : cadence de la demande client (Lead Time / nombre d'unités demandées)
   - **Ratio VA / NVA** : part de valeur ajoutée vs non-valeur ajoutée
4. **Identifier les gaspillages et goulots** : files d'attente, transferts, re-travail, approbations inutiles
5. **Concevoir l'état futur (future state)** : fluidifier les flux, supprimer les étapes sans VA, automatiser
6. **Plan d'action et mise en œuvre** : chantiers kaizen, quick wins et projets structurels

**Symboles standards de la VSM :**
- Boîte de processus : étape de transformation
- Triangle stock : accumulation de travail en attente (WIP)
- Flèche push / pull : sens du flux
- Éclair : flux électronique / automatisé
- Nuage : fournisseur / client externe

**Lean Six Sigma — DMAIC appliqué au SI :**
- **Define** : définir le problème et les CTQ (Critical To Quality)
- **Measure** : collecter les données (Lead Time, taux de défauts, MTTR)
- **Analyze** : identifier les causes racines (RCA, VSM)
- **Improve** : implémenter les solutions (automatisation, kaizen)
- **Control** : pérenniser les gains (indicateurs, standards)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|-----------|---------------|
| Visualisation systémique du flux de bout en bout | Effort de collecte de données important |
| Langage commun entre IT et métier | Résistance des équipes à la transparence |
| Identification factuelle des gaspillages | Risque de cartographie trop théorique si non validée terrain |
| Base solide pour prioriser les améliorations | Difficile à maintenir à jour dans des SI complexes |
| Applicable aux processus ITSM et DevOps | Nécessite une formation spécifique aux symboles et méthodes |

### Acteurs
- **Mike Rother & John Shook** : auteurs de *Learning to See*, référence VSM
- **Lean IT Institute** : promotion du lean dans les SI
- **Institut Lean France** : formations et certification
- **Six Sigma Council** : certification Black Belt, Green Belt
- **SAFe (Scaled Agile Framework)** : intègre le VSM dans la planification PI

### Cas d'usage
- **Pipeline CI/CD** : cartographier le flux depuis le commit développeur jusqu'au déploiement en production pour réduire le Lead Time de livraison
- **Gestion des incidents ITSM** : identifier les étapes d'escalade sans valeur ajoutée dans le processus de ticketing
- **Onboarding IT** : cartographier le processus de création de compte et d'équipement d'un nouveau collaborateur
- **Flux de data** : optimiser le pipeline ETL en identifiant les latences et re-traitements inutiles

### Chiffres complémentaires
- Après VSM et chantiers lean, les équipes DevOps réduisent leur Lead Time de déploiement de 60 % en médiane (rapport DORA)
- La réduction du WIP (Work in Progress) de 30 % améliore la productivité de 40 % (Kanban Studies)

---

## Flashcards
#flashcards/Optimisation_du_SI/Value_Stream_Mapping

Qu'est-ce que la Value Stream Mapping ? :: Un outil visuel lean permettant de cartographier toutes les étapes (VA et NVA) d'un flux de valeur pour identifier les gaspillages et optimiser le processus.

Que représentent les indicateurs Lead Time et Process Time dans une VSM ? :: Le Lead Time est le temps total de bout en bout ; le Process Time (ou Value-Added Time) est le temps réellement travaillé — leur ratio révèle l'efficience du flux.

Qu'est-ce que le Takt Time ? :: Le rythme de la demande client : temps disponible divisé par le nombre d'unités demandées — il définit la cadence cible de production.

Quelles sont les 6 étapes de réalisation d'une VSM ? :: Sélectionner le flux, cartographier l'état actuel, calculer les indicateurs, identifier les gaspillages, concevoir l'état futur, plan d'action.

Que signifie DMAIC dans le Lean Six Sigma ? :: Define, Measure, Analyze, Improve, Control — démarche structurée d'amélioration par réduction des gaspillages et de la variabilité.

Comment la VSM s'applique-t-elle au DevOps ? :: En cartographiant le pipeline depuis le commit jusqu'au déploiement pour identifier les délais d'attente, les approbations manuelles et les goulots d'étranglement.

Quelle est la différence entre Lean et Six Sigma ? :: Le Lean élimine les gaspillages et réduit les délais ; le Six Sigma réduit la variabilité et les défauts. Le Lean Six Sigma combine les deux approches.

---

## Sources
- Mike Rother & John Shook, *Learning to See*, Lean Enterprise Institute, 1998
- James Womack & Daniel Jones, *Lean Thinking*, Free Press, 1996
- DORA State of DevOps Report, 2023
- Lean IT Institute — leanit.org
- SAFe 6.0 Framework — scaledagileframework.com

---

## Notions liées
- [[Amélioration continue (PDCA - Lean - Kaizen)]]
- [[DORA Metrics]]
- [[CI - CD]]
- [[DevOps]]
- [[ISO 9001 et qualité]]
- [[Outils ITSM]]
