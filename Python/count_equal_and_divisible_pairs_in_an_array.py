# Count Equal and Divisible Pairs in an Array

class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count

solution = Solution()
print(solution.countPairs([3,1,2,2,2,1,3], 2))