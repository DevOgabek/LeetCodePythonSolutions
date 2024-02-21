# Number of Employees Who Met the Target

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return len([None for hour in hours if hour >= target])

test = Solution()
print(test.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))