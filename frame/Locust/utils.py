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

def load_csv(filename):
    lines = [line.rstrip() for line in open(filename)]
    header = lines.pop(0).split(',')
    for i in range(len(lines)):
        accout = lines[i].split(',')
        lines[i] = dict()
        for j in range(len(header)):
            lines[i][header[j]] = accout[j]
        line = lines[i]
    return lines

def generate_index(table:list,key:str):
    if table:
         return [line[key] for line in table]


