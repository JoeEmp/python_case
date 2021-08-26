import random
from time import sleep
from flask import Flask
APP = Flask(__name__)


@APP.route('/<username>')
def hello_user(username='world'):
    # 模拟返回缓慢
    i = random.randint(0, 1000)
    if i > 800:
        sleep(2)
        print('%s requests sleep 2s' % username)
    return 'Hello, %s' % username


if __name__ == "__main__":
    APP.run(debug=False, port=5000)
