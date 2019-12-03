#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午1:19
# @Author  : Chenzd
# @Site    : 隐藏式开关逻辑设备冒烟
# @File    : hiddenSwitch_logic.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.hiddenSwitch.hiddenSwitch_logic').getlog()

class hiddenSwitch_logic(unittest.TestCase):
    '''隐藏式--逻辑设备冒烟'''

    @classmethod
    def setUpClass(cls):
        print('隐藏式--逻辑设备冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test_hiddenSwitch_logic(self):
        self.logicName = '隐藏式开关8'
        self.commonpage.enter_device_list_nextPage('隐藏式开关', self.logicName)
        # 进入逻辑设备
        self.commonpage.get_title()
        print('进入设备的名称为【%s】'% CommonPage.title_text)
        self.lightpage.enter_light_logic()
        result = self.lightpage.enter_light_logic_type()
        if result == 0:
            name = self.lightpage.get_logicName()
            print('1. 设备名称编辑')
            logger.info('1. 设备名称编辑')
            result = self.commonpage.edit_name('', name+self.commonpage.random_name(),'保存','返回')
            self.assertEqual(0, result, '结果：名称编辑异常')
            self.lightpage.enter_light_logic()
            interface = self.lightpage.enter_light_logic_type()
            if interface == 0:
                print('2. 检测定位图标是否正常')
                logger.info('2. 检测定位图标是否正常')
                result = self.commonpage.location_is_normal()
                self.assertEqual(0, result, '结果：图标定位异常')
                print('3. 检测设备位置显示是否正确')
                logger.info('3. 检测设备位置显示是否正确')
                result = self.commonpage.device_location_show_logic()
                self.assertEqual(0, result, '结果：设备位置显示错误')
                result = self.commonpage.device_location_show2_logic()
                self.assertEqual(0, result, '结果：设备位置显示错误')
                print('4. 检测滑动屏幕是否正常')
                logger.info('4. 检测滑动屏幕是否正常')
                result = self.commonpage.is_swipe('按键控制其它设备')
                self.assertEqual(0, result, '结果：屏幕滑动异常')
                self.lightpage.swipe_up()
                print('5. 检测图标替换是否正常')
                logger.info('5. 检测图标替换是否正常')
                result = self.lightpage.icon_replace()
                self.assertEqual(0, result, '结果：图标替换异常')
                print('6. 按键控制其它设备是否正常')
                logger.info('6. 按键控制其它设备是否正常')
                result = self.lightpage.control_other()
                self.assertEqual(0, result, '结果：按键控制其它设备异常')
                self.lightpage.enter_logic_by_name()
                # 关闭按键控制其它设备
                self.lightpage.close_control_other()
                print('7. 隐藏是否正常')
                logger.info('7. 隐藏是否正常')
                result = self.lightpage.Hide_is_normal()
                self.assertEqual(0,result,'结果：隐藏功能异常')
                # 关闭隐藏
                print('8. 关闭隐藏')
                logger.info('8. 关闭隐藏')
                self.commonpage.enter_device_list_nextPage('隐藏式开关', CommonPage.title_text[-1])
                self.lightpage.cancle_hide()
                self.commonpage.back_top()
            else:
                logger.info('进行P1操作')
                self.lightpage.config_P1()
        else:
            logger.info('进行P1操作')
            self.lightpage.config_P1()
        CommonPage.title_text = []
        CommonPage.update_name = []
    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('隐藏式--逻辑设备冒烟结束')