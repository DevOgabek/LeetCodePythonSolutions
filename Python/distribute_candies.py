# Distribute Candies

class Solution(object):
    def distributeCandies(self, candyType):
        unique_candies = len(set(candyType))
        max_candies = min(unique_candies, len(candyType) // 2)
        
        return max_candies
    
solution = Solution()
print(solution.distributeCandies([1,1,2,2,3,3]))