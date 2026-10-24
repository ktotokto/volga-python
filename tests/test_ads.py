import pytest
import allure
from pages.ads_page import AdsPage
from utils.automation_tools import get_automation_tools_text


@allure.feature("Рекламные окна")
class TestAds:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = AdsPage(driver)

    @allure.story("Рекламная модалка")
    @allure.title("Рекламная модалка появляется автоматически")
    def test_ad_appears_automatically(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        assert self.page.is_ad_visible()

    @allure.story("Рекламная модалка")
    @allure.title("Проверка заголовка рекламы")
    def test_ad_title(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        title = self.page.get_ad_title()
        assert title == "Hi"

    @allure.story("Рекламная модалка")
    @allure.title("Проверка содержимого рекламы")
    def test_ad_content(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        content = self.page.get_ad_content()
        assert "ad" in content.lower()

    @allure.story("Рекламная модалка")
    @allure.title("Закрытие рекламной модалки")
    def test_close_ad(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        assert not self.page.is_ad_visible()

    @allure.story("Simple Modal на странице Ads")
    @allure.title("Открытие простой модалки на странице Ads")
    def test_open_simple_modal_on_ads(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        self.page.click_simple_modal()
        assert self.page.is_simple_modal_visible()

    @allure.story("Form Modal на странице Ads")
    @allure.title("Заполнение формы в модалке на странице Ads")
    def test_fill_form_modal_on_ads(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        self.page.click_form_modal()
        self.page.fill_form_name("Тест")
        self.page.fill_form_email("test@test.com")
        self.page.fill_form_message("Тест")
        self.page.click_form_submit()
        message = self.page.get_form_success_message()
        assert "Thank you" in message

    @allure.story("Поле Message")
    @allure.title("Заполнение поля Message данными из Automation Tools")
    def test_fill_message_from_automation_tools(self):
        from selenium.webdriver.common.by import By
        tools_text = get_automation_tools_text(self.page.driver)
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        self.page.click_form_modal()
        self.page.fill_form_name("Тест")
        self.page.fill_form_email("test@test.com")
        self.page.fill_form_message(tools_text)
        self.page.click_form_submit()
        message = self.page.get_form_success_message()
        assert "Thank you" in message

    @allure.story("Негативные")
    @allure.title("Попытка отправить пустую форму в модалке Ads")
    def test_submit_empty_form_on_ads(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        self.page.click_form_modal()
        self.page.click_form_submit()
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "#pum-674 [id*='contact-form-success'] h4"),
            timeout=3
        )

    @allure.story("Негативные")
    @allure.title("Некорректный email в форме Ads")
    def test_invalid_email_on_ads(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        self.page.click_form_modal()
        self.page.fill_form_name("Тест")
        self.page.fill_form_email("неправильный")
        self.page.click_form_submit()
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "#pum-674 [id*='contact-form-success'] h4"),
            timeout=3
        )


from selenium.webdriver.common.by import By