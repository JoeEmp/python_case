# coding:utf-8
from behave import *
from com import TestDriver
from settings import implicitly_wait_sec

__author__ = 'joe'


def before_all(context):
    pass


def after_all(context):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context.driver = TestDriver().driver
    context.driver.implicitly_wait(implicitly_wait_sec)


def after_scenario(context, scenario):
    try:
        context.driver.quit()
    except Exception as e:
        print(e)


def before_step(context, step):
    pass


def after_step(cotext, step):
    pass
