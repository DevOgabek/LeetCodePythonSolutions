# Find Numbers with Even Number of Digits

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count 

solution = Solution()
print(solution.findNumbers([12,345,2,6,7896]))