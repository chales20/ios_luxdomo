#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 上午11:33
# @Author  : Chenzd
# @Site    : 智能锁控制冒烟
# @File    : lock_control.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from page.leebus.lock.lockPage import LockPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.lock.lock_control').getlog()
class lock_control(unittest.TestCase):
    '''指纹锁--主界面控制'''

    @classmethod
    def setUpClass(cls):
        print('指纹锁--主界面控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.lockpage = LockPage(cls.driver)
        cls.commonpage.back_top()

    def test_lock_control(self):
        self.commonpage.enter_device_list_nextPage('智能锁', '智能锁9')
        text_list = self.commonpage.get_location_text()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)
        self.lightpage.click_device_interface(name_text)
        print('1. 开锁检验是否开启成功')
        logger.info('1. 开锁检验是否开启成功')
        self.lockpage.open_lock()
        result = self.lockpage.check_time()
        self.assertEqual(0, result, '结果：开锁异常')
        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.location_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('指纹锁--主界面控制冒烟结束')
