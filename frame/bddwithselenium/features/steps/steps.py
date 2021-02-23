from behave import When, Given, Then
# from pymouse.mac import PyMouse
import sys
sys.path.append('..')
from config import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



@When('打开{browser}浏览器')
def step_impl0(context, browser):
    '''
    打开浏览器
    :param context:
    :param browser: 浏览器名称 可选内容 参看config.browser_list
    :return:
    '''
    if browser not in browser_list:
        logging.warning('打开浏览器失败，请检查环境')
        return False
    if browser == '谷歌':
        context.browser = webdriver.Chrome()
    else:
        pass
    context.browser.implicitly_wait(implicitly_wait_sec)
    context.browser.maximize_window()
    return True


@When('访问{url}')
def step_impl1(context, url):
    try:
        context.browser.get(url_dict[url])
    except Exception as e:
        logging.warning(e)


@When('点击{ele}')
def step_impl2(context, ele):
    try:
        context.browser.find_element_by_xpath(page_ele_dict[ele]).click()
    except Exception as e:
        logging.warning(e)


@When('在{ele}输入{text}')
def step_impl3(context, ele, text):
    try:
        # context.browser.find_element_by_xpath(page_ele_dict[ele]).click()
        context.browser.find_element_by_xpath(page_ele_dict[ele]).clear()
        context.browser.find_element_by_xpath(
            page_ele_dict[ele]).send_keys(text)
    except Exception as e:
        logging.warning(e)


@When('sleep {n:d}s')
def step_impl4(context, n):
    sleep(n)


@When('关闭浏览器')
def step_impl5(context):
    context.browser.quit()


'''
# mac使用比较麻烦 要在windows下调试
@When('滚动屏幕到底部')
def step_impl6():
    mouse = PyMouse()
    mouse.scroll(mouse.screen_size()[1])
'''


@When('翻到第{n:d}页')
def step_impl7(context, n):
    ele = page_ele_dict['翻页按钮'].replace('[n]', '[%d]' % n)
    context.browser.find_element_by_xpath(ele).click()


@When('悬停在{ele}')
def step_impl8(context, ele):
    ele = context.browser.find_element_by_xpath(page_ele_dict[ele])
    ActionChains(context.browser).click_and_hold(ele).perform()


@When('确定(浏览器警告框)')
def step_impl9(context):
    context.browser.switch_to.alert.accept()


@When('取消(浏览器警告框)')
def step_impl9(context):
    context.browser.switch_to.alert.dismiss()


@When('输入内容{text}(浏览器警告框)')
def step_impl9(context, text):
    context.browser.switch_to.alert.send_keys(text)


@When('选择第{n:d}个推荐项')
def step_impl9(context, n):
    ele = page_ele_dict['推荐项'].replace('[n]', '[%d]' % n)
    context.browser.find_element_by_xpath(ele).click()


@Then('截图{file_name}')
def step_impl10(context, file_name):
    context.browser.save_screenshot('../%s' % file_name)
