---
type: notion
thèmes:
  - Cybersécurité
  - Mobilité
statut: pas vu
dernière_révision: 
---

# Outils de sécurité réseau

![[N — Outils de sécurité réseau.mp3]]
## En bref
> **Définition** : Les outils de sécurité réseau constituent l'arsenal technique permettant de protéger les infrastructures informatiques contre les intrusions, les malwares, les fuites de données et les vulnérabilités. Ils couvrent un spectre large : du filtrage réseau (firewall, WAF) à la prévention des fuites de données (DLP), en passant par la gestion des vulnérabilités (patch management) et le contrôle des accès réseau (NAC).
> **Pourquoi c'est important** : Pour une DSI, ces outils constituent le socle technique de la posture de sécurité. Leur absence ou leur mauvaise configuration est à l'origine de la majorité des incidents. Ils sont exigés par les référentiels NIS2, ISO 27001, et les cyber-assureurs, et doivent être adaptés aux environnements hybrides (cloud + on-premise) et mobiles.
> **Chiffres clés** :
> - 60 % des violations de données exploitent des vulnérabilités pour lesquelles un patch existait (Ponemon Institute, 2023)
> - Le marché mondial du WAF atteindra 8,6 Mds $ en 2027 (Allied Market Research)
> - Un pare-feu mal configuré est à l'origine de 95 % des incidents de sécurité réseau (Gartner)

## Approfondir

### Fonctionnement

**1. Firewall UTM (Unified Threat Management)**

Le pare-feu UTM est un firewall de nouvelle génération (NGFW) qui regroupe en une seule appliance plusieurs fonctions de sécurité :
- Filtrage de paquets et stateful inspection
- Prévention des intrusions (IPS/IDS)
- Antivirus et anti-malware réseau
- Filtrage de contenu web (URL filtering)
- Contrôle des applications (AppControl)
- VPN (site-à-site et client)
- Inspection SSL/TLS (déchiffrement du trafic HTTPS)

**Avantages vs limites :** Simplifie l'architecture et réduit les coûts de gestion. Peut devenir un goulot d'étranglement sur les très grands débits. Solutions : Fortinet FortiGate, Palo Alto Networks, Check Point, Sophos, Stormshield (français, qualifié ANSSI).

**2. WAF (Web Application Firewall)**

Pare-feu applicatif protégeant les applications web et APIs contre les attaques de couche 7 :
- Injection SQL, XSS (Cross-Site Scripting)
- Attaques OWASP Top 10
- DDoS applicatif
- Bot management (scraping, credential stuffing)

**Modes de déploiement :** en ligne (inline), en écoute (monitoring), reverse proxy, ou cloud (WAF as a Service). Solutions : F5 BIG-IP ASM, Imperva, Cloudflare WAF, AWS WAF, ModSecurity (open source). La norme PCI-DSS impose un WAF pour les sites e-commerce traitant des données de paiement.

**3. DLP (Data Loss Prevention)**

Système de prévention des fuites de données : surveille, détecte et bloque les transferts non autorisés de données sensibles.

**Canaux couverts :**
- DLP réseau (Network DLP) : surveille le trafic sortant (email, web, FTP)
- DLP endpoint : surveille les actions sur les postes (copie USB, impression, capture d'écran)
- DLP cloud (CASB) : surveille les échanges avec les applications SaaS

**Fonctionnement :** Identification du contenu sensible par patterns (numéros de CB, NIR, données personnelles RGPD), empreintes de fichiers, classification. Solutions : Symantec DLP (Broadcom), Forcepoint DLP, Microsoft Purview (ex-MIP), Teramind.

**4. Patch Management**

Gestion systématique des correctifs de sécurité pour maintenir les systèmes à jour et réduire la surface d'attaque.

**Processus :**
1. Inventaire des actifs et des versions logicielles (CMDB)
2. Veille sur les vulnérabilités (CVE, bulletins éditeurs, CERT-FR)
3. Évaluation et priorisation (score CVSS : critique > 9, élevé > 7)
4. Test des patches en environnement de préproduction
5. Déploiement et vérification

**KPIs clés :** délai moyen de correction des vulnérabilités critiques (objectif < 72h pour les CVE critiques selon NIS2), taux de systèmes patchés, fenêtres de maintenance. Solutions : Microsoft WSUS/MECM, Ivanti Patch Management, Qualys VMDR, Tenable.io, ManageEngine Patch Manager Plus.

**5. NAC (Network Access Control)**

Contrôle d'accès au réseau basé sur la conformité de l'équipement et l'identité de l'utilisateur.

**Fonctionnement :** Avant qu'un appareil accède au réseau, le NAC vérifie :
- Identité de l'utilisateur (authentification 802.1X)
- Conformité de l'appareil (OS à jour, antivirus actif, chiffrement activé)
- Profil de risque (appareil personnel vs professionnel, localisation)

Selon le résultat : accès complet, accès limité (VLAN de quarantaine) ou refus d'accès.

**Cas d'usage BYOD et mobilité :** Le NAC est essentiel pour contrôler les appareils personnels des employés (BYOD) et les appareils IoT. Solutions : Cisco ISE (Identity Services Engine), Forescout, Aruba ClearPass, Portnox.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Réduction de la surface d'attaque | Complexité de configuration et de maintenance |
| Protection multicouche (défense en profondeur) | Coût des licences et du matériel |
| Détection et blocage en temps réel | Risque de faux positifs (blocages légitimes) |
| Conformité réglementaire (NIS2, PCI-DSS, ISO 27001) | Performance réseau impactée (inspection SSL notamment) |
| Traçabilité et auditabilité | Nécessite une expertise technique spécialisée |
| Adaptation aux environnements cloud (WAF cloud, CASB) | Contournement possible par des attaques sophistiquées |

### Acteurs et solutions du marché
- **Firewall UTM/NGFW** : Fortinet (leader mondial), Palo Alto Networks, Check Point, Cisco Firepower, Stormshield (qualifié ANSSI), SonicWall
- **WAF** : F5, Imperva, Cloudflare, Akamai, AWS WAF, Azure WAF
- **DLP** : Broadcom/Symantec, Forcepoint, Microsoft Purview, Teramind, Safetica
- **Patch Management** : Qualys, Tenable, Ivanti, ManageEngine, Microsoft Defender Vulnerability Management
- **NAC** : Cisco ISE, Forescout, Aruba ClearPass (HPE), Portnox
- **Solutions françaises qualifiées ANSSI** : Stormshield (Airbus), Wallix (PAM), Gatewatcher (IDS/NDR)

### Cas d'usage concrets
1. **Protection d'un site e-commerce** : Un WAF Cloudflare est déployé devant un site de vente en ligne. Il bloque quotidiennement plusieurs milliers de tentatives d'injection SQL et de credential stuffing, tout en offrant une protection DDoS. La conformité PCI-DSS est maintenue.
2. **Crise ransomware et patch management** : En 2021, la vulnérabilité ProxyLogon (Exchange Server) a été exploitée massivement. Les organisations avec un patch management efficace ont déployé le correctif en moins de 72 heures. Les autres ont subi des compromissions massives, dont plusieurs hôpitaux français.
3. **Sécurisation BYOD dans un hôpital** : Un CHU déploie un NAC (Cisco ISE) pour contrôler l'accès Wi-Fi. Les appareils personnels des soignants sont orientés vers un VLAN restreint (accès internet uniquement), tandis que les équipements médicaux certifiés accèdent au réseau de soins. Les appareils non conformes sont mis en quarantaine.

### Chiffres et tendances
- Le marché mondial des NGFW atteindra 9,5 Mds $ en 2028 (Mordor Intelligence)
- Fortinet est leader du marché NGFW avec 24 % de parts de marché (IDC, 2023)
- Tendance SASE (Secure Access Service Edge) : convergence des fonctions réseau et sécurité (SD-WAN + FWaaS + CASB + ZTNA) dans une architecture cloud-native — réponse aux environnements distribués et mobilité
- L'inspection SSL/TLS est incontournable : 95 % du trafic web est chiffré (Google Transparency Report), nécessitant un déchiffrement pour l'inspection
- NDR (Network Detection and Response) : émergence d'outils d'analyse comportementale du trafic réseau pour détecter les menaces avancées (Darktrace, ExtraHop, Gatewatcher)

## Flashcards
#flashcards/Cybersécurité/Outils_de_sécurité_réseau #flashcards/Mobilité/Outils_de_sécurité_réseau
Qu'est-ce qu'un firewall UTM ? :: Unified Threat Management : firewall de nouvelle génération regroupant plusieurs fonctions de sécurité (IPS, antivirus réseau, filtrage URL, contrôle d'applications, VPN) en une seule appliance.

Quelle est la différence entre un firewall classique et un WAF ? :: Un firewall classique filtre le trafic réseau (couches 3-4, IP/ports). Un WAF (Web Application Firewall) analyse le contenu applicatif HTTP/HTTPS (couche 7) pour bloquer les attaques web (injection SQL, XSS, OWASP Top 10).

Qu'est-ce que le DLP et quels canaux couvre-t-il ? :: Data Loss Prevention : système qui surveille et bloque les transferts non autorisés de données sensibles. Couvre les canaux réseau (email, web), endpoint (USB, impression) et cloud (SaaS via CASB).

Comment prioriser le patch management ? :: En utilisant le score CVSS (Common Vulnerability Scoring System). Les CVE critiques (score > 9) doivent être corrigées en priorité, idéalement sous 72 heures selon NIS2. Les vulnérabilités sont suivies via le CERT-FR et les bulletins éditeurs.

Qu'est-ce que le NAC et à quoi sert-il ? :: Network Access Control : contrôle l'accès au réseau en vérifiant la conformité de l'appareil (OS à jour, antivirus, chiffrement) et l'identité de l'utilisateur (802.1X). Essentiel pour les politiques BYOD et la sécurisation des IoT.

Qu'est-ce que le SASE et pourquoi est-ce une tendance ? :: Secure Access Service Edge : architecture cloud-native qui converge les fonctions réseau (SD-WAN) et sécurité (firewall, CASB, ZTNA) en un service unifié. Répond aux besoins des environnements distribués, du télétravail et de la mobilité.

Quel score CVSS déclenche un patch en urgence ? :: Un score CVSS supérieur ou égal à 9 (critique). Les CVE élevées (7-8.9) sont traitées sous 30 jours, les moyennes (4-6.9) sous 90 jours. Les objectifs varient selon la criticité des systèmes.

## Sources
- ANSSI — Guide de l'hygiène informatique (42 mesures), dont patch management
- CERT-FR — Bulletins de sécurité et alertes CVE
- OWASP — Top 10 Web Application Security Risks 2021
- Ponemon Institute — Cost of a Data Breach Report 2023
- Gartner — Magic Quadrant for Network Firewalls 2023
- IDC — Worldwide Network Security Market Shares 2023

## Notions liées
- [[Authentification et gestion des accès (IAM)]]
- [[NIST Cybersecurity Framework]]
- [[ISO 27001 - 27002]]
- [[NIS2]]
- [[PCA - PRA]]
- [[ANSSI et acteurs de la cybersécurité]]
