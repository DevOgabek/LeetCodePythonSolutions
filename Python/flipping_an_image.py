# Flipping an Image

class Solution(object):
    def flipAndInvertImage(self, image):
        return [[1 ^ pixel for pixel in row[::-1]] for row in image]

solution = Solution()
print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))