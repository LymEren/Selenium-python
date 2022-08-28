### Eyyub Eren - Workshop
#
# Test Case 1: Hatali girislerde sistem uyari vermelidir (4 farkli test icerir) - Parametrize ve Dictionary kullanildi 
#       1- Kullanici adi ve sifre girdi alanlari bos oldugu durum 
#       2- Kullanici adi girdi alani bos oldugu durum
#       3- Sifre alani bos oldugu durum
#       4- Kullanici adi ve sifre girdi alanlari dogru ancak bu bilgide kullanicinin olmadigi durum
# 
# 


from unittest import expectedFailure
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Test Case 1 - Hatali Giris (Parametrize)

class Test_firstTest:
#This class includes login tests

    expected_login_errors = {
        "Both Blank"     : ["Epic sadface: Username is required"],
        "Username Blank" : ["Epic sadface: Username is required"],
        "Password Blank" : ["Epic sadface: Password is required"],
        "Wrong User"     : ["Epic sadface: Username and password do not match any user in this service"]
        
    }


    @pytest.mark.parametrize("username,password,result",[("","","Username Blank"),("","123","Username Blank"),("user","","Password Blank"),("user","123","Wrong User")])
    def test_wrong_logins(self,username,password,result):
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        
        
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))

        email_log = self.driver.find_element(By.ID,"user-name")
        email_log.send_keys(username)
        
        password_log = self.driver.find_element(By.ID,"password")
        password_log.send_keys(password)

        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()

        # sleep() yerine WebDriverWait kullanildi 
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=\"error\"]")))
        errorMessage = self.driver.find_element(By.CSS_SELECTOR,"[data-test=\"error\"]")
        

        # Extra: Strip may use
        self.expected_login_errors[result] = errorMessage

        sleep(1)

        self.driver.quit()

