from mitmproxy import http
from mitmproxy import ctx
from datetime import datetime
import logging
import json
import copy

nt = datetime.now()


class logRecord:
    def __init__(self):
        self.ts = nt.strftime("%Y%m%d%H%M%S")
        # 需要录制的主机
        self.target_hosts = []
        self.logs = []
        self.log_name = "mitmproxy_requests_%s" % self.ts
        self.request_log = {}
        # debug
        # print('log Record start %s'%nt.strftime('%Y-%m-%d %H:%M:%S'))

    def request(self, flow: http.HTTPFlow):
        if not self.target_hosts or flow.request.host in self.target_hosts:
            self.request_log['url'] = flow.request.url
            self.request_log['version'] = flow.request.http_version
            self.request_log['headers'] = dict()
            headers = copy.deepcopy(flow.request.headers)
            for key, value in headers.items():
                self.request_log['headers'][key] = value
            self.request_log['text'] = flow.request.text
            print(self.request_log)


addons = [
    logRecord()
]
