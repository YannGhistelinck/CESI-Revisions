---
type: notion
thèmes:
  - Transversal
statut: pas vu
dernière_révision: 
---

## En bref

### Définition
La **VAN** (Valeur Actuelle Nette), le **TRI** (Taux de Rendement Interne) et le **Payback** (délai de récupération) sont les trois indicateurs financiers fondamentaux pour évaluer la rentabilité d'un investissement ou d'un projet. Ils constituent le socle de tout business case IT sérieux.

### Pourquoi c'est important
Décider d'investir dans un ERP, une migration cloud, une infrastructure de cybersécurité ou un projet de data warehouse nécessite de justifier financièrement le choix devant un CODIR. Ces trois indicateurs permettent de répondre à : "Cet investissement crée-t-il de la valeur ? En combien de temps récupère-t-on la mise ?"

### Chiffres clés
- Un projet est acceptable si **VAN > 0** (il crée de la valeur) et **TRI > WACC** (il surperforme le coût du capital).
- Le WACC (Weighted Average Cost of Capital) des entreprises du CAC 40 oscille entre **7 % et 10 %** selon les secteurs (2023-2024).
- **60 %** des projets IT dépassent leur budget initial (rapport Standish Group, CHAOS Report 2023) — d'où l'importance d'un business case rigoureux.

---

## Approfondir

### Fonctionnement

#### Valeur Actuelle Nette (VAN)

La VAN actualise l'ensemble des flux de trésorerie futurs générés par un projet pour les ramener à leur valeur aujourd'hui, en tenant compte du coût du temps et du risque.

**Formule :**

> VAN = −I₀ + Σ [ CFₜ / (1 + r)ᵗ ]

- **I₀** : investissement initial (négatif, décaissement)
- **CFₜ** : cash-flow net à la période t (gains − coûts)
- **r** : taux d'actualisation (généralement le WACC ou un taux de risque ajusté)
- **t** : période (année 1, 2, 3…)

**Interprétation :**

| VAN | Interprétation |
|---|---|
| VAN > 0 | Le projet crée de la valeur → à retenir |
| VAN = 0 | Le projet couvre exactement le coût du capital → neutre |
| VAN < 0 | Le projet détruit de la valeur → à rejeter (sauf contrainte stratégique) |

#### Taux de Rendement Interne (TRI)

Le TRI est le taux d'actualisation qui rend la VAN nulle. C'est le rendement intrinsèque du projet.

**Formule implicite (résolution numérique) :**

> 0 = −I₀ + Σ [ CFₜ / (1 + TRI)ᵗ ]

**Règle de décision :**
- Si **TRI > WACC** → le projet est rentable (il rémunère mieux que le coût du capital).
- Si **TRI < WACC** → le projet ne couvre pas le coût de financement → à rejeter.
- Entre deux projets, on préfère celui avec le TRI le plus élevé (toutes choses égales par ailleurs).

**Limite du TRI** : il suppose que les flux intermédiaires sont réinvestis au même taux (hypothèse souvent irréaliste). On lui préfère parfois le **TRI Modifié (TRIM)** ou on le couple systématiquement à la VAN.

#### Payback (Délai de récupération)

Le Payback mesure le temps nécessaire pour récupérer l'investissement initial grâce aux cash-flows générés.

**Payback simple :**
> Payback = I₀ / CF annuel moyen (si les flux sont constants)

**Payback actualisé** : on cumule les cash-flows actualisés jusqu'à ce que leur somme atteigne I₀. Plus prudent car il tient compte de la valeur temps de l'argent.

**Interprétation** : Plus le Payback est court, moins le projet est risqué. C'est l'indicateur privilégié dans les environnements incertains ou à cycle technologique court (IT).

### Avantages / Inconvénients

| Indicateur | Avantages | Inconvénients |
|---|---|---|
| **VAN** | Mesure la création de valeur absolue ; tient compte de la valeur temps | Très sensible au taux d'actualisation choisi |
| **TRI** | Indépendant du montant investi ; facile à comparer au WACC | Peut être multiple (plusieurs TRI si flux alternent) ; hypothèse de réinvestissement irréaliste |
| **Payback** | Simple, intuitif, rapide à calculer | Ignore les flux après le seuil de récupération ; ne mesure pas la rentabilité globale |

### Acteurs / Outils
- **Qui l'utilise** : DAF, contrôleur de gestion, chef de projet, DSI lors de la construction d'un business case.
- **Outils** : Excel (VAN avec fonction `VAN()`, TRI avec `TRI()`), PowerPoint pour la présentation CODIR, outils de PPM (Planview, Clarity).
- **Contexte CESI** : indispensable dans les livrables de cadrage projet (dossier d'opportunité, business case).

### Cas d'usage concrets en IT

**Exemple : Migration vers le cloud (AWS)**

| Année | Investissement | Économies réalisées | CF net | CF actualisé (r=8%) |
|---|---|---|---|---|
| 0 | −150 000 € | 0 | −150 000 € | −150 000 € |
| 1 | 0 | 40 000 € | 40 000 € | 37 037 € |
| 2 | 0 | 55 000 € | 55 000 € | 47 150 € |
| 3 | 0 | 65 000 € | 65 000 € | 51 603 € |
| 4 | 0 | 60 000 € | 60 000 € | 44 101 € |
| **Total** | | | | **29 891 €** |

- **VAN = +29 891 €** → le projet crée de la valeur → à retenir.
- **TRI ≈ 14 %** > WACC de 8 % → rentable.
- **Payback simple ≈ 2 ans 10 mois**.
- **Payback actualisé ≈ 3 ans 5 mois**.

### Chiffres et tendances
- Le **WACC moyen des entreprises tech** européennes est autour de **9-11 %** (Damodaran, 2024).
- Les DSI utilisent un Payback cible de **2 à 3 ans** maximum pour les projets IT d'infrastructure.
- Dans les projets d'IA/ML, la VAN est souvent difficile à calculer sur des gains intangibles : on utilise des proxies monétaires ou des analyses de sensibilité.

---

## Flashcards
#flashcards/Transversal/VAN_TRI_Payback

Qu'est-ce que la VAN et comment l'interpréter ? :: La Valeur Actuelle Nette actualise tous les flux futurs d'un projet. **VAN > 0** = le projet crée de la valeur et doit être retenu. **VAN < 0** = le projet détruit de la valeur. Formule : VAN = −I₀ + Σ [CFₜ / (1+r)ᵗ].

Qu'est-ce que le TRI et comment le comparer ? :: Le Taux de Rendement Interne est le taux qui annule la VAN. Si **TRI > WACC**, le projet est rentable. Si TRI < WACC, il ne couvre pas le coût du capital et doit être rejeté.

Quelle est la principale limite du TRI ? :: Le TRI suppose que les flux intermédiaires sont réinvestis au même taux (irréaliste en pratique). Il peut aussi être multiple si les flux changent de signe plusieurs fois. Il doit toujours être couplé à la VAN.

Quelle est la différence entre Payback simple et Payback actualisé ? :: Le Payback **simple** divise l'investissement par le flux annuel moyen sans actualisation. Le Payback **actualisé** cumule les flux actualisés jusqu'à récupérer I₀ — plus prudent car il intègre la valeur temps de l'argent.

Quel taux utiliser pour actualiser dans la VAN ? :: Généralement le **WACC** (coût moyen pondéré du capital), qui reflète le coût de financement de l'entreprise. Il peut être majoré d'une prime de risque spécifique au projet.

Dans quel document du projet trouve-t-on VAN, TRI et Payback ? :: Dans le **business case** (dossier d'opportunité ou d'investissement), présenté au CODIR ou au comité de pilotage pour valider le lancement du projet.

Pourquoi le Payback est-il particulièrement utilisé en IT ? :: Parce que les technologies évoluent vite et que les directions souhaitent limiter leur exposition au risque. Un Payback court (2-3 ans) garantit que l'investissement est récupéré avant que la technologie ne soit obsolète.

---

## Sources
- Brealey, Myers & Allen — *Principles of Corporate Finance* (McGraw-Hill, 13e éd.)
- Damodaran, A. — *Investment Valuation* (Wiley, 3e éd.) + bases de données WACC (damodaran.com)
- Standish Group — *CHAOS Report 2023*
- PMI — *Business Analysis for Practitioners: A Practice Guide* (2015)

---

## Notions liées
- [[AMDEC]]
- [[SWOT - PESTEL]]
- [[Matrice de Kraljic]]
- [[Méthode MoSCoW]]
