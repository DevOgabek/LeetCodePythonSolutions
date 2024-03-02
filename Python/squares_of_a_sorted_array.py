# Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, nums):
        squares = [num * num for num in nums]
        squares.sort()
        return squares

solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))