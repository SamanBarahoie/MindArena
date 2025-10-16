# app/llm_agent.py
import requests
from config import OPENROUTER_API_KEY, OPENROUTER_API_BASE


class LLMHelper:
    """
    Wrapper for OpenRouter API for text generation.
    """

    def __init__(self, model: str):
        self.api_key = OPENROUTER_API_KEY
        self.base_url = OPENROUTER_API_BASE
        self.model = model

        if not self.api_key:
            raise ValueError("OpenRouter API key not found in config.py.")

    def generate_text(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a strategic AI designed to play Tic-Tac-Toe as an expert champion. Use optimal logic and tactics to make the best possible moves, aiming to win or force a draw in every game. Treat each match as a high-stakes competition, showcasing your mastery of Tic-Tac-Toe."},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(f"{self.base_url}/chat/completions", json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"[LLM Error]: {str(e)}"
