# MemShield Development Guidelines

Welcome to the MemShield repository. This project focuses on defending stateful autonomous AI agents against **Persistent Memory Poisoning** (e.g., MemoryGraft, eTAMP, InjecMEM, MINJA). 

## Architecture 
The MemShield middleware operates via three core layers:
1. **Provenance Check**: Validates cryptographic tokens to reject anonymous writes.
2. **Trust-Weighted Retrieval**: Modifies retrieval distance based on source similarity, trust scores, and temporal decay functions. 
3. **Semantic Conflict Layer**: Uses an LLM consistency judge to flag logical flaws and contradictions between incoming memory and verified history.

## Development Constraints & Standards
* **Python**: Core engine is built in Python. Use robust typing (`typing` module - `List, Dict, Any, Optional`).
* **Security & Auth**: Use `uuid`, `hmac`, `hashlib` for state tracking and mnemonic token generation.
* **Testing**: Red Team components (`AdversarialAttackEngine`) simulate attacks (e.g., executing eTAMP payload simulating web scrape injections). Blue Team pieces (`MemShieldCore`) validate. Always write corresponding red-team/blue-team pairs when adding new vulnerabilities.

## References
* **ASI06**: Memory & Context Poisoning 
* Treat LTM (Long-Term Memory) stores as an unmonitored write-surface threat unless validated by MemShield.
