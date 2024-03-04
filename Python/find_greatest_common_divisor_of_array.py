# Find Greatest Common Divisor of Array

class Solution(object):
    def findGCD(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if not nums:
            return None

        smallest = min(nums)
        largest = max(nums)

        result = gcd(smallest, largest)

        return result

solution = Solution()
print(solution.findGCD([2,5,6,9,10]))