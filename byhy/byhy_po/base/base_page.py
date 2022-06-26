from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def geturl(self, url):
        self.driver.get(url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()

    def alert(self):
        self.driver.switch_to.alert.accept()
