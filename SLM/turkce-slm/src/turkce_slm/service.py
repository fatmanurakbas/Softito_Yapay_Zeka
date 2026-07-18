"""Türkçe SLM istemini hazırlayan ve yanıtı yapılandıran servis katmanı."""
from __future__ import annotations

from .config import AppConfig
from .ollama_client import OllamaClient
from .prompts import SYSTEM_PROMPT, build_user_prompt


class TurkishSLMService:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.client = OllamaClient(config.base_url)

    def answer(self, question: str, context: str | None = None) -> dict[str, object]:
        if self.config.model == "your-local-model":
            raise ValueError("configs/app_config.json içindeki model alanını yerel model adınızla değiştirin.")
        messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": build_user_prompt(question, context)}]
        result = self.client.chat(self.config.model, messages, {"temperature": self.config.temperature, "num_ctx": self.config.num_ctx, "num_predict": self.config.max_output_tokens}, self.config.keep_alive)
        return {"answer": result.get("message", {}).get("content", "").strip(), "model": result.get("model", self.config.model), "total_seconds": round(result.get("total_duration", 0) / 1e9, 3), "generated_tokens": result.get("eval_count", 0)}
