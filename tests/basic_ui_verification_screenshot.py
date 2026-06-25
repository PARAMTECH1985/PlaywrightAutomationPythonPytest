from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (set headless=False to see it work visually)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to target website
    page.goto("https://example.com")

    # Extract page header text
    heading = page.locator("h1").inner_text()
    print(f"Page heading text is: {heading}")

    # Capture a visual screenshot
    page.screenshot(path="example.png")

    # Close browser session
    browser.close()