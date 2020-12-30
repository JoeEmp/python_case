# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:
# 输入: 123
# 输出: 321

#  示例 2:
# 输入: -123
# 输出: -321

# 示例 3:
# 输入: 120
# 输出: 21
# 注意:

# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

import unittest


class mytest(unittest.TestCase):
    def setUp(self):
        self.data = [
            [123, 321],
            [120, 21],
            [-123, -321],
            [2**31,0]
        ]

    def test_case(self):
        for data in self.data:
            self.assertEqual(reverse(data[0]), data[1])


def reverse(num: int):
    target_str = ''.join(list(str(num).strip('0'))[::-1])
    if num < 0:
        target_str = '-' + target_str.strip('-')
    target = int(target_str)
    if -2**31 > target or target > 2**31-1:
        return 0
    return target


if __name__ == "__main__":
    unittest.main()
