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

    def open_ads(self):
        self.open(self.URL)

    def wait_for_ad(self, timeout=10):
        self.wait.until(lambda d: d.find_element(*self.AD_OVERLAY).is_displayed())

    def is_ad_visible(self):
        return self.is_displayed(self.AD_OVERLAY)

    def get_ad_title(self):
        return self.get_text(self.AD_TITLE)

    def get_ad_content(self):
        return self.get_text(self.AD_CONTENT)

    def close_ad(self):
        self.click(self.AD_CLOSE)
        self.wait_for_invisibility(self.AD_OVERLAY)
