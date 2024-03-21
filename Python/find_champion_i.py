# Find Champion I

class Solution(object):
    def findChampion(self, grid):
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n - 1:
                return i
    
solution = Solution()
print(solution.findChampion([[0,1],[0,0]]))