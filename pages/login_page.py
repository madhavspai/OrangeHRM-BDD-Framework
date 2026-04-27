from selenium.webdriver.common.by import By 

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME,"password") 
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]") 
    VALIDATION_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")                 


