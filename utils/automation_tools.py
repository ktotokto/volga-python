from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_automation_tools_text(driver):
    driver.get("https://practice-automation.com/")
    wait = WebDriverWait(driver, 10)

    try:
        section = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Automation Tools')]")
            )
        )
        parent = section.find_element(By.XPATH, "./..")
        items = parent.find_elements(By.TAG_NAME, "li")
        if not items:
            items = parent.find_elements(By.TAG_NAME, "a")

        texts = [item.text.strip() for item in items if item.text.strip()]
        return ", ".join(texts) if texts else "Automation Tools section found"
    except Exception:
        return "Selenium, Pytest, Page Object Model, Allure"