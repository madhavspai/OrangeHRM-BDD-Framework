from selenium.webdriver.common.by import By

class EmployeePage:
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMPLOYEE_ID = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_EMPLOYEE_LINK = (By.LINK_TEXT, "Add Employee")
    