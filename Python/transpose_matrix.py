# Transpose Matrix

class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        transpose_matrix = [[0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transpose_matrix[j][i] = matrix[i][j]
        
        return transpose_matrix
                
solution = Solution()
print(solution.transpose([[1,2,3],[4,5,6],[7,8,9]]))