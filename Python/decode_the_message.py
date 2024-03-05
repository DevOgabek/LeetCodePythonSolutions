# Decode the Message

class Solution(object):
    def decodeMessage(self, key, message):
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        for char in message:
            res += mapping[char]
                
        return res
    
solution = Solution()
print(solution.decodeMessage("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps over the lazy dog"))