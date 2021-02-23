Feature: 游戏相关模块

  @skip
  Scenario: 第一次开始游戏
    # Given 清除数据
    When 点击New_Game按钮
    When 点击dialog_New_game按钮
    Then 等待1s
    Then 截图


  Scenario: 第二次开始游戏
    When 点击New_Game按钮
    When 点击dialog_New_game按钮
    Then 等待1s
    Then 截图

  Scenario: 选择数字1
    When 点击New_Game按钮
    When 点击dialog_New_game按钮
    Then 等待1s
    When 模拟点击num1
    Then 等待1s
    Then 截图

  @debug
  Scenario: 滑动屏幕测试
    When 点击setting_icon按钮
    When 点击Assists按钮
    Then 等待1s
    Then 截图
    Then 等待1s
    When 上划
    Then 截图
