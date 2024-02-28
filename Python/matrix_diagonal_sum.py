# Matrix Diagonal Sum

class Solution(object):
    def diagonalSum(self, mat):
        count = 0
        n = len(mat)
        for i in range(n):
            count += mat[i][i] + mat[i][-(i+1)]
        if n % 2 == 0:
            return count
        return count - mat[n // 2][n // 2]

test = Solution()
print(test.diagonalSum([[1,2,3],
                        [4,5,6],
                        [7,8,9]]))