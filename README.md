# MemShield

**Defense Architecture against Persistent Memory Poisoning in Stateful Autonomous AI Agents**

MemShield is a Python-based middleware designed to protect long-term memory (LTM) subsystems of autonomous AI agents from memory and context poisoning (OWASP ASI06).

## Overview
Autonomous agents are vulnerable to indirect prompt injections (e.g., eTAMP, MemoryGraft, MINJA, InjecMEM) that lie dormant in vector databases until retrieved in future sessions. MemShield mitigates these threats through a three-layer verification pipeline:
1. **Provenance Check**: Validates cryptographic tokens to reject anonymous writes.
2. **Trust-Weighted Retrieval**: Modifies retrieval distance based on similarity, trust scores, and temporal decay.
3. **Semantic Conflict Layer**: Uses a Mistral-powered LLM consistency judge (with automated capacity fallback routing) to flag logical contradictions.

## Project Setup

### Prerequisites
* Python 3.10+
* `pip`
* A Mistral API Key (for Layer 3 Validation runs)

### Installation
1. Clone the repository.
2. Setup a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure `.env`:
   Ensure `MISTRAL_API_KEY` is present in your local `.env`. The system uses an automated LLM router that switches models if usage limits (429) are reached during testing.

### Running the R&D Pipeline
To execute the baseline poisoning simulation and MemShield defense pipeline:
```bash
python run_verification.py
```
To run the automated research evaluations for the paper:
```bash
python run_experiments.py
```

## Documentation
- See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architectural mechanics.
- See [AGENTS.md](AGENTS.md) for interacting with our simulated Red/Blue team AI coders.
