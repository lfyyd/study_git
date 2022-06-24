import pytest
from selenium import webdriver

from byhy.POM.page_object.login_page import LoginPage
from byhy.POM.page_object.yaopin_page import YaopinPage
from byhy.POM.page_object.kehu_page import KehuPage
from byhy.POM.page_object.dingdan_page import DingdanPage
from byhy.POM.data.open_file import loadyaml


@pytest.mark.smoke
@pytest.mark.parametrize('udata', loadyaml('./POM/data/user.yaml'))
def test_00(udata):
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login_ok(udata['username'], udata['password'])


@pytest.mark.smoke
@pytest.mark.parametrize('udata', loadyaml('./POM/data/user.yaml'))
def test_000(udata):
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login_no(udata['usr'], udata['pwd'])


@pytest.mark.parametrize('udata', loadyaml('./POM/data/yaopin.yaml'))
def test_01(driver, udata):
    yp = YaopinPage(driver)
    yp.yaopin_ok(udata['aa'], udata['bb'], udata['cc'])


def test_02(driver):
    yp = YaopinPage(driver)
    yp.yaopin_no()


@pytest.mark.parametrize('udata', loadyaml('./POM/data/kehu.yaml'))
def test_03(driver, udata):
    kh = KehuPage(driver)
    kh.kehu_ok(udata['a'], udata['b'], udata['c'])


def test_04(driver):
    kh = KehuPage(driver)
    kh.kehu_no()


@pytest.mark.parametrize('udata', loadyaml('./POM/data/dingdan.yaml'))
def test_05(driver, udata):
    dd = DingdanPage(driver)
    dd.dingdan_ok(udata['aaa'], udata['bbb'])


def test_06(driver):
    dd = DingdanPage(driver)
    dd.dingdan_no()
