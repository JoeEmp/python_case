from behave import When, Given, Then
from element import elements
from com import ConfigError
import datetime
from time import sleep
import logging
from utils import swipe

@When('点击{text}按钮')
def click_button(context, text):
    elementObj = elements.get(text, None)
    if not elementObj:
        raise ConfigError('%s 按钮不存在' % text)
    if 'xpath' in elementObj.keys():
        context.driver.find_element_by_xpath(elementObj['xpath']).click()
    if 'id' in elementObj.keys():
        context.driver.find_element_by_id(elementObj['id']).click()

@Then('截图')
def screenshot(context):
    file = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.png'
    logging.info(' save result png as %s'%file)
    context.driver.get_screenshot_as_file(file)

@when('模拟点击{text}')
def driver_tap(context,text):
    elementObj = elements.get(text, None)
    context.driver.tap(elementObj.get('bounds'),500)

@Then('等待{sec}s')
def wait(context,sec):
    sleep(float(sec))

@When('上划')
def up_swipe(context):
    swipe(context)

@When('下划')
def down_swipe(context):
    swipe(context,'down')
