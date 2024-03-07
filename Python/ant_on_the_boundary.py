# Ant on the Boundary

class Solution(object):
    def returnToBoundaryCount(self, nums):
        position = 0
        boundary_count = 0

        for step in nums:
            position += step

            if position == 0:
                boundary_count += 1

        return boundary_count

solution = Solution()
print(solution.returnToBoundaryCount([2,3,-5]))