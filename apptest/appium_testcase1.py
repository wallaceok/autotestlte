#coding=utf-8
from appium import webdriver
import os
import time
import unittest

PATH=lambda p:os.path.abspath( os.path.join(os.path.dirname(__file__ ),p))

global driver

import requests,		pymysql, time, sys, re
import urllib,	zlib
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep
from apitest import mod_config

HOSTNAME = '127.0.0.1'

def readSQLcase():	#流程的相关接口
    sql="SELECT id,`appcasename`,appfindmethod,appevelement,appoptmethod,appassertdata,`apptestresult` from apptest_appcasestep where apptest_appcasestep.Appcase_id=1 ORDER BY id ASC "
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
def apptestcase(case_list):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[2]
            evelement = case[3]
            optmethod = case[4]
        except Exception as e:
            return '测试用例格式不正确！%s' % e
        print(evelement)
        time.sleep(10)
        if optmethod == 'click' and findmethod == 'find_element_by_id':
            driver.find_element_by_id(evelement).send_keys('wayto')
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            driver.find_element_by_name(evelement).click()
        elif optmethod == 'sendkey':
            driver.find_element_by_name(evelement).send_keys()
if __name__== ' main ':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'com.android.test'
    desired_caps['appActivity'] = '.Test'
    desired_caps['app'] = PATH('E:\\release\\csdn.apk')
    time.sleep(1)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(1)
    readSQLcase()
    driver.quit()
    print('Done!')
    time.sleep(1)






