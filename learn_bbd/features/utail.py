from selenium import webdriver
from features.config import *
import pymouse


def find():
    b = webdriver.Chrome()
    # b.find_element_by_xpath().click()
    b.find_element_by_xpath().send_keys()
    print(page_ele_dict['搜索输入框'])
    print(page_ele_dict['搜索按钮'])
    m = pymouse.PyMouse()


if __name__ == '__main__':
    find()
