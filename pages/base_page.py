from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.clear()
        except Exception:
            self.driver.execute_script("arguments[0].value = '';", element)

        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_displayed(self, locator):
        try:
            return self.find_visible(locator).is_displayed()
        except (TimeoutException, Exception):
            return False

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_invisibility(self, locator, timeout=10):
        self.wait.until(EC.invisibility_of_element_located(locator))