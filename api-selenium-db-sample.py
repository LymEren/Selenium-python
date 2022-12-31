# This program contains an API, selenium, database usage example.

# 1- Obtaining tokens for authorization
# 2- Functions
# 3- Registering with the API
# 4- Automate a process using Selenium
# 5- DB order Query
# 6- Calling Functions

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import psycopg2
import requests

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# 1- Obtaining tokens for authorization
def get_token():
  tokenReq = {
      'username': '',
      'password': '',
      'grant_type': '',
      'client_id': ''
  }
  myToken = requests.post(
      url='Token URL',
      data=tokenReq
  )
  return myToken.json()['Token Column']

myToken = get_token()
userMail = "Ernn@sample.com"
firstName = "Eyyub"
uiPass = '123456'
bearer = f'Bearer {myToken}'

# 2- Functions
# Safe Clicker Work Modes-> 0: Safe Click, 1:Click, 2:Wait
def safe_clicker(pth, work_mode=0, wt=15, writer=""):
    if work_mode != 1:
        WebDriverWait(driver, wt).until(expected_conditions.visibility_of_element_located((By.XPATH, pth)))
    if work_mode != 2:
        driver.find_element(By.XPATH, pth).click()
    if writer != '':
        driver.find_element(By.XPATH, pth).send_keys(writer)
