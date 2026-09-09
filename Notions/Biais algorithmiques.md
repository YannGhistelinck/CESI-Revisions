---
type: notion
thèmes:
  - IA
  - Big DATA
statut: pas vu
dernière_révision: 2026-09-08
---

# Biais algorithmiques

## En bref

### Définition
Un **biais algorithmique** est une erreur systématique dans les résultats produits par un algorithme, qui génère des décisions injustes ou discriminatoires envers certains groupes (selon le genre, l'origine ethnique, l'âge, etc.). Il résulte généralement de données d'entraînement biaisées, d'un mauvais choix de variables ou d'un manque de représentativité.

### Pourquoi c'est important
Les algorithmes sont utilisés pour des décisions à fort impact (crédit, recrutement, justice, santé). Un biais non détecté peut amplifier des inégalités existantes à grande échelle, de façon invisible et automatisée, ce qui rend leur correction plus complexe que dans une décision humaine.

### Chiffres clés
- **2016** : ProPublica révèle que le logiciel COMPAS prédit deux fois plus de récidive pour des prévenus noirs que pour des prévenus blancs (à tort).
- **2018** : Étude MIT/Microsoft — les systèmes de reconnaissance faciale de grands éditeurs ont un taux d'erreur de **34 %** sur les femmes à peau foncée vs **< 1 %** sur les hommes à peau claire.
- **Amazon (2018)** : son outil de recrutement par IA pénalisait les CV contenant le mot "femmes" — le projet est abandonné.

---

## Approfondir

### Fonctionnement

1. **Biais dans les données** : les données historiques reflètent des discriminations passées (ex. : moins de femmes promues → l'IA apprend à ne pas les promouvoir).
2. **Proxy variable** : une variable neutre (code postal, prénom) corrèle avec une caractéristique protégée (origine, genre) et introduit une discrimination indirecte.
3. **Boucle de rétroaction (feedback loop)** : l'algorithme prend des décisions qui modifient les données futures, renforçant le biais initial (ex. : surpolice dans certains quartiers → plus d'arrestations → quartier considéré "à risque").
4. **Biais de sélection** : les données collectées ne représentent pas la population cible.
5. **Biais de mesure** : la variable cible (label) est elle-même biaisée (ex. : "récidive" mesurée par de nouvelles arrestations, elles-mêmes biaisées).

### Avantages / Inconvénients

| Avantages des algorithmes (sans biais) | Risques liés aux biais |
|---|---|
| Décisions rapides et à grande échelle | Discrimination systématique et invisible |
| Réduction des biais humains conscients | Amplification des inégalités existantes |
| Reproductibilité et auditabilité potentielle | Opacité des modèles (boîte noire) |
| Cohérence dans l'application des règles | Difficile à contester pour les personnes lésées |

### Acteurs
- **COMPAS (Northpointe)** : outil de prédiction de récidive, cas emblématique de biais racial.
- **IBM AI Fairness 360** : bibliothèque open-source de détection et correction de biais.
- **Fairlearn (Microsoft)** : framework Python pour évaluer et améliorer l'équité des modèles.
- **NIST** : a publié un rapport sur la gestion des biais dans l'IA (NIST SP 1270, 2022).
- **Haute Autorité de Lutte contre les Discriminations (HALDE / Défenseur des droits)** en France.

### Cas d'usage
- **Justice prédictive** : COMPAS aux États-Unis pour la liberté conditionnelle.
- **Recrutement** : outils de tri de CV (Amazon, HireVue).
- **Crédit scoring** : refus de prêt discriminatoire basé sur des proxys.
- **Publicité ciblée** : Meta montrait des offres d'emploi masculines aux hommes, féminines aux femmes.
- **Médical** : algorithme de triage hospitalier (Obermeyer, 2019) sous-estimait la gravité des patients noirs.

### Chiffres complémentaires
- Obermeyer et al. (2019, *Science*) : un algorithme de santé très utilisé aux USA présentait un biais racial significatif, affectant **environ 200 millions de patients**.
- Le marché des outils de fairness IA devrait atteindre **1,5 Md$** d'ici 2028 (MarketsandMarkets).

---

## Flashcards
#flashcards/IA/Biais_algorithmiques #flashcards/Big_DATA/Biais_algorithmiques

**Qu'est-ce qu'un biais algorithmique ?** :: Erreur systématique d'un algorithme produisant des décisions injustes ou discriminatoires envers certains groupes, généralement due à des données biaisées ou des variables proxy.

**Qu'est-ce qu'une variable proxy ?** :: Variable a priori neutre (ex. : code postal) qui corrèle avec une caractéristique protégée (ex. : origine ethnique) et introduit une discrimination indirecte.

**Qu'est-ce qu'une boucle de rétroaction dans les biais IA ?** :: Phénomène où les décisions d'un algorithme modifient les données futures, renforçant le biais initial (ex. : surpolice → plus d'arrestations → quartier "à risque" → surpolice).

**Quel est le cas COMPAS ?** :: Logiciel américain de prédiction de récidive révélé en 2016 par ProPublica comme produisant deux fois plus de faux positifs pour les prévenus noirs que pour les blancs.

**Citez deux frameworks open-source pour détecter les biais IA.** :: IBM AI Fairness 360 et Fairlearn (Microsoft).

**Quels sont les deux grands types d'équité (fairness) en IA ?** :: Équité individuelle (traitement identique pour des individus similaires) et équité de groupe (résultats équivalents entre groupes démographiques).

**Pourquoi les biais algorithmiques sont-ils plus dangereux que les biais humains ?** :: Ils s'appliquent à grande échelle, de façon automatique, reproductible et souvent opaque, rendant la contestation et la correction plus difficiles.

---

## Sources
- ProPublica, "Machine Bias", 2016 — [propublica.org](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
- Buolamwini & Gebru, "Gender Shades", MIT, 2018
- Obermeyer et al., "Dissecting racial bias in an algorithm", *Science*, 2019
- NIST SP 1270 — Towards a Standard for Identifying and Managing Bias in Artificial Intelligence, 2022
- European Commission, "Ethics Guidelines for Trustworthy AI", HLEG, 2019

---

## Notions liées
- [[Audit algorithmique]]
- [[IA de confiance et IA responsable]]
- [[Éthique de l'IA]]
- [[AI Act]]
- [[RGPD]]
- [[Profilage et surveillance]]
