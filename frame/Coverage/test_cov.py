import os
import unittest
from coverage import Coverage
from add import add
from comm import deal_case, read_file


class my_test(unittest.TestCase):

    def setUp(self):
        if not os.path.exists(self._testMethodName):
            os.system('mkdir %s' % self._testMethodName)
        # 这里依赖于命名规范，include指定要测试的文件
        if self._testMethodName.startswith("test_"):
            include_name = self._testMethodName[5:]
        self.cov = Coverage(
            include=['comm.py', '%s.py' % include_name])
        self.cov.start()
        return super().setUp()

    def test_add(self):
        cases = deal_case(read_file("add_test.txt", is_line=True))
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
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    unittest.main()
