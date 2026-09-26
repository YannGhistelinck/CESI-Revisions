---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# MDR

![[N — MDR.mp3]]
## En bref
> **Définition** : Le MDR (Managed Detection and Response) est un service managé de cybersécurité qui combine technologie (EDR/XDR, SIEM), expertise humaine (analystes SOC) et processus de réponse pour détecter et traiter les menaces en continu, 24/7. Contrairement à un MSSP classique qui se contente de surveiller et d'alerter, le MDR inclut la réponse active aux incidents (confinement, investigation, remédiation guidée).
> **Pourquoi c'est important** : La pénurie mondiale de talents en cybersécurité (3,5 millions de postes non pourvus selon ISC², 2024) rend impossible pour la majorité des PME et ETI de monter un SOC interne compétent. Le MDR démocratise l'accès à une détection et réponse de niveau enterprise, sans nécessiter d'équipe interne spécialisée.
> **Chiffres clés** :
> - Le marché mondial du MDR atteindra 9,5 Md$ en 2028 (MarketsandMarkets, 2024).
> - Les organisations utilisant un service MDR réduisent le temps moyen de réponse à un incident de 80 % (Forrester, 2023).
> - 65 % des PME/ETI européennes prévoient d'adopter un service MDR d'ici 2026 (Gartner).

## Approfondir

### Fonctionnement

**Chaîne de valeur MDR**
```
Déploiement agents (EDR/XDR) → Collecte télémétrie 24/7 → 
Détection automatique (IA/ML + règles) → Triage par analystes SOC → 
Investigation approfondie → Réponse active (confinement, remédiation) → 
Rapport et recommandations
```

**Ce qui distingue le MDR**
1. **Réponse active** : le prestataire MDR ne se contente pas d'alerter — il peut isoler un endpoint compromis, bloquer un processus malveillant, ou révoquer des accès, selon un mandat préétabli avec le client.
2. **Threat hunting proactif** : les analystes MDR recherchent activement des menaces non détectées par les outils automatiques, en explorant la télémétrie historique.
3. **Expertise humaine intégrée** : des analystes SOC N2/N3 sont inclus dans le service, pas en option.

**MDR vs MSSP vs SOC interne**

| Critère | SOC interne | MSSP | MDR |
|---------|-------------|------|-----|
| Détection | Oui | Oui | Oui |
| Réponse active | Oui | Non (alertes seulement) | Oui |
| Threat hunting | Selon les ressources | Rarement | Oui |
| Investissement initial | Très élevé | Modéré | Modéré |
| Compétences requises en interne | Élevées | Faibles | Faibles |
| Personnalisation | Maximale | Limitée | Bonne |
| Adapté aux PME | Non | Partiellement | Oui |

**MDR vs PDIS**

| Critère | MDR | PDIS |
|---------|-----|------|
| Origine | Marché international (Gartner) | Qualification française ANSSI |
| Scope | Détection + réponse | Détection uniquement |
| Certification | Pas de certification obligatoire | Qualification ANSSI obligatoire pour OIV |
| Public | Toute organisation | OIV, OSE, entités soumises à NIS2 |
| Souveraineté | Variable selon le prestataire | Garantie (données en France, personnel habilité) |

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection et réponse 24/7 sans SOC interne | Dépendance à un prestataire externe |
| Accès à des analystes experts N2/N3 | Moindre connaissance du contexte métier du client |
| Déploiement rapide (semaines vs mois pour un SOC) | Coût récurrent (abonnement mensuel/endpoint) |
| Threat hunting proactif inclus | Périmètre de réponse limité au mandat |
| Scalable (ajout d'endpoints simple) | Risque de vendor lock-in sur la stack technologique |
| Réduction drastique du MTTR | Enjeux de souveraineté des données (cloud US) |

### Acteurs et solutions du marché

| Éditeur | Spécificité |
|---------|-------------|
| **CrowdStrike Falcon Complete** | MDR premium, réponse en <1h, leader Gartner |
| **SentinelOne Vigilance** | MDR automatisé + analystes, bon rapport qualité/prix |
| **Microsoft Defender Experts** | MDR natif pour l'écosystème Microsoft 365 |
| **Sophos MDR** | Leader PME, intégration multi-éditeurs (Open XDR) |
| **Arctic Wolf** | Spécialiste MDR pur, forte croissance |
| **Orange Cyberdefense** | Acteur européen, offre MDR + qualification PDIS |
| **Advens** | MDR français, spécialiste ETI/grands comptes |

### Cas d'usage concrets

1. **PME industrielle (200 salariés)** : n'ayant ni RSSI ni SOC, l'entreprise souscrit un service MDR. En 3 semaines, des agents EDR sont déployés sur les 300 endpoints. Deux mois après, le MDR détecte et contient une attaque ransomware à 2h du matin : l'endpoint patient zéro est isolé en 12 minutes, le chiffrement est stoppé à 3 postes. Sans MDR, l'attaque aurait touché l'ensemble du SI.

2. **ETI dans la santé** : soumise à NIS2, l'ETI choisit un MDR français pour bénéficier de la souveraineté des données. Le service inclut du threat hunting trimestriel qui révèle un accès persistant non détecté (backdoor installée 6 mois plus tôt via une vulnérabilité VPN). Remédiation complète en 48h.

### Chiffres et tendances
- Gartner prédit que d'ici 2028, 60 % des organisations utiliseront un service MDR (contre 30 % en 2024).
- Le coût moyen d'un MDR est de 15-40 €/endpoint/mois, contre 200-500 K€/an pour un SOC interne minimal.
- La convergence MDR + PDIS est une tendance française : les PDIS qualifiés proposent désormais des offres MDR pour élargir leur marché au-delà des OIV.
- L'IA générative est intégrée dans les plateformes MDR (CrowdStrike Charlotte AI, SentinelOne Purple AI) pour accélérer l'investigation.

## Flashcards
#flashcards/Cybersécurité/MDR

Qu'est-ce que le MDR et en quoi diffère-t-il d'un MSSP ? :: Le MDR (Managed Detection and Response) est un service managé combinant technologie et analystes pour détecter ET répondre activement aux menaces 24/7. Le MSSP traditionnel se limite à surveiller et alerter, sans réponse active.

Quels sont les 3 éléments distinctifs d'un service MDR ? :: 1. Réponse active (confinement, remédiation), pas seulement des alertes. 2. Threat hunting proactif par des analystes. 3. Expertise humaine N2/N3 intégrée dans le service.

Quelle est la différence entre MDR et PDIS ? :: Le MDR est un service commercial international (détection + réponse). Le PDIS est une qualification ANSSI française (détection uniquement), obligatoire pour les OIV. Le PDIS garantit la souveraineté ; le MDR offre un scope plus large.

Pourquoi le MDR est-il particulièrement adapté aux PME ? :: Les PME n'ont ni les budgets (200-500 K€/an pour un SOC interne) ni les talents (pénurie mondiale de 3,5M de profils cyber) pour monter un SOC. Le MDR offre une détection et réponse 24/7 à 15-40 €/endpoint/mois.

Citez 3 acteurs majeurs du MDR. :: CrowdStrike Falcon Complete (leader, réponse <1h), Sophos MDR (leader PME, multi-éditeurs), Orange Cyberdefense (acteur européen, combinant MDR et qualification PDIS).

## Sources
- Gartner — *Market Guide for Managed Detection and Response Services*, 2024
- Forrester — *The Forrester Wave: MDR Services*, 2023
- ISC² — *Cybersecurity Workforce Study*, 2024
- MarketsandMarkets — *MDR Market Forecast*, 2024

## Notions liées
- [[EDR - XDR - NDR]]
- [[SOC]]
- [[SIEM]]
- [[SOAR]]
- [[PDIS]]
- [[ANSSI et acteurs de la cybersécurité]]
- [[Menaces cyber]]
- [[Cyber-résilience]]
