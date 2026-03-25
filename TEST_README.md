# Selenium Test Suite - Chrome WebDriver

Comprehensive Selenium test suite for the Student Feedback Registration Form using Chrome WebDriver.

## Test Files

### 1. test_feedback_form.py
Main functional test suite covering:
- Page load verification
- Valid form submission
- Empty field validation
- Invalid email validation
- Invalid mobile validation
- Dropdown selection
- Button functionality (Submit/Reset)

### 2. test_ui_elements.py
UI and accessibility test suite covering:
- Form element presence and visibility
- CSS styling and layout verification
- Accessibility attributes
- Placeholder text validation
- Button states and styling
- Responsive design (Desktop/Tablet/Mobile)
- Form field focus states

### 3. test_advanced_scenarios.py
Advanced test scenarios with screenshot capabilities:
- Keyboard navigation (Tab key)
- Special character handling
- Maximum length input testing
- Rapid submission handling
- Error message clearing
- Success message persistence
- Reset functionality during error states

### 4. run_all_tests.py
Master test runner that executes all test suites and provides comprehensive reporting.

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- selenium>=4.0.0
- webdriver-manager>=4.0.0

## Running Tests

### Run Individual Test Suites

```bash
# Feedback form tests
python test_feedback_form.py

# UI elements tests
python test_ui_elements.py

# Advanced scenarios tests
python test_advanced_scenarios.py
```

### Run All Tests

```bash
# Normal mode (with browser window)
python run_all_tests.py

# Headless mode (no browser window, for CI/CD)
python run_all_tests.py --headless

# Advanced scenarios without screenshots
python test_advanced_scenarios.py --no-screenshots
```

## Headless Mode

All test suites support headless mode for CI/CD environments:

```bash
python test_feedback_form.py --headless
python test_ui_elements.py --headless
python test_advanced_scenarios.py --headless
```

Headless mode is automatically enabled when `CI=true` environment variable is set.

## Screenshots

The advanced test suite (`test_advanced_scenarios.py`) automatically captures screenshots during test execution. Screenshots are saved in the `test_screenshots/` directory with timestamps.

To disable screenshots:
```bash
python test_advanced_scenarios.py --no-screenshots
```

## Test Results

Test results are displayed with clear indicators:
- `[PASS]` - Test passed successfully
- `[FAIL]` - Test failed

Each test suite provides:
- Individual test case results
- Summary with pass/fail counts
- Success rate percentage
- Exit code (0 for success, 1 for failure)

## CI/CD Integration

These tests are designed for Jenkins/CI pipeline integration:

1. Tests run in headless mode when `CI=true` environment variable is set
2. Exit codes indicate success (0) or failure (1)
3. Compatible with Windows and Linux environments
4. Detailed console output for Jenkins logs

## Browser Compatibility

Currently configured for Chrome/Chromium browsers. The test suite uses:
- ChromeDriver (auto-managed by webdriver-manager)
- Chrome browser (must be installed on the system)

## Test Coverage

Total test cases across all suites:
- **Feedback Form**: 7 test cases
- **UI Elements**: 7 test cases
- **Advanced Scenarios**: 7 test cases
- **Total**: 21 comprehensive test cases

## File Structure

```
CA-2/
├── index.html                      # Form HTML
├── styles.css                      # Form styles
├── validation.js                   # Form validation
├── requirements.txt                # Python dependencies
├── test_feedback_form.py          # Main test suite
├── test_ui_elements.py            # UI/accessibility tests
├── test_advanced_scenarios.py     # Advanced tests with screenshots
├── run_all_tests.py               # Test runner
├── TEST_README.md                 # This file
└── test_screenshots/              # Screenshot directory (auto-created)
```

## Troubleshooting

### ChromeDriver Issues
If ChromeDriver is not found, ensure Chrome browser is installed and up to date. The `webdriver-manager` package will automatically download the correct ChromeDriver version.

### Headless Mode Failures
Some tests may behave differently in headless mode. The test suite includes appropriate waits and timeouts to handle this.

### Screenshot Directory
The `test_screenshots/` directory is automatically created when running advanced tests with screenshot capability enabled.

## License

This test suite is part of the DevOps CA-2 project.
