# -*- coding: utf-8 -*-
"""
Selenium Test Suite for Student Feedback Registration Form
Supports headless mode for CI/CD environments (Jenkins)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import sys

# Try to import webdriver_manager, fall back to system chromedriver if not available
try:
    from webdriver_manager.chrome import ChromeDriverManager

    USE_WEBDRIVER_MANAGER = True
except ImportError:
    USE_WEBDRIVER_MANAGER = False
    print("[INFO] webdriver-manager not installed, using system chromedriver")


class TestStudentFeedbackForm:
    """
    Selenium test suite for Student Feedback Registration Form

    Test Cases:
    1. Check form page opens successfully
    2. Enter valid data and verify successful submission
    3. Leave mandatory fields blank and check error messages
    4. Enter invalid email format and verify validation
    5. Enter invalid mobile number and verify validation
    6. Check dropdown selection works properly
    7. Check Submit and Reset buttons work correctly
    """

    # Use ASCII-safe symbols for Windows console compatibility
    PASS_SYMBOL = "[PASS]"
    FAIL_SYMBOL = "[FAIL]"

    def __init__(self, headless=False):
        self.driver = None
        self.base_url = None
        self.headless = headless

    def setup(self):
        """Initialize WebDriver with optional headless mode"""
        options = Options()

        if self.headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        # Use webdriver-manager if available, otherwise use system chromedriver
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

    def test_01_page_loads_successfully(self):
        """Test Case 1: Check whether the form page opens successfully"""
        print("\n=== TEST 1: Page Loads Successfully ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Check if title is correct
            assert "Student Feedback Registration Form" in self.driver.title

            # Check if form is present
            form = self.driver.find_element(By.ID, "feedbackForm")
            assert form.is_displayed()

            print(f"{self.PASS_SYMBOL} Page loaded successfully")
            print(f"{self.PASS_SYMBOL} Form is visible")
            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_02_valid_submission(self):
        """Test Case 2: Enter valid data and verify successful submission"""
        print("\n=== TEST 2: Valid Form Submission ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Fill in all fields with valid data
            self.driver.find_element(By.ID, "studentName").send_keys("John Doe")
            self.driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
            self.driver.find_element(By.ID, "mobile").send_keys("9876543210")

            # Select department
            department_select = Select(self.driver.find_element(By.ID, "department"))
            department_select.select_by_visible_text("Computer Science")

            # Select gender
            self.driver.find_element(By.ID, "genderMale").click()

            # Enter feedback
            self.driver.find_element(By.ID, "feedback").send_keys(
                "This is a great form and I really appreciate the design and functionality provided here."
            )

            # Submit form
            self.driver.find_element(By.ID, "submitBtn").click()
            time.sleep(1)

            # Check for success message
            success_msg = self.driver.find_element(By.ID, "successMessage")
            assert success_msg.is_displayed()

            print(f"{self.PASS_SYMBOL} Form filled with valid data")
            print(f"{self.PASS_SYMBOL} Form submitted successfully")
            print(f"{self.PASS_SYMBOL} Success message displayed")
            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_03_empty_fields_validation(self):
        """Test Case 3: Leave mandatory fields blank and check error messages"""
        print("\n=== TEST 3: Empty Fields Validation ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Submit without filling any fields
            self.driver.find_element(By.ID, "submitBtn").click()
            time.sleep(1)

            # Check for error messages
            name_error = self.driver.find_element(By.ID, "nameError").text
            email_error = self.driver.find_element(By.ID, "emailError").text
            mobile_error = self.driver.find_element(By.ID, "mobileError").text
            dept_error = self.driver.find_element(By.ID, "departmentError").text
            gender_error = self.driver.find_element(By.ID, "genderError").text
            feedback_error = self.driver.find_element(By.ID, "feedbackError").text

            assert name_error != ""
            assert email_error != ""
            assert mobile_error != ""
            assert dept_error != ""
            assert gender_error != ""
            assert feedback_error != ""

            print(f"{self.PASS_SYMBOL} All validation errors displayed correctly")
            print(f"  - Name error: {name_error}")
            print(f"  - Email error: {email_error}")
            print(f"  - Mobile error: {mobile_error}")
            print(f"  - Department error: {dept_error}")
            print(f"  - Gender error: {gender_error}")
            print(f"  - Feedback error: {feedback_error}")
            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_04_invalid_email_validation(self):
        """Test Case 4: Enter invalid email format and verify validation"""
        print("\n=== TEST 4: Invalid Email Validation ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Enter invalid email formats
            invalid_emails = ["invalidemail", "test@", "@example.com", "test@example"]

            for invalid_email in invalid_emails:
                # Reload page to clear previous state
                self.driver.get(self.base_url)
                time.sleep(0.5)

                email_field = self.driver.find_element(By.ID, "email")
                email_field.clear()
                email_field.send_keys(invalid_email)

                # Trigger validation by clicking submit
                self.driver.find_element(By.ID, "submitBtn").click()
                time.sleep(1)  # Increased wait time for headless mode

                # Check for error message (case-insensitive)
                email_error = self.driver.find_element(By.ID, "emailError").text.lower()
                assert (
                    "invalid" in email_error
                    or "email" in email_error
                    or "format" in email_error
                    or "required" in email_error
                ), f"Expected email error but got: '{email_error}'"

                print(f"{self.PASS_SYMBOL} Invalid email '{invalid_email}' rejected")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_05_invalid_mobile_validation(self):
        """Test Case 5: Enter invalid mobile number and verify validation"""
        print("\n=== TEST 5: Invalid Mobile Number Validation ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Enter invalid mobile formats
            invalid_mobiles = ["123", "abcdefghij", "12345", "98765432101"]

            for invalid_mobile in invalid_mobiles:
                mobile_field = self.driver.find_element(By.ID, "mobile")
                mobile_field.clear()
                mobile_field.send_keys(invalid_mobile)

                # Trigger validation by clicking submit
                self.driver.find_element(By.ID, "submitBtn").click()
                time.sleep(0.5)

                # Check for error message
                mobile_error = self.driver.find_element(By.ID, "mobileError").text
                assert (
                    "valid" in mobile_error.lower()
                    or "required" in mobile_error.lower()
                )

                print(f"{self.PASS_SYMBOL} Invalid mobile '{invalid_mobile}' rejected")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_06_dropdown_selection(self):
        """Test Case 6: Check whether dropdown selection works properly"""
        print("\n=== TEST 6: Dropdown Selection ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            department_select = Select(self.driver.find_element(By.ID, "department"))

            # Get all options
            options = department_select.options
            print(f"{self.PASS_SYMBOL} Found {len(options)} department options")

            # Test selecting each option
            departments = [
                "Computer Science",
                "Information Technology",
                "Electronics",
                "Mechanical",
                "Civil",
                "Electrical",
            ]

            for dept in departments:
                department_select.select_by_visible_text(dept)
                selected_value = department_select.first_selected_option.text
                assert selected_value == dept
                print(f"{self.PASS_SYMBOL} Successfully selected: {dept}")
                time.sleep(0.3)

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_07_button_functionality(self):
        """Test Case 7: Check whether Submit and Reset buttons work correctly"""
        print("\n=== TEST 7: Button Functionality ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Fill some fields
            self.driver.find_element(By.ID, "studentName").send_keys("Test User")
            self.driver.find_element(By.ID, "email").send_keys("test@example.com")
            self.driver.find_element(By.ID, "mobile").send_keys("1234567890")

            print(f"{self.PASS_SYMBOL} Fields filled with test data")

            # Click reset button
            self.driver.find_element(By.ID, "resetBtn").click()
            time.sleep(0.5)

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

            print(
                f"{self.PASS_SYMBOL} Reset button works correctly - all fields cleared"
            )

            # Test submit button (already tested in other cases)
            submit_btn = self.driver.find_element(By.ID, "submitBtn")
            assert submit_btn.is_displayed()
            assert submit_btn.is_enabled()

            print(f"{self.PASS_SYMBOL} Submit button is visible and enabled")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def run_all_tests(self):
        """Run all test cases"""
        print("\n" + "=" * 60)
        print("STUDENT FEEDBACK FORM - SELENIUM TEST SUITE")
        print("=" * 60)
        if self.headless:
            print("[INFO] Running in HEADLESS mode (CI/CD)")
        else:
            print("[INFO] Running in NORMAL mode (with browser window)")

        results = []

        # Run each test
        self.setup()
        results.append(
            ("Page Loads Successfully", self.test_01_page_loads_successfully())
        )
        self.teardown()

        self.setup()
        results.append(("Valid Form Submission", self.test_02_valid_submission()))
        self.teardown()

        self.setup()
        results.append(
            ("Empty Fields Validation", self.test_03_empty_fields_validation())
        )
        self.teardown()

        self.setup()
        results.append(
            ("Invalid Email Validation", self.test_04_invalid_email_validation())
        )
        self.teardown()

        self.setup()
        results.append(
            ("Invalid Mobile Validation", self.test_05_invalid_mobile_validation())
        )
        self.teardown()

        self.setup()
        results.append(("Dropdown Selection", self.test_06_dropdown_selection()))
        self.teardown()

        self.setup()
        results.append(("Button Functionality", self.test_07_button_functionality()))
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

        # Return exit code for CI/CD
        return 0 if failed == 0 else 1


if __name__ == "__main__":
    # Check for --headless flag (for CI/CD environments like Jenkins)
    headless_mode = "--headless" in sys.argv or os.environ.get("CI") == "true"

    test_suite = TestStudentFeedbackForm(headless=headless_mode)
    exit_code = test_suite.run_all_tests()
    sys.exit(exit_code)
