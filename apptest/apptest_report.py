#coding=utf-8
from appium import webdriver
import time
import os
import HTMLTestRunner

PATH=lambda p:os.path.abspath( os.path.join(os.path.dirname(__file__),p))

global driver
# -*- coding:utf-8 -*-
import requests,pymysql,time,sys,re

import urllib,	zlib
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep
from apitest import mod_config
import unittest

HOSTNAME = '127.0.0.1'

class Calculator(unittest.TestCase):
    def setUp(self):
        time.sleep(1)

    def test_readSQLcase(self):  # 流程的相关接口
        sql = "SELECT id,appfindmethod,appevelement,appoptmethod,appassertdata,`apptestresult` from apptest_appcasestep where apptest_appcasestep.Appcase_id = 1 ORDER BY id ASC "
        coon = pymysql.connect(user='root', passwd='test123456', db='autotest', port=3306,host=mod_config.getConfig("dat abase", "host"), charset='utf8')

        cursor = coon.cursor()
        aa = cursor.execute(sql)
        info = cursor.fetchmany(aa)
        for ii in info:
            case_list = []
            case_list.append(ii)
            apptestcase(case_list)
        coon.commit()
        cursor.close()
        coon.close()

    def tearDown(self):
        self.driver.quit()


def apptestcase(case_list):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[1]
            evelement = case[2]
            optmethod = case[3]
        except Exception as e:
            return '测试用例格式不正确！%s' % e
        print(evelement)
        time.sleep(10)
        if optmethod == 'click' and findmethod == 'find_element_by_id':
            driver.find_element_by_id(evelement).click()
            writeResult(case_id, '1')
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            driver.find_element_by_name(evelement).click()
            writeResult(case_id, '1')
        elif optmethod == 'sendkey':
            driver.find_element_by_id(evelement).send_keys('testdata')
            writeResult(case_id, '1')

def writeResult(case_id,result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apptest_appcasestep set apptest_appcasestep.apptestresult = % s, apptest_appcasestep.create_time = % s  where apptest_appcasestep.id = % s;"
    param = (result, now, case_id)
    print('app autotest result is ' + result.decode())
    coon = pymysql.connect(user='root', passwd='test123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8 ')
    cursor = coon.cursor()
    cursor.execute(sql, param)
    coon.commit()
    cursor.close()
    coon.close()

def caseWriteResult(case_id,result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apptest_appcase set apptest_apptest.apptestresult=%s,apptest_apptest.create_time=%s where apptest_apptest.id=%s;"
    param = (result, now, case_id)
    print('app autotest result is ' + result.decode())
    coon = pymysql.connect(user='root', passwd='test123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8 ')
    cursor = coon.cursor()
    cursor.execute(sql, param)
    coon.commit()
    cursor.close()
    coon.close()

if __name__ == ' main ':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calculator'
    time.sleep(1)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(1)

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Calculator("test_readSQLcase"))

    filename = "C:\\Users\\zh\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\autotest\\apptest\\templ ates\\" + "apptest_report.html"

    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"app 自动化测试汇总报告", description=u"app 自动化测试")
    runner.run(testunit)
    driver.quit()
    print('Done!')
    time.sleep(1)














