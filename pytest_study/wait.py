from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://baidu.com/')
# driver.implicitly_wait(5)
driver.find_element(By.ID,'kw').send_keys('csnd')
driver.find_element(By.ID,'su').click()
# sleep(1) #强制等待
driver.find_element(By.LINK_TEXT,'CSDN - 专业开发者社区').click()