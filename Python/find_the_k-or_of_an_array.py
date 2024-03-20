# Find the K-or of an Array

class Solution(object):
    def findKOr(self, nums, k):
        result = 0
        
        for i in range(31, -1, -1):
            count = 0
            for num in nums:
                if num & (1 << i):
                    count += 1
            if count >= k:
                result |= (1 << i)
        
        return result
    
solution = Solution()
print(solution.findKOr([7,12,9,8,9,15], 4 ))