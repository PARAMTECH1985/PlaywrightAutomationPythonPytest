from playwright.async_api import async_playwright, expect
import asyncio
from logger.logger_utils import setup_logger

logger = setup_logger(name="basic_ui_registration_test.py", log_file="basic_ui_registration_test.log")

async def test_user_registration():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        await page.goto("https://example.com")
        await page.locator("#username").fill("testuser_99")
        await page.locator("#email").fill("testuser99@example.com")
        await page.locator("#password").fill("SecurePassword123!")
        await page.locator("#terms-checkbox").click()
        await page.locator("button=[type='Submit']").click()
        # 5. Assert successful registration
        # Expects the URL to change to the dashboard or success page
        await expect(page).to_have_url("https://example.com")
        # Expects a visible success message on the screen
        success_message = page.locator(".welcome-message")
        await expect(success_message).to_be_visible()
        await expect(success_message).to_contain_text("Welcome, testuser_99!")
        await browser.close()

# Run the async function
asyncio.run(test_user_registration())
