# Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s
        
        start = 0
        max_len = 1
        
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_len = 2
                
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
                    start = i
                    max_len = length
                    
        return s[start:start + max_len]
    
solution = Solution()
print(solution.longestPalindrome("babad"))