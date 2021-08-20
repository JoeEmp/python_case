import yaml
import os
import importlib
from com.auto_error import AutoTestException
from unittest import TestCase
from copy import deepcopy
import logging


class YamlCaseManager():

    def __init__(self, suites_dir='cases'):
        self.suites = get_suites(suites_dir)
        self.all_cases = self.gen_all_cases()
        # if driver:
        #     self.exec_all_cases()

    def get_effective_suites(self):
        """过滤无效用例"""
        for case_name, content in self.suites.items():
            if not content:
                logging.info('%s目录无用例文件' % case_name)
                continue
            datas, template = content.get(
                'data', []), content.get('template', [])
            if not template:
                logging.warning('%s-template.yaml内容为空' % case_name)
                continue
            elif 0 == len(template):
                logging.warning('%s-template.yaml步骤为空' % case_name)
                continue
            yield case_name, template, datas

    def gen_all_cases(self):
        all_cases = []
        for case_name, template, datas in self.get_effective_suites():
            for case in YamlTemplateCases(template, datas).gen_cases():
                all_cases.append((case_name, case))
        return all_cases

    def show_cases(self):
        for case_name, template, datas in self.get_effective_suites():
            for case in YamlTemplateCases(template, datas).gen_cases():
                print(case_name, '\n', case)
                print('-'*80)

    def exec_all_cases(self):
        for case_name, case in self.all_cases:
            try:
                self.exec_case(case_name, case)
            except AutoTestException as e:
                msg = '\n用例: %s\n参数: %s\n错误信息: %s\n' % (case_name, case, e)
                logging.error(msg)
                continue
            except Exception as e:
                logging.error(e)

    def exec_case(self, case_name, case, driver, test_case_obj=None, cap=None):
        YamlCaseRunner(
            case,
            driver,
            cap=cap,
            test_case_obj=test_case_obj
        )

    def get_case(self):
        for case in self.all_cases:
            yield case


class YamlTemplateCases():

    def __init__(self, template, datas=[]):
        self.template = template
        self.datas = datas

    def gen_cases(self):
        if not self.datas:
            yield self.gen_case({}, self.template)
        for data in self.datas:
            yield self.gen_case(data, self.template)

    def gen_case(self, data, template):
        case = []
        # template
        # {'Driver': {'get': 'https://www.baidu.com'}},
        # {'BaiduIndexPage': {'search_input': {'send_keys': '{key}'}}},
        # {'BaiduIndexPage': {'search_button': {'click': None}}},
        # {'Assert': ['in', 'github JoeEmp', '$driver.title']}
        temp = deepcopy(template)
        for step in temp:
            case.append(self.gen_step(step, data))
        return case

    def gen_step(self, step, data):
        if not data:
            return step
        if isinstance(step, dict):
            for k in step.keys():
                step[k] = self.gen_step(step[k], data)
            return step
        elif isinstance(step, list) or isinstance(step, str):
            if isinstance(step, str):
                step = [step]
            for i in range(len(step)):
                step[i] = step[i].format(**data)
            return step
        else:
            return step


class YamlCaseRunner():
    def __init__(self, case, driver, cap=None, test_case_obj=None):
        self.case = case
        self.driver = driver
        self.cap = cap
        self.test_case_obj = test_case_obj
        self.exec_case()

    def exec_case(self):
        # [
        #  {'Driver': {'get': 'https://www.baidu.com'}},
        #  {'BaiduIndexPage': {'search_input': {'send_keys': '{key}'}}},
        #  {'BaiduIndexPage': {'search_button': {'click': None}}},
        #  {'Assert': ['in', 'github JoeEmp', '$driver.title']}
        # ]
        result = None
        imp_module = importlib.import_module('page')
        for step in self.case:
            result_tuple = self.exec_step(
                step=step, result=result, imp_module=imp_module)
            if 'page' == result_tuple[0]:
                result = result_tuple[1]

    def exec_step(self, step: dict, result=None, imp_module=None, *args, **kwargs):
        """[summary]

        Args:
            step (dict): 步骤json
            result (obj): 上个执行步骤的结果. Defaults to None.
            imp_module (): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        for func, args in step.items():
            # 断言步骤
            if 'assert' == func.lower():
                return ('assert',
                        self.exec_assert_step(
                            self.test_case_obj,
                            func_args=args, 
                            driver=self.driver, 
                            result=result))
            # driver步骤
            elif 'driver' == func.lower():
                return ('driver',
                        self.exec_driver_step(
                            func_dict=args,
                            driver=self.driver, 
                            cap=self.cap))
            # 普通步骤
            else:
                page = func
                return ('page',
                        self.exec_po_step(
                            page=page, 
                            ele_dict=args,
                            imp_module=imp_module, 
                            driver=self.driver, 
                            cap=self.cap))

    def exec_assert_step(self, test_case_obj: TestCase, func_args, driver=None, result=None):
        assert_type, func_args = func_args[0], func_args[1:]
        logging.info(assert_type, func_args)
        for i in range(len(func_args)):
            if func_args[i].startswith('$result.') and result:
                func_args[i] = getattr(result, func_args[i][8:])
            elif func_args[i].startswith('$driver.') and driver:
                func_args[i] = getattr(driver, func_args[i][8:])
        if 'equal' == assert_type.lower():
            test_case_obj.assertEqual(*func_args)
        elif 'in' == assert_type.lower():
            test_case_obj.assertIn(*func_args)
        else:
            logging.warning('%s类型断言,尚未支持' % assert_type)

    def exec_po_step(self, page, ele_dict, imp_module, driver, cap):
        #  {'BaiduIndexPage': {'search_input': {'send_keys': '{key}'}}},
        #  {'BaiduIndexPage': {'search_button': {'click': None}}},
        page_class = getattr(imp_module, page)
        page_obj = page_class(driver, cap)
        for ele, fun_dict in ele_dict.items():
            ele_obj = getattr(page_obj, ele)
            for func, arg in fun_dict.items():
                func_obj = getattr(ele_obj, func)
                if arg:
                    func_obj(*arg)
                else:
                    func_obj()

    def exec_driver_step(self, driver, func_dict, cap=None):
        # {'Driver': {'get': 'https://www.baidu.com'}}
        for func_name, args in func_dict.items():
            func = getattr(driver, func_name)
            if args:
                func(*args)
            else:
                func()


def get_yaml(filename):
    with open(filename, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_suites(root_dir='cases'):
    """提供用例套件的数据和模板
    {"用例名":{"data":[],"template":[]}}
    {"用例名":{"template":[]}}
    """
    cases = {}
    for root, dirs, files in os.walk(root_dir):
        if root == root_dir:
            continue
        case_name = root.split(os.path.sep)[-1]
        cases[case_name] = {}
        for file in files:
            if not file.endswith('.yaml'):
                continue
            part = file[:-5]
            cases[case_name][part] = get_yaml(os.path.join(root, file))
    return cases


def show_cases(suites: dict):
    for suite, content in suites.items():
        if not content:
            continue
        print(suite)
        print('-'*80)
        for data in content['data']:
            print(data)
        for page, step in content['template'].items():
            print(page, step)
        print()
