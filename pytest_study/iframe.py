from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
iframe = driver.find_element(By.XPATH,'//iframe[@frameborder="0"]')
driver.switch_to.frame(iframe)
sleep(1)
driver.find_element(By.NAME,'email').send_keys('123456')
sleep(1)
driver.find_element(By.NAME,'password').send_keys('123456')
