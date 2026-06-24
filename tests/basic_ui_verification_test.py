import re
from logger import logger_utils
from playwright.sync_api import Page, expect

from logger.logger_utils import setup_logger

logger = setup_logger(name="basic_ui_verification_test.py", log_file="basic_ui_verification_test.log")


def test_homepage_has_title_and_login(page: Page):
    logger.info(f"Open the browser")
    page.goto("https://playwright.dev/")
    # Expect Page to Have Title
    logger.info(f"Verify page has the title Playwright")
    expect(page).to_have_title(re.compile("Playwright"))
    # Create the Locator to find the link
    logger.info(f"Create the locator to find the link with name Get started")
    get_started = page.get_by_role("link", name="Get started")
    logger.info(f"Link={get_started}")
    logger.info(f"Click on the Link Get started")
    get_started.click()
    # Expects the URL to contain "intro"
    logger.info(f"Verifying that URL has text intro")
    expect(page).to_have_url(re.compile(".*intro"))
