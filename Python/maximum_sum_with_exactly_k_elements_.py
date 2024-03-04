# Maximum Sum With Exactly K Elements 

class Solution(object):
    def maximizeSum(self, nums, k):
        nums.sort()
        count = 0
        for i in range(k):
            count += nums[-1]
            nums[-1] = nums[-1] + 1
        return count

solution = Solution()
print(solution.maximizeSum([1,2,3,4,5], 3))