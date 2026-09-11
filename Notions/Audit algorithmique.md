---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 
---

# Audit algorithmique

## En bref

### Définition
L'**audit algorithmique** est un processus d'évaluation systématique d'un système d'IA ou d'un algorithme visant à vérifier sa conformité, son équité, sa transparence et sa fiabilité. Il peut être interne (auto-évaluation) ou externe (tiers indépendant), et couvre les données, le modèle, le code et les impacts réels.

### Pourquoi c'est important
Face à la multiplication des décisions automatisées à fort impact (crédit, recrutement, justice), l'audit algorithmique est devenu un outil clé de gouvernance et de responsabilité. L'AI Act européen le rend obligatoire pour les systèmes IA à haut risque. Sans audit, les biais et les dérives restent invisibles.

### Chiffres clés
- L'**AI Act (2024)** impose des audits de conformité obligatoires pour tous les systèmes IA classés "haut risque" avant leur mise sur le marché.
- **70 %** des organisations déclarent ne pas disposer de processus formalisés d'audit de leurs modèles IA (Gartner, 2023).
- Le marché de l'audit et de la gouvernance IA devrait dépasser **5 Md$** d'ici 2027.

---

## Approfondir

### Fonctionnement

Un audit algorithmique comprend généralement plusieurs étapes :

1. **Définition du périmètre** : quel système, quels usages, quelles parties prenantes ?
2. **Audit des données** : origine, qualité, représentativité, biais potentiels (datasheets).
3. **Audit du modèle** : architecture, métriques de performance, robustesse, explicabilité.
4. **Audit des impacts** : effets réels sur les utilisateurs, tests de discrimination, analyse des cas limites.
5. **Documentation et certification** : production d'un rapport, d'une model card, recommandations correctives.
6. **Suivi continu** : re-audit périodique, monitoring en production.

**Outils documentaires clés :**
- **Model Card** (Google, 2019) : fiche standardisée décrivant les caractéristiques d'un modèle (performance par sous-groupe, usages prévus, limites).
- **Datasheet for Datasets** (Gebru et al., 2018) : documentation structurée des jeux de données (origine, collecte, biais potentiels, usages appropriés).

### Avantages / Inconvénients

| Avantages | Inconvénients / Limites |
|---|---|
| Détection précoce des biais et risques | Coût et complexité élevés |
| Conformité réglementaire (AI Act) | Accès au code/données souvent restreint (audit externe) |
| Renforce la confiance des utilisateurs | Pas de standard universel encore établi |
| Responsabilisation des organisations | Risque de "compliance washing" sans réelle correction |
| Base pour la certification et l'assurance qualité IA | Difficulté à auditer les modèles boîte noire (LLM) |

### Acteurs
- **IBM AI Fairness 360** : bibliothèque open-source pour détecter et atténuer les biais dans les jeux de données et les modèles.
- **Fairlearn (Microsoft)** : framework Python d'évaluation et d'amélioration de l'équité des modèles ML.
- **NIST (USA)** : AI Risk Management Framework (AI RMF 1.0, 2023) — cadre de gestion des risques IA.
- **AlgorithmWatch** : ONG européenne spécialisée dans l'audit et la surveillance des algorithmes.
- **AFNOR / ISO** : travaux de normalisation (ISO/IEC 42001, 23894).
- **Équipe RED d'Anthropic, OpenAI, etc.** : red-teaming interne des modèles de fondation.

### Cas d'usage
- **Recrutement** : audit des outils de tri de CV pour détecter les discriminations de genre ou d'origine.
- **Crédit** : vérification des algorithmes de scoring pour garantir la non-discrimination.
- **Justice prédictive** : audit de COMPAS et systèmes similaires.
- **Santé** : audit des dispositifs médicaux IA (classification haut risque sous AI Act et MDR).
- **Secteur public** : audit des algorithmes de décision administrative (CAF, Pôle Emploi).

### Chiffres complémentaires
- En France, le rapport Villani (2018) recommandait déjà la création d'un droit à l'audit des algorithmes publics.
- L'article 22 du **RGPD** donne un droit d'explication pour toute décision automatisée individuelle significative.
- L'AI Act prévoit des amendes allant jusqu'à **30 M€ ou 6 % du CA mondial** pour non-conformité des systèmes à haut risque.

---

## Flashcards
#flashcards/IA/Audit_algorithmique

**Qu'est-ce qu'un audit algorithmique ?** :: Processus d'évaluation systématique d'un système IA vérifiant sa conformité, son équité, sa transparence et sa fiabilité, réalisé par un tiers ou en interne.

**Qu'est-ce qu'une model card ?** :: Fiche standardisée (Google, 2019) documentant les caractéristiques d'un modèle IA : performances par sous-groupe, usages prévus, limites et biais connus.

**Qu'est-ce qu'un datasheet for datasets ?** :: Document structuré (Gebru et al., 2018) décrivant l'origine, la collecte, les biais potentiels et les usages appropriés d'un jeu de données.

**Quels outils open-source permettent d'auditer l'équité d'un modèle IA ?** :: IBM AI Fairness 360 (détection et correction de biais) et Fairlearn de Microsoft (évaluation et amélioration de l'équité).

**Quelles obligations l'AI Act impose-t-il en matière d'audit ?** :: Les systèmes IA à haut risque doivent faire l'objet d'une évaluation de conformité avant mise sur le marché, avec documentation, journalisation et supervision humaine.

**Qu'est-ce que le red-teaming en IA ?** :: Méthode d'audit consistant à tester adversarialement un système IA pour identifier ses failles, biais ou comportements dangereux avant déploiement.

---

## Sources
- Mitchell et al., "Model Cards for Model Reporting", Google, 2019
- Gebru et al., "Datasheets for Datasets", 2018
- NIST AI RMF 1.0, 2023 — [nist.gov](https://www.nist.gov/artificial-intelligence)
- AlgorithmWatch — [algorithmwatch.org](https://algorithmwatch.org)
- AI Act (Règlement UE 2024/1689)

---

## Notions liées
- [[Biais algorithmiques]]
- [[IA de confiance et IA responsable]]
- [[Éthique de l'IA]]
- [[AI Act]]
- [[Normes ISO pour l'IA]]
- [[RGPD]]
