from flask import Flask, request, jsonify
import logging
import os
from utils import generate_index,generate_account,load_csv

app = Flask(__name__)
USER_TABLE = []
USER_INDEX = []

file_dir = os.path.abspath(os.path.dirname(__file__))+os.sep

def generate_account(num, filename=''):
    import os
    file_dir = os.path.abspath(os.path.dirname(__file__))+os.sep
    filename = filename or file_dir+"locuts_account.csv"
    if os.path.exists(filename):
        return filename
    else:
        from faker import Faker
        fake = Faker()
        Faker.seed(10086)
        lines = []
        lines.append('username,password'+os.linesep)
        for i in range(num):
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
        logging.warning('system without user {}'.format(username))
        return {}
    except KeyError as e:
        logging.error('Data asymmetry {}'.format(e))
        return {}

def init_data():
    global USER_TABLE
    global USER_INDEX
    filename = generate_account(100)
    USER_TABLE = load_csv(filename)
    USER_INDEX = generate_index(USER_TABLE,'username')

def request_parse(req_data):
    '''解析请求数据并以json形式返回'''
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data

def is_legal_uer(username):
    return True if get_user(username) else False

def is_right_password(username, password):
    account = get_user(username)
    if account:
        return True if password == account['password'] else False
    else:
        return False

@app.route('/')
def index():
    return '<h1>Hello</h1>'


@app.route('/login', methods=['POST'])
def login():
    data = request_parse(request)
    try:
        username, password = data.get('username'), data.get('password')
    except Exception as e:
        print(e)
    if is_legal_uer(username):
        if is_right_password(username, password):
            logging.info('login success')
            return jsonify(msg='login success')
        else:
            logging.info('the password is error')
            return jsonify(msg='the password is error')
    else:
        return jsonify(msg='user %s is not exist' % username)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return jsonify(msg='about flask')


if __name__ == "__main__":
    init_data()
    app.config['JSON_AS_ASCII'] = False
    try:
        app.run(host='0.0.0.0',
                port=10086,
                debug=True,
                threaded=True
                )
        os.system('lsof -i:10086')
    except Exception as e:
        logging.error(e)
