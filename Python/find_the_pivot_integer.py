# Find the Pivot Integer

from math import sqrt

class Solution(object):
    def pivotInteger(self, n):
        x = sqrt(n * (n + 1) / 2)
        
        if x % 1 != 0:
            return -1
        else:
            return int(x)
        
solution = Solution()
print(solution.pivotInteger(8))