#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 上午9:20
# @Author  : Chenzd
# @Site    : 六路输入模块--逻辑配置和控制移动
# @File    : input_main.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.output.outputPage import OutputPage
from page.leebus.input.inputPage import InputPage
from page.leebus.light.lightPage import LightPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.input.input_main').getlog()

class input_main(unittest.TestCase):
    '''6路输入模块--逻辑设备配置和控制和移动'''
    @classmethod
    def setUpClass(cls):
        print('6路输入模块--逻辑设备配置和控制和移动开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.outputPage = OutputPage(cls.driver)
        cls.inputPage = InputPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test01_input_logic(self):
        '''6路输入模块--逻辑设备配置'''
        self.logicName = '6路输入模块'
        self.commonpage.enter_device_list('6路开关量输入模块', self.logicName)
        print('1. 对模块进行配置')
        logger.info('1. 对模块进行配置')
        result = self.outputPage.output_config(self.outputPage.TypeButton)
        self.assertEqual(0,result,'结果：配置异常')
        print('2. 检测显示位置是否正常')
        logger.info('2. 检测显示位置是否正常')
        result = self.commonpage.device_location_show_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        result = self.commonpage.device_location_show2_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        print('3. 检测滑动屏幕是否正常')
        logger.info('3. 检测滑动屏幕是否正常')
        result = self.commonpage.is_swipe('楼层房间配置')
        self.assertEqual(0, result, '结果：屏幕滑动异常')
        print('4. 检测推送按钮默认状态及控制')
        logger.info('4. 检测推送按钮默认状态及控制')
        res = self.inputPage.pushSwitch_state()
        if res == 0:
            result = self.inputPage.pushSwitch_control()
            self.assertEqual(0, result, '结果：控制异常')
        self.commonpage.save()

        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        CommonPage(MyDriver.cur_driver()).back_home()    # 确保报错后  不影响下一条用例

    def test02_input_interface(self):
        '''6路输入模块--主界面编辑'''
        self.commonpage.enter_room_for_roomName(CommonPage.default_roomName[-1])
        self.lightpage.click_device_interface('其它设备')
        text = self.inputPage.random_enter_one()
        self.commonpage.enter_menu()
        print('1. 设备名称编辑')
        logger.info('1. 设备名称编辑')
        result = self.commonpage.edit_name('', text + self.commonpage.random_name(), '保存', '返回')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.commonpage.enter_menu()
        print('2. 检测显示位置是否正常')
        logger.info('2. 检测显示位置是否正常')
        result = self.commonpage.device_location_show_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        result = self.commonpage.device_location_show2_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        print('3. 检测滑动屏幕是否正常')
        logger.info('3. 检测滑动屏幕是否正常')
        result = self.commonpage.is_swipe('楼层房间配置')
        self.assertEqual(0, result, '结果：屏幕滑动异常')
        print('4. 检测推送按钮默认状态及控制')
        logger.info('4. 检测推送按钮默认状态及控制')
        res = self.inputPage.pushSwitch_state()
        if res == 0:
            result = self.inputPage.pushSwitch_control()
            self.assertEqual(0, result, '结果：控制异常')
        self.commonpage.save()
        self.commonpage.back()
        self.commonpage.back()
        print('5. 检验长按是否有菜单')
        logger.info('5. 检验长按是否有菜单')
        self.lightpage.random_longPress('其它设备')
        result = self.inputPage.is_ele('名称')
        self.assertEqual(0, result, '结果：长按异常')
        self.commonpage.id_click('完成')

        self.commonpage.swipe_up()
        self.commonpage.back_top()
        CommonPage.default_roomName = []
        CommonPage.update_name = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('6路输入模块--逻辑设备配置和控制和移动')