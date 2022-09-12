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
from time import sleep

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
  
  

  # Customer Account Detaylarini kontrol eden test
class TestCustomerAccount():
  def setup_method(self):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_customerAccount(self):

    # URL 
    self.driver.get("http://localhost:4200/customer-dashboard")
    # Yeniden boyutlandirdik
    self.driver.set_window_size(1552, 849)

    # First Name girdi alani icin degisken tanimlandi
    firstName = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")
    firstName.send_keys("nappie")
    sleep(2)
    self.driver.find_element(By.CLASS_NAME, "e-btn-search").click()
    sleep(2)
    
    # Cust ID si 2 olan kullaniciya tikladik
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