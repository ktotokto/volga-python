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

    NAME_INPUT = (By.ID, "g1065-name")
    EMAIL_INPUT = (By.ID, "g1065-email")
    MESSAGE_TEXTAREA = (By.ID, "contact-form-comment-g1065-message")
    SUBMIT_FORM_BTN = (By.CSS_SELECTOR, "#jp-form-4ae566e741892db7f82c27b19f133d98dbda317d button[type='submit']")


    def open_calendar(self):
        self.open(self.URL)

    def enter_date(self, date_text):
        self.send_keys(self.DATE_INPUT, date_text)

    def click_submit_date(self):
        self.click(self.SUBMIT_DATE_BTN)

    def get_success_message(self):
        WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return self.get_text(self.ERROR_MESSAGE)

    def click_submit_form(self):
        self.click(self.SUBMIT_FORM_BTN)