from time import sleep
import pytest
from selenium import webdriver
from byhy_po.page_object.login_page import LoginPage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('byhy', '88888888')
    yield driver
    sleep(2)
    driver.quit()
