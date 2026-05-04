from behave import given, when, then
from pages.employee_page import EmployeePage 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from test_data import EMPLOYEE_FIRST_NAME, EMPLOYEE_LAST_NAME
import  time
from selenium.webdriver.common.by import By

from utils.logger import get_logger
logger = get_logger("employee_steps")  # change name per file

@given("user is on the add employee page")
def step_navigate_to_add_employee(context):
    logger.info("Navigating to add employee page")
    driver = context.driver
    wait = WebDriverWait (driver, 10) 
    wait.until(EC.presence_of_element_located(EmployeePage.PIM_MENU)).click() 
    wait.until(EC.presence_of_element_located(EmployeePage.ADD_EMPLOYEE_LINK)).click() 

# @when ("user enters valid firstname and lastname") 
# def step_enter_employee_details(context):
#     logger.info("Entering employee details")
#     driver = context.driver
#     wait = WebDriverWait(driver, 10) 
#     wait.until(EC.presence_of_element_located(EmployeePage.FIRST_NAME)).send_keys(EMPLOYEE_FIRST_NAME)
#     driver.find_element(*EmployeePage.LAST_NAME).send_keys(EMPLOYEE_LAST_NAME)                                                                              

@when ("user enters valid firstname and lastname") 
def step_enter_employee_details(context):
    logger.info("Entering employee details")
    driver = context.driver
    wait = WebDriverWait(driver, 10) 
    
    # 1. Enter First and Last Name
    wait.until(EC.presence_of_element_located(EmployeePage.FIRST_NAME)).send_keys(EMPLOYEE_FIRST_NAME)
    driver.find_element(*EmployeePage.LAST_NAME).send_keys(EMPLOYEE_LAST_NAME)
    # 2. Wait EXPLICITLY for the ID field to appear before trying to clear it
    # This prevents the NoSuchElementException
    id_field = wait.until(EC.presence_of_element_located(EmployeePage.EMPLOYEE_ID))

    #GENERATE DYNAMIC ID
    # This grabs the exact current second in time (e.g., "1714838291")
    unique_id = str(int(time.time()))
    logger.info(f"Injecting dynamic Employee ID: {unique_id}")
    
    # 3. Clear the pre-filled ID and type our unique one
    id_field = driver.find_element(*EmployeePage.EMPLOYEE_ID)
    
    # OrangeHRM pre-fills this, so we MUST clear it first or it will append to the existing ID
    #.clear() is flaky on React sites. Sending a blank space helps clear the DOM state.
    from selenium.webdriver.common.keys import Keys
    id_field.send_keys(Keys.COMMAND + "a") # Select all text (Mac shortcut)
    id_field.send_keys(Keys.BACKSPACE)     # Delete it
    
    # Now send the guaranteed unique ID
    id_field.send_keys(unique_id)


@when("user saves the details")
def step_save_employee(context):
    logger.info("Saving employee record")
    context.driver.find_element(*EmployeePage.SAVE_BUTTON).click()

# @then("user should see personal details saved message")
# def step_verify_employee_saved(context):
#     wait = WebDriverWait(context.driver, 10) 
#     wait.until(lambda driver: "viewPersonalDetails" in driver.current_url)
#     assert "viewPersonalDetails" in context.driver.current_url

@then('user should see personal details saved message')
def step_verify_employee_saved(context):
    wait = WebDriverWait(context.driver, 10)
    
    # We add a custom message to the until() method
    wait.until(
        lambda driver: "viewPersonalDetails" in driver.current_url,
        message=f"Timed out waiting for URL to contain 'viewPersonalDetails'. Current URL is: {context.driver.current_url}"
    )


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

# @when("user submits the form without firstname and lastname")
# def step_submit_without_both(context):
#     driver = context.driver
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.presence_of_element_located(EmployeePage.SAVE_BUTTON)).click()

@when("user submits the form without firstname and lastname")
def step_submit_without_both(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    
    # THE FIX: Wait for the loading spinner to disappear completely
    # This ensures no invisible overlay is blocking our click
    wait.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".oxd-form-loader"))
    )
    # Now that the "glass" is gone, we can click the button
    wait.until(EC.element_to_be_clickable(EmployeePage.SAVE_BUTTON)).click()

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
