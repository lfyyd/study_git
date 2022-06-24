from selenium.webdriver.common.by import By

from byhy.byhy_po.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://127.0.0.1/mgr/sign.html'
    user = (By.ID, 'username')
    word = (By.ID, 'password')
    btn = (By.XPATH, '//*[text()="登录"]')
    sms = (By.XPATH, "//*[contains(text(),'操作菜单')]")
    dy = (By.XPATH, '//*[text()="输入用户名、密码登录"]')

    def login_ok(self, username, password):
        self.geturl(self.url)
        self.input(self.user, username)
        self.input(self.word, password)
        self.click(self.btn)
        ast = self.asser(self.sms)
        print(ast)
        assert ast == '操作菜单'

    def login_no(self, username, password):
        self.geturl(self.url)
        self.input(self.user, username)
        self.input(self.word, password)
        self.click(self.btn)
        # pdb.set_trace()
        self.sleep(1)
        self.alert()
        ast = self.asser(self.dy)
        print(ast)
        assert ast == '输入用户名、密码登录'
