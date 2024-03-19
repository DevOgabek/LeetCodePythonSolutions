# First Letter to Appear Twice

class Solution(object):
    def repeatedCharacter(self, s):
        hash_set = set()
        
        for char in s:
            if char in hash_set:
                return char
            hash_set.add(char)

        return char
     
solution = Solution()
print(solution.repeatedCharacter("abccbaacz"))