import random
import time
import requests
import gevent
from gevent import Timeout, monkey

monkey.patch_all()

TIMER = Timeout(1)
TIMER.start()


def get_data(num, begin=0, **kwargs):
    """

    Arguments:
        num {[int} -- 获取数量

    Yields:
        [str] -- 用户名
    """
    if 'filename' not in kwargs:
        kwargs['filename'] = ''
    try:
        with open(kwargs['filename'], 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if i < begin:
                    continue
                yield lines[i]
    except IndexError:
        print('文件内容不足，使用随机生成名字')
        for i in range(len(lines), num):
            yield make_name()
    except FileNotFoundError:
        for i in range(num):
            yield make_name()


def make_name(length=4):
    s = ''
    for i in range(len):
        if 0 == i:
            s += chr(random.randrange(65, 65+26))
        else:
            s += chr(random.randrange(97, 97+26))
    print('生成name：', s)
    return s


def make_data(num, filename):
    with open(filename, 'w') as f:
        for _ in range(num):
            f.write(make_name+'\n')
        f.close()


def req(name):
    return requests.get('http://localhost:5000/%s' % name)


def erupt_get_hello(num, **kwargs):
    if 'filename' not in kwargs:
        kwargs['filename'] = ''
        begin_time = time.time()
    # 异步模式
    run_gevent_list = []
    for name in get_data(num):
        run_gevent_list.append(gevent.spawn(req, name))
    try:
        gevent.joinall(run_gevent_list, timeout=TIMER)
    except Timeout:
        print('返回超时')
    # 同步处理查看哪一次请求返回缓慢，但是速度慢
    # for name in get_data(num):
    #     try:
    #         gevent.spawn(req,name).join(timeout=timer)
    #         # gevent.joinall(run_gevent_list,timeout=timer)
    #     except Timeout:
    #         print('%s 返回超时'%name)
    end = time.time()
    print('单次测试时间（平均）s:', (end - begin_time) / num)
    print('累计测试时间 s:', end - begin_time)


if __name__ == "__main__":
    erupt_get_hello(100)
