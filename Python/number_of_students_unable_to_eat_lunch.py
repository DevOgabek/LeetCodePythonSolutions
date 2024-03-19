# Number of Students Unable to Eat Lunch

class Solution(object):
    def countStudents(self, students, sandwiches):
        temp = 0
        while True:
            if not students or temp == len(students):
                break
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                temp = 0
            else:
                temp += 1
                students.append(students[0])
                del students[0]
        
        return len(students)
    
solution = Solution()
print(solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))