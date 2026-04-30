from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window() 
    context.driver.get("https://opensource-demo.orangehrmlive.com")

def after_scenario(context, scenario):
        if scenario.status == "failed":  
              context.driver.save_screenshot(f"logs/{scenario.name}.png")  #this is screenshot
        context.driver.quit() 

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://opensource-demo.orangehrmlive.com") 
    
       
    # Auto login only for non-login features
    if "Login" not in scenario.feature.name:
        from pages.login_page import LoginPage
        from test_data import VALID_USERNAME, VALID_PASSWORD
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.presence_of_element_located(LoginPage.USERNAME)).send_keys(VALID_USERNAME)
        context.driver.find_element(*LoginPage.PASSWORD).send_keys(VALID_PASSWORD)
        context.driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        wait.until(lambda driver: "dashboard" in driver.current_url.lower())



