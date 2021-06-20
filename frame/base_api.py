from requests import request, session,Response
import logging
from hyper.contrib import HTTP20Adapter
import re
api_proxies = {
    'http': 'http://0.0.0.0:8888/',
    'https': 'https://0.0.0.0:8888/'
}


class base_api(object):
    """ 该类是requests的二次封装,算是一个sub版,如有入参错误查看requests即可. """

    def __init__(self):
        self.last_url, self.last_response = None, None
        self.log_str = "\nurl:{url}\nbody:{body}\nreponese{response}\n"

    @staticmethod
    def is_normal(response: Response, code_ranges=list()) -> bool:
        """ check http status code,you can use code_ranges assert expectation value """
        if not code_ranges:
            return response.ok
        elif isinstance(code_ranges, list) and response.status_code in code_ranges:
            return True
        return False

    def get_api(self, url: str, method='post',version='1.0',withlog=False, *args, **kwargs) -> dict:
        """version param is support http2.0 request."""
        ret = dict(status=True)
        try:
            s = session()
            if '2.0' in version:
                search = r'https://.+?/' if url.startswith(
                    'https') else r'http://.+?/'
                start, end = re.search(search, url).span()
                url_perfix = url[start:end-1]
                s.mount(url_perfix, HTTP20Adapter())
            response = s.request(method, url, **kwargs)
            if 'code_ranges' in kwargs.keys():
                kwargs['code_ranges'] = list()
                ret['status'] = base_api.is_normal(
                    response, code_ranges=kwargs['code_ranges'])
            try:
                ret['response'] = response.json()
            except:
                ret['response'] = response.text
            self.last_url, self.last_response = url, response
            for key in ['data', 'json', 'params']:
                if key in kwargs.keys():
                    body = kwargs[key]
            if withlog:
                logging.info(self.log_str.format_map(
                    dict(url=url, body=body, response=ret['response'])))
        except Exception as e:
            ret['status'], ret['reason'] = False, e
        return ret

    def post(self, url, *args, **kwargs):
        """ get_api use post method """
        return self.get_api(url, method='post', *args, **kwargs)

    def get(self, url, *args, **kwargs):
        """ get_api use get method """
        return self.get_api(url, method='get', *args, **kwargs)

    def options(self, url, *args, **kwargs):
        """ get_api use options method """
        return self.get_api(url, method='options', *args, **kwargs)

    def __doc__(self):
        """该类是requests的二次封装,算是一个sub版,如有入参错误查看requests即可.
        last_url,last_response分别为最近一次的请求地址和请求结果(Response)。在并发请求的时候请注意这两个属性的使用.
        """


if __name__ == "__main__":
    api = base_api()
    print(api.get("http://www.baidu.com/s",version='2.0'))
    print(api.get("http://www.baidu.com/s"))