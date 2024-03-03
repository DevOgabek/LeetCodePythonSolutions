# Find Maximum Number of String Pairs

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if words[i][::-1] == words[j]:
                    count += 1
        return count

solution = Solution()
print(solution.build_array())