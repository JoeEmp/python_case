def add(a, b):
    # 转成浮点数
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return {'code': 1, 'msg': '参数类型错误'}
    result = a + b
    return {"code": 0, "msg": '成功', "result": result}