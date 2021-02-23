import os
import json
import re
import requests
from settings import apk_install_path, COMMAND_EXECUTOR_URL
import logging
from appium import webdriver


class DrviceError(BaseException):
    def __init__(self, reason, *args, **kwargs):
        self.reason = reason
        super().__init__(*args, **kwargs)


class ConfigError(BaseException):
    def __init__(self, reason, *args, **kwargs):
        self.reason = reason
        super().__init__(*args, **kwargs)


class TestDriver():
    """自动生成构建driver """

    def __init__(self, desired_caps=None):
        self.desired_caps = desired_caps or self.init_desired_caps()
        self.init_driver()
        print('desired_caps config')
        print(self.desired_caps)
        print('-'*80)

    def init_desired_caps(self):
        desired_caps = self.load_desired_caps()
        self.check_pkg(desired_caps['appPackage'])
        return desired_caps

    def init_driver(self):
        self.driver = driver = webdriver.Remote(
            COMMAND_EXECUTOR_URL, self.desired_caps)

    @staticmethod
    def get_devices_list():
        """获取adb连接设备. """
        devices_list = []
        readlines = os.popen("adb devices").read().splitlines()
        for i in range(len(readlines)):
            if "List" in readlines[i]:
                break
        readlines = [line for line in readlines[i+1:] if line]
        if 0 == len(readlines):
            raise DrviceError('not devices connect')
        for i in readlines:
            deviceName, status = i.split("\t")
            devices_list.append(deviceName)
        return devices_list

    @staticmethod
    def get_desired_caps():
        """获取当前包名和设备信息. """
        deviceName = get_devices_list()[0]
        r = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
        appPackage, appActivity = r.strip().split(" ")[-1].split("/")
        appActivity = appActivity[:-1]
        version = os.popen(
            "adb shell getprop ro.build.version.release").read().strip()
        if int(version) >= 7:
            automationName = "UIAutomator2"
        return {
            "platformName": "Android",
            "platformVersion": version,
            "deviceName": deviceName,
            "appPackage": appPackage,
            "appActivity": appActivity,
            "automationName": automationName,
            "noReset": True,
            'fullReset': False,
        }

    @staticmethod
    def check_connect_device(deviceName):
        """检验设备连接是否正常. """
        devices_list = TestDriver.get_devices_list()
        if deviceName in devices_list:
            return deviceName
        elif len(devices_list) > 0:
            return devices_list[0]
        else:
            return ''

    @staticmethod
    def get_pkg_list():
        """获取用户安装包名. """
        lines = os.popen('adb shell pm list packages').read().split(os.linesep)
        lines = [line for line in lines if line]
        if not lines:
            raise DrviceError('not devices connect')
        return lines

    @staticmethod
    def load_desired_caps(use_cur=False, filename='desired_caps.json'):
        """加载配置文件或者获取当前设置配置."""
        desired_caps = {}
        try:
            with open(filename) as f:
                desired_caps = json.loads(f.read())
            desired_caps['deviceName'] = TestDriver.check_connect_device(
                desired_caps['deviceName'])
        except json.JSONDecodeError as e:
            raise ConfigError('json格式错误,请检查json,可以删除json或手动修复解决改问题')
        except FileNotFoundError as e:
            desired_caps = TestDriver.get_desired_caps()
            with open(filename, 'w') as f:
                f.write(json.dumps(desired_caps))
        return desired_caps

    @staticmethod
    def install_apk(apk_path, filename=''):
        pattern = '(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
        searchObj = re.search(pattern, apk_path, flags=0)
        url = searchObj.group() if searchObj else ''
        if url:
            apk_path = url.split(os.sep)[-1]
            r = requests.post(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
        result = os.popen('adb install -r %s' % apk_path).read()
        print(result)

    @staticmethod
    def check_pkg(appPackage):
        pkgs = TestDriver.get_pkg_list()
        if 0 == len(pkgs):
            raise DrviceError('drviec not connect')
        for pkg in pkgs:
            if appPackage in pkg:
                return appPackage
        logging.warning(
            'test package not install the devies use apk_install_path install.')
        TestDriver.install_apk(apk_install_path)


if "__main__" == __name__:
    TestDriver.check_pkg('ee.dustland.android.dustlandsudoku')
