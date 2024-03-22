# Top K Frequent Elements

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]
    
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))