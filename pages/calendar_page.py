from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalendarPage(BasePage):
    URL = "https://practice-automation.com/calendars/"

    DATE_INPUT = (By.ID, "g1065-1-selectorenteradate")
    SUBMIT_DATE_BTN = (By.CSS_SELECTOR, "#jp-form-d789f525b512b8c992166cfbd9a18204964b4777 button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id*='contact-form-success'] h4")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".contact-form__input-error.has-errors span:last-child")
    DATE_SUCCESS = (By.CSS_SELECTOR, "#contact-form-success-d789f525b512b8c992166cfbd9a18204964b4777 h4")
    DATE_SUBMIT_BTN = (By.CSS_SELECTOR, "#jp-form-d789f525b512b8c992166cfbd9a18204964b4777 button[type='submit']")


    def open_calendar(self):
        self.open(self.URL)

    def enter_date(self, date_text):
        self.send_keys(self.DATE_INPUT, date_text)

    def click_submit_date(self):
        self.click(self.SUBMIT_DATE_BTN)

    def is_date_success_visible(self, timeout=3):
        try:
            from selenium.webdriver.support import expected_conditions as EC
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.DATE_SUCCESS)
            )
            return True
        except:
            return False

    def is_date_field_present(self, timeout):
        return self.is_element_present(self.DATE_INPUT, timeout=timeout)

    def get_success_message(self):
        WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return self.get_text(self.ERROR_MESSAGE)