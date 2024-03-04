# Height Checker

class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        
        count = sum(1 for i in range(len(heights)) if heights[i] != expected[i])
        
        return count

solution = Solution()
print(solution.heightChecker([1,1,4,2,1,3]))