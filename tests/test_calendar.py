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

    @allure.story("Негативные")
    @allure.title("Ввод некорректного формата данных")
    def test_enter_invalid_type(self):
        self.page.open_calendar()
        self.page.enter_date("not-a-date")
        self.page.click_submit_date()
        message = self.page.get_error_message()
        assert "Please enter" in message

    @allure.story("Негативные")
    @allure.title("Ввод некорректной даты")
    def test_enter_invalid_date(self):
        self.page.open_calendar()
        self.page.enter_date("2022-44-51")
        self.page.click_submit_date()
        message = self.page.get_error_message()
        assert "Please enter" in message

    @allure.story("Негативные")
    @allure.title("Отправка пустой формы календаря")
    def test_submit_empty_calendar(self):
        self.page.open_calendar()
        self.page.click_submit_date()
        assert not self.page.is_date_success_visible(timeout=3), \
            "Пустая форма не должна была отправиться успешно"

        assert self.page.is_date_field_present(timeout=3), \
            "Поле даты должно оставаться видимым"
