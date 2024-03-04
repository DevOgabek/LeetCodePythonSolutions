# Largest Local Values in a Matrix

class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        max_local = []
        
        for i in range(n - 2):
            row_max = []
            for j in range(n - 2):
                submatrix_max = max(
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2],

                )
                row_max.append(submatrix_max)
            max_local.append(row_max)
        
        return max_local

test = Solution()
print(test.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))