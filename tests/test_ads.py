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
        with allure.step("Открыть страницу рекламных окон"):
            self.page.open_ads()
        with allure.step("Дождаться появления рекламной модалки"):
            self.page.wait_for_ad()
        with allure.step("Проверить видимость рекламной модалки"):
            assert self.page.is_ad_visible()

    @allure.story("Рекламная модалка")
    @allure.title("Проверка содержимого рекламы")
    def test_ad_title(self):
        with allure.step("Открыть страницу рекламных окон"):
            self.page.open_ads()
        with allure.step("Дождаться появления рекламной модалки"):
            self.page.wait_for_ad()
        with allure.step("Получить заголовок и содержимое рекламы"):
            title = self.page.get_ad_title()
            content = self.page.get_ad_content()
        with allure.step("Проверить заголовок и содержимое"):
            assert title == "Hi"
            assert "ad" in content.lower()

    @allure.story("Рекламная модалка")
    @allure.title("Закрытие рекламной модалки")
    def test_close_ad(self):
        with allure.step("Открыть страницу рекламных окон"):
            self.page.open_ads()
        with allure.step("Дождаться появления рекламной модалки"):
            self.page.wait_for_ad()
        with allure.step("Закрыть рекламную модалку"):
            self.page.close_ad()
        with allure.step("Проверить невидимость рекламной модалки"):
            assert not self.page.is_ad_visible()