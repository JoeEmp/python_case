# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

import unittest


class mytest(unittest.TestCase):
    def setUp(self):
        self.datas = [
            [["flower", "flow", "flight"], 'fl'],
            [["dog", "racecar", "car"], ''],
            [[], ''],
            [['', ''], ''],
            [['ad1', 'a'], 'a'],
            [['a'], 'a']
        ]

    def test_case(self):
        for data in self.datas:
            self.assertEqual(myFunction(
                data[0]), data[1], "case is %r" % data[0])


def myFunction(strs: list):
    #  32 ms 15MB
    prefix = ''
    if not strs:
        return prefix
    elif 1 == len(strs):
        return strs[0]
    strs.sort(key=lambda x: len(x))
    first_str = strs.pop(0)
    for i in range(len(first_str)):
        prefix = first_str[0:i+1]
        for s in strs:
            if not s.startswith(prefix):
                return prefix[:-1]
    return prefix


if __name__ == "__main__":
    unittest.main()
