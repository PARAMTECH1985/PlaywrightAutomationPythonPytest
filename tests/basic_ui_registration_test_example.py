from playwright.sync_api import sync_playwright


def test_registration():
    with sync_playwright() as p:
        # Launch the browser (headless=False lets you see the action)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            # 1. Navigate to the registration/login page
            print("Navigating to the website...")
            page.goto("https://practicetestautomation.com")

            # 2. Fill out the form fields using modern locators
            print("Filling out the registration form...")
            page.get_by_label("Username").fill("student")
            page.get_by_label("Password").fill("Password123")

            # 3. Click the submit button
            print("Submitting the form...")
            page.get_by_role("button", name="Submit").click()

            # 4. Wait for the success URL or a success element
            print("Waiting for navigation...")
            page.wait_for_url("**/logged-in-successfully/")

            # 5. Assert / Verify the success message is visible
            success_message = page.locator("h1.post-title")

            if success_message.is_visible() and "Logged In Successfully" in success_message.text_content():
                print("Registration/Login Test Passed successfully!")
            else:
                print("Test Failed: Success message not found.")

        except Exception as e:
            print(f"An error occurred during the test: {e}")

        finally:
            # Always close the browser to clean up resources
            context.close()
            browser.close()


test_registration()
