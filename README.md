# CortexOps AI

AI-powered incident intelligence and root cause detection platform for infrastructure observability.

CortexOps AI simulates distributed microservices environments, detects infrastructure anomalies, correlates incidents across services, and generates automated incident reports for root cause analysis workflows.

---

# Current Features

## Infrastructure Simulation
- Synthetic infrastructure log generation
- Simulated distributed microservices environment
- Realistic service metrics and incident scenarios
- Cascading failure simulation

## Anomaly Detection
- Statistical threshold-based anomaly detection
- Z-score inspired metric analysis
- Detection across multiple infrastructure metrics

## Incident Detection
- Multi-service incident grouping
- Time-window-based incident correlation
- Severity classification

## Incident Reporting
- Automated markdown incident reports
- Infrastructure reasoning summaries
- Recommended troubleshooting steps

---

# Simulated Services

- api-gateway
- auth-service
- payment-service
- notification-service
- inventory-service
- recommendation-engine
- database
- cache-layer

---

# Current Incident Types

- database_slowdown
- cache_failure
- memory_leak
- traffic_spike
- authentication_outage

---

# Project Architecture

```text
logs
   ↓
anomaly detection
   ↓
incident correlation
   ↓
incident reasoning
   ↓
report generation
```

---

# Repository Structure

```text
cortexops-ai/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── simulated/
│
├── notebooks/
│
├── src/
│   └── cortexops_ai/
│       ├── ingestion/
│       ├── detection/
│       ├── reasoning/
│       └── utils/
│
├── outputs/
│   ├── reports/
│   └── screenshots/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Example Log Event

```json
{
  "timestamp": "2026-05-12 18:05:29",
  "service": "payment-service",
  "level": "ERROR",
  "message": "Database connection timeout",
  "latency_ms": 4021,
  "cpu_usage": 91,
  "memory_usage": 87,
  "error_rate": 0.23
}
```

---

# Example Incident Flow

```text
database latency spike
        ↓
payment-service timeout
        ↓
api-gateway failures
        ↓
incident detection
        ↓
incident report generation
```

---

# Tech Stack

## Core
- Python
- Pandas
- NumPy
- scikit-learn

## Planned Infrastructure
- FastAPI
- Kafka
- PostgreSQL
- Redis
- Docker

## Planned MLOps
- MLflow
- EvidentlyAI

## Planned Visualization
- Streamlit
- Plotly
- NetworkX
- Grafana

---

# How To Run

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run Phase 1 pipeline

```bash
PYTHONPATH=src/cortexops_ai python src/cortexops_ai/run_phase1.py
```

---

# Current Outputs

The pipeline generates:

```text
data/simulated/system_logs.csv
data/processed/anomalies.csv
data/processed/incidents.csv
outputs/reports/
```

---

# Example Workflow

```text
Generate logs
    ↓
Detect anomalies
    ↓
Detect incidents
    ↓
Generate incident reports
```

---

# Roadmap

## Phase 1 — Foundation
- [x] Synthetic infrastructure simulation
- [x] Statistical anomaly detection
- [x] Incident grouping
- [x] Automated report generation

## Phase 2 — Incident Intelligence
- [ ] Dependency graph engine
- [ ] Event correlation logic
- [ ] Incident propagation analysis

## Phase 3 — Root Cause Analysis
- [ ] Root cause reasoning engine
- [ ] Service dependency analysis
- [ ] Infrastructure timeline reconstruction

## Phase 4 — Platform Engineering
- [ ] FastAPI backend
- [ ] Streamlit dashboard
- [ ] Docker deployment
- [ ] MLflow integration
- [ ] Kafka streaming

## Phase 5 — Advanced AI Features
- [ ] Drift detection
- [ ] AI incident copilot
- [ ] Historical incident memory
- [ ] Vector similarity search

---

# Vision

CortexOps AI is designed as an AI-powered observability and incident intelligence platform inspired by modern infrastructure monitoring systems such as Datadog, Splunk, and Microsoft Sentinel.

The long-term goal is to build a production-style AI system capable of:
- detecting infrastructure anomalies,
- correlating incidents,
- identifying likely root causes,
- and assisting engineers with automated operational intelligence.

---

# Author

Clara Yousif
