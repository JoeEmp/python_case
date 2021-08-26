# https://github.com/joke2k/faker
# pip3 install Faker

import json
from typing import Union
from urllib import parse
import logging
from faker import Faker


fake = Faker('zh-CN')


class myFaker(Faker):
    json_types = [int, float, bool, dict, None, list, str]

    def guess_type(self, obj: str, types=None):
        """guess string data type.
        return type like 'bool'
        """
        types = types or self.json_types
        for obj_type in types:
            try:
                if obj_type is bool:
                    if "true" == obj.lower() or "false" == obj.lower():
                        return 'bool'
                    continue
                elif obj_type is dict:
                    if "{" == obj[0] and "}" == obj[-1]:
                        json.loads(obj.replace("'", '"'))
                        return 'dict'
                    continue
                elif obj_type is list:
                    if self.isList(obj):
                        return 'list'
                    continue
                elif obj_type is None:
                    if "null" == obj:
                        return "None"
                    continue
                else:
                    obj_type(obj)
                    return str(obj_type)
            except Exception as e:
                pass
        return str(type(None))

    @staticmethod
    def is_list(valueStr: str):
        # case [1,2,3,4,[1,2,[1,2]]]
        start_index = valueStr.rindex('[')
        end_index = valueStr.index(']')
        try:
            eval(valueStr[start_index:end_index+1])
            if ',' == valueStr[end_index-1]:
                return False
            newValueStr = valueStr.replace(
                valueStr[start_index:end_index+1], '0')
            if len(newValueStr) < 2:
                return True
            else:
                return myFaker.isList(newValueStr)
        except Exception as e:
            logging.warning(e)
            return False

    def fakeDataByTpye(self, valueStr, is_str=False):
        # 暂时仅支持json的数据类型
        strType = self.guess_type(valueStr)
        if 'int' in strType:
            return self.pyint()
        if 'float' in strType:
            return self.fake.pyfloat()
        if 'bool' in strType:
            return self.pybool()
        if 'dict' in strType:
            obj = eval(valueStr)
            for k, v in obj.items():
                obj[k] = self.fakeDataByTpye(str(v))
            return obj
        if 'list' in strType:
            obj = eval(valueStr)
            for i in range(len(obj)):
                obj[i] = self.fakeDataByTpye(str(obj[i]))
            return obj
        if 'str' in strType:
            return self.word()
        return None if not is_str else "null"

    def syncParameter(self, source_param: Union[str, dict]):
        """ return parameter from url or body."""
        result = None
        if isinstance(source_param, dict):
            result = self.syncBodyParameter(source_param)
        else:
            result = self.syncUrlParameter(source_param)
        return result

    def syncBodyParameter(self, source_param: dict):
        for k, v in source_param.items():
            if isinstance(v, dict):
                source_param[k] = json.dumps(v)
            else:
                source_param[k] = str(v)
        return source_param

    def syncUrlParameter(self, source_param: str):
        if 'dict' in self.guess_type(source_param):
            return self.syncBodyParameter(json.loads(source_param))
        source_param = parse.unquote(source_param)
        source_param = source_param.split('?')[-1]
        fakerData = {}
        for kv in source_param.split('&'):
            kv = kv.split('=')
            fakerData[kv[0]] = kv[1]
        return fakerData

    def generatorParameter(self, source_param: Union[str, dict], withoutFaker: Union[str, list]):
        """return faker data by json. """
        # 解析并faker
        source_param = self.syncParameter(source_param)
        for key, value in source_param.items():
            if key not in withoutFaker:
                source_param[key] = self.fakeDataByTpye(value)
        return source_param

    def fakeRequests(self, param_type: str, source_param: [str, dict], withoutFaker=None):
        result = None
        if not withoutFaker:
            withoutFaker = []
        fakerData = self.generatorParameter(source_param, withoutFaker)
        if 'url' == param_type:
            if 0 >= source_param.find('?'):
                result = ''
            else:
                result = source_param.split('?')[0] + "?"
            urlParam = '&'.join([k+"="+str(v) for k, v in fakerData.items()])
            result += urlParam
        elif "body" == param_type:
            result = fakerData
        return result

    def fakeUrlRequests(self, url, withoutFaker=None):
        return self.fakeRequests('url', url, withoutFaker)

    def fakeBodyRequests(self, body, withoutFaker=None):
        return self.fakeRequests('body', body, withoutFaker)


def simpleDemo(seed=0):
    fake = myFaker('zh-CN')
    myFaker.seed(seed)
    ret = fake.fakeDataByTpye("1")
    print("faker int data %s" % ret)


def requestsDemo(seed=0):
    fake = myFaker('zh-CN')
    myFaker.seed(seed)
    fakeUrl = fake.fakeUrlRequests('https://www.baidu.com/s?wd=google')
    print("faker new url is %s" % fakeUrl)
    fakeBody = fake.fakeBodyRequests({'errormsg': "fake data", "result": 344})
    print("faker new body is %s" % fakeBody)
    fakeBody = fake.fakeBodyRequests(
        {'errormsg': "fake data", "result": {"total": {"show_num": ["213++", 3], "hide_num": 0}}})
    print("faker new body is %s" % fakeBody)


if __name__ == "__main__":
    simpleDemo()
    requestsDemo()
