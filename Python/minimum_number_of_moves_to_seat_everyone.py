# Minimum Number of Moves to Seat Everyone

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        count = 0
        for seat, student, in zip(seats, students):
            count += abs(seat - student)
        return count

solution = Solution()
print(solution.minMovesToSeat([3,1,5], [2,7,4]))