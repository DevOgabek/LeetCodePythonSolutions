# Split Strings by Separator

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        return [char for word in words for char in word.split(separator) if char]
    
solution = Solution()
print(solution.splitWordsBySeparator(["one.two.three","four.five","six"], '.'))