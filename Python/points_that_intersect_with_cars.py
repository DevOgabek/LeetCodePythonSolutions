# Points That Intersect With Cars

class Solution(object):
    def numberOfPoints(self, nums):
        covered_points = set()
        
        for start, end in nums:
            for point in range(start, end + 1):
                covered_points.add(point)
        
        return len(covered_points)

solution = Solution()
print(solution.numberOfPoints([[3,6],[1,5],[4,7]]))