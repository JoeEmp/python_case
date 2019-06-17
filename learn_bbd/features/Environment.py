# coding:utf-8
from behave import *
from selenium import webdriver
from features.config import *

__author__ = 'joe'


def before_all(context):
    pass


def after_all(context):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    try:
        context.browser.quit()
    except Exception as e:
        print(e)


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(implicitly_wait_sec)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    try:
        context.browser.quit()
    except Exception as e:
        print(e)


def before_step(context, step):
    pass


def after_step(cotext, step):
    pass



