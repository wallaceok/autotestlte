#encoding:utf-8
#name:mod_config.py

import configparser
import os

def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/settings.conf'
    config.read(path)
    # print(path)
    return config.get(section, key)

print(getConfig('user','username'))