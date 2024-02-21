# Build Array from Permutation

class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]

test = Solution()
print(test.buildArray([0,2,1,5,3,4]))