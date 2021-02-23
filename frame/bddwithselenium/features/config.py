import logging
from os import chdir

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s')

url_dict = {
    "百度": "https://www.baidu.com",
    "github": "https://github.com",
    "大众点评": 'http://www.dianping.com/'
}

page_ele_dict = {
    '搜索框': '//*[@id="kw"]',
    '搜索按钮': '//*[@id="su"]',
    '翻页按钮': '//*[@id="page"]/a[3]/span[n]',
    '设置': '//*[@id="u"]/a[2]',
    '搜索设置': '//*[@class="setpref"]',
    '保存设置': '//*[@id="gxszButton"]/a[1]',
    '推荐项': '//*[@id="form"]/div/ul/li[n]',
    '学术': '//*[@id="u1"]/a[6]'
}

# 环境支持可自动化的浏览器
browser_list = [
    '谷歌'
]

implicitly_wait_sec = 100

dir = __file__[:-len(__file__.split('/')[-1])]
chdir(dir)