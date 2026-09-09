---
type: notion
thèmes:
  - Cybersécurité
statut: pas vu
dernière_révision: 
---

# Menaces cyber

## En bref
> **Définition** : Les menaces cyber désignent l'ensemble des attaques informatiques malveillantes visant à compromettre la confidentialité, l'intégrité ou la disponibilité des systèmes d'information. Elles couvrent un spectre large : ransomware, phishing, APT, zero-day et attaques sur la supply chain.
> **Pourquoi c'est important** : Pour une DSI, connaître la taxonomie des menaces est indispensable pour prioriser les investissements en sécurité, choisir les bons outils de détection et construire des plans de réponse adaptés.
> **Chiffres clés** :
> - 66 % des entreprises françaises ont subi au moins une cyberattaque en 2023 (Baromètre CESIN 2024).
> - Le coût moyen d'une violation de données est de 4,45 M$ en 2023 (IBM Cost of a Data Breach 2023).
> - Les ransomwares représentent 24 % des incidents recensés dans le rapport Verizon DBIR 2024.

## Approfondir

### Fonctionnement

**Ransomware** : logiciel malveillant qui chiffre les données de la victime puis exige une rançon (en cryptomonnaie) pour la clé de déchiffrement. La chaîne d'attaque typique : accès initial (phishing, RDP exposé), mouvement latéral, élévation de privilèges, chiffrement de masse.

**RaaS (Ransomware-as-a-Service)** : modèle économique criminel où des développeurs louent leur ransomware à des affiliés (opérateurs). Les affiliés gardent 70-80 % de la rançon. Exemples : LockBit, BlackCat/ALPHV, Cl0p. Ce modèle a industrialisé la cybercriminalité.

**Phishing / Spear phishing / Vishing / Smishing** :
- Phishing : email frauduleux de masse imitant une marque légitime.
- Spear phishing : ciblage précis d'un individu avec personnalisation (nom, poste, contexte).
- Vishing : attaque vocale (téléphone), usurpation d'identité orale.
- Smishing : phishing par SMS.

**BEC (Business Email Compromise) / Fraude au président** : l'attaquant usurpe l'identité d'un dirigeant ou partenaire pour ordonner un virement frauduleux. Vecteur : compromission de boîte mail ou spoofing. Pertes mondiales > 50 Md$ depuis 2013 (FBI IC3 2023).

**APT (Advanced Persistent Threat)** : attaque sophistiquée, longue durée, conduite par un acteur étatique ou para-étatique. Objectif : espionnage, sabotage ou vol de propriété intellectuelle. Exemples : APT28 (Fancy Bear, Russie), APT41 (Chine).

**Zero-day** : vulnérabilité inconnue du fournisseur, sans correctif disponible. Exploitée avant toute divulgation publique. Très prisée sur les marchés noirs (jusqu'à plusieurs millions de dollars).

**Supply chain attack** : compromission d'un fournisseur ou d'une dépendance logicielle pour atteindre les clients finaux. Exemple emblématique : SolarWinds (2020) — backdoor injectée dans des mises à jour légitimes, impactant 18 000 organisations dont des agences gouvernementales américaines.

**Malware polymorphe** : malware qui modifie son code à chaque exécution pour échapper aux signatures antivirales statiques. Nécessite une détection comportementale (EDR).

**Mouvement latéral** : une fois l'accès initial obtenu, l'attaquant se déplace au sein du réseau pour élever ses privilèges et accéder à des cibles à plus forte valeur (Active Directory, serveurs de sauvegarde). Techniques : Pass-the-Hash, Pass-the-Ticket, Kerberoasting.

**Exfiltration** : extraction de données sensibles vers l'extérieur. Souvent précède le chiffrement dans les attaques de double extorsion (payer ou les données sont publiées).

### Avantages / Inconvénients
| Perspective défensive — Connaître les menaces | Limites |
|-----------|---------------|
| Permet de prioriser les mesures de sécurité | Paysage des menaces en évolution constante |
| Facilite la sensibilisation des utilisateurs | Asymétrie attaquant/défenseur (l'attaquant choisit le moment) |
| Permet de construire des scénarios de crise réalistes | Les APT contournent souvent les défenses conventionnelles |
| Base pour le threat intelligence et le threat hunting | Coût élevé d'une veille permanente |

### Acteurs et solutions du marché

**Éditeurs de threat intelligence** : Recorded Future, Mandiant (Google), CrowdStrike Intelligence, Sekoia.io (France).

**Outils de détection** : CrowdStrike Falcon, SentinelOne, Microsoft Defender for Endpoint, ESET.

**Organismes de référence** : ANSSI (France), CISA (USA), ENISA (Europe), CERT-FR.

**Rapports de référence** : Verizon DBIR (annuel), IBM X-Force Threat Intelligence Index, rapport ANSSI sur la menace.

### Cas d'usage concrets

1. **Hôpital de Corbeil-Essonnes (2022)** : attaque ransomware par le groupe PYSA/Mespinoza. Données de patients publiées après refus de payer la rançon de 10 M$. Paralysie des SI pendant plusieurs semaines.

2. **SolarWinds (2020)** : supply chain attack sophistiquée attribuée à APT29 (SVR russe). Backdoor "Sunburst" dans la plateforme Orion. Impact sur le Trésor américain, le Pentagone, Microsoft.

3. **MGM Resorts (2023)** : attaque BEC/social engineering. Les attaquants ont appelé le helpdesk en usurpant l'identité d'un employé pour réinitialiser les accès. Perte estimée : 100 M$.

### Chiffres et tendances
- Verizon DBIR 2024 : 68 % des violations impliquent un facteur humain.
- Le délai médian de détection d'une intrusion est de 21 jours (Mandiant M-Trends 2024), contre 204 jours en 2012 — net progrès.
- Les attaques sur la supply chain logicielle ont augmenté de 742 % entre 2019 et 2022 (Sonatype).
- Marché du RaaS : LockBit seul aurait collecté plus de 91 M$ de rançons aux USA (CISA, 2023).

## Flashcards
#flashcards/Cybersécurité/Menaces_cyber
Qu'est-ce que le RaaS ? :: Ransomware-as-a-Service : modèle où des développeurs criminels louent leur ransomware à des affiliés qui conduisent les attaques et partagent les rançons (généralement 70-80 % pour les affiliés).

Quelle est la différence entre phishing et spear phishing ? :: Le phishing est un envoi de masse non ciblé ; le spear phishing cible précisément un individu avec des informations personnalisées (nom, poste, contexte professionnel) pour augmenter le taux de succès.

Qu'est-ce qu'un zero-day ? :: Une vulnérabilité logicielle inconnue de l'éditeur, sans correctif disponible, exploitée avant toute divulgation publique.

Définir la double extorsion dans les ransomwares. :: L'attaquant chiffre les données ET les exfiltre avant le chiffrement. Il menace de les publier si la rançon n'est pas payée, forçant la victime à payer même si elle dispose de sauvegardes.

Qu'est-ce qu'une APT ? :: Advanced Persistent Threat : attaque longue durée conduite par un acteur étatique ou para-étatique, visant l'espionnage, le sabotage ou le vol de propriété intellectuelle. Ex. : APT28 (Russie), APT41 (Chine).

Qu'est-ce qu'une supply chain attack ? :: Compromission d'un fournisseur ou d'une dépendance logicielle pour atteindre les clients finaux via un canal de confiance. Exemple : SolarWinds 2020.

Qu'est-ce que le mouvement latéral ? :: Technique par laquelle un attaquant, après l'accès initial, se déplace au sein du réseau pour atteindre des cibles à plus haute valeur, via des techniques comme Pass-the-Hash ou Kerberoasting.

## Sources
- ANSSI — Panorama de la cybermenace (rapport annuel) — www.cert.fr
- Verizon Data Breach Investigations Report (DBIR) 2024 — www.verizon.com/business/resources/reports/dbir/
- IBM Cost of a Data Breach Report 2023 — www.ibm.com/security/data-breach
- FBI IC3 — Internet Crime Report 2023 — www.ic3.gov
- CESIN — Baromètre de la cybersécurité des entreprises 2024
- Mandiant M-Trends 2024 — www.mandiant.com/m-trends
- Sonatype — State of the Software Supply Chain 2022

## Notions liées
- [[Ingénierie sociale]]
- [[Zero Trust]]
- [[Défense en profondeur]]
- [[Cyber-résilience]]
- [[SIEM]]
- [[SOAR]]
- [[EDR - XDR - NDR]]
