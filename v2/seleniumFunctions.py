from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

    
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

class seleniumFunctions:
    
    
    # def browseSauceDemo():
    #     driver.get('https://www.saucedemo.com/')
    #     driver.maximize_window()

    def browseOrangeHrmLive():
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        driver.maximize_window()
        driver.getDev


    def safe_clicker(path, work_mode=1, wt=60, writer=""):
        """
        This function allows you to perform the click operation more safely.
        
        :path: xPath for related element
        :work_mode: 
            1: Wait related element
            2: Click related element
        :wt: Wait time before the break
        :writer: Contains the text that needs to be written. Writer will be work if writer input is not empty.
        """

        if work_mode != 1:
            WebDriverWait(driver, wt).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
        if work_mode != 2:
            WebDriverWait(driver, wt).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
            driver.find_element(By.XPATH, path).click()
        if writer != '':
            driver.find_element(By.XPATH, path).send_keys(writer)

    def page_scroller(y=500, x=0):
        driver.execute_script(f"window.scrollBy({x},{y})", "")