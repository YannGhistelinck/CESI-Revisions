---
type: notion
thèmes:
  - Cloud et Virtualisation
statut: pas vu
dernière_révision: 
---

# Service Mesh

## En bref
> **Définition** : Un service mesh est une couche d'infrastructure dédiée à la gestion de la communication entre microservices. Il injecte un proxy sidecar (ex : Envoy) à côté de chaque service pour gérer de façon transparente et centralisée le chiffrement mTLS, le routage, la résilience (retries, circuit breakers) et l'observabilité (traces, métriques).
> **Pourquoi c'est important** : Dans une architecture microservices, chaque service doit communiquer de façon sécurisée et fiable avec des dizaines d'autres. Sans service mesh, cette logique est codée dans chaque application (bibliothèques, SDK), créant de la duplication et des risques. Le service mesh externalise cette complexité au niveau de l'infrastructure, simplifiant la vie des équipes de développement et de sécurité.
> **Chiffres clés** :
> - 40 % des entreprises utilisant des microservices en production ont adopté un service mesh en 2023 (CNCF Survey 2023).
> - Istio est le service mesh le plus utilisé : 71 % des utilisateurs de service mesh (CNCF, 2023).
> - Le marché des service meshes devrait dépasser 1,5 Md$ en 2028 (Allied Market Research).

## Approfondir

### Fonctionnement

Un service mesh se compose de deux plans :

**Data Plane (plan de données)**
- Ensemble de proxies légers (*sidecars*) déployés automatiquement à côté de chaque instance de service (pattern Sidecar dans Kubernetes : un conteneur proxy dans le même Pod).
- Le proxy le plus utilisé est **Envoy** (CNCF), un proxy L4/L7 haute performance écrit en C++.
- Tout le trafic réseau entrant/sortant du service passe par le sidecar, de façon transparente pour l'application.

**Control Plane (plan de contrôle)**
- Centralise la configuration et distribue les politiques aux proxies.
- Gère la découverte de services, les certificats mTLS, les règles de routage.
- Exemples : **Istiod** (composant central d'Istio), **Linkerd Control Plane**.

**Fonctionnalités clés :**
- **mTLS (Mutual TLS)** : chiffrement et authentification mutuelle automatiques entre tous les services, sans modifier le code applicatif.
- **Routage avancé** : canary releases, A/B testing, traffic shifting, mirroring.
- **Résilience** : retries automatiques, timeouts, circuit breakers, rate limiting.
- **Observabilité** : génération automatique de métriques (latence, taux d'erreur, throughput), traces distribuées (Jaeger, Zipkin), logs d'accès.
- **Politique de sécurité** : contrôle d'accès fin entre services (AuthorizationPolicy dans Istio).

**Solutions principales :**
- **Istio** : service mesh le plus complet et le plus répandu, développé par Google/IBM/Lyft. Utilise Envoy comme sidecar. Riche en fonctionnalités mais complexe à opérer.
- **Linkerd** : service mesh CNCF, plus léger et plus simple qu'Istio. Utilise des proxies écrits en Rust (linkerd2-proxy). Privilégié pour sa simplicité opérationnelle.
- **Consul Connect (HashiCorp)** : service mesh intégré à Consul, adapté aux environnements hybrides (VMs + conteneurs).
- **AWS App Mesh** : service mesh managé d'AWS, basé sur Envoy.
- **Kuma / Kong Mesh** : service mesh multi-zone supportant Kubernetes et VMs.

**Sidecarless / Ambient Mesh** : évolution récente (Istio Ambient, Linkerd sidecarless) qui élimine le sidecar par pod au profit d'un proxy partagé par nœud, réduisant la consommation de ressources.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Sécurité zero-trust inter-services (mTLS automatique) | Complexité opérationnelle élevée (surtout Istio) |
| Observabilité unifiée sans modifier le code | Surcoût en ressources (CPU/mémoire) dû aux sidecars |
| Résilience (circuit breakers, retries) sans bibliothèque dédiée | Latence additionnelle introduite par les proxies (quelques ms) |
| Routage avancé pour déploiements progressifs (canary, blue/green) | Courbe d'apprentissage importante pour les équipes ops |
| Découplage entre logique applicative et logique réseau | Débogage plus complexe en cas d'incident réseau |
| Politique de sécurité centralisée et auditable | Pas toujours justifié pour des architectures simples |

### Acteurs et solutions du marché
| Acteur | Solution | Particularité |
|--------|----------|---------------|
| Google / IBM | Istio | Le plus complet, écosystème large, CNCF graduated |
| Buoyant | Linkerd | CNCF graduated, le plus simple, proxy Rust ultra-léger |
| HashiCorp | Consul Connect | Multi-plateforme (VMs + K8s), intégré à la suite HashiCorp |
| AWS | App Mesh | Managé, intégré à l'écosystème AWS |
| Kong | Kuma / Kong Mesh | Multi-zone, supporte K8s et VMs |
| Solo.io | Gloo Mesh | Distribution enterprise d'Istio avec UI et support |

### Cas d'usage concrets
1. **Netflix** : utilise un service mesh (basé sur Envoy) pour gérer la communication entre ses centaines de microservices, avec du circuit breaking automatique et des métriques en temps réel sur chaque appel de service.
2. **Lyft** (co-créateur d'Envoy) : a développé Envoy pour résoudre ses propres problèmes de communication inter-services à grande échelle, notamment le contrôle fin du trafic et la gestion des pannes en cascade.
3. **Société Générale** : a adopté Istio sur OpenShift pour sécuriser les communications entre microservices dans ses environnements bancaires, remplaçant des solutions de sécurité réseau traditionnelles par du mTLS automatique.

### Chiffres et tendances
- Istio est devenu un projet CNCF Graduated en 2023, signe de sa maturité.
- L'architecture Ambient Mesh (sans sidecar) représente la prochaine vague : -60 % de consommation CPU par rapport à l'approche sidecar classique (benchmark Istio, 2023).
- 68 % des utilisateurs de service mesh citent la sécurité (mTLS) comme motivation principale (CNCF, 2023).
- La convergence entre API Gateway et Service Mesh s'accélère (Kong, Gloo, Traefik).

## Flashcards
#flashcards/Cloud_et_Virtualisation/Service_Mesh
- Qu'est-ce qu'un service mesh ? :: Une couche d'infrastructure qui gère de façon transparente la communication inter-services (sécurité mTLS, routage, résilience, observabilité) via des proxies sidecars injectés à côté de chaque service.
- Qu'est-ce qu'un proxy sidecar ? :: Un proxy léger (ex : Envoy) déployé dans le même Pod que le service, qui intercepte tout le trafic réseau entrant et sortant sans modification du code applicatif.
- Quelle est la différence entre le Data Plane et le Control Plane d'un service mesh ? :: Le Data Plane est l'ensemble des proxies sidecars qui traitent le trafic ; le Control Plane (ex : Istiod) configure et distribue les politiques à ces proxies.
- Qu'est-ce que le mTLS et pourquoi le service mesh le simplifie-t-il ? :: mTLS (Mutual TLS) est un chiffrement avec authentification mutuelle entre services. Le service mesh l'active automatiquement via les sidecars, sans modifier le code applicatif.
- Quelle est la différence entre Istio et Linkerd ? :: Istio est plus complet et riche en fonctionnalités (mais complexe), Linkerd est plus léger et plus simple à opérer (proxy Rust ultra-léger).
- Qu'est-ce qu'un circuit breaker dans un service mesh ? :: Un mécanisme de résilience qui coupe temporairement les appels vers un service défaillant pour éviter les pannes en cascade, puis teste régulièrement sa disponibilité avant de rétablir le trafic.
- Qu'est-ce que l'Ambient Mesh ? :: Une évolution du service mesh (Istio Ambient, Linkerd) qui supprime le sidecar par pod au profit d'un proxy partagé par nœud, réduisant significativement la consommation de ressources.

## Sources
- CNCF Annual Survey 2023 : https://www.cncf.io/reports/cncf-annual-survey-2023/
- Istio Documentation : https://istio.io/latest/docs/
- Linkerd Documentation : https://linkerd.io/docs/
- Envoy Proxy : https://www.envoyproxy.io/
- Allied Market Research, Service Mesh Market, 2023

## Notions liées
- [[Conteneurisation (Docker - Kubernetes)]]
- [[Cloud Native et 12-Factor App]]
- [[Zero Trust]]
- [[Outils de sécurité réseau]]
- [[Défense en profondeur]]
