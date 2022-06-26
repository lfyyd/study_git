import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://xfbfu.com/registIndex/login?isLogout=1')
driver.add_cookie({"userType": "0","userMobile": "17610372399","userPsw": "lf123456"})
driver.add_cookie({"userType": "0","userMobile": "17610372399","userPsw": "lf123456"})
# 再次访问xxxx网站，将会自动登录
driver.get("https://xfbfu.com/")
