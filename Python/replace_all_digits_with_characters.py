# Replace All Digits with Characters

class Solution(object):
    def replaceDigits(self, s):
        for i in range(1,len(s),2):
            s = s[:i] + chr(ord(s[i-1])+int(s[i])) + s[i+1:]
        return s

solution = Solution()
print(solution.replaceDigits("a1c1e1"))