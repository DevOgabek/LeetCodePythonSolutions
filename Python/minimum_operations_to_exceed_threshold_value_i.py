# Minimum Operations to Exceed Threshold Value I

class Solution(object):
    def minOperations(self, nums, k):
        return sum(n < k for n in nums)

solution = Solution()
print(solution.build_array())