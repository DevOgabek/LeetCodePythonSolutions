# Count Prefixes of a Given String

class Solution(object):
    def countPrefixes(self, words, s):
        count = 0

        for word in words:
            if word == s[:len(word)]:
                count += 1

        return count
    
solution = Solution()
print(solution.countPrefixes(["a","b","c","ab","bc","abc"], "abc"))