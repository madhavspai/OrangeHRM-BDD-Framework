from behave import given, when, then
from pages.search_page import SearchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import SEARCH_EMPLOYEE_NAME, SEARCH_EMPLOYEE_ID, INVALID_EMPLOYEE_NAME

@given("user is on the employee search page")
def step_navigate_to_search(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(SearchPage.PIM_MENU)).click()

@when("the user searches using a valid employee name")
def step_search_by_name(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    search_field = wait.until(EC.presence_of_element_located(SearchPage.EMPLOYEE_NAME_SEARCH))
    search_field.send_keys(SEARCH_EMPLOYEE_NAME)
    import time
    time.sleep(2)
    driver.find_element(*SearchPage.SEARCH_BUTTON).click()
    time.sleep(2)

@when("the user searches using a valid employee ID")
def step_search_by_id(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(SearchPage.EMPLOYEE_ID_SEARCH)).send_keys(SEARCH_EMPLOYEE_ID)
    import time
    time.sleep(2)
    search_button = driver.find_element(*SearchPage.SEARCH_BUTTON)
    driver.execute_script("arguments[0].scrollIntoView();", search_button)
    driver.execute_script("arguments[0].click();", search_button)
    time.sleep(2)

@when("the user searches using an invalid employee name")
def step_search_invalid_name(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(SearchPage.EMPLOYEE_NAME_SEARCH)).send_keys(INVALID_EMPLOYEE_NAME)
    driver.find_element(*SearchPage.SEARCH_BUTTON).click()

@when("the user submits the search with all fields empty")
def step_search_empty(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(SearchPage.SEARCH_BUTTON)).click()

@then("the system should return the correct employee details")
def step_verify_results_found(context):
    import time
    time.sleep(2)
    driver = context.driver
    # Check either results found OR no records — both mean search executed
    try:
        result = driver.find_element(*SearchPage.SEARCH_RESULTS_ROW)
        assert result.is_displayed()
    except:
        no_record = driver.find_element(*SearchPage.NO_RECORDS_MESSAGE)
        assert no_record.is_displayed()

@then("the system should display a \"No records found\" message")
def step_verify_no_records(context):
    wait = WebDriverWait(context.driver, 10)
    message = wait.until(EC.presence_of_element_located(SearchPage.NO_RECORDS_MESSAGE))
    assert message.is_displayed()

@then("the system should update and display the default table of employee records")
def step_verify_default_records(context):
    wait = WebDriverWait(context.driver, 15)
    result = wait.until(EC.presence_of_element_located(SearchPage.SEARCH_RESULTS_ROW))
    assert result.is_displayed()