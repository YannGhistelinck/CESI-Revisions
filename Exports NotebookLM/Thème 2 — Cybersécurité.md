# Cybersécurité — Guide de révision complet

## Introduction

La cybersécurité est aujourd'hui l'une des préoccupations stratégiques majeures pour toute Direction des Systèmes d'Information. Dans un contexte où soixante-six pourcent des entreprises françaises ont subi au moins une cyberattaque en 2023, et où le coût moyen d'une violation de données dépasse quatre millions de dollars, la question n'est plus de savoir si une organisation sera attaquée, mais quand et comment elle en sortira. Ce guide couvre l'intégralité des notions clés du thème, des menaces aux cadres réglementaires, en passant par les outils de détection, les stratégies de défense et la gouvernance de la sécurité.

---

## Notions clés à maîtriser

### Menaces cyber

Les menaces cyber désignent l'ensemble des attaques informatiques malveillantes visant à compromettre la confidentialité, l'intégrité ou la disponibilité des systèmes d'information. Elles couvrent un spectre très large que tout manager informatique doit maîtriser.

Le ransomware, ou rançongiciel, est aujourd'hui la menace la plus médiatisée. Il chiffre les données de la victime puis exige une rançon en cryptomonnaie pour la clé de déchiffrement. La chaîne d'attaque type commence par un accès initial via un email de phishing ou un accès distant mal sécurisé, se poursuit par un mouvement latéral au sein du réseau, une élévation de privilèges, puis un chiffrement de masse. Les groupes criminels ont industrialisé ce modèle grâce au Ransomware as a Service, ou RaaS : des développeurs louent leur ransomware à des affiliés qui conduisent les attaques et conservent généralement soixante-dix à quatre-vingts pourcent des rançons. Des groupes comme LockBit ou BlackCat ont généré des centaines de millions de dollars avec ce modèle.

Le phishing, ou hameçonnage, reste le vecteur d'accès initial numéro un. Le phishing classique est un envoi de masse imitant une marque légitime, tandis que le spear phishing cible précisément un individu avec des informations personnalisées. Les variantes incluent le vishing, par téléphone, et le smishing, par SMS. La Business Email Compromise, ou fraude au président, consiste à usurper l'identité d'un dirigeant pour ordonner un virement frauduleux : les pertes mondiales dépassent cinquante milliards de dollars depuis 2013 selon le Federal Bureau of Investigation.

Les APT, c'est-à-dire les menaces persistantes avancées, sont des attaques longue durée conduites par des acteurs étatiques ou para-étatiques. Leur objectif est l'espionnage, le sabotage ou le vol de propriété intellectuelle. Les groupes APT28, dit Fancy Bear, et APT41 sont parmi les plus connus. Les vulnérabilités zero-day sont des failles inconnues de l'éditeur, sans correctif disponible, exploitées avant toute divulgation publique. Les attaques sur la chaîne d'approvisionnement, ou supply chain attacks, compromettent un fournisseur pour atteindre ses clients : l'affaire SolarWinds en 2020, où une backdoor nommée Sunburst a été injectée dans des mises à jour légitimes et a impacté dix-huit mille organisations dont des agences gouvernementales américaines, en est l'exemple emblématique.

Chiffres à retenir : soixante-six pourcent des entreprises françaises ont subi une cyberattaque en 2023, le coût moyen d'une violation atteint quatre virgule quarante-cinq millions de dollars, et le délai médian de détection d'une intrusion est de vingt et un jours.

---

### Ingénierie sociale

L'ingénierie sociale est l'ensemble des techniques de manipulation psychologique visant à amener une personne à divulguer des informations confidentielles ou à effectuer des actions compromettant la sécurité, sans recourir à des exploits techniques. Elle exploite les biais cognitifs humains, notamment l'autorité, l'urgence, la réciprocité et la confiance.

Robert Cialdini identifie six leviers d'influence exploités par les attaquants. L'autorité consiste à usurper l'identité d'un dirigeant ou d'un technicien. L'urgence crée une pression temporelle du type "le virement doit être effectué avant dix-sept heures." La réciprocité, la similarité, la preuve sociale et la rareté complètent cet arsenal psychologique. Aucun dispositif technique ne protège contre un employé manipulé : c'est pourquoi soixante-huit pourcent des violations de données impliquent un facteur humain selon le rapport Verizon DBIR 2024.

Les deepfakes vocaux et vidéo constituent une menace émergente particulièrement préoccupante. En 2024, un employé de la finance de la société Arup à Hong Kong a viré vingt-cinq millions de dollars après une visioconférence deepfake impliquant de faux collègues générés par intelligence artificielle. Les modèles de langage de grande taille, ou LLM, permettent désormais de générer des emails de spear phishing parfaitement rédigés, sans faute d'orthographe, adaptés au contexte professionnel de la cible, en exploitant les informations publiques disponibles sur LinkedIn ou dans la presse.

L'insider threat, ou menace interne, désigne les risques posés par des personnes ayant un accès légitime au système d'information : employé malveillant, négligent ou dont le compte a été compromis. La détection est difficile car l'insider dispose déjà d'accès légitimes.

Pour se défendre, les organisations doivent combiner sensibilisation régulière, simulations de phishing, procédures de vérification hors bande pour les demandes sensibles, et détection comportementale via les outils d'analyse comportementale des utilisateurs et des entités.

---

### Zero Trust

Zero Trust est une architecture de sécurité fondée sur le principe "ne jamais faire confiance, toujours vérifier." Elle refuse la notion de périmètre réseau de confiance et exige une authentification et une autorisation continues pour chaque utilisateur, appareil et flux réseau, qu'ils soient internes ou externes.

Ce modèle est devenu indispensable car le périmètre réseau traditionnel a disparu. Avec la généralisation du cloud, du télétravail et des appareils mobiles, un utilisateur connecté au réseau d'entreprise n'est plus nécessairement digne de confiance. Le pionnier de ce modèle est Google, qui a supprimé son réseau privé virtuel interne dès 2014 avec son projet BeyondCorp.

Les principes fondateurs, définis dans le référentiel américain NIST SP 800-207, sont au nombre de cinq. Toutes les ressources sont considérées comme non fiables par défaut. L'accès est accordé au cas par cas selon le contexte. Chaque identité ne dispose que des droits strictement nécessaires, c'est le principe de moindre privilège, ou least privilege. Tout le trafic est inspecté et journalisé. Enfin, l'authentification est dynamique et continuellement réévaluée.

La micro-segmentation divise le réseau en zones de sécurité granulaires pour empêcher les mouvements latéraux en cas de compromission. Le ZTNA, c'est-à-dire Zero Trust Network Access, remplace le réseau privé virtuel traditionnel : l'accès est accordé application par application après vérification de l'identité, et l'utilisateur n'accède jamais au réseau entier. Les entreprises ayant adopté Zero Trust ont un coût moyen de violation de données inférieur d'un million sept cent soixante mille dollars à celles qui ne l'ont pas fait.

---

### Défense en profondeur

La défense en profondeur est une stratégie consistant à superposer plusieurs couches de protection indépendantes, de sorte que la compromission d'une couche ne suffise pas à compromettre l'ensemble du système. Elle est héritée du concept militaire de défense étagée.

Les sept couches de la défense en profondeur sont les suivantes. La sécurité physique protège l'accès aux locaux et aux salles serveurs. La sécurité réseau s'appuie sur les pare-feux, la segmentation, les systèmes de détection et de prévention d'intrusion, et le filtrage DNS. La sécurité des postes et serveurs repose sur les outils de détection et réponse sur les endpoints, la gestion des correctifs et le durcissement des configurations. La sécurité des applications utilise l'authentification multifacteur, les pare-feux applicatifs et les tests de sécurité. La sécurité des données passe par le chiffrement, la prévention des fuites de données et la gestion des droits d'accès. La sécurité organisationnelle englobe la politique de sécurité des systèmes d'information et les procédures. Enfin, la couche humaine constitue ce que l'on appelle le pare-feu humain : chaque collaborateur formé et vigilant est une barrière réelle.

L'ANSSI publie quarante-deux mesures d'hygiène informatique constituant le socle minimal pour toute organisation. Parmi les faits marquants, quatre-vingts pourcent des incidents de sécurité auraient pu être évités par l'application de mesures d'hygiène de base. La directive NIS2, transposée en France en 2024, impose à plus de dix mille entités françaises supplémentaires de formaliser une défense en profondeur. La clé de ce modèle par rapport à la sécurité périmétrique est simple : la défense en profondeur postule que le périmètre sera franchi, et prépare des barrières internes à chaque couche.

---

### Cyber-résilience

La cyber-résilience désigne la capacité d'une organisation à préparer, résister, s'adapter et se remettre d'une cyberattaque, tout en maintenant la continuité de ses activités métier. C'est une posture stratégique qui intègre la certitude que l'attaque aura lieu.

Le principe fondateur est l'assume breach, ou postulat de compromission : concevoir l'architecture et les processus en partant du principe que l'attaquant est déjà présent dans le système d'information. Cela conduit à la micro-segmentation, à la surveillance interne intensive et à des plans de réponse immédiatement activables.

La règle de sauvegarde de référence est la règle 3-2-1 : trois copies des données, sur deux supports différents, dont une copie hors site. Elle est étendue en 3-2-1-1-0 : une copie hors ligne, dite air gap, et zéro erreur vérifiée lors de la restauration. Les sauvegardes immuables, ou WORM pour Write Once Read Many, sont impossibles à modifier ou supprimer même par un ransomware ayant compromis le compte administrateur. Un air gap correspond à une isolation physique ou logique complète d'une copie de sauvegarde du réseau de production.

Les deux métriques centrales sont le RTO, Recovery Time Objective, qui est la durée maximale acceptable avant la restauration des systèmes, et le RPO, Recovery Point Objective, qui est la perte de données maximale acceptable exprimée en durée. Concernant les chiffres clés : le délai moyen de reprise après un ransomware est de vingt et un jours, et quatre-vingt-treize pourcent des entreprises qui perdent l'accès à leurs données pendant plus de dix jours font faillite dans l'année. Le règlement DORA, Digital Operational Resilience Act, est entré en application en janvier 2025 pour vingt-deux mille entités financières européennes.

---

### SIEM

Le SIEM, Security Information and Event Management, est une plateforme centralisant la collecte, l'agrégation, la normalisation et la corrélation des journaux et événements de sécurité issus de l'ensemble du système d'information. Il permet la détection en temps réel des menaces et la conservation des journaux à des fins d'investigation et de conformité.

Le fonctionnement du SIEM se décompose en six étapes. La collecte récupère les journaux de toutes les sources via des agents ou des protocoles standards. La normalisation les convertit dans un format commun. La corrélation croise des événements de sources différentes : par exemple, une connexion depuis Paris à neuf heures et une connexion depuis Shanghai à neuf heures cinq, un phénomène appelé "impossible travel", génère automatiquement une alerte. Le stockage conserve les journaux pour l'investigation forensique et la conformité réglementaire. L'alerting génère des tickets d'incident. Enfin, le reporting produit des tableaux de bord de conformité.

L'UEBA, User and Entity Behavior Analytics, est un module d'intelligence artificielle intégré aux SIEM modernes qui établit un profil comportemental de base pour chaque utilisateur et entité, puis détecte les anomalies statistiques. Un SOC reçoit en moyenne onze mille alertes par jour, dont quarante-cinq pourcent sont des faux positifs. Les principales solutions du marché sont Splunk, leader historique à la tarification par volume de données, Elastic Security en version open source, IBM QRadar pour les grandes entreprises, Wazuh en open source gratuit pour les PME, et Microsoft Sentinel en version cloud-native.

---

### SOAR

Le SOAR, Security Orchestration Automation and Response, est une plateforme permettant d'orchestrer les outils de sécurité, d'automatiser les tâches répétitives de réponse aux incidents et de standardiser les procédures via des playbooks. Il complète le SIEM en transformant les alertes en actions concrètes.

La distinction essentielle est la suivante : le SIEM détecte et alerte, le SOAR agit et automatise. Ils sont complémentaires et forment, avec les flux de renseignement sur les menaces, le triptyque fondamental du centre opérationnel de sécurité moderne.

Un playbook est un flux de travail automatisé définissant la séquence d'actions en réponse à un type d'incident. Par exemple, le playbook anti-phishing extrait automatiquement les indicateurs de compromission de l'email, les vérifie sur des bases de réputation comme VirusTotal, bloque l'adresse IP malveillante sur le pare-feu et l'adresse web sur le proxy, liste les autres utilisateurs ayant reçu le même message, les notifie, puis crée un ticket d'incident. Ce processus qui prenait deux heures manuellement est réduit à huit minutes. Le SOAR réduit le MTTR, Mean Time To Respond, de quatre-vingts pourcent en moyenne selon IBM Security. Face à une pénurie mondiale de quatre millions de postes en cybersécurité non pourvus en 2023, le SOAR est une réponse partielle indispensable pour que les équipes réduites puissent traiter un volume d'alertes disproportionné.

---

### EDR, XDR et NDR

Les outils de détection et réponse sur les terminaux, dans le réseau et de manière étendue constituent la troisième ligne technologique du centre opérationnel de sécurité, aux côtés du SIEM et du SOAR.

L'EDR, Endpoint Detection and Response, installe un agent léger sur chaque terminal, poste de travail ou serveur. Cet agent collecte en continu la télémétrie système : processus créés, connexions réseau, accès au registre, exécution de scripts. Il détecte les attaques sans signature connue, notamment les malwares fileless qui s'exécutent directement en mémoire sans écrire de fichier sur le disque et échappent donc aux antivirus traditionnels. Il permet aussi l'isolation immédiate du terminal depuis la console centralisée. CrowdStrike, SentinelOne et Microsoft Defender Endpoint sont les leaders, et HarfangLab est l'acteur français certifié par l'ANSSI, requis pour les opérateurs d'importance vitale.

Le NDR, Network Detection and Response, analyse le trafic réseau en temps réel pour détecter les comportements anormaux : communications avec un serveur de commande et contrôle, exfiltration de données, mouvements latéraux. Son avantage est de couvrir les appareils sans agent, notamment les objets connectés et les équipements de technologie opérationnelle.

Le XDR, Extended Detection and Response, est l'évolution naturelle. Il corrèle la télémétrie de multiples sources, terminaux, réseau, messagerie, cloud et identités, dans une plateforme unifiée pour offrir une vision globale d'une attaque multi-vecteurs. Le framework MITRE ATT&CK recense plus de quatre cents techniques réparties en quatorze tactiques et sert de référentiel universel pour cartographier les détections.

---

### Threat Intelligence et Threat Hunting

La Cyber Threat Intelligence, ou CTI, est le processus de collecte, d'analyse et de partage d'informations sur les menaces cyber afin d'anticiper et de contrer les attaques. Le Threat Hunting est une démarche proactive consistant à rechercher activement des compromissions dans le système d'information, sans attendre qu'une alerte soit levée.

La CTI s'organise en quatre niveaux. Le niveau stratégique fournit des informations aux décideurs sur les tendances géopolitiques. Le niveau opérationnel renseigne sur les campagnes d'attaques en cours. Le niveau tactique fournit des indicateurs de compromission concrets : adresses IP malveillantes, hachages de fichiers, noms de domaines de serveurs de commande et contrôle. Le niveau technique détaille les exploits et variantes de malwares.

Les indicateurs de compromission sont partagés via des formats standardisés : STIX pour la structure des données et TAXII pour le protocole de transport. MISP, Malware Information Sharing Platform, est la plateforme open source la plus utilisée pour ce partage. La distinction entre indicateurs de compromission et TTP, Tactics Techniques and Procedures, est fondamentale : les indicateurs changent rapidement car l'attaquant peut modifier son adresse IP facilement, mais les TTP, c'est-à-dire la manière d'opérer de l'attaquant, sont beaucoup plus durables et pertinents pour la détection long terme.

Le Threat Hunting suit un processus itératif en quatre étapes : formuler une hypothèse, investiguer via des requêtes sur les journaux et les EDR, découvrir des comportements anormaux, puis répondre et enrichir les règles de détection. Le dwell time, ou temps de séjour de l'attaquant avant détection, est de seize jours en 2023 selon Mandiant, contre vingt-quatre jours en 2022 : une amélioration qui témoigne de la montée en maturité des équipes.

---

### SOC

Un Security Operations Center, ou SOC, est une équipe centralisée appuyée par des outils technologiques dont la mission est de surveiller en continu le système d'information, détecter les incidents, y répondre et améliorer la posture de sécurité. Il constitue le centre névralgique opérationnel de la cybersécurité d'une organisation.

Il existe plusieurs modèles de SOC. Le SOC interne, ou in-house, opère vingt-quatre heures sur vingt-quatre et sept jours sur sept avec des équipes dédiées. Il offre le meilleur niveau de personnalisation mais coûte entre un et cinq millions d'euros par an. Le prestataire de services de sécurité managés, ou MSSP, fournit la surveillance en mode mutualisé. Le Managed Detection and Response, ou MDR, est l'évolution du MSSP : il répond activement en isolant les terminaux compromis et inclut du Threat Hunting intégré. La distinction clé est que le MDR agit là où le MSSP classique se contente d'alerter. Le SOC hybride combine une équipe interne pour les niveaux experts et une externalisation de la surveillance vingt-quatre heures sur vingt-quatre.

Les analystes SOC sont organisés en trois niveaux. Le niveau 1 assure le triage des alertes et la qualification des faux positifs. Le niveau 2 mène des investigations approfondies et effectue le confinement. Le niveau 3 gère les incidents complexes, mène le Threat Hunting et améliore les règles de détection. La fatigue d'alerte est le problème numéro un cité par soixante-cinq pourcent des analystes : un analyste de niveau 1 traite en moyenne quatre mille cinq cents alertes par semaine. Sans SOC dédié, le délai de détection est de cent quatre-vingt-dix-sept jours contre seize jours avec un SOC mature.

---

### Red Team, Blue Team et Purple Team

La Red Team simule des attaquants réels pour tester les défenses d'une organisation en conditions réalistes. La Blue Team est l'équipe défensive qui surveille, détecte et répond. La Purple Team est un mode collaboratif où les deux travaillent ensemble pour améliorer simultanément les capacités offensives et défensives.

Un test de pénétration classique, ou pentest, a un périmètre défini, une durée courte d'une à deux semaines et produit un rapport de vulnérabilités techniques. Un engagement Red Team est fondamentalement différent : il simule un acteur de menace persistante avancée sur un objectif métier défini, sur une durée longue de quatre à douze semaines, sans périmètre limité, en testant la détection réelle par la Blue Team. En moyenne, une Red Team professionnelle accède aux systèmes critiques dans soixante-quinze pourcent des engagements.

Le mode Purple Team est plus accessible et didactique : la Red Team exécute une technique du référentiel MITRE ATT&CK, la Blue Team vérifie immédiatement si le SIEM a généré une alerte, et ensemble ils améliorent les règles. Un exercice de table, ou tabletop exercise, simule un scénario d'incident sans actions techniques réelles, idéal pour tester les procédures décisionnelles et la communication de crise avec le comité de direction. TIBER-EU et le DORA TLPT, Threat-Led Penetration Testing, imposent des exercices Red Team basés sur de la Threat Intelligence réelle dans le secteur financier européen.

---

### Forensics

L'investigation numérique, ou forensics, est l'ensemble des techniques et processus permettant de collecter, préserver, analyser et présenter des preuves numériques de manière légalement recevable. Elle vise à reconstituer ce qui s'est passé, comment et par qui.

Quatre principes fondamentaux gouvernent la forensics. La préservation de l'intégrité impose que toute copie soit effectuée sur un support bloquant l'écriture, avec vérification par hachage cryptographique avant et après. La chaîne de custody, ou chain of custody, est la traçabilité documentée de chaque pièce à conviction : sans elle, les preuves peuvent être irrecevables en justice. L'ordre de volatilité impose de collecter du plus volatil au moins volatil : mémoire RAM en premier, puis processus actifs, connexions réseau, journaux système, et enfin le disque dur. Enfin, le principe de non-altération du système source s'impose en toutes circonstances.

Les types d'investigation incluent la forensics disque, qui analyse les systèmes de fichiers et récupère les fichiers supprimés, la forensics mémoire qui utilise l'outil Volatility pour extraire les malwares fileless présents uniquement en RAM, la forensics réseau avec Wireshark, l'analyse des journaux Active Directory, et la forensics cloud qui s'appuie sur les journaux natifs des fournisseurs de services cloud. Les quarante pourcent d'attaques fileless en 2023 rendent l'analyse mémoire incontournable. En France, soixante-dix pourcent des affaires cyber portées devant les tribunaux sont rejetées ou affaiblies faute de preuves numériques correctement collectées.

---

### Intelligence artificielle en cybersécurité

L'intelligence artificielle appliquée à la cybersécurité désigne l'utilisation du machine learning, du deep learning et des modèles de langage de grande taille pour automatiser la détection de menaces et accélérer la réponse aux incidents. Mais elle accroît aussi la sophistication des attaques.

Du côté défensif, l'UEBA modélise le comportement normal de chaque utilisateur et entité et détecte les déviations statistiques. Les EDR modernes utilisent des modèles de classification pour détecter des malwares inconnus sur la base du comportement plutôt que de signatures, avec des taux de détection supérieurs à quatre-vingt-dix-neuf pourcent sur les malwares connus. Des assistants basés sur des LLM comme Microsoft Copilot for Security et CrowdStrike Charlotte AI permettent aux analystes d'interroger les journaux en langage naturel et de générer automatiquement les requêtes correspondantes.

Du côté offensif, les attaquants utilisent l'IA pour générer des emails de phishing ultra-ciblés, réduisant de quatre-vingt-quinze pourcent le temps de création et augmentant le taux de succès. Les deepfakes audio et vidéo ont causé des pertes supérieures à vingt-cinq millions de dollars dans un seul incident en 2024. Des outils permettent d'automatiser la reconnaissance et l'exploitation de vulnérabilités.

Les modèles d'IA eux-mêmes sont des surfaces d'attaque. L'empoisonnement de modèle, ou data poisoning, consiste à injecter des données malveillantes dans le jeu d'entraînement pour biaiser les détections. Les attaques adversariales modifient imperceptiblement un fichier pour tromper un modèle de machine learning. La prompt injection manipule un assistant LLM via des instructions cachées dans des données qu'il traite. Le référentiel MITRE ATLAS recense ces nouvelles menaces spécifiques aux systèmes d'IA.

---

### Métriques de sécurité

Les métriques de sécurité sont des indicateurs quantifiables permettant de mesurer l'efficacité des contrôles de sécurité, la performance du SOC et la progression de la maturité cyber. Elles permettent de piloter objectivement la cybersécurité et de justifier les investissements auprès de la direction.

Le MTTD, Mean Time To Detect, est le temps moyen entre le début d'une compromission et sa détection. C'est l'indicateur le plus critique car chaque jour supplémentaire augmente l'étendue des dégâts. La référence sectorielle est de seize jours, l'objectif d'un SOC mature est inférieur à vingt-quatre heures pour les incidents critiques. Le MTTR, Mean Time To Respond, est le temps entre la détection et la résolution complète. Il se décompose en MTTC pour le confinement et MTTF pour la correction.

Le CTR, Click-Through Rate, mesure le pourcentage d'employés ayant cliqué sur un lien lors d'une campagne de phishing simulé. Le taux moyen initial est de trente-deux pourcent ; l'objectif après un programme de sensibilisation mature est inférieur à cinq pourcent. Le Report Rate mesure le taux de signalement de mails suspects au SOC. Un report rate élevé transforme les collaborateurs en capteurs humains au profit de l'équipe de sécurité. Les SLA de contrat avec un prestataire de services de sécurité managés définissent des délais précis : un incident de priorité une doit être notifié en moins de quinze minutes, avec un containment sous deux heures. La loi de Goodhart s'applique ici : quand une mesure devient un objectif, elle cesse d'être une bonne mesure. Il faut toujours combiner plusieurs indicateurs complémentaires.

---

### Sensibilisation et facteur humain

La sensibilisation à la sécurité désigne l'ensemble des programmes, formations et pratiques visant à modifier les comportements humains pour réduire le risque cyber. Le facteur humain est impliqué dans soixante-quatorze pourcent des incidents de sécurité.

Un programme de sensibilisation efficace ne se réduit pas à une formation annuelle obligatoire. Le modèle de maturité SANS Security Awareness définit cinq niveaux progressifs, du simple respect des obligations réglementaires jusqu'à l'intégration totale dans la culture d'entreprise. Les composantes d'un programme mature incluent des formations e-learning modulaires et courtes, des simulations de phishing régulières avec formation immédiate post-clic, des newsletters et communications de sécurité, et un suivi par métriques.

Le micro-learning est une approche pédagogique basée sur des contenus courts d'une à cinq minutes, répétés à intervalles réguliers. Elle s'appuie sur la courbe de l'oubli d'Ebbinghaus : sans répétition, quatre-vingts pourcent des informations sont oubliées en trente jours. La gamification augmente l'engagement de soixante pourcent par rapport aux formations classiques. Le Security Champion est un référent sécurité bénévole dans une équipe métier, qui joue le rôle d'ambassadeur entre la direction des systèmes d'information et les collaborateurs. Le nudge, inspiré des sciences comportementales, consiste à orienter naturellement vers le comportement sécurisé en modifiant l'environnement de choix : activer le MFA par défaut plutôt que de le laisser optionnel, ou ajouter une friction sur les virements urgents. Le retour sur investissement moyen d'un programme de sensibilisation mature est de trente-sept pour un euro investi selon le Ponemon Institute.

---

### EBIOS RM et gestion des risques cyber

EBIOS Risk Manager est la méthode française d'analyse et de traitement des risques de sécurité des systèmes d'information, publiée par l'ANSSI en 2018. Elle est la référence recommandée pour les opérateurs d'importance vitale, les opérateurs de services essentiels et les entités soumises à NIS2.

La méthode est structurée en cinq ateliers successifs. L'atelier un porte sur le cadrage et le socle de sécurité : définir le périmètre, identifier les valeurs métier critiques et les biens supports. L'atelier deux identifie les sources de risques pertinentes et leurs objectifs visés, qu'il s'agisse de cybercriminels, d'États, de concurrents ou d'insiders. L'atelier trois construit des scénarios stratégiques à haut niveau pour chaque couple source de risque et objectif visé. L'atelier quatre décline ces scénarios en scénarios opérationnels détaillés, mappés sur le référentiel MITRE ATT&CK. L'atelier cinq définit le plan de traitement des risques avec quatre stratégies possibles : réduire le risque par des mesures de sécurité, transférer le risque vers une assurance cyber, accepter le risque résiduel avec l'accord du management, ou refuser en évitant l'activité trop risquée.

La formule de base du risque est la suivante : un risque est le produit d'une menace, d'une vulnérabilité et d'un impact. Les critères DICT, Disponibilité, Intégrité, Confidentialité et Traçabilité, permettent d'évaluer les besoins de sécurité. FAIR, Factor Analysis of Information Risk, complète EBIOS RM en quantifiant les risques en valeur financière, permettant un dialogue entre le Responsable de la Sécurité des Systèmes d'Information et le directeur financier en termes de perte annuelle prévue.

---

### PCA et PRA

Le Plan de Continuité d'Activité définit les dispositions permettant à une organisation de maintenir ses activités critiques en cas de sinistre. Le Plan de Reprise d'Activité est le volet informatique du PCA : il décrit les procédures pour restaurer les systèmes d'information après une interruption.

L'étape fondatrice est le Business Impact Analysis, ou analyse d'impact sur les activités, qui identifie les processus critiques, leurs dépendances et les impacts d'une interruption sur les plans financier, réglementaire et réputationnel. Elle permet de définir les priorités de reprise et les objectifs de RTO et de RPO.

Les stratégies techniques vont du site de repli à chaud, un environnement miroir opérationnel en temps réel avec un RTO inférieur à une heure, au site à froid, une infrastructure disponible mais à configurer avec un RTO supérieur à vingt-quatre heures, en passant par la réplication cloud. Seulement quarante pourcent des entreprises françaises disposent d'un PCA formalisé et testé, et soixante pourcent des PME victimes d'une cyberattaque majeure mettent la clé sous la porte dans les dix-huit mois. Le règlement DORA impose des PCA et PRA stricts au secteur financier européen depuis janvier 2025, et NIS2 des obligations similaires à toutes les entités essentielles et importantes.

---

### Cyber-assurance

La cyber-assurance est un contrat couvrant les pertes financières liées à un incident de sécurité informatique. Elle est devenue un outil stratégique de transfert du risque résiduel.

Les couvertures typiques se divisent en deux catégories. Les pertes propres, ou first-party, incluent les frais de réponse à incident, les pertes d'exploitation, la restauration des données, les frais de notification RGPD et la gestion de crise. La responsabilité civile, ou third-party, couvre les réclamations de tiers pour violation de données et les frais de défense juridique.

Les assureurs imposent désormais un niveau minimal de maturité cyber avant d'accorder une couverture : authentification multifacteur obligatoire sur les accès distants et les comptes administrateurs, sauvegardes isolées et testées selon la règle 3-2-1-1, plan de réponse aux incidents documenté, et gestion des correctifs à jour. La clause de cyberguerre est un sujet contentieux majeur : l'affaire Merck contre Ace American Insurance a montré son ambiguïté. Merck réclamait un milliard quatre cents millions de dollars pour les dommages causés par NotPetya attribué à la Russie, et la cour du New Jersey a finalement donné raison à Merck en 2023. En France, seulement treize pourcent des PME disposent d'une cyber-assurance selon l'AMRAE.

---

### NIS2

La directive NIS2, Network and Information Security 2, est une directive européenne adoptée en janvier 2023 remplaçant la directive NIS1 de 2016. Elle élargit le champ des entités soumises à des obligations de cybersécurité de cinq cents à dix mille ou quinze mille entités en France.

La directive distingue deux catégories. Les entités essentielles opèrent dans des secteurs hautement critiques comme l'énergie, la santé, les transports, les banques et les infrastructures numériques. Les entités importantes couvrent des secteurs critiques élargis incluant la chimie, l'alimentation, les dispositifs médicaux et les fournisseurs numériques.

Les obligations clés sont au nombre de cinq. La gouvernance rend les dirigeants personnellement responsables de la mise en conformité, avec une obligation de formation à la cybersécurité. La gestion des risques impose une politique de sécurité formalisée. L'article 21 définit les mesures minimales obligatoires : politique de sécurité, gestion des incidents, continuité des activités, sécurité de la chaîne d'approvisionnement, authentification multifacteur et chiffrement. La notification des incidents suit des délais stricts : alerte précoce dans les vingt-quatre heures, notification initiale dans les soixante-douze heures, rapport final dans le mois. La sécurité de la chaîne d'approvisionnement oblige à évaluer les risques liés aux fournisseurs. Les sanctions maximales atteignent dix millions d'euros ou deux pourcent du chiffre d'affaires mondial pour les entités essentielles. L'ANSSI est l'autorité nationale compétente pour NIS2 en France.

---

### ISO 27001 et ISO 27002

L'ISO 27001 est la norme internationale définissant les exigences pour établir, mettre en oeuvre et améliorer un Système de Management de la Sécurité de l'Information, ou SMSI. L'ISO 27002 est son guide de bonnes pratiques. Seule l'ISO 27001 fait l'objet d'une certification.

La version 2022 de la norme regroupe quatre-vingt-treize contrôles en quatre domaines : trente-sept contrôles organisationnels, huit contrôles humains, quatorze contrôles physiques et trente-quatre contrôles technologiques. La version précédente de 2013 en comptait cent quatorze en quatorze domaines. Parmi les onze nouveaux contrôles introduits en 2022 figurent la Threat Intelligence, la sécurité du cloud et la prévention des fuites de données.

Le SMSI suit le cycle PDCA : Planifier pour définir la politique et les risques, Déployer pour implémenter les contrôles, Contrôler pour surveiller et auditer, et Améliorer pour les actions correctives. La certification est valable trois ans avec des audits de surveillance annuels. Plus de soixante-dix mille certificats ont été délivrés dans cent cinquante pays en 2022, et la norme est devenue un prérequis pour de nombreux appels d'offres publics et privés dans les secteurs réglementés. Les quatre-vingt-treize contrôles de l'annexe A couvrent la majorité des mesures obligatoires de l'article 21 de NIS2.

---

### NIST Cybersecurity Framework

Le NIST Cybersecurity Framework est un cadre de référence volontaire développé par l'Institut américain des normes et de la technologie, publié en 2014 et mis à jour en version 2.0 en février 2024. Il structure la gestion des risques cyber en six fonctions et fournit un langage commun pour piloter la cybersécurité à tous les niveaux.

La version 2.0 introduit une sixième fonction nommée GOVERN qui pilote toutes les autres. Les six fonctions sont GOVERN pour la gouvernance stratégique et la politique, IDENTIFY pour l'inventaire des actifs et l'analyse des risques, PROTECT pour les mesures de protection incluant le contrôle d'accès, la sensibilisation et le chiffrement, DETECT pour la surveillance continue et les systèmes de détection, RESPOND pour la gestion des incidents et la communication de crise, et RECOVER pour la restauration des capacités et le retour d'expérience.

Le framework définit quatre niveaux d'implémentation : le Tier 1, partiel et réactif, le Tier 2, informé des risques et partiellement formalisé, le Tier 3, répétable et formalisé, et le Tier 4, adaptatif avec amélioration continue. Le NIST CSF n'est pas certifiable mais est complémentaire à l'ISO 27001 : il est plus flexible et stratégique, adapté à la communication avec la direction, là où l'ISO 27001 est normative et opérationnelle.

---

### Authentification et gestion des accès

L'IAM, Identity and Access Management, désigne l'ensemble des processus et technologies permettant de gérer les identités numériques et de contrôler les droits d'accès. Il repose sur trois piliers : l'authentification, c'est-à-dire qui êtes-vous, l'autorisation, c'est-à-dire qu'avez-vous le droit de faire, et la traçabilité, c'est-à-dire qu'avez-vous fait.

L'authentification multifacteur, ou MFA, combine au moins deux facteurs différents : ce que l'on sait comme un mot de passe, ce que l'on possède comme un token physique ou un smartphone, et ce que l'on est comme la biométrie. L'adoption du MFA réduit de quatre-vingt-dix-neuf virgule neuf pourcent le risque de compromission de compte selon Microsoft. Pourtant, seulement quarante pourcent des entreprises françaises l'ont déployé sur l'ensemble de leurs accès. Le standard FIDO2 et WebAuthn permettent une authentification forte sans mot de passe, résistante au phishing.

Le SSO, Single Sign-On, permet une authentification unique pour accéder à plusieurs applications. Son risque principal est le point unique de défaillance, raison pour laquelle il doit impérativement être couplé au MFA. Le PAM, Privileged Access Management, gère les comptes à privilèges via un coffre-fort de mots de passe, l'enregistrement des sessions et la rotation automatique des identifiants. Le RBAC, Role-Based Access Control, attribue les droits selon le rôle, tandis que l'ABAC, Attribute-Based Access Control, les définit par des attributs contextuels plus granulaires, mieux adaptés au modèle Zero Trust. Le cycle de vie des identités, de la création à la suppression lors du départ d'un collaborateur, est une source majeure de failles si le déprovisionnement n'est pas automatisé.

---

### Outils de sécurité réseau

Les outils de sécurité réseau constituent le socle technique de la posture de sécurité. Un pare-feu mal configuré est à l'origine de quatre-vingt-quinze pourcent des incidents de sécurité réseau selon Gartner.

Le firewall UTM, Unified Threat Management, est un pare-feu de nouvelle génération qui regroupe en une seule appliance le filtrage réseau, la prévention des intrusions, l'antivirus réseau, le filtrage web, le contrôle des applications et le réseau privé virtuel. Les acteurs leaders sont Fortinet, Palo Alto Networks, Check Point et Stormshield pour l'acteur français qualifié par l'ANSSI.

Le WAF, Web Application Firewall, protège les applications web et les interfaces de programmation contre les attaques applicatives de couche 7 : injection SQL, cross-site scripting, et l'ensemble des attaques du référentiel OWASP Top 10. Il est imposé par la norme PCI-DSS pour les sites e-commerce traitant des données de paiement.

Le DLP, Data Loss Prevention, surveille, détecte et bloque les transferts non autorisés de données sensibles sur trois canaux : le réseau, les terminaux et le cloud via les CASB, Cloud Access Security Broker. Le patch management est la gestion systématique des correctifs : les vulnérabilités critiques, c'est-à-dire avec un score CVSS supérieur à neuf, doivent être corrigées en priorité, idéalement sous soixante-douze heures selon NIS2. Le NAC, Network Access Control, contrôle l'accès au réseau en vérifiant la conformité et l'identité de l'équipement, essentiel pour les politiques d'apport de ses propres équipements et la sécurisation des objets connectés. La tendance de fond est le SASE, Secure Access Service Edge, qui converge les fonctions réseau et sécurité dans une architecture cloud-native adaptée aux environnements distribués.

---

### ANSSI et acteurs de la cybersécurité

L'ANSSI, Agence Nationale de la Sécurité des Systèmes d'Information, est l'autorité nationale française en matière de cybersécurité, créée en 2009 sous tutelle du Premier Ministre. Elle est l'interlocuteur de référence pour toute organisation soumise à des obligations réglementaires.

L'ANSSI exerce quatre grandes missions. La défense couvre la protection des systèmes d'information de l'État, des opérateurs d'importance vitale et des entités critiques, via le CERT-FR qui publie alertes et indicateurs de compromission. La régulation fait de l'ANSSI l'autorité compétente pour NIS2 en France, avec pouvoir de qualification et de délivrance de visas de sécurité. La promotion passe par la publication de guides et référentiels gratuits, notamment les quarante-deux mesures d'hygiène et la méthode EBIOS RM. La coordination internationale représente la France auprès de l'ENISA, l'agence européenne de cybersécurité, et de l'OTAN.

La qualification SecNumCloud est délivrée aux prestataires de services cloud garantissant un niveau de sécurité élevé et une immunité aux lois extra-territoriales étrangères comme le Cloud Act américain. Elle est exigée pour héberger les données sensibles de l'État dans le cadre de la doctrine "cloud au centre." La plateforme cybermalveillance.gouv.fr est le dispositif national d'assistance aux victimes, principalement les particuliers, les TPE et PME et les collectivités. Le Campus Cyber, inauguré en 2022 à La Défense, rassemble deux cents organisations membres et trois mille experts dans un hub de référence de l'écosystème cyber français. En 2023, l'ANSSI a traité trois mille sept cents événements de sécurité signalés et conduit cent quatre-vingt-sept opérations de cyberdéfense.

---

## Questions que le jury pourrait poser

Voici les questions que le jury est susceptible de poser lors du grand oral sur le thème de la cybersécurité.

Quelles sont les principales menaces cyber pour une PME en 2025 ?

SOC interne ou externalisé : comment choisir pour une entreprise de taille intermédiaire ?

Comment sensibiliser efficacement les collaborateurs à la cybersécurité ?

Qu'est-ce que le modèle Zero Trust et pourquoi remplace-t-il l'approche périmétrique ?

Comment l'intelligence artificielle transforme-t-elle la détection des menaces ?

Quelle est la différence entre un EDR, un XDR et un NDR ?

Comment réaliser une analyse de risques avec EBIOS Risk Manager ?

Quelles sont les obligations de NIS2 pour les entreprises ?

PCA et PRA : comment les adapter face aux ransomwares ?

Quel est le rôle du Responsable de la Sécurité des Systèmes d'Information face à l'avènement du cloud ?

Comment justifier le budget cybersécurité auprès du comité de direction ?

Quelle est la valeur ajoutée d'une cyber-assurance ?

---

## Points de vigilance

Voici les cinq principaux pièges à éviter lors du grand oral.

**Confondre SIEM et SOAR.** Ces deux outils sont complémentaires mais distincts. Le SIEM détecte et alerte via la corrélation de journaux. Le SOAR agit et automatise la réponse via des playbooks. Un jury attendra que vous expliquiez leur complémentarité et non leur confusion.

**Réduire la cybersécurité à la technique.** La cybersécurité est avant tout une discipline de management. Soixante-quatorze pourcent des incidents impliquent le facteur humain. Les réponses les plus pertinentes articulent dimension technique, gouvernance, sensibilisation et aspects réglementaires. Évitez de rester uniquement sur les outils.

**Présenter Zero Trust comme un produit.** Zero Trust est un modèle architectural et une philosophie, pas une solution logicielle. On ne "déploie" pas Zero Trust en achetant un outil : c'est un projet de transformation qui dure de deux à cinq ans et nécessite une maturité IAM préalable. Plusieurs jurés piègent les candidats sur ce point.

**Oublier le cadre réglementaire français et européen.** NIS2, DORA, RGPD et la Loi de Programmation Militaire sont des cadres réels avec des obligations concrètes, des sanctions chiffrées et des délais précis. Un responsable informatique doit les connaître, pas seulement les citer. Savoir distinguer une entité essentielle d'une entité importante, ou expliquer les délais de notification NIS2, fait la différence.

**Présenter la cybersécurité comme un état atteignable.** La cybersécurité est un processus continu d'amélioration, pas un état final. Le principe d'assume breach signifie que même avec les meilleures défenses, une organisation doit se préparer à être compromise. Mettre en avant la cyber-résilience, la capacité à rebondir rapidement, et les métriques de pilotage continu est beaucoup plus mature que promettre une sécurité absolue.
