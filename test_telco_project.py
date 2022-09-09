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
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sistemeGiris(self):
    self.driver.get("http://localhost:4200/login")
    self.driver.set_window_size(1520, 819)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[1]/input")))
   
    username = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[1]/input")
    username.click()
    username.send_keys("admin")

    password = self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[2]/input")
    password.click()
    password.send_keys("admin")
    sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/button").click()
    sleep(1)

    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/p")))

    assert self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/p").text == "SEARCH RESULT"
  
    