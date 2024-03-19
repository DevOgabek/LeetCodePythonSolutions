# Find the Distinct Difference Array

class Solution(object):
    def distinctDifferenceArray(self, nums):
        diff = []
        
        for i in range(len(nums)):
            prefix = len(set(nums[:i+1]))
            surfix = len(set(nums[i+1:]))
            diff.append(prefix-surfix)

        return diff
    
solution = Solution()
print(solution.distinctDifferenceArray([1,2,3,4,5]))