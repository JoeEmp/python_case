### 准备
mitmproxy安装 `brew install mitmproxy`

nohup安装`brew instll nohup`

插件开发所需 `pip3 install mitmproxy`

常用请求库`pip install mitmproxy`


[mitmproxy官网](https://mitmproxy.org/)


### launch.py
这是一个简单的启动代理的脚本，具体使用可查看help,
快速使用，`python3 launch.py`,然后输入`launch`,启动代理程序。

### replay.py
在录制完成后，我们退出launch脚本，运行前修改我们所需的录制日志名,然后我们运行`python3 replay.py`，回放我们的请求。

### 后话
快速录制后，当然就是准备下一步的性能测试了🌝