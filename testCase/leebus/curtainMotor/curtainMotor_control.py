#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 下午1:47
# @Author  : Chenzd
# @Site    : 
# @File    : curtainMotor_control.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.curtain.curtainPage import CurtainPage
from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.curtainMotor.curtainMotor_control').getlog()
class curtainMotor_control(unittest.TestCase):
    '''窗帘电机--控制'''

    @classmethod
    def setUpClass(cls):
        print('窗帘电机--控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.curtainpage = CurtainPage(cls.driver)
        cls.commonpage.back_top()

    def test_curtainMotor_control(self):
        self.commonpage.enter_device_list_nextPage('窗帘电机', '窗帘电机8')
        text_list = self.commonpage.get_location_text()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)
        self.lightpage.click_device_interface(name_text)
        print('1. 打开窗帘，并判断是否控制成功')
        logger.info('1. 打开窗帘，并判断是否控制成功')
        result = self.curtainpage.control_curtain('打开')
        self.assertEqual(0, result, '结果：控制失败')
        print('1. 关闭窗帘，并判断是否控制成功')
        logger.info('1. 关闭窗帘，并判断是否控制成功')
        result = self.curtainpage.control_curtain('关闭')
        self.assertEqual(0, result, '结果：控制失败')
        print('1. 暂停窗帘，并判断是否控制成功')
        logger.info('1. 暂停窗帘，并判断是否控制成功')
        result = self.curtainpage.control_curtain('暂停')
        self.assertEqual(0, result, '结果：控制失败')

        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.location_text = []
        CurtainPage.location_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('窗帘电机--控制冒烟结束')