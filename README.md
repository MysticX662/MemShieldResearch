<div align="center">

# MemShield: Mitigating Persistent Memory Poisoning in Stateful AI Agents

[![Paper](https://img.shields.io/badge/Paper-PDF-red)](paper/MemShield_WhitePaper_Final.pdf)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Defense Architecture against Persistent Memory Poisoning in Stateful Autonomous AI Agents**

</div>

## 📖 Overview

Autonomous agents rely heavily on Vector Databases to store long-term memory (LTM). This makes them vulnerable to **indirect prompt injections** (e.g., eTAMP, MemoryGraft, MINJA, InjecMEM) that can lie dormant in the memory store until retrieved in future sessions. 

**MemShield** is a Python-based middleware architecture designed to protect these subsystems from memory and context poisoning (OWASP ASI06). It mitigates threats through a robust, three-layer verification pipeline:

1. **Provenance Check**: Validates cryptographic tokens (HMAC/SHA256) to reject unauthorized or anonymous writes to memory.
2. **Trust-Weighted Retrieval**: Modifies retrieval distance based on semantic similarity, historical trust scores, and temporal exponential decay.
3. **Semantic Conflict Layer**: Utilizes a Mistral-powered LLM consistency judge (with automated capacity fallback routing) to flag logical contradictions during generation.

---

## 🗂️ Repository Structure

```text
MemShield/
├── data/                   # Datasets (raw & processed) for empirical evaluations
├── figures/                # Output directory for generated charts and architectures
├── notebooks/              # Jupyter notebooks for data exploration and demonstrations
├── paper/                  # Final white paper deliverables (PDF/HTML)
├── results/                # Evaluation outputs, metrics, and empirical summaries
├── scripts/                # Standalone helper scripts (e.g., charting)
├── src/                    # Core MemShield middleware and LLM routing logic
├── tests/                  # Unit and integration test suite
├── .env.example            # Environment variables template
├── AGENTS.md               # Details on Red/Blue team simulated AI coders
├── ARCHITECTURE.md         # Deep-dive into MemShield's verification layers
└── requirements.txt        # Python dependency manifest
```

---

## 🚀 Installation & Setup

### Prerequisites
* **Python 3.10+**
* `pip`
* A **Mistral API Key** (required for Layer 3 Semantic Validation runs)

### Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/MysticX662/MemShieldResearch.git
   cd MemShieldResearch
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Create a `.env` file in the root directory and add your Mistral API Key. 
   ```bash
   echo "MISTRAL_API_KEY=your_api_key_here" > .env
   ```
   > **Note**: The system uses an automated LLM router (`src/llm_router.py`) that intelligently switches models if usage limits (HTTP 429) are reached during stress testing.

---

## 🧪 Usage & Reproducibility

### Baseline Poisoning Simulation
To execute the baseline poisoning simulation against the MemShield defense pipeline:
```bash
python src/run_verification.py
```
*This script will simulate a Red-Team injection attack and demonstrate how the Blue-Team MemShield layers quarantine anomalous memory entries.*

### Full Empirical Evaluation
To run the automated research evaluations that generate the metrics cited in the paper:
```bash
python src/run_experiments.py
```
Results will be output to the `results/` directory, and visualizations will be saved to `figures/`.

---

## 📊 Results

The empirical evaluation of MemShield demonstrates significant improvements in maintaining agent integrity under adversarial conditions. For detailed charts, such as the trust decay curves and performance baselines, see the `figures/` directory or refer to the full [White Paper](paper/MemShield_WhitePaper_Final.pdf).

---

## 📚 Documentation

For an in-depth understanding of the system, please refer to our extended documentation:
- 🧠 **[ARCHITECTURE.md](ARCHITECTURE.md)**: Detailed mechanical breakdown of the defense layers and Mnemonic Sovereignty.
- 🤖 **[AGENTS.md](AGENTS.md)**: Instructions and profiles for our specialized Red-Team, Blue-Team, and Auditor agents.

---

## 📝 Citation

If you use MemShield or find our research helpful in your work, please cite our paper:

```bibtex
@article{memshield2026,
  title={MemShield: Mitigating Persistent Memory Poisoning in Stateful AI Agents},
  author={MysticX662 et al.},
  year={2026},
  publisher={GitHub},
  url={https://github.com/MysticX662/MemShieldResearch}
}
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
