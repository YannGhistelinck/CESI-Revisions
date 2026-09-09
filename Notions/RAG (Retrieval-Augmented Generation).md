---
type: notion
thèmes:
  - IA
statut: pas vu
dernière_révision: 
---

# RAG (Retrieval-Augmented Generation)

## En bref

### Définition
Le **RAG** (Retrieval-Augmented Generation) est une architecture qui augmente un LLM en lui fournissant, au moment de l'inférence, des documents pertinents extraits d'une base de connaissances externe. Le modèle génère sa réponse en se basant sur ces documents récupérés (**grounding**), ce qui réduit drastiquement les **hallucinations** et permet au LLM d'accéder à des informations récentes ou propriétaires sans nécessiter de re-entraînement.

### Pourquoi c'est important
Le RAG est la réponse pragmatique aux deux limitations majeures des LLM : les hallucinations et la péremption des connaissances (cutoff date). Il permet de déployer des assistants IA sur des bases documentaires d'entreprise (intranets, bases légales, documentations techniques) tout en gardant le contrôle sur les sources. C'est l'architecture dominante pour les chatbots d'entreprise en 2024.

### Chiffres clés
- Réduction des hallucinations : jusqu'à **60 %** avec un RAG bien configuré vs LLM seul (études Microsoft/Meta)
- Adoption : **80 % des projets LLM en entreprise** intègrent une forme de RAG (Gartner, 2024)
- Latence ajoutée par le RAG : typiquement **200-800 ms** pour la phase de retrieval
- Coût : 3 à 10x moins cher qu'un fine-tuning complet pour adapter un LLM à un corpus métier

---

## Approfondir

### Fonctionnement

**Pipeline RAG en 5 étapes :**

```
[Question utilisateur]
        ↓
1. EMBEDDING de la question → vecteur
        ↓
2. RECHERCHE vectorielle dans la base (top-k documents pertinents)
        ↓
3. CONSTRUCTION du prompt : [contexte récupéré] + [question]
        ↓
4. GÉNÉRATION par le LLM à partir du prompt augmenté
        ↓
5. RÉPONSE ancrée sur les sources (avec citations possibles)
```

**Composants clés :**

| Composant | Rôle | Exemples d'outils |
|---|---|---|
| **Embedding model** | Convertit texte → vecteur sémantique | text-embedding-ada-002 (OpenAI), E5, BGE |
| **Vector store** | Stocke et indexe les vecteurs | Pinecone, Weaviate, ChromaDB, pgvector |
| **Retriever** | Trouve les k documents les plus proches | Similarité cosinus, BM25, hybride |
| **LLM** | Génère la réponse finale | GPT-4o, Claude, Mistral, LLaMA |
| **Orchestrateur** | Coordonne le pipeline | LangChain, LlamaIndex, Haystack |

**RAG vs alternatives :**

| Approche | Quand l'utiliser | Avantage | Inconvénient |
|---|---|---|---|
| **RAG** | Corpus volumineux, informations évolutives | Pas de re-entraînement, sources citables | Pipeline complexe, latence |
| **Fine-tuning** | Style/format spécifique, connaissances stables | Connaissance intégrée, latence faible | Coûteux, hallucinations persistantes |
| **Contexte long** | Corpus < 1M tokens, one-shot | Simple | Coûteux à chaque appel, bruit |
| **RAG + Fine-tuning** | Cas complexes en production | Complémentarité | Complexité maximale |

**Variantes avancées :**
- **RAG hybride** : combine recherche vectorielle (sémantique) + BM25 (lexicale)
- **RAG avec reranking** : un modèle cross-encoder re-classe les documents récupérés
- **Agentic RAG** : l'agent décide quand et comment requêter la base
- **GraphRAG** (Microsoft) : combine graphe de connaissances + RAG pour raisonnement multi-hop

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Réduit les hallucinations (grounding sur sources) | Pipeline plus complexe à maintenir |
| Accès à des informations récentes/propriétaires | Qualité dépendante du retrieval (garbage in, garbage out) |
| Traçabilité : réponses citant leurs sources | Latence supplémentaire (retrieval + génération) |
| Pas de re-entraînement coûteux | Chunking et indexation requièrent une expertise |
| Mise à jour de la base sans toucher au modèle | Risque de retrieval pertinent mais mal interprété |
| Confidentialité (données restent en interne) | Coût des embeddings et du vector store |

### Acteurs
- **Frameworks** : LangChain, LlamaIndex, Haystack, Semantic Kernel (Microsoft)
- **Vector stores** : Pinecone, Weaviate, Qdrant, ChromaDB, Milvus, pgvector (PostgreSQL)
- **Embedding models** : OpenAI (ada-002, text-3), Cohere, HuggingFace (BGE, E5)
- **Solutions clés en main** : Azure AI Search + OpenAI, Amazon Kendra + Bedrock, Vertex AI Search

### Cas d'usage
- **Support client** : chatbot répondant sur la base de la documentation produit
- **Juridique/conformité** : assistant interrogeant des contrats, textes réglementaires (RGPD, NIS2)
- **RH** : assistant RH sur les politiques internes, conventions collectives
- **IT/Support** : chatbot interrogeant runbooks, base de connaissances ITSM
- **Finance** : analyse de rapports financiers, extraction d'informations de prospectus

### Chiffres complémentaires
- Chunking optimal : **512-1024 tokens** avec overlap de 10-20 %
- Top-k recommandé : entre **3 et 10** documents selon la tâche
- Précision du retrieval (Hit Rate@5) : 70-90 % sur corpus bien structuré

---

## Flashcards
#flashcards/IA/RAG_Retrieval_Augmented_Generation

Qu'est-ce que le RAG et à quel problème répond-il ? :: Le RAG (Retrieval-Augmented Generation) est une architecture qui enrichit le prompt d'un LLM avec des documents récupérés en temps réel depuis une base de connaissances. Il répond aux hallucinations et à la péremption des connaissances des LLM.

Décrivez les 4 étapes principales d'un pipeline RAG. :: 1) Embedding de la question en vecteur. 2) Recherche des k documents les plus proches dans le vector store. 3) Construction du prompt avec les documents récupérés + question. 4) Génération de la réponse par le LLM à partir du prompt augmenté.

Qu'est-ce qu'un vector store ? Donnez 3 exemples. :: Base de données spécialisée dans le stockage et la recherche de vecteurs d'embeddings via similarité cosinus. Exemples : Pinecone, Weaviate, ChromaDB, pgvector (PostgreSQL), Qdrant.

Quelle est la différence entre RAG et fine-tuning ? :: Le RAG injecte des informations au moment de l'inférence sans modifier le modèle (adapté aux données évolutives). Le fine-tuning ajuste les poids du modèle sur un corpus spécifique (adapté au style ou aux connaissances stables), mais reste coûteux et ne garantit pas l'élimination des hallucinations.

Qu'est-ce que le grounding dans le contexte du RAG ? :: Le grounding est le fait d'ancrer les réponses du LLM sur des sources documentaires réelles récupérées, rendant les réponses vérifiables et réduisant les hallucinations. Les sources peuvent être citées dans la réponse finale.

Qu'est-ce que le RAG hybride ? :: Combinaison de la recherche vectorielle (sémantique, basée sur embeddings) et de la recherche lexicale BM25 (basée sur les mots-clés), permettant de récupérer des documents à la fois sémantiquement proches et lexicalement pertinents.

---

## Sources
- Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, Meta AI (2020)
- Microsoft Research — GraphRAG (2024)
- LangChain Documentation — RAG best practices
- Gartner — Top Strategic Technology Trends 2024
- AWS — RAG Architecture Patterns (2024)

---

## Notions liées
- [[Intelligence Artificielle — fondamentaux]]
- [[IA générative et LLM]]
- [[Fine-tuning et prompt engineering]]
- [[MLOps - DataOps]]
- [[Chatbots et assistants virtuels]]
