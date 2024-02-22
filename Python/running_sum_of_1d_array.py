# Running Sum of 1d Array

class Solution(object):
    def runningSum(self, nums):
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            nums[i] = count
        return nums

test = Solution()
print(test.runningSum([1,2,3,4]))