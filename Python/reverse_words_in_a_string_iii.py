# Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)
    
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))