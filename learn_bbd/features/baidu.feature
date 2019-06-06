# Created by iyourcar at 2019-06-06
Feature: learn bbd
  学习bbd，提供了一些操作元素的例子

  Scenario: 搜素github
    When 打开谷歌浏览器
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When sleep 2s
    When 关闭浏览器

  Scenario: 翻页切换到第2页
    When 打开谷歌浏览器
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When sleep 2s
#    When 滚动屏幕到底部
    When 翻到第2页
    When sleep 2s
    When 关闭浏览器

  Scenario: 悬停选择设置,搜索设置
    When 打开谷歌浏览器
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When 悬停在设置
    When 点击搜索设置
    When 点击设置保存
    When sleep 2s

  Scenario: 保存搜素设置
    When 打开谷歌浏览器
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When 悬停在设置
    When 点击搜索设置
    When 点击设置保存
    When sleep 2s
    When 确定(浏览器警告框)
    When sleep 2s