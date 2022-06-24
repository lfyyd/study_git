import pdb

from selenium.webdriver.common.by import By
from ShopXo.base.base_page import BasePage


class ShoppingPage(BasePage):
    url = 'http://www.mzhshopxo.com/'
    sp = (By.XPATH, '/html/body/div[2]/div/ul[2]/div[4]/div/a/span')
    qx = (By.XPATH, '//*[text()="全选"]')
    js = (By.XPATH, '//*[text()="结算"]')
    new = (By.XPATH, '//*[text()="使用新地址"]')
    name = (By.NAME, 'name')
    tel = (By.NAME, 'tel')
    sheng = (By.XPATH, '/html/body/div[1]/form/div[4]/div[1]/a')
    shi = (By.XPATH, '/html/body/div[1]/form/div[4]/div[2]/a')
    qu = (By.XPATH, '/html/body/div[1]/form/div[4]/div[3]/a')
    shuru1 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[1]/div/div/input')
    shuru2 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[2]/div/div/input')
    shuru3 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[3]/div/div/input')
    dianji1 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[1]/div/ul')
    dianji2 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[2]/div/ul')
    dianji3 = (By.XPATH, '/html/body/div[1]/form/div[4]/div[3]/div/ul')
    address = (By.NAME, 'address')
    btn = (By.XPATH, '/html/body/div[1]/form/div[7]/button')
    iframe = (By.XPATH, '//iframe[@src="http://www.mzhshopxo.com/?s=useraddress/saveinfo/system_type/default.html"]')

    def shopping(self, name, tel, sheng, shi, qu, address):
        self.geturl(self.url)
        self.click(self.sp)
        self.click(self.qx)
        self.click(self.js)
        self.alert()  # 弹框点击
        self.click(self.new)
        self.alert()  # 弹框点击
        self.frame(self.iframe)
        self.input(self.name, name)
        self.input(self.tel, tel)
        self.get_click(self.sheng, self.shuru1, self.dianji1, sheng)
        self.get_click(self.shi, self.shuru2, self.dianji2, shi)
        self.get_click(self.qu, self.shuru3, self.dianji3, qu)
        self.input(self.address, address)
        self.roll(self.address)
        self.click(self.btn)
        self.result()
        self.alert()
        self.alert()



