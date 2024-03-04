# Remove Palindromic Subsequences

class Solution(object):
    def removePalindromeSub(self, s):
        return 1 if s == s[::-1] else 2

solution = Solution()
print(solution.build_array())