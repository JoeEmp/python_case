import unittest


class mytest(unittest.TestCase):
    def setUp(self):
        self.datas = [
            # ([1,3,5,6], 5,2),
            ([1,3,5,6], 2,1),
            # ([1,3,5,6], 7,4),
            # ([1,3,5,6], 0,0),
            # ([1,3],2,1)
        ]

    def test_case(self):
        for data in self.datas:
            *args,ans = data
            print("-"*80)
            print(args,ans)
            self.assertEqual(myFunction(*args),ans)


def myFunction(nums,target):
    low,height = 0, len(nums)-1
    if nums[0] > target:
        return low
    if nums[-1] < target:
        return len(nums)
    pos = 0
    while low <= height:
        mid = int((height+low)/2)
        print("low:%d height:%d mid:%d"%(low,height,mid))
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            height, pos = mid - 1,mid
        else:
            low, pos = mid + 1, mid
    return pos

if __name__ == "__main__":
    unittest.main()
