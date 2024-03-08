# Maximum Strong Pair XOR I

class Solution(object):
    def maximumStrongPairXor(self, nums):
        xor = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                x = nums[i]
                y = nums[j]
                if abs(x - y) <= min(x, y) and x ^ y > xor:
                    xor = x ^ y
        return xor

solution = Solution()
print(solution.maximumStrongPairXor([1,2,3,4,5]))