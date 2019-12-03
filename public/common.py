#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 上午10:48
# @Author  : Chenzd
# @Site    : 通用数据读取
# @File    : common.py
# @Software: PyCharm
# @company:  LEELEN
import os
import filePath
import yaml
import xlrd


'''获取yaml文件内容，返回字典类型'''
def get_yaml_data(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return data

'''获取excel的所有数据，放在列表里面'''
def get_excel_case(xls_path, xls_name, sheet_name):
    cls = []
    xlsPath = os.path.join(xls_path, xls_name)
    file = xlrd.open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0] != u'test_modules':
            cls.append(sheet.row_values(i))
    return cls


if __name__ == '__main__':
    xls1 = get_excel_case(filePath.testFile_path, 'caseList.xlsx', 'leebus')
    print(xls1)