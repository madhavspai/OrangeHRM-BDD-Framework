from behave import given, when, then 
from pages.myinfo_page import MyInfoPage 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from test_data import EMPLOYEE_FIRST_NAME, EMPLOYEE_LAST_NAME 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def force_clear(element):
    """
    Custom helper to bypass Vue.js state issues and Mac ChromeDriver modifier key bugs.
    """
    # 1. Standard clear to empty the DOM
    element.clear()
    # 2. Click and add a space to wake up the Vue.js event listener
    element.click()
    element.send_keys(" ")
    # 3. Brute-force backspace to guarantee the field and state are empty
    for _ in range(20):
        element.send_keys(Keys.BACKSPACE)

@given("user is on the personal details page") 
def step_navigate_to_myinfo(context): 
    driver = context.driver 
    wait = WebDriverWait(driver, 10) 
    wait.until(EC.presence_of_element_located(MyInfoPage.MY_INFO_MENU)).click() 

@when("user updates valid firstname and lastname")
def step_update_valid_names(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    
    first_name = wait.until(EC.presence_of_element_located(MyInfoPage.FIRST_NAME))
    force_clear(first_name)
    first_name.send_keys(EMPLOYEE_FIRST_NAME)
    
    last_name = driver.find_element(*MyInfoPage.LAST_NAME)
    force_clear(last_name)
    last_name.send_keys(EMPLOYEE_LAST_NAME)

@when("user updates firstname only")
def step_update_firstname_only(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    
    first_name = wait.until(EC.presence_of_element_located(MyInfoPage.FIRST_NAME))
    force_clear(first_name)
    first_name.send_keys(EMPLOYEE_FIRST_NAME)
    
    last_name = driver.find_element(*MyInfoPage.LAST_NAME)
    force_clear(last_name)

@when("user updates lastname only")
def step_update_lastname_only(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    
    first_name = wait.until(EC.presence_of_element_located(MyInfoPage.FIRST_NAME))
    force_clear(first_name)
    
    last_name = driver.find_element(*MyInfoPage.LAST_NAME)
    force_clear(last_name)
    last_name.send_keys(EMPLOYEE_LAST_NAME)

@when("user submits personal details form without firstname and lastname")
def step_submit_myinfo_without_both(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    
    first_name = wait.until(EC.presence_of_element_located(MyInfoPage.FIRST_NAME))
    force_clear(first_name)
    
    last_name = driver.find_element(*MyInfoPage.LAST_NAME)
    force_clear(last_name)
    
    save_btn = wait.until(EC.element_to_be_clickable(MyInfoPage.SAVE_BUTTON))
    save_btn.click()

@when("user saves personal details")
def step_save_details(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    save_btn = wait.until(EC.element_to_be_clickable(MyInfoPage.SAVE_BUTTON))
    save_btn.click()

@then("user should see error message as required lastname")
def step_verify_lastname_error(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(MyInfoPage.VALIDATION_MESSAGE))
    assert error.is_displayed()

@then("user should see error message as required firstname")
def step_verify_firstname_error(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(EC.presence_of_element_located(MyInfoPage.VALIDATION_MESSAGE))
    assert error.is_displayed()

@then('user should see myinfo first name last name "required" message')
def step_verify_both_errors(context):
    wait = WebDriverWait(context.driver, 10)
    errors = wait.until(EC.presence_of_all_elements_located(MyInfoPage.VALIDATION_MESSAGE))
    assert len(errors) > 0

    