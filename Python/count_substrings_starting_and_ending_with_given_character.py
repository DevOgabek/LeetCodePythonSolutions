# Count Substrings Starting and Ending with Given Character

class Solution(object):
    def countSubstrings(self, s, c):
        count = s.count(c)
        return count * (count + 1) // 2
    
solution = Solution()
print(solution.countSubstrings())