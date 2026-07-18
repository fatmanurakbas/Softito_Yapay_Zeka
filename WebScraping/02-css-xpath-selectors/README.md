# 02 — CSS ve XPath Seçicileri

Seçici, HTML içinden hangi verinin alınacağını tarif eder. Aynı hedef için mümkün olduğunca sayfanın anlamına dayalı ve kırılgan olmayan seçiciler kullanın.

## CSS seçicileri

Beautiful Soup'ta `select` ve `select_one` ile kullanılır:

```python
soup.select_one("article.card h2")
soup.select("a[href]")
```

`article.card h2`, `card` sınıfındaki makale içindeki `h2` öğesini seçer. CSS, çoğu standart sayfa için en okunabilir tercihtir.

## XPath

XPath, metin içeriği, hiyerarşi veya konuma dayalı daha karmaşık sorgular için yararlıdır:

```python
tree.xpath("//article[contains(@class, 'card')]//span/text()")
```

Örnek kodu çalıştırmak için `lxml` kurulmalıdır. Tarayıcıya özgü otomatik üretilmiş uzun XPath'ler yerine, mümkün olduğunda sabit sınıf/adlandırmalara dayalı kısa ifadeler yazın.
