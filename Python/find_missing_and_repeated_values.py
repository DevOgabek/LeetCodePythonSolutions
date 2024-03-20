# Find Missing and Repeated Values

from collections import Counter

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        nums = []
        
        for row in grid:
            nums.extend(row)
            
        counted_nums = Counter(nums)
        repeating = None
        
        for num in counted_nums:
            if counted_nums[num] == 2:
                repeating = num
                break
        
        missing = None
        for num in range(1, n*n + 1):
            if num not in counted_nums:
                missing = num
                break
        
        return [repeating, missing]
    
solution = Solution()
print(solution.findMissingAndRepeatedValues([[1,3],[2,2]]))