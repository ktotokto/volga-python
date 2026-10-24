import pytest
import allure
from pages.calendar_page import CalendarPage


@allure.feature("Календарь")
class TestCalendar:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = CalendarPage(driver)

    @allure.story("Позитивные")
    @allure.title("Ввод корректной даты")
    def test_enter_valid_date(self):
        self.page.open_calendar()
        self.page.enter_date("2025-07-15")
        self.page.click_submit_date()
        message = self.page.get_success_message()
        assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Заполнение формы полностью")
    def test_fill_full_form(self):
        self.page.open_calendar()
        self.page.enter_date("2025-01-01")
        self.page.fill_name("Иван Иванов")
        self.page.fill_email("ivan@test.com")
        self.page.fill_message("Тестовое сообщение")
        self.page.click_submit_form()
        message = self.page.get_success_message()
        assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Ввод даты в прошлом")
    def test_enter_past_date(self):
        self.page.open_calendar()
        self.page.enter_date("2020-01-01")
        self.page.click_submit_date()
        message = self.page.get_success_message()
        assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Ввод даты в будущем")
    def test_enter_future_date(self):
        self.page.open_calendar()
        self.page.enter_date("2030-12-31")
        self.page.click_submit_date()
        message = self.page.get_success_message()
        assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Заполнение только имени и email")
    def test_fill_name_and_email_only(self):
        self.page.open_calendar()
        self.page.fill_name("Пётр")
        self.page.fill_email("petr@test.com")
        self.page.click_submit_form()
        message = self.page.get_success_message()
        assert "Thank you" in message


    @allure.story("Негативные")
    @allure.title("Ввод некорректной даты")
    def test_enter_invalid_date(self):
        self.page.open_calendar()
        self.page.enter_date("not-a-date")
        self.page.click_submit_date()
        # Форма не должна отправиться успешно
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "[id*='contact-form-success'] h4"), timeout=3
        )

    @allure.story("Негативные")
    @allure.title("Отправка пустой формы")
    def test_submit_empty_form(self):
        self.page.open_calendar()
        self.page.click_submit_form()
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "[id*='contact-form-success'] h4"), timeout=3
        )

    @allure.story("Негативные")
    @allure.title("Ввод некорректного email")
    def test_enter_invalid_email(self):
        self.page.open_calendar()
        self.page.fill_name("Тест")
        self.page.fill_email("не-email")
        self.page.click_submit_form()
        assert not self.page.is_element_present(
            (By.CSS_SELECTOR, "[id*='contact-form-success'] h4"), timeout=3
        )


from selenium.webdriver.common.by import By