import os
from time import sleep
import json
import urllib3
from settings import *
from com import *

def main():
    try:
        driver = TestDriver().driver
        driver.implicitly_wait(10)
        driver.find_element_by_id(
            'ee.dustland.android.dustlandsudoku:id/main_start_game_button').click()
        sleep(0.5)
        driver.find_element_by_id(
            'ee.dustland.android.dustlandsudoku:id/prompt_positive_button').click()
        sleep(0.5)
        driver.tap([(653, 1488), (654, 1489)], 500)
        sleep(0.5)
        driver.get_screenshot_as_file('tap.png')
        if not is_debug:
            driver.quit()
    except DrviceError as e:
        logging.error(e.reason)
    except ConfigError as e:
        logging.error(e.reason)
    except urllib3.exceptions.MaxRetryError as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)
        reset()

def reset():
    desired_caps = {'deviceName': TestDriver.check_connect_device(
        ''), 'platformName': 'Android'}
    driver = webdriver.Remote(COMMAND_EXECUTOR_URL, desired_caps)
    driver.quit()


if "__main__" == __name__:
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'reset':
        reset()
    else:
        main()
