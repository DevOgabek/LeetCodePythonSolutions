# Kth Distinct String in an Array

class Solution:
    def kthDistinct(self, arr, k):
        count = {}
        
        for string in arr:
            count[string] = count.get(string, 0) + 1
        
        distinct_strings = [string for string, freq in count.items() if freq == 1]

        if len(distinct_strings) < k:
            return ""
            
        return distinct_strings[k - 1]
    
solution = Solution()
print(solution.kthDistinct(["d","b","c","b","c","a"], 2))