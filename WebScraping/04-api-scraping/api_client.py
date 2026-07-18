import requests

def fetch_json(url: str) -> dict | list:
    response = requests.get(url, timeout=15, headers={"Accept": "application/json"})
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("Kullanım: fetch_json('https://izinli-api.example/items')")
