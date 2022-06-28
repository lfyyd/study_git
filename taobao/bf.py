from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# b = webdriver.Chrome(options=option)
b = webdriver.Chrome()

b.get('https://xfbfu.com/registIndex/login?isLogout=1')

b.find_element(By.XPATH,'//input[@placeholder="请输入手机号"]').send_keys('17610372399')
b.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys('lf123456')
b.find_element(By.XPATH,'//button[@data-v-76960b6a]').click()
input('hahahahhahaha')
