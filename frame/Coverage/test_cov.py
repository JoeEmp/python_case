import os
import unittest
from coverage import Coverage
from frame.Coverage.add import add
from frame.Coverage.comm import *


class my_test(unittest.TestCase):

    def setUp(self):
        try:
            os.system('mkdir %s' % self._testMethodName)
        except Exception as e:
            print(e)
        # 这里依赖于命名规范，include指定要测试的文件
        self.cov = Coverage(include=['comm.py', '%s.py' % self._testMethodName[5:]])
        self.cov.start()
        return super().setUp()

    def test_add(self):
        with open('./add_test.txt', 'r') as f:
            cases = f.readlines()
        cases = deal_case(cases)
        for case in cases:
            result = add(case[0], case[1])
            if 0 == result['code']:
                result = result['result']
                self.assertEqual(result, float(case[2]))
            elif 1 == result['code']:
                result = result['msg']
                self.assertEqual(result, case[2])

    def tearDown(self):
        self.cov.stop()
        self.cov.save()
        self.cov.html_report(directory='%s' % self._testMethodName)
        self.cov.erase()
        return super().tearDown()


if __name__ == "__main__":
    os.chdir(__file__[:-len(__file__.split('/')[-1])])
    unittest.main()
