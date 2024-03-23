# Lexicographically Smallest Palindrome

class Solution(object):
    def makeSmallestPalindrome(self, s):
        return ''.join(map(min, zip(s, s[::-1])))
    
solution = Solution()
print(solution.makeSmallestPalindrome("egcfe"))