# Sum of Squares of Special Elements 

class Solution(object):
    def sumOfSquares(self, nums):
        square_sum = 0
        n = len(nums)
        for i in range(1, n+1):
            if n % i == 0:
                square_sum += nums[i-1] ** 2
        return square_sum

solution = Solution()
print(solution.sumOfSquares([1,2,3,4]))