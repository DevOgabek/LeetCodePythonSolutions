# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

test = Solution()
print(test.isPalindrome(121))