# Number of Unequal Triplets in Array

class Solution(object):
    def unequalTriplets(self, nums):
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
                        
        return count
    
solution = Solution()
print(solution.unequalTriplets([4,4,2,4,3]))