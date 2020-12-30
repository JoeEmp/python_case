# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import unittest


class mytest(unittest.TestCase):
    def setUp(self):
        # self.part = {"(": ")", "[": "]", "{": "}", "": ''}
        self.datas = [
            # ['()', True],
            # ["()[]{}", True],
            # ["(]", False],
            # ['([)]', False],
            # ['{[]}', True],
            # ['', True],
            ['(', False],
            [']', False],
        ]

    def test_case(self):
        for data in self.datas:
            self.assertEqual(myFunction(
                data[0]), data[1], "case is %r" % data[0])


def myFunction(s: str):
    # 292ms 130.3MB 我是傻逼
    part = {"(": ")", "[": "]", "{": "}", "": ''}
    if not s:
        return True
    else:
        try:
            begin_char_indexs = [s.rfind('{'), s.rfind('('), s.rfind('[')]
            begin_char_index = max([i for i in begin_char_indexs if i >= 0])
            begin_char = s[begin_char_index]
            sub_s = s[begin_char_index+1:]
            end_char_indexs = [sub_s.find('}'), sub_s.find(')'), sub_s.find(']')]
            end_char_index = min([i for i in end_char_indexs if i >= 0])
            target_char_index = sub_s.find(part[begin_char])
        except Exception as e:
            return False
        if target_char_index != end_char_index:
            return False
        else:
            list_s = list(s)
            list_s[begin_char_index] = ''
            list_s[end_char_index+begin_char_index+1] = ''
            return myFunction(''.join(list_s))

def otherFunction(s:str):
    # wings-kbftQ3BYHH wings 2018-11-29
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''

if __name__ == "__main__":
    unittest.main()
    # print(myFunction('(233)'))
    # min([])