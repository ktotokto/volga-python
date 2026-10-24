from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class ModalPage(BasePage):
    URL = "https://practice-automation.com/modals/"

    SIMPLE_MODAL_BTN = (By.ID, "simpleModal")
    FORM_MODAL_BTN = (By.ID, "formModal")

    SIMPLE_MODAL_OVERLAY = (By.ID, "pum-1318")
    SIMPLE_MODAL_TITLE = (By.ID, "pum_popup_title_1318")
    SIMPLE_MODAL_CONTENT = (By.CSS_SELECTOR, "#pum-1318 .pum-content")
    SIMPLE_MODAL_CLOSE = (By.CSS_SELECTOR, "#pum-1318 .pum-close")

    FORM_MODAL_OVERLAY = (By.ID, "pum-674")
    FORM_MODAL_TITLE = (By.ID, "pum_popup_title_674")
    FORM_NAME_INPUT = (By.ID, "g1051-name")
    FORM_EMAIL_INPUT = (By.ID, "g1051-email")
    FORM_MESSAGE_INPUT = (By.ID, "contact-form-comment-g1051-message")
    FORM_SUBMIT_BTN = (By.CSS_SELECTOR, "#pum-674 .pushbutton-wide")
    FORM_MODAL_CLOSE = (By.CSS_SELECTOR, "#pum-674 .pum-close")
    FORM_SUCCESS = (By.CSS_SELECTOR, "#pum-674 [id*='contact-form-success'] h4")

    def open_modals(self):
        self.open(self.URL)

    def click_simple_modal(self):
        self.click(self.SIMPLE_MODAL_BTN)
        self.wait.until(lambda d: d.find_element(*self.SIMPLE_MODAL_OVERLAY).is_displayed())

    def is_simple_modal_visible(self):
        return self.is_displayed(self.SIMPLE_MODAL_OVERLAY)

    def get_simple_modal_title(self):
        return self.get_text(self.SIMPLE_MODAL_TITLE)

    def get_simple_modal_content(self):
        return self.get_text(self.SIMPLE_MODAL_CONTENT)

    def close_simple_modal(self):
        self.click(self.SIMPLE_MODAL_CLOSE)
        self.wait_for_invisibility(self.SIMPLE_MODAL_OVERLAY)

    def click_form_modal(self):
        self.click(self.FORM_MODAL_BTN)
        self.wait.until(lambda d: d.find_element(*self.FORM_MODAL_OVERLAY).is_displayed())

    def is_form_modal_visible(self):
        return self.is_displayed(self.FORM_MODAL_OVERLAY)

    def get_form_modal_title(self):
        return self.get_text(self.FORM_MODAL_TITLE)

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
        self.wait_for_invisibility(self.FORM_MODAL_OVERLAY)

    def close_form_modal_by_escape(self):
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.wait_for_invisibility(self.FORM_MODAL_OVERLAY)