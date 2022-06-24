from time import sleep
import pytest
from selenium import webdriver
from ShopXo.page_object.home import HomePage
from ShopXo.page_object.login_page import LoginPage
from ShopXo.page_object.shopping_page import ShoppingPage
from ShopXo.data.loadyaml import LoadYaml


# data = [
#     ('', '', '', '', '', '', '姓名格式 2~16 个字符之间'),
#     ('梁枫', '', '', '', '', '', '电话格式有误'),
#     ('梁枫', '17610372399', '', '', '', '', '详细地址格式1~80个字符之间'),
#     ('梁枫', '17610372399', '', '', '', '奥体', '请选择省份'),
#     ('梁枫', '17610372399', '浙江省', '', '', '奥体', '请选择城市'),
#     ('梁枫', '17610372399', '浙江省', '杭州市', '', '奥体', '请选择区/县'),
#     ('梁枫', '17610372399', '浙江省', '杭州市', '萧山区', '奥体', '操作成功'),
# ]

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login_ok('admin', 'shopxo')
    yield driver
    sleep(2)
    driver.quit()


# @pytest.mark.parametrize('udata', LoadYaml('./ShopXo/data/user.yaml'))
# def test_01(udata):
#     driver = webdriver.Chrome()
#     lp = LoginPage(driver)
#     lp.login_ok(udata['username'], udata['password'])
#     ast = lp.msg()
#     print(ast)
#     assert ast == udata['assert']


def test_02(driver):
    hm = HomePage(driver)
    hm.home('苹果（Apple）iPhone 6 Plus 金色 16G')


# @pytest.mark.parametrize('udata', LoadYaml('./ShopXo/data/msg.yaml'))
# def test_03(driver, udata):
#     sp = ShoppingPage(driver)
#     sp.shopping(udata['name'], udata['tel'], udata['sheng'], udata['shi'], udata['qu'], udata['address'])
#     ast = sp.msg()
#     print(ast)
#     assert ast == udata['assert']


# if __name__ == '__main__':
#     pytest.main()
