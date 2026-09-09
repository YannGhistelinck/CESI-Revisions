---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 
---

# Intelligence Artificielle — fondamentaux

## En bref

### Définition
L'**intelligence artificielle** (IA) désigne l'ensemble des techniques permettant à une machine de simuler des capacités cognitives humaines : raisonnement, apprentissage, perception, compréhension du langage. Elle recouvre plusieurs sous-domaines emboîtés : le **machine learning** (ML), le **deep learning**, le **NLP**, la **vision par ordinateur**, et vise à terme l'**AGI** (intelligence artificielle générale).

### Pourquoi c'est important
L'IA est la technologie transversale du XXIe siècle : elle restructure tous les secteurs (santé, finance, industrie, marketing), redéfinit les métiers du SI (AIOps, MLOps), et constitue un enjeu stratégique majeur pour les entreprises et les États. Dans le contexte MAALSI, elle est le fil rouge de la transformation des systèmes d'information.

### Chiffres clés
- Marché mondial de l'IA : **184 Md$ en 2024**, attendu à ~**826 Md$ en 2030** (CAGR ~27 %)
- **85 % des entreprises** du CAC 40 ont une initiative IA en production (2024)
- Le deep learning représente **>60 %** des publications IA scientifiques depuis 2020
- ChatGPT : **100 millions d'utilisateurs** en 2 mois (record historique d'adoption)

---

## Approfondir

### Fonctionnement

```
IA (concept large)
 └── Machine Learning — apprendre à partir de données
      └── Deep Learning — réseaux de neurones profonds
           ├── NLP — comprendre/générer le langage
           ├── Vision par ordinateur — interpréter les images
           └── Modèles fondamentaux — pré-entraînés sur corpus massifs
```

| Terme | Définition courte |
|---|---|
| **Machine Learning** | Algorithmes qui apprennent automatiquement à partir de données (supervisé, non supervisé, renforcement) |
| **Deep Learning** | ML basé sur des réseaux de neurones artificiels à plusieurs couches (CNN, RNN, Transformer) |
| **NLP** | Traitement automatique du langage naturel : compréhension, génération, traduction |
| **Vision par ordinateur** | Analyse d'images et vidéos : détection d'objets, reconnaissance faciale, OCR |
| **Modèle fondamental** | Grand modèle pré-entraîné sur données massives, adaptable par fine-tuning (GPT-4, Gemini, LLaMA) |
| **AGI** | IA hypothétique aux capacités cognitives générales équivalentes à l'humain — non atteinte à ce jour |

**Types d'apprentissage ML :**
- **Supervisé** : données étiquetées → classification, régression
- **Non supervisé** : données brutes → clustering, détection d'anomalies
- **Par renforcement** : agent + récompenses → optimisation de décisions (AlphaGo, robotique)

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Automatisation de tâches répétitives | Biais dans les données d'entraînement |
| Détection de patterns invisibles à l'humain | Boîte noire : faible explicabilité (XAI requis) |
| Personnalisation à grande échelle | Coût énergétique et environnemental élevé |
| Disponibilité 24/7, scalabilité | Nécessite des volumes importants de données |
| Amélioration continue avec les données | Risques éthiques, légaux (RGPD, AI Act) |

### Acteurs
- **Big Tech** : OpenAI (GPT-4o), Google DeepMind (Gemini), Meta AI (LLaMA 3), Microsoft (Copilot), Amazon (Bedrock), Mistral AI (Europe)
- **Hardware** : NVIDIA (GPU H100/B200), AMD, Intel
- **Cloud** : AWS SageMaker, Azure AI, Google Vertex AI
- **Régulateurs** : Commission Européenne (AI Act), CNIL (France)

### Cas d'usage
- **Santé** : diagnostic par imagerie médicale (détection cancer), découverte de molécules
- **Finance** : détection de fraude, trading algorithmique, scoring crédit
- **Industrie** : maintenance prédictive, contrôle qualité visuel
- **Marketing** : recommandation, personnalisation, chatbots (voir fiches dédiées)
- **SI/Ops** : AIOps, génération de code (GitHub Copilot)

### Chiffres complémentaires
- 70 % de la valeur IA en entreprise vient du ML supervisé (McKinsey, 2023)
- L'entraînement de GPT-4 a consommé ~50 GWh d'électricité
- 97 M d'emplois nouveaux liés à l'IA d'ici 2025 (WEF) contre 85 M supprimés

---

## Flashcards
#flashcards

Qu'est-ce qui différencie le Deep Learning du Machine Learning classique ? :: Le Deep Learning utilise des réseaux de neurones artificiels à plusieurs couches (profonds) pour apprendre des représentations hiérarchiques des données, sans feature engineering manuel, là où le ML classique nécessite une extraction manuelle des caractéristiques.

Citez les 3 types d'apprentissage en ML avec un exemple chacun. :: Supervisé (données étiquetées) → détection de spam ; Non supervisé → segmentation client ; Renforcement → agent jouant aux échecs (AlphaGo).

Qu'est-ce qu'un modèle fondamental ? :: Un très grand modèle pré-entraîné sur des corpus massifs (texte, images…), capable d'être adapté à de nombreuses tâches par fine-tuning ou prompting (ex : GPT-4, LLaMA 3, Gemini).

Que signifie AGI et est-elle atteinte ? :: Artificial General Intelligence = IA aux capacités cognitives générales équivalentes à l'humain. Non atteinte à ce jour ; les systèmes actuels sont des IA "étroites" (narrow AI) spécialisées par tâche.

Qu'est-ce que le NLP ? Donnez 2 applications concrètes. :: Natural Language Processing : traitement automatique du langage naturel. Applications : chatbots / assistants virtuels, traduction automatique, analyse de sentiment, génération de texte.

Quel cadre réglementaire européen encadre l'IA ? :: L'AI Act (Règlement européen sur l'IA), entré en vigueur en 2024, classe les systèmes IA par niveau de risque (inacceptable, élevé, limité, minimal) et impose des obligations proportionnées.

Quelle est la différence entre IA étroite et AGI ? :: L'IA étroite (narrow AI) est spécialisée sur une ou quelques tâches spécifiques (ex : reconnaissance d'image). L'AGI serait capable de réaliser n'importe quelle tâche cognitive comme un humain, avec transfert de connaissances généralisé.

---

## Sources
- McKinsey Global Institute — *The state of AI in 2024*
- Gartner Hype Cycle for Artificial Intelligence, 2024
- European Commission — AI Act (2024)
- Stanford HAI — *AI Index Report 2024*
- NVIDIA — State of AI Infrastructure, 2024

---

## Notions liées
- [[IA générative et LLM]]
- [[RAG (Retrieval-Augmented Generation)]]
- [[Fine-tuning et prompt engineering]]
- [[AIOps]]
- [[MLOps - DataOps]]
- [[IA et marketing]]
- [[Chatbots et assistants virtuels]]
- [[Métriques marketing et IA]]
