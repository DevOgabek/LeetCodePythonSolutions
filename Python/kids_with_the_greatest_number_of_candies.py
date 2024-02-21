# Kids With the Greatest Number of Candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = [kid_candies + extraCandies >= max_candies for kid_candies in candies]
        return result

test = Solution()
print(test.kidsWithCandies([2,3,5,1,3], 3))