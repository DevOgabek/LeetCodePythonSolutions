# Baseball Game

class Solution(object):
    def calPoints(self, operations):
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                record.append(record[-1] + record[-2])
            elif operations[i] == 'D':
                record.append(record[-1] * 2)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))