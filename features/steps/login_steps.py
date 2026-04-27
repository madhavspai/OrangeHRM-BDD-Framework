from test_data import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
from behave import Given, When , Then
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Positive Scenario
@Given("user is on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage()

@When("user enters valid credentials") 
def step_enter_valid_credentials(context):
    driver = context.driver
    wait = WebDriverWait (driver, 10) 
    wait.until(EC.presence_of_element_located(LoginPage.USERNAME)).send_keys(VALID_USERNAME) 
    driver.find_element(*LoginPage.PASSWORD).send_keys(VALID_PASSWORD) 
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()  

@Then("user should be directed to homepage")
def step_verify_login_success(context):
        wait = WebDriverWait(context.driver, 10)
        wait.until(lambda driver:"dashboard" in driver.current_url.lower())
        assert  "dashboard" in context.driver.current_url.lower() 


@When("user enters invalid credentials")
def step_verify_invalid_credentials(context):
    driver = context.driver
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located(LoginPage.USERNAME)).send_keys(INVALID_USERNAME)
    driver.find_element(*LoginPage.PASSWORD).send_keys(INVALID_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
@Then("user must see error message on login page")
def step_verify_error_message(context):
    wait = WebDriverWait (context.driver, 10)
    error = wait.until(EC.presence_of_element_located(LoginPage.ERROR_MESSAGE)) 
    assert error.is_displayed() 

@When("the user submits the login form with username empty and valid password")
def step_empty_username(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPage.PASSWORD)).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

@When("the user submits the login form with valid username and password empty")
def step_empty_password(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPage.USERNAME)).send_keys(VALID_USERNAME)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

@When("the user submits the login form with both username and password empty")
def step_empty_both(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

@Then('a validation message "Required" should be displayed for the username field')
def step_check_username_validation(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(LoginPage.VALIDATION_MESSAGE))
    assert error.is_displayed()

@Then('a validation message "Required" should be displayed for the password field')
def step_check_password_validation(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(LoginPage.VALIDATION_MESSAGE))
    assert error.is_displayed()

@Then("the user should not be logged in")
def step_user_not_logged_in(context):
    assert "dashboard" not in context.driver.current_url.lower()
