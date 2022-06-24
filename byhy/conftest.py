import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver



@pytest.fixture(scope="function")
def driver():
    # print('前置条件')
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1/mgr/sign.html')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # print('后置条件')
    driver.quit()

@pytest.fixture(scope='session')
def create(scope="session"):
    # print('前置条件')
    create = webdriver.Chrome()
    create.get('http://127.0.0.1/mgr/sign.html')
    # create.maximize_window()
    create.implicitly_wait(5)
    create.find_element(By.ID, 'username').send_keys('byhy')
    create.find_element(By.ID, 'password').send_keys('88888888')
    create.find_element(By.XPATH, '//*[text()="登录"]').click()
    yield create
    # print('后置条件')
    create.quit()
