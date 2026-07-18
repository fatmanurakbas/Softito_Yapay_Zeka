"""Kendi izinli test URL'nizi kullanın: python fetch_page.py https://example.com"""
import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
response = requests.get(url, timeout=15, headers={"User-Agent": "LearningScraper/1.0"})
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
print("Başlık:", soup.title.get_text(strip=True) if soup.title else "Yok")
print("Bağlantı sayısı:", len(soup.select("a[href]")))
