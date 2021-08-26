import os
from faker import Faker


def generate_account(num, filename=''):
    file_dir = os.path.abspath(os.path.dirname(__file__))+os.sep
    filename = filename or file_dir+"locuts_account.csv"
    if not os.path.exists(filename):
        fake = Faker()
        Faker.seed(10086)
        lines = []
        lines.append('username,password'+os.linesep)
        for _ in range(num):
            lines.append(fake.free_email()+','+fake.ean8()+os.linesep)
        with open(filename, 'w') as f:
            f.writelines(lines)
    return filename


def load_csv(filename):
    lines = [line.rstrip() for line in open(filename)]
    header = lines.pop(0).split(',')
    for i in range(len(lines)):
        accout = lines[i].split(',')
        lines[i] = dict()
        for j in range(len(header)):
            lines[i][header[j]] = accout[j]
    return lines


def generate_index(table: list, key: str):
    result = []
    if table:
        result = [line[key] for line in table]
    return result
