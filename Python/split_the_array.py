# Split the Array

class Solution(object):
    def isPossibleToSplit(self, nums):
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] >= 3:
                return False
        
        return True
        
solution = Solution()
print(solution.isPossibleToSplit([1,1,2,2,3,4]))