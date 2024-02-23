# Find First Palindromic String in the Array

class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word[::-1] == word:
                return word
        return ''

test = Solution()
print(test.firstPalindrome(["abc","car","ada","racecar","cool"]))