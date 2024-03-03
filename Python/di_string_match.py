# DI String Match

class Solution(object):
    def diStringMatch(self, s):
        n = len(s)
        perm = list(range(n + 1))
        result = []

        for char in s:
            if char == 'I':
                result.append(perm.pop(0))
            elif char == 'D':
                result.append(perm.pop())

        result.append(perm[0])
        return result

solution = Solution()
print(solution.diStringMatch("IDID"))