import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure
import time


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("permissions.default.image", 2)
        options.page_load_strategy = 'eager'
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser

    browser.quit()


@pytest.fixture(autouse=True)
def clean_browser_state(driver):
    """Очищает cookies и переходит на пустую страницу между тестами"""
    yield
    try:
        driver.delete_all_cookies()
        driver.get("about:blank")
    except Exception:
        pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            try:
                time.sleep(1)
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name=f"failure_screenshot_{report.nodeid}",
                    attachment_type=allure.attachment_type.PNG
                )
                page_source = driver.page_source
                allure.attach(
                    page_source,
                    name="page_source_on_failure",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception:
                pass