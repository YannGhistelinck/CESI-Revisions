---
type: notion
thèmes:
  - IA
  - Big DATA
statut: pas vu
dernière_révision: 
---

# IA générative et LLM

## En bref

### Définition
L'**IA générative** désigne les systèmes capables de produire des contenus originaux (texte, image, audio, code, vidéo) à partir d'un entraînement sur de vastes corpus. Les **LLM** (Large Language Models) en sont la forme la plus répandue : des modèles de langage à plusieurs centaines de milliards de paramètres, basés sur l'architecture **Transformer**, entraînés à prédire le token suivant dans une séquence. L'**hallucination** est leur défaut structurel majeur : ils génèrent des affirmations plausibles mais fausses.

### Pourquoi c'est important
Les LLM ont déclenché une rupture technologique en 2022-2023 (ChatGPT, GPT-4, Gemini). Ils transforment la productivité (génération de code, rédaction, synthèse), mais introduisent de nouveaux risques (désinformation, hallucinations, coût carbone). Pour le SI, ils sont le socle des nouvelles applications IA (RAG, agents, copilots).

### Chiffres clés
- GPT-4 : ~**1 800 Md de paramètres** (estimation, non confirmé par OpenAI)
- Marché de l'IA générative : **67 Md$ en 2024** → **1 300 Md$ attendus en 2032**
- ChatGPT dépasse **200 millions d'utilisateurs hebdomadaires** (2024)
- Taux d'hallucination des LLM : entre **3 % et 27 %** selon les benchmarks et domaines

---

## Approfondir

### Fonctionnement

**Architecture Transformer (2017, Google — "Attention is All You Need") :**
- Mécanisme d'**attention** : pondère l'importance de chaque token par rapport aux autres dans le contexte
- Traitement **parallèle** (vs RNN séquentiel) → scalabilité massive
- **Token** : unité de traitement (~0,75 mot en moyenne)

**Pipeline d'entraînement d'un LLM :**
1. **Pré-entraînement** : corpus massif (web, livres, code) → prédiction du token suivant
2. **Fine-tuning supervisé (SFT)** : exemples de conversations de qualité
3. **RLHF** (Reinforcement Learning from Human Feedback) : alignement sur les préférences humaines
4. **Inférence** : génération token par token via sampling (température, top-p)

**Types de génération IA :**

| Type | Modèles | Sortie |
|---|---|---|
| Texte | GPT-4o, Gemini, LLaMA 3, Mistral | Texte, code |
| Image | DALL-E 3, Midjourney, Stable Diffusion | Images |
| Audio | Whisper, ElevenLabs, MusicGen | Audio, parole |
| Vidéo | Sora (OpenAI), Runway | Vidéo |
| Code | GitHub Copilot, Codestral | Code |
| Multimodal | GPT-4o, Gemini 1.5 Pro | Texte + image + audio |

**Hallucination — causes et conséquences :**
- Cause : le modèle optimise la vraisemblance statistique, pas la vérité factuelle
- Facteurs aggravants : questions hors distribution d'entraînement, dates récentes
- Conséquences : désinformation, erreurs médicales/juridiques, perte de confiance
- Remèdes : RAG, grounding, fact-checking, température basse

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Génération de contenu à grande vitesse | Hallucinations — fiabilité factuelle non garantie |
| Polyvalence multi-tâches (texte, code, analyse) | Coût d'entraînement et d'inférence très élevé |
| Interface en langage naturel (accessibilité) | Biais issus des données d'entraînement |
| Accélération de la productivité (+30-40 % estimés) | Opacité : boîte noire difficile à auditer |
| Amélioration continue (RLHF, feedback) | Risques légaux (droits d'auteur, RGPD) |
| Personnalisable par fine-tuning ou RAG | Consommation énergétique importante |

### Acteurs
- **Propriétaires** : OpenAI (GPT-4o, o1), Google (Gemini 1.5 Pro/Flash), Anthropic (Claude 3.5), Microsoft (Copilot/Azure OpenAI), Amazon (Titan/Bedrock)
- **Open-source** : Meta (LLaMA 3), Mistral AI (Mistral Large, Mixtral), Falcon (TII)
- **Infrastructure** : NVIDIA (GPU), Hugging Face (hub de modèles), LangChain (orchestration)

### Cas d'usage
- **Entreprise** : génération de rapports, résumé de réunions, rédaction d'e-mails
- **Développement** : GitHub Copilot (complétion de code), génération de tests, documentation
- **Marketing** : création de contenu, A/B testing de textes, personnalisation
- **Support client** : chatbots avancés (voir fiche Chatbots)
- **Recherche** : synthèse bibliographique, génération d'hypothèses

### Chiffres complémentaires
- 75 % des travailleurs du savoir utilisent des outils IA générative (Microsoft, 2024)
- Réduction de 55 % du temps de rédaction de code avec GitHub Copilot (GitHub, 2023)
- Contexte window : GPT-4o = 128k tokens, Gemini 1.5 Pro = **1 M tokens**

---

## Flashcards
#flashcards/IA/IA_générative_et_LLM #flashcards/Big_DATA/IA_générative_et_LLM

Qu'est-ce qu'un LLM et sur quelle architecture repose-t-il ? :: Un Large Language Model est un modèle de langage à très grande échelle (milliards de paramètres) basé sur l'architecture Transformer (2017). Il prédit le token suivant dans une séquence, entraîné sur des corpus massifs de texte.

Qu'est-ce que l'hallucination dans un LLM ? Citez 2 remèdes. :: L'hallucination est la génération d'informations plausibles mais factuellement incorrectes, car le modèle optimise la vraisemblance statistique plutôt que la vérité. Remèdes : RAG (ancrage sur des sources externes), réduction de la température, grounding, fact-checking humain.

Qu'est-ce que le RLHF ? :: Reinforcement Learning from Human Feedback : technique d'alignement où des évaluateurs humains notent les réponses du modèle, permettant d'entraîner un modèle de récompense qui guide le LLM vers des réponses plus utiles, honnêtes et inoffensives.

Quelle est la différence entre un LLM propriétaire et open-source ? Donnez 2 exemples de chaque. :: Propriétaire : poids non accessibles, accès via API payante (GPT-4o d'OpenAI, Gemini de Google). Open-source : poids téléchargeables librement, déployables localement (LLaMA 3 de Meta, Mistral de Mistral AI).

Qu'est-ce que le mécanisme d'attention dans un Transformer ? :: L'attention permet au modèle de pondérer dynamiquement l'importance de chaque token du contexte par rapport aux autres pour générer le token suivant. Cela lui permet de capturer des dépendances longue distance dans le texte.

Citez 3 types de contenu que peut générer l'IA générative. :: Texte (GPT-4o), images (DALL-E 3, Midjourney), code (GitHub Copilot), audio (ElevenLabs), vidéo (Sora), musique (MusicGen).

Quelle est la différence entre température et top-p dans la génération de texte ? :: La température contrôle la créativité : haute → réponses variées/créatives, basse → réponses déterministes/précises. Le top-p (nucleus sampling) limite le tirage aux tokens dont la probabilité cumulée atteint p, évitant les tokens très improbables.

---

## Sources
- Vaswani et al. — *Attention is All You Need*, Google Brain (2017)
- OpenAI — GPT-4 Technical Report (2023)
- Gartner — Market Guide for Generative AI, 2024
- GitHub — *The economic impact of the AI coding assistant* (2023)
- Microsoft Work Trend Index 2024

---

## Notions liées
- [[Intelligence Artificielle — fondamentaux]]
- [[RAG (Retrieval-Augmented Generation)]]
- [[Fine-tuning et prompt engineering]]
- [[Chatbots et assistants virtuels]]
- [[MLOps - DataOps]]
