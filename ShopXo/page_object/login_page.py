from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from ShopXo.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://www.mzhshopxo.com/'
    denglv = (By.LINK_TEXT, '登录')
    usr = (By.NAME, 'accounts')
    pwd = (By.NAME, 'pwd')
    btn = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')

    def login_ok(self, username, password):
        self.geturl(self.url)
        self.click(self.denglv)
        self.input(self.usr, username)
        self.input(self.pwd, password)
        self.click(self.btn)

    # def login_no(self, username, password):
    #     self.geturl(self.url)
    #     self.click(self.denglv)
    #     self.input(self.usr, username)
    #     self.input(self.pwd, password)
    #     self.click(self.btn)
    #     ast = self.msg()
    #     print(ast)
    #     assert ast == '密码错误'

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lp = LoginPage(driver)
#     lp.login_ok('admin', 'shopxo')
