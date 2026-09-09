---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 2026-09-08
---

# IA de confiance et IA responsable

## En bref

### Définition
L'**IA de confiance (Trustworthy AI)** désigne une IA légale, éthique et robuste techniquement. L'**IA responsable** insiste sur la responsabilité des acteurs tout au long du cycle de vie du système. Ces deux notions convergent : une IA doit être transparente, explicable, équitable, sûre et respectueuse des droits fondamentaux.

### Pourquoi c'est important
Alors que l'IA prend des décisions à fort impact, la confiance des citoyens et des organisations est un prérequis à son adoption durable. Les scandales (COMPAS, biais de recrutement, deep fakes) ont montré que sans cadre éthique et technique solide, l'IA peut causer des dommages réels et miner la démocratie.

### Chiffres clés
- **2019** : la Commission européenne publie les "Ethics Guidelines for Trustworthy AI" avec 7 exigences clés (HLEG).
- **2023** : l'OCDE identifie 5 principes pour une IA responsable adoptés par 46 pays.
- **63 %** des consommateurs déclarent ne pas faire confiance aux décisions prises par une IA sans supervision humaine (Edelman Trust Barometer, 2023).

---

## Approfondir

### Fonctionnement

#### Les 7 exigences du HLEG (IA de confiance selon la CE, 2019)
1. **Action humaine et supervision** (human-in-the-loop)
2. **Robustesse technique et sécurité**
3. **Respect de la vie privée et gouvernance des données**
4. **Transparence**
5. **Diversité, non-discrimination et équité**
6. **Bien-être sociétal et environnemental**
7. **Responsabilité et obligation de rendre compte**

#### Concepts clés
- **XAI (Explainable AI)** : ensemble de méthodes permettant de rendre les décisions d'un modèle IA compréhensibles par des humains (LIME, SHAP, attention maps). Essentiel pour la confiance et la contestation des décisions.
- **Human-in-the-loop (HITL)** : paradigme où un humain intervient dans le processus de décision automatisé pour valider, corriger ou superviser l'IA.
- **AI Alignment** : problème fondamental consistant à s'assurer que les objectifs et comportements d'un système IA sont alignés avec les valeurs et intentions humaines. Domaine de recherche majeur face aux IA avancées.
- **Constitutional AI (Anthropic)** : approche d'entraînement où l'IA est guidée par un ensemble de principes éthiques explicites pour auto-critiquer et corriger ses réponses.

### Avantages / Inconvénients

| Avantages | Défis |
|---|---|
| Adoption durable et confiance des utilisateurs | Tension entre explicabilité et performance (boîte noire vs interprétable) |
| Conformité réglementaire (AI Act, RGPD) | Coût de mise en oeuvre des garde-fous |
| Réduction des risques réputationnels | Définition variable selon les acteurs et contextes |
| Meilleure détection des dérives | L'alignement reste un problème ouvert pour les IA avancées |
| Responsabilisation des développeurs et déployeurs | Risque de "ethics washing" sans engagement réel |

### Acteurs
- **HLEG (High-Level Expert Group on AI)** : groupe d'experts mandaté par la Commission européenne, auteur des lignes directrices de 2019.
- **Anthropic** : recherche en AI alignment et Constitutional AI.
- **DeepMind (Google)** : équipe de recherche en AI safety et alignment.
- **Partnership on AI** : consortium multi-acteurs (Google, Amazon, Microsoft, ONG) sur les bonnes pratiques IA.
- **AI Safety Institute (UK, 2023)** : premier organisme gouvernemental dédié à la sécurité des IA de frontier.

### Cas d'usage
- **Médical** : IA de diagnostic avec human-in-the-loop obligatoire (médecin valide le résultat).
- **Justice** : outils d'aide à la décision avec obligation d'explicabilité (RGPD art. 22).
- **Finance** : modèles de crédit avec droit d'explication et de contestation.
- **Conduite autonome** : niveaux d'autonomie avec supervision humaine graduelle (SAE L1-L5).
- **Modération de contenu** : IA + réviseurs humains pour les cas complexes.

### Chiffres complémentaires
- L'**AI Act** classe 8 types de systèmes IA comme "inacceptables" (interdits) et impose le HITL pour les systèmes à haut risque.
- **SHAP et LIME** sont les deux méthodes XAI les plus utilisées en entreprise (State of AI Report 2023).
- Le domaine de l'AI safety représente moins de **1 %** des publications en IA, mais attire **> 500 M$** d'investissements annuels (2023).

---

## Flashcards
#flashcards/IA/IA_de_confiance_et_IA_responsable

**Qu'est-ce que l'IA de confiance (Trustworthy AI) selon la Commission européenne ?** :: Une IA qui respecte 7 exigences : supervision humaine, robustesse, vie privée, transparence, équité, bien-être sociétal et responsabilité (HLEG, 2019).

**Qu'est-ce que l'XAI (Explainable AI) ?** :: Ensemble de méthodes (LIME, SHAP) rendant les décisions d'un modèle IA compréhensibles par des humains, pour permettre confiance et contestation.

**Qu'est-ce que le human-in-the-loop ?** :: Paradigme où un humain supervise, valide ou corrige les décisions d'un système IA, garantissant un contrôle humain dans la boucle décisionnelle.

**Qu'est-ce que l'AI alignment ?** :: Problème de recherche consistant à s'assurer que les objectifs et comportements d'une IA sont alignés avec les valeurs et intentions humaines.

**Qu'est-ce que la Constitutional AI d'Anthropic ?** :: Méthode d'entraînement guidant l'IA par un ensemble de principes éthiques explicites pour qu'elle auto-critique et corrige ses réponses selon ces valeurs.

**Quelle est la différence entre IA de confiance et IA responsable ?** :: La trustworthy AI met l'accent sur les propriétés techniques et éthiques du système ; l'IA responsable insiste sur la responsabilité des acteurs (développeurs, déployeurs) tout au long du cycle de vie.

**Quelles sont les deux méthodes XAI les plus utilisées ?** :: SHAP (SHapley Additive exPlanations) et LIME (Local Interpretable Model-agnostic Explanations).

---

## Sources
- HLEG, "Ethics Guidelines for Trustworthy AI", Commission européenne, 2019
- OCDE, "Principles on AI", 2019 (révisés 2023)
- Anthropic, "Constitutional AI: Harmlessness from AI Feedback", 2022
- Ribeiro et al., "Why Should I Trust You? LIME", 2016
- AI Safety Institute (AISI), UK, 2023 — [gov.uk/ai-safety-institute](https://www.gov.uk/government/organisations/ai-safety-institute)

---

## Notions liées
- [[Biais algorithmiques]]
- [[Audit algorithmique]]
- [[Éthique de l'IA]]
- [[AI Act]]
- [[Cadre international de l'IA]]
- [[Normes ISO pour l'IA]]
- [[RGPD]]
