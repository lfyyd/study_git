# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from pytest_study.open import yamlload
#
#
# @pytest.mark.parametrize('udata', yamlload('./study.yaml'))
# def test_01(udata):
#     driver = webdriver.Chrome()
#     driver.get(udata['url'])
#     driver.find_element(udata['input']['key'],udata['input']['value']).send_keys(udata['txt'])
#     driver.find_element(udata['input']['key'],udata['input']['value']).click()
