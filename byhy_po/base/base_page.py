from time import sleep

import allure
from prompt_toolkit.contrib.telnet.protocol import EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # img = self.driver.get_screenshot_as_png()  # 截图
        # allure.attach(img, f'po实例化完成')

    def geturl(self, url):
        self.driver.get(url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()

    def alert(self):
        # img = self.driver.get_screenshot_as_png()
        # allure.attach(img, f'弹框截图')
        self.driver.switch_to.alert.accept()

    def wait(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(loc))
