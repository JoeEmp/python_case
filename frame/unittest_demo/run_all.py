import unittest
from JsonTestRunner import JosnTestResult, JosnTestRunner
import os


def main(filename='jsonResult.json'):
    tests_case_path = os.path.abspath(os.path.dirname(__file__))+os.sep+'tests'
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    all_cases = loader.discover(start_dir=tests_case_path, pattern='test_*.py')
    suite.addTests(all_cases)
    runner = JosnTestRunner(
        verbosity=2, descriptions='auto_test', filename=filename)
    runner.run(suite)


if '__main__' in __name__:
    main()
