#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 下午3:39
# @Author  : Chenzd
# @Site    : 调色灯--控制
# @File    : palette_control.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from page.leebus.palette.palettePage import palettePage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.palette.palette_control').getlog()
class palette_control(unittest.TestCase):
    '''调色灯--控制'''

    @classmethod
    def setUpClass(cls):
        print('调色灯--控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.palettepage = palettePage(cls.driver)
        cls.commonpage.back_top()

    def test_palette_control(self):
        self.commonpage.enter_device_list_nextPage('调色灯', '调色灯8')
        text_list = self.commonpage.get_location_text_ID()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)
        self.lightpage.click_device_interface(name_text)
        print('1. 打开调色灯并判断是否开启成功')
        logger.info('1. 打开调色灯并判断是否开启成功')
        result = self.palettepage.palette_control(self.palettepage.open_icon)
        self.assertEqual(0, result, '结果：控制异常')
        print('2. 调整调色灯饱和度')
        logger.info('2. 调整调色灯饱和度')
        result = self.palettepage.open_saturationbar()
        self.assertEqual(0, result, '结果：调整异常')
        print('3. 调整调色灯亮度')
        logger.info('3. 调整调色灯亮度')
        result = self.palettepage.control_brighter()
        self.assertEqual(0, result, '结果：调整异常')
        print('4. 检测收藏功能是否正常')
        logger.info('4. 检测收藏功能是否正常')
        result = self.palettepage.check_collection()
        self.assertEqual(0, result, '结果：收藏异常')
        print('5. 检测删除功能是否正常')
        logger.info('5. 检测删除功能是否正常')
        result = self.palettepage.delete_collection()
        self.assertEqual(0, result, '结果：删除异常')
        print('6. 关闭调色灯并判断是否开启成功')
        logger.info('6. 关闭调色灯并判断是否开启成功')
        result = self.palettepage.palette_control(self.palettepage.close_icon)
        self.assertEqual(0, result, '结果：控制异常')
        time.sleep(1)
        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.location_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('调色灯--控制冒烟结束')