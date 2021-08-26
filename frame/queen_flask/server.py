from queue import Queue
import random
from time import sleep
import json
from json import JSONDecodeError
from flask import Flask, request, jsonify


INDEX_QUEUE = None
APP = Flask(__name__)


class ApiQueue():
    def __init__(self, max_size=2):
        self.queue = Queue(max_size)

    def __len__(self):
        return self.queue.qsize()

    def put(self, func, *args, **kwargs):
        block = kwargs.pop("block", True)
        timeout = kwargs.pop("timeout", None)
        self.queue.put((func, args, kwargs), block=block, timeout=None)

    def get(self, *args, **kwargs):
        func, args, kwargs = self.queue.get(*args, **kwargs)
        return func(*args, **kwargs)

    def full(self):
        return self.queue.full()

    def empty(self):
        return self.queue.empty()


def say_hello(data):
    sleep(random.randint(0, 4))
    return {"code": 0, "result": "%s" % data['name']}


@APP.route('/queue/hello', methods=["POST"])
def hello_world():
    global INDEX_QUEUE
    if INDEX_QUEUE.full():
        return jsonify(code=1, msg="服务繁忙请稍后再试")
    try:
        data = json.loads(request.get_data())
    except JSONDecodeError:
        print(request.get_data())
        return jsonify(code=-1, msg='参数错误')
    INDEX_QUEUE.put(say_hello, data)
    return INDEX_QUEUE.get()


def init_modules():
    global INDEX_QUEUE
    INDEX_QUEUE = ApiQueue()


if __name__ == "__main__":
    init_modules()
    APP.config['JSON_AS_ASCII'] = False
    APP.run(debug=True, threaded=True)
