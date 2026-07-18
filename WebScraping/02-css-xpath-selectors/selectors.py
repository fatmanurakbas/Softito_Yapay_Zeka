from bs4 import BeautifulSoup
from lxml import html

DOCUMENT = "<main><article class='card'><h2>Python</h2><span class='price'>120</span></article></main>"
soup = BeautifulSoup(DOCUMENT, "html.parser")
tree = html.fromstring(DOCUMENT)
print("CSS:", soup.select_one("article.card h2").get_text(strip=True))
print("XPath:", tree.xpath("//article[contains(@class, 'card')]//span/text()")[0])
