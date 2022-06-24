from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pytest


def test_01(driver):
    print('登录成功')
    driver.find_element(By.ID, 'username').send_keys('byhy')
    sleep(0.5)
    driver.find_element(By.ID, 'password').send_keys('88888888')
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[text()="登录"]').click()
    sleep(0.5)
    mag = driver.find_element(By.XPATH, "//*[contains(text(),'操作菜单')]").text
    assert mag == '操作菜单'
    sleep(1)


# @pytest.mark.xfail  # 当出现错误就是预料中的
def test_02(driver):
    print('登录失败')
    driver.find_element(By.ID, 'username').send_keys('byhy')
    sleep(0.5)
    driver.find_element(By.ID, 'password').send_keys('8888')
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[text()="登录"]').click()
    sleep(0.5)
    driver.switch_to.alert.accept()  # 弹框自动点击
    sleep(1)
    with pytest.raises(AssertionError):  # 异常等于这个括号里面的就是pass，不等于就是False
        mag = driver.find_element(By.XPATH, "//*[text()='输入用户名、密码登录']").text
    assert mag != '输入用户名、密码登录'
    sleep(1)
    # driver.switch_to.window(driver.window_handles[-1])  #切换到最后的窗口


def test_03(create):
    print('药品下单成功')
    create.find_element(By.XPATH, "//*[text()='药品']").click()
    sleep(0.5)
    create.find_element(By.XPATH, "//*[text()='添加']").click()
    sleep(0.5)
    create.find_element(
        By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys('花露水')
    sleep(0.5)
    create.find_element(
        By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys('E100732')
    sleep(0.5)
    create.find_element(
        By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys('梁家花露水就是棒')
    sleep(0.5)
    create.find_element(By.XPATH, "//*[text()='创建']").click()


def test_04(create):
    print('药品删除成功')
    sleep(0.5)
    create.get('http://127.0.0.1/mgr/index.html#/medicines')
    sleep(0.5)
    create.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]').click()
    sleep(0.5)
    create.find_element(By.XPATH, "//*[text()='删除']").click()
    sleep(0.5)
    create.switch_to.alert.accept()
    sleep(1)
