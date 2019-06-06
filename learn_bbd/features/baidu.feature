# Created by iyourcar at 2019-06-06
Feature: learn bbd
  # Enter feature description here

  Scenario: 搜素github
    When 打开谷歌浏览器
    When 访问百度
    When sleep 3s
    When 在搜索框输入github
    When 点击搜索按钮
    When sleep 2s
    When 关闭浏览器

  Scenario: 翻页切换
    When 打开谷歌浏览器
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When sleep 2s
#    When 滚动屏幕到底部
    When 翻到第2页
    When sleep 2s
    When 关闭浏览器