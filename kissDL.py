import json
import os
import pip
import time

try:
    from bs4 import BeautifulSoup
except ImportError:
    pip.main(['install', BeautifulSoup])

try:
    from pySmartDL import SmartDL
except ImportError:
    pip.main(['install', pySmartDL])

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions     import *
except ImportError:
    pip.main(['install', selenium])


'''
    CHANGE VALUES HERE:
'''
USERNAME      = 'dltest'
PASSWORD      = '1q2w3e4r5t'

DRIVER_PATH   = r"C:\Users\asus x550l\Documents\chromedriver_win32\chromedriver.exe"

LOGIN_PAGE    = 'http://kisscartoon.me/Login'
TARGET_PAGE   = 'http://kisscartoon.me/Cartoon/Rick-and-Morty'


DOWNLOAD_PATH = r"C:\Users\asus x550l\Downloads"
