#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午2:45
# @Author  : Chenzd
# @Site    : 智能锁逻辑设备编辑
# @File    : lock_logic.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.dimmer.dimmerPage import DimmerPage
from page.leebus.lock.lockPage import LockPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.lock.lock_logic').getlog()

class lock_logic(unittest.TestCase):
    '''智能锁--逻辑设备冒烟'''

    @classmethod
    def setUpClass(cls):
        print('智能锁--逻辑设备冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.dimmerpage = DimmerPage(cls.driver)
        cls.lockpage = LockPage(cls.driver)
        cls.commonpage.back_top()

    def test_lock_logic(self):
        self.logicName = '智能锁9'
        self.commonpage.enter_device_list_nextPage('智能锁', self.logicName)
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        # 进入逻辑设备
        print('1. 点击隐藏，判断是否有弹框')
        logger.info('1. 点击隐藏，判断是否有弹框')
        result = self.dimmerpage.dimmer_hide_click()
        self.assertEqual(0,result,'结果：存在异常')
        print('2. 在主页检测是否隐藏成功')
        logger.info('2. 在主页检测是否隐藏成功')
        result = self.dimmerpage.dimmer_hide_normal()
        self.assertEqual(0,result,'结果：存在异常')
        self.commonpage.back_top()
        print('3. 取消隐藏')
        logger.info('3. 取消隐藏')
        self.dimmerpage.cancle_hide_dimmer_nextPage('智能锁', self.logicName)
        print('4. 从主页进入控制页')
        logger.info('4. 从主页进入控制页')
        self.lightpage.click_device_interface('指纹锁')
        self.commonpage.enter_menu()
        print('5. 设备名称编辑')
        logger.info('5. 设备名称编辑')
        name = self.lightpage.get_logicName()
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(), '保存', '返回')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.commonpage.enter_menu()
        print('6. 开启指纹锁远程密码保护')
        logger.info('6. 开启指纹锁远程密码保护')
        self.lockpage.click_password()
        result = self.lockpage.is_checkpwd()
        self.assertEqual(0, result, '结果：密码保护开启异常')
        print('7. 开启推送消息通知')
        logger.info('7. 开启推送消息通知')
        self.lockpage.click_pushMsg()
        self.commonpage.save()
        print('8. 开锁检验指纹锁远程密码保护及验证消息推送')
        logger.info('8. 开锁检验指纹锁远程密码保护及验证消息推送')
        self.lockpage.open_lock()
        result = self.lockpage.is_checkpwd_one()
        self.assertEqual(0, result, '结果：密码保护检测异常')
        result = self.lockpage.is_msgTv()
        self.assertEqual(0, result, '结果：消息推送检测异常')
        result = self.lockpage.check_time()
        self.assertEqual(0, result, '结果：开锁异常')
        self.commonpage.enter_menu()
        print('9. 关闭指纹锁远程密码保护及消息推送')
        logger.info('9. 关闭指纹锁远程密码保护及消息推送')
        self.lockpage.click_password()
        result = self.lockpage.is_checkpwd()
        self.assertEqual(0, result, '结果：密码保护关闭异常')
        self.lockpage.click_pushMsg()

        self.commonpage.save()
        self.commonpage.back()
        self.commonpage.back_top()


    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('智能锁--逻辑设备冒烟结束')