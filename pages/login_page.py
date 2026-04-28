from selenium import webdriver
from selenium.webdriver.common.by import By 

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME,"password") 
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]") 
    VALIDATION_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")                 



    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME  = (By.NAME,"lastName") 
    EMPLOYEE_ID = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")



