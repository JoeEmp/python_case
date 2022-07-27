from unittest import TextTestResult, TextTestRunner
from unittest.util import strclass
import json


class JosnTestResult(TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.jsonResult = []
        self.showAll = True
        separator2 = ''

    def startTest(self, test):
        super(TextTestResult, self).startTest(test)
        if self.showAll:
            self.jsonResult.append(
                {
                    'testMethodName': test._testMethodName,
                    'case': strclass(test.__class__)
                })

    def addSuccess(self, test):
        self.jsonResult[-1]['status'] = 'success'

    def addError(self, test, err):
        self.jsonResult[-1]['status'] = 'error'
        self.jsonResult[-1]['msg'] = self._exc_info_to_string(err, test)

    def addFailure(self, test, err):
        self.jsonResult[-1]['status'] = 'fail'
        self.jsonResult[-1]['msg'] = self._exc_info_to_string(err, test)

    def addSkip(self, test, reason):
        self.jsonResult[-1]['status'] = 'skip'
        self.jsonResult[-1]['msg'] = reason

    def addExpectedFailure(self, test, err):
        self.jsonResult[-1]['status'] = 'expected failure'
        self.jsonResult[-1]['msg'] = self._exc_info_to_string(err, test)

    def addUnexpectedSuccess(self, test, err):
        self.jsonResult[-1]['status'] = 'unexpected success'

    def printErrors(self):
        pass


class JosnTestRunner(TextTestRunner):
    def __init__(self, stream=None, descriptions=True, verbosity=1, failfast=False,
                 buffer=False, resultclass=JosnTestResult, warnings=None, tb_locals=False, filename='jsonResult.json', *args):
        super().__init__(stream=stream, descriptions=descriptions, verbosity=verbosity,
                         failfast=failfast, buffer=buffer, resultclass=resultclass, warnings=warnings, tb_locals=tb_locals)
        self.filename = filename

    def run(self, test):
        result = super().run(test)
        with open(self.filename, 'w') as f:
            f.write(json.dumps(result.jsonResult, ensure_ascii=False,
                               sort_keys=True, indent=4, separators=(',', ': ')))
