from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
import logging


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window() 
    context.driver.get("https://opensource-demo.orangehrmlive.com")

def after_scenario(context, scenario):
        if scenario.status == "failed":  #this is assertion
              context.driver.save_screenshot(f"logs/{scenario.name}.png")  #this is screenshot
        context.driver.quit() 








