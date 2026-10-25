import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
import time


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.page_load_strategy = 'eager'

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser

    browser.quit()


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
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")