#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 上午10:30
# @Author  : Chenzd
# @Site    :  链接设备的函数封装
# @File    : appiumDriver.py
# @Software: PyCharm
# @company:  LEELEN
import os
import filePath
import threading
from public.common import get_yaml_data
from appium import webdriver
import warnings
class AppiumDriver:

    def __init__(self):
        warnings.filterwarnings("ignore")
        data_file = os.path.join(filePath.config_path, 'desired_caps.yaml')
        self.data = get_yaml_data(data_file)

        caps = {
            'platformName': self.data['platformName'],
            'platformVersion': self.data['platformVersion'],
            'deviceName': self.data['deviceName'],
            'udid': self.data['udid'],
            'bundleId': self.data['bundleId'],
            'noReset': bool(self.data['noReset']),
            'unicodeKeyboard': self.data['unicodeKeyboard'],
            'resetkeyboard': self.data['resetkeyboard']
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()

class MyDriver:
    driver = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def cur_driver():
        if MyDriver.driver is None:
            MyDriver.mutex.acquire()
            MyDriver.driver = AppiumDriver().get_driver()
            MyDriver.mutex.release()
        return MyDriver.driver

if __name__ == '__main__':
    # AppiumDriver().get_driver()
    MyDriver.cur_driver()