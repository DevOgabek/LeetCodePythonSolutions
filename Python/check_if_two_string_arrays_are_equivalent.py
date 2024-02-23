# Check If Two String Arrays are Equivalent

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)

test = Solution()
print(test.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))