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
#
# Test Case 4: Urunler isim ve fiyata gore siralanabilmelidir
#       On Kosullar: - Sisteme giris yapilmis olmalidir
#

from cgitb import text
from lib2to3.pgen2 import driver
from unittest import expectedFailure
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import constants

##############################################################################################

# Test Case 1 - Hatali girislerde sistem hata mesaji gostermelidir  (Parametrize - Dictionary)

class Test_wrong_login:
#This class includes login tests



    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize("username,password,result",[("","","Both Blank"),("","123","Username Blank"),("user","","Password Blank"),("user","123","Wrong User")])
    def test_wrong_logins(self,username,password,result):
        
        
        self.driver.get("https://www.saucedemo.com")
        
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
        assert constants.login_errors[result][0] == errorMessage.text.strip()


##############################################################################################

# Test Case 2: Urunler sepete eklenebilmelidir

class Test_basket_control:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_basket_control(self):

        #### Login 

        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))

        email_log = self.driver.find_element(By.ID,"user-name")
        email_log.send_keys("standard_user")
        
        password_log = self.driver.find_element(By.ID,"password")
        password_log.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"shopping_cart_container")))

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


##############################################################################################

# Test Case 3: After logout, user will not be able to access the basket.


class Test_log_out_basket:


    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_log_out_basket(self):
        
        # Login 

        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))

        email_log = self.driver.find_element(By.ID,"user-name")
        email_log.send_keys("standard_user")
        
        password_log = self.driver.find_element(By.ID,"password")
        password_log.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"shopping_cart_container")))

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


##############################################################################################

# Test Case 4: Urunler isim ve fiyata gore siralanabilmelidir


class Test_sort_by:


    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_sort_by(self):
        
        # Login 
        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))

        email_log = self.driver.find_element(By.ID,"user-name")
        email_log.send_keys("standard_user")
        
        password_log = self.driver.find_element(By.ID,"password")
        password_log.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"shopping_cart_container")))    


        # Sort By Name (A to Z)
        sortby = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[1]")
        sortby.click()
        first_item = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
        sleep(1)
        assert first_item.text == constants.item_list["First"][0]
        # Take ScreenShot
        sleep(1)
        self.driver.save_screenshot(f"sort_of_atoz_{date.today()}.png")
        
        # Sort By Name (Z to A)
        sortby = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[2]")
        sortby.click()
        first_item = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
        sleep(1)
        assert first_item.text == constants.item_list["Sixth"][0]
        sleep(1)
        self.driver.save_screenshot(f"sort_of_ztoa_{date.today()}.png")

        # Sort By Price (Low to High)
        sortby = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[3]")
        sortby.click()
        first_item = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
        sleep(1)
        assert first_item.text == constants.item_list["Fifth"][0]
        sleep(1)
        self.driver.save_screenshot(f"sort_of_lowprice_{date.today()}.png")

        # Sort By Price (High to Low)
        sortby = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[4]")
        sortby.click()
        first_item = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
        sleep(1)
        assert first_item.text == constants.item_list["Fourth"][0] 
        sleep(1)
        self.driver.save_screenshot(f"sort_of_highprice_{date.today()}.png")
