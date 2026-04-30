from selenium.webdriver.common.by import By

class SearchPage:
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    EMPLOYEE_NAME_SEARCH = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    EMPLOYEE_ID_SEARCH = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    NO_RECORDS_MESSAGE = (By.XPATH, "//span[text()='No Records Found']")
    RECORDS_FOUND = (By.XPATH, "//span[contains(text(),'Records Found')]")
    SEARCH_RESULTS_ROW = (By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")
    