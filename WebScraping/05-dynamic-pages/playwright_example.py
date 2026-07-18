from playwright.sync_api import sync_playwright

def get_title(url: str) -> str:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")
        title = page.title()
        browser.close()
        return title

if __name__ == "__main__":
    print("İzinli URL için get_title(url) fonksiyonunu çağırın.")
