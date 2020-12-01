import json
import os
import logging
import sys
import requests
dirpath = os.path.abspath(os.path.dirname(__file__))


def get_records(filename):
    records = []
    filename = dirpath+'/'+filename
    with open(filename, 'r') as f:
        records = [eval(line.strip(os.linesep))
                   for line in f if not line.startswith(os.linesep)]
    for record in records:
        # 默认为http,有证书可以注释该处理
        record['url'] = record['url'].replace('https', 'http')
        new_headers = {}
        for key, value in record['headers'].items():
            # requests 不支持2.0请求头,过滤请求头
            if ":" == value[0]:
                continue
            new_headers[str(key)] = str(value)
        record['headers'] = new_headers
    return records


if __name__ == "__main__":
    last_dirpath = os.sep.join(dirpath.split(os.sep)[:-1])
    sys.path.append(last_dirpath)
    from base_api import base_api, api_proxies
    api = base_api()
    log_name = 'record_xxxx.log'
    for record in get_records(log_name):
        url, headers, data = record['url'], record['headers'], record['text']
        ret = requests.post(url, headers=headers, data=data)
        print(ret)
        break
