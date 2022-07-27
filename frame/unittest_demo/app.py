
from flask import Flask, request, jsonify
from flask_cors import *
from utils import api_queue
import json
from json import JSONDecodeError
import run_all
from concurrent.futures import ThreadPoolExecutor
import logging

index_queue = None
app = Flask(__name__)
CORS(app, supports_credentials=True)
executor = None


def run_all_test():
    executor.submit(run_all.main)
    return 'star task'


@app.route('/run', methods=["POST"])
def run_test():
    global index_queue
    if index_queue.full():
        return jsonify(code=1, msg="服务繁忙请稍后再试")
    index_queue.put(run_all_test)
    return index_queue.get()


@app.route('/report/detail', methods=["POST", "GET"])
def report_detail():
    try:
        with open('jsonResult.json') as f:
            results = json.loads(f.read())
            return jsonify(code=0, list=results, total=len(results))
    except Exception as e:
        logging.error(e)
        return jsonify(code=0, list=[], total=0)


@app.route('/', methods=["POST", "GET"])
def index():
    return '<h1>hello<h1>'


def init_modules():
    global index_queue, executor
    index_queue = api_queue()
    executor = ThreadPoolExecutor(2)


if __name__ == "__main__":
    init_modules()
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, threaded=True)
