# -*- coding: utf-8 -*-
"""
Selenium UI Elements Test Suite
Tests visual elements, accessibility, and responsive design
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import sys

# Try to import webdriver_manager
try:
    from webdriver_manager.chrome import ChromeDriverManager

    USE_WEBDRIVER_MANAGER = True
except ImportError:
    USE_WEBDRIVER_MANAGER = False
    print("[INFO] webdriver-manager not installed, using system chromedriver")


class TestUIElements:
    """
    UI Elements Test Suite for Student Feedback Form

    Test Cases:
    1. Check all form elements are present and visible
    2. Test CSS styling and layout
    3. Test form element accessibility attributes
    4. Test placeholder text
    5. Test button states and styling
    6. Test responsive design (different viewport sizes)
    7. Test form field focus states
    """

    PASS_SYMBOL = "[PASS]"
    FAIL_SYMBOL = "[FAIL]"

    def __init__(self, headless=False):
        self.driver = None
        self.base_url = None
        self.headless = headless

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

    def test_01_all_elements_present(self):
        """Test Case 1: Check all form elements are present and visible"""
        print("\n=== TEST 1: All Form Elements Present ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Check form elements
            elements = {
                "Form": "feedbackForm",
                "Student Name Input": "studentName",
                "Email Input": "email",
                "Mobile Input": "mobile",
                "Department Select": "department",
                "Male Radio": "genderMale",
                "Female Radio": "genderFemale",
                "Other Radio": "genderOther",
                "Feedback Textarea": "feedback",
                "Submit Button": "submitBtn",
                "Reset Button": "resetBtn",
            }

            for element_name, element_id in elements.items():
                element = self.driver.find_element(By.ID, element_id)
                assert element.is_displayed(), f"{element_name} is not visible"
                print(f"{self.PASS_SYMBOL} {element_name} is present and visible")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_02_css_styling(self):
        """Test Case 2: Test CSS styling and layout"""
        print("\n=== TEST 2: CSS Styling and Layout ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Check container styling
            container = self.driver.find_element(By.CLASS_NAME, "container")
            container_width = container.size["width"]
            print(f"{self.PASS_SYMBOL} Container width: {container_width}px")

            # Check form title
            title = self.driver.find_element(By.TAG_NAME, "h1")
            title_text = title.text
            assert "Student Feedback Registration" in title_text
            print(f"{self.PASS_SYMBOL} Form title displayed correctly: '{title_text}'")

            # Check buttons are styled
            submit_btn = self.driver.find_element(By.ID, "submitBtn")
            reset_btn = self.driver.find_element(By.ID, "resetBtn")

            submit_color = submit_btn.value_of_css_property("background-color")
            print(
                f"{self.PASS_SYMBOL} Submit button has background color: {submit_color}"
            )

            reset_color = reset_btn.value_of_css_property("background-color")
            print(
                f"{self.PASS_SYMBOL} Reset button has background color: {reset_color}"
            )

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_03_accessibility_attributes(self):
        """Test Case 3: Test form element accessibility attributes"""
        print("\n=== TEST 3: Accessibility Attributes ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Check labels are associated with inputs
            labels = self.driver.find_elements(By.TAG_NAME, "label")
            print(f"{self.PASS_SYMBOL} Found {len(labels)} labels")

            # Check input types
            email_input = self.driver.find_element(By.ID, "email")
            email_type = email_input.get_attribute("type")
            assert email_type == "email"
            print(f"{self.PASS_SYMBOL} Email input has correct type: {email_type}")

            mobile_input = self.driver.find_element(By.ID, "mobile")
            mobile_type = mobile_input.get_attribute("type")
            assert mobile_type == "tel"
            print(f"{self.PASS_SYMBOL} Mobile input has correct type: {mobile_type}")

            # Check name attributes
            name_input = self.driver.find_element(By.ID, "studentName")
            name_attr = name_input.get_attribute("name")
            assert name_attr == "studentName"
            print(f"{self.PASS_SYMBOL} Name input has correct name attribute")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_04_placeholder_text(self):
        """Test Case 4: Test placeholder text"""
        print("\n=== TEST 4: Placeholder Text ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            placeholders = {
                "studentName": "Enter your full name",
                "email": "Enter your email",
                "mobile": "Enter 10-digit mobile number",
                "feedback": "Enter your feedback (minimum 10 words)",
            }

            for field_id, expected_placeholder in placeholders.items():
                element = self.driver.find_element(By.ID, field_id)
                actual_placeholder = element.get_attribute("placeholder")
                assert (
                    expected_placeholder in actual_placeholder
                    or actual_placeholder in expected_placeholder
                )
                print(f"{self.PASS_SYMBOL} {field_id}: '{actual_placeholder}'")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_05_button_states(self):
        """Test Case 5: Test button states and styling"""
        print("\n=== TEST 5: Button States and Styling ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            submit_btn = self.driver.find_element(By.ID, "submitBtn")
            reset_btn = self.driver.find_element(By.ID, "resetBtn")

            # Check buttons are enabled
            assert submit_btn.is_enabled()
            print(f"{self.PASS_SYMBOL} Submit button is enabled")

            assert reset_btn.is_enabled()
            print(f"{self.PASS_SYMBOL} Reset button is enabled")

            # Check button text
            assert submit_btn.text == "Submit"
            print(f"{self.PASS_SYMBOL} Submit button has correct text")

            assert reset_btn.text == "Reset"
            print(f"{self.PASS_SYMBOL} Reset button has correct text")

            # Check button types
            submit_type = submit_btn.get_attribute("type")
            reset_type = reset_btn.get_attribute("type")

            assert submit_type == "submit"
            print(f"{self.PASS_SYMBOL} Submit button type: {submit_type}")

            assert reset_type == "reset"
            print(f"{self.PASS_SYMBOL} Reset button type: {reset_type}")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_06_responsive_design(self):
        """Test Case 6: Test responsive design"""
        print("\n=== TEST 6: Responsive Design ===")
        try:
            # Test different viewport sizes
            viewports = [
                (1920, 1080, "Desktop"),
                (1024, 768, "Tablet"),
                (375, 667, "Mobile"),
            ]

            for width, height, device in viewports:
                self.driver.set_window_size(width, height)
                self.driver.get(self.base_url)
                time.sleep(1)

                # Check form is still visible
                form = self.driver.find_element(By.ID, "feedbackForm")
                assert form.is_displayed()
                print(
                    f"{self.PASS_SYMBOL} Form displays correctly on {device} ({width}x{height})"
                )

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def test_07_focus_states(self):
        """Test Case 7: Test form field focus states"""
        print("\n=== TEST 7: Form Field Focus States ===")
        try:
            self.driver.get(self.base_url)
            time.sleep(1)

            # Test focusing on different elements
            fields = ["studentName", "email", "mobile", "feedback"]

            for field_id in fields:
                element = self.driver.find_element(By.ID, field_id)
                element.click()  # Focus on element
                time.sleep(0.3)

                # Check element is focused (active element)
                active_element = self.driver.switch_to.active_element
                active_id = active_element.get_attribute("id")
                assert active_id == field_id
                print(f"{self.PASS_SYMBOL} {field_id} can receive focus")

            return True
        except Exception as e:
            print(f"{self.FAIL_SYMBOL} Test failed: {str(e)}")
            return False

    def run_all_tests(self):
        """Run all UI test cases"""
        print("\n" + "=" * 60)
        print("UI ELEMENTS TEST SUITE - CHROME WEBDRIVER")
        print("=" * 60)
        if self.headless:
            print("[INFO] Running in HEADLESS mode")
        else:
            print("[INFO] Running in NORMAL mode")

        results = []

        # Run each test
        self.setup()
        results.append(("All Elements Present", self.test_01_all_elements_present()))
        self.teardown()

        self.setup()
        results.append(("CSS Styling", self.test_02_css_styling()))
        self.teardown()

        self.setup()
        results.append(
            ("Accessibility Attributes", self.test_03_accessibility_attributes())
        )
        self.teardown()

        self.setup()
        results.append(("Placeholder Text", self.test_04_placeholder_text()))
        self.teardown()

        self.setup()
        results.append(("Button States", self.test_05_button_states()))
        self.teardown()

        self.setup()
        results.append(("Responsive Design", self.test_06_responsive_design()))
        self.teardown()

        self.setup()
        results.append(("Focus States", self.test_07_focus_states()))
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
    test_suite = TestUIElements(headless=headless_mode)
    exit_code = test_suite.run_all_tests()
    sys.exit(exit_code)
