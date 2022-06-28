
from selenium.webdriver.common.by import By

from byhy_po.base.base_page import BasePage


class KehuPage(BasePage):
    url = 'http://127.0.0.1/mgr/index.html#/customers'
    kh = (By.XPATH, "//*[text()='客户']")
    tj = (By.XPATH, "//*[text()='添加']")
    name = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input')
    dh = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input')
    dizhi = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea')
    btn = (By.XPATH, "//*[text()='创建']")
    data = (By.XPATH, '//*[@id="root"]/div/section[2]/div[3]')
    sc = (By.XPATH, "//*[text()='删除']")

    def kehu(self, a, b, c):
        self.click(self.kh)
        self.click(self.tj)
        self.input(self.name, a)
        self.input(self.dh, b)
        self.input(self.dizhi, c)
        self.click(self.btn)
        self.click(self.data)
        self.click(self.sc)
        self.alert()



