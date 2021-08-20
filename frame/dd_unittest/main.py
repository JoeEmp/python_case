from com.sync_case import YamlCaseManager, YamlCaseRunner
from unittest import TestCase
from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from copy import deepcopy
from collections import deque


class MyListener(AbstractEventListener):
    def after_click(self, url, driver):
        sleep(0.5)


class TestALL(TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        ef_driver = EventFiringWebDriver(driver, MyListener())
        self.driver = ef_driver
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


def main():
    ym = YamlCaseManager()
    length = len(ym.all_cases)
    q = deque(ym.all_cases)

    def func(self):
        case_name, case = q.popleft()
        YamlCaseRunner(
            case,
            self.driver,
            test_case_obj=self
        )
    for i in range(length):
        setattr(TestALL, 'test_%s' % i, func)
    unittest.main()


if "__main__" in __name__:
    main()
