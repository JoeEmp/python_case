# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import unittest
import logging
import time

# 题解
"""
假设有数组 a,b,c,d....
sum,max = 0,0
if a+b>a:
    b > 0
else:
    b <= 0
if b = 0:
    a+b+c > a+b 类推
else:
    b + c > b
"""

class Solution():
    @staticmethod
    def maxSubArray(l: list):
        length = len(l)
        if not l or 1 == length:
            return None
        SubArray = [l[l.index(max(l))]]
        maxSum = max(l)
        for i in range(length):
            for j in range(i+1, length):
                if maxSum <= sum(l[i:j+1]):
                    maxSum = sum(l[i:j+1])
                    SubArray = l[i:j+1]
        return (maxSum, SubArray)

    # 优解
    @staticmethod
    def maxSubArray2(l: list):
        max_, sum_ = l[0], l[0]
        for n in l[1:]:
            sum_ = sum_ + n if sum_ >= 0 else n
            max_ = max_ if max_ > sum_ else sum_  # 比max快点?
        return (max_, list())


class MyTest(unittest.TestCase):
    def test_maxSubArray(self):
        cases = [
            {"list": [-2, 1, -3, 4, -1, 2, 1, -5, 4], 'result':6},
            {"list": [-2, -5, -4, -3, -1], 'result':-1},
            {"list": [0,0,0], 'result':0}
        ]
        for case in cases:
            start_time = time.time()
            try:
                self.assertEqual(Solution.maxSubArray2(
                    case['list'])[0], case['result'])       
            except AssertionError:
                logging.error(' {} != {} case fail {}'.format(
                    Solution.maxSubArray(case['list'])[0], case['result'], case))
            print('pass case {} use {:.3f} s'.format(
                case, (time.time()-start_time) * 1000))


if __name__ == "__main__":
    unittest.main()
