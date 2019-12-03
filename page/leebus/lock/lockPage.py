#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 上午9:02
# @Author  : Chenzd
# @Site    : 指纹锁页面类
# @File    : lockPage.py
# @Software: PyCharm
# @company:  LEELEN
import datetime
import time

from page.basePage import BasePage
class LockPage(BasePage):

    # 开关按钮
    TypeSwitch = "type=='XCUIElementTypeSwitch'"
    # 输入框
    TextField = "type=='XCUIElementTypeTextField'"
    # 开锁图标
    lockIcon = 'dc zl unlock nor'
    # 文本
    TypeStaticText = "type=='XCUIElementTypeStaticText'"
    # 验证密码输入框
    SecureTextField = "type=='XCUIElementTypeSecureTextField'"

    # 点击密码保护按钮
    def click_password(self):
        eles = self.findIpts(self.TypeSwitch)
        self.click_element(eles[0])

    # 点击推送按钮

    def click_pushMsg(self):
        eles = self.findIpts(self.TypeSwitch)
        self.click_element(eles[1])

    # 检测密码保护
    def is_checkpwd(self):
        print('判断是否有弹出开锁密码框')
        suc = 0
        time.sleep(1)
        eles = self.findIpts(self.TextField)
        if len(eles) == 2:
            self.input(eles[-1], 'a123456')
            self.id_click('确定')
            print('结果：有弹出开锁密码框')
        else:
            suc = 1
            print('结果：没有弹出开锁密码框')
        return suc

    # 检测密码保护--页面只有一个输入框
    def is_checkpwd_one(self):
        print('判断是否有弹出开锁密码框')
        suc = 0
        time.sleep(1)
        eles = self.findIpts(self.SecureTextField)
        if len(eles) > 0:
            self.input(eles[-1], 'a123456')
            self.id_click('确定')
            print('结果：有弹出开锁密码框')
        else:
            suc = 1
            print('结果：没有弹出开锁密码框')
        return suc

    # 开锁
    def open_lock(self):
        self.id_click(self.lockIcon)

    # 检测是否有推送弹框
    def is_msgTv(self):
        time.sleep(3)
        ele = self.wait_for_element(id='我知道了')
        suc = 0
        print('判断是否有消息推送')
        if ele:
            eles = self.findIpts(self.TypeStaticText)
            text = self.getText_element(eles[1])
            print('【%s】' % text)
            self.id_click('我知道了')
            print('结果：检测到消息推送')
        else:
            suc = 1
            print('结果：没有消息推送')
        return suc

    # 根据开门记录检测是否开锁成功
    def check_time(self):
        time.sleep(3)
        system_time = time.strftime('%H:%M', time.localtime())
        print('获取系统时间--时分：'+ str(system_time))
        system_time2 = datetime.datetime.now() - datetime.timedelta(minutes=1)
        system_time2.strftime('%H:%M')
        eles = self.findIpts(self.TypeStaticText)
        app_time = self.getText_element(eles[5])
        print('获取最新一条开门记录到时间：'+ str(app_time))
        suc = 0
        print('对比时间判断，允许误差1分钟')
        if app_time == system_time or app_time == system_time2:
            print('结果：开锁成功')
        else:
            suc = 1
            print('结果：开锁失败')
        return suc


