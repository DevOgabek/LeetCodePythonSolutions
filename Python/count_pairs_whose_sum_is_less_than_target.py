# Count Pairs Whose Sum is Less than Target

class Solution(object):
    def countPairs(self, nums, target):
        return len([None for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] + nums[j] < target])

test = Solution()
print(test.countPairs([-1,1,2,3,1], 2))