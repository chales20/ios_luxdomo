#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 下午1:36
# @Author  : Chenzd
# @Site    : 多功能配置
# @File    : scenePanel_config.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.scenePanel.scenePanelPage import ScenePanelPage
from public.configLog import Logger
logger = Logger(logger='testCase.leebus.scenePanel.ScenePanel_config').getlog()

class ScenePanel_config(unittest.TestCase):
    '''多功能面板--配置'''
    @classmethod
    def setUpClass(cls):
        print('多功能面板--配置冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.scenepanelpage = ScenePanelPage(cls.driver)

    def test_scenePanel_config(self):
        self.logicName = '4路多功能'
        self.commonpage.enter_device_list('多功能控制面板', self.logicName)
        print('1. 配置多功能面板--设备')
        logger.info('1. 配置多功能面板--设备')
        result = self.scenepanelpage.config_device()
        self.assertEqual(0,result,'结果：配置设备异常')
        print('2. 配置多功能面板--场景')
        logger.info('2. 配置多功能面板--场景')
        result = self.scenepanelpage.config_scene()
        self.assertEqual(0, result, '结果：配置设备异常')

        self.commonpage.id_click('barItem back n')
        self.commonpage.back()
        self.commonpage.home_click()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('多功能面板--配置冒烟结束')