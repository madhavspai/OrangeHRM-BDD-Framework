
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
    wait.until(EC.presence_of_element_located(LoginPage.USERNAME)).send_keys("Admin") 
    driver.find_element(*LoginPage.PASSWORD).send_keys("admin123") 
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
    wait.until(EC.presence_of_element_located(LoginPage.USERNAME)).send_keys("Admin")
    driver.find_element(*LoginPage.PASSWORD).send_keys("wrong password")
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
@Then("user must see error message on login page")
def step_verify_error_message(context):
    wait = WebDriverWait (context.driver, 10)
    error = wait.until(EC.presence_of_element_located(LoginPage.ERROR_MESSAGE)) 
    assert error.is_displayed() 




