import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import date
from time import sleep


## TELCO PROJECT TESTS
# 1 - Sisteme Giris Testi
# 2 - Musteri Arama Testi 
# 3 - Musteri Fatura Hesabi olusturma testi (Yavas)
# 4 - Musteri Fatura Hesabi olusturma testi (Hizli)





  ########### 1- Sisteme giris yapan test otomasyonu

class TestSistemeGiris():

  # Setup Method testlerimizin baslangicinda gerceklesecek komutlari barindirir
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    
  # Teardown Method testlerimizin sonunda gerceklesecek komutlari barindirir
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sistemeGiris(self):

    # Testin baslangicinda kullanilan URL
    self.driver.get("http://localhost:4200/login")

    # Ekran boyutu degistirildi
    self.driver.set_window_size(1520, 819)

    # Bir sonraki komuta gecmeden once login ekranindaki "username" yazisi gorunene kadar bekler (Xpath kullanildi)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[1]/input")))
   
    # Username girdi alani icin degisken tanimlandi
    username = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[1]/input")
    # Girdi alanina tiklandi
    username.click()
    # Girdi alanina "admin" yazildi
    username.send_keys("admin")

    # Ayni islemler password icin yapildi
    password = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[2]/input")
    password.click()
    password.send_keys("admin")

    # Login butonu click
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/button").click()
    
    # Customer Search ekrani gorunene kadar bekleyen komut
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/p")))
    sleep(1)
    # Son olarak "Search Results" yazisini kontrol ederek, giris yapildigini dogruluyoruz ve testimiz bu yaziya gore true veya false donuyor
    assert self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/p").text == "SEARCH RESULT"
  
  

  ########### 2- Musterinin Customer Account sayfasindaki bilgilerinin dogru gosterildigini kontrol eden test otomasyonu
class TestSearchCustomerAccount():
  def setup_method(self):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_customerAccount(self):

    # URL 
    self.driver.get("http://localhost:4200/customer-dashboard")
    # Yeniden boyutlandirdik
    self.driver.set_window_size(1552, 849)
    sleep(1)
    body = self.driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.PAGE_DOWN)
    sleep(0.5)
    # First Name girdi alani icin degisken tanimlandi
    firstName = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")
    firstName.send_keys("nappie")
    sleep(2)
    self.driver.find_element(By.CLASS_NAME, "e-btn-search").click()
    sleep(2)
    
    # Cust ID si 2 olan kullaniciya tikladik
    body.send_keys(Keys.PAGE_UP)
    sleep(1)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "2")))
    self.driver.find_element(By.LINK_TEXT, "2").click()
    sleep(2)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(1) > .col-4:nth-child(2) > .e-frame-label")))
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
    sleep(2)

    #Detaylari Actik
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".e-accordion-header > .col-2:nth-child(2)")))
    self.driver.find_element(By.CSS_SELECTOR, "#flush-heading1 .col-1 > img").click()
    sleep(2)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#flush-collapse1 .ng-star-inserted:nth-child(1) > td:nth-child(2)")))
    
    # Detaylarda daha onceden belirttigimiz 70 Mbps VDSL yazisini dogruladik
    assert self.driver.find_element(By.CSS_SELECTOR, "#flush-collapse1 .ng-star-inserted:nth-child(1) > td:nth-child(2)").text == "70 Mbps VDSL"


  ########### 3- Yeni bir kullanici (odeme) hesabi acan ve sonrasinda bilgileri kontrol eden test otomasyonu

class TestCreateCustomerAccount_Slow():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createCustomerAccount(self):
    self.driver.get("http://localhost:4200/dashboard/customers/customer-billing-account-detail/2")
    self.driver.set_window_size(1552, 849)
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".ml-5").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".mt-3")))
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".e-input-dark").click()
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".e-input-dark").send_keys("Acc1")
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".e-address-desc").send_keys("Account 1")
    sleep(1)
    
    # Islem yapilacak alan ekranda gorunmedigi icin sayfayi asagiya kaydirdik
    sleep(1)
    body = self.driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.PAGE_DOWN)

    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".e-btn-new-address").click()
    
    dropdown = self.driver.find_element(By.ID, "gender")
    sleep(1)
    
    dropdown.click()
    sleep(1)
    dropdown.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[1]/div/div[2]/div/select/option[6]").click()
    sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[2]/div/div[2]/input").click()
    sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[2]/div/div[2]/input").send_keys("21")
    sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[3]/div/div[2]/input").click()
    sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[3]/div/div[2]/input").send_keys("Oklahoma")
    sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[4]/div/div[2]/textarea").send_keys("Oklahoma Apartment")
    sleep(1)

    body.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".ml-auto > .e-btn-clear").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "th > div:nth-child(2)")))
    sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".col-lg-5 > .e-btn-clear").click()
    sleep(1)
    self.driver.execute_script("window.scrollTo(0,0)")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".e-layout-title")))
    sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "#flush-heading3 .col-2:nth-child(4)").text == "Acc1"

    arrow = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/app-main-layout/div/div/div[2]/div/app-table-accordion[3]/div/div/h2/button/div/div[1]/img").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".e-accordion-header > .col-2:nth-child(2)")))
    sleep(0.1)
    body.send_keys(Keys.PAGE_DOWN)
    sleep(0.2)

    self.driver.save_screenshot(f"new_customer_account_{date.today()}.png")


class TestCreateCustomerAccount_Fast():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createCustomerAccount(self):
    self.driver.get("http://localhost:4200/dashboard/customers/customer-billing-account-detail/2")
    self.driver.set_window_size(1552, 849)
    self.driver.find_element(By.CSS_SELECTOR, ".ml-5").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".mt-3")))
    self.driver.find_element(By.CSS_SELECTOR, ".e-input-dark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".e-input-dark").send_keys("Acc1")
    self.driver.find_element(By.CSS_SELECTOR, ".e-address-desc").send_keys("Account 1")
    sleep(0.3)
    
    # Islem yapilacak alan ekranda gorunmedigi icin sayfayi asagiya kaydirdik
    body = self.driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.PAGE_DOWN)

    sleep(0.3)
    self.driver.find_element(By.CSS_SELECTOR, ".e-btn-new-address").click()
    
    dropdown = self.driver.find_element(By.ID, "gender")
    sleep(0.3)
    
    dropdown.click()
    sleep(0.1)
    dropdown.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[1]/div/div[2]/div/select/option[6]").click()
    sleep(0.1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[2]/div/div[2]/input").click()
    sleep(0.1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[2]/div/div[2]/input").send_keys("21")
    sleep(0.1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[3]/div/div[2]/input").click()
    sleep(0.1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[3]/div/div[2]/input").send_keys("Oklahoma")
    sleep(0.1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div/form/div[1]/div[4]/div/div[2]/textarea").send_keys("Oklahoma Apartment")
    sleep(0.1)

    body.send_keys(Keys.PAGE_DOWN)
    sleep(0.2)
    self.driver.find_element(By.CSS_SELECTOR, ".ml-auto > .e-btn-clear").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "th > div:nth-child(2)")))
    sleep(0.2)
    self.driver.find_element(By.CSS_SELECTOR, ".col-lg-5 > .e-btn-clear").click()
    sleep(0.2)
    self.driver.execute_script("window.scrollTo(0,0)")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".e-layout-title")))
    assert self.driver.find_element(By.CSS_SELECTOR, "#flush-heading3 .col-2:nth-child(4)").text == "Acc1"


    arrow = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/app-main-layout/div/div/div[2]/div/app-table-accordion[3]/div/div/h2/button/div/div[1]/img").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".e-accordion-header > .col-2:nth-child(2)")))
    sleep(0.1)
    body.send_keys(Keys.PAGE_DOWN)
    sleep(0.2)

    self.driver.save_screenshot(f"new_customer_account_fast_{date.today()}.png")