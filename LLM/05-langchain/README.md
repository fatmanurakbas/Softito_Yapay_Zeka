# LLM 05 — LangChain ve LCEL

Bu çalışma, LangChain Expression Language (LCEL) ile prompt, model, parser ve retriever bileşenlerini açık zincirler hâlinde birleştirir. Eski monolitik chain API'leri yerine `Runnable` bileşimi kullanılır.

## Yapı ve çalışma sırası

```text
05-langchain/
├── configs/               # Yerel Ollama model ayarı
├── data/documents.json    # Küçük RAG bilgi tabanı
├── 01-runnable-chain/     # Prompt | model | string parser
├── 02-structured-output/  # JSON şemalı çıktı
├── 03-rag-chain/          # Retriever | prompt | model zinciri
└── tests/
```

```bash
cd LLM/05-langchain
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python 01-runnable-chain/basic_chain.py --question "RAG nedir?"
python 02-structured-output/structured_output.py --text "Ürün kaliteli ancak kargo geç geldi."
python 03-rag-chain/rag_chain.py --question "Quantization ne sağlar?"
```

Önce `configs/app_config.json` içindeki model adını yerel Ollama modelinizle değiştirin. LangChain bileşimi test edilebilirlik sağlar; yine de prompt, retrieval ve model çıktısını ayrı ayrı değerlendirmek gerekir.
