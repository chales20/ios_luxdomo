#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 下午2:57
# @Author  : Chenzd
# @Site    : 调光灯控制
# @File    : dimmer_control.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.dimmer.dimmerPage import DimmerPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.dimmer.Dimmer_control').getlog()
class Dimmer_control(unittest.TestCase):
    '''调光灯--随机控制一个'''

    @classmethod
    def setUpClass(cls):
        print('调光灯--控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.dimmerpage = DimmerPage(cls.driver)
        cls.commonpage.back_top()

    def test_dimmer_control(self):
        self.commonpage.enter_device_list_random('调光', '调光灯')
        text_list = self.commonpage.get_location_text()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)
        self.lightpage.click_device_interface(name_text)
        print('1. 打开调光灯，并判断是否控制成功')
        logger.info('1. 打开调光灯，并判断是否控制成功')
        result = self.dimmerpage.control_dimmer_open()
        self.assertEqual(0, result, '结果：控制失败')
        print('2. 关闭调光灯，并判断是否控制成功')
        logger.info('2. 关闭调光灯，并判断是否控制成功')
        result = self.dimmerpage.control_dimmer_close()
        self.assertEqual(0, result, '结果：控制失败')

        self.commonpage.back()
        self.commonpage.back_top()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('调光灯--控制冒烟结束')