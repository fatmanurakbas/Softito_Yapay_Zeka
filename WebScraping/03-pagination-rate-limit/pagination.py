import time
import requests

def collect_pages(base_url: str, page_count: int, delay_seconds: float = 1.0):
    rows = []
    for page in range(1, page_count + 1):
        response = requests.get(base_url, params={"page": page}, timeout=15)
        response.raise_for_status()
        rows.append(response.text)
        if page < page_count:
            time.sleep(delay_seconds)
    return rows

if __name__ == "__main__":
    print("Örnek: collect_pages('https://izinli-site.example/list', 3)")
