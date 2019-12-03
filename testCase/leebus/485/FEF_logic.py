#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 上午10:38
# @Author  : Chenzd
# @Site    : 485逻辑设备编辑
# @File    : FEF_logic.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.dimmer.dimmerPage import DimmerPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.485.FEF_logic').getlog()

class FEF_logic(unittest.TestCase):
    '''485--逻辑设备冒烟'''

    @classmethod
    def setUpClass(cls):
        print('485--逻辑设备冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.dimmerpage = DimmerPage(cls.driver)
        cls.commonpage.back_top()

    def test_FEF_logic(self):
        self.logicName = '485对接模块4'
        self.commonpage.enter_device_list_nextPage('485对接模块', self.logicName)
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        text_list = self.commonpage.get_location_text_ID()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)

        print('4. 从主页进入控制页')
        logger.info('4. 从主页进入控制页')
        self.lightpage.click_device_interface(name_text)
        self.commonpage.enter_menu()
        name = self.lightpage.get_logicName()
        print('5. 设备名称编辑')
        logger.info('5. 设备名称编辑')
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(), '保存', '返回')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.commonpage.enter_menu()
        print('6. 检测定位图标是否正常')
        logger.info('6. 检测定位图标是否正常')
        result = self.commonpage.location_is_normal()
        self.assertEqual(0, result, '结果：图标定位异常')
        print('7. 检测设备位置显示是否正确')
        logger.info('7. 检测设备位置显示是否正确')
        result = self.commonpage.device_location_show_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        result = self.commonpage.device_location_show2_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        print('8. 检测滑动屏幕是否正常')
        logger.info('8. 检测滑动屏幕是否正常')
        result = self.commonpage.is_swipe('楼层房间配置')
        self.assertEqual(0, result, '结果：屏幕滑动异常')

        self.commonpage.save()
        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.title_text = []
        CommonPage.physical_device = []
        DimmerPage.hide_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('485--逻辑设备冒烟结束')
