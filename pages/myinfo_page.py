

from selenium.webdriver.common.by import By

class MyInfoPage:
    MY_INFO_MENU = (By.XPATH, "//span[text()='My Info']")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']") 
    VALIDATION_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")
    LOADER = (By.CSS_SELECTOR, ".oxd-loading-spinner")

    