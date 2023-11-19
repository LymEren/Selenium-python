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

def load_waiter():
    pth = "//*[text()='Loading...']"
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, pth)))
    WebDriverWait(driver, 30).until_not(expected_conditions.visibility_of_element_located((By.XPATH, pth)))

def page_scroller(y=500, x=0):
    driver.execute_script(f"window.scrollBy({x},{y})", "")

# 3- Registering with the API
def api_register():
    url = 'API URL'
    myReq = {'Your API request'}
    logReq = requests.post(url, json=myReq)
    sampleOne = logReq.json()["Related Column"]
    print(f"Sample One: {sampleOne}\n")

# 4- Automate a process using Selenium
def selenium_ui():
    driver.get("Your URL")
    driver.maximize_window()

    # Login Page
    safe_clicker("//*[text()='Login']")
    # ...
    # ...

    load_waiter()
    page_scroller()
    sample_id = driver.find_element(By.XPATH, "Example").text
    print(f'Sample ID: {sample_id}')
    return sample_id

# 5- DB order Query
def db_complete():

    connectDbTest = psycopg2.connect(host="", database="", port="",
                                     user="", password="")

    sampleCursor = connectDbTest.cursor()
    sampleCursor.execute(f'Query')
    sampleResult = sampleCursor.fetchall()

    # ... Information about the related API

    api_complete = "Other API"
    headers = {
        'Authorization': f'{myToken}',
        'LocalToken': '1',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url=api_complete, headers=headers, data=None)

# 6- Calling Functions

# Register User
api_register()
input('Press any key after verify email...')

# Sample Submit
sample_id = selenium_ui()

# Db Result
db_complete()

# After this section, information can be controlled.

# if sampleResult == True
#    print("\nSample Process Validated!")
