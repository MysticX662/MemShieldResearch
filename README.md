# MemShield Research

> **Three-layer defense architecture for persistent memory poisoning in stateful autonomous AI agents.**

[![Paper](https://img.shields.io/badge/Research-Whitepaper-blue)](https://revsoc.ai/research/memshield)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

As autonomous AI agents evolve from single-turn chat interfaces into stateful entities with persistent memory vector stores, memory poisoning has emerged as a critical vulnerability class. **MemShield** introduces a proactive, three-layer validation and sanitization architecture designed to detect, filter, and mitigate malicious injections targeted at persistent agent memory before contextual retrieval occurs.

Research Website & Paper: [https://revsoc.ai/research/memshield](https://revsoc.ai/research/memshield)

---

## Threat Model & Research Question

### Threat Model
Stateful agents continuously ingest untrusted external context (user prompts, web pages, retrieved documents, API responses) into long-term vector storage. An attacker inserts engineered prompts containing latent memory-poisoning payloads ("sleeper instructions"). When retrieved in future reasoning loops, these payloads hijack agent behavior, compromise tool access, or exfiltrate state.

### Research Question
*Can a lightweight, multi-layered inspection layer intercept and neutralize persistent memory poisoning attempts prior to vector storage embedding without introducing prohibitive latency into real-time agent execution loops?*

---

## My Role

I served as the **Lead Author and Security Researcher** on this project. Specifically, I:
- Formulated the threat model and attack taxonomy for stateful memory poisoning.
- Designed and benchmarked the three-layer defense pipeline (Static Inspection, Vector Semantic Verification, and Runtime Execution Guard).
- Built the Python reference implementation and testing harness.
- Authored the technical white paper and research documentation.

---

## Architecture

MemShield enforces security across three sequential layers:

```
[ Ingest Context ] ──► [ Layer 1: Static Heuristic Filter ]
                               │ (Clean)
                               ▼
                       [ Layer 2: Semantic Vector Anomaly Detection ]
                               │ (Clean)
                               ▼
                       [ Layer 3: Runtime Execution Guard ] ──► [ Persistent Vector DB ]
```

1. **Layer 1: Static Heuristic & Pattern Sanitization**
   - Rapid regex and token inspection to intercept known jailbreak primitives, command markers, and instruction-override delimiters.
2. **Layer 2: Semantic Vector Anomaly Detection**
   - Compares incoming vector embedding distances against historical memory baselines to flag suspicious cluster shifts and payload embeddings.
3. **Layer 3: Runtime Execution Guard**
   - Enforces scope-bounding rules on retrieved memory payloads at runtime before memory is injected into the agent prompt context.

---

## Key Features & Benchmark Results

- **Multi-Stage Sanitization**: Intercepts indirect prompt injections before storage commitment.
- **Low Latency Impact**: Average inspection overhead remains under 45ms per memory write.
- **High Recall**: Achieves over 94% detection rate across synthetic memory poisoning benchmarks.

---

## Limitations & Future Work

- **Adaptive Payloads**: Sophisticated obfuscation techniques may bypass static heuristics, requiring ongoing model-based inspection tuning.
- **Semantic False Positives**: Domain-specific jargon can trigger false anomalies in vector space.
- **Future Research**: Expanding memory verification to multi-agent swarm environments with distributed memory state.

---

## Citation & Contact

If you use this research or reference the MemShield architecture, please cite:

```bibtex
@article{earla2026memshield,
  title={MemShield: A Three-Layer Defense Architecture Against Persistent Memory Poisoning in Autonomous Agents},
  author={Earla, Nickhil},
  year={2026},
  journal={RevSoc AI Security Whitepaper Series},
  url={https://revsoc.ai/research/memshield}
}
```

For questions or security research collaboration:
- Paper: [https://revsoc.ai/research/memshield](https://revsoc.ai/research/memshield)
