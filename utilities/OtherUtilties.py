from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

class Utilities:
    @staticmethod
    def take_screenshot(driver,
                        test_name,
                        status):
        # Check if the specific element is visible
        screenshot_path =f".\\Screenshots\\{test_name}_{status}.png"
        screenshot =  driver.save_screenshot(screenshot_path)
        return screenshot


    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """Waits for an element to be visible on the page."""
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {timeout} seconds.")



class TestStatus:
    """Utility class to manage test status across files."""
    status = {}  # Dictionary to store status of tests by name

    @staticmethod
    def set_status(test_name, status):
        """Set the status of a test case."""
        TestStatus.status[test_name] = status

    @staticmethod
    def get_status(test_name):
        """Get the status of a test case."""
        return TestStatus.status.get(test_name, False)  # Default to False if not set

    @staticmethod
    def all_tests_passed(*test_names):
        """Check if all specified test cases have passed."""
        return all(TestStatus.get_status(test) for test in test_names)

    @staticmethod
    def check_status(*test_names):
        """
        Check the status of one or more test cases.

        If a single test case name is passed, return its status (True/False).
        If multiple test case names are passed, return True only if all have passed.
        """
        if len(test_names) == 1:
            return TestStatus.status.get(test_names[0], False)  # Return status of the single test
        return all(TestStatus.status.get(test, False) for test in test_names)  # Check all tests


class Utilities2:
    @staticmethod
    def take_screenshot(driver,
                        test_name,
                        status,
                        element_locator=None,
                        timeout=5):
        """
        Captures a screenshot if a specific element is visible, otherwise takes a full-page screenshot.
        """
        screenshots_dir = "./Screenshots1/"
        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{status}.png")

        if element_locator:
            try:
                WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(element_locator))
            except TimeoutException:
                print(f"Element {element_locator} not visible. Taking full-page screenshot.")

        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        return screenshot_path
