# Apply Operations to Make Sum of Array Greater Than or Equal to k

import math

class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        
        ans = float('inf')
        for i in range(1, (k // 2) + 1):
            temp = math.ceil(k / i)
            m = (i - 1) + (temp - 1)
            ans = min(m, ans)
        
        return ans
    
solution = Solution()
print(solution.minOperations(11))