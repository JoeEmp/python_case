import logging
import os
from flask import Flask, request, jsonify
from utils import generate_index, load_csv

APP = Flask(__name__)
USER_TABLE = []
USER_INDEX = []

def generate_account(num, filename=''):
    file_dir = os.path.abspath(os.path.dirname(__file__))+os.sep
    filename = filename or file_dir + "locuts_account.csv"
    if not os.path.exists(filename):
        from faker import Faker
        fake = Faker()
        Faker.seed(10086)
        lines = []
        lines.append('username,password'+os.linesep)
        for _ in range(num):
            lines.append(fake.free_email()+','+fake.ean8()+os.linesep)
        with open(filename, 'w') as f:
            f.writelines(lines)
    return filename



def get_user(username):
    global USER_TABLE
    global USER_INDEX
    try:
        return USER_TABLE[USER_INDEX.index(username)]
    except ValueError as e:
        logging.warning('system without user %s' % (username))
        return {}
    except KeyError as e:
        logging.error('Data asymmetry %s' % (e))
        return {}


def init_data():
    global USER_TABLE
    global USER_INDEX
    filename = generate_account(1000)
    USER_TABLE = load_csv(filename)
    USER_INDEX = generate_index(USER_TABLE, 'username')


def request_parse(req_data):
    '''解析请求数据并以json形式返回'''
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


def is_legal_uer(username):
    return bool(get_user(username))



def is_right_password(username, password):
    account = get_user(username)
    result = False
    if account:
        result = bool(password == account['password'])
    return result


@APP.route('/')
def index():
    return '<h1>Hello</h1>'


@APP.route('/login', methods=['POST'])
def login():
    msgs = {
        "success": "login success",
        "pwd_error": "the password is error",
        "not_exist": "user {username} is not exist"
    }
    msg_param = {}
    data = request_parse(request)
    try:
        username, password = data.get('username'), data.get('password')
        logging.warning('user:{},pwd:{}'.format(username, password))
    except Exception as e:
        print(e)
        return jsonify(msg='params error')
    if is_legal_uer(username):
        if is_right_password(username, password):
            logging.info('login success')
            key = 'success'
        else:
            logging.info('the password is error')
            key = 'pwd_error'
    else:
        key, msg_param['username'] = 'not_exist', username
    return jsonify(msg=msgs[key])


@APP.route('/about', methods=['GET', 'POST'])
def about():
    return jsonify(msg='about flask')

@app.route('/jmeter/app/good/list',methods=['GET', 'POST'])
def good_list():
    return jsonify(
        code=0,
        list=['python3 base','python3 flask']
    )

if __name__ == "__main__":
    init_data()
    APP.config['JSON_AS_ASCII'] = False
    try:
        APP.run(host='0.0.0.0',
                port=10086,
                debug=False,
                threaded=True
                )
        os.system('lsof -i:10086')
    except Exception as e:
        logging.error(e)
