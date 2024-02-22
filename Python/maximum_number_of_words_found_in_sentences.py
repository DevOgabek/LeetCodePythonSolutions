# Maximum Number of Words Found in Sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        return max([sentence.count(' ') for sentence in sentences]) + 1

test = Solution()
print(test.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))