# Count Number of Pairs With Absolute Difference K

class Solution(object):
    def countKDifference(self, nums, k):
        n = len(nums)
        return len([None for i in range(n) for j in range(i+1, n) if abs(nums[i] - nums[j]) == k])

test = Solution()
print(test.countKDifference([1,2,2,1], 1))