
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '11',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.tencent.mm',  # 启动APP Package名称     获取包名命令 adb shell dumpsys window|findstr mCurrentFocus
    'appActivity': '.ui.LauncherUI',
    'noReset': True,  # 不要重置App
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)
