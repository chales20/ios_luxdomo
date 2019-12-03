#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 下午2:34
# @Author  : Chenzd
# @Site    : 基础类封装
# @File    : basePage.py
# @Software: PyCharm
# @company:  LEELEN
import os
import time
from PIL import Image
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

import filePath
from page.appiumDriver import MyDriver
from public.configLog import Logger
logger = Logger(logger='page.basePage.BasePage').getlog()

class BasePage(object):

    def __init__(self, appium_driver):
        self.driver = appium_driver

    '''获取单个元素'''
    def get_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            element = self.driver.find_element(*loc)
            return element
        except Exception as e:
            self.save_screenShot('get_element')
            print('查找元素异常【get_elememt】方法[%s]页面[%s]元素'%(self, loc))
            logger.info(e)
            return False

    '''获取多个元素'''
    def get_elements(self,loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except Exception as e:
            self.save_screenShot('get_elements')
            print('查找元素异常【get_elememts】方法[%s]页面[%s]元素' % (self, loc))
            return False

    '''屏幕截图'''
    def save_screenShot(self, log_sign):
        filename = filePath.get_filePath(filePath.screenShot_path, '%s.png'%(log_sign))
        self.driver.get_screenshot_as_file(filename)

    '''点击'''
    def click(self, loc):
        try:
            element = self.get_element(*loc)
            element.click()
        except Exception as e:
            self.save_screenShot('click')
            print('点击元素异常[%s]页面[%s]元素'%(self, loc))
            logger.info(e)

    '''点击元素'''
    def click_element(self, ele):
        try:
            ele.click()
        except Exception as e:
            self.save_screenShot('click_element')
            print('点击元素异常[%s]页面[%s]元素'%(self, ele))
            logger.info(e)

    '''获取元素文本'''
    def getText_element(self,ele):
        try:
            return ele.text
        except Exception as e:
            self.save_screenShot('getText_element')
            print('获取元素文本异常[%s]页面[%s]元素' % (self, ele))
            logger.info(e)

    '''输入文本'''
    def input(self, element, value):
        try:
            element.clear()
            element.set_value(value)
            element.set_value('\n')
        except Exception as e:
            self.save_screenShot('input')
            print('输入框输入异常[%s]页面[%s]元素'%(self, element))
            logger.info(e)

    '''输入文本'''
    def notclear_input(self, element, value):
        try:
            element.set_value(value)
            element.set_value('\n')
        except Exception as e:
            self.save_screenShot('notclear_input')
            print('输入框输入异常[%s]页面[%s]元素' % (self, element))
            logger.info(e)

    '''自定义元素查找方法--单个元素'''
    def wait_for_element(self,  id=None, index=None, timeOut=15):
        starTime = time.time()
        nowTime = time.time()
        while nowTime - starTime < timeOut:
            # 通过 id 或者 name 查找控件
            try:
                if id is not None:
                    if index is not None:
                        return self.driver.find_element_by_accessibility_id(id)[index]
                    else:
                        return self.driver.find_element_by_accessibility_id(id)
            except:
                return False
            nowTime = time.time()
        raise Exception("Elementid[%s] index[%s] not found" % (id, index))

    '''自定义元素查找方法--多个元素'''
    def wait_for_elements(self, id=None, index=None, timeOut=15):
        starTime = time.time()
        nowTime = time.time()
        while nowTime - starTime < timeOut:
            # 通过 id 或者 name 查找控件
            try:
                if id is not None:
                    if index is not None:
                        return self.driver.find_elements_by_accessibility_id(id)[index]
                    else:
                        return self.driver.find_elements_by_accessibility_id(id)
            except:
                return False
            nowTime = time.time()
        raise Exception("Elementids[%s] index[%s] not found" % (id, index))

    '''IOS单元素原生定位--类似Xpath，查询速度快'''
    def findIpt(self, value):
        try:
            ipt = WebDriverWait(self.driver, 5).until(lambda x:x.find_element_by_ios_predicate(value))
            # print(ipt)
            return ipt
        except Exception:
            # self.save_screenShot('findIpt')
            # print('通过Ipt查找元素异常[%s]页面[%s]元素'%(self, value))
            return False

    '''IOS多元素原生定位--类似Xpath，查询速度快'''

    def findIpts(self, value):
        try:
            if len(self.driver.find_elements_by_ios_predicate(value)):
                 return self.driver.find_elements_by_ios_predicate(value)
        except Exception:
            self.save_screenShot('findIpts')
            print('通过Ipts查找元素异常[%s]页面[%s]元素' % (self, value))
            return False

    # 根据accessibility_id定位
    def id_click(self, name):
        ele = self.wait_for_element(id=name)
        self.click_element(ele)

    '''向上滑动'''
    def swipe_up(self):
        try:
            window_size = self.driver.get_window_size()
            width = window_size.get('width')
            height = window_size.get('height')
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                  "fromX": width / 2, "fromY": height * 4 / 5,
                                                                  "toX": width / 2, "toY": height / 5})
        except Exception:
            self.save_screenShot('swipe_up')
            print('向上滑动屏幕异常[%s]页面'%(self))

    '''向上滑动--快速滑动'''
    def swipe_up_Big(self):
        try:
            window_size = self.driver.get_window_size()
            width = window_size.get('width')
            height = window_size.get('height')
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                        "fromX": width / 2, "fromY": height * 9 / 10,
                                                                        "toX": width / 2, "toY": height / 10})
        except Exception:
            self.save_screenShot('swipe_up_Big')
            print('向上滑动屏幕异常[%s]页面' % (self))

    '''向上滑动--窗帘设置时长'''
    def swipe_up_small(self):
        try:
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                        "fromX": 207, "fromY": 430,
                                                                        "toX": 207, "toY": 330})
        except Exception:
            self.save_screenShot('swipe_up_small')
            print('向上滑动屏幕异常[%s]页面' % (self))

    '''向上滑动--场景延迟开启时长'''

    def swipe_up_small_scene(self):
        try:
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                        "fromX": 200, "fromY": 710,
                                                                        "toX": 200, "toY": 670})
        except Exception:
            self.save_screenShot('swipe_up_small_scene')
            print('向上滑动屏幕异常[%s]页面' % (self))

    '''向下滑动--窗帘设置时长'''

    def swipe_down_small(self):
        try:
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                        "fromX": 207, "fromY": 330,
                                                                        "toX": 207, "toY": 430})
        except Exception:
            self.save_screenShot('swipe_down_small')
            print('向上滑动屏幕异常[%s]页面' % (self))

    '''通用滑动'''
    def swipe_control(self,x1,y1,x2,y2):
        try:
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                        "fromX": x1, "fromY": y1,
                                                                        "toX": x2, "toY": y2})
        except Exception:
            self.save_screenShot('swipe_control')
            print('向上滑动屏幕异常[%s]页面' % (self))

    '''向上滑动--回到最顶端'''

    def findElement(self,ele):
            x = 435  # 滑动区域x轴的大小--固定
            y = 737 # 滑动区域Y轴的大小--固定
            location = ele.location # 获取元素的x,y
            if 0<=location['x']<x and 64<location['y']<y:
                return True
            else:
                return False

    '''主界面查找元素---出现在屏幕内'''
    def findElement_for_interface(self,ele):
            x = 375  # 滑动区域x轴的大小--固定
            y = 687 # 滑动区域Y轴的大小--固定
            location = ele.location # 获取元素的x,y
            if 0<=location['x']<x and 64<location['y']<y:
                return True
            else:
                return False

    '''等待元素出现后停止向下滑动'''
    def waitEle_for_down(self,name):
        try:
            ele = self.findIpt("name CONTAINS '" + name + "'")
            r = self.findElement(ele)
            while r is False:
                self.swipe_up()
                ele = self.findIpt("name CONTAINS '" + name + "'")
                r = self.findElement(ele)
            return True
        except Exception as e:
            logger.info(e)
            return False

    '''等待元素出现后停止向下滑动'''

    def waitEle_for_down_by_ele(self, ele):
        try:
            r = self.findElement(ele)
            while r is False:
                self.swipe_up()
                r = self.findElement(ele)
            return True
        except Exception as e:
            logger.info(e)
            return False

    '''等待元素出现后停止向s上滑动'''
    def waitEle_for_up(self, ele):
        try:
            r = self.findElement(ele)
            while r is False:
                self.swipe_down()
                r = self.findElement(ele)
            return True
        except Exception as e:
            logger.info(e)
            return False

    '''向上滑动--快速滑动'''

    def swipe_down(self):
        try:
            window_size = self.driver.get_window_size()
            width = window_size.get('width')
            height = window_size.get('height')
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 0.1, "element": None,
                                                                        "fromX": width / 2, "fromY": height/ 10,
                                                                        "toX": width / 2, "toY": height*9/ 10})
        except Exception:
            self.save_screenShot('swipe_down')
            print('向上滑动屏幕异常[%s]页面' % (self))

    '''长按元素'''
    def longPress(self, ele):
        try:
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 3, "element": ele,
                                                                   "fromX": 0, "fromY": 0,
                                                                   "toX": 0, "toY": 0})
        except Exception as e:
            self.save_screenShot('longPress')
            print('长按异常【%s】页面【%s】元素'%(self,ele))
            logger.info(e)

    '''长按元素--调色灯删除'''

    def longPress_palette(self, ele):
        try:
            self.driver.execute_script("mobile:dragFromToForDuration", {"duration": 4, "element": ele,
                                                                        "fromX": 20, "fromY": 20,
                                                                        "toX": 20, "toY": 17})
        except Exception as e:
            self.save_screenShot('longPress')
            print('长按异常【%s】页面【%s】元素' % (self, ele))
            logger.info(e)
    '''根据元素获取属性值'''
    def element_attribute(self,ele,attribute):
        try:
            attr = ele.get_attribute(attribute)
            return attr
        except Exception as e:
            logger.info(e)
            # self.save_screenShot('element_attribute')
            print('获取元素属性异常【%s】页面【%s】元素'%(self,ele))
            return False

    '''清除文件夹下所有文件'''
    def del_file(self,path):
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取出文件绝对路径
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                BasePage(MyDriver.cur_driver()).del_file(path_file)

    '''截取整张图'''
    def complete_screen(self, complete_path):
        self.driver.get_screenshot_as_file(complete_path+"/image.png")

    '''根据单个元素截取图片----如图标'''
    def icon_screen(self, complete_path, part_path, ele, type=".png"):
        location = ele.location
        size = ele.size
        box = (location["x"],location["y"],location["x"]+size["width"],location["y"]+size["height"])
        image = Image.open(complete_path+'/image.png')
        newImage = image.crop(box)
        newImage.save(part_path+"/"+'1'+type)
        return self

    '''根据单个元素截取图片----在滑动区域内的元素'''

    def icon_screen_interface(self, complete_path, part_path, ele, type=".png"):
        location = ele.location
        size = ele.size
        box = (location["x"]+15, location["y"]+200, location["x"] + size["width"]+15, location["y"] + size["height"]+200)
        image = Image.open(complete_path + '/image.png')
        newImage = image.crop(box)
        newImage.save(part_path + "/" + '1' + type)
        return self

    '''获取图片颜色--根据像素点获取'''
    def get_color(self, img, x, y):
        el_rgba = Image.open(img+"/1.png")
        color =  el_rgba.getpixel((x,y))
        return color