def deal_case(cases):
    new_cases = []
    for case in cases:
        case = case.rstrip('\n')
        new_cases.append(case.split(','))
    return new_cases

def read_file(filename, is_line=False, *args, **kwargs):
    with open(filename) as f:
        if is_line:
            return f.readlines()
        else:
            return f.read()