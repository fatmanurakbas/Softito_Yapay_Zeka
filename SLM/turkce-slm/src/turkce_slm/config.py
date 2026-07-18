"""Uygulama yapılandırmasını okuma ve doğrulama."""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    model: str
    base_url: str = "http://localhost:11434/api"
    temperature: float = 0.2
    num_ctx: int = 4096
    max_output_tokens: int = 256
    keep_alive: str = "5m"

    @classmethod
    def from_file(cls, path: str | Path) -> "AppConfig":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        config = cls(**data)
        if not config.base_url.startswith(("http://", "https://")):
            raise ValueError("base_url http:// veya https:// ile başlamalıdır.")
        if not 0 <= config.temperature <= 2:
            raise ValueError("temperature 0 ile 2 arasında olmalıdır.")
        if config.num_ctx < 128 or config.max_output_tokens < 1:
            raise ValueError("num_ctx ve max_output_tokens geçerli olmalıdır.")
        return config
