import csv

def clean(rows: list[dict]) -> list[dict]:
    return [
        {"title": str(row.get("title", "")).strip(), "price": float(row["price"])}
        for row in rows
        if str(row.get("title", "")).strip() and row.get("price") is not None
    ]

def save_csv(rows: list[dict], path: str = "products.csv") -> None:
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price"])
        writer.writeheader(); writer.writerows(rows)
