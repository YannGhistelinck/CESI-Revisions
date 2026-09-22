---
type: notion
thèmes:
  - Développement
  - Optimisation du SI
statut: pas vu
dernière_révision: 
---

# Observabilité

![[N — Observabilité.mp3]]
## En bref
> **Définition** : L'observabilité est la capacité à comprendre l'état interne d'un système à partir de ses sorties externes (logs, métriques, traces). Empruntée à la théorie du contrôle (Rudolf Kalman, 1960), elle est appliquée aux systèmes distribués depuis les années 2010 par des pionniers comme Twitter et Netflix. **OpenTelemetry** (CNCF, 2019) est devenu le standard universel pour instrumenter les applications et collecter ces données de façon portable.
> **Pourquoi c'est important** : Dans une architecture microservices ou cloud native, un incident peut impliquer des dizaines de services. Le monitoring traditionnel (seuils statiques) ne suffit plus pour diagnostiquer "pourquoi le service X est lent" dans un système distribué. L'observabilité permet de poser n'importe quelle question sur le système sans avoir à le modifier au préalable.
> **Chiffres clés** :
> - Le coût moyen d'une heure d'indisponibilité est de 300 000 $ pour les grandes entreprises (Gartner, 2023).
> - OpenTelemetry est le 2e projet le plus actif de la CNCF après Kubernetes (2024).
> - Les organisations avec une haute observabilité restaurent les services 3,5 fois plus vite (DORA, 2023).

## Approfondir

### Fonctionnement

**Les 3 piliers de l'observabilité**

| Pilier | Définition | Outils | Usage |
|--------|-----------|--------|-------|
| **Logs** | Enregistrement textuel des événements horodatés | ELK Stack, Loki (Grafana), Splunk | Audit, débogage d'erreurs précises, conformité |
| **Métriques** | Données numériques agrégées dans le temps (time series) | Prometheus, InfluxDB, Datadog | Alerting, capacity planning, SLO/SLI |
| **Traces** | Suivi du chemin d'une requête à travers les services distribués | Jaeger, Tempo (Grafana), Zipkin | Performance, identification du bottleneck |

**La différence entre monitoring et observabilité**
- **Monitoring** : surveiller des métriques connues à l'avance (seuils, alertes statiques). On sait ce qu'on cherche.
- **Observabilité** : capacité à explorer et questionner le comportement d'un système pour découvrir des problèmes inconnus. On peut poser des questions non anticipées.

**OpenTelemetry (OTel)**
Standard open source CNCF (fusion d'OpenCensus et OpenTracing en 2019) :
- **SDK** : bibliothèques d'instrumentation pour Java, Python, Go, Node.js, .NET…
- **Collector** : agent/gateway recevant les données OTel et les exportant vers n'importe quel backend (Prometheus, Jaeger, Datadog, Splunk…)
- **Protocole OTLP** : protocole standard pour transmettre logs, métriques et traces
- Avantage : **vendor-neutral** — on change de backend d'observabilité sans modifier le code applicatif

**Architecture typique d'observabilité**
```
Application (SDK OTel) → OTel Collector → 
  ├── Prometheus (métriques) → Grafana (dashboards + alertes)
  ├── Tempo/Jaeger (traces) → Grafana (trace viewer)
  └── Loki (logs) → Grafana (log explorer)
```

**Prometheus — fonctionnement**
- Modèle **pull** : Prometheus scrape (récupère) les métriques des applications à intervalles réguliers
- **PromQL** : langage de requête puissant pour analyser les time series
- **AlertManager** : gestion des alertes (routing, silences, notifications Slack/PagerDuty)
- **Exporters** : adaptateurs pour exposer des métriques d'applications tierces (node_exporter, mysql_exporter…)

**Grafana — fonctionnement**
- Plateforme de visualisation multi-sources (Prometheus, Loki, Tempo, InfluxDB, Elasticsearch…)
- Dashboards configurables, alerting, on-call scheduling (Grafana OnCall)
- Grafana Stack : Mimir (métriques), Loki (logs), Tempo (traces), Pyroscope (profiling) → observabilité complète

**Distributed Tracing**
Une trace est composée de **spans** : chaque span représente une unité de travail dans un service (appel DB, appel HTTP, traitement). Les spans sont reliés par un **trace ID** unique, permettant de visualiser le chemin complet d'une requête et d'identifier le service responsable de la latence.

### Avantages / Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Détection et résolution d'incidents plus rapides (MTTR réduit) | Volume de données élevé (coûts de stockage et d'ingestion) |
| Compréhension des systèmes distribués complexes | Instrumentation initiale du code nécessaire |
| Proactivité (détection avant l'impact utilisateur) | Complexité de mise en place d'une stack complète |
| Support des SLO/SLI/error budget (SRE) | Cardinality issues (métriques à haute cardinalité) |
| Alignement avec les pratiques DevOps/SRE | Nécessite une culture de la donnée dans les équipes |
| Standard OpenTelemetry = évite le vendor lock-in | Risque de "dashboard sprawl" (prolifération sans gouvernance) |

### Acteurs et solutions du marché
| Catégorie | Solutions |
|-----------|-----------|
| Métriques (open source) | Prometheus + AlertManager, InfluxDB, VictoriaMetrics |
| Logs (open source) | Grafana Loki, ELK Stack (Elasticsearch + Logstash + Kibana), OpenSearch |
| Traces (open source) | Jaeger (CNCF), Tempo (Grafana), Zipkin |
| Stack complète (SaaS) | Datadog, Dynatrace, New Relic, Splunk Observability |
| Stack complète (open source) | Grafana Stack (LGTM), OpenTelemetry + backends open source |
| Instrumentation | OpenTelemetry SDK (standard), Micrometer (Java), Pyroscope (profiling) |

### Cas d'usage concrets
1. **Netflix** : Netflix a développé Atlas (métriques) et Edgar (tracing) pour observer ses 700+ microservices. Ils traitent des milliards de métriques par minute. La corrélation logs/métriques/traces permet d'identifier les incidents en moins de 5 minutes sur une plateforme servant 260 millions d'utilisateurs.
2. **Leboncoin** : migration de leur stack de monitoring vers Prometheus + Grafana + Loki (Grafana Stack). Résultat : économie de 70 % sur les coûts d'observabilité vs Datadog, tout en améliorant la visibilité grâce à des dashboards unifiés.
3. **BlaBlaCar** : adoption d'OpenTelemetry pour instrumenter leurs 80+ microservices. La portabilité OTel leur a permis de migrer de Datadog vers Grafana Cloud sans modifier le code applicatif, économisant 300 k€/an en licences.

### Chiffres et tendances
- OpenTelemetry a dépassé 1 milliard d'artefacts téléchargés en 2024 (CNCF).
- Grafana est utilisé par 20 millions de personnes dans le monde (Grafana Labs, 2024).
- Le marché de l'observabilité atteindra 4,1 Md$ en 2028 (MarketsandMarkets).
- Le "profiling continu" (Pyroscope, Parca) devient le 4e pilier de l'observabilité après logs/métriques/traces.

## Flashcards
#flashcards/Développement/Observabilité #flashcards/Optimisation_du_SI/Observabilité
- Quels sont les 3 piliers de l'observabilité ? :: Logs (événements textuels horodatés), métriques (données numériques agrégées en time series), et traces distribuées (suivi du chemin d'une requête à travers les services).
- Quelle est la différence entre monitoring et observabilité ? :: Le monitoring surveille des métriques prédéfinies (on sait ce qu'on cherche). L'observabilité permet d'explorer le comportement d'un système pour répondre à des questions non anticipées (on peut découvrir des problèmes inconnus).
- Qu'est-ce qu'OpenTelemetry et pourquoi est-il important ? :: Un standard open source CNCF pour instrumenter les applications et collecter logs, métriques et traces de façon unifiée et vendor-neutral. Il évite le vendor lock-in en permettant de changer de backend sans modifier le code.
- Comment fonctionne le distributed tracing ? :: Une trace suit le chemin d'une requête à travers les services via un trace ID unique. Chaque service crée des "spans" (unités de travail) reliés entre eux, permettant de visualiser le chemin complet et d'identifier le service responsable de la latence.
- Quelle est la différence entre Prometheus et Grafana ? :: Prometheus est une base de données time series avec un moteur d'alerte (collecte et stocke les métriques). Grafana est un outil de visualisation multi-sources qui interroge Prometheus (et d'autres sources) pour créer des dashboards.
- Qu'est-ce que la "cardinality" et pourquoi est-ce un problème dans Prometheus ? :: La cardinalité est le nombre de combinaisons uniques de labels d'une métrique. Une haute cardinalité (ex. label avec user_id de millions d'utilisateurs) provoque une explosion de la mémoire Prometheus et dégrade les performances.
- Qu'est-ce que le profiling continu et pourquoi est-il considéré comme le 4e pilier de l'observabilité ? :: Le profiling continu capture en permanence l'utilisation CPU/mémoire par fonction de code (via Pyroscope, Parca). Il complète logs/métriques/traces en identifiant précisément quelles lignes de code consomment des ressources, permettant l'optimisation de performance.

## Sources
- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering*, O'Reilly, 2022
- OpenTelemetry documentation : https://opentelemetry.io/
- Prometheus documentation : https://prometheus.io/docs/
- Grafana documentation : https://grafana.com/docs/
- DORA State of DevOps Report 2023 : https://dora.dev/

## Notions liées
- [[DevOps]]
- [[SRE (Site Reliability Engineering)]]
- [[Cloud Native et 12-Factor App]]
- [[Conteneurisation (Docker - Kubernetes)]]
- [[PCA - PRA]]
- [[SIEM]]
