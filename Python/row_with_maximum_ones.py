# Row With Maximum Ones

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        smaller_row_index = 0
        max_count = 0
        m = len(mat)
        
        for i in range(m):
            count = mat[i].count(1)
            if count > max_count:
                max_count = count
                smaller_row_index = i
                
        return [smaller_row_index, max_count]
    
solution = Solution()
print(solution.rowAndMaximumOnes([[0,1],[1,0]]))