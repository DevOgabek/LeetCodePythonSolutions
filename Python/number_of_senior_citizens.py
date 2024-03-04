# Number of Senior Citizens

class Solution(object):
    def countSeniors(self, details):
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1
        return count

solution = Solution()
print(solution.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))