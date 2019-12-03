#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 下午1:46
# @Author  : Chenzd
# @Site    : 485对接模块控制
# @File    : FEF_control.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.wind.windPage import WindPage
from page.leebus.FEF.FEFPage import FEFPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.485.FEF_control').getlog()
class FEF_control(unittest.TestCase):
    '''485--随机控制一个'''

    @classmethod
    def setUpClass(cls):
        print('485--控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.windpage = WindPage(cls.driver)
        cls.FEFpage = FEFPage(cls.driver)
        cls.commonpage.back_top()

    def test_FEF_control(self):
        self.logicName = '485对接模块4'
        self.commonpage.enter_device_list_nextPage('485对接模块', self.logicName)
        # 进入逻辑设备
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        text_list = self.commonpage.get_location_text_ID()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)

        self.lightpage.click_device_interface(name_text)
        if name_text.startswith('新风'):
            print('1. 打开新风，并判断是否控制成功')
            logger.info('1. 打开新风，并判断是否控制成功')
            result = self.windpage.wind_control((4, 193, 125))
            self.assertEqual(0, result, '结果：控制失败')
            print('2. 控制风速，并判断是否控制成功')
            logger.info('2. 控制风速，并判断是否控制成功')
            result = self.windpage.wind_speed()
            self.assertEqual(0, result, '结果：控制失败')
            print('3. 关闭新风，并判断是否控制成功')
            logger.info('3. 关闭新风，并判断是否控制成功')
            result = self.windpage.wind_control((173, 182, 181))
            self.assertEqual(0, result, '结果：控制失败')
        if name_text.startswith('中央空调'):
            print('1. 打开空调，并判断是否控制成功')
            logger.info('1. 打开空调，并判断是否控制成功')
            result = self.FEFpage.open_condition()
            self.assertEqual(0, result, '结果：控制失败')
            print('2. 控制空调，并判断是否控制成功')
            logger.info('2. 控制空调，并判断是否控制成功')
            result = self.FEFpage.control_condition()
            self.assertEqual(0, result, '结果：控制失败')
            print('3. 关闭空调，并判断是否控制成功')
            logger.info('3. 关闭空调，并判断是否控制成功')
            result = self.FEFpage.close_condition()
            self.assertEqual(0, result, '结果：控制失败')
        if name_text.startswith('地暖'):
            print('1. 打开地暖，并判断是否控制成功')
            logger.info('1. 打开地暖，并判断是否控制成功')
            result = self.FEFpage.warm_control((58, 169, 189))
            self.assertEqual(0, result, '结果：控制失败')
            print('2. 关闭地暖，并判断是否控制成功')
            logger.info('2. 关闭地暖，并判断是否控制成功')
            result = self.FEFpage.warm_control((173, 182, 181))
            self.assertEqual(0, result, '结果：控制失败')
        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.location_text = []
        CommonPage.title_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('485--控制冒烟结束')