from behave import Given, When, Then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD
)
from utils.logger import get_logger
logger = get_logger("login_steps")



@Given("user is on the login page")
def step_open_login_page(context):
    logger.info("Navigating to login page")
    context.login_page = LoginPage()


@When("user enters valid credentials")
def step_enter_valid_credentials(context):
    logger.info("Entering valid credentials")

    driver = context.driver
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(LoginPage.USERNAME)
    ).send_keys(VALID_USERNAME)

    driver.find_element(*LoginPage.PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()


@Then("user should be directed to homepage")
def step_verify_login_success(context):
    logger.info("Verifying successful login")

    driver = context.driver
    wait = WebDriverWait(driver, 15)

    #Wait for SPA to stabilize
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "header"))
    )

    # proof of login: user profile dropdown
    user_menu = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-userdropdown")
        )
    )

    assert user_menu.is_displayed()
    logger.info("Login successful")

@When("user enters invalid credentials")
def step_enter_invalid_credentials(context):
    logger.info("Entering invalid credentials")

    driver = context.driver
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(LoginPage.USERNAME)
    ).send_keys(INVALID_USERNAME)

    driver.find_element(*LoginPage.PASSWORD).send_keys(INVALID_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()


@Then("user must see error message on login page")
def step_verify_error_message(context):
    logger.info("Verifying login error message")

    wait = WebDriverWait(context.driver, 10)
    error = wait.until(
        EC.presence_of_element_located(LoginPage.ERROR_MESSAGE)
    )

    assert error.is_displayed()


@When("the user submits the login form with username empty and valid password")
def step_empty_username(context):
    logger.info("Submitting login with empty username")

    driver = context.driver
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(LoginPage.PASSWORD)
    ).send_keys(VALID_PASSWORD)

    driver.find_element(*LoginPage.LOGIN_BUTTON).click()


@When("the user submits the login form with valid username and password empty")
def step_empty_password(context):
    logger.info("Submitting login with empty password")

    driver = context.driver
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(LoginPage.USERNAME)
    ).send_keys(VALID_USERNAME)

    driver.find_element(*LoginPage.LOGIN_BUTTON).click()


@When("the user submits the login form with both username and password empty")
def step_empty_both(context):
    logger.info("Submitting login with empty username and password")

    driver = context.driver
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(LoginPage.LOGIN_BUTTON)
    )
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()


@Then('a validation message "Required" should be displayed for the username field')
def step_check_username_validation(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(
        EC.presence_of_element_located(LoginPage.VALIDATION_MESSAGE)
    )
    assert error.is_displayed()


@Then('a validation message "Required" should be displayed for the password field')
def step_check_password_validation(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(
        EC.presence_of_element_located(LoginPage.VALIDATION_MESSAGE)
    )
    assert error.is_displayed()


@Then("the user should not be logged in")
def step_user_not_logged_in(context):
    logger.info("Verifying user is not logged in")

    #Strong negative assertion: user menu must NOT exist
    elements = context.driver.find_elements(
        By.CSS_SELECTOR, ".oxd-userdropdown"
    )

    assert len(elements) == 0