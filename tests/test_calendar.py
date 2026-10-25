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
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести корректную дату 2025-09-21"):
            self.page.enter_date("2025-09-21")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об успехе"):
            message = self.page.get_success_message()
            assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Ввод даты в прошлом")
    def test_enter_past_date(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести дату в прошлом 2018-02-12"):
            self.page.enter_date("2018-02-12")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об успехе"):
            message = self.page.get_success_message()
            assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Ввод даты в будущем")
    def test_enter_future_date(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести дату в будущем 2029-10-11"):
            self.page.enter_date("2029-10-11")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об успехе"):
            message = self.page.get_success_message()
            assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Ввод даты високосного года")
    def test_enter_leap_year_date(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести корректную дату високосного года 2024-02-29"):
            self.page.enter_date("2024-02-29")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об успехе"):
            message = self.page.get_success_message()
            assert "Thank you" in message

    @allure.story("Позитивные")
    @allure.title("Ввод даты на границе года")
    def test_enter_end_of_year_date(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести дату на границе года 2021-12-31"):
            self.page.enter_date("2021-12-31")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об успехе"):
            message = self.page.get_success_message()
            assert "Thank you" in message

    @allure.story("Негативные")
    @allure.title("Отправка пустой формы календаря")
    def test_submit_empty_calendar(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Нажать кнопку Submit без ввода даты"):
            self.page.click_submit_date()
        with allure.step("Проверить, что сообщение об успехе НЕ появилось"):
            assert not self.page.is_date_success_visible(timeout=3)
        with allure.step("Проверить, что поле даты всё ещё на месте"):
            assert self.page.is_date_field_present(timeout=3)

    @allure.story("Негативные")
    @allure.title("Ввод некорректного формата данных")
    def test_enter_invalid_type(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести некорректный текст not-a-date"):
            self.page.enter_date("not-a-date")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об ошибке"):
            message = self.page.get_error_message()
            assert "Please enter" in message

    @allure.story("Негативные")
    @allure.title("Ввод некорректной даты")
    def test_enter_invalid_date(self):
        with allure.step("Открыть страницу календаря"):
            self.page.open_calendar()
        with allure.step("Ввести несуществующую дату 2042-44-51"):
            self.page.enter_date("2042-44-51")
        with allure.step("Нажать кнопку Submit"):
            self.page.click_submit_date()
        with allure.step("Проверить появление сообщения об ошибке"):
            message = self.page.get_error_message()
            assert "Please enter" in message
