# Widest Vertical Area Between Two Points Containing No Points

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda x: x[0])
        max_width = 0
        for i in range(1, len(points)):
            width = points[i][0] - points[i-1][0]
            max_width = max(max_width, width)
        return max_width

test = Solution()
print(test.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))