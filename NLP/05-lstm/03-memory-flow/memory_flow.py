"""RNN ve LSTM'de uzun vadeli bellek aktarımının sade karşılaştırması."""
from __future__ import annotations


def retained_signal(multiplier: float, steps: int = 25) -> float:
    return multiplier ** steps


if __name__ == "__main__":
    print("25 zaman adımı sonrasında başlangıç bilgisinin teorik korunumu:")
    for name, multiplier in (("RNN (tekrarlayan ağırlık=0.70)", 0.70), ("LSTM (forget gate=0.95)", 0.95), ("LSTM (forget gate=0.99)", 0.99)):
        print(f"{name:32} -> {retained_signal(multiplier):.5f}")
