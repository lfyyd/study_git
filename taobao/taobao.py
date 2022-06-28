import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

os.popen("d:chrome.bat")
sleep(5)
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:"
driver = webdriver.Chrome(options=options)

driver.get('https://login.taobao.com/member/login.jhtml')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'id="fm-login-id"').send_keys('17610372399')
driver.find_element(By.ID, 'TPL_password_1').send_keys('Lf123456')
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()
input('hahahahhahaha')
