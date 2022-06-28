from selenium.webdriver.common.by import By

from byhy_po.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://127.0.0.1/mgr/sign.html'
    user = (By.ID, 'username')
    word = (By.ID, 'password')
    btn = (By.XPATH, '//*[text()="登录"]')
    sms = (By.XPATH, "//*[contains(text(),'操作菜单')]")

    def login(self, username, password):
        self.geturl(self.url)
        self.input(self.user, username)
        self.input(self.word, password)
        self.click(self.btn)

