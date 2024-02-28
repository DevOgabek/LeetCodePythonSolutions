# Subarrays Distinct Element Sum of Squares I

class Solution(object):
    def sumCounts(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                count += len(set(nums[i:j+1])) ** 2

        return count

test = Solution()
print(test.sumCounts([1,2,1]))