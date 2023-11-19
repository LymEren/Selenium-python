# Selenium with Safe Clicker function
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_WscFive:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_login_wsc(self):
        self.driver.get("https://www.selenium.dev/documentation/")

        # I define this function for safe click. Can be improved with a try except loop.
        # 0: Safe Click, 1:Click, 2:Wait, 3:Write
        def safe_clicker(pth, work_mode=0, wt=15, m_input=""):
            if work_mode != 1:
                WebDriverWait(self.driver, wt).until(expected_conditions.visibility_of_element_located((By.XPATH, pth)))
            if work_mode != 2:
                self.driver.find_element(By.XPATH, pth).click()
            if work_mode == 3:
                self.driver.find_element(By.XPATH, pth).send_keys(m_input)

        # 1- Home Page
        safe_clicker("//*[text()='Overview']")
        safe_clicker("//*[text()='Components']")

        # 2- About Dropdown Menu
        # Only WaitDriver Wait Mode
        safe_clicker("//*[contains(@class,'dropdown-toggle') and (text()='About')]", 2, 15)
        # Only Click Mode
        safe_clicker("//*[contains(@class,'dropdown-toggle') and (text()='About')]", 1)
        safe_clicker("//*[@href='/getinvolved']")



