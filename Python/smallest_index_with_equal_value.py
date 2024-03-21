# Smallest Index With Equal Value

class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1
    
solution = Solution()
print(solution.smallestEqual([0,1,2]))