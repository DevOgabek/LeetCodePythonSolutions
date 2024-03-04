# Count Negative Numbers in a Sorted Matrix

class Solution(object):
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0
        row, col = m - 1, 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += n - col
                row -= 1
            else:
                col += 1

        return count

solution = Solution()
print(solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))