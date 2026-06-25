from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # Using Firefox in headful mode
    page = browser.new_page()
    page.goto("https://wikipedia.org")

    # Locate search field by its placeholder or ID and type
    search_input = page.get_by_role("searchbox") or page.locator("#searchInput")
    search_input.fill("Python (programming language)")

    # Press Enter or click search button
    search_input.press("Enter")

    # Wait explicitly for heading to appear
    page.wait_for_selector("h1")
    print(f"New page URL: {page.url}")

    browser.close()