# AClass Object

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import requests

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

firstName = "John"

# Functions
# Safe Clicker Work Modes-> 0: Safe Click, 1:Click, 2:Wait
def safe_clicker(pth, work_mode=0, wt=60, writer=""):
    if work_mode != 1:
        WebDriverWait(driver, wt).until(expected_conditions.visibility_of_element_located((By.XPATH, pth)))
    if work_mode != 2:
        driver.find_element(By.XPATH, pth).click()
    if writer != '':
        driver.find_element(By.XPATH, pth).send_keys(writer)
def page_scroller(y=500, x=0):
    driver.execute_script(f"window.scrollBy({x},{y})", "")

  myToken = requests.post(url='URL', data=tokenReq)
  
  return myToken.json()['access_token']

class pageOne():
    def system_login(userMail=''):
        driver.get("URL")
        driver.maximize_window()

        safe_clicker("//*[text()='Sign In']")
        # ...

class pageTwo():

    def system_logout(uiName=''):
        #....
        safe_clicker("//*[text()=' Sign Out ']")

    def system_mobile(uiName=''):
        safe_clicker("(//*[@class='...")
 
        load_waiter()

    def system_my_profile(uiName=''):
        safe_clicker("//*[contains(@class,'text-white text-lg')]")
        safe_clicker("//*[text()='My Profile']")
        load_waiter()
        safe_clicker("(//*[text()=' Home '])[1]")

    def system_my_services(uiName=''):
        safe_clicker("//*[contains(@class,'text-white text-lg')]")
        safe_clicker("//*[text()='My Services']")
