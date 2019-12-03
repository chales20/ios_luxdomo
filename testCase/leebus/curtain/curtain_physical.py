#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 下午2:48
# @Author  : Chenzd
# @Site    : 窗帘物理设备编辑
# @File    : curtain_physical.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.curtain.curtainPage import CurtainPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.curtain.curtain_physical').getlog()

class Curtain_physical(unittest.TestCase):
    '''窗帘--物理设备编辑'''
    @classmethod
    def setUpClass(cls):
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.curtainpage = CurtainPage(cls.driver)
        print('窗帘--物理设备编辑冒烟开始')

    def test_curtain_physical(self):
        self.logicName = self.curtainpage.random_curtain_logicName()
        self.commonpage.enter_device_list('窗帘控制面板',self.logicName)
        self.commonpage.get_title()
        self.commonpage.enter_menu()
        if CommonPage.title_text[-1].startswith('ZigBee'):
            print('1. 设备名称编辑')
            logger.info('1. 设备名称编辑')
            result = self.commonpage.edit_name('', self.logicName + self.commonpage.random_name(), '保存', 'barItem back n')
            self.assertEqual(0, result, '结果：名称编辑异常')
        else:
            print('1. 设备名称编辑')
            logger.info('1. 设备名称编辑')
            result = self.commonpage.edit_name('',self.logicName+self.commonpage.random_name(),'保存','返回')
            self.assertEqual(0,result,'结果：名称编辑异常')
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
        print('5. 判断是否有接近感应')
        logger.info('5. 判断是否有接近感应')
        result = self.commonpage.is_induction()
        self.assertEqual(0, result, '结果：延时关闭异常')
        self.commonpage.save()

        if CommonPage.title_text[-1].startswith('ZigBee'):
            self.commonpage.id_click('barItem back n')
        else:
            self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        CommonPage.title_text = []



    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('窗帘--物理设备编辑冒烟结束')

