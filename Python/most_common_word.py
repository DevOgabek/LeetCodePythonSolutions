# Most Common Word

from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        symbols = "!?',;." 
        for s in symbols:
            paragraph = paragraph.replace(s," ")
            
        paraList = paragraph.lower().split()
        wordCounter = Counter(paraList)
        
        for banned_word in banned:
            del wordCounter[banned_word]
        
        most_frequent = wordCounter.most_common(1)

        return most_frequent[0][0]
    
solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))