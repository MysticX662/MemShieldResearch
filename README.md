<div align="center">

# MemShield: Mitigating Persistent Memory Poisoning in Stateful AI Agents

[![Paper](https://img.shields.io/badge/White%20Paper-PDF-red)](paper/MemShield_WhitePaper_Final.pdf)
[![Published by RevSoc](https://img.shields.io/badge/Publisher-RevSoc%20Research-1f6feb)](https://revsoc.ai/research/memshield)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A three-layer defensive middleware architecture for protecting long-term memory in stateful autonomous AI agents.**

**Author:** Nickhil Earla  
**Publisher:** RevSoc Research Division  
**Published:** May 2026  
**Research status:** Independent white paper; simulation-based evaluation; not peer reviewed

[Read the RevSoc publication](https://revsoc.ai/research/memshield) · [Open the paper](paper/MemShield_WhitePaper_Final.pdf) · [View the architecture](ARCHITECTURE.md)

</div>

---

## Overview

Stateful autonomous agents store instructions, preferences, retrieved content, and operational context in long-term memory. That persistence creates an attack surface: malicious content can be written into memory during one interaction and influence the agent later, after the original source is no longer visible.

MemShield is a Python middleware framework designed to reduce this risk through three defenses:

1. **Cryptographic provenance** — HMAC/SHA-256 tokens distinguish authenticated instructions from anonymous or untrusted memory writes.
2. **Trust-weighted retrieval** — retrieval priority combines semantic similarity, source trust, historical behavior, and temporal exponential decay.
3. **Semantic contradiction detection** — an isolated Mistral-powered evaluator checks candidate memories against protected directive anchors and quarantines conflicting instructions.

The project focuses on persistent memory poisoning and indirect prompt-injection patterns, including the MemoryGraft and eTAMP attack models described in the paper.

## Simulated Results

The paper reports results from a custom Monte Carlo simulation harness:

| Condition | Simulated attack success |
|---|---:|
| MemoryGraft baseline | 77.0% |
| eTAMP baseline | 59.1% |
| With MemShield enabled | 0.1% |

The simulation also reported a **1.0% false-positive rate**.

These results should be interpreted as evidence from the included simulation design, not as independently validated production benchmarks. They have not yet been generalized across diverse model families, vector databases, RAG configurations, or live enterprise environments.

## Architecture

```text
Untrusted content or memory write
              │
              ▼
┌──────────────────────────────┐
│ 1. Provenance verification   │
│ HMAC/SHA-256 authentication  │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 2. Trust-weighted retrieval  │
│ similarity + trust + decay   │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 3. Semantic conflict check   │
│ contradiction + quarantine   │
└──────────────┬───────────────┘
               ▼
        Approved context
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full mechanical design and [AGENTS.md](AGENTS.md) for the simulated red-team, blue-team, and auditor roles.

## Repository Structure

```text
MemShieldResearch/
├── data/                   # Raw and processed evaluation data
├── figures/                # Generated charts and architecture figures
├── notebooks/              # Exploration and demonstrations
├── paper/                  # White paper in PDF/HTML formats
├── results/                # Evaluation outputs and summaries
├── scripts/                # Supporting utilities
├── src/                    # Middleware, routing, and evaluation code
├── tests/                  # Unit and integration tests
├── AGENTS.md               # Simulated attacker/defender roles
├── ARCHITECTURE.md         # Detailed architecture documentation
└── requirements.txt        # Python dependencies
```

## Reproduce the Evaluation

### Requirements

- Python 3.10+
- `pip`
- A Mistral API key for Layer 3 semantic validation

### Setup

```bash
git clone https://github.com/MysticX662/MemShieldResearch.git
cd MemShieldResearch
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Add your key to `.env`:

```text
MISTRAL_API_KEY=your_api_key_here
```

### Run a verification demonstration

```bash
python src/run_verification.py
```

### Run the full simulation suite

```bash
python src/run_experiments.py
```

Outputs are written to `results/`, with visualizations saved to `figures/`.

## Scope and Limitations

- The reported metrics come from a custom simulation harness.
- The work has not been independently peer reviewed or externally replicated.
- Performance may differ across embedding models, vector stores, agent frameworks, prompts, and deployment environments.
- The semantic-conflict layer depends on an external model and can inherit model-specific errors or availability limits.
- MemShield is an experimental research framework, not a finished production security product.

## Citation

```bibtex
@techreport{earla2026memshield,
  title     = {MemShield: Mitigating Persistent Memory Poisoning in Stateful AI Agents},
  author    = {Nickhil Earla},
  year      = {2026},
  month     = {May},
  institution = {RevSoc Research Division},
  type      = {White Paper},
  url       = {https://revsoc.ai/research/memshield}
}
```

A machine-readable citation is also available in [`CITATION.cff`](CITATION.cff).

## License

This repository is licensed under the [MIT License](LICENSE).
