# Cells with Odd Values in a Matrix

class Solution(object):
    def oddCells(self, m, n, indices):
        matrix = [[0] * n for _ in range(m)]

        for ri, ci in indices:
            for j in range(n):
                matrix[ri][j] += 1
            for i in range(m):
                matrix[i][ci] += 1
        
        odd_count = sum(cell % 2 != 0 for row in matrix for cell in row)
        return odd_count

solution = Solution()
print(solution.oddCells(2, 3, [[0,1],[1,1]]))