# Maximum Product of Two Elements in an Array

class Solution(object):
    def maxProduct(self, nums):
        count = 0
        n = len(nums)  
        for i in range(n):
            for j in range(i+1, n):
                count = max(count, (nums[i]-1) * (nums[j]-1))
        return count

solution = Solution()
print(solution.maxProduct([3,4,5,2]))