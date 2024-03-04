# Maximum Product Difference Between Two Pairs

class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

solution = Solution()
print(solution.maxProductDifference([5,6,2,7,4]))