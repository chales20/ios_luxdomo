#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 下午1:50
# @Author  : Chenzd
# @Site    : 输入输出模块--逻辑设备配置和控制移动
# @File    : inoutput_main.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.input.inputPage import InputPage
from page.leebus.output.outputPage import OutputPage
from page.leebus.inoutput.inoutputPage import InoutputPage
from page.leebus.curtain.curtainPage import CurtainPage
from page.leebus.light.lightPage import LightPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.inoutput.inoutput_main').getlog()

class inoutput_main(unittest.TestCase):
    '''输入输出模块--逻辑设备配置和控制和移动'''

    name_list_one = ['灯', '电磁阀', '声光报警器', '单路通用']
    name_list_two = ['窗帘', '推窗器', '机械手', '双路通用']
    device_name = []

    @classmethod
    def setUpClass(cls):
        print('输入输出模块--逻辑设备配置和控制和移动开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.outputPage = OutputPage(cls.driver)
        cls.inoutputPage = InoutputPage(cls.driver)
        cls.inputPage = InputPage(cls.driver)
        cls.curtainpage = CurtainPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test01_inoutput_logic(self):
        '''输出模块--逻辑设备配置'''
        self.logicName = '输入输出模块8'
        self.commonpage.enter_device_list_nextPage('输入输出模块', self.logicName)
        print('1. 对模块进行配置')
        logger.info('1. 对模块进行配置')
        result = self.outputPage.output_config(self.inoutputPage.StaticText)
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
        res = self.inoutputPage.is_pushSwitch(self.inputPage.TypeSwitch)
        if res == 0:
            print('4. 检测推送按钮默认状态及控制')
            logger.info('4. 检测推送按钮默认状态及控制')
            self.inputPage.pushSwitch_state()
            result = self.inputPage.pushSwitch_control()
            self.assertEqual(0, result, '结果：控制异常')
        self.commonpage.save()

        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()

    def test02_inoutput_interface(self):
        '''输入输出模块--主界面编辑控制'''
        self.commonpage.enter_room_for_roomName(CommonPage.default_roomName[-1])
        if len([i for i in self.name_list_one + self.name_list_two if i in self.outputPage.deviceName[-1]]) > 0:
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
            self.lightpage.longPress_text(CommonPage.update_name[-1])
            self.lightpage.id_click('移动到')
            self.lightpage.move_to_defaule(CommonPage.default_roomName[-1])
        else:
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

        time.sleep(1)
        self.commonpage.back_top()
        CommonPage.default_roomName = []
        CommonPage.update_name = []



    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('输入输出模块--逻辑设备配置和控制和移动')