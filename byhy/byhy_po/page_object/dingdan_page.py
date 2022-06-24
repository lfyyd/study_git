from selenium.webdriver.common.by import By

from byhy.byhy_po.base.base_page import BasePage


class DingdanPage(BasePage):
    url = 'http://127.0.0.1/mgr/index.html#/orders'
    kh = (By.XPATH, "//*[text()='订单']")
    tj = (By.XPATH, "//*[text()='添加']")
    id = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input')
    keh = (By.XPATH, '//*[text()="南京中医院1"]')
    yaop = (By.XPATH, '//*[text()="青霉素盒装1"]')
    sl = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/div/input')
    btn = (By.XPATH, "//*[text()='创建']")
    data = (By.XPATH, '//*[@id="root"]/div/section[2]/div[3]')
    sc = (By.XPATH, "//*[text()='删除']")

    def dingdan_ok(self, aaa, bbb):
        self.click(self.kh)
        self.click(self.tj)
        self.input(self.id, aaa)
        self.click(self.keh)
        self.click(self.yaop)
        self.input(self.sl, bbb)
        self.click(self.btn)

    def dingdan_no(self):
        self.geturl(self.url)
        self.click(self.data)
        self.click(self.sc)
        self.alert()
