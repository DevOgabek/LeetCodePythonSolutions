# Neither Minimum nor Maximum

class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1
        
        sorted_nums = sorted(nums)
        return sorted_nums[1]

solution = Solution()
print(solution.findNonMinOrMax([3,2,1,4]))