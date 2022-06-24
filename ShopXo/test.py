# import pdb
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#

#
# def msg():  # 页面提示断言
#     el = driver.find_element(By.XPATH, '//p[@class="prompt-msg"]')
#     return el.text
#
#
# driver = webdriver.Chrome()
# driver.get('http://www.mzhshopxo.com/')
# # driver.maximize_window()
# # driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT, '登录').click()
# driver.find_element(By.NAME, 'accounts').send_keys('admin')
# driver.find_element(By.NAME, 'pwd').send_keys('shopxo')
# # sleep(0.3)
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
# # sleep(3)
# driver.find_element(By.ID, 'search-input').send_keys('苹果')
# driver.find_element(By.XPATH, '//*[text()="搜索"]').click()
# sleep()
# target = driver.find_element(By.LINK_TEXT, '苹果（Apple）iPhone 6 Plus 金色 16G')
# driver.execute_script("arguments[0].scrollIntoView();", target)
# sleep(1)
# driver.find_element(By.LINK_TEXT, '苹果（Apple）iPhone 6 Plus 金色 16G').click()
# driver.switch_to.window((driver.window_handles[-1]))
# driver.find_element(By.XPATH, '//li[@class="sku-line "]').click()
# driver.find_element(
#     By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/div[2]/ul/li[1]')
# driver.find_element(By.XPATH, '//*[contains(text(),"32G")]')
# ast = msg()
# print(ast)
# assert ast == '加入成功'
# sleep(0.3)
# driver.quit()
