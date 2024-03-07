# Split Strings by Separator

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        return [substring for word in words for substring in word.split(separator) if substring]

solution = Solution()
print(solution.splitWordsBySeparator(["$easy$","$problem$"], "$"))