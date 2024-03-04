# Unique Number of Occurrences

class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}
        
        for num in arr:
            count[num] = count.get(num, 0) + 1
            
        return len(count.values()) == len(set(count.values()))

solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))