"""JSON tabanlı prompt şablonlarını yükler ve güvenli biçimde işler."""
from __future__ import annotations

import json
from pathlib import Path


class PromptTemplateStore:
    def __init__(self, path: str | Path) -> None:
        self.templates = json.loads(Path(path).read_text(encoding="utf-8"))

    def render(self, task: str, **variables: str) -> list[dict[str, str]]:
        if task not in self.templates:
            raise ValueError(f"Bilinmeyen görev: {task}. Seçenekler: {', '.join(self.templates)}")
        template = self.templates[task]
        try:
            return [{"role": "system", "content": template["system"]}, {"role": "user", "content": template["user"].format(**variables)}]
        except KeyError as error:
            raise ValueError(f"Eksik şablon değişkeni: {error.args[0]}") from error
