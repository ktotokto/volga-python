import pytest
import allure
from pages.ads_page import AdsPage


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
    @allure.title("Проверка содержимого рекламы")
    def test_ad_title(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        title = self.page.get_ad_title()
        content = self.page.get_ad_content()
        assert title == "Hi" and "ad" in content.lower()

    @allure.story("Рекламная модалка")
    @allure.title("Закрытие рекламной модалки")
    def test_close_ad(self):
        self.page.open_ads()
        self.page.wait_for_ad()
        self.page.close_ad()
        assert not self.page.is_ad_visible()
