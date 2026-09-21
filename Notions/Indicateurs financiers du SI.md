---
type: notion
thèmes:
  - Transversal
statut: pas vu
dernière_révision: 
---

# Indicateurs financiers du SI

## En bref
> **Définition** : Les indicateurs financiers du SI désignent les outils comptables et analytiques permettant à un DSI de lire la santé financière d'une organisation, de construire un business case solide et de justifier un investissement IT devant un CODIR. Ils couvrent le bilan, le compte de résultat, les indicateurs de liquidité (BFR, FRNG, trésorerie) et les indicateurs de rentabilité (marge, seuil de rentabilité, coût de revient).
> **Pourquoi c'est important** : Un DSI qui maîtrise le langage financier parle le même langage que le DAF et le DG. Comprendre le bilan permet de positionner un projet IT dans son contexte financier réel, d'anticiper les contraintes de trésorerie et de dimensionner les investissements de manière réaliste.
> **Chiffres clés** :
> - 60 % des projets IT dépassent leur budget initial (Standish Group, CHAOS Report 2023).
> - Seuls 34 % des DSI se déclarent à l'aise avec la lecture d'un bilan comptable (Harvey Nash/KPMG CIO Survey, 2022).
> - Le coût total de possession (TCO) d'un ERP sur 5 ans est en moyenne 2,5x le coût d'acquisition initial (Gartner, 2022).

## Approfondir

### Fonctionnement

**Le bilan comptable**

Le bilan est une photographie de la situation patrimoniale de l'entreprise à un instant T. Il est équilibré : Actif = Passif.

| ACTIF (emplois) | PASSIF (ressources) |
|-----------------|---------------------|
| **Actif immobilisé** (long terme) | **Capitaux propres** |
| - Immobilisations incorporelles (licences, brevets, logiciels) | - Capital social |
| - Immobilisations corporelles (serveurs, équipements) | - Réserves |
| - Immobilisations financières (participations) | - Résultat de l'exercice |
| **Actif circulant** (court terme) | **Dettes** |
| - Stocks | - Dettes financières (emprunts) |
| - Créances clients | - Dettes fournisseurs |
| - Disponibilités (trésorerie) | - Dettes fiscales et sociales |

*Lecture DSI* : Les investissements IT (serveurs, licences logicielles, développements capitalisés) apparaissent en actif immobilisé. L'amortissement annuel réduit la valeur nette comptable et constitue une charge dans le compte de résultat.

**Le compte de résultat**

Le compte de résultat mesure la performance sur une période (généralement l'exercice annuel). Il enregistre les flux de produits et de charges.

```
Chiffre d'Affaires (CA)
- Coût des marchandises vendues / coût de production
= Marge brute
- Charges d'exploitation (personnel, loyers, SI...)
= EBE (Excédent Brut d'Exploitation) ou EBITDA
- Amortissements et provisions
= Résultat d'exploitation (REX) ou EBIT
+/- Résultat financier (intérêts d'emprunts...)
= Résultat courant avant impôt
- Impôt sur les sociétés (IS)
= Résultat net
```

*Lecture DSI* : Le budget IT figure dans les charges d'exploitation. Un projet IT capitalisé (actif immobilisé) n'impacte pas immédiatement le résultat mais via l'amortissement annuel.

**Le BFR et le FRNG**

Ces deux indicateurs mesurent l'équilibre financier de l'entreprise :

- **FRNG (Fonds de Roulement Net Global)** = Ressources stables (capitaux propres + dettes LT) − Emplois stables (actif immobilisé). Il mesure le "matelas" de ressources à long terme disponible pour financer le cycle d'exploitation.

- **BFR (Besoin en Fonds de Roulement)** = Actif circulant d'exploitation (stocks + créances clients) − Passif circulant d'exploitation (dettes fournisseurs). Il mesure le besoin de financement généré par le cycle d'exploitation.

- **Trésorerie nette** = FRNG − BFR. Si positif : l'entreprise dispose de liquidités. Si négatif : tension de trésorerie.

*Impact IT* : Un grand projet SI (ERP, migration cloud) peut dégrader temporairement le BFR (décaissements avant bénéfices) et créer une tension de trésorerie. Le DSI doit anticiper ces impacts avec le DAF.

**Le seuil de rentabilité (point mort)**

Le seuil de rentabilité est le niveau de CA à partir duquel l'entreprise couvre l'ensemble de ses charges (fixes + variables) et commence à dégager un bénéfice.

```
Seuil de rentabilité = Charges fixes / Taux de marge sur coûts variables
Taux de marge sur coûts variables = (CA - Charges variables) / CA
```

*Application IT* : Pour un projet SaaS ou une prestation de service IT, le point mort détermine à partir de combien de clients/utilisateurs le service devient rentable.

**Marges**

- **Marge brute** = CA − Coût des marchandises vendues. Mesure la rentabilité commerciale brute.
- **Marge nette** = Résultat net / CA. Indicateur de rentabilité globale (après toutes charges et impôts).
- **Marge d'EBITDA** = EBITDA / CA. Indicateur de performance opérationnelle avant amortissements.

**Les amortissements**

L'amortissement répartit le coût d'un actif immobilisé sur sa durée d'utilisation.

| Type d'actif IT | Durée d'amortissement courante |
|-----------------|-------------------------------|
| Matériel informatique | 3 à 5 ans |
| Logiciels acquis | 1 à 3 ans |
| Développements capitalisés | 3 à 5 ans |
| Infrastructure cloud (IaaS capitalisé) | 3 à 7 ans |

*Règle* : Un projet IT avec amortissement sur 5 ans génère une charge annuelle de 20 % du coût total dans le compte de résultat.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Langage commun avec le DAF et le CODIR | Maîtrise comptable non intuitive pour les profils techniques |
| Meilleure justification des investissements IT | Vision financière pas suffisante seule (il faut aussi VAN/TRI) |
| Anticipation des impacts de trésorerie | Données comptables souvent disponibles avec délai |
| Positionnement DSI comme partenaire stratégique | Risque de sur-optimisation financière au détriment de la qualité |

### Acteurs et solutions du marché

**Outils ERP/Finance**
- **SAP FI/CO** — module finance référence en entreprise.
- **Sage** — PME françaises (Sage 100, Sage X3).
- **Cegid** — secteur comptable/retail français.
- **Oracle Fusion Financials** — grands comptes.

**Contrôle de gestion SI**
- Outils de gestion de portefeuille projets (PPM) : Planview, Clarity PPM, Microsoft Project Online.
- Outil de FinOps Cloud (optimisation coûts cloud) : CloudHealth, Apptio Cloudability.

### Cas d'usage concrets

1. **Justification d'une migration cloud** : Le DSI présente au CODIR un tableau comparatif TCO On-premise vs Cloud sur 5 ans, incluant les coûts d'infrastructure, de licences, de personnel, d'amortissements et la trésorerie nette attendue à fin de période.

2. **Arbitrage entre achat de licence et développement sur mesure** : Analyse des charges d'exploitation (OPEX) vs investissement capitalisé (CAPEX), impact sur le résultat d'exploitation selon chaque option.

3. **Business case ERP PME** : Calcul du seuil de rentabilité du projet (à partir de combien d'années le projet couvre son coût ?), avec présentation du BFR prévisionnel pendant la phase de déploiement.

### Chiffres et tendances

- Le ratio "budget IT / CA" moyen est de 3,2 % en France (toutes industries, 2023), avec des écarts de 1 % (industrie) à 8 % (banque/assurance) (Syntec Numérique, 2023).
- 73 % des entreprises qui formalisent leur TCO réduisent leur budget IT de plus de 15 % dans les 2 ans suivants (Forrester, 2022).
- Le FinOps cloud représente en 2024 un enjeu moyen de 28 % de réduction des coûts cloud non optimisés (FinOps Foundation, State of FinOps 2024).

## Flashcards
#flashcards/Transversal/Indicateurs_financiers_du_SI

Qu'est-ce que le BFR et comment se calcule-t-il ? :: Besoin en Fonds de Roulement = Actif circulant d'exploitation (stocks + créances clients) − Passif circulant d'exploitation (dettes fournisseurs). Il mesure le besoin de financement du cycle d'exploitation.

Quelle est la relation entre FRNG, BFR et trésorerie nette ? :: Trésorerie nette = FRNG − BFR. Si positive : l'entreprise a des liquidités. Si négative : tension de trésorerie.

Comment se calcule le seuil de rentabilité ? :: Charges fixes / Taux de marge sur coûts variables, avec Taux de marge sur CV = (CA − Charges variables) / CA.

Quelle est la différence entre CAPEX et OPEX dans un contexte IT ? :: CAPEX (Capital Expenditure) = investissement capitalisé à l'actif et amorti (ex : achat de serveurs). OPEX (Operating Expenditure) = charge d'exploitation immédiate (ex : abonnement SaaS, maintenance). Le cloud transforme du CAPEX en OPEX.

Quelle est la structure d'un compte de résultat simplifié ? :: CA → Marge brute → EBE/EBITDA → Résultat d'exploitation (REX/EBIT) → Résultat courant → Résultat net (après IS).

Sur combien d'années amortit-on le matériel informatique en général ? :: 3 à 5 ans. Les logiciels acquis : 1 à 3 ans. Les développements capitalisés : 3 à 5 ans.

Pourquoi un DSI doit-il maîtriser la lecture d'un bilan ? :: Pour positionner les investissements IT dans le contexte financier réel de l'entreprise, anticiper les impacts sur la trésorerie, et parler le même langage que le DAF et le CODIR lors des arbitrages budgétaires.

Qu'est-ce que l'EBITDA et pourquoi est-il utilisé ? :: Earnings Before Interest, Taxes, Depreciation and Amortization (EBE en français). Mesure la performance opérationnelle avant effets comptables (amortissements) et financiers. Permet de comparer des entreprises indépendamment de leurs choix d'amortissement.

Comment un grand projet IT impacte-t-il le BFR ? :: Il peut dégrader temporairement le BFR car les décaissements interviennent avant que les bénéfices soient générés, créant une tension de trésorerie que le DSI doit anticiper avec le DAF.

## Sources
- Plan Comptable Général (PCG) — Autorité des Normes Comptables (ANC) — https://www.anc.gouv.fr
- Vernimmen — *Finance d'entreprise* (édition annuelle) — Dalloz.
- Gartner — *IT Key Metrics Data* (2022-2023).
- FinOps Foundation — *State of FinOps 2024* — https://data.finops.org
- Standish Group — *CHAOS Report 2023*.

## Notions liées
- [[VAN - TRI - Payback]]
- [[Tableau de Bord DSI]]
- [[RACI et outils de gouvernance projet]]
- [[Outils ITSM]]
- [[Système d'Information (SI)]]
