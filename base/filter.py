'''
测试了一些筛选的写法的性能
期间发现修饰器影响了对函数性能的评估，所以后面注释掉了。
原生的filter函数性能十分之高。
'''

import copy
import time
from memory_profiler import profile


def get_run_time(fun):
    def wrapper(num):
        start = time.time()
        fun(num)
        end = time.time() - start
        print(end)

    return wrapper


# @profile # 用于查看内存的使用情况
# @get_run_time
def filter_1(num):
    '''
    使用了深拷贝，拷贝了数据。结果时间十分漫长。应该是拷贝所造成的
    :param num:
    :return:
    '''
    o_list = [i for i in range(num)]
    for i in copy.deepcopy(o_list):
        if i % 2 == 0:
            o_list.remove(i)


# @profile
# @get_run_time
def filter_2(num):
    '''
    使用了标记，标记了每个筛选的数字。然后筛选，效率很低。
    :param num:
    :return:
    '''
    marks = []
    o_list = [i for i in range(num)]
    for i in o_list:
        if i % 2 == 0:
            marks.append(i)
    for i in marks:
        o_list.remove(i)


# @profile
# @get_run_time
def filter_3(num):
    '''
    仿c的一种写法。在c中for的处理机制不同我会在完成某些操作然后变更i。
    python中，每次for都会重新赋值i，同时for的可迭代对象不可短长度。
    故此加入了偏置，防止越界
    :param num:
    :return:
    '''
    o_list = [i for i in range(num)]
    offset = 0
    for i in range(len(o_list)):
        if o_list[i + offset] % 2 == 0:
            o_list.remove(i + offset)
            offset -= 1


# @profile
# @get_run_time
def filter_4(num):
    '''
    使用filter原生方法,速度相当的快
    :param num:
    :return:
    '''
    o_list = [i for i in range(num)]
    return filter(filter_list, o_list)


def filter_list(num):
    if num % 2 != 0:
        return num
    else:
        return None


if __name__ == "__main__":
    for i in range(3):
        # start = time.time()
        # filter_1(100000)
        # print(time.time() - start)
        # start = time.time()
        # filter_2(100000)
        # print(time.time() - start)
        # start = time.time()
        # # start = time.time()
        # filter_3(100000)
        # print(time.time() - start)
        start = time.time()
        l = list(filter_4(100000))
        print(l[0:5])
        print(time.time() - start)
        print('-' * 20)

'''
效率对比
19.59002423286438    19秒
23.484858989715576   23秒
1.0671992301940918   1秒
0.005151033401489258 50毫秒
--------------------
28.62985110282898
28.572277069091797
1.144117832183838
0.006360054016113281
--------------------
'''