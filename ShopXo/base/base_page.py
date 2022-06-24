from time import sleep

from prompt_toolkit.contrib.telnet.protocol import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # WebDriverWait(driver, 5, 0.5)

        # img = self.driver.get_screenshot_as_png() #截图
        # allure.attach(img,f'po实例化完成')

    def geturl(self, url):
        self.driver.get(url)

    def locator(self, loc):
        # img = self.driver.get_screenshot_as_png()
        # allure.attach(img, f'元素定位前')
        return self.driver.find_element(*loc)

    def input(self, loc, txt):  # 输入元素
        self.locator(loc).send_keys(txt)

    def click(self, loc):  # 点击元素
        self.locator(loc).click()

    def handles(self):  # 跳转页面
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def roll(self, tc):  # 页面下滑到执行位置
        target = self.locator(tc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(1)

    def alert(self):  # 弹框处理
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def msg(self):  # 页面提示断言
        el = self.driver.find_element(By.XPATH, '//p[@class="prompt-msg"]')
        return el.text

    def frame(self, loc):  # 跳转到 iframe
        a = self.locator(loc)
        self.driver.switch_to.frame(a)

    def result(self):
        self.driver.switch_to.default_content()

    def get_click(self, loc, locs, locss, txt):  # 弹框点击查找元素
        self.click(loc)
        # a = self.locator(locs)
        # WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable(a))
        sleep(1.3)
        self.input(locs, txt)
        # b = self.locator(locss)
        # WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable(b))
        self.click(locss)

    # def wait(self,loc):
    #     # a = self.locator(wt)
    #     WebDriverWait(self.driver, 10, 0.5).until(lambda el:self.locator(loc))

