# Difference Between Element Sum and Digit Sum of an Array

class Solution(object):
    def differenceOfSum(self, nums):
        return sum(nums) - sum([int(s) for num in nums for s in str(num)])

test = Solution()
print(test.differenceOfSum())