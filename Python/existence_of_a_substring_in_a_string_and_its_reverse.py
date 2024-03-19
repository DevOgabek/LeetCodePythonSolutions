# Existence of a Substring in a String and Its Reverse

class Solution(object):
    def isSubstringPresent(self, s):
        for i in range(len(s) - 1):
            if s[i:i+2] in s[::-1]:
                return True
            
        return False
    
solution = Solution()
print(solution.isSubstringPresent("leetcode"))