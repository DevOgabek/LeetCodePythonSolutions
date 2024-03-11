# Majority Element

from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)
        
solution = Solution()
print(solution.majorityElement([3,2,3]))