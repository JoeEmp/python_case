# 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import unittest


class mytest(unittest.TestCase):
    def setUp(self):
        self.data = [2, 7, 11, 15]

    def test_case1(self):
        target = 9
        self.assertEqual([0, 1], find_target_num(self.data, target))


# 暴力穷举
def find_target_num(nums: list, target):
    num_len = len(nums)
    for i in range(num_len):
        for j in range(i+1, num_len):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# 双指针
def twoSum(nums: list, target: int) -> list:
    temp = nums.copy()
    temp.sort()
    i = 0
    j = len(nums)-1
    while i < j:
        if (temp[i]+temp[j]) > target:
            j = j-1
        elif (temp[i]+temp[j]) < target:
            i = i+1
        else:
            break
    p = nums.index(temp[i])
    nums.pop(p)
    k = nums.index(temp[j])
    if k >= p:
        k = k+1
    return [p, k]


if __name__ == "__main__":
    unittest.main()
