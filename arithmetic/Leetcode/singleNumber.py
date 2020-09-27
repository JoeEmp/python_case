# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution():
    def singleNumber(self, nums: list) -> int:
        if not nums:
            return None
        if 1 == len(nums):
            return nums[0]
        count = dict()
        for num in nums:
            try:
                count[num] += 1
            except:
                count[num] = 1
        for i in count:
            if 1 == count[i]:
                return i

    # 优解
    def singleNumber_xor(self, nums):
        if not nums:
            return None
        if 1 == len(nums):
            return nums[0]
        ans = nums[0] ^ nums[1]
        for i in range(2, len(nums)):
            ans = ans ^ nums[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    ret = s.singleNumber([1, 22, 22, 1, 589])
    print(ret)
    ret = s.singleNumber_xor([1, 22, 22, 1, 589])
    print(ret)
