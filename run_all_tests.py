#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Selenium Test Runner - Chrome WebDriver
Runs all Selenium test suites for the Student Feedback Form
"""

import sys
import os
import time
from datetime import datetime

# Import all test suites
from test_feedback_form import TestStudentFeedbackForm
from test_ui_elements import TestUIElements
from test_advanced_scenarios import TestAdvancedScenarios


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_section(title):
    """Print formatted section"""
    print("\n" + "-" * 70)
    print(f"  {title}")
    print("-" * 70)


def run_all_tests(headless=False):
    """Run all test suites and collect results"""

    print_header("SELENIUM TEST SUITE - CHROME WEBDRIVER")
    print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Mode: {'HEADLESS (CI/CD)' if headless else 'NORMAL (Browser Window)'}")
    print(f"Python Version: {sys.version}")

    all_results = {}
    total_passed = 0
    total_failed = 0

    # Test Suite 1: Feedback Form Tests
    print_section("Running Test Suite 1: Feedback Form Tests")
    suite1 = TestStudentFeedbackForm(headless=headless)
    exit_code1 = suite1.run_all_tests()
    all_results["Feedback Form Tests"] = exit_code1

    # Test Suite 2: UI Elements Tests
    print_section("Running Test Suite 2: UI Elements Tests")
    suite2 = TestUIElements(headless=headless)
    exit_code2 = suite2.run_all_tests()
    all_results["UI Elements Tests"] = exit_code2

    # Test Suite 3: Advanced Scenarios Tests
    print_section("Running Test Suite 3: Advanced Scenarios Tests")
    suite3 = TestAdvancedScenarios(headless=headless, screenshots=not headless)
    exit_code3 = suite3.run_all_tests()
    all_results["Advanced Scenarios Tests"] = exit_code3

    # Print overall summary
    print_header("OVERALL TEST SUMMARY")

    for suite_name, exit_code in all_results.items():
        status = "PASSED" if exit_code == 0 else "FAILED"
        symbol = "[PASS]" if exit_code == 0 else "[FAIL]"
        print(f"{symbol} {suite_name}: {status}")

        if exit_code == 0:
            total_passed += 1
        else:
            total_failed += 1

    print("\n" + "=" * 70)
    print(f"Total Test Suites: {len(all_results)}")
    print(f"Suites Passed: {total_passed}")
    print(f"Suites Failed: {total_failed}")

    if total_failed == 0:
        print("\n✓ ALL TEST SUITES PASSED!")
        print("=" * 70)
        return 0
    else:
        print(f"\n✗ {total_failed} TEST SUITE(S) FAILED")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    # Check for headless mode
    headless_mode = "--headless" in sys.argv or os.environ.get("CI") == "true"

    # Add help option
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Selenium Test Runner - Chrome WebDriver")
        print("\nUsage:")
        print("  python run_all_tests.py              # Run with browser window")
        print("  python run_all_tests.py --headless   # Run in headless mode")
        print("\nOptions:")
        print("  --headless    Run tests in headless mode (no browser window)")
        print("  -h, --help    Show this help message")
        sys.exit(0)

    # Run all tests
    exit_code = run_all_tests(headless=headless_mode)
    sys.exit(exit_code)
