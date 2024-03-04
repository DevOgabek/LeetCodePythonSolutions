# N-Repeated Element in Size 2N Array

class Solution(object):
    def repeatedNTimes(self, nums):
        count = {}
        n = len(nums) // 2

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] == n:
                return num

solution = Solution()
print(solution.repeatedNTimes([1,2,3,3]))