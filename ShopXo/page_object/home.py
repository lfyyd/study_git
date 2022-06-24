import pdb
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ShopXo.base.base_page import BasePage


class HomePage(BasePage):
    url = 'http://www.mzhshopxo.com/?s=search/index/wd/8EB89B6EE9C9.html'
    ssk = (By.ID, 'search-input')
    btn = (By.XPATH, '//*[text()="搜索"]')
    apple = (By.LINK_TEXT, '苹果（Apple）iPhone 6 Plus 金色 16G')
    tc = (By.XPATH, '//li[@class="sku-line "]')
    color = (
        By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/div[2]/ul/li[1]')
    content = (By.XPATH, '//*[contains(text(),"32G")]')
    btns = (By.XPATH, '//button[@data-type="cart"]')

    def home(self, aa):
        self.geturl(self.url)
        self.input(self.ssk, aa)
        self.click(self.btn)
        self.roll(self.apple)
        self.click(self.apple)
        self.handles()
        self.click(self.tc)
        # WebDriverWait(self.driver, 10).until(lambda el: self.driver.find_element(self.))
        sleep(1.5)
        self.click(self.color)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.content))
        sleep(1.5)
        self.click(self.content)
        self.click(self.btns)
        ast = self.msg()
        print(ast)
        assert ast == '加入成功'
