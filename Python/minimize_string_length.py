# Minimize String Length

class Solution(object):
    def minimizedStringLength(self, s):
        return len(set(s))
    
solution = Solution()
print(solution.minimizedStringLength("aaabc"))