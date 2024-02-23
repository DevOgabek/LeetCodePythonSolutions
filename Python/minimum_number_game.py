# Minimum Number Game

class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        for i in range(0, len(nums), 2):
            num = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = num
        return nums

test = Solution()
print(test.numberGame([5,4,2,3]))