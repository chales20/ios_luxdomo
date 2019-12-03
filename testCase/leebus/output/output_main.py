#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午3:32
# @Author  : Chenzd
# @Site    : 4路输出模块--逻辑设备配置和控制和移动
# @File    : output_main.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.output.outputPage import OutputPage
from page.leebus.curtain.curtainPage import CurtainPage
from page.leebus.light.lightPage import LightPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.output.output_main').getlog()

class output_main(unittest.TestCase):
    '''4路输出模块--逻辑设备配置和控制和移动'''
    @classmethod
    def setUpClass(cls):
        print('4路多功能输出模块--逻辑设备配置和控制和移动开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.outputPage = OutputPage(cls.driver)
        cls.curtainpage = CurtainPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test01_output_logic(self):
        '''4路输出模块--逻辑设备配置'''
        self.logicName = '4路输出模块'
        self.commonpage.enter_device_list('4路多功能输出模块', self.logicName)
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
        self.commonpage.save()

        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()

    def test02_output_control(self):
        '''4路输出模块控制'''
        self.commonpage.enter_room_for_roomName(CommonPage.default_roomName[-1])
        res = self.outputPage.output_control_type()
        if res == 1:
            print('1. 打开窗帘，并判断是否控制成功')
            logger.info('1. 打开窗帘，并判断是否控制成功')
            result = self.curtainpage.control_curtain('打开')
            self.assertEqual(0, result, '结果：控制失败')
            print('2. 关闭窗帘，并判断是否控制成功')
            logger.info('2. 关闭窗帘，并判断是否控制成功')
            result = self.curtainpage.control_curtain('关闭')
            self.assertEqual(0, result, '结果：控制失败')
            print('3. 暂停窗帘，并判断是否控制成功')
            logger.info('3. 暂停窗帘，并判断是否控制成功')
            result = self.curtainpage.control_curtain('暂停')
            self.assertEqual(0, result, '结果：控制失败')
            self.commonpage.enter_menu()
            print('4. 检测设备位置显示是否正确')
            logger.info('4. 检测设备位置显示是否正确')
            result = self.commonpage.device_location_show_physical()
            self.assertEqual(0, result, '结果：设备位置显示错误')
            result = self.commonpage.device_location_show2_physical()
            self.assertEqual(0, result, '结果：设备位置显示错误')
            print('5. 检测滑动屏幕是否正常')
            logger.info('5. 检测滑动屏幕是否正常')
            result = self.commonpage.is_swipe('楼层房间配置')
            self.assertEqual(0, result, '结果：屏幕滑动异常')
            print('6. 检测设置窗帘时长是否正常')
            logger.info('6. 检测设置窗帘时长是否正常')
            result = self.curtainpage.set_time()
            self.assertEqual(0, result, '结果：设置时长异常')
            self.commonpage.save()
            self.commonpage.back()
        self.commonpage.back_top()

    def test03_output_move(self):
        '''4路输出模块移动'''
        self.lightpage.random_longPress(self.outputPage.deviceName[-1])
        self.lightpage.id_click('名称')
        name = self.lightpage.get_logicName()
        print('1. 主界面长按设备名称编辑')
        logger.info('1. 主界面长按设备名称编辑')
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(), '确定', '完成')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.lightpage.id_click('完成')
        self.lightpage.random_longPress(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        print('2. 主界面长按设备移动到功能检测')
        logger.info('2. 主界面长按设备移动到功能检测')
        result = self.lightpage.move_to(CommonPage.default_roomName[-1])
        self.assertEqual(0, result, '结果：移动到功能异常')
        print('3. 移动回默认房间')
        logger.info('3. 移动回默认房间')
        self.lightpage.longPress_text(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        self.lightpage.move_to_defaule(CommonPage.default_roomName[-1])
        time.sleep(1)
        self.commonpage.back_top()
        CommonPage.default_roomName = []
        CommonPage.update_name = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('4路输出模块--逻辑设备配置和控制和移动')