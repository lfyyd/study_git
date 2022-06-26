from time import sleep

import pytest
from selenium import webdriver
from byhy.byhy_po.page_object.dingdan_page import DingdanPage
from byhy.byhy_po.page_object.kehu_page import KehuPage
from byhy.byhy_po.page_object.login_page import LoginPage
from byhy.byhy_po.data.open_file import loadyaml
from byhy.byhy_po.page_object.yaopin_page import YaopinPage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('byhy', '88888888')
    yield driver
    sleep(2)
    driver.quit()

@pytest.mark.smoke
@pytest.mark.parametrize('udata', loadyaml('../data/user.yaml'))
def test_01(udata):
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login(udata['username'], udata['password'])

def test_02(driver,udata)
    dirver = webdriver.Chrome()

if __name__ == "__main__":
    pytest.main(['-m', 'smoke'])
