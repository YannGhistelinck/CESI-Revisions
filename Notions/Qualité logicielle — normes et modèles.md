---
type: notion
thèmes:
  - Développement
statut: pas vu
dernière_révision: 
---

# Qualité logicielle — normes et modèles

## En bref
> **Définition** : La qualité logicielle désigne l'ensemble des propriétés d'un logiciel lui permettant de satisfaire des besoins exprimés ou implicites. Elle est évaluée selon des modèles normalisés qui structurent les critères de qualité en caractéristiques mesurables.
> **Pourquoi c'est important** : Pour une DSI, disposer d'un référentiel commun de qualité permet de contractualiser des exigences avec les prestataires, d'objectiver les décisions d'acceptation, et de réduire les coûts de maintenance. La qualité logicielle est un levier direct de réduction du risque projet.
> **Chiffres clés** :
> - Les défauts non détectés en phase de conception coûtent en moyenne **100 fois plus cher** à corriger en production (NIST, 2002).
> - Selon le Standish Group (CHAOS Report 2020), seulement **31 % des projets logiciels** se terminent dans les délais, le budget et le périmètre prévus.
> - La norme ISO 25010 identifie **8 caractéristiques de qualité** principales et plus de 30 sous-caractéristiques.

## Approfondir

### Fonctionnement

#### Modèle de McCall (1977)
Premier modèle structuré de qualité logicielle, organisé en **3 axes** :
- **Révision du produit** : maintenabilité, flexibilité, testabilité.
- **Transition du produit** : portabilité, réutilisabilité, interopérabilité.
- **Opération du produit** : correction, fiabilité, efficacité, intégrité, facilité d'utilisation.

McCall propose des facteurs de qualité mesurés via des critères et des métriques. C'est une approche hiérarchique : Facteur → Critère → Métrique.

#### Modèle de Boehm (1978)
Étend McCall en ajoutant la notion de **portabilité** et en structurant la qualité selon des caractéristiques de haut niveau (utilité générale, maintenabilité, portabilité), qui se décomposent récursivement jusqu'à des primitives mesurables. Boehm introduit explicitement les compromis entre caractéristiques (ex. : efficacité vs portabilité).

#### FURPS+ (Grady, HP, 1987)
Acronyme utilisé dans le Unified Process (UP/RUP) :
- **F**unctionality — fonctionnalités et sécurité.
- **U**sability — facilité d'utilisation, documentation.
- **R**eliability — fréquence des défaillances, récupérabilité.
- **P**erformance — temps de réponse, débit, utilisation ressources.
- **S**upportability — maintenabilité, adaptabilité, testabilité.
- **+** : contraintes de conception, d'implémentation, d'interface, physiques.

FURPS+ est couramment utilisé pour rédiger des exigences non fonctionnelles dans les spécifications.

#### ISO 9126 (1991–2004)
Norme internationale structurant la qualité logicielle en **6 caractéristiques** : fonctionnalité, fiabilité, facilité d'utilisation, efficacité, maintenabilité, portabilité. Chaque caractéristique se décompose en sous-caractéristiques. ISO 9126 distingue :
- **Qualité interne** : propriétés du code source (métriques statiques).
- **Qualité externe** : comportement observable à l'exécution.
- **Qualité en utilisation** : satisfaction de l'utilisateur dans son contexte réel (efficacité, productivité, sécurité, satisfaction).

#### ISO 25010 / SQuaRE (2011, révisée 2023)
La norme **SQuaRE** (Systems and software Quality Requirements and Evaluation) remplace ISO 9126 et constitue la référence actuelle. Elle est organisée en plusieurs parties (ISO 2500x) :
- **ISO 25010** : modèle de qualité du produit (8 caractéristiques) et qualité en utilisation.
- **ISO 25012** : modèle de qualité des données.
- **ISO 25023** : métriques de qualité.

Les **8 caractéristiques ISO 25010** (version 2011) :
1. Adéquation fonctionnelle
2. Efficacité de performance
3. Compatibilité
4. Facilité d'utilisation
5. Fiabilité
6. Sécurité
7. Maintenabilité
8. Portabilité

La révision 2023 ajoute **Sûreté** (Safety) et réorganise certaines sous-caractéristiques.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Fournit un langage commun entre équipes et parties prenantes | Les modèles anciens (McCall, Boehm) sont peu adaptés aux systèmes distribués et agiles |
| Permet de contractualiser et d'auditer la qualité | ISO 25010 est perçue comme complexe et difficile à mesurer exhaustivement |
| Base de référence pour les outils d'analyse de code | Risque de conformité de façade sans véritable amélioration de la qualité réelle |
| ISO 25010 couvre les systèmes et les données, pas seulement le logiciel | Nécessite des outils et compétences spécifiques pour mesurer les métriques |
| Facilite les appels d'offres et la sélection de prestataires | Les caractéristiques peuvent être contradictoires (sécurité vs performance) |

### Acteurs et solutions du marché
- **SonarQube / SonarCloud** (Sonar) : mesure automatisée de qualité interne (maintenabilité, fiabilité, sécurité), alignée ISO 25010.
- **CAST Highlight / CAST Imaging** : analyse de portefeuille applicatif, calcul de dette technique et de niveau de qualité.
- **Coverity** (Synopsys) : analyse statique orientée fiabilité et sécurité.
- **NDepend** (.NET), **PMD** (Java) : métriques de complexité, couplage, conformité aux règles de qualité.
- **Jira + plugins qualité** : suivi des indicateurs de qualité dans le cycle de vie projet.

### Cas d'usage concrets
1. **Appel d'offres DSI** : une DSI rédige ses exigences non fonctionnelles en utilisant FURPS+ ou ISO 25010 comme grille, permettant d'évaluer objectivement les offres des ESN candidates.
2. **Audit d'un legacy** : une entreprise utilise CAST pour mesurer la qualité de son ERP vieillissant avant migration, en quantifiant la dette technique selon les critères ISO 25010 (maintenabilité, fiabilité).
3. **Quality Gate CI/CD** : une équipe DevOps configure SonarQube avec des seuils basés sur les sous-caractéristiques ISO 25010 (ex. : taux de duplication < 3 %, couverture de tests > 80 %) comme condition bloquante avant déploiement.

### Chiffres et tendances
- Le marché des outils de qualité logicielle est estimé à **7,8 Md$ en 2024**, avec une croissance annuelle de ~12 % (MarketsandMarkets).
- ISO 25010 est la norme de référence citée dans **70 % des appels d'offres** de grands comptes en Europe pour les systèmes critiques.
- La révision 2023 d'ISO 25010 intègre la **sûreté fonctionnelle** (Safety), répondant aux enjeux des systèmes embarqués et de l'IA.

## Flashcards
#flashcards
Quel modèle de qualité organise les critères selon 3 axes : Opération, Révision, Transition ? :: Le modèle de **McCall** (1977).

Quelle norme remplace ISO 9126 et constitue la référence actuelle pour la qualité logicielle ? :: **ISO 25010** (famille SQuaRE — ISO 2500x), publiée en 2011 et révisée en 2023.

Quelle est la différence entre qualité interne, externe et en utilisation selon ISO 9126/25010 ? :: Qualité **interne** = propriétés du code (statique) ; qualité **externe** = comportement observable à l'exécution ; qualité **en utilisation** = satisfaction dans le contexte réel de l'utilisateur.

Que signifie l'acronyme FURPS+ ? :: **F**unctionality, **U**sability, **R**eliability, **P**erformance, **S**upportability, **+** (contraintes design, implémentation, interface, physiques).

Quelles sont les 8 caractéristiques de qualité de la norme ISO 25010 (2011) ? :: Adéquation fonctionnelle, Efficacité de performance, Compatibilité, Facilité d'utilisation, Fiabilité, Sécurité, Maintenabilité, Portabilité.

Quelle nouvelle caractéristique la révision 2023 d'ISO 25010 ajoute-t-elle ? :: La **Sûreté** (Safety), répondant aux enjeux des systèmes embarqués et de l'IA.

Quel outil de qualité logicielle est le plus utilisé comme "Quality Gate" en CI/CD ? :: **SonarQube** (ou SonarCloud pour le cloud), édité par Sonar.

## Sources
- ISO/IEC 25010:2011 — Systems and software engineering — SQuaRE
- ISO/IEC 25010:2023 — révision
- McCall, J.A. (1977). *Factors in Software Quality*. RADC-TR-77-369.
- Boehm, B.W. (1978). *Characteristics of Software Quality*. North-Holland.
- Grady, R.B. & Caswell, D.L. (1987). *Software Metrics: Establishing a Company-Wide Program*. HP / Prentice Hall.
- NIST (2002). *The Economic Impacts of Inadequate Infrastructure for Software Testing*.
- Standish Group. *CHAOS Report 2020*.

## Notions liées
- [[CMMI]]
- [[Analyse de code (SAST - DAST)]]
- [[Clean Code et refactoring]]
- [[Dette technique]]
- [[Maintenance logicielle]]
