import pytest
from selenium import webdriver
from byhy.byhy_po.page_object.dingdan_page import DingdanPage
from byhy.byhy_po.page_object.kehu_page import KehuPage
from byhy.byhy_po.page_object.login_page import LoginPage
from byhy.byhy_po.data.open_file import loadyaml
from byhy.byhy_po.page_object.yaopin_page import YaopinPage


# @pytest.fixture(scope='function')
# @pytest.mark.parametrize('udata', loadyaml('../data/user.yaml'))
# def driver(udata):
#     driver = webdriver.Chrome()
#     lp = LoginPage(driver)
#     lp.login(udata['username'], udata['password'])


class TestByhy:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lp = LoginPage(self.driver)
        self.yp = YaopinPage(self.driver)
        self.kh = KehuPage(self.driver)
        self.dd = DingdanPage(self.driver)

    def teardown_class(self):
        self.lp.sleep(1)
        self.driver.quit()

    @pytest.mark.smoke
    @pytest.mark.parametrize('udata', loadyaml('../data/user.yaml'))
    def test_01(self, udata):
        self.lp.login(udata['username'], udata['password'])

    @pytest.mark.parametrize('udata', loadyaml('../data/yaopin.yaml'))
    def test_02(self, udata):
        self.yp.yaopin_ok(udata['aa'], udata['bb'], udata['cc'])

    def test_03(self):
        self.yp.yaopin_no()

    @pytest.mark.parametrize('udata', loadyaml('../data/kehu.yaml'))
    def test_04(self, udata):
        self.kh.kehu_ok(udata['a'], udata['b'], udata['c'])

    def test_05(self):
        self.kh.kehu_no()

    @pytest.mark.parametrize('udata', loadyaml('../data/dingdan.yaml'))
    def test_06(self, udata):
        self.dd.dingdan_ok(udata['aaa'], udata['bbb'])

    def test_07(self):
        self.dd.dingdan_no()

