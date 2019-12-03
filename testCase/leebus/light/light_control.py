#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 下午1:28
# @Author  : Chenzd
# @Site    : 灯主界面所有灯控制
# @File    : light_control.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.light.Linght_control').getlog()
class Linght_control(unittest.TestCase):
    '''灯--主界面所有灯控制'''
    @classmethod
    def setUpClass(cls):
        print('灯--主界面所有灯控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test_light_control(self):
        self.lightpage.enter_room_for_hide(CommonPage.default_roomName[-1])
        print('1. 控制主页所有灯--打开')
        logger.info('1. 控制主页所有灯--打开')
        self.lightpage.control_light()
        print('2. 向上滑动到最顶部')
        logger.info('2. 向上滑动到最顶部')
        self.commonpage.back_top()
        time.sleep(2)
        print('3. 控制主页所有灯--关闭')
        logger.info('3. 控制主页所有灯--关闭')
        self.lightpage.control_light()

        self.commonpage.back_top()

        CommonPage.default_roomName = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('灯--主界面所有灯控制冒烟结束')

