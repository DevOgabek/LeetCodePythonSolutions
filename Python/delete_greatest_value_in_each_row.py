# Delete Greatest Value in Each Row

class Solution(object):
    def deleteGreatestValue(self, grid):
        cound = 0
        n = len(grid)
        if n > 1:
            for i in range(len(grid[0])):
                new_list = []
                for j in range(n):
                    a = sorted(grid[j])
                    new_list.append(a[i])
                cound+=max(new_list)
            return cound
        else: 
            return sum(grid[0])

solution = Solution()
print(solution.deleteGreatestValue([[1,2,4],[3,3,1]]))