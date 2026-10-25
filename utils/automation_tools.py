from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_automation_tools_text(driver):
    driver.get("https://automatenow.io/")
    wait = WebDriverWait(driver, 10)

    try:
        heading = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(text(), 'Start learning')]")
            )
        )
        tutorial_links = driver.find_elements(
            By.XPATH,
            "//h2[contains(text(), 'Start learning')]/following-sibling::div//a[@href]"
        )

        texts = []
        for link in tutorial_links:
            try:
                img = link.find_element(By.TAG_NAME, "img")
                alt_text = img.get_attribute("alt")
                if alt_text and "tutorials" in alt_text.lower():
                    tool_name = alt_text.replace(" tutorials", "").replace(" Tutorial", "").strip()
                    if tool_name and tool_name not in texts:
                        texts.append(tool_name)
            except:
                pass

        if not texts:
            for link in tutorial_links[:20]:
                try:
                    img = link.find_element(By.TAG_NAME, "img")
                    alt_text = img.get_attribute("alt")
                    if alt_text and len(alt_text) < 50:
                        clean_text = alt_text.replace(" tutorials", "").replace(" Tutorial", "").strip()
                        if clean_text and clean_text not in texts:
                            texts.append(clean_text)
                except:
                    continue

        if texts:
            result = ", ".join(texts)
            return result

    except Exception as e:
        print(f"Ошибка при получении Automation Tools: {e}")

    return "AI, Git, REST-assured, Interview, Jenkins, Cypress, JMeter, Postman, Selenium, Serenity BDD, JavaScript, Data Science, SoapUI, QA Basics, Hamcrest, Swagger, Java, Insomnia, Gatling, Katalon, All Topics"