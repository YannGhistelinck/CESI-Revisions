---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Défense en profondeur

![[N — Défense en profondeur.mp3]]
## En bref
> **Définition** : La défense en profondeur est une stratégie de sécurité consistant à superposer plusieurs couches de protection indépendantes (réseau, système, application, données, utilisateur), de sorte que la compromission d'une couche ne suffise pas à compromettre l'ensemble du système. Elle est héritée du concept militaire de défense étagée.
> **Pourquoi c'est important** : Aucun mécanisme de sécurité n'est infaillible. La défense en profondeur garantit qu'un attaquant doit contourner de multiples barrières pour atteindre son objectif, augmentant le temps de détection et réduisant l'impact. Elle est au coeur de la PSSI de toute organisation mature.
> **Chiffres clés** :
> - L'ANSSI identifie 42 mesures d'hygiène informatique comme base minimale pour toute organisation.
> - 80 % des incidents de sécurité auraient pu être évités par l'application de mesures d'hygiène de base (ANSSI).
> - Le coût moyen d'une violation pour les entreprises sans programme de sécurité mature est 2,3 fois supérieur à celui des organisations matures (IBM 2023).

## Approfondir

### Fonctionnement

**Les couches de la défense en profondeur** :
1. **Sécurité physique** : contrôle d'accès aux locaux, salles serveurs, destruction des supports.
2. **Sécurité réseau** : firewall, segmentation, IDS/IPS, DMZ, filtrage DNS, proxy.
3. **Sécurité des postes et serveurs** : antivirus/EDR, gestion des correctifs (patching), durcissement (hardening), chiffrement des disques.
4. **Sécurité des applications** : authentification forte (MFA), contrôles d'entrées, SAST/DAST, WAF.
5. **Sécurité des données** : chiffrement au repos et en transit, DLP, classification des données, contrôle des accès (IAM).
6. **Sécurité organisationnelle** : PSSI, procédures, formation, gestion des incidents.
7. **Sécurité humaine** : sensibilisation, culture de sécurité, human firewall.

**Les 42 mesures d'hygiène informatique de l'ANSSI** : référentiel fondateur publié par l'ANSSI, couvrant 42 mesures regroupées en grandes familles : connaissance du SI, authentification, gestion des accès, mises à jour, sauvegardes, journalisation, gestion des incidents. Ces mesures constituent le socle minimal recommandé pour toute organisation, quelle que soit sa taille.

**PSSI (Politique de Sécurité des Systèmes d'Information)** : document de référence définissant les objectifs, les règles, les responsabilités et les mesures de sécurité d'une organisation. Validée par la direction, elle gouverne l'ensemble des pratiques SSI. Elle est obligatoire pour les OIV (Opérateurs d'Importance Vitale) et les opérateurs de services essentiels (OSE).

**Human firewall** : concept selon lequel chaque employé est une couche de défense. Un utilisateur formé, vigilant et qui applique les bons réflexes (signaler un email suspect, vérifier l'identité d'un appelant, ne pas brancher une clé USB inconnue) constitue une barrière réelle contre les attaques d'ingénierie sociale.

**Principe de defense en profondeur vs sécurité périmétrique** : la sécurité périmétrique (tout protéger en périphérie, "château fort") est insuffisante car une fois le périmètre franchi, l'attaquant a accès à tout. La défense en profondeur postule que le périmètre sera franchi et prépare des défenses internes.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Résistance à la compromission d'une couche unique | Complexité de gestion de multiples solutions |
| Ralentit et détecte l'attaquant à chaque couche | Coût cumulé des solutions et de la maintenance |
| Compatible avec toutes les architectures (on-premise, cloud, hybride) | Risque de "sécurité en silo" si les couches ne communiquent pas |
| Référencé dans les normes (ISO 27001, ANSSI, NIST) | Peut créer une fausse impression de sécurité totale |
| Réduit l'impact d'un zero-day ou d'un insider threat | Nécessite une gouvernance et une coordination forte |

### Acteurs et solutions du marché

**Firewall / IDS-IPS** : Palo Alto Networks, Fortinet (FortiGate), Check Point, Stormshield (France, qualifié ANSSI).

**WAF (Web Application Firewall)** : F5, Imperva, Cloudflare WAF, ModSecurity (open source).

**DLP (Data Loss Prevention)** : Symantec DLP (Broadcom), Microsoft Purview, Forcepoint.

**Gestion des correctifs** : Ivanti, ManageEngine, Microsoft WSUS/SCCM, Qualys VMDR.

**Chiffrement** : VeraCrypt, BitLocker (Microsoft), solutions HSM (Thales, Entrust).

**Référentiels et cadres** : ANSSI (42 mesures, guides sectoriels), ISO/IEC 27001, NIST Cybersecurity Framework, CIS Controls.

### Cas d'usage concrets

1. **OIV et NIS2** : les Opérateurs d'Importance Vitale (énergie, transports, santé) et les opérateurs couverts par la directive NIS2 (2024) sont contraints par la réglementation d'appliquer une défense en profondeur formalisée dans une PSSI. L'ANSSI audite leur conformité.

2. **Attaque stoppée en couche 3** : lors de l'attaque NotPetya (2017), les organisations ayant correctement segmenté leur réseau (couche réseau) ont contenu la propagation. Celles sans segmentation ont vu le malware se propager à l'ensemble du SI.

3. **Secteur bancaire** : les établissements financiers appliquent la défense en profondeur sous la supervision de l'ACPR et conformément aux guidelines EBA. Exemple : double validation humaine pour les virements (procédure = couche organisationnelle) + MFA + DLP.

### Chiffres et tendances
- La directive NIS2 (transposée en France en 2024) impose à plus de 10 000 entités françaises supplémentaires de mettre en place des mesures de défense en profondeur.
- Le NIST Cybersecurity Framework 2.0 (2024) intègre désormais la gouvernance (Govern) comme pilier principal, aux côtés d'Identify, Protect, Detect, Respond, Recover.
- Les organisations appliquant les 20 contrôles CIS réduisent leur surface d'attaque de 85 % selon le Center for Internet Security.

## Flashcards
#flashcards/Cybersécurité/Défense_en_profondeur
Qu'est-ce que la défense en profondeur ? :: Stratégie consistant à superposer plusieurs couches de protection indépendantes (réseau, système, application, données, humain) pour qu'un attaquant doive contourner chaque barrière successivement.

Quelles sont les 42 mesures de l'ANSSI ? :: Un référentiel de 42 mesures d'hygiène informatique fondamentales publié par l'ANSSI, couvrant la connaissance du SI, l'authentification, la gestion des accès, les mises à jour, les sauvegardes et la journalisation.

Qu'est-ce qu'une PSSI ? :: Politique de Sécurité des Systèmes d'Information : document de référence définissant les objectifs, règles, responsabilités et mesures SSI d'une organisation, validée par la direction.

Qu'est-ce qu'un human firewall ? :: Le concept selon lequel chaque employé est une couche de défense grâce à sa formation, sa vigilance et l'application des bons réflexes face aux tentatives de manipulation.

En quoi la défense en profondeur diffère-t-elle de la sécurité périmétrique ? :: La sécurité périmétrique mise tout sur la frontière extérieure. La défense en profondeur postule que le périmètre sera franchi et construit des barrières internes à chaque couche du SI.

Quel est le cadre américain équivalent aux mesures ANSSI ? :: Le NIST Cybersecurity Framework (CSF) et les CIS Controls, qui définissent des niveaux de maturité et des contrôles prioritaires pour réduire la surface d'attaque.

Pourquoi la NIS2 renforce-t-elle la défense en profondeur en France ? :: La directive NIS2, transposée en 2024, étend les obligations de sécurité à plus de 10 000 nouvelles entités françaises (PME critiques, collectivités), imposant des mesures techniques et organisationnelles formalisées.

## Sources
- ANSSI — Guide d'hygiène informatique (42 mesures) — www.ssi.gouv.fr
- ANSSI — La Défense en profondeur appliquée aux systèmes d'information — www.ssi.gouv.fr
- NIST Cybersecurity Framework 2.0 (2024) — www.nist.gov/cyberframework
- CIS Controls v8 — www.cisecurity.org
- IBM — Cost of a Data Breach Report 2023
- Directive NIS2 — eur-lex.europa.eu (Directive 2022/2555)

## Notions liées
- [[Menaces cyber]]
- [[Ingénierie sociale]]
- [[Zero Trust]]
- [[Cyber-résilience]]
- [[SIEM]]
- [[SOAR]]
- [[EDR - XDR - NDR]]
