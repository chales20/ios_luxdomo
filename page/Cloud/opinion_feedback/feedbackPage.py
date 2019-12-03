#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 下午3:53
# @Author  : Chenzd
# @Site    : 意见反馈页面类
# @File    : feedbackPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

import filePath
from page.basePage import BasePage
class FeedbackPage(BasePage):

    # 意见反馈
    feedback_layout = "type=='XCUIElementTypeStaticText' and name=='意见反馈'"
    # 问题
    problem = "type=='XCUIElementTypeStaticText' and name=='问题'"
    # 选中的颜色
    chose_color = '(4, 193, 125)'
    # 编辑框
    StaticText = "type=='XCUIElementTypeStaticText'"
    # 编辑后编辑框
    TextView = "type=='XCUIElementTypeTextView'"
    # 选择问题设备
    TextField = "type=='XCUIElementTypeTextField'"
    # 空白处
    CollectionView = "type=='XCUIElementTypeCollectionView'"
    # 勾选照片
    TypeButton = "type=='XCUIElementTypeButton'"
    # 删除照片按钮
    del_btn = "type=='XCUIElementTypeButton' and name=='fb del'"

    def random_name200(self):
        str_name = ['1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e', 'f', '你', '我', '他', '黑', '豹', '鸽']
        str_sum = []
        for i in range(200):
            a = str_name[random.randint(0, len(str_name) - 1)]
            str_sum.append(a)
        name = ''.join(str_sum)
        return name

    # 进入意见反馈页
    def enter_feedback(self):
        self.id_click('更多')
        ele = self.findIpt(self.feedback_layout)
        self.click_element(ele)

    # 检测默认选项
    def check_defaul(self):
        ele = self.findIpt(self.problem)
        self.del_file(filePath.picture_feedback_path)
        time.sleep(7)
        self.complete_screen(filePath.screen_path)
        self.icon_screen_interface(filePath.screen_path, filePath.compare_after_path, ele)
        print('取出控制后的颜色进行对比...')
        rgba = self.get_color(filePath.compare_after_path, 30, 5)
        suc = 0
        if str(rgba) == self.chose_color:
            print('结果：按钮被选中')
        else:
            suc = 1
            print('结果：按钮未被选中')
        return suc

    # 编辑反馈内容
    def edit_suggestEt(self):
        eles = self.findIpts(self.StaticText)
        self.input(eles[2], 'a')
        print('输入名称少于6个字符')
        self.id_click('提交')
        suc = 0
        ele = self.wait_for_element(self.feedback_layout)
        if ele:
            suc = 1
            print('结果：名称少于6个字符可以保存')
        else:
            print('结果：反馈内容不少于6字')
        ele = self.findIpt(self.TextView)
        self.input(ele, self.random_name200())
        print('输入名称上限（包括数字/中文/英文）')
        eles = self.findIpts(self.CollectionView)
        self.click_element(eles[0])
        self.id_click('提交')
        ele = self.wait_for_element(self.feedback_layout)
        if ele:
            suc = 1
            print('结果：未选择问题设备可以保存')
        else:
            print('结果：请选择问题设备')
        return suc

    # 编辑建议内容
    def edit_suggestEt_opinion(self):
        eles = self.findIpts(self.StaticText)
        self.input(eles[2], 'a')
        print('输入名称少于6个字符')
        self.id_click('建议')
        self.id_click('提交')
        suc = 0
        ele = self.wait_for_element(self.feedback_layout)
        if ele:
            suc = 1
            print('结果：名称少于6个字符可以保存')
        else:
            print('结果：反馈内容不少于6字')
        ele = self.findIpt(self.TextView)
        self.input(ele, self.random_name200())
        print('输入名称上限（包括数字/中文/英文）')
        eles = self.findIpts(self.CollectionView)
        self.click_element(eles[0])
        return suc

    # 选择问题设备
    def chose_device(self):
        eles = self.findIpts(self.TextField)
        self.click_element(eles[0])
        eles = self.findIpts(self.StaticText)
        ran = random.randint(4, 10)
        device_name = self.getText_element(eles[ran - 1])
        self.click_element(eles[ran - 1])
        print('选择控制的设备名称为【%s】' % device_name)
        self.id_click('ci bar back')
        eles = self.findIpts(self.TextField)
        text = self.getText_element(eles[0])
        suc = 0
        if text == device_name:
            print('结果：选择问题设备正常')
        else:
            suc = 1
            print('结果：选择问题设备异常')
        return suc

    # 检验添加照片
    def add_photo(self):
        self.id_click('fb_add')
        self.id_click('从手机相册选择')
        time.sleep(2)
        ranlist = []
        for i in range(3):
            eles = self.findIpts(self.TypeButton)
            ran = random.randint(5, len(eles)-1)
            while ran in ranlist:
                ran = random.randint(5, len(eles) - 1)
            ranlist.append(ran)
            self.click_element(eles[ran])
        print('随机添加照片三张')
        self.id_click('完成')
        time.sleep(2)
        suc = 0
        ele = self.wait_for_element(id='fb_add')
        if ele:
            suc = 1
            print('结果：添加三张照片后还可以添加')
        else:
            print('结果：最多只能添加3张照片')
        return suc

    # 检验删除照片
    def del_photo(self):
        suc = 0
        eles = self.findIpts(self.del_btn)
        ran = random.randint(0, len(eles)-1)
        self.click_element(eles[ran])
        print('随机删除一张照片')
        eles = self.findIpts(self.StaticText)
        text = self.getText_element(eles[1])
        print('【%s】' % text)
        self.id_click('确定')
        ele = self.wait_for_element(id='fb_add')
        if ele:
            print('结果：删除一张照片后，存在添加照片按钮，正常')
        else:
            suc = 1
            print('结果：删除一张照片后，不存在添加照片按钮，异常')
        return suc

    # 检验提交是否成功
    def check_submit(self):
        time.sleep(2)
        self.id_click('提交')
        suc = 0
        time.sleep(13)
        ele = self.wait_for_element(id='家')
        if ele:
            print('结果：提交成功')
        else:
            suc = 1
            print('结果：提交异常')
        return suc

    # 建议编辑界面-------------------------------------------------------------

    def click_opinion(self):
        ele = self.wait_for_element(id='建议')
        self.click_element(ele)

    # 记录界面---------------------------------------------------------------
    TypeTable = "type=='XCUIElementTypeTable'"
    TypeCell = "type=='XCUIElementTypeCell'"

    def click_record(self):
        ele = self.wait_for_element(id='记录')
        self.click_element(ele)

    # 检验提交的记录
    def check_record(self):
        time.sleep(10)
        ele1 = self.wait_for_element(id='问题')
        ele2 = self.wait_for_element(id='建议')
        suc = 0
        if ele1 and ele2:
            print('结果：刚才提交的记录有存在')
        else:
            suc = 1
            print('结果：刚才提交的记录未存在')
        return suc

    def click_edit(self):
        ele = self.wait_for_element(id='编辑')
        self.click_element(ele)

    # 检测全选
    def all_chose(self):
        self.id_click('全选')
        ele = self.wait_for_element(id='取消')
        suc = 0
        if ele:
            print('结果：全选成功')
        else:
            suc = 1
            print('结果：全选失败')
        return suc

    # 检测删除
    def check_delete(self):
        self.id_click('删除')
        eles = self.findIpts(self.StaticText)
        text = self.getText_element(eles[0])
        print('[%s]' % text)
        self.id_click('确定')
        time.sleep(2)
        eles = self.findIpts(self.TypeCell)
        suc = 0
        if eles:
            suc = 1
            print('结果：删除失败')
        else:
            print('结果：删除成功')
        ele = self.findIpt(self.TypeTable)
        text = self.getText_element(ele)
        print('界面显示为[%s]' % text)
        return suc
