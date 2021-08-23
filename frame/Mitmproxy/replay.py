import json
import os
import logging
import sys
import requests
from hyper.contrib import HTTP20Adapter
dirpath = os.path.abspath(os.path.dirname(__file__))


def get_records(filename):
    records = []
    filename = dirpath + os.sep + filename
    with open(filename, 'r') as f:
        records = [eval(line.strip(os.linesep))
                   for line in f if not line.startswith(os.linesep)]
    for record in records:
        new_headers = {}
        for key, value in record['headers'].items():
            new_headers[str(key)] = str(value)
        record['headers'] = new_headers
    return records


if __name__ == "__main__":
    last_dirpath = os.sep.join(dirpath.split(os.sep)[:-1])
    sys.path.append(last_dirpath)
    from base_api import base_api, api_proxies
    api = base_api()
    log_name = 'record_20210621020246.log'
    for record in get_records(log_name):
        kwargs = {
            "url": record['url'],
            "method": record['method'],
            "version": record['version'],
            "headers": record['headers']
        }
        if 'json' in record['headers']['content-type']:
            kwargs['json'] = json.loads(record['text'])
        if 'form' in record['headers']['content-type']:
            kwargs['data'] = json.loads(record['text'])
        r = api.get_api(**kwargs)
        print(r)
