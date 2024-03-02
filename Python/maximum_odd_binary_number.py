# Maximum Odd Binary Number

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        ones_count = s.count("1")
        zeros_count = len(s) - ones_count

        return "1" * (ones_count - 1) + "0" * zeros_count + "1"

solution = Solution()
print(solution.maximumOddBinaryNumber("010"))