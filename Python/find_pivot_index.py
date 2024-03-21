# Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            
        return -1
        
solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))