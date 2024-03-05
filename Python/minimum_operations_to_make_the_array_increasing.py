# Minimum Operations to Make the Array Increasing

class Solution(object):
    def minOperations(self, nums):
        operations = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                operations += prev - nums[i] + 1
                prev += 1
            else:
                prev = nums[i]

        return operations

solution = Solution()
print(solution.minOperations([1,1,1]))