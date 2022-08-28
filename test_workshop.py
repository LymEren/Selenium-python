### Eyyub Eren - Workshop
#
# Test Case 1: Hatali girislerde sistem hata mesaji gostermelidir (4 farkli test icerir) - Parametrize ve Dictionary kullanildi 
#       1- Kullanici adi ve sifre girdi alanlari bos oldugu durum 
#       2- Kullanici adi girdi alani bos oldugu durum
#       3- Sifre alani bos oldugu durum
#       4- Kullanici adi ve sifre girdi alanlari dogru ancak bu bilgide kullanicinin olmadigi durum
# 
# Test Case 2: Urunler sepete eklenebilmelidir
#       On Kosullar: - Sisteme giris yapilmis olmalidir
#
# Test Case 3: Sistemden cikis yapildiginda sepete ulasilamamalidir
#       On Kosullar: - Sisteme giris yapilmis olmalidir


from cgitb import text
from unittest import expectedFailure
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


##############################################################################################

# Test Case 1 - Hatali girislerde sistem hata mesaji gostermelidir  (Parametrize - Dictionary)

class Test_wrong_login:
#This class includes login tests

    expected_login_errors = {
        "Both Blank"     : ["Epic sadface: Username is required"],
        "Username Blank" : ["Epic sadface: Username is required"],
        "Password Blank" : ["Epic sadface: Password is required"],
        "Wrong User"     : ["Epic sadface: Username and password do not match any user in this service"]
        
    }


    @pytest.mark.parametrize("username,password,result",[("","","Both Blank"),("","123","Username Blank"),("user","","Password Blank"),("user","123","Wrong User")])
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

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=\"error\"]")))
        errorMessage = self.driver.find_element(By.CLASS_NAME,"error-message-container")
        sleep(1)
        
        # We compared the expected result with the actual result

        assert self.expected_login_errors[result][0] == errorMessage.text.strip()

        self.driver.quit()



##############################################################################################

# Test Case 2: Urunler sepete eklenebilmelidir

class Test_basket_control:

    def test_basket_control(self):

        #### Login 

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))

        email_log = self.driver.find_element(By.ID,"user-name")
        email_log.send_keys("standard_user")
        
        password_log = self.driver.find_element(By.ID,"password")
        password_log.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        sleep(1)

        #### Add Basket

        # WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]"))

        item_select = self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack")
        item_select.click()
        sleep(1)

        item_select = self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-bike-light")
        item_select.click()
        sleep(1)

        item_select = self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt")
        item_select.click()
        sleep(1)

        item_select = self.driver.find_element(By.ID,"shopping_cart_container")
        item_select.click()
        sleep(1)

        # We compared the expected results with the actual results

        assert self.driver.find_element(By.ID,"item_4_title_link").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.ID,"item_0_title_link").text == "Sauce Labs Bike Light"
        assert self.driver.find_element(By.ID,"item_1_title_link").text == "Sauce Labs Bolt T-Shirt"

        self.driver.quit()


##############################################################################################

# Test Case 3: Sistemden cikis yapildiginda sepete ulasilmamalidir


class Test_log_out_basket:

    def test_log_out_basket(self):
        
        # Login 

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))

        email_log = self.driver.find_element(By.ID,"user-name")
        email_log.send_keys("standard_user")
        
        password_log = self.driver.find_element(By.ID,"password")
        password_log.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        sleep(1)
        
        # Add some item to basket

        item_select = self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack")
        item_select.click()
        sleep(1)

        # Log out

        self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        sleep(2)
        self.driver.find_element(By.ID,"logout_sidebar_link").click()

        # Try to go basket
        sleep(2)
        self.driver.get("https://www.saucedemo.com/cart.html")
        

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=\"error\"]")))
        errorMessage = self.driver.find_element(By.CLASS_NAME,"error-message-container")

         # We compared the expected result with the actual result

        assert errorMessage.text.strip() == "Epic sadface: You can only access '/cart.html' when you are logged in."

        sleep(3)

        self.driver.quit()
