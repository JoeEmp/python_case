from flask import Flask
import random
from time import sleep
import logging
import os
app = Flask(__name__)


@app.route('/<username>')
def hello_user(username='world'):
    # 模拟返回缓慢
    # i = random.randint(0, 1000)
    # if i > 800:
    #     sleep(2)
    #     logging.warning('%s requests sleep 2s'%username)
    return 'Hello, %s' % username


if __name__ == "__main__":
    print(os.popen('ifconfig |grep 192').read().strip('\t'))
    app.run('0.0.0.0',debug=True, port=5000, threaded=True)
