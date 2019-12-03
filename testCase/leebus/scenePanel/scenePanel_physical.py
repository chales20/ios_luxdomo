#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 上午11:20
# @Author  : Chenzd
# @Site    : 多功能面板物理设备编辑
# @File    : scenePanel_physical.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.scenePanel.ScenePanel_physical').getlog()
class ScenePanel_physical(unittest.TestCase):
    '''多功能面板--物理设备编辑'''
    @classmethod
    def setUpClass(cls):
        print('多功能面板--物理设备编辑冒烟')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)

    def test_scenePanel_physical(self):
        self.logicName = '4路多功能'
        self.commonpage.enter_device_list('多功能控制面板', self.logicName)
        self.commonpage.enter_menu()
        print('1. 设备名称编辑')
        logger.info('1. 设备名称编辑')
        result = self.commonpage.edit_name('', self.logicName + self.commonpage.random_name(), '保存', 'barItem back n')
        self.assertEqual(0, result, '结果：名称编辑异常')
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
        print('5. 判断是否有接近感应')
        logger.info('5. 判断是否有接近感应')
        result = self.commonpage.is_induction()
        self.assertEqual(0, result, '结果：延时关闭异常')
        self.commonpage.save()

        self.commonpage.id_click('barItem back n')
        self.commonpage.back()
        self.commonpage.home_click()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('多功能--物理设备编辑冒烟')