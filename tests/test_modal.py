import pytest
import allure
from pages.modal_page import ModalPage


@allure.feature("Модальные окна")
class TestModal:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = ModalPage(driver)

    @allure.story("Simple Modal")
    @allure.title("Открытие простой модалки")
    def test_open_simple_modal(self):
        self.page.open_modals()
        self.page.click_simple_modal()
        assert self.page.is_simple_modal_visible()

    @allure.story("Simple Modal")
    @allure.title("Проверка заголовка простой модалки")
    def test_simple_modal_title(self):
        self.page.open_modals()
        self.page.click_simple_modal()
        title = self.page.get_simple_modal_title()
        assert title == "Simple Modal"

    @allure.story("Simple Modal")
    @allure.title("Проверка содержимого простой модалки")
    def test_simple_modal_content(self):
        self.page.open_modals()
        self.page.click_simple_modal()
        content = self.page.get_simple_modal_content()
        assert "simple modal" in content.lower()

    @allure.story("Simple Modal")
    @allure.title("Закрытие простой модалки")
    def test_close_simple_modal(self):
        self.page.open_modals()
        self.page.click_simple_modal()
        self.page.close_simple_modal()
        assert not self.page.is_simple_modal_visible()

    @allure.story("Form Modal")
    @allure.title("Открытие модалки с формой")
    def test_open_form_modal(self):
        self.page.open_modals()
        self.page.click_form_modal()
        assert self.page.is_form_modal_visible()

    @allure.story("Form Modal")
    @allure.title("Заголовок модалки с формой")
    def test_form_modal_title(self):
        self.page.open_modals()
        self.page.click_form_modal()
        title = self.page.get_form_modal_title()
        assert "Form" in title

    @allure.story("Form Modal")
    @allure.title("Заполнение и отправка формы в модалке")
    def test_fill_and_submit_form_modal(self):
        self.page.open_modals()
        self.page.click_form_modal()
        self.page.fill_form_name("Тест")
        self.page.fill_form_email("test@test.com")
        self.page.fill_form_message("Сообщение")
        self.page.click_form_submit()
        message = self.page.get_form_success_message()
        assert "Thank you" in message

    @allure.story("Form Modal")
    @allure.title("Закрытие модалки с формой по кнопке")
    def test_close_form_modal_by_button(self):
        self.page.open_modals()
        self.page.click_form_modal()
        self.page.close_form_modal()
        assert not self.page.is_form_modal_visible()

    @allure.story("Form Modal")
    @allure.title("Закрытие модалки клавишей Escape")
    def test_close_form_modal_by_escape(self):
        self.page.open_modals()
        self.page.click_form_modal()
        self.page.close_form_modal_by_escape()
        assert not self.page.is_form_modal_visible()


    @allure.story("Негативные")
    @allure.title("Отправка пустой формы в модалке")
    def test_submit_empty_form_modal(self):
        self.page.open_modals()
        self.page.click_form_modal()
        self.page.click_form_submit()
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "#pum-674 [id*='contact-form-success'] h4"),
            timeout=3
        )

    @allure.story("Негативные")
    @allure.title("Некорректный email в модалке")
    def test_invalid_email_in_modal(self):
        self.page.open_modals()
        self.page.click_form_modal()
        self.page.fill_form_name("Тест")
        self.page.fill_form_email("bad")
        self.page.click_form_submit()
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "#pum-674 [id*='contact-form-success'] h4"),
            timeout=3
        )


from selenium.webdriver.common.by import By