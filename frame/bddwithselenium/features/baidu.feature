# Created by joe at 2019-06-06
Feature: learn bbd
  实现了一些web上一些操作元素的例子
  上网搜索 bbd 或者 behave 获得更多资料

  Scenario: 搜素github
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When sleep 2s

  Scenario: 翻页切换到第2页
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When sleep 2s
#    When 滚动屏幕到底部
    When 翻到第2页
    When sleep 2s

  Scenario: 悬停选择设置,搜索设置
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When 悬停在设置
    When 点击搜索设置
    When 点击设置保存
    When sleep 2s

  Scenario: 保存搜索设置(如果弹窗不及时，可能造成失败)
    When 访问百度
    When 在搜索框输入github
    When 点击搜索按钮
    When 悬停在设置
    When 点击搜索设置
    When 点击保存设置
    When sleep 2s
    When 确定(浏览器警告框)
    When sleep 2s

  Scenario: 搜索框使用(标签可能不同但是结构基本相似)
    When 访问百度
    When 在搜索框输入github
    When sleep 2s
    When 选择第1个推荐项
    When sleep 2s

  Scenario Outline: 访问不同的网站
    When 访问<site>
    When sleep 2s
    Then 截图<file_name>

    Examples: 网站,截图
      | site | file_name           |
      | 百度   | baidu.png           |
      | 大众点评 | dazhongdianping.png |