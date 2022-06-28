
from byhy.byhy_po.base.base_page import BasePage

from selenium.webdriver.common.by import By


class YaopinPage(BasePage):
    url = 'http://127.0.0.1/mgr/index.html#/medicines'
    yp = (By.XPATH, "//*[text()='药品']")
    tj = (By.XPATH, "//*[text()='添加']")
    mc = (
        By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input')
    bh = (
        By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input')
    ms = (
        By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea')
    btn = (By.XPATH, "//*[text()='创建']")
    data = (By.XPATH, '//*[@id="root"]/div/section[2]/div[3]')
    sc = (By.XPATH, "//*[text()='删除']")

    def yaopin(self, aa, bb, cc):
        self.click(self.yp)
        self.click(self.tj)
        self.input(self.mc, aa)
        self.input(self.bh, bb)
        self.input(self.ms, cc)
        self.click(self.btn)
        self.click(self.data)
        self.click(self.sc)
        self.alert()
