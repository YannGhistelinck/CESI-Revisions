---
type: notion
thèmes:
  - IA
  - Management et stratégie
statut: pas vu
dernière_révision: 2026-09-08
---

# Shadow AI

## En bref

### Définition
Le **Shadow AI** désigne l'utilisation non autorisée, non déclarée et non contrôlée d'outils d'IA par des employés dans un contexte professionnel, sans validation de la DSI, de la direction ou des équipes de conformité. Par analogie avec le "shadow IT", il crée des angles morts en matière de sécurité, de conformité et de gouvernance des données.

### Pourquoi c'est important
Depuis l'émergence des IA génératives grand public (ChatGPT, Gemini, Copilot, Claude...), des millions de salariés utilisent ces outils au quotidien pour rédiger, coder, analyser, sans que leurs employeurs en soient nécessairement informés. Cela expose les organisations à des risques majeurs : fuite de données confidentielles, non-conformité RGPD, violation de droits d'auteur, hallucinations présentées comme vérités.

### Chiffres clés
- **65 %** des employés utilisent des outils IA non approuvés par leur employeur (Microsoft Work Trend Index, 2024).
- **55 %** des utilisateurs de ChatGPT en entreprise y transmettent des informations confidentielles (Cyberhaven, 2023).
- **46 %** des dirigeants ignorent que leurs équipes utilisent des outils IA non validés (IBM, 2023).
- Samsung a interdit ChatGPT après que des ingénieurs y ont collé du **code source propriétaire** (avril 2023).

---

## Approfondir

### Fonctionnement

#### Pourquoi le Shadow AI se développe
1. **Pression de productivité** : les outils IA générative offrent des gains de temps immédiats que les employés ne veulent pas manquer.
2. **Lenteur des processus d'approbation** : validation DSI/RSSI souvent longue face à l'agilité des outils SaaS.
3. **Manque de solutions approuvées** : les entreprises n'ont pas encore déployé d'alternatives institutionnelles.
4. **Méconnaissance des risques** : les employés ne réalisent pas que leurs saisies peuvent alimenter les modèles ou être exposées.

#### Risques principaux

| Type de risque | Description | Exemple |
|---|---|---|
| **Fuite de données** | Informations confidentielles envoyées à des serveurs tiers | Code source, données clients, stratégie envoyés à ChatGPT |
| **Non-conformité RGPD** | Traitement de données personnelles sans encadrement légal | Données RH, médicales traitées par une IA hors DPA |
| **Violation droits d'auteur** | Contenus générés potentiellement contrefaisants | Textes, images générées revendiquées par des tiers |
| **Qualité / hallucinations** | Résultats incorrects présentés comme fiables | Analyse juridique erronée, code vulnérable |
| **Risque réputationnel** | Publication de contenu IA non relu et embarrassant | Réponse client générée incorrecte ou discriminatoire |
| **Sécurité** | Injection de prompt, exfiltration de données | Attaque via plugin ou extension IA malveillante |

#### Stratégies de gouvernance du Shadow AI

1. **Détection** : outils DLP (Data Loss Prevention) pour identifier les transferts de données vers des IA non approuvées, surveillance réseau.
2. **Politiques claires** : charte d'utilisation de l'IA, liste blanche des outils approuvés, niveaux de classification des données.
3. **Solutions approuvées** : déploiement d'alternatives sécurisées (Azure OpenAI Service, Copilot for Microsoft 365, instances privées).
4. **Formation et sensibilisation** : expliquer les risques, pas seulement interdire.
5. **Gouvernance IA** : mise en place d'un comité IA, d'un AI Officer, d'un processus d'approbation rapide.
6. **Monitoring continu** : revue régulière des usages, threat intelligence sur les nouveaux outils.

### Avantages / Inconvénients (du phénomène Shadow AI)

| "Avantages" perçus par les utilisateurs | Risques pour l'organisation |
|---|---|
| Gains de productivité immédiats | Fuite de données confidentielles |
| Accès à des outils innovants | Non-conformité RGPD / réglementaire |
| Autonomie et créativité | Perte de contrôle sur les actifs informationnels |
| Contournement de processus jugés lents | Risque juridique (droits d'auteur, responsabilité) |
| | Incohérence dans la qualité des livrables |

### Acteurs
- **Microsoft** : Copilot for Microsoft 365 comme alternative approuvée au Shadow AI.
- **Google** : Gemini for Workspace, déploiement contrôlé en entreprise.
- **Cyberhaven** : éditeur de DLP, études sur les fuites de données via IA.
- **Gartner** : recommandations sur la gouvernance IA en entreprise.
- **ANSSI** : recommandations sur la sécurité des usages IA en entreprise (2024).

### Cas d'usage
- **Samsung (2023)** : fuite de code source via ChatGPT → interdiction immédiate, développement d'une IA interne.
- **Secteur juridique** : avocats utilisant ChatGPT pour rédiger des conclusions avec citations de jurisprudences inexistantes (affaire Mata v. Avianca, USA, 2023).
- **Finance** : analyse financière réalisée avec des données internes non anonymisées sur des outils grand public.
- **Santé** : médecins saisissant des données patients dans des IA grand public pour rédiger des comptes-rendus.

### Chiffres complémentaires
- **10 Md$** de pertes estimées liées aux incidents de sécurité IA en entreprise d'ici 2025 (Gartner).
- **72 %** des entreprises du CAC 40 n'avaient pas de politique formelle de gouvernance IA en 2023 (PAC/CXP).
- Le terme "Shadow AI" est apparu dans le vocabulaire professionnel courant fin **2023**, avec l'essor de ChatGPT.

---

## Flashcards
#flashcards/IA/Shadow_AI #flashcards/Management_et_stratégie/Shadow_AI

**Qu'est-ce que le Shadow AI ?** :: Utilisation non autorisée et non contrôlée d'outils IA par des employés dans un contexte professionnel, sans validation de la DSI ou de la conformité, par analogie avec le shadow IT.

**Quel est le principal risque du Shadow AI pour une organisation ?** :: La fuite de données confidentielles (code source, données clients, stratégie) vers des serveurs tiers hébergeant les IA grand public, sans encadrement contractuel ni mesure de sécurité.

**Citez le cas emblématique de fuite de données via Shadow AI.** :: Samsung (avril 2023) : des ingénieurs ont collé du code source propriétaire dans ChatGPT ; l'entreprise a ensuite interdit l'outil et lancé le développement d'une IA interne.

**Quelles sont les 4 stratégies clés pour gouverner le Shadow AI ?** :: Détection (DLP), politiques claires (charte, liste blanche), déploiement de solutions approuvées, formation et sensibilisation.

**Qu'est-ce qu'un AI Officer ?** :: Responsable en charge de la gouvernance de l'IA dans l'organisation : définition des politiques, approbation des outils, conformité réglementaire et gestion des risques IA.

**Pourquoi le Shadow AI est-il difficile à éradiquer par la seule interdiction ?** :: Car la pression de productivité et les gains immédiat sont réels ; sans alternatives approuvées et accessibles, les employés continueront d'utiliser des outils non contrôlés. La gouvernance doit équilibrer contrôle et adoption.

**Quel article du RGPD est directement concerné par le Shadow AI ?** :: L'art. 28 (sous-traitance) et l'art. 35 (AIPD) — traitement de données personnelles via des tiers (fournisseurs IA) sans DPA ni analyse d'impact préalable.

---

## Sources
- Microsoft, "Work Trend Index 2024 — AI at Work" — [microsoft.com](https://www.microsoft.com/en-us/worklab/work-trend-index)
- Cyberhaven, "The Rise of AI Data Leakage", 2023
- IBM Institute for Business Value, "CEO Study on AI", 2023
- ANSSI, "Recommandations de sécurité pour les systèmes d'IA", 2024
- Gartner, "Top Strategic Technology Trends 2024"

---

## Notions liées
- [[IA de confiance et IA responsable]]
- [[Éthique de l'IA]]
- [[AI Act]]
- [[RGPD]]
- [[Privacy by Design]]
- [[Gouvernance IT]]
- [[DevSecOps]]
- [[Sensibilisation et facteur humain]]
