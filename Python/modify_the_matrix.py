# Modify the Matrix

class Solution(object):
    def modifiedMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        max_values = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_values[j]
                    
        return matrix
    
solution = Solution()
print(solution.modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))