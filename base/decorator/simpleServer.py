'''
@Author: your name
@Date: 2020-03-18 22:34:38
@LastEditTime: 2020-03-20 09:17:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /base/decorator/simpleServer.py
'''
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/ContributorList')
def ContributorList():
    if request.form.get("test"):
        return 'By joe & winn'
    else:
        return 'Not Found', 404


if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(port=5000)
