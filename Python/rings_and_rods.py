# Rings and Rods

class Solution(object):
    def countPoints(self, rings):
        rods = {str(i) : set() for i in range(10)}
        
        for i in range(0, len(rings), 2):
            color, rod = rings[i], rings[i + 1]
            rods[rod].add(color)
        
        count = 0
        for rod_colors in rods.values():
            if len(rod_colors) == 3:
                count += 1
                
        return count
    
solution = Solution()
print(solution.countPoints("B0B6G0R6R0R6G9"))