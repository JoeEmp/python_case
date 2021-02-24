### 阅读帮助

BDD用例弱化了服务端的测试，加强了用户行为的覆盖，强化联调的效果，同时我们使用接口测试来保证接口的质量。
后面是二轮测试，或是探索性测试来提高系统的稳定性和可用性。
BDD的编写过程本身就是，在模拟用户操作，它很容易发现在需求中逻辑中的不足。从而很快的补齐需求

vscode上友好阅读需安装插件 Feature Syntax Highlight and Snippets README

pycharm上则需要 BDD Support

### 安装
```(shell)
pip install behave
pip install selenium
```

### 快速开始
```(shell)
mv {this_file_dir}
behave baidu.feature
```

#### 简单概念

Given: 可以理解为前置条件

When:  可以理解为行为用户的操作

Then:  可以理解为期望结果

And、But: 可以理解为补充说明，这里做出约定，And为期望内容，But为不期望内容

#### 补充阅读
[behave官方文档](https://behave.readthedocs.io/en/latest/api.html)

[简书上的blog简单demo](https://www.jianshu.com/p/98a58ccded32)

[behave在有车以后的实现](http://gitlab.repos.suv163.com/xingzhongxiang/iyc-appium/tree/master)

[BDD简介和学习](https://www.ibm.com/developerworks/cn/opensource/os-cn-bdd-web-ui-test/index.html)