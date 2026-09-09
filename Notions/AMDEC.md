---
type: notion
thèmes:
  - Transversal
statut: pas vu
dernière_révision: null
---

## En bref

### Définition
L'AMDEC (Analyse des Modes de Défaillance, de leurs Effets et de leur Criticité) est une méthode d'analyse préventive et structurée visant à identifier, évaluer et hiérarchiser les risques de défaillance d'un système, d'un produit ou d'un processus, avant qu'ils ne surviennent.

### Pourquoi c'est important
L'AMDEC permet d'anticiper les pannes et les erreurs plutôt que de les subir. Dans un projet IT, elle structure la gestion des risques, oriente les plans de mitigation et justifie les choix d'architecture ou de redondance. Elle est exigée dans les secteurs fortement réglementés (aéronautique, automobile, santé, nucléaire) et s'applique désormais largement aux systèmes d'information.

### Chiffres clés
- Méthode développée par l'armée américaine (MIL-P-1629) en **1949**, adoptée par l'industrie automobile dans les années 1970.
- Normalisée par la **CEI 60812** (IEC 60812) pour les systèmes électriques et électroniques.
- Alignée sur **ISO 31000** (management du risque) pour la démarche globale.
- Un IPR supérieur à **100** (sur 1000) est généralement le seuil déclencheur d'un plan d'action obligatoire (seuil variable selon les entreprises).

---

## Approfondir

### Fonctionnement

L'AMDEC se déroule en équipe pluridisciplinaire et suit une logique structurée :

1. **Définir le périmètre** : système analysé, fonctions attendues, frontières.
2. **Identifier les modes de défaillance** : comment chaque composant peut tomber en panne ou dysfonctionner.
3. **Analyser les effets** : conséquences sur le système global et sur l'utilisateur final.
4. **Rechercher les causes** : origines techniques, humaines, environnementales.
5. **Coter la criticité** via l'IPR (Indice de Priorité du Risque) :

| Critère | Signification | Échelle |
|---|---|---|
| **G** — Gravité | Impact de la défaillance sur l'utilisateur/système | 1 (négligeable) → 10 (catastrophique) |
| **O** — Occurrence | Probabilité d'apparition de la cause | 1 (très rare) → 10 (quasi certain) |
| **D** — Détection | Capacité à détecter la défaillance avant impact | 1 (détection certaine) → 10 (indétectable) |

> **IPR = G × O × D** (valeur de 1 à 1 000)

6. **Hiérarchiser** : traiter en priorité les IPR les plus élevés.
7. **Définir les actions correctives** et recalculer l'IPR résiduel.
8. **Suivre l'efficacité** des actions mises en place.

### Types d'AMDEC

| Type | Objet | Exemple IT |
|---|---|---|
| **AMDEC Produit** | Défaillances d'un produit conçu | Analyse d'un firmware embarqué |
| **AMDEC Processus** | Défaillances lors d'un processus de fabrication ou déploiement | Pipeline CI/CD, processus de release |
| **AMDEC Moyen** | Défaillances d'un équipement de production | Serveur de build, baie de stockage |
| **AMDEC Système** | Vision globale d'un système complexe | Architecture micro-services en production |

### Avantages / Inconvénients

| Avantages | Inconvénients |
|---|---|
| Approche proactive et structurée | Chronophage (mobilise une équipe pluridisciplinaire) |
| Priorise objectivement les risques via l'IPR | Subjectivité possible dans la cotation |
| Documentation traçable et auditable | Peut devenir une usine à gaz si le périmètre est trop large |
| Compatible ISO 31000 / IEC 60812 | Nécessite une expertise métier pour être pertinente |
| Applicable à tout domaine (IT, industrie, santé) | Risque de se concentrer sur l'IPR au détriment de la logique de risque |

### Acteurs / Outils

- **Qui anime** : ingénieur qualité, risk manager, architecte système, chef de projet.
- **Qui participe** : représentants de chaque domaine impacté (dev, ops, métier, sécurité).
- **Outils** : tableur Excel/Google Sheets structuré, outils QHSE (Qualnet, Intelex), modules dans des ALM (Jira + plugins).
- **Normes de référence** : IEC 60812, ISO 31000, AIAG-VDA (automotive).

### Cas d'usage concrets en IT

**Cas 1 — Défaillance serveur de production**

| Composant | Mode de défaillance | Effet | G | O | D | IPR | Action |
|---|---|---|---|---|---|---|---|
| Disque dur RAID | Panne simultanée de 2 disques | Perte de données / indisponibilité | 9 | 2 | 3 | 54 | Supervision SMART + remplacement préventif |
| Alimentation redondante | Court-circuit | Coupure serveur | 8 | 1 | 4 | 32 | UPS + test mensuel |

**Cas 2 — Migration vers le cloud**
- Mode : migration partielle de la base de données (script incomplet)
- Effet : incohérence des données entre ancien et nouveau système
- G = 8, O = 4, D = 6 → IPR = **192** → Plan d'action obligatoire : tests de validation, rollback automatisé, fenêtre de migration en heures creuses.

### Chiffres et tendances
- Selon une étude IBM (2023), **67 %** des migrations cloud rencontrent des incidents évitables par une analyse de risque préalable structurée.
- La norme **IEC 60812:2018** a renforcé l'importance de la traçabilité des décisions de mitigation.
- L'AMDEC est un outil clé dans les démarches **DevSecOps** pour anticiper les vulnérabilités dès la phase de conception.

---

## Flashcards
#flashcards

Qu'est-ce que l'IPR dans une AMDEC ? :: L'Indice de Priorité du Risque, calculé par la formule **G × O × D** (Gravité × Occurrence × Détection), sur une échelle de 1 à 1000. Il permet de hiérarchiser les défaillances à traiter en priorité.

Quel est le seuil classique d'IPR déclenchant un plan d'action ? :: Un IPR supérieur à **100** (sur 1000) est le seuil généralement retenu, bien qu'il soit paramétrable selon le contexte et l'entreprise.

Quels sont les 3 types principaux d'AMDEC ? :: AMDEC **Produit** (conception), AMDEC **Processus** (déploiement, fabrication), AMDEC **Moyen** (équipements). Il existe aussi l'AMDEC Système pour une vision globale.

Que signifie un score de Détection élevé (ex. : 9/10) dans une AMDEC ? :: Que la défaillance est **très difficile à détecter** avant qu'elle ne produise ses effets. Un D élevé aggrave donc l'IPR et justifie d'investir dans la supervision ou les tests.

Quelle norme internationale régit l'AMDEC pour les systèmes électriques ? :: La norme **IEC 60812** (CEI 60812), complétée par **ISO 31000** pour le cadre global de management du risque.

Comment l'AMDEC s'intègre-t-elle dans un projet IT agile ? :: Elle peut être réalisée en amont d'un sprint ou d'une release (AMDEC Processus sur le pipeline CI/CD) pour identifier les risques de régression, de déploiement ou de sécurité, et alimenter le backlog de risques.

Quelle est la différence entre AMDEC et analyse de risque ISO 31000 ? :: L'AMDEC est un **outil** d'analyse de risque bottom-up, centré sur les modes de défaillance et leur cotation IPR. ISO 31000 est le **cadre** de management du risque qui définit le processus global (identification, évaluation, traitement, communication). L'AMDEC s'inscrit dans ce cadre.

---

## Sources
- IEC 60812:2018 — *Analysis techniques for system reliability — Procedure for failure mode and effects analysis (FMEA)*
- ISO 31000:2018 — *Management du risque — Lignes directrices*
- AIAG & VDA FMEA Handbook (2019)
- NASA SP-6105 — *Failure Modes and Effects Analysis Guidance*

---

## Notions liées
- [[VAN - TRI - Payback]]
- [[Conduite du changement]]
- [[SWOT - PESTEL]]
- [[Scrum]]
