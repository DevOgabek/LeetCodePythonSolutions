# Array Partition

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        count = 0
        for i in range(0, len(nums), 2):
            count += min(nums[i], nums[i+1])
        return count
        
solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))