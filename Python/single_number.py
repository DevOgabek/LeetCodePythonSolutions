# Single Number

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

solution = Solution()
print(solution.singleNumber([2,2,1]))