# Sum of All Odd Length Subarrays

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            total_sum += ((i + 1) * (n - i) + 1) // 2 * arr[i]

        return total_sum

test = Solution()
print(test.sumOddLengthSubarrays([1,4,2,5,3]))