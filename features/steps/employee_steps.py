from behave import given, when, then
from pages.employee_page import EmployeePage 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from test_data import EMPLOYEE_FIRST_NAME, EMPLOYEE_LAST_NAME


@given("user is on the add employee page")
def step_navigate_to_add_employee(context):
    driver = context.driver
    wait = WebDriverWait (driver, 10) 
    wait.until(EC.presence_of_element_located(EmployeePage.PIM_MENU)).click() 
    wait.until(EC.presence_of_element_located(EmployeePage.ADD_EMPLOYEE_LINK)).click() 

@when ("user enters valid firstname and lastname") 
def step_enter_employee_details(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10) 
    wait.until(EC.presence_of_element_located(EmployeePage.FIRST_NAME)).send_keys(EMPLOYEE_FIRST_NAME)
    driver.find_element(*EmployeePage.LAST_NAME).send_keys(EMPLOYEE_LAST_NAME)                                                                              

@when("user saves the details")
def step_save_employee(context):
    context.driver.find_element(*EmployeePage.SAVE_BUTTON).click()

@then("user should see successfully saved message")
def step_verify_employee_saved(context):
    wait = WebDriverWait(context.driver, 10) 
    wait.until(lambda driver: "viewPersonalDetails" in driver.current_url)
    assert "viewPersonalDetails" in context.driver.current_url


@when("user submits the form without last name")
def step_submit_without_lastname(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(EmployeePage.FIRST_NAME)).send_keys(EMPLOYEE_FIRST_NAME)
    driver.find_element(*EmployeePage.SAVE_BUTTON).click()

@when("user submits the form without first name")
def step_submit_without_firstname(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(EmployeePage.LAST_NAME)).send_keys(EMPLOYEE_LAST_NAME)
    driver.find_element(*EmployeePage.SAVE_BUTTON).click()

@when("user submits the form without firstname and lastname")
def step_submit_without_both(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(EmployeePage.SAVE_BUTTON)).click()

@then("user should see last name \"required\" message")
def step_verify_lastname_required(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(EmployeePage.VALIDATION_MESSAGE))
    assert error.is_displayed()

@then("user should see first name \"required\" message")
def step_verify_firstname_required(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(EmployeePage.VALIDATION_MESSAGE))
    assert error.is_displayed()

@then("user should see first name last name \"required\" message")
def step_verify_both_required(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(EmployeePage.VALIDATION_MESSAGE))
    assert error.is_displayed()
