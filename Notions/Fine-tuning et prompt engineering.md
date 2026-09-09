---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 
---

# Fine-tuning et prompt engineering

## En bref

### Définition
Le **fine-tuning** (affinage) consiste à continuer l'entraînement d'un modèle pré-entraîné sur un corpus spécifique pour adapter ses comportements, son style ou ses connaissances à un domaine précis (**transfer learning**). Le **prompt engineering** est l'art de formuler les instructions données au modèle (le prompt) pour obtenir les sorties souhaitées, sans modifier les poids — notamment via les techniques **few-shot** (exemples dans le prompt) et **zero-shot** (instruction directe sans exemples).

### Pourquoi c'est important
Ces deux approches sont les principaux leviers d'adaptation des LLM en entreprise. Le choix entre prompter, fine-tuner ou utiliser le RAG dépend du cas d'usage, du budget et des données disponibles. Un bon prompt engineer peut multiplier par 2 à 5 la qualité des sorties d'un LLM sans aucun coût d'entraînement.

### Chiffres clés
- Coût d'un fine-tuning GPT-3.5 : ~**$0,008/1k tokens** (OpenAI), soit quelques centaines de dollars pour un corpus métier
- Fine-tuning LLaMA 3 (7B) avec LoRA : faisable sur **un GPU A100** en quelques heures
- Le prompt engineering améliore les performances de **20 à 30 %** sur des tâches structurées (benchmarks internes)
- Chain-of-Thought prompting : +**17-40 %** sur les tâches de raisonnement mathématique (Google, 2022)

---

## Approfondir

### Fonctionnement

#### Transfer Learning et Fine-tuning

**Principe du transfer learning :**
Un modèle fondamental (GPT, BERT, LLaMA) a appris des représentations générales du langage lors du pré-entraînement. Le fine-tuning réutilise ces représentations en ne ré-entraînant que les couches supérieures ou en ajustant légèrement tous les poids sur un corpus cible.

**Types de fine-tuning :**

| Type | Description | Ressources | Cas d'usage |
|---|---|---|---|
| **Full fine-tuning** | Ajuste tous les poids du modèle | GPU cluster, très coûteux | Changement comportemental profond |
| **LoRA** (Low-Rank Adaptation) | Injecte des matrices de faible rang, n'ajuste que celles-ci | 1-2 GPU, accessible | Adaptation style/domaine |
| **QLoRA** | LoRA + quantification 4-bit | 1 GPU grand public | Fine-tuning local (LLaMA) |
| **PEFT** | Parameter-Efficient Fine-Tuning (famille) | Variable | Tous cas enterprise |
| **RLHF / RLAIF** | Fine-tuning par feedback humain/IA | Coûteux | Alignement comportemental |

#### Prompt Engineering

**Techniques fondamentales :**

| Technique | Description | Exemple d'usage |
|---|---|---|
| **Zero-shot** | Instruction directe, aucun exemple | "Résume ce texte en 3 points" |
| **Few-shot** | 1 à 10 exemples dans le prompt | Prompt avec 3 exemples de classification |
| **Chain-of-Thought (CoT)** | "Réfléchis étape par étape" | Problèmes mathématiques, raisonnement |
| **System prompt** | Instructions persistantes de contexte/rôle | "Tu es un assistant RH expert en droit français" |
| **Role prompting** | Attribution d'un rôle/persona | "En tant qu'expert cybersécurité…" |
| **RAG prompting** | Contexte documentaire injecté | Voir fiche RAG |
| **Self-consistency** | Génère N réponses, vote majoritaire | Tâches de raisonnement critiques |
| **ReAct** | Alternance Reasoning + Acting (outils) | Agents IA |

**Anatomie d'un bon prompt :**
```
[RÔLE]      Tu es un expert en fiscalité française.
[CONTEXTE]  L'entreprise est une PME de 50 salariés.
[TÂCHE]     Analyse le document suivant et identifie les risques fiscaux.
[FORMAT]    Réponds en JSON avec les champs : risque, niveau (1-3), recommandation.
[EXEMPLES]  (si few-shot) ---
[INPUT]     {document}
```

**Paramètres d'inférence à maîtriser :**
- **Température** (0-2) : 0 = déterministe, 1 = créatif
- **Top-p** : nucleus sampling (0.9 = standard)
- **Max tokens** : longueur maximale de la réponse
- **Frequency/Presence penalty** : réduction des répétitions

### Avantages / Inconvénients

| | Fine-tuning | Prompt Engineering |
|---|---|---|
| **Coût** | Élevé (GPU, données, temps) | Quasi nul |
| **Expertise requise** | MLOps, Data Science | Accessible aux non-développeurs |
| **Résultat** | Comportement intégré, rapide à l'inférence | Dépendant de la qualité du prompt |
| **Flexibilité** | Faible (nécessite re-entraînement si changement) | Très haute |
| **Données nécessaires** | Oui (centaines à milliers d'exemples) | Non |
| **Hallucinations** | Réduites mais pas éliminées | Persiste (combiner avec RAG) |
| **Idéal pour** | Style maison, format spécifique, domaine très fermé | Prototypage, tâches générales, itération rapide |

### Acteurs
- **Frameworks fine-tuning** : Hugging Face (PEFT, TRL), Axolotl, Unsloth (QLoRA)
- **Plateformes cloud** : OpenAI Fine-tuning API, Azure AI Studio, Google Vertex AI, Amazon Bedrock
- **Outils de prompt** : PromptFlow (Microsoft), LangSmith, PromptLayer
- **Recherche** : Google Brain (CoT), Anthropic (Constitutional AI), Meta FAIR

### Cas d'usage
- **Fine-tuning** : chatbot médical adapté à la terminologie clinique, générateur de code dans le style interne de l'entreprise, modèle de classification de tickets support
- **Prompt engineering** : extraction d'informations structurées depuis des e-mails, analyse de sentiment, génération d'annonces marketing, traduction avec ton spécifique

### Chiffres complémentaires
- LoRA réduit le nombre de paramètres entraînables de **10 000x** (r=8, LLaMA 7B)
- OpenAI fine-tuning GPT-4o mini : disponible depuis août 2024
- Un dataset de **500 à 2 000 exemples** suffit pour un fine-tuning spécialisé de qualité

---

## Flashcards
#flashcards/IA/Fine_tuning_et_prompt_engineering

Qu'est-ce que le transfer learning appliqué aux LLM ? :: Le transfer learning consiste à réutiliser les représentations apprises par un grand modèle pré-entraîné (GPT, LLaMA) et à les adapter à une tâche spécifique via fine-tuning, en économisant massivement les ressources par rapport à un entraînement from scratch.

Quelle est la différence entre zero-shot et few-shot prompting ? :: Zero-shot : instruction directe sans exemple ("Classe ce texte comme positif ou négatif"). Few-shot : on fournit 1 à N exemples entrée/sortie dans le prompt avant la question cible, ce qui guide le modèle sur le format et la tâche attendus.

Qu'est-ce que LoRA et quel est son avantage ? :: LoRA (Low-Rank Adaptation) est une technique de fine-tuning qui injecte de petites matrices de faible rang dans les couches du modèle, n'entraînant que ces matrices (<<1 % des paramètres totaux). Avantage : réduit de >99 % les ressources nécessaires vs full fine-tuning tout en atteignant des performances comparables.

Citez 4 éléments constitutifs d'un prompt efficace. :: Rôle/persona (contexte du modèle), tâche précise, format de sortie attendu (JSON, liste…), exemples (few-shot), et contraintes éventuelles (longueur, langue, ton).

Qu'est-ce que le Chain-of-Thought prompting ? :: Technique consistant à demander au modèle de "raisonner étape par étape" avant de donner sa réponse finale. Améliore significativement les performances sur les tâches de raisonnement complexe, mathématique ou logique.

Quand préférer le fine-tuning au prompt engineering ? :: Le fine-tuning est préférable quand : le comportement doit être systématique (pas oublié entre les sessions), le style/format est très spécifique, les données d'entraînement existent, et la tâche est répétée à grande échelle. Le prompt engineering suffit pour le prototypage et les tâches générales.

Qu'est-ce que le RLHF ? :: Reinforcement Learning from Human Feedback : méthode d'alignement où des annotateurs humains classent les réponses du modèle, entraînant un modèle de récompense qui guide ensuite l'optimisation du LLM via PPO, pour produire des réponses plus utiles et alignées.

---

## Sources
- Hu et al. — *LoRA: Low-Rank Adaptation of Large Language Models*, Microsoft (2021)
- Wei et al. — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*, Google (2022)
- OpenAI — Fine-tuning documentation (2024)
- Anthropic — Prompt Engineering Guide (2024)
- Hugging Face — PEFT Documentation

---

## Notions liées
- [[Intelligence Artificielle — fondamentaux]]
- [[IA générative et LLM]]
- [[RAG (Retrieval-Augmented Generation)]]
- [[MLOps - DataOps]]
