#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 下午2:54
# @Author  : Chenzd
# @Site    : 删除场景
# @File    : delete_scene.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.scene.scenePage import ScenePage
from page.leebus.commonPage import CommonPage
from page.leebus.scene.scene_editPage import Scene_editPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.scene.delete_scene').getlog()
class delete_scene(unittest.TestCase):
    '''删除场景--冒烟'''

    @classmethod
    def setUpClass(cls):
        print('删除场景--冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.scenePage = ScenePage(cls.driver)
        cls.commonPage = CommonPage(cls.driver)
        cls.scene_editPage = Scene_editPage(cls.driver)

    def test_delete_scene(self):
        '''创建快速添加的场景'''
        self.commonPage.scene_click()
        while len(self.commonPage.scene_name_list) > 0:
            print('1.=====长按是否有编辑菜单=====')
            logger.info('1.=====长按是否有编辑菜单=====')
            result = self.scene_editPage.enter_sceneEt(self.commonPage.scene_name_list[-1])
            self.assertEqual(0, result, '结果：长按异常')
            self.commonPage.scene_name_list.pop(-1)
            print('2.删除场景')
            logger.info('2.删除场景')
            result = self.scene_editPage.delete_scene()
            self.assertEqual(0, result, '结果：删除异常')
        self.commonPage.swipe_down()
        self.commonPage.home_click()


    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('删除场景--冒烟结束')