# Maximum Number of Pairs in Array

from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums):
        nums_counts = Counter(nums)
        leftover_count = 0
        formed_count = 0
        
        for count in nums_counts.values():
            if count % 2 != 0:
                leftover_count += 1
            formed_count += count // 2
        return [formed_count, leftover_count]
    
solution = Solution()
print(solution.numberOfPairs([1,3,2,1,3,2,2]))