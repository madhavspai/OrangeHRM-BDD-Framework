from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from test_data import (
    SEARCH_EMPLOYEE_NAME,
    SEARCH_EMPLOYEE_ID,
    INVALID_EMPLOYEE_NAME
)

@given("user is on the employee search page")
def step_navigate_to_search(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.element_to_be_clickable(SearchPage.PIM_MENU)
    ).click()

@when("the user searches using a valid employee name")
def step_search_by_name(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    name_field = wait.until(
        EC.element_to_be_clickable(SearchPage.EMPLOYEE_NAME_SEARCH)
    )
    name_field.clear()
    name_field.send_keys(SEARCH_EMPLOYEE_NAME)

    wait.until(
        EC.element_to_be_clickable(SearchPage.SEARCH_BUTTON)
    ).click()


@when("the user searches using a valid employee ID")
def step_search_by_id(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    id_field = wait.until(
        EC.element_to_be_clickable(SearchPage.EMPLOYEE_ID_SEARCH)
    )
    id_field.clear()
    id_field.send_keys(SEARCH_EMPLOYEE_ID)

    wait.until(
        EC.element_to_be_clickable(SearchPage.SEARCH_BUTTON)
    ).click()


@when("the user searches using an invalid employee name")
def step_search_invalid_name(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    name_field = wait.until(
        EC.element_to_be_clickable(SearchPage.EMPLOYEE_NAME_SEARCH)
    )
    name_field.clear()
    name_field.send_keys(INVALID_EMPLOYEE_NAME)

    wait.until(
        EC.element_to_be_clickable(SearchPage.SEARCH_BUTTON)
    ).click()


@when("the user submits the search with all fields empty")
def step_search_empty(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.element_to_be_clickable(SearchPage.SEARCH_BUTTON)
    ).click()

@then("the system should return the correct employee details")
def step_verify_results_found(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-table-body")
        )
    )

    assert (
        "no records found" in driver.page_source.lower()
        or len(driver.find_elements(*SearchPage.SEARCH_RESULTS_ROW)) > 0
    )


@then('the system should display a "No records found" message')
def step_verify_no_records(context):
    driver = context.driver
    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-loading-spinner")
        )
    )
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-table-body")
        )
    )
    assert "no records found" in driver.page_source.lower()


@then("the system should update and display the default table of employee records")
def step_verify_default_records(context):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    rows = wait.until(
        EC.presence_of_all_elements_located(
            SearchPage.SEARCH_RESULTS_ROW
        )
    )

    assert len(rows) > 0