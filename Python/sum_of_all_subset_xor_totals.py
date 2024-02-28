# Sum of All Subset XOR Totals

class Solution(object):
    def subsetXORSum(self, nums):
        total_sum = 0
        n = len(nums)

        for mask in range(1 << n):
            xor_subset = 0
            for i in range(n):
                if (mask >> i) & 1:
                    xor_subset ^= nums[i]
            total_sum += xor_subset

        return total_sum

test = Solution()
print(test.subsetXORSum([5,1,6]))