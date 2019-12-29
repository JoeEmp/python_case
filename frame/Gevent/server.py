'''
@Author: JoeEmp
@Date: 2019-12-29 11:53:48
@LastEditTime : 2019-12-29 15:00:46
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Gevent/server.py
'''
from flask import Flask
import random
from time import sleep
app = Flask(__name__)

@app.route('/<username>')
def hello_user(username='world'):
    # 模拟返回缓慢
    i = random.randint(0,1000)
    if i > 800:
        sleep(2)
        print('%s requests sleep 2s'%username)
    return 'Hello, %s'%username

if __name__ == "__main__":
    app.run(debug=False,port=5000)