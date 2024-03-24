# Longest Common Suffix Queries

class Node:
    def __init__(self):
        self.link = [None] * 26
        self.idx = -1
        self.end = -1
        self.min_len = 10**9

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s, i):
        s = s[::-1]
        ptr = self.root
        for ch in s:
            if not ptr.link[ord(ch) - ord('a')]:
                ptr.link[ord(ch) - ord('a')] = Node()
            if len(s) < ptr.min_len:
                ptr.idx = i
                ptr.min_len = len(s)
            ptr = ptr.link[ord(ch) - ord('a')]

        if ptr.end == -1:
            ptr.end = i

    def find(self, s):
        s = s[::-1]
        ptr = self.root
        for ch in s:
            if not ptr.link[ord(ch) - ord('a')]:
                if ptr.end != -1:
                    return ptr.end
                return ptr.idx
            ptr = ptr.link[ord(ch) - ord('a')]

        if ptr.end != -1:
            return ptr.end

        return ptr.idx

class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        t = Trie()
        for i in range(len(wordsContainer)):
            t.insert(wordsContainer[i], i)

        ans = [0] * len(wordsQuery)
        for i in range(len(ans)):
            ans[i] = t.find(wordsQuery[i])

        return ans
    
solution = Solution()

wordsContainer = ["apple", "banana", "app", "application", "bat", "ball"]

wordsQuery = ["app", "b", "ban", "apples"]

result = solution.stringIndices(wordsContainer, wordsQuery)

print("Indices of words in wordsContainer matching the prefixes in wordsQuery:")
for i in range(len(wordsQuery)):
    print(f"Query: {wordsQuery[i]}, Index: {result[i]}")