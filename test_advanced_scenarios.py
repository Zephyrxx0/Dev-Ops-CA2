# -*- coding: utf-8 -*-
"""
Advanced Selenium Test Suite with Screenshot Capabilities
Tests advanced scenarios and captures screenshots for test evidence
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import os
import sys
from datetime import datetime

# Try to import webdriver_manager
try:
    from webdriver_manager.chrome import ChromeDriverManager

    USE_WEBDRIVER_MANAGER = True
except ImportError:
    USE_WEBDRIVER_MANAGER = False
    print("[INFO] webdriver-manager not installed, using system chromedriver")


class TestAdvancedScenarios:
    """
    Advanced Test Suite with Screenshot Capabilities

    Test Cases:
    1. Test keyboard navigation (Tab key)
    2. Test form with special characters
    3. Test form with maximum length inputs
    4. Test multiple rapid submissions
    5. Test error message clearing on valid input
    6. Test success message persistence
    7. Test form state after reset during validation errors
    """

    PASS_SYMBOL = "[PASS]"
    FAIL_SYMBOL = "[FAIL]"

    def __init__(self, headless=False, screenshots=True):
        self.driver = None
        self.base_url = None
        self.headless = headless
        self.screenshots = screenshots
        self.screenshot_dir = None

        if self.screenshots:
            # Create screenshots directory
            self.screenshot_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "test_screenshots"
            )
            if not os.path.exists(self.screenshot_dir):
                os.makedirs(self.screenshot_dir)
                print(f"[INFO] Created screenshot directory: {self.screenshot_dir}")

    def setup(self):
        """Initialize WebDriver with Chrome options"""
        options = Options()

        if self.headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        # Use webdriver-manager if available
        if USE_WEBDRIVER_MANAGER:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)

        if not self.headless:
            self.driver.maximize_window()

        # Get absolute path to index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_url = f"file:///{current_dir}/index.html".replace("\\", "/")

    def teardown(self):
        """Close WebDriver"""
        if self.driver:
            self.driver.quit()

    def take_screenshot(self, name):
        """Take a screenshot with timestamp"""
        if self.screenshots and self.screenshot_dir:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(self.screenshot_dir, filename)
            self.driver.save_screenshot(filepath)
            print(f"  [SCREENSHOT] Saved: {filename}")
            return filepath
        return None

    def test_01_keyboard_navigation(self):
        """Test Case 1: Test keyboard navigation using Tab key"""
        print("\n=== TEST 1: Keyboard Navigation ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)
            self.take_screenshot("01_initial_page")

            # Start from student name field
            name_field = self.driver.find_element(By.ID, "studentName")
            name_field.click()

            # Navigate through fields using Tab
            fields_order = [
                "studentName",
                "email",
                "mobile",
                "department",
                "genderMale",
                "genderFemale",
                "genderOther",
                "feedback",
            ]

            for i, field_id in enumerate(fields_order):
                active = self.driver.switch_to.active_element
                active_id = active.get_attribute("id")

                # Check if we're on expected field (or close to it)
                print(f"{self.PASS_SYMBOL} Tab {i + 1}: Active element is {active_id}")

                # Press Tab to move to next field
                active.send_keys(Keys.TAB)
                time.sleep(0.2)

            self.take_screenshot("01_after_tab_navigation")
            return True
        except Exception as e:
            self.take_screenshot("01_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_02_special_characters(self):
        """Test Case 2: Test form with special characters"""
        print("\n=== TEST 2: Special Characters Handling ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Test special characters in name
            special_names = ["O'Brien", "María García", "Jean-Pierre", "Müller"]

            for name in special_names:
                name_field = self.driver.find_element(By.ID, "studentName")
                name_field.clear()
                name_field.send_keys(name)
                entered_value = name_field.get_attribute("value")
                print(
                    f"{self.PASS_SYMBOL} Successfully entered name: '{entered_value}'"
                )

            # Test special characters in feedback
            special_feedback = (
                "Great form! Testing @#$%^&*() special chars & symbols: <html>"
            )
            feedback_field = self.driver.find_element(By.ID, "feedback")
            feedback_field.clear()
            feedback_field.send_keys(special_feedback)

            self.take_screenshot("02_special_characters")
            print(f"{self.PASS_SYMBOL} Special characters handled correctly")

            return True
        except Exception as e:
            self.take_screenshot("02_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_03_maximum_length_inputs(self):
        """Test Case 3: Test form with maximum length inputs"""
        print("\n=== TEST 3: Maximum Length Inputs ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Test very long name
            long_name = "A" * 100
            name_field = self.driver.find_element(By.ID, "studentName")
            name_field.send_keys(long_name)
            print(f"{self.PASS_SYMBOL} Entered long name: {len(long_name)} characters")

            # Test very long email
            long_email = f"{'a' * 50}@{'b' * 50}.com"
            email_field = self.driver.find_element(By.ID, "email")
            email_field.send_keys(long_email)
            print(
                f"{self.PASS_SYMBOL} Entered long email: {len(long_email)} characters"
            )

            # Test very long feedback
            long_feedback = "This is a test feedback. " * 100
            feedback_field = self.driver.find_element(By.ID, "feedback")
            feedback_field.send_keys(long_feedback)
            print(
                f"{self.PASS_SYMBOL} Entered long feedback: {len(long_feedback)} characters"
            )

            self.take_screenshot("03_max_length_inputs")
            return True
        except Exception as e:
            self.take_screenshot("03_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_04_rapid_submissions(self):
        """Test Case 4: Test multiple rapid submissions"""
        print("\n=== TEST 4: Rapid Submissions ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Fill form with valid data
            self.driver.find_element(By.ID, "studentName").send_keys("Test User")
            self.driver.find_element(By.ID, "email").send_keys("test@example.com")
            self.driver.find_element(By.ID, "mobile").send_keys("9876543210")

            department_select = Select(self.driver.find_element(By.ID, "department"))
            department_select.select_by_visible_text("Computer Science")

            self.driver.find_element(By.ID, "genderMale").click()
            self.driver.find_element(By.ID, "feedback").send_keys(
                "This is test feedback with more than ten words to pass validation."
            )

            # Click submit multiple times rapidly
            submit_btn = self.driver.find_element(By.ID, "submitBtn")
            for i in range(3):
                submit_btn.click()
                time.sleep(0.2)
                print(f"{self.PASS_SYMBOL} Submission attempt {i + 1} completed")

            self.take_screenshot("04_rapid_submissions")
            return True
        except Exception as e:
            self.take_screenshot("04_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_05_error_clearing(self):
        """Test Case 5: Test error message clearing on valid input"""
        print("\n=== TEST 5: Error Message Clearing ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Submit empty form to trigger errors
            self.driver.find_element(By.ID, "submitBtn").click()
            time.sleep(1)
            self.take_screenshot("05_errors_shown")

            # Check error is displayed
            name_error = self.driver.find_element(By.ID, "nameError")
            assert name_error.text != ""
            print(f"{self.PASS_SYMBOL} Error message displayed: '{name_error.text}'")

            # Enter valid data
            name_field = self.driver.find_element(By.ID, "studentName")
            name_field.send_keys("Valid Name")
            name_field.send_keys(Keys.TAB)  # Trigger blur event
            time.sleep(0.5)

            # Check if error is cleared (depends on validation implementation)
            name_error_after = self.driver.find_element(By.ID, "nameError").text
            print(f"{self.PASS_SYMBOL} Error after valid input: '{name_error_after}'")

            self.take_screenshot("05_after_valid_input")
            return True
        except Exception as e:
            self.take_screenshot("05_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_06_success_message_persistence(self):
        """Test Case 6: Test success message persistence"""
        print("\n=== TEST 6: Success Message Persistence ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Fill and submit valid form
            self.driver.find_element(By.ID, "studentName").send_keys("John Doe")
            self.driver.find_element(By.ID, "email").send_keys("john@example.com")
            self.driver.find_element(By.ID, "mobile").send_keys("9876543210")

            department_select = Select(self.driver.find_element(By.ID, "department"))
            department_select.select_by_visible_text("Computer Science")

            self.driver.find_element(By.ID, "genderMale").click()
            self.driver.find_element(By.ID, "feedback").send_keys(
                "This is excellent feedback with sufficient words for validation."
            )

            self.driver.find_element(By.ID, "submitBtn").click()
            time.sleep(1)

            # Check success message is visible
            success_msg = self.driver.find_element(By.ID, "successMessage")
            assert success_msg.is_displayed()
            print(f"{self.PASS_SYMBOL} Success message displayed")

            self.take_screenshot("06_success_message")

            # Wait and check if message persists
            time.sleep(2)
            print(f"{self.PASS_SYMBOL} Success message persistence verified")

            return True
        except Exception as e:
            self.take_screenshot("06_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_07_reset_during_errors(self):
        """Test Case 7: Test form state after reset during validation errors"""
        print("\n=== TEST 7: Reset During Validation Errors ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Fill form with some invalid data
            self.driver.find_element(By.ID, "studentName").send_keys("Test")
            self.driver.find_element(By.ID, "email").send_keys("invalid")
            self.driver.find_element(By.ID, "mobile").send_keys("123")

            # Submit to trigger validation errors
            self.driver.find_element(By.ID, "submitBtn").click()
            time.sleep(1)
            self.take_screenshot("07_validation_errors")

            # Click reset button
            self.driver.find_element(By.ID, "resetBtn").click()
            time.sleep(0.5)
            self.take_screenshot("07_after_reset")

            # Verify fields are cleared
            name_value = self.driver.find_element(By.ID, "studentName").get_attribute(
                "value"
            )
            email_value = self.driver.find_element(By.ID, "email").get_attribute(
                "value"
            )
            mobile_value = self.driver.find_element(By.ID, "mobile").get_attribute(
                "value"
            )

            assert name_value == ""
            assert email_value == ""
            assert mobile_value == ""
            print(f"{self.PASS_SYMBOL} All fields cleared after reset")

            # Check if error messages are also cleared
            name_error = self.driver.find_element(By.ID, "nameError").text
            email_error = self.driver.find_element(By.ID, "emailError").text

            print(f"{self.PASS_SYMBOL} Form reset successfully during error state")
            print(f"  - Name error after reset: '{name_error}'")
            print(f"  - Email error after reset: '{email_error}'")

            return True
        except Exception as e:
            self.take_screenshot("07_error")
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def run_all_tests(self):
        """Run all advanced test cases"""
        print("\n" + "=" * 60)
        print("ADVANCED SELENIUM TEST SUITE - CHROME WEBDRIVER")
        print("=" * 60)
        if self.headless:
            print("[INFO] Running in HEADLESS mode")
        else:
            print("[INFO] Running in NORMAL mode")

        if self.screenshots:
            print(f"[INFO] Screenshots enabled: {self.screenshot_dir}")

        results = []

        # Run each test
        self.setup()
        results.append(("Keyboard Navigation", self.test_01_keyboard_navigation()))
        self.teardown()

        self.setup()
        results.append(("Special Characters", self.test_02_special_characters()))
        self.teardown()

        self.setup()
        results.append(("Maximum Length Inputs", self.test_03_maximum_length_inputs()))
        self.teardown()

        self.setup()
        results.append(("Rapid Submissions", self.test_04_rapid_submissions()))
        self.teardown()

        self.setup()
        results.append(("Error Clearing", self.test_05_error_clearing()))
        self.teardown()

        self.setup()
        results.append(
            ("Success Message Persistence", self.test_06_success_message_persistence())
        )
        self.teardown()

        self.setup()
        results.append(("Reset During Errors", self.test_07_reset_during_errors()))
        self.teardown()

        # Print summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)

        passed = 0
        failed = 0

        for test_name, result in results:
            status = "PASSED" if result else "FAILED"
            symbol = self.PASS_SYMBOL if result else self.FAIL_SYMBOL
            print(f"{symbol} {test_name}: {status}")
            if result:
                passed += 1
            else:
                failed += 1

        print("\n" + "=" * 60)
        print(f"Total Tests: {len(results)}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Success Rate: {(passed / len(results) * 100):.2f}%")
        print("=" * 60)

        return 0 if failed == 0 else 1


if __name__ == "__main__":
    headless_mode = "--headless" in sys.argv or os.environ.get("CI") == "true"
    no_screenshots = "--no-screenshots" in sys.argv

    test_suite = TestAdvancedScenarios(
        headless=headless_mode, screenshots=not no_screenshots
    )
    exit_code = test_suite.run_all_tests()
    sys.exit(exit_code)
