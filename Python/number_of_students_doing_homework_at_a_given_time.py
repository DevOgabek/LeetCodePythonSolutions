# Number of Students Doing Homework at a Given Time

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for start, end, in zip(startTime, endTime):
            if start <= queryTime and end >= queryTime:
                count += 1
        return count

solution = Solution()
print(solution.busyStudent([1,2,3], [3,2,7], 4))