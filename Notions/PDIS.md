---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# PDIS

![[N — PDIS.mp3]]
## En bref
> **Définition** : Un PDIS (Prestataire de Détection d'Incidents de Sécurité) est un organisme qualifié par l'ANSSI pour fournir des services de détection d'incidents de sécurité informatique. La qualification PDIS, créée en 2017 et encadrée par le référentiel d'exigences de l'ANSSI, garantit que le prestataire dispose des compétences techniques, organisationnelles et de confidentialité nécessaires pour surveiller un SI et détecter les attaques. Elle est obligatoire pour les OIV (Opérateurs d'Importance Vitale) qui externalisent leur détection.
> **Pourquoi c'est important** : La détection des incidents est le maillon critique de la chaîne de cybersécurité : sans détection, pas de réponse. Les OIV et OSE (Opérateurs de Services Essentiels) sont légalement tenus de mettre en place des systèmes de détection d'incidents (Loi de Programmation Militaire 2013, directive NIS/NIS2). Le recours à un PDIS qualifié ANSSI offre une garantie de qualité et de souveraineté.
> **Chiffres clés** :
> - Seulement 5 prestataires sont qualifiés PDIS par l'ANSSI en 2024 (source : ANSSI, liste des prestataires qualifiés).
> - Le délai moyen de détection d'une intrusion est de 204 jours sans SOC externalisé (IBM Cost of a Data Breach, 2023).
> - 249 OIV français sont soumis à l'obligation de détection d'incidents (estimation publique).

## Approfondir

### Fonctionnement

**Cadre réglementaire**
La qualification PDIS s'inscrit dans un écosystème réglementaire français :
- **LPM 2013** (Loi de Programmation Militaire) : impose aux OIV de mettre en place des systèmes de détection et de notifier les incidents à l'ANSSI.
- **Directive NIS / NIS2** : étend les obligations aux OSE et aux entités essentielles/importantes.
- **Référentiel PDIS de l'ANSSI** : définit les exigences pour la qualification (dernière version : 2.0).

**Processus de qualification ANSSI**
1. **Candidature** : le prestataire soumet un dossier à l'ANSSI.
2. **Audit** : un organisme d'évaluation agréé (COFRAC) audite le prestataire sur les exigences techniques, organisationnelles et de sécurité.
3. **Qualification** : l'ANSSI délivre la qualification pour 3 ans, renouvelable.
4. **Surveillance** : audits de suivi intermédiaires.

**Exigences clés du référentiel PDIS**

| Catégorie | Exigences principales |
|-----------|----------------------|
| **Techniques** | SOC opérationnel 24/7, sondes de détection qualifiées, capacité d'analyse de logs, corrélation d'événements |
| **Organisationnelles** | Personnel habilité, processus formalisés, gestion des astreintes, reporting |
| **Confidentialité** | Localisation des données en France, habilitation du personnel, cloisonnement des clients |
| **Réactivité** | Notification du client sous 2h en cas d'incident majeur, escalade vers le CERT |

**PDIS vs PRIS**
| | PDIS | PRIS |
|---|---|---|
| **Fonction** | Détection des incidents | Réponse aux incidents |
| **Activité** | Surveillance continue, analyse, alertes | Investigation, remédiation, forensics |
| **Analogie** | La vigie qui repère le danger | Les pompiers qui interviennent |
| **Qualification ANSSI** | Oui (référentiel PDIS) | Oui (référentiel PRIS) |

**Relation avec le SOC**
Le PDIS opère ou supervise un SOC (Security Operations Center) pour le compte de ses clients. La chaîne est :
```
Sources de logs → Collecte (agents, syslog) → SIEM (corrélation) → 
Analystes SOC (N1/N2/N3) → Alerte client → Escalade CERT/PRIS si nécessaire
```

Les sondes de détection déployées chez le client (sondes réseau qualifiées ANSSI) alimentent le SOC du PDIS.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Garantie de compétence certifiée par l'ANSSI | Nombre très limité de prestataires qualifiés |
| Souveraineté (données en France, personnel habilité) | Coût élevé (SOC 24/7 qualifié) |
| Conformité réglementaire OIV/NIS2 | Délais d'obtention de la qualification (12-18 mois) |
| Détection 24/7 avec expertise cyber de haut niveau | Dépendance à un prestataire externe |
| Notification rapide et escalade formalisée | Complexité d'intégration des sondes chez le client |

### Prestataires qualifiés PDIS (2024)
| Prestataire | Profil |
|-------------|--------|
| **Thales** | Grand groupe défense, SOC à Élancourt |
| **Orange Cyberdefense** | Filiale cybersécurité d'Orange, leader européen des MSSP |
| **Atos (Eviden)** | ESN, SOC européen intégré |
| **Capgemini** | ESN, activité cybersécurité en forte croissance |
| **CS Group (désormais ATOS)** | Historique défense et spatial |

*Note : la liste exacte peut varier, consulter le site de l'ANSSI pour la liste à jour.*

### Cas d'usage concrets

1. **OIV du secteur énergie** : un opérateur d'importance vitale dans l'énergie externalise sa détection d'incidents auprès d'un PDIS qualifié. Des sondes réseau qualifiées sont déployées sur les points névralgiques du SI industriel (OT) et du SI de gestion. Le PDIS détecte une tentative de reconnaissance réseau ciblant les automates industriels et alerte l'OIV en moins de 2 heures.

2. **Collectivité territoriale soumise à NIS2** : avec l'extension NIS2 aux collectivités, une métropole choisit un PDIS qualifié pour la surveillance de son SI. Le SOC du PDIS corrèle les logs Active Directory, pare-feu et messagerie, et détecte une compromission de compte administrateur via du phishing ciblé.

### Chiffres et tendances
- L'ANSSI a qualifié moins de 10 PDIS depuis la création du référentiel en 2017, reflétant le niveau d'exigence élevé.
- NIS2 (transposition 2024-2025) va considérablement élargir le nombre d'entités devant recourir à des services de détection qualifiés.
- Le marché français des services managés de cybersécurité (SOC, MDR) croît de 15 % par an (PAC, 2024).
- L'ANSSI publie régulièrement des guides de recommandations pour la détection d'incidents, complémentaires au référentiel PDIS.

## Flashcards
#flashcards/Cybersécurité/PDIS

Qu'est-ce qu'un PDIS et qui délivre la qualification ? :: Prestataire de Détection d'Incidents de Sécurité, qualifié par l'ANSSI. Il fournit des services de surveillance et de détection d'attaques pour les organisations, avec un niveau de compétence et de confidentialité certifié.

Quelle est la différence entre PDIS et PRIS ? :: Le PDIS détecte les incidents (surveillance continue, SOC, alertes). Le PRIS répond aux incidents (investigation, remédiation, forensics). Le PDIS est la vigie, le PRIS est l'équipe d'intervention.

Pourquoi la qualification PDIS est-elle obligatoire pour les OIV ? :: La Loi de Programmation Militaire (2013) impose aux OIV de mettre en place des systèmes de détection d'incidents. S'ils externalisent cette fonction, ils doivent recourir à un PDIS qualifié ANSSI pour garantir la compétence et la souveraineté.

Quelles sont les principales exigences du référentiel PDIS ? :: SOC opérationnel 24/7, sondes de détection qualifiées, personnel habilité, données localisées en France, notification sous 2h en cas d'incident majeur, processus formalisés et audités.

Combien de prestataires sont qualifiés PDIS par l'ANSSI ? :: Moins de 10 (environ 5 en 2024), ce qui reflète le niveau d'exigence très élevé du référentiel. Parmi eux : Thales, Orange Cyberdefense, Atos/Eviden.

## Sources
- ANSSI — Référentiel d'exigences PDIS v2.0 — www.ssi.gouv.fr
- ANSSI — Liste des prestataires qualifiés — www.ssi.gouv.fr/qualification
- Loi de Programmation Militaire 2013 (LPM) — Art. L.1332-6-1 et suivants
- Directive NIS2 — Directive (UE) 2022/2555

## Notions liées
- [[SOC]]
- [[SIEM]]
- [[SOAR]]
- [[MDR]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[NIS2]]
- [[EDR - XDR - NDR]]
- [[Cyber-résilience]]
