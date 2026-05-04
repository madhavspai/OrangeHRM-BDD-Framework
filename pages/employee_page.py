from selenium.webdriver.common.by import By

class EmployeePage:
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMPLOYEE_ID = (By.XPATH,"//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_EMPLOYEE_LINK = (By.LINK_TEXT, "Add Employee")
    VALIDATION_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")
    