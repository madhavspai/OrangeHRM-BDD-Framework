from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # <-- Added Import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import get_logger

logger = get_logger("environment")

BASE_URL = "https://opensource-demo.orangehrmlive.com"


def before_scenario(context, scenario):
    logger.info(f"Starting scenario: {scenario.name}")

    #Fresh browser start
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # ------------------------------

    #Fresh browser per scenario (prevents SPA state leakage)
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options  # <-- Added options parameter
    )
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

    #Always start from a clean session
    context.driver.delete_all_cookies()
    context.driver.get(BASE_URL)

    #Login ONLY if scenario is not a login scenario
    if "login" not in scenario.feature.name.lower():
        from pages.login_page import LoginPage
        from test_data import VALID_USERNAME, VALID_PASSWORD

        driver = context.driver
        wait = WebDriverWait(driver, 15)

        logger.info("Performing precondition login")

        wait.until(
            EC.element_to_be_clickable(LoginPage.USERNAME)
        ).clear()
        driver.find_element(*LoginPage.USERNAME).send_keys(VALID_USERNAME)

        driver.find_element(*LoginPage.PASSWORD).clear()
        driver.find_element(*LoginPage.PASSWORD).send_keys(VALID_PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON).click()

        #SPA‑safe login verification (NOT URL based)
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".oxd-userdropdown")
            )
        )


def after_scenario(context, scenario):
    logger.info(
        f"Completed scenario: {scenario.name} - Status: {scenario.status}"
    )

    #Screenshot only on failure
    if scenario.status == "failed":
        screenshot_path = f"logs/{scenario.name.replace(' ', '_')}.png"
        context.driver.save_screenshot(screenshot_path)
        logger.error(f"Screenshot saved: {screenshot_path}")

    context.driver.quit()