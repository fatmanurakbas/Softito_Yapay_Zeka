# LLM 09 — RAG Değerlendirmesi

RAG sistemini yalnızca “iyi yanıt verdi mi?” sorusuyla değerlendirmek yeterli değildir. Bu proje retrieval başarısını ve yanıtın kaynağa sadakatini ayrı ölçer.

## Ölçülen metrikler

- **Recall@k:** Altın kaynak, ilk `k` getirilen parça içinde mi?
- **Context precision:** Getirilen parçaların ne kadarı ilgili?
- **Answer relevance:** Beklenen anahtar kavramlar yanıtta var mı?
- **Citation faithfulness:** Yanıtta belirtilen kaynak kimliği gerçekten retrieval sonucunda mı?

## Çalıştırma

```bash
cd LLM/09-rag-evaluation
python 01-retrieval-evaluation/evaluate_retrieval.py
python 02-answer-evaluation/evaluate_answers.py
python -m unittest discover -s tests -v
```

Bu metrikler otomatik regresyon kontrolüdür. Üretim kararlarında uzman insan değerlendirmesi, zararlı/uydurma yanıt incelemesi ve gerçek kullanıcı sorguları da eklenmelidir.
