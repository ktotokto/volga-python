import pytest
import allure
from pages.modal_page import ModalPage
from utils.automation_tools import get_automation_tools_text


@allure.feature("Модальные окна")
class TestModal:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = ModalPage(driver)

    @allure.story("Simple Modal")
    @allure.title("Открытие простой модалки")
    def test_open_simple_modal(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Simple Modal"):
            self.page.click_simple_modal()
        with allure.step("Проверить видимость простой модалки"):
            assert self.page.is_simple_modal_visible()

    @allure.story("Simple Modal")
    @allure.title("Проверка содержимого и заголовка простой модалки")
    def test_simple_modal_content(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Simple Modal"):
            self.page.click_simple_modal()
        with allure.step("Получить заголовок и содержимое модалки"):
            title = self.page.get_simple_modal_title()
            content = self.page.get_simple_modal_content()
        with allure.step("Проверить соответствие заголовка и содержимого"):
            assert title == "Simple Modal"
            assert "simple modal" in content.lower()

    @allure.story("Simple Modal")
    @allure.title("Закрытие простой модалки")
    def test_close_simple_modal(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Simple Modal"):
            self.page.click_simple_modal()
        with allure.step("Закрыть простую модалку"):
            self.page.close_simple_modal()
        with allure.step("Проверить невидимость простой модалки"):
            assert not self.page.is_simple_modal_visible()

    @allure.story("Form Modal")
    @allure.title("Открытие модалки с формой")
    def test_open_form_modal(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Проверить видимость модалки с формой"):
            assert self.page.is_form_modal_visible()

    @allure.story("Form Modal")
    @allure.title("Проверка заголовка модалки с формой")
    def test_form_modal_title(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Получить заголовок модалки"):
            title = self.page.get_form_modal_title()
        with allure.step("Проверить наличие слова 'Form' в заголовке"):
            assert "Form" in title

    @allure.story("Form Modal")
    @allure.title("Заполнение и отправка формы")
    @allure.description(
        "Получает список инструментов на главной странице, преобразует в текст через запятую и заполняет поле Message")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_message_from_automation_tools(self, driver):
        with allure.step("Получить список инструментов из раздела Start learning"):
            tools_text = get_automation_tools_text(driver)
            allure.attach(
                tools_text,
                name="Текст из раздела Start learning",
                attachment_type=allure.attachment_type.TEXT
            )
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Заполнить поле Name"):
            self.page.fill_form_name("Гриша")
        with allure.step("Заполнить поле Email"):
            self.page.fill_form_email("mail@mail.com")
        with allure.step("Заполнить поле Message текстом из Start learning"):
            self.page.fill_form_message(tools_text)
        with allure.step("Нажать кнопку Submit"):
            self.page.click_form_submit()
        with allure.step("Проверить сообщение об успехе"):
            message = self.page.get_form_success_message()
            assert "Thank you" in message, f"Ожидалось сообщение об успехе, получено: {message}"

    @allure.story("Form Modal")
    @allure.title("Закрытие модалки с формой по кнопке")
    def test_close_form_modal_by_button(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Закрыть модалку по кнопке"):
            self.page.close_form_modal()
        with allure.step("Проверить невидимость модалки с формой"):
            assert not self.page.is_form_modal_visible()

    @allure.story("Form Modal")
    @allure.title("Закрытие модалки клавишей Escape")
    def test_close_form_modal_by_escape(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Закрыть модалку клавишей Escape"):
            self.page.close_form_modal_by_escape()
        with allure.step("Проверить невидимость модалки с формой"):
            assert not self.page.is_form_modal_visible()

    @allure.story("Негативные")
    @allure.title("Некорректный email в модалке")
    def test_invalid_email_in_modal(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Заполнить поле Name"):
            self.page.fill_form_name("Боб")
        with allure.step("Ввести некорректный email"):
            self.page.fill_form_email("непочта")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_form_submit()
        with allure.step("Проверить появление сообщения об ошибке email"):
            message = self.page.get_form_email_error_message()
            assert "Please enter" in message

    @allure.story("Негативные")
    @allure.title("Отправка пустой формы в модалке")
    def test_submit_empty_form_modal(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Нажать кнопку Submit без заполнения полей"):
            self.page.click_form_submit()
        with allure.step("Получить текст общей ошибки формы"):
            error_message = self.page.get_text(self.page.FORM_ERROR_MESSAGE)
        with allure.step("Проверить наличие сообщения об общей ошибке"):
            assert "Please fill out the form correctly" in error_message
        with allure.step("Проверить наличие списка ошибок"):
            assert self.page.is_element_present(self.page.FORM_ERROR_LIST, timeout=3)
        with allure.step("Проверить, что модалка осталась открытой"):
            assert self.page.is_form_modal_visible()

    @allure.story("Негативные")
    @allure.title("Отправка формы с пустым полем Name")
    def test_submit_form_with_empty_name(self):
        with allure.step("Открыть страницу модальных окон"):
            self.page.open_modals()
        with allure.step("Нажать кнопку Form Modal"):
            self.page.click_form_modal()
        with allure.step("Заполнить только поле Email"):
            self.page.fill_form_email("mail@mail.com")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_form_submit()
        with allure.step("Получить текст общей ошибки формы"):
            error_message = self.page.get_text(self.page.FORM_ERROR_MESSAGE)
        with allure.step("Проверить наличие сообщения об общей ошибке"):
            assert "Please fill out the form correctly" in error_message
        with allure.step("Получить список конкретных ошибок"):
            error_list = self.page.get_form_errors()
        with allure.step("Проверить наличие ошибки для поля Name"):
            assert any("Name" in error and "required" in error for error in error_list)
        with allure.step("Проверить, что модалка осталась открытой"):
            assert self.page.is_form_modal_visible()