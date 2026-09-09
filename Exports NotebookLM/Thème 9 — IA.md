# Intelligence Artificielle — Guide de révision complet

## Introduction

L'intelligence artificielle est la technologie transversale du XXIe siècle : elle restructure tous les secteurs, redéfinit les métiers des systèmes d'information et constitue un enjeu stratégique majeur pour les entreprises comme pour les États. Ce guide couvre l'ensemble des notions du thème, des fondements techniques aux enjeux éthiques et réglementaires, en passant par les applications marketing, les opérations informatiques et les nouvelles formes de déploiement embarqué. Il est conçu pour une lecture à voix haute, sans tableaux, avec des phrases complètes et des acronymes systématiquement développés.

---

## Notions clés à maîtriser

### Intelligence Artificielle — Fondamentaux

En bref : l'intelligence artificielle désigne l'ensemble des techniques permettant à une machine de simuler des capacités cognitives humaines — raisonnement, apprentissage, perception, compréhension du langage. Elle recouvre plusieurs sous-domaines emboîtés : le machine learning, ou apprentissage automatique, le deep learning, ou apprentissage profond, le traitement automatique du langage naturel, et la vision par ordinateur.

Le machine learning regroupe des algorithmes qui apprennent automatiquement à partir de données. Il existe trois grandes familles d'apprentissage. L'apprentissage supervisé utilise des données étiquetées pour des tâches de classification ou de régression, par exemple la détection de spam. L'apprentissage non supervisé travaille sur des données brutes pour découvrir des structures cachées, par exemple la segmentation de clients. L'apprentissage par renforcement place un agent dans un environnement et le guide par des récompenses, comme dans AlphaGo ou la robotique.

Le deep learning est une sous-branche du machine learning qui utilise des réseaux de neurones artificiels à plusieurs couches. Ces réseaux apprennent des représentations hiérarchiques des données sans nécessiter d'extraction manuelle de caractéristiques. Ils sont à la base des modèles fondamentaux, c'est-à-dire de très grands modèles pré-entraînés sur des corpus massifs, adaptables à de nombreuses tâches par fine-tuning ou par prompting. GPT-4, Gemini et LLaMA 3 sont des exemples de modèles fondamentaux.

L'intelligence artificielle générale, souvent désignée par le sigle AGI pour Artificial General Intelligence, désigne une intelligence artificielle hypothétique aux capacités cognitives équivalentes à celles d'un humain pour n'importe quelle tâche. Elle n'est pas atteinte à ce jour : tous les systèmes actuels sont des intelligences artificielles dites étroites, spécialisées sur une ou quelques tâches précises.

Chiffres à retenir : le marché mondial de l'intelligence artificielle représentait 184 milliards de dollars en 2024 et devrait atteindre environ 826 milliards de dollars en 2030, avec une croissance annuelle de 27 pour cent. ChatGPT a atteint 100 millions d'utilisateurs en deux mois, un record historique d'adoption. L'entraînement de GPT-4 a consommé environ 50 gigawattheures d'électricité. Soixante-dix pour cent de la valeur créée par l'intelligence artificielle en entreprise provient du machine learning supervisé selon McKinsey.


### Intelligence Artificielle Générative et Grands Modèles de Langage

En bref : l'intelligence artificielle générative désigne les systèmes capables de produire des contenus originaux — texte, image, audio, code, vidéo — à partir d'un entraînement sur de vastes corpus. Les grands modèles de langage, souvent désignés par le sigle LLM pour Large Language Models, en sont la forme la plus répandue. Ils s'appuient sur l'architecture Transformer, publiée par Google en 2017 sous le titre "Attention is All You Need". Ces modèles comprennent des centaines de milliards de paramètres et sont entraînés à prédire le token suivant dans une séquence, un token étant une unité de traitement représentant environ trois quarts de mot en moyenne.

Le mécanisme d'attention est au cœur de l'architecture Transformer : il permet au modèle de pondérer dynamiquement l'importance de chaque token du contexte par rapport aux autres pour générer le token suivant. Cela permet de capturer des dépendances longue distance dans le texte et de traiter les séquences en parallèle, contrairement aux réseaux récurrents qui travaillaient de façon séquentielle.

Le pipeline d'entraînement d'un grand modèle de langage comprend quatre étapes. D'abord le pré-entraînement sur un corpus massif — web, livres, code — par prédiction du token suivant. Ensuite un fine-tuning supervisé sur des exemples de conversations de qualité. Puis l'apprentissage par renforcement à partir des retours humains, désigné par le sigle RLHF pour Reinforcement Learning from Human Feedback, qui aligne le modèle sur les préférences humaines. Enfin l'inférence, c'est-à-dire la génération token par token, avec des paramètres comme la température et le top-p qui contrôlent la créativité et la précision des réponses.

L'hallucination est le défaut structurel majeur des grands modèles de langage : ils génèrent des affirmations plausibles mais factuellement incorrectes, car ils optimisent la vraisemblance statistique et non la vérité. Le taux d'hallucination oscille entre 3 et 27 pour cent selon les benchmarks et les domaines. Les principaux remèdes sont la technique RAG que nous détaillerons plus bas, la réduction de la température, le grounding sur des sources vérifiées et la vérification humaine.

On distingue les modèles propriétaires, dont les poids ne sont pas accessibles et qui s'utilisent via des interfaces de programmation payantes — GPT-4o d'OpenAI, Gemini de Google, Claude d'Anthropic — et les modèles open source dont les poids sont téléchargeables librement — LLaMA 3 de Meta, Mistral de Mistral AI.

Chiffres à retenir : le marché de l'intelligence artificielle générative représentait 67 milliards de dollars en 2024 et devrait dépasser 1 300 milliards de dollars en 2032. ChatGPT compte plus de 200 millions d'utilisateurs hebdomadaires en 2024. Soixante-quinze pour cent des travailleurs du savoir utilisent des outils d'intelligence artificielle générative selon Microsoft.


### RAG — La Génération Augmentée par la Récupération

En bref : le RAG, sigle de Retrieval-Augmented Generation, est une architecture qui augmente un grand modèle de langage en lui fournissant, au moment de la génération de la réponse, des documents pertinents extraits d'une base de connaissances externe. Le modèle génère sa réponse en s'ancrant sur ces documents récupérés, ce que l'on appelle le grounding, ce qui réduit drastiquement les hallucinations et permet d'accéder à des informations récentes ou propriétaires sans re-entraîner le modèle.

Le pipeline du RAG fonctionne en cinq étapes. Premièrement, la question de l'utilisateur est convertie en un vecteur numérique appelé embedding, qui capture son sens sémantique. Deuxièmement, ce vecteur est comparé par similarité cosinus aux vecteurs de tous les documents stockés dans une base vectorielle. Troisièmement, les documents les plus pertinents sont récupérés. Quatrièmement, ces documents sont injectés dans le prompt du modèle aux côtés de la question originale. Cinquièmement, le modèle génère une réponse ancrée sur les sources, qu'il peut citer explicitement.

Il existe des variantes avancées du RAG. Le RAG hybride combine la recherche vectorielle sémantique et la recherche lexicale classique de type BM25. Le RAG avec reranking utilise un modèle croisé pour re-classer les documents récupérés avant de les injecter dans le prompt. L'Agentic RAG laisse un agent décider quand et comment interroger la base. Le GraphRAG de Microsoft combine un graphe de connaissances avec le RAG pour des raisonnements multi-étapes.

La différence fondamentale entre RAG et fine-tuning est la suivante : le RAG injecte des informations au moment de l'inférence sans modifier les poids du modèle, ce qui est adapté aux données évolutives et préserve la traçabilité des sources. Le fine-tuning ajuste les poids du modèle sur un corpus spécifique, ce qui est adapté pour inculquer un style ou des connaissances stables, mais il est coûteux et ne garantit pas l'élimination des hallucinations. Les deux peuvent aussi être combinés pour les cas d'usage les plus exigeants.

Chiffres à retenir : un RAG bien configuré réduit les hallucinations jusqu'à 60 pour cent par rapport à un modèle seul. Quatre-vingts pour cent des projets de grands modèles de langage en entreprise intègrent une forme de RAG selon Gartner en 2024. Le coût d'un RAG est trois à dix fois inférieur à celui d'un fine-tuning complet pour adapter un modèle à un corpus métier.


### Fine-Tuning et Prompt Engineering

En bref : le fine-tuning, ou affinage en français, consiste à continuer l'entraînement d'un modèle pré-entraîné sur un corpus spécifique pour adapter ses comportements, son style ou ses connaissances à un domaine précis. C'est une application du transfer learning : le modèle fondamental a déjà appris des représentations générales du langage, et l'affinage réutilise ces représentations en les spécialisant. Le prompt engineering est l'art de formuler les instructions données au modèle — le prompt — pour obtenir les sorties souhaitées, sans modifier les poids du modèle.

Les principales techniques de fine-tuning sont les suivantes. Le fine-tuning complet ajuste tous les poids du modèle et nécessite de nombreux processeurs graphiques et beaucoup de données. Le LoRA, qui signifie Low-Rank Adaptation, injecte de petites matrices de faible rang dans les couches du modèle et n'entraîne que ces matrices, représentant moins de un pour cent des paramètres totaux, avec des performances comparables au fine-tuning complet. Le QLoRA combine LoRA avec une quantification sur 4 bits, rendant le fine-tuning faisable sur un seul processeur graphique grand public.

Les principales techniques de prompt engineering sont les suivantes. Le prompting zéro-shot donne une instruction directe sans exemple. Le prompting few-shot fournit de un à dix exemples dans le prompt pour guider le modèle sur le format et la tâche attendus. Le Chain-of-Thought, ou chaîne de raisonnement, demande au modèle de raisonner étape par étape avant de répondre, ce qui améliore de 17 à 40 pour cent les performances sur des tâches de raisonnement mathématique selon Google en 2022. Le system prompt donne des instructions persistantes de rôle et de contexte au modèle. Le self-consistency génère plusieurs réponses et prend la réponse majoritaire pour les tâches critiques.

Un bon prompt efficace contient généralement cinq éléments : un rôle ou persona donné au modèle, une tâche précise, le format de sortie attendu comme un fichier JSON ou une liste structurée, des exemples si l'on est en mode few-shot, et les contraintes éventuelles en termes de longueur ou de langue.

Pour choisir entre fine-tuning et prompt engineering : le prompt engineering convient au prototypage rapide, aux tâches générales et à l'itération, car il est quasi gratuit et accessible aux non-développeurs. Le fine-tuning est préférable quand le comportement doit être systématique et reproductible, quand le style est très spécifique à l'organisation, quand les données d'entraînement existent et quand la tâche est répétée à très grande échelle.

Chiffres à retenir : le fine-tuning de LLaMA 3 avec LoRA est réalisable sur un seul processeur graphique A100 en quelques heures. Un dataset de 500 à 2 000 exemples suffit pour un fine-tuning spécialisé de qualité. Le prompt engineering améliore les performances de 20 à 30 pour cent sur des tâches structurées selon des benchmarks internes.


### AIOps — L'Intelligence Artificielle pour les Opérations Informatiques

En bref : l'AIOps, sigle de Artificial Intelligence for IT Operations, désigne l'application de l'intelligence artificielle et du machine learning à la gestion et l'exploitation des systèmes d'information. L'objectif est d'automatiser la détection d'anomalies, la corrélation d'événements, le diagnostic et la remédiation des incidents. Cela se concrétise par des capacités d'auto-réparation de l'infrastructure, appelée self-healing infrastructure, de jumeaux numériques du système d'information, et de provisionnement sans intervention humaine, appelé Zero-Touch Provisioning. Le tout progresse vers des niveaux d'autonomie croissants.

Les niveaux d'autonomie de l'intelligence artificielle dans les opérations informatiques sont analogues aux niveaux de conduite autonome. Au niveau zéro, tout est manuel. Au niveau un, les outils de monitoring génèrent des alertes mais l'action reste humaine. Au niveau deux, l'intelligence artificielle détecte les anomalies et suggère des actions que l'humain exécute. Au niveau trois, l'intelligence artificielle exécute des remédiations pré-approuvées pendant que l'humain supervise. Au niveau quatre, l'intelligence artificielle gère la majorité des incidents en autonomie et l'humain n'intervient que sur les exceptions. Au niveau cinq, le système d'information est totalement auto-géré, l'humain définissant uniquement les objectifs. La plupart des entreprises avancées se situent au niveau deux ou trois en 2024.

Le self-healing, ou auto-réparation, fonctionne ainsi : le système détecte automatiquement une anomalie, comme un pod Kubernetes en état d'échec en boucle, en identifie la cause — mémoire insuffisante, configuration incorrecte, dépendance défaillante — puis applique une remédiation automatique comme un redémarrage, une mise à l'échelle ou un rollback, avant d'apprendre ce pattern pour prévenir les occurrences futures.

Le jumeau numérique d'infrastructure est une réplique virtuelle du système d'information comprenant sa topologie, ses dépendances et ses configurations. Il permet de simuler l'impact de changements avant leur application en production et de détecter les dérives de configuration par comparaison avec le référentiel.

Le Zero-Touch Provisioning permet à un équipement réseau ou serveur de se configurer automatiquement au démarrage sans intervention humaine, en récupérant sa configuration depuis un serveur central. Il réduit le temps de déploiement réseau de plusieurs jours à quelques minutes.

Chiffres à retenir : le marché de l'AIOps représentait environ 21 milliards de dollars en 2024 avec une croissance annuelle de 33 pour cent jusqu'en 2030. L'AIOps réduit le temps moyen de réparation, ou MTTR pour Mean Time To Repair, de 50 à 75 pour cent. Il réduit le bruit d'alertes de 70 à 90 pour cent. Le retour sur investissement moyen est de 200 à 350 pour cent sur trois ans selon Forrester.


### MLOps et DataOps — L'Industrialisation de l'Intelligence Artificielle

En bref : le MLOps, sigle de Machine Learning Operations, est l'ensemble des pratiques, outils et processus qui industrialisent le cycle de vie des modèles de machine learning — du développement au déploiement, en passant par le monitoring et le ré-entraînement. Le DataOps applique les principes DevOps aux pipelines de données pour garantir leur qualité, disponibilité et fiabilité. Les deux sont interdépendants : sans DataOps, pas de MLOps robuste.

Le cycle de vie MLOps comprend huit étapes qui forment une boucle continue : la définition du problème, la collecte et préparation des données relevant du DataOps, l'ingénierie des variables et l'expérimentation, l'entraînement du modèle, l'évaluation et la validation, le déploiement ou serving, le monitoring des performances et de la dérive, et enfin le ré-entraînement si une dérive est détectée.

La dérive des modèles est un phénomène clé à surveiller. La dérive des données, ou data drift, survient quand la distribution des données d'entrée change dans le temps. La dérive conceptuelle, ou concept drift, apparaît quand la relation entre les variables d'entrée et la variable cible change, par exemple les comportements d'achat post-pandémie versus avant. La dérive du modèle est la dégradation progressive des performances mesurables. Sans monitoring, un modèle dérive en moyenne au bout de trois à six mois.

Les stratégies de déploiement des modèles incluent le déploiement bleu-vert avec basculement instantané et rollback immédiat, le déploiement canary qui dirige cinq à dix pour cent du trafic vers le nouveau modèle pour tester sans risque massif, le déploiement shadow où le nouveau modèle tourne en parallèle sans que ses résultats soient utilisés, et les tests A/B qui comparent deux modèles sur des populations distinctes pour mesurer l'impact business.

Un Feature Store est une base de données centralisée qui stocke, gère et sert les variables, appelées features, utilisées pour l'entraînement et l'inférence des modèles. Il garantit la cohérence entre la phase d'entraînement et la phase de production, et permet la réutilisabilité des variables entre plusieurs projets.

Chiffres à retenir : 87 pour cent des projets de machine learning n'atteignent jamais la production selon VentureBeat. Le marché du MLOps devrait passer de 4,5 milliards de dollars en 2024 à 75 milliards en 2033, avec une croissance annuelle de 43 pour cent. Soixante pour cent du temps d'un data scientist est consacré à la préparation des données selon IBM.


### Intelligence Artificielle et Marketing

En bref : l'intelligence artificielle transforme le marketing en rendant possible l'hyper-personnalisation à l'échelle individuelle, l'automatisation des campagnes, la recommandation algorithmique et le ciblage publicitaire en temps réel. Le marketing prédictif anticipe les comportements futurs des clients — achat, résiliation, réponse à une offre — en s'appuyant sur des algorithmes de machine learning entraînés sur des données historiques.

L'hyper-personnalisation se distingue de la segmentation traditionnelle de la façon suivante. La segmentation regroupe des clients en catégories et leur envoie le même message. La personnalisation adapte le message au profil individuel. L'hyper-personnalisation adapte le message, l'offre et le canal en temps réel au contexte et au comportement de chaque individu — par exemple une notification push envoyée au moment précis où un client passe devant un magasin physique.

Le marketing automation consiste à automatiser des workflows marketing déclenchés par des événements comportementaux : la séquence de bienvenue envoyée à l'inscription, le rappel d'abandon de panier une heure, vingt-quatre heures et soixante-douze heures après l'abandon, la campagne de réengagement si le client est inactif depuis un certain nombre de jours, ou encore les contenus adaptés au score de maturité du prospect dans son parcours d'achat.

La recommandation algorithmique fonctionne selon trois approches principales. Le filtrage collaboratif recommande des contenus ou produits appréciés par des utilisateurs ayant un profil similaire, comme Netflix et Spotify. Le filtrage basé sur le contenu recommande des items similaires à ce que l'utilisateur a déjà aimé, en se basant sur les attributs du contenu, comme YouTube. L'approche hybride combine les deux, comme Amazon ou Booking.com.

La plateforme de données client, souvent désignée par le sigle CDP pour Customer Data Platform, unifie toutes les données client — comportementales, transactionnelles, offline — en un profil temps réel pour l'activation marketing. Elle se distingue du CRM qui gère les interactions commerciales : le CDP sert à personnaliser et activer les communications, le CRM à gérer la relation commerciale au sens large.

Le programmatic advertising et le Real-Time Bidding permettent à un annonceur d'acheter de l'espace publicitaire personnalisé en temps réel, en moins de cent millisecondes : l'utilisateur charge une page, le fournisseur d'espace envoie une enchère aux acheteurs potentiels, chacun évalue l'utilisateur avec ses modèles d'intelligence artificielle, le plus offrant remporte l'espace et la publicité personnalisée s'affiche.

Chiffres à retenir : 71 pour cent des consommateurs attendent une expérience personnalisée selon McKinsey. Les entreprises avec personnalisation avancée génèrent 40 pour cent de revenus supplémentaires. La recommandation par intelligence artificielle génère 35 pour cent du chiffre d'affaires d'Amazon et 80 pour cent des contenus visionnés sur Netflix. Le programmatic représente environ 90 pour cent des achats publicitaires digitaux en 2024.


### Chatbots et Assistants Virtuels

En bref : un chatbot est un programme capable de simuler une conversation humaine via texte ou voix. Les assistants virtuels sont leur forme évoluée : ils combinent le traitement du langage naturel, la compréhension du contexte, l'intégration à des systèmes métier et, depuis 2023, des capacités issues des grands modèles de langage. L'analyse de sentiment évalue l'émotion ou l'opinion exprimée dans un texte. Le social listening utilise ces techniques pour surveiller automatiquement les conversations en ligne sur une marque ou un sujet.

Les chatbots ont connu quatre générations. Les chatbots à règles de première génération suivent des arbres de décision prédéfinis et échouent dès qu'ils sortent des scénarios prévus. Les chatbots de deuxième génération utilisent la reconnaissance d'intention et des entités nommées pour comprendre des formulations variées. Les chatbots de troisième génération s'appuient sur des grands modèles de langage combinés au RAG et à des outils externes, capables de conversations ouvertes et contextualisées. Les agents de quatrième génération combinent grands modèles de langage, outils, mémoire et planification pour exécuter des tâches complexes de façon autonome.

La compréhension du langage naturel, souvent désignée par le sigle NLU pour Natural Language Understanding, extrait deux informations clés du message de l'utilisateur : l'intention, c'est-à-dire ce que l'utilisateur veut faire, et les entités, c'est-à-dire les données spécifiques mentionnées comme une date, un numéro de commande ou un lieu. Par exemple, "Je veux annuler ma commande numéro douze mille" donne l'intention "annulation de commande" et l'entité "numéro douze mille".

L'analyse de sentiment peut opérer à plusieurs niveaux : binaire positif ou négatif, ternaire en ajoutant le neutre, émotionnel en distinguant joie, peur, colère et surprise, ou par aspect en identifiant le sentiment exprimé pour chaque dimension spécifique d'un sujet — par exemple "la livraison était lente" est négatif sur l'aspect livraison, "mais le produit est excellent" est positif sur l'aspect produit. Ce dernier niveau de granularité est l'analyse de sentiment dite aspect-based.

L'injection de prompt, ou prompt injection, est une attaque où un utilisateur malveillant insère des instructions dans ses messages pour manipuler le comportement du grand modèle de langage et contourner ses garde-fous. Elle nécessite des filtres de sécurité et des mesures de protection spécifiques lors du déploiement.

Chiffres à retenir : un chatbot peut gérer 80 pour cent des requêtes de support standard sans intervention humaine. Un contact chatbot coûte entre 0,50 et 1,70 dollar contre 5 à 12 dollars pour un agent humain, soit un ratio de cinq à dix fois. Le marché des chatbots devrait passer de 5,4 milliards de dollars en 2023 à 42 milliards en 2032. D'ici 2027, les chatbots seront le canal de service client principal pour 25 pour cent des entreprises selon Gartner.


### Métriques Marketing et Intelligence Artificielle

En bref : les métriques marketing pilotées par l'intelligence artificielle permettent de quantifier, prédire et optimiser la valeur client. Les principales sont la valeur vie client, souvent désignée par le sigle CLV pour Customer Lifetime Value, le taux d'attrition ou churn, le lead scoring prédictif, le pricing dynamique, et les données propriétaires dites first-party et zero-party dans un contexte de disparition progressive des cookies tiers.

La valeur vie client est la valeur totale des revenus qu'un client génère pour l'entreprise sur toute la durée de la relation. Avec l'intelligence artificielle, elle devient prédictive : des modèles probabilistes et du machine learning permettent d'estimer la valeur vie client future à six, douze ou vingt-quatre mois pour orienter les investissements d'acquisition et de rétention. La segmentation RFM — Récence du dernier achat, Fréquence des achats, Montant dépensé — enrichie par des données comportementales est un point d'entrée classique dans ces modèles.

Le churn prédictif est un modèle de machine learning qui calcule la probabilité qu'un client résilie dans une fenêtre temporelle donnée. Il utilise des signaux comportementaux comme la fréquence de connexion, le montant des achats, les interactions avec le service client, le score de satisfaction et l'utilisation des fonctionnalités du produit. Un modèle performant identifie 70 à 80 pour cent des clients sur le point de résilier trente jours avant qu'ils ne le fassent, permettant des actions de rétention proactives et personnalisées.

Le lead scoring prédictif utilise le machine learning entraîné sur les leads historiquement convertis pour calculer automatiquement la probabilité de conversion de chaque nouveau prospect. Il dépasse le scoring traditionnel à base de règles manuelles en capturant des patterns non linéaires et en intégrant des signaux d'intention en temps réel, comme des visites répétées sur les pages de tarification ou des téléchargements de fiches produit.

Le pricing dynamique est l'ajustement automatique des prix en temps réel en fonction de l'offre, de la demande, de la concurrence et du profil client. Il est utilisé dans le transport aérien, l'hôtellerie, le commerce en ligne, l'énergie et l'assurance. Amazon modifie ses prix 2,5 millions de fois par jour grâce à l'intelligence artificielle.

La distinction entre les types de données est cruciale dans un contexte de disparition des cookies tiers. Les données third-party collectées par des tiers via des cookies cross-sites sont en voie de disparition sous l'effet du RGPD et des restrictions des navigateurs. Les données first-party collectées directement par l'entreprise — historique d'achat, comportement sur le site et l'application — sont fiables et conformes au RGPD. Les données zero-party sont déclarées volontairement par le client, par exemple ses préférences dans un questionnaire de personnalisation : elles sont de la plus haute qualité car elles présupposent un consentement explicite de la personne.

Chiffres à retenir : augmenter la rétention client de cinq pour cent augmente les profits de 25 à 95 pour cent selon Bain et Company. Le pricing dynamique augmente le revenu de deux à cinq pour cent en moyenne selon McKinsey. Le CLV moyen d'un client fidèle est cinq fois supérieur à celui d'un nouveau client.


### Biais Algorithmiques

En bref : un biais algorithmique est une erreur systématique dans les résultats produits par un algorithme, qui génère des décisions injustes ou discriminatoires envers certains groupes selon le genre, l'origine ethnique, l'âge ou d'autres caractéristiques protégées. Il résulte généralement de données d'entraînement biaisées, d'un mauvais choix de variables ou d'un manque de représentativité dans les données.

Les mécanismes de génération des biais sont multiples. Les biais dans les données surviennent quand les données historiques reflètent des discriminations passées, que l'algorithme apprend et perpétue à grande échelle. La variable proxy est une variable a priori neutre — un code postal, un prénom — qui corrèle avec une caractéristique protégée comme l'origine ethnique et introduit ainsi une discrimination indirecte. La boucle de rétroaction, ou feedback loop, est un phénomène où les décisions de l'algorithme modifient les données futures et renforcent le biais initial : par exemple la surpolice dans certains quartiers produit plus d'arrestations, ce qui renforce la notation du quartier comme zone à risque, ce qui justifie plus de présence policière, et ainsi de suite. Le biais de sélection survient quand les données collectées ne représentent pas la population cible.

Les cas emblématiques sont les suivants. En 2016, l'organisation journalistique ProPublica révèle que le logiciel COMPAS, utilisé pour prédire la récidive aux États-Unis, prédit deux fois plus de récidive pour des prévenus noirs que pour des prévenus blancs à tort. En 2018, une étude du MIT et de Microsoft révèle que les systèmes de reconnaissance faciale de grands éditeurs ont un taux d'erreur de 34 pour cent sur les femmes à peau foncée contre moins de un pour cent sur les hommes à peau claire. La même année, Amazon abandonne son outil de recrutement par intelligence artificielle qui pénalisait les curriculum vitae contenant le mot "femmes". En 2019, une étude publiée dans la revue Science révèle qu'un algorithme de triage hospitalier très utilisé aux États-Unis sous-estimait la gravité des patients noirs, affectant environ 200 millions de patients.

Les biais algorithmiques sont plus dangereux que les biais humains pour trois raisons : ils s'appliquent à grande échelle de façon automatique et reproductible, ils sont souvent opaques donc difficiles à identifier, et ils sont plus compliqués à contester pour les personnes qui en sont victimes.

Les principaux outils de détection et correction sont IBM AI Fairness 360, une bibliothèque open source de détection et atténuation des biais dans les jeux de données et les modèles, et Fairlearn de Microsoft, un framework Python pour évaluer et améliorer l'équité des modèles de machine learning.


### Audit Algorithmique

En bref : l'audit algorithmique est un processus d'évaluation systématique d'un système d'intelligence artificielle visant à vérifier sa conformité, son équité, sa transparence et sa fiabilité. Il peut être interne, réalisé en auto-évaluation, ou externe, réalisé par un tiers indépendant. Il couvre les données, le modèle, le code source et les impacts réels sur les utilisateurs.

Un audit algorithmique complet suit plusieurs étapes. La définition du périmètre identifie le système concerné, ses usages et les parties prenantes. L'audit des données examine leur origine, qualité, représentativité et biais potentiels. L'audit du modèle analyse son architecture, ses métriques de performance, sa robustesse et son explicabilité. L'audit des impacts teste les effets réels sur les utilisateurs et analyse les cas limites. La documentation produit un rapport avec des recommandations correctives. Le suivi continu assure un re-audit périodique et un monitoring en production.

Deux outils documentaires sont des standards de facto dans la communauté de recherche. La model card, conçue par Google en 2019, est une fiche standardisée décrivant les caractéristiques d'un modèle : performances par sous-groupe démographique, usages prévus et limites connues. Le datasheet for datasets, proposé par Timnit Gebru et ses collègues en 2018, est une documentation structurée des jeux de données précisant leur origine, les modalités de collecte, les biais potentiels et les usages appropriés.

Le red-teaming est une méthode d'audit consistant à tester adversarialement un système d'intelligence artificielle pour identifier ses failles, ses biais ou ses comportements dangereux avant le déploiement.

L'article 22 du RGPD donne un droit d'explication pour toute décision automatisée individuelle significative. L'AI Act impose des audits de conformité obligatoires pour les systèmes à haut risque avant leur mise sur le marché, avec des amendes pouvant atteindre 30 millions d'euros ou six pour cent du chiffre d'affaires mondial pour non-conformité.

Chiffres à retenir : 70 pour cent des organisations ne disposent pas de processus formalisés d'audit de leurs modèles d'intelligence artificielle selon Gartner en 2023. Le marché de l'audit et de la gouvernance de l'intelligence artificielle devrait dépasser cinq milliards de dollars d'ici 2027.


### Intelligence Artificielle de Confiance et Intelligence Artificielle Responsable

En bref : l'intelligence artificielle de confiance, désignée en anglais par le terme Trustworthy AI, est une intelligence artificielle légale, éthique et robuste techniquement. L'intelligence artificielle responsable insiste sur la responsabilité des acteurs tout au long du cycle de vie du système. Ces deux notions convergent : une intelligence artificielle doit être transparente, explicable, équitable, sûre et respectueuse des droits fondamentaux.

En 2019, le groupe d'experts de haut niveau sur l'intelligence artificielle mandaté par la Commission européenne, désigné par le sigle HLEG, a défini sept exigences pour une intelligence artificielle de confiance. Premièrement, la supervision humaine et le contrôle humain dans la boucle décisionnelle. Deuxièmement, la robustesse technique et la sécurité. Troisièmement, le respect de la vie privée et la gouvernance des données. Quatrièmement, la transparence. Cinquièmement, la diversité, la non-discrimination et l'équité. Sixièmement, le bien-être sociétal et environnemental. Septièmement, la responsabilité et l'obligation de rendre compte.

L'intelligence artificielle explicable, souvent désignée par le sigle XAI pour Explainable AI, regroupe les méthodes permettant de rendre les décisions d'un modèle compréhensibles par des humains. Les deux méthodes les plus utilisées sont SHAP pour SHapley Additive exPlanations et LIME pour Local Interpretable Model-agnostic Explanations. Ces méthodes sont essentielles pour la confiance et pour permettre aux personnes concernées de contester les décisions automatisées.

Le human-in-the-loop, ou contrôle humain dans la boucle de décision, est le paradigme où un humain intervient dans le processus décisionnel automatisé pour valider, corriger ou superviser l'intelligence artificielle. C'est une exigence clé de l'AI Act pour les systèmes à haut risque.

L'alignement de l'intelligence artificielle, ou AI alignment, est le problème fondamental consistant à s'assurer que les objectifs et comportements d'un système d'intelligence artificielle sont alignés avec les valeurs et intentions humaines. C'est un domaine de recherche majeur, notamment chez Anthropic avec l'approche Constitutional AI qui encode des principes éthiques explicites dans le processus d'entraînement pour que le modèle s'auto-critique et corrige ses réponses.

Chiffres à retenir : 63 pour cent des consommateurs déclarent ne pas faire confiance aux décisions prises par une intelligence artificielle sans supervision humaine selon l'Edelman Trust Barometer en 2023. L'AI Safety Institute créé au Royaume-Uni en 2023 est le premier organisme gouvernemental dédié à la sécurité des intelligences artificielles de frontier. Le domaine de la sécurité de l'intelligence artificielle représente moins de un pour cent des publications scientifiques mais attire plus de 500 millions de dollars d'investissements annuels.


### Éthique de l'Intelligence Artificielle

En bref : l'éthique de l'intelligence artificielle est l'ensemble des principes, valeurs et pratiques qui guident la conception, le déploiement et l'usage des systèmes d'intelligence artificielle de façon juste, transparente et respectueuse des droits humains. Elle s'articule autour de cinq principes convergents au niveau international : la bienfaisance, c'est-à-dire que l'intelligence artificielle doit bénéficier à l'humanité ; la non-malfaisance, ne pas causer de tort ; l'autonomie, respecter la capacité de décision des individus ; la justice et l'équité dans la distribution des bénéfices et des risques ; et enfin l'explicabilité, pour que les décisions puissent être comprises et contestées.

L'Ethics by Design, ou éthique dès la conception, consiste à intégrer les considérations éthiques dès la phase de conception d'un système d'intelligence artificielle et tout au long de son cycle de développement, par analogie avec le Privacy by Design pour les données personnelles. Cette approche implique des évaluations d'impact éthique, des choix architecturaux éclairés et des revues éthiques systématiques à chaque étape du projet.

L'ethics washing, également appelé AI washing, est la pratique consistant à afficher un discours éthique sans engagement réel ni mécanisme de contrôle effectif, uniquement pour rassurer le public ou éviter la régulation. Ce risque est documenté : 84 pour cent des entreprises déclarent avoir une politique d'intelligence artificielle, mais seulement 24 pour cent l'appliquent de façon systématique selon Capgemini.

Le dual use désigne le risque qu'une technologie d'intelligence artificielle développée à des fins positives soit détournée à des fins malveillantes, comme la génération de deepfakes, la désinformation automatisée ou les cyberattaques automatisées. Ce risque est au cœur du débat sur la régulation des modèles de fondation dans l'AI Act.

L'analyse d'impact relative à la protection des données, désignée par le sigle AIPD, est une évaluation obligatoire sous le RGPD lorsqu'un traitement d'intelligence artificielle est susceptible d'engendrer un risque élevé pour les personnes. Elle couvre les risques de discrimination, de profilage et de prise de décision automatisée.

Chiffres à retenir : plus de 160 chartes et codes éthiques sur l'intelligence artificielle ont été recensés dans le monde en 2023. L'UNESCO a adopté sa recommandation sur l'éthique de l'intelligence artificielle en novembre 2021, signée par 193 pays membres. Vingt-trois pour cent des incidents d'intelligence artificielle documentés en 2022 relevaient de problèmes éthiques selon la base de données des incidents d'intelligence artificielle.


### AI Act — Le Règlement Européen sur l'Intelligence Artificielle

En bref : l'AI Act, correspondant au règlement UE numéro 2024/1689, est le premier cadre réglementaire contraignant et global sur l'intelligence artificielle au monde. Il a été adopté par le Parlement européen en mars 2024 et est entré en vigueur en août 2024. Il classe les systèmes d'intelligence artificielle selon leur niveau de risque et impose des obligations proportionnées à ce risque.

La classification par niveau de risque comprend quatre catégories. Les systèmes à risque inacceptable sont totalement interdits : la notation sociale des citoyens par l'État, la manipulation subliminale exploitant les vulnérabilités psychologiques des personnes, et l'identification biométrique en temps réel dans l'espace public sauf exceptions strictement encadrées. Les systèmes à haut risque impactent significativement la vie des personnes dans des domaines comme le recrutement, le crédit, la justice, l'éducation, les infrastructures critiques et les dispositifs médicaux. Ils doivent être certifiés avant mise sur le marché. Les systèmes à risque limité — chatbots, deepfakes, intelligence artificielle générative — doivent respecter des obligations de transparence et informer les utilisateurs qu'ils interagissent avec une intelligence artificielle. Les systèmes à risque minimal — filtres antispam, jeux vidéo — ne font l'objet d'aucune obligation spécifique.

Les obligations pour les systèmes à haut risque comprennent : un système de management des risques actif tout au long du cycle de vie, une gouvernance des données d'entraînement garantissant leur qualité et représentativité, une documentation technique et une journalisation des actions permettant la traçabilité, une transparence envers les déployeurs, une supervision humaine dans la boucle décisionnelle, une robustesse et une cybersécurité démontrées, et un enregistrement dans la base de données européenne des systèmes à haut risque.

Le bac à sable réglementaire, ou regulatory sandbox, est un espace contrôlé permettant aux entreprises de tester des systèmes d'intelligence artificielle innovants sous la supervision des autorités nationales avant leur mise sur le marché officielle, pour favoriser l'innovation sans contournement de la loi.

Le calendrier d'application est progressif : les interdictions des pratiques inacceptables s'appliquent depuis février 2025, les obligations pour les systèmes à haut risque s'appliqueront en août 2026, et la pleine application est prévue pour 2027.

L'AI Office est l'entité de la Commission européenne chargée de superviser l'application de l'AI Act, notamment pour les modèles de fondation à usage général et les cas transfrontaliers entre États membres.

Chiffres à retenir : les amendes peuvent atteindre 35 millions d'euros ou sept pour cent du chiffre d'affaires mondial pour les systèmes interdits, et 15 millions d'euros ou trois pour cent pour les systèmes à haut risque non conformes. Environ 400 000 systèmes d'intelligence artificielle seraient en circulation dans l'Union européenne au moment de l'adoption. L'AI Act s'applique aussi aux entreprises dont le siège est hors Union européenne, à partir du moment où leurs systèmes impactent des citoyens européens.


### Cadre International de l'Intelligence Artificielle

En bref : le cadre international de l'intelligence artificielle désigne l'ensemble des textes, principes et organisations qui définissent, à l'échelle mondiale ou régionale, les normes de gouvernance, d'éthique et de responsabilité pour les systèmes d'intelligence artificielle. Il repose sur des instruments variés : conventions contraignantes, recommandations, lignes directrices et rapports d'experts nationaux.

Le texte le plus fort juridiquement est la Convention du Conseil de l'Europe sur l'intelligence artificielle adoptée en 2024. C'est le premier traité international juridiquement contraignant sur l'intelligence artificielle, portant sur les droits humains, la démocratie et l'État de droit, et ouvert à la signature d'États non membres du Conseil de l'Europe comme les États-Unis, le Canada et le Japon.

Les Principes de l'OCDE sur l'intelligence artificielle, adoptés en 2019 et révisés en 2023, ont été adoptés par 46 pays dont l'ensemble du G20. Ils comprennent cinq principes : croissance inclusive, valeurs centrées sur l'humain, transparence et explicabilité, robustesse et sécurité, et responsabilité. Ils ont inspiré le Processus Hiroshima du G7 en 2023 et les principes de fond de l'AI Act européen.

La Recommandation de l'UNESCO sur l'éthique de l'intelligence artificielle de 2021 est le premier instrument normatif mondial sur ce sujet, signé par 193 pays membres. Elle préconise notamment des évaluations d'impact éthique avant tout déploiement de système d'intelligence artificielle.

Le rapport Villani, publié en France en 2018 sous le titre "Donner un sens à l'intelligence artificielle", est commandé par le gouvernement français et structuré en six axes sectoriels : santé, transport, environnement, défense et sécurité, industrie et services publics. Il recommande notamment l'ouverture des données publiques, le droit à l'audit algorithmique et la sobriété numérique. Il a positionné la France comme un acteur de référence dans le débat mondial sur l'intelligence artificielle éthique.

La principale limite de ces cadres internationaux est que la grande majorité des instruments sont non contraignants, ce que l'on appelle la soft law. Il n'existe pas de mécanisme international d'application uniforme face aux États ou aux acteurs privés non coopératifs. La fragmentation entre l'approche européenne très réglementaire, l'approche américaine fondée davantage sur l'autorégulation et l'approche chinoise orientée développement national reste un défi géopolitique majeur.


### Normes ISO pour l'Intelligence Artificielle

En bref : les normes ISO pour l'intelligence artificielle sont des standards internationaux développés principalement par le comité technique désigné ISO/IEC JTC 1/SC 42, qui signifie Joint Technical Committee 1, Subcommittee 42. Ce comité encadre la gouvernance, la gestion des risques, la terminologie et la fiabilité des systèmes d'intelligence artificielle. Ces normes fournissent un langage commun, des outils pratiques et une base de certification reconnue mondialement. L'AI Act encourage explicitement le recours aux normes harmonisées et prévoit qu'elles confèrent une présomption de conformité pour les systèmes à haut risque.

L'ISO/IEC 42001, publiée en décembre 2023, est la première norme de système de management spécifiquement dédiée à l'intelligence artificielle. Elle est analogue à l'ISO 27001 pour la sécurité de l'information ou à l'ISO 9001 pour la qualité. Elle définit un système de management de l'intelligence artificielle, souvent désigné par le sigle AIMS pour AI Management System, couvrant le contexte de l'organisation, le leadership et la politique IA, la planification des risques, le support et les compétences, les opérations de développement et déploiement responsable, l'évaluation des performances et l'amélioration continue.

L'ISO/IEC 23894, publiée en 2023, fournit des lignes directrices pour la gestion des risques spécifiques à l'intelligence artificielle, en s'appuyant sur l'ISO 31000 de management des risques général et en l'adaptant aux spécificités de l'IA. Elle couvre les risques liés aux données, au modèle, au déploiement et les risques sociétaux.

Parmi les autres normes du comité SC 42, l'ISO/IEC 22989 traite de la terminologie et des concepts de l'intelligence artificielle. L'ISO/IEC TR 24027 traite des biais dans les systèmes d'intelligence artificielle. L'ISO/IEC 24368 offre une vue d'ensemble éthique et sociétale de l'IA.

En parallèle, le NIST américain, l'Institut national des normes et de la technologie, a publié en 2023 son cadre de gestion des risques d'intelligence artificielle, l'AI RMF 1.0 pour AI Risk Management Framework. Ce référentiel est largement utilisé et aligné avec les principes ISO mais sans portée réglementaire directe dans l'Union européenne.

Chiffres à retenir : plus de 40 normes sont en cours d'élaboration au sein du comité SC 42. La certification ISO/IEC 42001 est décernée par des organismes comme Bureau Veritas, SGS ou BSI. Le marché de la certification ISO pour l'intelligence artificielle devrait atteindre 800 millions de dollars d'ici 2026 selon MarketsandMarkets.


### Shadow AI — L'Intelligence Artificielle dans l'Ombre

En bref : le Shadow AI désigne l'utilisation non autorisée, non déclarée et non contrôlée d'outils d'intelligence artificielle par des employés dans un contexte professionnel, sans validation de la direction des systèmes d'information, de la direction générale ou des équipes de conformité. Par analogie avec le shadow IT, il crée des angles morts en matière de sécurité, de conformité et de gouvernance des données.

Les raisons pour lesquelles le Shadow AI se développe sont multiples. D'abord la pression de productivité : les outils d'intelligence artificielle générative offrent des gains de temps immédiats que les employés ne veulent pas manquer. Ensuite la lenteur des processus d'approbation par rapport à l'agilité des outils en mode service en ligne. Puis l'absence de solutions institutionnelles approuvées déployées par l'entreprise. Enfin la méconnaissance des risques : les employés ne réalisent pas que leurs saisies peuvent alimenter les modèles ou être exposées à des tiers.

Les risques principaux pour l'organisation sont la fuite de données confidentielles — code source, données clients, stratégie — envoyées vers des serveurs tiers hébergeant les intelligences artificielles grand public sans accord contractuel. Il y a aussi la non-conformité au RGPD par traitement de données personnelles sans encadrement légal approprié. Il y a la violation potentielle des droits d'auteur via des contenus générés pouvant être contrefaisants. Il y a la dégradation de la qualité des livrables lorsque des hallucinations sont présentées comme des vérités vérifiées. Et il y a les risques de sécurité via des extensions ou plugins d'intelligence artificielle potentiellement malveillants.

Le cas emblématique est celui de Samsung en avril 2023 : des ingénieurs ont copié du code source propriétaire dans ChatGPT, ce qui a conduit l'entreprise à interdire immédiatement l'outil et à lancer le développement d'une intelligence artificielle interne souveraine.

Les stratégies de gouvernance pour maîtriser le Shadow AI s'articulent en cinq axes. La détection via des outils de prévention de la fuite de données, en anglais Data Loss Prevention. Des politiques claires avec une charte d'utilisation de l'intelligence artificielle et une liste blanche des outils approuvés. Le déploiement de solutions approuvées et sécurisées comme Azure OpenAI Service ou Copilot for Microsoft 365. La formation et la sensibilisation, car interdire sans expliquer ni proposer d'alternative pousse à contourner. Et la mise en place d'une gouvernance IA avec un AI Officer, un comité dédié et un processus d'approbation agile.

Chiffres à retenir : 65 pour cent des employés utilisent des outils d'intelligence artificielle non approuvés par leur employeur selon le Microsoft Work Trend Index 2024. 55 pour cent des utilisateurs de ChatGPT en entreprise y transmettent des informations confidentielles selon Cyberhaven en 2023. 46 pour cent des dirigeants ignorent que leurs équipes utilisent des outils d'intelligence artificielle non validés selon IBM.


### Edge AI — L'Intelligence Artificielle en Périphérie

En bref : l'Edge AI, ou intelligence artificielle en périphérie, désigne l'exécution de modèles d'intelligence artificielle directement sur des dispositifs locaux — smartphones, capteurs IoT, caméras, véhicules, équipements industriels — plutôt que sur des serveurs cloud distants. L'inférence se fait au plus près des données, sans ou avec peu de connectivité réseau.

L'architecture Edge AI distingue trois niveaux. Le dispositif en périphérie, comme un capteur ou une caméra intelligente, exécute l'inférence locale avec un modèle léger et optimisé. La passerelle en périphérie, ou edge gateway, agrège et pré-filtre les résultats de plusieurs dispositifs. Le cloud ou datacenter reste responsable du ré-entraînement des modèles lourds et de leur déploiement vers les dispositifs sous forme de mises à jour.

Plusieurs techniques permettent de compresser les modèles pour les rendre compatibles avec les contraintes matérielles des dispositifs en périphérie. La quantification réduit la précision des poids du modèle, par exemple en passant de float32 à int8, divisant la taille par quatre et accélérant l'inférence. L'élagage, ou pruning, supprime les connexions et neurones peu contributifs, réduisant la taille du modèle de deux à dix fois. La distillation de connaissances consiste à entraîner un petit modèle élève à imiter un grand modèle professeur tout en atteignant des performances proches. Certaines architectures sont conçues nativement pour la périphérie, comme MobileNet, EfficientNet ou les variants YOLO allégés.

Le TinyML est la branche de l'Edge AI qui fait tourner des modèles de machine learning sur des microcontrôleurs très contraints, avec quelques centaines de kilooctets de mémoire et quelques milliwatts de consommation électrique seulement. Il ouvre des applications sur des objets aussi simples qu'une montre connectée, un capteur industriel autonome ou un appareil médical portable.

L'avantage principal de l'Edge AI pour les véhicules autonomes illustre bien les enjeux temporels : la latence d'un aller-retour vers un serveur cloud est de 50 à 200 millisecondes, ce qui est totalement incompatible avec les décisions de sécurité temps réel comme le freinage d'urgence qui requièrent moins de 10 millisecondes. Le traitement doit être local et fonctionner même en l'absence de réseau.

Chiffres à retenir : le marché de l'Edge AI devrait atteindre 107 milliards de dollars d'ici 2030 avec une croissance annuelle de 20 pour cent. 55 pour cent des données mondiales seront traitées en périphérie du réseau d'ici 2025 selon IDC. Un modèle de détection d'objet peut fonctionner en moins de cinq millisecondes en local contre 50 à 200 millisecondes avec un aller-retour cloud, soit une réduction de latence de 60 à 80 pour cent.


---

## Questions que le jury pourrait poser

Les questions suivantes sont tirées directement des sujets de Grand Oral associés au thème IA et complétées par les questions types identifiées pour les jurys.

Première question : qu'est-ce qu'un grand modèle de langage et comment fonctionne l'intelligence artificielle générative ? La réponse doit expliquer l'architecture Transformer, la prédiction du token suivant, le RLHF, et illustrer avec des exemples concrets comme ChatGPT, Gemini ou Mistral.

Deuxième question : quelle est la différence entre RAG et fine-tuning, et quand utiliser l'un ou l'autre ? La réponse doit positionner clairement les deux approches sur les axes du coût, de la fraîcheur des données, de la traçabilité des sources et du comportement souhaité.

Troisième question : quels sont les risques des biais algorithmiques et comment les détecter ? La réponse doit citer les cas COMPAS, Amazon et l'étude du MIT sur la reconnaissance faciale, et mentionner les outils IBM AI Fairness 360 et Fairlearn.

Quatrième question : comment l'AI Act classifie-t-il les systèmes d'intelligence artificielle par niveau de risque ? La réponse doit maîtriser les quatre niveaux — inacceptable, haut risque, risque limité, risque minimal — avec des exemples concrets pour chacun, et citer les amendes encourues.

Cinquième question : l'intelligence artificielle face à la cybersécurité — est-elle plus une menace ou une solution ? La réponse doit traiter les deux versants : l'intelligence artificielle comme outil de défense via l'AIOps, la détection d'anomalies et la corrélation d'événements, et l'intelligence artificielle comme vecteur d'attaque via les deepfakes, le phishing automatisé et l'ingénierie sociale augmentée.

Sixième question : comment mettre en place une gouvernance de l'intelligence artificielle dans l'entreprise ? La réponse doit articuler Shadow AI, politique d'utilisation formalisée, AI Officer, liste blanche des outils approuvés, formation des collaborateurs, conformité AI Act et certification ISO/IEC 42001.

Septième question : comment contrôler l'usage non autorisé de l'intelligence artificielle générative, le Shadow AI ? La réponse doit mentionner les stratégies de détection avec les outils de prévention de la fuite de données, les politiques claires, les solutions approuvées comme Copilot for Microsoft 365, et souligner que l'interdiction seule est insuffisante sans alternatives accessibles.

Huitième question : quels indicateurs de performance pour mesurer le retour sur investissement d'un projet d'intelligence artificielle en entreprise ? La réponse doit distinguer les métriques techniques — précision, AUC-ROC, dérive des données — des métriques business — réduction du temps moyen de réparation, taux de résolution du chatbot, augmentation du chiffre d'affaires par la recommandation, retour sur investissement du pricing dynamique.

Neuvième question : que signifie l'intelligence artificielle de confiance et comment l'appliquer concrètement ? La réponse doit détailler les sept exigences du HLEG, le human-in-the-loop, l'intelligence artificielle explicable avec SHAP et LIME, et la notion d'alignement.

Dixième question : comment l'intelligence artificielle transforme-t-elle le marketing et la relation client ? La réponse doit couvrir l'hyper-personnalisation, le marketing automation, la recommandation algorithmique, les chatbots, les métriques prédictives comme le churn et la valeur vie client, et les enjeux liés aux données first-party en contexte post-cookies.

Onzième question : comment l'intelligence artificielle peut-elle optimiser les opérations informatiques via l'AIOps ? La réponse doit expliquer les niveaux d'autonomie de zéro à cinq, le self-healing, le jumeau numérique d'infrastructure et quantifier les gains sur le temps moyen de réparation.


---

## Points de vigilance

Premier piège à éviter : confondre intelligence artificielle générative et intelligence artificielle en général. L'intelligence artificielle générative, fondée sur les grands modèles de langage, est un sous-ensemble spectaculaire mais récent de l'intelligence artificielle. Le machine learning supervisé classique reste responsable de 70 pour cent de la valeur créée en entreprise selon McKinsey, et des pans entiers comme la maintenance prédictive ou le scoring crédit ne reposent pas sur les grands modèles de langage.

Deuxième piège à éviter : présenter le RAG et le fine-tuning comme deux alternatives équivalentes et interchangeables. Ils répondent à des besoins différents. Le RAG est adapté aux informations évolutives et à la traçabilité des sources — corpus documentaires d'entreprise, bases réglementaires. Le fine-tuning est adapté à l'acquisition d'un style ou de connaissances stables à intégrer dans le modèle. Ils peuvent par ailleurs être combinés pour les cas les plus exigeants.

Troisième piège à éviter : croire que l'AI Act s'applique uniquement aux entreprises européennes. Il s'applique à toute organisation dont les systèmes d'intelligence artificielle ont des effets sur des citoyens de l'Union européenne, quelle que soit la localisation du siège social. C'est exactement le même mécanisme d'extraterritorialité que le RGPD, qui s'impose déjà à des entreprises américaines et asiatiques.

Quatrième piège à éviter : réduire les biais algorithmiques à un simple problème technique de données mal équilibrées. Les biais sont aussi sociaux, historiques et systémiques. La correction technique — rééquilibrer un dataset — ne suffit pas sans une réflexion sur les variables utilisées, les objectifs réels du système, les effets des boucles de rétroaction et les impacts concrets sur les populations concernées.

Cinquième piège à éviter : traiter le Shadow AI comme un simple problème de sécurité informatique à résoudre par l'interdiction. C'est avant tout un problème de gouvernance et d'accompagnement du changement. Les entreprises qui répondent uniquement par l'interdiction sans proposer d'alternatives approuvées et accessibles échouent à contenir le phénomène, car la pression de productivité reste intacte. Une gouvernance efficace équilibre le contrôle et l'adoption.
