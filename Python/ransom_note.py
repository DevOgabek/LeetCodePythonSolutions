# Ransom Note

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s1, s2 = Counter(ransomNote), Counter(magazine)
        return True if s1 & s2 == s1 else False
        
solution = Solution()
print(solution.canConstruct("a", "b"))