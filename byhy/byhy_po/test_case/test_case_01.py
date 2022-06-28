import pytest
from selenium import webdriver
from byhy.byhy_po.page_object.dingdan_page import DingdanPage
from byhy.byhy_po.page_object.kehu_page import KehuPage
from byhy.byhy_po.page_object.login_page import LoginPage
from byhy.byhy_po.data.open_file import loadyaml
from byhy.byhy_po.page_object.yaopin_page import YaopinPage




@pytest.mark.smoke
@pytest.mark.parametrize('udata', loadyaml('./byhy/byhy_po/data/user.yaml'))
def test_01(udata):
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login(udata['username'], udata['password'])


@pytest.mark.parametrize('udata', loadyaml('./byhy/byhy_po/data/kehu.yaml'))
def test_02(driver, udata):
    kh = KehuPage(driver)
    kh.kehu(udata['a'], udata['b'],udata['c'])


@pytest.mark.parametrize('udata', loadyaml('./byhy/byhy_po/data/yaopin.yaml'))
def test_03(driver, udata):
    yp = YaopinPage(driver)
    yp.yaopin(udata['aa'], udata['bb'], udata['cc'])


@pytest.mark.parametrize('udata', loadyaml('./byhy/byhy_po/data/dingdan.yaml'))
def test_04(driver, udata):
    dd = DingdanPage(driver)
    dd.dingdan(udata['aaa'], udata['bbb'])
