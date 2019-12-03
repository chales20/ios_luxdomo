#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 上午8:56
# @Author  : Chenzd
# @Site    : 新风控制
# @File    : wind_control.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.wind.windPage import WindPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.wind.wind_control.Wind_control').getlog()
class Wind_control(unittest.TestCase):
    '''新风--随机控制一个'''

    @classmethod
    def setUpClass(cls):
        print('新风--控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.windpage = WindPage(cls.driver)
        cls.commonpage.back_top()

    def test_wind_control(self):
        self.logicName = '新风执行器'
        self.commonpage.enter_device_list_random('新风', self.logicName)
        # 进入逻辑设备
        print('1. 判断是否有添加面板按钮，有则是对接模块0，无则是两线新风1')
        logger.info('1. 判断是否有添加面板按钮，有则是对接模块0，无则是两线新风1')
        result = self.windpage.is_add_panle_btn()
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        if result == 1:
            text_list = self.commonpage.get_location_text()
            location = text_list[0]
            name_text = text_list[1]
        else:
            text_list = self.commonpage.get_location_text_ID()
            location = text_list[0]
            name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)

        self.lightpage.click_device_interface(name_text)
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

        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.location_text = []
        CommonPage.title_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('新风--控制冒烟结束')