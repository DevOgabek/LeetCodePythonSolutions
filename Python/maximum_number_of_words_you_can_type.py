# Maximum Number of Words You Can Type

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken_set = set(brokenLetters)
        words = text.split()
        fully_typed_count = 0
        
        for word in words:
            if any(letter in broken_set for letter in word):
                continue
            fully_typed_count += 1
            
        return fully_typed_count
    
solution = Solution()
print(solution.canBeTypedWords("hello world", "ad"))