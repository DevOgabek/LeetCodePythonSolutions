# Split a String in Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        count_L, count_R, max_splits = 0, 0, 0
        
        for char in s:
            if char == 'L':
                count_L += 1
            elif char == 'R':
                count_R += 1
            
            if count_L == count_R:
                max_splits += 1
        
        return max_splits

solution = Solution()
print(solution.balancedStringSplit("RLRRLLRLRL"))