import requests
from appium import webdriver
import os
import sys


EXISTS_ADB = None


def is_exists_adb():
    global EXISTS_ADB
    r = os.popen('which adb').read()
    EXISTS_ADB = False if 'not found' in r else True


def get_cur_activity():
    r = os.popen('adb shell dumpsys activity top').read()


def get_activities():
    r = os.popen('adb shell dumpsys activity activities').read()


def get_apk_laubchable_activity():
    r = os.popen('adb logcat|grep -i displayed').read()
    print(r)


def launch_pkg(laubchable_activity):
    """启动app """
    r = os.popen('adb shell am start -W -n %s -S' % laubchable_activity).read()


is_exists_adb()
get_apk_laubchable_activity()