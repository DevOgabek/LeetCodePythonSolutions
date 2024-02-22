# Sum of Values at Indices With K Set Bits

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        return sum([nums[i] for i in range(len(nums)) if bin(i)[2:].count('1') == k])

test = Solution()
print(test.sumIndicesWithKSetBits([5,10,1,5,2], 1))