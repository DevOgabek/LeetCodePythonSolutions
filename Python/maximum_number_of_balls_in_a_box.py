# Maximum Number of Balls in a Box

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        box_counts = {}
        
        for num in range(lowLimit, highLimit + 1):
            box_number = sum(int(digit) for digit in str(num))
            box_counts[box_number] = box_counts.get(box_number, 0) + 1
        
        max_balls = max(box_counts.values())
        
        return max_balls
    
solution = Solution()
print(solution.countBalls(1, 10))