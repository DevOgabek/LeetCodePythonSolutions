# Divide Array Into Equal Pairs

class Solution(object):
    def divideArray(self, nums):
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for count in counts.values():
            if count % 2 != 0:
                return False
            
        return True
    
solution = Solution()
print(solution.divideArray([3,2,3,2,2,2]))