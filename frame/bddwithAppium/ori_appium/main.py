from appium import webdriver
import json
import unittest
import selenium
# from ha
from time import sleep

# 多关注于展示，数据类交给接口。

class autoError(BaseException):
    def __init__(self, reason: str, *args, **kwargs):
        self.reason = reason
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.reason)


def element_not_found(func, *args):
    def wrapper_func(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except selenium.common.exceptions.NoSuchElementException:
           AssertionError('element not found')
    return wrapper_func


class ApiDemo(unittest.TestCase):

    @staticmethod
    def LoadStartCap(filename: str) -> dict:
        try:
            with open(filename) as f:
                return json.loads(f.read())
        except FileNotFoundError:
            print('file not Found')
        except json.JSONDecodeError:
            print('file content is not josn')
        return {}

    def setUp(self):
        filename = './desired_caps.json'
        self.cap = self.LoadStartCap(filename)
        if not self.cap:
            raise autoError('without caps start fail')
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.cap)
        self.driver.implicitly_wait(20)  # 大型测试时间为15分钟强制结束。900

    # @element_not_found
    # def test_toast(self):
    #     self.driver.find_element_by_accessibility_id('Views').click()
    #     self.driver.find_element_by_accessibility_id('AAA').click()
    #     if self.cap['platformName'].lower() == 'android':
    #         # 滚动控件滚动到对应元素
    #         # https://appium.io/docs/en/writing-running-appium/android/uiautomator-uiselector/index.html
    #         self.driver.find_element_by_android_uiautomator(
    #             'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));'
    #         ).click()
    #     else:
    #         self.driver.swipe()
    #         self.driver.find_element_by_accessibility_id('Popup Menu').click()
    #     self.driver.find_element_by_accessibility_id('Make a Popup!').click()
    #     self.driver.find_element_by_xpath('//*[@text="Search"]').click()
    #     text = self.driver.find_element_by_xpath(
    #         '//*[@class="android.widget.Toast"]').text
    #     self.assertIn('Search', text)

    def test_webview(self):
        # myWebView.setWebContentsDebuggingEnabled(true);
        # self.driver.find_element_by_accessibility_id
        self.driver.find_element_by_xpath("//*[@text='选课']").click()
        self.driver.find_element_by_xpath("//*[@text='正价课精品推荐']").click()
        for i in range(5):
            sleep(1)
            print(self.driver.contexts)

    def tearDown(self):
        self.driver.quit()


if "__main__" in __name__:
    unittest.main()
