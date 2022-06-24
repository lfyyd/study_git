from selenium.webdriver.common.by import By

from byhy.POM.base.base_page import BasePage


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

    def kehu_ok(self, a, b, c):
        self.click(self.kh)
        self.sleep()
        self.click(self.tj)
        self.sleep()
        self.input(self.name, a)
        self.sleep()
        self.input(self.dh, b)
        self.sleep()
        self.input(self.dizhi, c)
        self.sleep()
        self.click(self.btn)
        self.sleep()
        self.alert()

    def kehu_no(self):
        self.geturl(self.url)
        self.click(self.data)
        self.click(self.sc)
        self.alert()

