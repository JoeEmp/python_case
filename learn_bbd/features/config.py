import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s')

url_dict = {
    "百度": "https://www.baidu.com"
}

page_ele_dict = {
    '搜索框': '//*[@id="kw"]',
    '搜索按钮': '//*[@id="su"]',
    '翻页按钮':'//*[@id="page"]/a[3]/span[n]'
}

# 环境支持可自动化的浏览器
browser_list = [
    '谷歌'
]
