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
            ['(123)', True],
            ["()[]{}", True],
            ["(]", False],
            ['([)]', False],
            ['{[]}', True],
            ['', True],
            ['(', False],
            [']', False],
        ]

    def test_case(self):
        for data in self.datas:
            self.assertEqual(isValid(
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
            end_char_indexs = [sub_s.find(
                '}'), sub_s.find(')'), sub_s.find(']')]
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


def isValid(s: str) -> bool:
    # jyd
    dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
    l = ['{','}','[',']','(',')']
    stack = ['?']
    for c in s:
        if c not in l:
            continue
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c: 
            return False 
    return len(stack) == 1

if __name__ == "__main__":
    # unittest.main()
    # print(myFunction('(233)'))
    # min([])