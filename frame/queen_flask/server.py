from queue import Queue
from flask import Flask, request, jsonify
import random
from time import sleep
import json
from json import JSONDecodeError

index_queue = None
app = Flask(__name__)


class api_queue():
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
    sleep(random.randint(0,4))
    return {"code": 0, "result": "%s" % data['name']}


@app.route('/queue/hello', methods=["POST"])
def hello_world():
    global index_queue
    if index_queue.full():
        return jsonify(code=1, msg="服务繁忙请稍后再试")
    try:
        data = json.loads(request.get_data())
    except JSONDecodeError as e:
        print(request.get_data())
        return jsonify(code=-1, msg='参数错误')
    index_queue.put(say_hello, data)
    return index_queue.get()


def init_modules():
    global index_queue
    index_queue = api_queue()


if __name__ == "__main__":
    init_modules()
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, threaded=True)
