import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdsPage(BasePage):
    URL = "https://practice-automation.com/ads/"

    SIMPLE_MODAL_BTN = (By.ID, "simpleModal")
    FORM_MODAL_BTN = (By.ID, "formModal")

    AD_OVERLAY = (By.ID, "pum-1272")
    AD_TITLE = (By.ID, "pum_popup_title_1272")
    AD_CONTENT = (By.CSS_SELECTOR, "#pum-1272 .pum-content")
    AD_CLOSE = (By.CSS_SELECTOR, "#pum-1272 .pum-close")

    SIMPLE_MODAL_OVERLAY = (By.ID, "pum-1318")
    SIMPLE_MODAL_TITLE = (By.ID, "pum_popup_title_1318")
    SIMPLE_MODAL_CONTENT = (By.CSS_SELECTOR, "#pum-1318 .pum-content")
    SIMPLE_MODAL_CLOSE = (By.CSS_SELECTOR, "#pum-1318 .pum-close")

    FORM_MODAL_OVERLAY = (By.ID, "pum-674")
    FORM_MODAL_TITLE = (By.ID, "pum_popup_title_674")
    FORM_NAME_INPUT = (By.ID, "g1274-name")
    FORM_EMAIL_INPUT = (By.ID, "g1274-email")
    FORM_MESSAGE_INPUT = (By.ID, "contact-form-comment-g1274-message")
    FORM_SUBMIT_BTN = (By.CSS_SELECTOR, "#pum-674 .pushbutton-wide")
    FORM_MODAL_CLOSE = (By.CSS_SELECTOR, "#pum-674 .pum-close")
    FORM_SUCCESS = (By.CSS_SELECTOR, "#pum-674 [id*='contact-form-success'] h4")

    def open_ads(self):
        self.open(self.URL)

    def wait_for_ad(self, timeout=10):
        self.wait.until(
            lambda d: d.find_element(*self.AD_OVERLAY).is_displayed()
        )

    def is_ad_visible(self):
        return self.is_displayed(self.AD_OVERLAY)

    def get_ad_title(self):
        return self.get_text(self.AD_TITLE)

    def get_ad_content(self):
        return self.get_text(self.AD_CONTENT)

    def close_ad(self):
        self.click(self.AD_CLOSE)

    def click_simple_modal(self):
        self.click(self.SIMPLE_MODAL_BTN)

    def is_simple_modal_visible(self):
        return self.is_displayed(self.SIMPLE_MODAL_OVERLAY)

    def get_simple_modal_title(self):
        return self.get_text(self.SIMPLE_MODAL_TITLE)

    def close_simple_modal(self):
        self.click(self.SIMPLE_MODAL_CLOSE)

    def click_form_modal(self):
        self.click(self.FORM_MODAL_BTN)

    def is_form_modal_visible(self):
        return self.is_displayed(self.FORM_MODAL_OVERLAY)

    def fill_form_name(self, name):
        self.send_keys(self.FORM_NAME_INPUT, name)

    def fill_form_email(self, email):
        self.send_keys(self.FORM_EMAIL_INPUT, email)

    def fill_form_message(self, text):
        self.send_keys(self.FORM_MESSAGE_INPUT, text)

    def click_form_submit(self):
        self.click(self.FORM_SUBMIT_BTN)

    def get_form_success_message(self):
        return self.get_text(self.FORM_SUCCESS)

    def close_form_modal(self):
        self.click(self.FORM_MODAL_CLOSE)