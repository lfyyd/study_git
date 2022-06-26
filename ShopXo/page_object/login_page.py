from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from ShopXo.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://shop-xo.hctestedu.com/'
    denglv = (By.XPATH,'//div/a[@class="am-btn-primary btn am-fl"]')
    usr = (By.NAME, 'accounts')
    pwd = (By.NAME, 'pwd')
    btn = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')

    def login_ok(self, username, password):
        self.geturl(self.url)
        self.click(self.denglv)
        self.input(self.usr, username)
        self.input(self.pwd, password)
        self.click(self.btn)

