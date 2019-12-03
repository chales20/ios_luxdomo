#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 上午10:32
# @Author  : Chenzd
# @Site    : 所有文件路径统一封装
# @File    : filePath.py
# @Software: PyCharm
# @company:  LEELEN

import os
import time

'''一级目录'''
pro_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前项目目录

config_path = os.path.join(pro_path, 'config')
result_path = os.path.join(pro_path, 'result')
testCase_path = os.path.join(pro_path, 'testCase')
testFile_path = os.path.join(pro_path, 'testFile')

'''二级目录'''
log_path = os.path.join(result_path, 'log')
report_path = os.path.join(result_path, 'report')
screenShot_path = os.path.join(result_path, 'screenShot')
picture_feedback_path = os.path.join(result_path, 'picture_feedback')

'''三级目录'''
compare_after_path = os.path.join(picture_feedback_path,'compare_after')
screen_path = os.path.join(picture_feedback_path,'screen')

'''文件路径'''
emailContent_path = os.path.join(testFile_path, 'emailContent.html')
caselist_path = os.path.join(testFile_path, 'caseList.xlsx')


# 文件夹名称以日期命名
def get_filePath(file_path, file_type):

    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    now = time.strftime('%m-%d-%H_%M_%S',time.localtime(time.time()))

    filePath = os.path.join(file_path, day)
    if not os.path.exists(filePath):
        os.mkdir(filePath)
    fileName = os.path.join(filePath, now+file_type)
    return fileName

if __name__ == '__main__':
    print(get_filePath(log_path, '.log'))