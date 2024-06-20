from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def is_displayed(self, locator):
        try:
            element = self.wait_for_element(locator)
            return element.is_displayed()
        except:
            return False

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
