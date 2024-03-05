# Find N Unique Integers Sum up to Zero

class Solution(object):
    def sumZero(self, n):
        result = list(range(1, n))
        result.append(-sum(result))

        return result

solution = Solution()
print(solution.sumZero(5))