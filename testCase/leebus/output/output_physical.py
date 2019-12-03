#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午3:07
# @Author  : Chenzd
# @Site    : 四路输出模块物理设备冒烟
# @File    : output_physical.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.output.output_physical').getlog()
class output_physical(unittest.TestCase):
    '''四路输出--物理设备编辑'''
    @classmethod
    def setUpClass(cls):
        print('四路输出--物理设备编辑冒烟')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)

    def test_output_physical(self):
        self.logicName = '4路输出模块'
        self.commonpage.enter_device_list_nextPage('4路多功能输出模块', self.logicName)
        self.commonpage.enter_menu()
        print('1. 设备名称编辑')
        logger.info('1. 设备名称编辑')
        name = self.lightpage.get_logicName()
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(), '保存', '返回')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        self.commonpage.enter_menu()
        print('2. 检测定位图标是否正常')
        logger.info('2. 检测定位图标是否正常')
        result = self.commonpage.location_is_normal()
        self.assertEqual(0, result, '结果：图标定位异常')
        print('3. 检测设备位置显示是否正确')
        logger.info('3. 检测设备位置显示是否正确')
        result = self.commonpage.device_location_show_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        result = self.commonpage.device_location_show2_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        print('4. 检测滑动屏幕是否正常')
        logger.info('4. 检测滑动屏幕是否正常')
        result = self.commonpage.is_swipe('删除设备')
        self.assertEqual(0, result, '结果：屏幕滑动异常')
        self.commonpage.save()

        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('四路输出--物理设备编辑冒烟')