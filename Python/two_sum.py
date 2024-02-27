# Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]

            num_indices[num] = i

test = Solution()
print(test.twoSum([2,7,11,15], 9))