# Separate the Digits in an Array

class Solution(object):
    def separateDigits(self, nums):
        return [int(digit) for num in nums for digit in str(num)]

solution = Solution()
print(solution.separateDigits([13,25,83,77]))