# Check if All Characters Have Equal Number of Occurrences

from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        counted_chars = Counter(s)
        main_count = counted_chars.most_common(1)[0][1]
        
        for count in counted_chars.values():
            if main_count != count:
                return False
        
        return True
    
solution = Solution()
print(solution.areOccurrencesEqual("abacbc"))