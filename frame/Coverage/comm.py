def deal_case(cases):
    new_cases = []
    for case in cases:
        case = case.replace('\n', '')
        new_cases.append(case.split(','))
    # print(new_cases)
    return new_cases