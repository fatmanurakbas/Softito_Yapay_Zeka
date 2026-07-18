"""Tekrarlayan ağırlık ölçeğinin gradient normuna etkisini gösterir."""
from __future__ import annotations

import numpy as np


def gradient_norms(scale: float, steps: int = 25) -> list[float]:
    """Basitleştirilmiş BPTT'de tekrar eden çarpımların normunu hesaplar."""
    recurrent = np.eye(4) * scale
    gradient = np.ones(4)
    norms = []
    for _ in range(steps):
        gradient = recurrent.T @ gradient
        norms.append(float(np.linalg.norm(gradient)))
    return norms


if __name__ == "__main__":
    for scale in (0.7, 1.0, 1.3):
        norms = gradient_norms(scale)
        print(f"ölçek={scale:.1f} | adım 1={norms[0]:.4f} | adım 10={norms[9]:.4f} | adım 25={norms[-1]:.4f}")
