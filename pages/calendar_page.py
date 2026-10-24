from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CalendarPage(BasePage):
    URL = "https://practice-automation.com/calendars/"

    DATE_INPUT = (By.ID, "g1065-1-selectorenteradate")
    SUBMIT_DATE_BTN = (By.CSS_SELECTOR, "#jp-form-d789f525b512b8c992166cfbd9a18204964b4777 button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id*='contact-form-success'] h4")

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
        return self.get_text(self.SUCCESS_MESSAGE)

    def fill_name(self, name):
        self.send_keys(self.NAME_INPUT, name)

    def fill_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def fill_message(self, text):
        self.send_keys(self.MESSAGE_TEXTAREA, text)

    def click_submit_form(self):
        self.click(self.SUBMIT_FORM_BTN)