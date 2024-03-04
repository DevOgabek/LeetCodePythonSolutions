# Goal Parser Interpretation

class Solution(object):
    def interpret(self, command):
        return command.replace('()', 'o').replace('(', '').replace(')', '')

solution = Solution()
print(solution.interpret("G()(al)"))