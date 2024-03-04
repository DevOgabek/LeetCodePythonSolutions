# Counting Words With a Given Prefix

class Solution(object):
    def prefixCount(self, words, pref):
        n = len(pref)
        count = 0
        for i in range(len(words)):
            if words[i][:n] == pref:
                count += 1
        return count

solution = Solution()
print(solution.prefixCount(["pay","attention","practice","attend"], "at"))