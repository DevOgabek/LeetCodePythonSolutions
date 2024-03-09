# Generate Parentheses

class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                result.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        result = []
        backtrack()
        return result

solution = Solution()
print(solution.generateParenthesis(3))