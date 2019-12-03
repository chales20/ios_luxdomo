#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 下午4:38
# @Author  : Chenzd
# @Site    : 场景压力脚本
# @File    : scene.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
import time
class scene_pressure(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        print('场景压力开始')


    def test_scenePressure(self):

        for i in range(2):
            self.commonpage.scene_click()
            self.commonpage.id_click('上电')
            time.sleep(60)
            self.commonpage.home_click()
            time.sleep(60)
            self.commonpage.scene_click()
            time.sleep(60)
            self.commonpage.home_click()
            time.sleep(60)
            self.commonpage.scene_click()
            time.sleep(60)
            self.commonpage.home_click()
            time.sleep(60)
            self.commonpage.scene_click()
            time.sleep(60)
            self.commonpage.home_click()
            time.sleep(60)
            self.commonpage.scene_click()
            self.commonpage.id_click('断电')
            time.sleep(60)
            print('上电断电场景执行【%s】次' % str(i+1))

    @classmethod
    def tearDownClass(cls):
        print('场景压力结束')