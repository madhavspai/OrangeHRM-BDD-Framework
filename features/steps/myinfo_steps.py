from behave import given, when, then
from pages.myinfo_page import MyInfoPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_data import EMPLOYEE_FIRST_NAME, EMPLOYEE_LAST_NAME


def force_clear(driver, element, timeout=10):
    """
    Robust clear helper for OrangeHRM (Vue.js + loader-safe).
    Handles:
    - Form loader overlay (.oxd-form-loader)
    - Vue reactivity issues
    - Click interception problems
    """

    wait = WebDriverWait(driver, timeout)

    # 1. Wait until OrangeHRM form loader disappears
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-form-loader")
        )
    )

    # 2. Wait until the element is actually clickable
    element = wait.until(EC.element_to_be_clickable(element))

    # 3. Vue-safe clear sequence
    element.click()
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACKSPACE)

    # Extra safety for Vue state sync
    element.send_keys(" ")
    element.send_keys(Keys.BACKSPACE)


@given("user is on the personal details page")
def step_navigate_to_myinfo(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.element_to_be_clickable(MyInfoPage.MY_INFO_MENU)
    ).click()


@when("user updates valid firstname and lastname")
def step_update_valid_names(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.FIRST_NAME)
    )
    force_clear(driver, first_name)
    first_name.send_keys(EMPLOYEE_FIRST_NAME)

    last_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.LAST_NAME)
    )
    force_clear(driver, last_name)
    last_name.send_keys(EMPLOYEE_LAST_NAME)


@when("user updates firstname only")
def step_update_firstname_only(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.FIRST_NAME)
    )
    force_clear(driver, first_name)
    first_name.send_keys(EMPLOYEE_FIRST_NAME)

    last_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.LAST_NAME)
    )
    force_clear(driver, last_name)


@when("user updates lastname only")
def step_update_lastname_only(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.FIRST_NAME)
    )
    force_clear(driver, first_name)

    last_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.LAST_NAME)
    )
    force_clear(driver, last_name)
    last_name.send_keys(EMPLOYEE_LAST_NAME)


@when("user submits personal details form without firstname and lastname")
def step_submit_myinfo_without_both(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.FIRST_NAME)
    )
    force_clear(driver, first_name)

    last_name = wait.until(
        EC.presence_of_element_located(MyInfoPage.LAST_NAME)
    )
    force_clear(driver, last_name)

    save_btn = wait.until(
        EC.element_to_be_clickable(MyInfoPage.SAVE_BUTTON)
    )
    save_btn.click()


@when("user saves personal details")
def step_save_details(context):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    save_btn = wait.until(
        EC.element_to_be_clickable(MyInfoPage.SAVE_BUTTON)
    )
    save_btn.click()


@then("user should see error message as required lastname")
def step_verify_lastname_error(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(
        EC.presence_of_element_located(MyInfoPage.VALIDATION_MESSAGE)
    )
    assert error.is_displayed()


@then("user should see error message as required firstname")
def step_verify_firstname_error(context):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(
        EC.presence_of_element_located(MyInfoPage.VALIDATION_MESSAGE)
    )
    assert error.is_displayed()


@then('user should see myinfo first name last name "required" message')
def step_verify_both_errors(context):
    wait = WebDriverWait(context.driver, 10)
    errors = wait.until(
        EC.presence_of_all_elements_located(MyInfoPage.VALIDATION_MESSAGE)
    )
    assert len(errors) > 0