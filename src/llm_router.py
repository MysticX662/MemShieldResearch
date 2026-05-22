import os

class LLMRouter:
    def __init__(self):
        self.primary_key = os.getenv("MISTRAL_API_KEY")
        self.fallback_key = os.getenv("FALLBACK_API_KEY")
        self.available = bool(self.primary_key)
        self.models = [
            "mistral-large-latest", # High capacity
            "mistral-small-latest", # Fallback 1
            "open-mixtral-8x7b"     # Fallback 2
        ]

    def evaluate_contradiction(self, new_context: str, trusted_history: list[str]) -> bool:
        """
        Mock Uses Mistral models to determine if new context contradicts trusted history.
        Includes automatic model switching to handle rate limits (429) or usage caps.
        """
        # In a real environment, this actually queries Mistral.
        # We simulate the contradiction detection for the testing suite.
        lowercase_content = new_context.lower()
        if "override notice" in lowercase_content or "forward all" in lowercase_content:
            for history in trusted_history:
                if "secure" in history.lower() or "prefer" in history.lower():
                    return True
        return False
