import pytest
from selenium import webdriver

from byhy.POM.page_object.login_page import LoginPage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login_ok('byhy', '88888888')
    yield driver
    lp.sleep(2)
    driver.quit()